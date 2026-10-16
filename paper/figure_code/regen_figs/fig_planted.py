#!/usr/bin/env python3
"""Fig. planted violations (P2): which of the 37 planted violations the
outside verifier caught, by kind and by attacker model, at one-column
print width.

Reads planted_violations/results.json (written by
planted_violations/plant_and_verify.py). One marker per planted violation;
filled = caught (verifier exit status non-zero), open = not caught.
"""
import json

import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

R = json.load(open(S.PAPER / "planted_violations" / "results.json"))

SHORT = {  # plain labels for the 11 kinds, same order as plant_and_verify.py
    1: "raw output file edited or dropped",
    2: "record entry edited, not rehashed",
    3: "record entry edited and rehashed",
    4: "record line deleted",
    5: "record lines reordered",
    6: "design file swapped after commitment",
    7: "signature forged or key swapped",
    8: "decision cites a later registration",
    9: "exceptional value downweighted",
    10: "theorist answers recorded out of order",
    11: "correction beyond declared reach",
}
# verification pair of the paper (the same two colours in every figure)
MODEL_COL = {"outside edit": S.VERIFY_A, "key holder": S.VERIFY_B}

kinds = {}
for m in R["mutations"]:
    kinds.setdefault(m["no"], []).append(m)

nmax = max(len(v) for v in kinds.values())
fig = plt.figure(figsize=(S.COL, 2.6), layout="none")
ax = fig.add_axes([0.6, 0.02, 0.30, 0.86])
for row, no in enumerate(sorted(kinds)):
    for j, m in enumerate(kinds[no]):
        c = MODEL_COL[m["model"]]
        ax.scatter([j], [row], s=34, zorder=3, linewidth=1.0,
                   facecolor=c if m["caught"] else "white", edgecolor=c)
    caught = sum(m["caught"] for m in kinds[no])
    ax.text(nmax - 0.1, row, f"{caught}/{len(kinds[no])}", va="center", ha="left",
            fontsize=7, clip_on=False)
ax.set_yticks(range(len(kinds)))
ax.set_yticklabels([SHORT[k] for k in sorted(kinds)])
ax.invert_yaxis()
ax.set_xlim(-0.6, nmax - 0.4)
ax.set_xticks([])
for sp in ("top", "right", "bottom"):
    ax.spines[sp].set_visible(False)
ax.tick_params(axis="y", length=0)
handles = [
    Line2D([], [], ls="", marker="o", ms=5, mfc=MODEL_COL["outside edit"], mec=MODEL_COL["outside edit"], label="outside edit, caught"),
    Line2D([], [], ls="", marker="o", ms=5, mfc=MODEL_COL["key holder"], mec=MODEL_COL["key holder"], label="key holder, caught"),
    Line2D([], [], ls="", marker="o", ms=5, mfc="white", mec=S.INK, label="not caught"),
]
fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False,
           handletextpad=0.1, columnspacing=0.9, borderaxespad=0.1, fontsize=7)
S.save(fig, "fig_planted")
