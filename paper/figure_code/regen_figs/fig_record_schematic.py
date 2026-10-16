#!/usr/bin/env python3
"""Fig. record schematic (P2): how one pre-registered acquisition is written
to the hash-chained ledger, and what an outside reader can check at each
step, at full two-column print width.

Concept figure, no data. The five steps and the three checks are the ones
the Methods describe (design hash, registration, raw-output Merkle root,
analysis, decision citing its registration); the example labels are the
SiGeC MACE gate of the main text.
"""
import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

BLUE, ORANGE, GREEN, GREY = "#0072B2", "#D55E00", "#009E73", S.GREY

STEPS = [  # (title, what is written, example, colour)
    ("1  Design", "design file\nand its hash", "gates, predictions,\ndecision rule", BLUE),
    ("2  Register", "record entry\nbefore any run", "pushed before\nthe job starts", BLUE),
    ("3  Run", "raw outputs,\nMerkle root", "root in the record\nbefore reading", GREY),
    ("4  Analyse", "registered\nscript applied", "gate failed:\nclaims unvalidated", ORANGE),
    ("5  Decide", "revision action\ncites step 2", "rerun registered,\nthen strengthen", GREEN),
]

fig = plt.figure(figsize=(S.FULL, 1.8), layout="none")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 10)
ax.set_ylim(-0.3, 2.45)
ax.axis("off")

w, h, y0 = 1.6, 0.85, 1.22
xs = [0.25 + i * 1.98 for i in range(len(STEPS))]
for x, (title, body, ex, c) in zip(xs, STEPS):
    ax.add_patch(FancyBboxPatch((x, y0), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc="white", ec=c, lw=1.2))
    ax.text(x + w / 2, y0 + h - 0.13, title, ha="center", va="top", fontsize=8,
            color=c, weight="bold")
    ax.text(x + w / 2, y0 + 0.36, body, ha="center", va="center", fontsize=7)
    ax.text(x + w / 2, y0 - 0.12, ex, ha="center", va="top", fontsize=7, color=S.GREY,
            style="italic")
for a, b in zip(xs[:-1], xs[1:]):
    ax.add_patch(FancyArrowPatch((a + w + 0.03, y0 + h / 2), (b - 0.03, y0 + h / 2),
                                 arrowstyle="-|>", mutation_scale=8, lw=0.9, color=S.INK))

# the decision cites its registration
ax.add_patch(FancyArrowPatch((xs[4] + w / 2, y0 + h + 0.02), (xs[1] + w / 2, y0 + h + 0.02),
                             connectionstyle="arc3,rad=0.07", arrowstyle="-|>", mutation_scale=7,
                             lw=0.7, ls="--", color=GREEN))

# ledger chain under the steps
ly = 0.18
ax.text(5.0, ly - 0.16, "Campaign record: one entry per step, each carrying the hash of the entry before it",
        fontsize=7, color=S.INK, va="top", ha="center")
for i, x in enumerate(xs):
    ax.add_patch(FancyBboxPatch((x + w / 2 - 0.22, ly - 0.1), 0.44, 0.22,
                                boxstyle="round,pad=0.01,rounding_size=0.04",
                                fc=S.LIGHT, ec=S.GREY, lw=0.6))
    ax.plot([x + w / 2] * 2, [ly + 0.12, y0 - 0.55], color=S.GREY, lw=0.6, ls=(0, (1.5, 1.5)))
    if i:
        ax.plot([xs[i - 1] + w / 2 + 0.22, x + w / 2 - 0.22], [ly + 0.01] * 2,
                color=S.GREY, lw=0.8)
S.save(fig, "fig_record_schematic")
