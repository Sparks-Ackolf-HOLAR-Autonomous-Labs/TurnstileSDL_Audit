#!/usr/bin/env python3
"""Fig. size-free conductivities (P2): box-size-free alloy lattice thermal
conductivity of Si(1-x)Ge(x) against composition at 300, 700 and 1100 K,
with the alloy law before and after the registered level decision, at full
print width.

Inputs (committed files only):
  gpumd/sizefree/analysis_sizefree.json   HNEMD points (seed means, SE)
  gpumd/sizefree/corrected_law_gk300.json Green-Kubo 300 K points, adopted
                                          level factors and law shape
"""
import json

import numpy as np

import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

A = json.load(open(S.PROJECT / "gpumd" / "sizefree" / "analysis_sizefree.json"))
G = json.load(open(S.PROJECT / "gpumd" / "sizefree" / "corrected_law_gk300.json"))
M300, M_HI = G["m_300K"], G["level_700_1100K"]


def law(x, T):  # shape fitted to rNEMD, level 1 (before the decision)
    return 1.0 / (0.2092492 + 1.9190900 * x - 2.2443438 * x**2 + 8.352241e-5 * T)


def level(T):
    return M300 + (M_HI - M300) * (T - 300) / 400 if T < 700 else M_HI


MD = S.PHYS
GK = S.PHYS_DARK
xs = np.linspace(0.05, 0.90, 200)
fig, axes = plt.subplots(1, 3, figsize=(S.FULL, 2.4), sharey=True)
for ax, T in zip(axes, (300, 700, 1100)):
    ax.plot(xs, law(xs, T), color=S.GREY, ls="--", lw=1.0)
    ax.plot(xs, level(T) * law(xs, T), color=S.SOURCE_COLOURS["law"], lw=1.2)
    for p in A["points"]:
        if p["T"] != T:
            continue
        used = T != 300 and p["in_law_domain"]
        mk = "o" if p["in_law_domain"] else "D"
        ax.errorbar(p["x"], p["kappa"], yerr=2 * p["se"], fmt=mk, ms=4,
                    color=MD, mfc=MD if used else "white", mew=1.0,
                    capsize=1.5, elinewidth=0.8, zorder=3)
        if not p["in_law_domain"]:
            ax.annotate("outside validity\ndomain", (p["x"], p["kappa"] + 2 * p["se"]),
                        xytext=(p["x"] - 0.12, p["kappa"] + 2 * p["se"] + 2.3),
                        fontsize=7, ha="center", va="bottom",
                        arrowprops=dict(arrowstyle="-", lw=0.6, color=S.INK))
    if T == 300:
        for k, v in G["gk_points_300K_box12"].items():
            x = float(k.split("_")[0][1:])
            ax.errorbar(x, v["kappa"], yerr=2 * v["se"], fmt="s", ms=4,
                        color=GK, capsize=1.5, elinewidth=0.8, zorder=4)
    ax.set_title(f"{T} K")
    ax.set_xlabel("Ge fraction $x$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 9)
axes[0].set_ylabel(r"$\kappa$ (W m$^{-1}$ K$^{-1}$)")
handles = [
    Line2D([], [], marker="o", ls="", color=MD, ms=4, label="HNEMD, used by the rule"),
    Line2D([], [], marker="o", ls="", color=MD, mfc="white", ms=4, label="HNEMD, set aside by the rule"),
    Line2D([], [], marker="s", ls="", color=GK, ms=4, label="Green-Kubo, third registration"),
    Line2D([], [], color=S.GREY, ls="--", lw=1.0, label="law, box-length level"),
    Line2D([], [], color="k", lw=1.2, label="law, registered level"),
]
axes[1].legend(handles=handles, loc="upper left", fontsize=7, handlelength=1.6)
S.save(fig, "fig_sizefree")
