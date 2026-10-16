#!/usr/bin/env python3
"""Analyse the GPUMD endpoint campaign exactly as pre-registered in
endpoint_campaign_design.json (analysis + acceptance blocks). Only
stages already committed to the ledger (commit_stage.py) are read, and
only from the committed copies under raw/. Writes analysis_results.json
with per-run gates R1-R4, per-point estimates, per-state estimates,
point gates P1-P3, the restore verdict, and the prediction checks.

Usage: python3 analyze_campaign.py
"""
import json
import math
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MT = os.path.abspath(os.path.join(HERE, "..", ".."))
LEDGER = os.path.join(MT, "phase_c", "ledger_campaign.jsonl")
RNEMD_X05_300 = 1.80
RNEMD_SE = 0.10
BTE = {("Si", 300): 160.5, ("Si", 700): 63.8, ("Si", 1100): 40.5,
       ("Ge", 300): 57.1, ("Ge", 700): 25.7, ("Ge", 1100): 16.7}


def run_stats(d, row):
    rows = [[float(v) for v in l.split()] for l in open(os.path.join(d, "kappa.out"))
            if l.strip()]
    expected = int(row["production_ns"] * 1e6) // 1000
    kx = [r[0] + r[1] for r in rows]
    kx = kx[int(len(kx) * 0.2):]
    nb = 10
    n = len(kx) // nb * nb
    m = n // nb
    means = [sum(kx[i:i + m]) / m for i in range(0, n, m)]
    mu = sum(means) / nb
    sem = st.stdev(means) / math.sqrt(nb)
    q = len(kx) // 5
    drift_z = ((sum(kx[-q:]) / q - sum(kx[:q]) / q) / (sem * math.sqrt(2))
               if sem > 0 else 0.0)
    Ts = [float(l.split()[0]) for l in open(os.path.join(d, "thermo.out"))
          if l.strip() and not l.startswith("#")]
    Tm = sum(Ts) / len(Ts)
    ex = int(open(os.path.join(d, "exit_status")).read().strip())
    gates = {"R1_exit": ex == 0 and len(rows) >= 0.9 * expected,
             "R2_temperature": abs(Tm - row["T_K"]) <= 0.02 * row["T_K"],
             "R3_no_runaway": drift_z < 3,
             "R4_physical": 0 < mu < 2000}
    return {"kappa": round(mu, 4), "sem": round(sem, 4),
            "drift_z": round(drift_z, 2), "mean_T": round(Tm, 1),
            "lines": len(rows), "gates": gates, "pass": all(gates.values())}


def committed_stages():
    out = set()
    for l in open(LEDGER):
        e = json.loads(l)
        if e["kind"] == "batch_result" and e["payload"].get("campaign", "") \
                .startswith("gpumd-endpoint-production"):
            out.add(e["payload"]["stage"])
    return out


def point_est(vals):
    if len(vals) < 2:
        return None
    return {"kappa": round(st.mean(vals), 3),
            "se": round(st.stdev(vals) / math.sqrt(len(vals)), 3),
            "n": len(vals)}


def within(a, b, sa, sb):
    return abs(a - b) <= 2 * math.sqrt(sa ** 2 + sb ** 2)


