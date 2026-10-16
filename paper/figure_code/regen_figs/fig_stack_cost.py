#!/usr/bin/env python3
"""Fig. stack cost (P2): verification cost of each layer against campaign
compute, at one-column print width.

Reads verify_record_result.json (written by
`python3 verify_record.py --json verify_record_result.json`). The two
reference values that are not in that file are the ones stated in the
Methods of the draft: bitwise re-execution of the six revision actions
(0.35 s) and the first endpoint campaign's compute (8.6 GPU-hours, the summed run times of its 33 GPUMD runs).
"""
import json

import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402

VR = json.load(open(S.PAPER / "verify_record_result.json"))
tm = VR["timing"]
raw_files = sum(v.get("raw_files", 0) for v in tm.values())
raw_s = sum(v["seconds"] for k, v in tm.items() if k != "ledger")

LAYER1, LAYER2, REF = "#0072B2", "#D55E00", S.GREY
rows = [  # (label, seconds, colour)
    (f"Layer 1: hash chain,\n{tm['ledger']['entries']} record entries", tm["ledger"]["seconds"], LAYER1),
    (f"Layer 1: re-hash of {raw_files}\nraw files, signatures", raw_s, LAYER1),
    ("Layer 2: re-execution of\nsix revision actions", 0.35, LAYER2),
    ("Endpoint campaign\ncompute, 8.6 GPU-h", 31077, REF),
]

fig, ax = plt.subplots(figsize=(S.COL, 1.75))
for i, (lab, s, c) in enumerate(rows):
    ax.plot([1e-4, s], [i, i], color=S.LIGHT, lw=1.6, zorder=1, solid_capstyle="butt")
    ax.scatter([s], [i], s=30, color=c, zorder=3, edgecolor="white", linewidth=0.8)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([r[0] for r in rows])
ax.invert_yaxis()
ax.set_xscale("log")
ax.set_xlim(1e-4, 1e6)
ax.set_xticks([1e-4, 1e-2, 1, 1e2, 1e4, 1e6])
ax.set_xlabel("Wall-clock time (s)")
ax.grid(axis="y", visible=False)
ax.tick_params(axis="y", length=0)
S.save(fig, "fig_stack_cost")
