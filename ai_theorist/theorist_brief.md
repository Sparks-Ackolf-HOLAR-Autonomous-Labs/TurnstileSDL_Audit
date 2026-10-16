# Brief for the AI theorist (issue 55, session 91)

You are acting as a theorist for an autonomous materials campaign on heat
transport in SiGe-based semiconductors (Si1-xGex alloys, nanostructured
SiGeC, strained SiGe films, and GeSn/SiGeSn films during annealing). The
campaign has several evidence sources of different and only qualitatively
known fidelity: published literature values, two molecular-dynamics (MD)
sources using the 1989 Tersoff potential (reverse non-equilibrium MD, and
GPUMD homogeneous non-equilibrium MD), MD with the MACE-MP-0 machine-learned
potential, first-principles Boltzmann transport (almaBTE, virtual-crystal
treatment of the alloy, DFT force constants), and open databases
(Starrydata2, Citrine).

For each question below, give a mechanism-level theory and a testable
prediction. Use only your own physics knowledge and the facts in this brief.
Do not look anything up and do not open any file.

Answer in a single JSON object with one key per question id. For each
question give:
- "theory": 1 to 3 sentences, the mechanism you propose;
- "category": one of the listed options, exactly as written;
- "p_category": your probability (0 to 1) that the category is right;
- "value": your numeric prediction where one is asked (else null);
- "value_range": a [low, high] interval you believe holds the true value
  with 80 % probability (else null);
- "falsifier": one run or measurement that would refute your theory;
- "reach": which other conclusions of the campaign would change if your
  theory holds (one sentence).

## Hindcast questions (the campaign faced these; answer as if before the result)

H1. Two 3C-SiC spheres of radius R are embedded in Si0.8Ge0.2 (Tersoff MD,
300 K, reverse NEMD). A continuum scattering model brackets the particle's
effect on lattice thermal conductivity between a density-contrast-only lower
bound and a stiffness-contrast-only upper bound. At R = 2.0 nm the bracket is
a 40 % to 75 % reduction of kappa relative to the same alloy without the
particle (with the surrounding composition held equal).
Category for the MD result at R = 2.0 nm: "below", "inside", "above".
Value: the MD reduction in percent.

H1b. In the same set-up, carbon prefers Si neighbours, so the control runs
place each particle inside a Si-rich (Ge-free) shell about 7 A thick. Does a
run with particle plus Si-rich shell conduct heat better or worse than the
bare Si0.8Ge0.2 alloy with neither?
Category: "higher", "lower". Value: percent change of kappa relative to the
bare alloy, for R = 2.0 nm.

H2. A symbolic law for Tersoff-MD kappa of Si1-xGex, of the form
kappa = 1/(a + b x + c x^2 + d T), was fitted on 0.05 <= x <= 0.93 at
finite box size. Points at x > 0.93 sit well above the law and an outlier
detector flagged two of them as isolated faults. At x = 0.90, 300 K, the
same box gives kappa = 4.5 W/mK.
Category: "fault" (the high points are errors), "physics" (they are real).
Value: kappa at x = 0.97, 300 K in the same box, W/mK.

H3. almaBTE (virtual crystal, DFT force constants, full iterative BTE)
gives kappa of bulk Si1-xGex in W/mK:

| x | 300 K | 700 K | 1100 K |
|---|---|---|---|
| 0 | 160.5 | 63.8 | 40.5 |
| 0.15 | 8.33 | 6.69 | 5.72 |
| 0.2 | 7.27 | 5.89 | 5.07 |
| 0.5 | 6.49 | 5.08 | 4.30 |
| 0.85 | 11.54 | 7.83 | 6.21 |
| 1 | 57.1 | 25.7 | 16.7 |

Value: almaBTE kappa at x = 0.7, 1100 K (W/mK). Category: where is the
composition of minimum kappa at 1100 K: "x<0.4", "0.4<=x<=0.6", "x>0.6".

H4. Amorphous Si0.5Ge0.5 is made by melt-quenching with the Tersoff
potential and kappa is computed by reverse NEMD in boxes of three lengths
(24, 48 and 96 conventional cells along the heat-flow direction, 4 x 4
cells across). Crystalline alloy kappa in these boxes rises with length.
Category: "size-independent", "rises with length", "falls with length".
Value: ratio kappa(96 cells)/kappa(24 cells).

H5. Pure crystalline Si: Tersoff-1989 GPUMD homogeneous NEMD kappa versus
almaBTE (160.5 W/mK at 300 K, 40.5 W/mK at 1100 K).
Value: ratio Tersoff/almaBTE at 300 K. Category for 1100 K:
"agree within 30 %", "Tersoff higher by more than 30 %",
"Tersoff lower by more than 30 %".

H6. Ball-milled and sintered Si0.8Ge0.2 with 1 at% carbon. MACE-MP-0
energies compare a substitutional C atom in the alloy with the same C atom
moved into a SiC precipitate.
Category: "SiC precipitate favoured", "substitutional favoured".
Value: energy gained per C atom by forming SiC, eV (positive = SiC
favoured). Also give, inside "theory", whether C prefers Si or Ge
neighbours and by how much (eV).

H7. A Si0.5Ge0.5 film is grown coherently on Si(001) (biaxial in-plane
compression of about 2 %) and kappa is computed by Tersoff MD in-plane and
across the film, compared with relaxed bulk Si0.5Ge0.5.
Category for the cross-plane change at 300 K: "increase", "decrease",
"no change within 5 %". Value: cross-plane change at 300 K in percent.
State in "theory" what happens in-plane.

H8. Starrydata2 holds digitized kappa of sintered (hot-pressed or spark
plasma sintered) Si0.8Ge0.2, many papers. almaBTE perfect-crystal kappa at
x = 0.2, 300 K is 7.27 W/mK.
Value: median ratio of sintered lattice kappa to the almaBTE value at
300 K. Category: "below 0.7", "0.7 to 0.9", "above 0.9".

H9. In-situ spectroscopic ellipsometry follows a Si0.08Ge0.88Sn0.04 film held
at 550 C. One sample is uncapped, the other capped with 3 nm SiO2. The
observable tracks loss of substitutional Sn near the surface.
Category: "cap suppresses the change", "cap accelerates the change",
"no difference". Value: for the uncapped film, the time in minutes before
the change becomes visible (incubation time).

## Open questions (no result exists yet; your answers will be tested later)

O1. MACE-MP-0 (the 2023 foundation potential) static calculation in
Ge0.88Sn0.12: binding energy of a Sn atom to a neighbouring vacancy
(positive = bound), eV. Category: "bound by more than 0.3 eV",
"bound by 0 to 0.3 eV", "unbound".

O2. MACE-MP-0 MD of Ge0.88Sn0.12 containing vacancies, 500 to 700 K,
about 1 ns. Effective activation energy of the Sn hops observed, eV.
Category: "close to the bulk Ge value (2.9 to 3.3 eV)",
"close to the low-temperature metastable-film value (1.1 to 1.8 eV)",
"below 1.1 eV".

O3. If the carbon-location calculation of H6 is repeated with a newer
foundation potential trained on more data (for example a MACE model trained
on MPtrj plus Alexandria), does the sign of the SiC-precipitation energy
hold? Category: "sign holds, magnitude within 0.3 eV", "sign holds,
magnitude changes by more than 0.3 eV", "sign flips". Value: predicted
energy gained per C atom, eV.