def main():
    design = json.load(open(os.path.join(HERE, "endpoint_campaign_design.json")))
    stages = committed_stages()
    runs = {}
    for r in design["runs"]:
        if r["stage"] in stages:
            runs[r["run_id"]] = dict(r, **run_stats(
                os.path.join(HERE, "raw", r["run_id"]), r))
    # points (system, T, Fe, cells)
    pts = {}
    for r in runs.values():
        key = (r["system"], r["T_K"], r["Fe_per_A"], tuple(r["cells"]))
        pts.setdefault(key, []).append(r)
    points = {}
    for (s, T, fe, c), rs in pts.items():
        ok = [x["kappa"] for x in rs if x["pass"]]
        points[f"{s}|{T}|{fe:g}|{'x'.join(map(str, c))}"] = {
            "system": s, "T": T, "Fe": fe, "cells": list(c),
            "n_runs": len(rs), "n_pass": len(ok),
            "estimate": point_est(ok)}
    # states and gates
    states, gates = {}, {}
    for s in ("Si", "Ge"):
        for T in (300, 700, 1100):
            ps = [p for p in points.values() if p["system"] == s and p["T"] == T
                  and p["cells"] == [8, 8, 8]]
            if len(ps) < 2:
                continue
            ps.sort(key=lambda p: p["Fe"])
            lo, hi = ps[0]["estimate"], ps[1]["estimate"]
            if lo is None or hi is None:
                gates[f"P1_linearity|{s}|{T}"] = False
                continue
            gates[f"P1_linearity|{s}|{T}"] = within(lo["kappa"], hi["kappa"],
                                                    lo["se"], hi["se"])
            k = 0.5 * (lo["kappa"] + hi["kappa"])
            se = 0.5 * math.sqrt(lo["se"] ** 2 + hi["se"] ** 2)
            states[f"{s}|{T}"] = {"kappa": round(k, 2), "se": round(se, 2),
                                  "bte_dft": BTE[(s, T)]}
    big = points.get("Si|300|1e-05|16x8x8")
    small = points.get("Si|300|1e-05|8x8x8")
    if big and small and big["estimate"] and small["estimate"]:
        gates["P2_size"] = within(big["estimate"]["kappa"],
                                  small["estimate"]["kappa"],
                                  big["estimate"]["se"], small["estimate"]["se"])
    al = points.get("SiGe|300|0.0002|8x8x8")
    if al and al["estimate"]:
        gates["P3_alloy_crosscheck"] = within(al["estimate"]["kappa"],
                                              RNEMD_X05_300,
                                              al["estimate"]["se"], RNEMD_SE)
    # restore verdict
    s1 = [p for p in points.values() if p["T"] == 300 and p["system"] != "SiGe"
          and p["cells"] == [8, 8, 8]]
    s1_ok = len(s1) == 4 and all(p["n_pass"] >= 2 for p in s1)
    restore = {"S1_runs_ok": s1_ok,
               "P1_Si_300": gates.get("P1_linearity|Si|300"),
               "P1_Ge_300": gates.get("P1_linearity|Ge|300"),
               "P2_size": gates.get("P2_size")}
    restore["condition_met"] = bool(s1_ok and restore["P1_Si_300"] and
                                    restore["P1_Ge_300"] and restore["P2_size"])
    restore["T_added"] = [T for T in (700, 1100)
                          if gates.get(f"P1_linearity|Si|{T}")
                          and gates.get(f"P1_linearity|Ge|{T}")]
    # predictions (reported, not gating)
    pred = {}
    if "Si|300" in states and "Ge|300" in states:
        pred["kSi300_gt_kGe300"] = states["Si|300"]["kappa"] > states["Ge|300"]["kappa"]
        pred["kSi300_in_150_300"] = 150 <= states["Si|300"]["kappa"] <= 300
    for s in ("Si", "Ge"):
        if all(f"{s}|{T}" in states for T in (300, 700, 1100)):
            k = [states[f"{s}|{T}"]["kappa"] for T in (300, 700, 1100)]
            pred[f"{s}_monotone_in_T"] = k[0] > k[1] > k[2]
            pred[f"{s}_ratio_300_1100_in_2.5_4.5"] = 2.5 <= k[0] / k[2] <= 4.5
    for key, v in states.items():
        pred[f"{key}_agrees_BTE"] = abs(v["kappa"] - v["bte_dft"]) <= \
            2 * v["se"] + 0.3 * v["bte_dft"]
    out = {"committed_stages": sorted(stages), "runs": runs, "points": points,
           "states": states, "gates": gates, "restore": restore,
           "predictions": pred}
    json.dump(out, open(os.path.join(HERE, "analysis_results.json"), "w"),
              indent=1, sort_keys=True)
    print(json.dumps({k: out[k] for k in ("committed_stages", "states",
                                          "gates", "restore", "predictions")},
                     indent=1))


if __name__ == "__main__":
    sys.exit(main())
