#!/usr/bin/env python3
"""Fig. SiGeC carbon energies (P2): where carbon goes in Si(1-x)Ge(x), from
the MACE-MP-0 relaxations of the SiGeC campaign, under the first run (failed
its force gate, energies unvalidated) and under the separately registered
converged rerun (validated), at one-column print width.

Left: energy gained when one substitutional carbon atom leaves the lattice to
form SiC (minus the precipitation energy), at x = 0, 0.2 and 0.5.
Right: energy cost of a carbon atom with the most rather than the fewest Ge
neighbours (site preference), at x = 0.2 and 0.5.
One marker per host configuration (three per x), bar = mean.

Inputs (committed files only):
  nano_sigec/m1/m1_summary.json     first run (force gate failed)
  nano_sigec/m1c/m1c_summary.json   converged rerun (gates passed)
"""
import json

import numpy as np

import paper_fig_style as S

S.apply_style()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

M1 = json.load(open(S.PROJECT / "nano_sigec" / "m1" / "m1_summary.json"))
M1C = json.load(open(S.PROJECT / "nano_sigec" / "m1c" / "m1c_summary.json"))
assert M1["gates_pass"] is False and M1C["gates_pass"] is True

RUNS = [  # (summary, label, colour, marker, filled, x offset)
    (M1, "first run, force gate failed (unvalidated)", S.PHYS, "o", False, -0.035),
    (M1C, "converged rerun, gates passed (validated)", S.PHYS_DARK, "s", True, 0.035),
]
XS = ["0", "0.2", "0.5"]

fig, (a1, a2) = plt.subplots(1, 2, figsize=(S.COL, 2.35),
                             gridspec_kw={"width_ratios": [3, 2.3]})
shift_prec, shift_site, spread = [], [], []
for summ, _lab, c, mk, filled, dx in RUNS:
    for xk in XS:
        d = summ["per_x"][xk]
        x = float(xk)
        e = -np.array(d["dE_prec_eV"])
        a1.scatter(np.full(e.size, x + dx), e, s=16, marker=mk, color=c,
                   facecolor=c if filled else "white", linewidth=1.0, zorder=3)
        a1.plot([x + dx - 0.025, x + dx + 0.025], [e.mean()] * 2, color=c, lw=1.6, zorder=4)
        if summ is M1C:
            spread.append(e.max() - e.min())
        if d["site_pref"]:
            s = np.array([q["dE_site"] for q in d["site_pref"]])
            a2.scatter(np.full(s.size, x + dx), s, s=16, marker=mk, color=c,
                       facecolor=c if filled else "white", linewidth=1.0, zorder=3)
            a2.plot([x + dx - 0.025, x + dx + 0.025], [s.mean()] * 2, color=c, lw=1.6, zorder=4)
for xk in XS:
    shift_prec.append(abs(M1C["per_x"][xk]["dE_prec_mean_eV"] - M1["per_x"][xk]["dE_prec_mean_eV"]))
    if M1["per_x"][xk]["dE_site_mean_eV"] is not None:
        shift_site.append(abs(M1C["per_x"][xk]["dE_site_mean_eV"] - M1["per_x"][xk]["dE_site_mean_eV"]))

a1.set_xticks([0, 0.2, 0.5])
a1.set_xlim(-0.1, 0.6)
a1.set_ylim(1.35, 1.85)
a1.set_xlabel("Ge fraction $x$")
a1.set_ylabel("Energy gained by forming SiC\n(eV per C)")
a1.set_title("C forms SiC", loc="left", fontsize=8)
a2.set_xticks([0.2, 0.5])
a2.set_xlim(0.05, 0.65)
a2.set_ylim(0, 0.45)
a2.set_xlabel("Ge fraction $x$")
a2.set_ylabel("Ge-rich minus Si-rich\nsite energy (eV per C)")
a2.set_title("C prefers Si sites", loc="left", fontsize=8)
handles = [Line2D([], [], ls="", marker=mk, ms=4.5, color=c, mfc=c if filled else "white",
                  mew=1.0, label=lab) for _s, lab, c, mk, filled, _dx in RUNS]
fig.legend(handles=handles, loc="outside lower center", ncol=1, handletextpad=0.3)
S.save(fig, "fig_sigec_carbon")
print(f"largest shift of the mean between runs: precipitation {max(shift_prec):.3f} eV, "
      f"site {max(shift_site):.3f} eV; largest spread over configurations "
      f"(rerun) {max(spread):.3f} eV")
print("rerun means (eV gained):", [round(-M1C["per_x"][x]["dE_prec_mean_eV"], 3) for x in XS])
