#!/usr/bin/env python3
"""Fig. SiGeC timeline (P2): the SiGeC campaign's ledger events against
wall-clock hours after the first pre-registration, at one-column print
width. Reads ../../phase_c/ledger_campaign.jsonl (entries 46-49, 53-55).
"""
import datetime as dt
import json

import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402

LEDGER = [json.loads(l) for l in open(S.PROJECT / "phase_c" / "ledger_campaign.jsonl")]
E = {e["seq"]: e for e in LEDGER}


def t(seq):
    return dt.datetime.strptime(E[seq]["time"], "%Y-%m-%dT%H:%M:%SZ")


t0 = t(46)


def hrs(s):
    return (t(s) - t0).total_seconds() / 3600


lanes = ["Pre-registration", "Raw outputs", "Gate failure", "Analysis", "Strengthen"]
ev = [(46, 0), (47, 1), (48, 2), (49, 3), (53, 0), (54, 1), (55, 4)]
# verification pair of the paper: blue = registered step, purple = gate failure
col = {0: S.VERIFY_A, 1: S.GREY, 2: S.VERIFY_B, 3: S.GREY, 4: S.VERIFY_A}

fig, ax = plt.subplots(figsize=(S.COL, 1.85))
ax.axvspan(hrs(48), hrs(55), color="#F2E0EA", lw=0, zorder=0)
ax.text((hrs(48) + hrs(55)) / 2, -0.85, "energies unvalidated",
        ha="center", va="center", fontsize=7)
# join each group's events in time order
for grp in ([46, 47, 48, 49], [53, 54, 55]):
    ax.plot([hrs(s) for s in grp], [dict(ev)[s] for s in grp], color=S.LIGHT,
            lw=1.0, zorder=1)
for s, lane in ev:
    ax.scatter([hrs(s)], [lane], s=30, color=col[lane], zorder=3,
               edgecolor="white", linewidth=0.8)
    ax.annotate(str(s), (hrs(s), lane), xytext=(0, 5), textcoords="offset points",
                ha="center", va="bottom", fontsize=7)
ax.set_yticks(range(len(lanes)))
ax.set_yticklabels(lanes)
ax.set_ylim(4.5, -1.3)
ax.set_xlim(-0.4, hrs(55) + 0.4)
ax.set_xlabel("Time after pre-registration (h)")
ax.grid(axis="y", visible=False)
ax.tick_params(axis="y", length=0)
S.save(fig, "fig_sigec_timeline")
