#!/usr/bin/env python3
"""Materialize the committed v2 endpoint design into GPUMD run
directories plus one SLURM array script per stage (CHPC guest GPUs).
Refuses unless the design's SHA-256 equals PREREGISTERED_SHA256 (written
by preregister_v2.py and pushed to git before any run exists).

Usage:
  python3 make_runs_v2.py --out DIR      (then rsync DIR to CHPC_ROOT/runs)
  python3 make_runs_v2.py --smoke DIR    (protocol smoke: one run per
      (system, cells), all lengths / 1000; no hash check; never pooled)
"""
import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "production"))
from make_runs import build  # noqa: E402  (same run.in + model builder as v1)

DESIGN = os.path.join(HERE, "endpoint_v2_design.json")
PREREG = os.path.join(HERE, "PREREGISTERED_SHA256")
CHPC_ROOT = "/uufs/chpc.utah.edu/common/home/u1496771/mat_theory/gpumd_v2"

# stage -> (cluster, partition, account, qos-or-empty, time limit, gres)
# Placement is execution detail, not design (the design allows any guest
# GPU). 2026-09-29: the first submission landed on notchpeak RTX 2080 Ti
# nodes where 11 of 20 tasks failed CUDA initialization before producing
# output (ledger deviation seq 31), so GPU models are now pinned per stage
# and a CUDA-init guard keeps such failures from writing an exit status.
# V1 was first pinned to a100, but those nodes stayed unavailable
# (ReqNodeNotAvail); it was moved to a6000 before any V1 task started.
PLACEMENT = {
    "V1-anchor-300K": ("notchpeak", "notchpeak-gpu-guest", "owner-gpu-guest", "", "08:00:00", "gpu:a6000:1"),
    "V2-size-check": ("notchpeak", "notchpeak-gpu-guest", "owner-gpu-guest", "", "12:00:00", "gpu:a6000:1"),
    "V3-highT": ("granite", "granite-gpu-guest", "sparks", "granite-gpu-guest", "06:00:00", "gpu:h200:1"),
}

ARRAY = """#!/bin/bash
#SBATCH -J v2_{short}
#SBATCH -M {cluster}
#SBATCH -p {partition}
#SBATCH -A {account}
{qos}#SBATCH -N 1 -n 1 -c 2
#SBATCH --gres={gres}
#SBATCH -t {time}
#SBATCH --requeue
#SBATCH --array=0-{last}
#SBATCH -o {root}/logs/{stage}_%A_%a.txt
# Pre-registered v2 endpoint campaign, stage {stage}. One run per task.
# Preemption -> requeue -> the run restarts from scratch with the same seed
# (declared protocol). grn061 / sparks-gpu-grn are never used.
module purge; module load cuda/12.8.1
NAMES=({names})
name=${{NAMES[$SLURM_ARRAY_TASK_ID]}}
d={root}/runs/$name
cd "$d" || exit 1
if [ -f exit_status ] && [ "$(cat exit_status)" = "0" ]; then exit 0; fi
echo "$(date -u +%FT%TZ) job=$SLURM_JOB_ID restart=${{SLURM_RESTART_COUNT:-0}} host=$(hostname)" >> attempts
if ! nvidia-smi --query-gpu=name,driver_version --format=csv,noheader > gpu_model 2>&1 \
   || grep -q "No devices" gpu_model; then
  echo "  cuda_init_fail (nvidia-smi) host=$(hostname)" >> attempts; rm -f exit_status; exit 3
fi
rm -f kappa.out thermo.out exit_status
date -u +%FT%TZ > started
{root}/GPUMD/src/gpumd > run.log 2>&1
ex=$?
if [ $ex -ne 0 ] && [ ! -s kappa.out ] && grep -q "CUDA Error" run.log; then
  echo "  cuda_init_fail (gpumd, exit $ex) host=$(hostname)" >> attempts; exit 3
fi
echo $ex > exit_status
date -u +%FT%TZ > finished
sha256sum kappa.out thermo.out run.log run.in model.xyz gpu_model > sha256sums 2>/dev/null
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--smoke")
    a = ap.parse_args()
    blob = open(DESIGN, "rb").read()
    design = json.loads(blob)
    runs = design["runs"]
    if a.smoke:
        seen, pick = set(), []
        for r in runs:
            k = (r["system"], tuple(r["cells"]))
            if k not in seen:
                seen.add(k)
                pick.append(r)
        build(a.smoke, pick, scale=1000)
        print("smoke:", [r["run_id"] for r in pick])
        return
    want = open(PREREG).read().split()[0]
    got = hashlib.sha256(blob).hexdigest()
    if got != want:
        sys.exit(f"REFUSING: design sha256 {got} != pre-registered {want}")
    build(os.path.join(a.out, "runs"), runs)
    for stage in design["protocol"]["stage_order"]:
        names = [r["run_id"] for r in runs if r["stage"] == stage]
        cl, part, acct, qos, t, gres = PLACEMENT[stage]
        s = ARRAY.format(short=stage.split("-")[0], cluster=cl, partition=part,
                         account=acct, qos=f"#SBATCH --qos={qos}\n" if qos else "",
                         time=t, gres=gres, last=len(names) - 1, root=CHPC_ROOT,
                         stage=stage, names=" ".join(names))
        open(os.path.join(a.out, f"array_{stage}.sbatch"), "w").write(s)
    open(os.path.join(a.out, "PREREGISTERED_SHA256"), "w").write(want + "\n")
    print(f"{len(runs)} runs + {len(PLACEMENT)} array scripts in {a.out}")


if __name__ == "__main__":
    main()
