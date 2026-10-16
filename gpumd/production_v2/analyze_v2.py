#!/usr/bin/env python3
"""Analyse the v2 GPUMD endpoint campaign exactly as pre-registered in
endpoint_v2_design.json. Reads only stages committed to the ledger, only
from the committed copies under raw/. Writes analysis_v2.json with
per-run gates R1-R4, per-point estimates (SE floored at the pooled
within-run SEM), per-state estimates, P1/P2, the per-temperature restore
verdicts with scope labels, prediction checks, and GPU/attempt records.

Usage: python3 analyze_v2.py
"""
import json
import math
import os
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "production"))
from analyze_campaign import run_stats, within, BTE  # noqa: E402

MT = os.path.abspath(os.path.join(HERE, "..", ".."))
LEDGER = os.path.join(MT, "phase_c", "ledger_campaign.jsonl")
CAMPAIGN = "gpumd-endpoint-v2-2026-09-29"


def committed_stages():
    out = set()
    for l in open(LEDGER):
        e = json.loads(l)
        if e["kind"] == "batch_result" and e["payload"].get("campaign") == CAMPAIGN:
            out.add(e["payload"]["stage"])
    return out


def point_est(runs, min_pass):
    ok = [r for r in runs if r["pass"]]
    if len(ok) < min_pass:
        return None
    v = [r["kappa"] for r in ok]
    n = len(v)
    seed_se = st.stdev(v) / math.sqrt(n)
    floor = math.sqrt(sum(r["sem"] ** 2 for r in ok)) / n
    return {"kappa": round(st.mean(v), 3), "se": round(max(seed_se, floor), 3),
            "seed_se": round(seed_se, 3), "sem_floor": round(floor, 3), "n": n}


def readf(d, f):
    p = os.path.join(d, f)
    return open(p).read().strip() if os.path.exists(p) else None


def main():
    design = json.load(open(os.path.join(HERE, "endpoint_v2_design.json")))
    stages = committed_stages()
    runs = {}
    for r in design["runs"]:
        if r["stage"] in stages:
            d = os.path.join(HERE, "raw", r["run_id"])
            runs[r["run_id"]] = dict(r, **run_stats(d, r),
                                     gpu=readf(d, "gpu_model"),
                                     attempts=len((readf(d, "attempts") or "").splitlines()))
    groups = {}
    for r in runs.values():
        groups.setdefault((r["system"], r["T_K"], r["Fe_per_A"], tuple(r["cells"])), []).append(r)
    points = {}
    for (s, T, fe, c), rs in groups.items():
        points[f"{s}|{T}|{fe:g}|{'x'.join(map(str, c))}"] = {
            "system": s, "T": T, "Fe": fe, "cells": list(c), "n_runs": len(rs),
            "n_pass": sum(r["pass"] for r in rs),
            "estimate": point_est(rs, 2 if list(c) == [16, 8, 8] else 3)}
    states, gates = {}, {}
    for s in ("Si", "Ge"):
        for T in (300, 700, 1100):
            ps = sorted([p for p in points.values() if p["system"] == s and p["T"] == T
                         and p["cells"] == [8, 8, 8]], key=lambda p: p["Fe"])
            if len(ps) < 2:
                continue
            lo, hi = ps[0]["estimate"], ps[1]["estimate"]
            if lo is None or hi is None:
                gates[f"P1_linearity|{s}|{T}"] = False
                continue
            gates[f"P1_linearity|{s}|{T}"] = within(lo["kappa"], hi["kappa"], lo["se"], hi["se"])
            k = 0.5 * (lo["kappa"] + hi["kappa"])
            se = 0.5 * math.sqrt(lo["se"] ** 2 + hi["se"] ** 2)
            states[f"{s}|{T}"] = {"kappa": round(k, 2), "se": round(se, 2),
                                  "bte_dft": BTE[(s, T)],
                                  "ratio_to_bte": round(k / BTE[(s, T)], 3)}
    big, small = points.get("Si|300|1e-05|16x8x8"), points.get("Si|300|1e-05|8x8x8")
    if big and small and big["estimate"] and small["estimate"]:
        gates["P2_size"] = within(big["estimate"]["kappa"], small["estimate"]["kappa"],
                                  big["estimate"]["se"], small["estimate"]["se"])
    restore = {}
    for T in (300, 700, 1100):
        pts = [p for p in points.values() if p["T"] == T and p["cells"] == [8, 8, 8]]
        runs_ok = len(pts) == 4 and all(p["estimate"] is not None for p in pts)
        cond = runs_ok and bool(gates.get(f"P1_linearity|Si|{T}")) and \
            bool(gates.get(f"P1_linearity|Ge|{T}"))
        if T == 300:
            cond = cond and bool(gates.get("P2_size"))
        restore[str(T)] = {"points_ok": runs_ok,
                           "P1_Si": gates.get(f"P1_linearity|Si|{T}"),
                           "P1_Ge": gates.get(f"P1_linearity|Ge|{T}"),
                           "P2_size": gates.get("P2_size") if T == 300 else "n/a",
                           "restored": cond,
                           "scope_label": ({"parentage": "Tersoff-1989",
                                            "ratio_to_bte_Si": states.get(f"Si|{T}", {}).get("ratio_to_bte"),
                                            "ratio_to_bte_Ge": states.get(f"Ge|{T}", {}).get("ratio_to_bte")}
                                           if cond else None)}
    pred = {}
    if "Si|300" in states and "Ge|300" in states:
        pred["P1_passes_300_both"] = bool(gates.get("P1_linearity|Si|300") and gates.get("P1_linearity|Ge|300"))
        p = points.get("Si|300|1e-05|8x8x8")
        if p and p["estimate"]:
            pred["kSi300_fe1e-5_within_20pct_of_284"] = abs(p["estimate"]["kappa"] / 284 - 1) <= 0.2
        pred["ratio300_in_1.4_2.2_both"] = all(1.4 <= states[f"{s}|300"]["ratio_to_bte"] <= 2.2 for s in ("Si", "Ge"))
    if "Si|1100" in states and "Ge|1100" in states:
        pred["agree_bte_30pct_1100_both"] = all(abs(states[f"{s}|1100"]["ratio_to_bte"] - 1) <= 0.3 for s in ("Si", "Ge"))
    for s in ("Si", "Ge"):
        if all(f"{s}|{T}" in states for T in (300, 700, 1100)):
            k = [states[f"{s}|{T}"]["kappa"] for T in (300, 700, 1100)]
            pred[f"{s}_monotone_in_T"] = k[0] > k[1] > k[2]
    out = {"committed_stages": sorted(stages), "runs": runs, "points": points,
           "states": states, "gates": gates, "restore": restore, "predictions": pred,
           "gpus": sorted({r["gpu"] or "?" for r in runs.values()}),
           "total_attempts": sum(r["attempts"] for r in runs.values())}
    json.dump(out, open(os.path.join(HERE, "analysis_v2.json"), "w"), indent=1, sort_keys=True)
    print(json.dumps({k: out[k] for k in ("committed_stages", "states", "gates", "restore",
                                          "predictions", "gpus", "total_attempts")}, indent=1))


if __name__ == "__main__":
    main()
