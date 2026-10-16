#!/usr/bin/env python3
"""Fig. endpoint campaign (P2): pure Si and Ge lattice thermal conductivity
against temperature from the pre-registered GPUMD HNEMD endpoint campaign
(first production design, Tersoff-1989, 4096-atom cells), at one-column
print width. Print-size version of the logic in
gpumd/production/make_endpoint_figure.py.

Inputs (committed files only):
  gpumd/production/analysis_results.json   runs, run gates, point estimates
  gpumd/production_v2/analysis_v2.json     DFT phonon BTE values per state
  pilot/kg/extracted_points.json           experimental database rows (pure Si)
"""
import json

import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

res = json.load(open(S.PROJECT / "gpumd" / "production" / "analysis_results.json"))
v2 = json.load(open(S.PROJECT / "gpumd" / "production_v2" / "analysis_v2.json"))
BTE = {s: {T: v2["states"][f"{s}|{T}"]["bte_dft"] for T in (300, 700, 1100)}
       for s in ("Si", "Ge")}
exp_si = sorted((q["T_K"], q["kappa_W_mK"]) for q in
                json.load(open(S.PROJECT / "pilot" / "kg" / "extracted_points.json"))
                if "CITRINE" in str(q.get("corpusId")) and q["x_ge"] == 0 and q["T_K"])

from matplotlib.ticker import FixedLocator, NullLocator, ScalarFormatter  # noqa: E402

MD = S.PHYS
MD_DARK = S.PHYS_DARK          # higher driving force, same evidence source
STYLE = {"lo": (MD, "o", -40), "hi": (MD_DARK, "s", 40)}
# temperatures the corrected, separately registered design restored
RESTORED = [int(T) for T, r in v2["restore"].items() if r["restored"]]
RUN_X = 22                     # single runs drawn beside their point estimate

fig, axes = plt.subplots(1, 2, figsize=(S.COL, 2.95))
for ax, s in zip(axes, ("Si", "Ge")):
    for T in RESTORED:
        ax.axvspan(T - 110, T + 110, color="#DCEAF5", lw=0, zorder=0)
        ax.text(T, 0.985, "restored", transform=ax.get_xaxis_transform(), ha="center",
                va="top", fontsize=7, color=S.VERIFY_A)
    pts = [p for p in res["points"].values() if p["system"] == s and p["cells"] == [8, 8, 8]]
    for p in pts:
        lo = p["Fe"] == min(q["Fe"] for q in pts if q["T"] == p["T"])
        c, mk, dx = STYLE["lo" if lo else "hi"]
        rs = [r for r in res["runs"].values() if r["system"] == s and r["T_K"] == p["T"]
              and r["Fe_per_A"] == p["Fe"] and r["cells"] == [8, 8, 8]]
        side = -1 if lo else 1
        for r in rs:
            ax.plot(p["T"] + dx + side * RUN_X, r["kappa"], mk, ms=3.4 if r["pass"] else 4.2,
                    color=c, mew=0.6 if r["pass"] else 1.1, alpha=0.6 if r["pass"] else 1.0,
                    mfc=c if r["pass"] else "white", zorder=2 if r["pass"] else 5)
        if p["estimate"]:
            e = p["estimate"]
            ax.errorbar(p["T"] + dx, e["kappa"], yerr=2 * e["se"], fmt=mk, color=c,
                        ms=5, mec="white", mew=0.5, capsize=2, elinewidth=0.9, zorder=3)
    ax.plot(list(BTE[s]), list(BTE[s].values()), "^-", color=S.SOURCE_COLOURS["bte_dft"],
            ms=4, lw=1.0, zorder=4)
    if s == "Si":
        T, k = zip(*exp_si)
        ax.plot(T, k, "D", color=S.SOURCE_COLOURS["database"], ms=3.5, mec="white",
                mew=0.4, zorder=4)
    ax.set_yscale("log")
    ax.set_ylim(9, 700)
    ax.yaxis.set_major_locator(FixedLocator([10, 20, 50, 100, 200, 500]))
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_xlim(180, 1340)
    ax.set_xticks([300, 700, 1100])
    ax.set_xlabel("Temperature (K)")
    ax.set_title(f"pure {s}", loc="left")
axes[0].set_ylabel(r"$\kappa$ (W m$^{-1}$ K$^{-1}$)")

handles = [
    Line2D([], [], color=MD, marker="o", ls="", ms=4, label="Tersoff MD, lower $F_e$"),
    Line2D([], [], color=MD_DARK, marker="s", ls="", ms=4, label="Tersoff MD, higher $F_e$"),
    Line2D([], [], color=S.SOURCE_COLOURS["bte_dft"], marker="^", ms=4, lw=1.0,
           label="DFT phonon BTE"),
    Line2D([], [], color=S.SOURCE_COLOURS["database"], marker="D", ls="", ms=3.5,
           label="experimental database"),
    Line2D([], [], color=MD, marker="o", ls="", ms=3.4, alpha=0.6, label="single run"),
    Line2D([], [], color=MD, marker="o", ls="", ms=4.2, mfc="white", mew=1.1,
           label="run failed a run gate"),
]
fig.legend(handles=handles, loc="outside lower center", ncol=2, handlelength=1.6,
           columnspacing=1.0)
S.save(fig, "endpoint_campaign")
