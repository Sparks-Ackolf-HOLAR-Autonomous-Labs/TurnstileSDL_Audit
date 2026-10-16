#!/usr/bin/env python3
"""Figure for paper 2: pure Si and Ge kappa(T) from the pre-registered
GPUMD HNEMD endpoint campaign (both driving forces, per-seed runs and
point estimates), against the BTE-DFT party and the DB-CITRINE
experimental pure-Si rows. Reads analysis_results.json only.
Usage: python3 make_endpoint_figure.py <out.png>
"""
import json
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
MT = os.path.abspath(os.path.join(HERE, "..", ".."))
res = json.load(open(os.path.join(HERE, "analysis_results.json")))
BTE = {"Si": {300: 160.5, 700: 63.8, 1100: 40.5},
       "Ge": {300: 57.1, 700: 25.7, 1100: 16.7}}
exp_si = [(q["T_K"], q["kappa_W_mK"]) for q in
          json.load(open(os.path.join(MT, "pilot", "kg", "extracted_points.json")))
          if "CITRINE" in str(q.get("corpusId")) and q["x_ge"] == 0 and q["T_K"]]

fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=False)
for ax, s in zip(axes, ("Si", "Ge")):
    pts = [p for p in res["points"].values() if p["system"] == s
           and p["cells"] == [8, 8, 8]]
    fes = sorted({p["Fe"] for p in pts})
    for p in pts:
        lo = p["Fe"] == min(q["Fe"] for q in pts if q["T"] == p["T"])
        c, dx = ("#1f77b4", -12) if lo else ("#ff7f0e", 12)
        rs = [r for r in res["runs"].values() if r["system"] == s
              and r["T_K"] == p["T"] and r["Fe_per_A"] == p["Fe"]
              and r["cells"] == [8, 8, 8]]
        for r in rs:
            ax.plot(p["T"] + dx, r["kappa"], "o", ms=3.5, color=c,
                    alpha=0.35 if r["pass"] else 1.0,
                    mfc=c if r["pass"] else "none")
        if p["estimate"]:
            e = p["estimate"]
            ax.errorbar(p["T"] + dx, e["kappa"], yerr=2 * e["se"], fmt="s",
                        color=c, ms=6, capsize=3)
    ax.plot(list(BTE[s]), list(BTE[s].values()), "k^-", label="BTE-DFT party")
    if s == "Si" and exp_si:
        T, k = zip(*sorted(exp_si))
        ax.plot(T, k, "D", color="#2ca02c", label="DB-CITRINE (experiment)")
    ax.plot([], [], "o", color="#1f77b4", label="HNEMD, lower $F_e$")
    ax.plot([], [], "o", color="#ff7f0e", label="HNEMD, higher $F_e$")
    ax.set_yscale("log")
    ax.set_xlabel("T (K)")
    ax.set_title(f"pure {s} (Tersoff 1989, 4096 atoms)")
    ax.set_xticks([300, 700, 1100])
axes[0].set_ylabel(r"$\kappa$ (W m$^{-1}$ K$^{-1}$)")
axes[0].legend(fontsize=7, loc="upper right")
fig.text(0.01, 0.01, "small markers: single 3-5 ns runs (open = failed a run gate); "
         "squares: point estimate +/- 2 seed SE", fontsize=7)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(sys.argv[1], dpi=200)
