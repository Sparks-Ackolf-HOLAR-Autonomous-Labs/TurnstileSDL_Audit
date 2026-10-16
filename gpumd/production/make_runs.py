#!/usr/bin/env python3
"""Materialize the committed endpoint-campaign design into GPUMD run
directories plus a serial driver script. Refuses to run unless the
design file's SHA-256 equals the pre-registered hash in
`PREREGISTERED_SHA256` (written by preregister.py and committed to git
before any run exists), so the runs executed are provably the runs
committed.

Usage:
  python3 make_runs.py [--root ~/mat_theory_gpumd/production]
  python3 make_runs.py --smoke DIR   (protocol smoke test: first run of
      each system with every run length divided by 1000; no hash check,
      output is not campaign data and is never pooled)
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DESIGN = os.path.join(HERE, "endpoint_campaign_design.json")
PREREG = os.path.join(HERE, "PREREGISTERED_SHA256")
MAKE_MODEL = os.path.join(HERE, "..", "make_model.py")


def run_in(r, scale=1):
    T, fe = r["T_K"], r["Fe_per_A"]
    npt = max(100000 // scale, 100)
    nvt = max(50000 // scale, 100)
    prod = max(int(r["production_ns"] * 1e6) // scale, 1000)
    return (f"potential   {r['potential']}\n"
            f"velocity    {T} seed {r['seed']}\n"
            f"time_step   1\n"
            f"ensemble    npt_ber {T} {T} 100 0 100 1000\n"
            f"run         {npt}\n"
            f"ensemble    nvt_nhc {T} {T} 100\n"
            f"run         {nvt}\n"
            f"ensemble    nvt_nhc {T} {T} 100\n"
            f"compute_hnemd 1000 {fe:g} 0 0\n"
            f"dump_thermo 10000\n"
            f"run         {prod}\n")


def build(root, runs, scale=1):
    os.makedirs(root, exist_ok=True)
    for r in runs:
        d = os.path.join(root, r["run_id"])
        os.makedirs(d, exist_ok=True)
        nx, ny, nz = r["cells"]
        if r["system"] == "SiGe":
            args = [str(nx), str(ny), str(nz), str(r["a0_A"]), "Si",
                    os.path.join(d, "model.xyz"), str(r["x_ge"]),
                    str(r["config_seed"])]
        else:
            args = [str(nx), str(ny), str(nz), str(r["a0_A"]), r["system"],
                    os.path.join(d, "model.xyz")]
        subprocess.run([sys.executable, MAKE_MODEL] + args, check=True,
                       stdout=subprocess.DEVNULL)
        with open(os.path.join(d, "run.in"), "w") as f:
            f.write(run_in(r, scale))
        with open(os.path.join(d, "design_row.json"), "w") as f:
            json.dump(r, f, indent=1, sort_keys=True)


DRIVER = """#!/bin/bash
# Serial driver for the pre-registered GPUMD endpoint campaign.
# Launch detached with:  RUNNER_TRACKING_ID= setsid nohup bash driver.sh > driver.log 2>&1 &
ROOT={root}
GPUMD=/home/sparksspark/mat_theory_gpumd/GPUMD/src/gpumd
cd "$ROOT"
for name in {names}; do
  if [ -f "$name/exit_status" ]; then continue; fi
  cd "$name"
  date -u +%FT%TZ > started
  "$GPUMD" > run.log 2>&1
  echo $? > exit_status
  date -u +%FT%TZ > finished
  sha256sum kappa.out thermo.out run.log run.in model.xyz > sha256sums 2>/dev/null
  cd "$ROOT"
done
date -u +%FT%TZ > "$ROOT/campaign_done"
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.expanduser(
        "~/mat_theory_gpumd/production"))
    ap.add_argument("--smoke")
    a = ap.parse_args()
    blob = open(DESIGN, "rb").read()
    design = json.loads(blob)
    order = design["protocol"]["stage_order"]
    runs = sorted(design["runs"],
                  key=lambda r: (order.index(r["stage"]), r["seed"]))
    if a.smoke:
        seen, pick = set(), []
        for r in runs:
            key = (r["system"], tuple(r["cells"]))
            if key not in seen:
                seen.add(key)
                pick.append(r)
        build(a.smoke, pick, scale=1000)
        print(f"smoke dirs: {[r['run_id'] for r in pick]} in {a.smoke}")
        return
    want = open(PREREG).read().split()[0]
    got = hashlib.sha256(blob).hexdigest()
    if got != want:
        sys.exit(f"REFUSING: design sha256 {got} != pre-registered {want}")
    build(a.root, runs)
    with open(os.path.join(a.root, "driver.sh"), "w") as f:
        f.write(DRIVER.format(root=a.root,
                              names=" ".join(r["run_id"] for r in runs)))
    with open(os.path.join(a.root, "PREREGISTERED_SHA256"), "w") as f:
        f.write(want + "\n")
    print(f"{len(runs)} run dirs + driver.sh in {a.root} (design {want})")


if __name__ == "__main__":
    main()
