You are a MAPPER, not a theorist. Do NOT use any tool at all (no file reads, no searches, no commands). Answer from the text below only.

A literature-grounded theorist (the Asta Theorizer) produced the theories in PART B. Your job is to fill the answer form defined in PART A (the brief) using ONLY what the theories in PART B state. Rules:
- For each question id (H1b, H5, H6, H7) (round 2b asks only these four; ignore every other id in the brief), give the fields the brief asks for (theory, category, p_category, value, value_range, falsifier, reach) plus a field "basis": an exact quote (one or two sentences, copied verbatim) from PART B that the category rests on.
- If the theories in PART B do not address a question well enough to choose a category, set "category": null, "p_category": null, "value": null, "value_range": null and "basis": null. Do not use your own physics knowledge to fill a gap. A numeric value may be given only if PART B states a number or a direct rule that yields it; otherwise value and value_range are null even if the category is filled.
- p_category expresses how strongly the quoted theory supports the category (0 to 1).
- Output a single JSON object, keys = question ids, nothing else before or after it.

PART A (the brief):
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


PART B (the Theorizer's theories):

# Theorizer run `r2b_carbon_sic` (task 08c7035b-f776-46e3-9e87-85c7be70cf91)

Papers extracted (5): Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys; Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing; Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si; Recent developments in vertical MOSFETs and SiGe HBTs; Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art

## A Si-rich shell can either offset or amplify the thermal resistance of a SiC nanoparticle, depending on which scattering dominates

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Three-term competition: inclusion scattering + interface resistance − alloy-disorder relief

A SiC particle lowers κ by scattering phonons and adding interface resistance, but a Si-rich shell can locally reduce alloy disorder and raise κ; the observed κ is set by the balance.

**Supporting evidence:**

  * Proposed strategy in L-PBF SiGe is to form nanoprecipitates (including SiC) specifically to scatter phonons and reduce lattice thermal conductivity, implying inclusion-scattering as a primary mechanism. [Baudry et al., 2024]

  * Review of SiC nanowires emphasizes strong size dependence of κ due to boundary/interface scattering, supporting the importance of nm-scale interfaces for phonon transport. [Li et al., 2021]

  * RTCVD SiGeC films show substitutional carbon causes strong local bond distortions and phonon-frequency shifts (Si–Si softening; Si–C mode hardening), consistent with strong local vibrational perturbations that can affect scattering and interface mismatch when C/SiC-related features are present. [Wasyluk et al., 2010]

  * This statement was logically inferred (abduction) from: (i) the mission statement’s continuum bracketing using density-contrast-only vs stiffness-contrast-only models for SiC spheres (implying at least two inclusion-scattering channels) and (ii) the mission statement’s explicit scenario of a Ge-free (Si-rich) shell around the particle (implying a third, composition-driven modification of intrinsic alloy scattering not included in bare-particle continuum bounds).

### Shell-thickness crossover between (beneficial) disorder relief and (harmful) added scattering area/interfaces

A very thin Si-rich layer can sometimes slightly help heat flow compared with a bare particle, but a thicker layer usually hurts because it makes the ‘obstacle’ bigger and adds another interface.

**Supporting evidence:**

  * Mission context specifies a Ge-free (Si-rich) shell of ~7 Å around the particle in control runs, implying shell thickness is physically relevant and comparable to a few atomic spacings.

  * SiC nanowire literature emphasizes that nm-scale boundary scattering can strongly suppress κ, consistent with the idea that adding an additional interface or increasing effective obstacle size can reduce κ. [Li et al., 2021]

  * This statement was logically inferred (abduction) by combining: (i) the general size dependence of boundary/interface scattering at nanoscales (supported by e6.1) with (ii) the mission’s explicit existence of a finite-thickness, compositionally distinct shell (7 Å), which simultaneously reduces alloy disorder locally and introduces extra scattering geometry.

### Predictions

### 3 Likely outcomes

  * At fixed SiC core radius R, κ_lat versus shell thickness t will often be non-monotonic: for very thin, high-quality shells κ_lat can be slightly higher than in the bare-core case (disorder relief dominates), while for thicker shells κ_lat decreases (extra interface/cross-section dominates).

  * Increasing the host Ge fraction x (stronger intrinsic alloy scattering) increases the potential κ benefit of a Ge-depleted shell, shifting t* to larger values (thicker shells needed before added scattering dominates).

  * Replacing an abrupt Ge-free shell with a graded (Si-rich→matrix) shell of the same outer radius increases κ_lat relative to the abrupt shell because the graded region reduces effective Kapitza resistance (better impedance matching).

### 2 Unknown outcomes

  * For R≈2 nm, an optimally graded shell could produce an MD κ reduction smaller than what a density-contrast-only continuum lower bound would predict for a bare particle (i.e., the shell acts as an impedance-matching layer for a significant part of the phonon spectrum).

  * At sufficient inclusion density, overlapping Ge-depleted shells could create a percolating Si-rich network that increases κ_lat relative to a random homogeneous Si0.8Ge0.2 matrix even while inclusions remain present, yielding a non-intuitive κ versus inclusion density curve (initial decrease then partial recovery).

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * If atomistic simulations sweeping shell thickness always show monotonic κ_lat decrease with t (for realistic interface structures), the proposed disorder-relief vs added-scattering crossover mechanism is falsified.

  * If an atom-probe or STEM-EDS measurement (in an experimental analog system) finds no meaningful Ge depletion around SiC/C-rich inclusions, then the disorder-relief term is negligible and the theory’s shell mechanism is unsupported.

  * If spectral phonon transmission calculations show that graded shells do not reduce interfacial resistance compared with abrupt shells, then the impedance-matching assumption is wrong.

### 1 Unaccounted for

  * No provided evidence directly measures κ of SiGe with SiC nanoprecipitates or with Si-rich/Ge-depleted shells; the theory extrapolates from general nanostructure/interface concepts and the mission scenario. [Baudry et al., 2024] [Li et al., 2021] [Wasyluk et al., 2010]

* * *

**Related Artifacts:**

  * [Extraction: Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art]

* * *

## Entities

[Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing](<https://www.semanticscholar.org/paper/273902266>)

M. Baudry, Guillaume Savelli, Guilhem Roux | 2024 | 2024 IEEE 14th International Conference Nanomaterials: Applications & Properties (NAP) | [Semantic Scholar](<https://www.semanticscholar.org/paper/273902266>)

[Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art](<https://www.semanticscholar.org/paper/232358380>)

You-Dong Li, Guilei Wang, Mehdi Akbari-Saatlu et al. | 2021 | Frontiers in Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/232358380>)

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

## Citation

Cite this artifact as `\cite{ast-si-2026-10-09}`.
[code] 
    @misc{ast-si-2026-10-09,
      title        = {A Si-rich shell can either offset or amplify the thermal resistance of a SiC nanoparticle, depending on which scattering dominates},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/a-si-rich-shell-can-either-offset-or-amplify-the-thermal-resistance-of-a-sic-nan.md},
      note         = {asta-artifact id: theory-3},
    }
[/code]

## Carbon can stay substitutional during growth, but later heat treatments can drive it into clusters or SiC if kinetics allow

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Growth-window substitutionality law (Cs dominates; SiC absent in as-grown RTCVD SiGeC up to ~1.8 at.% C)

Under certain RTCVD growth conditions, carbon stays mostly substitutional and does not form SiC precipitates even up to about 1.8% C.

**Supporting evidence:**

  * Si–C local vibrational mode near ~605 cm−1 attributed exclusively to substitutional carbon; integrated FTIR and Raman intensity scale linearly with substitutional carbon y and are essentially independent of Ge content up to 16%. [Wasyluk et al., 2010]

  * No SiC precipitates detected: FTIR shows no absorption peak in 750–800 cm−1 region where SiC stretching modes would appear (~800 cm−1); authors conclude absence of SiC precipitate phase in all samples studied. [Wasyluk et al., 2010]

### Thermal-budget/defect-injection law: oxidation/anneals drive Cs→Ci/clustering and possible precipitation

Heat treatments—especially oxidation and implant-related damage—tend to knock carbon out of substitutional sites, making it mobile and more likely to cluster or precipitate.

**Supporting evidence:**

  * Paper discussing SiGe:C in HBT processing emphasizes that substitutional carbon is desired but can be lost/redistributed or cluster during post-growth thermal processing; oxidation generates higher carbon loss rates than vacuum/inert anneals; Si-cap thickness and thermal budget strongly influence retention and clustering. [Hall et al., 2004]

  * Ge:C MBE study shows incorporation is kinetically limited and temperature-windowed: improved incorporation above ~450 °C but roughening/bond breakage above ~475 °C, illustrating that carbon incorporation state can change when bond stability/kinetics change with temperature. [Stephenson et al., 2016]

### Predictions

### 3 Likely outcomes

  * For SiGeC layers with similar C content, oxidation anneals will reduce the substitutional-C spectroscopic signature (e.g., ~610 cm−1 FTIR line discussed in processing paper) more strongly than inert anneals at comparable temperatures, and will increase signatures consistent with clustering/redistribution.

  * As-grown RTCVD SiGeC compositions within x≈9–16%, y≤1.8% will remain free of detectable SiC (FTIR ~800 cm−1) unless subjected to additional thermal budget or defect injection.

  * In MBE-like kinetically limited growth, a temperature window exists where substitutional incorporation is high and clustering is minimal; exceeding it increases bond breakage/roughening and raises the likelihood of non-substitutional carbon configurations.

### 2 Unknown outcomes

  * At fixed C content, there exists a critical combination of (temperature, time, interstitial injection rate) beyond which SiC nucleation becomes rapid; mapping this would yield a time–temperature–defect-injection ‘TTD’ diagram for SiC precipitation in SiGe:C.

  * Carbon nearest-neighbor preference (Si vs Ge) could shift the dominant precipitation pathway: if C strongly avoids Ge, Ge-rich matrices might exhibit faster Ge-depletion shells and earlier SiC nucleation at lower global C than Si-rich matrices.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * If controlled anneals in oxidizing vs inert ambients produce identical Cs retention/clustering behavior, the oxidation-driven interstitial flux mechanism is incorrect or irrelevant for these structures.

  * If SiC precipitates form readily in as-grown RTCVD films within the stated growth window despite the reported FTIR null result, then either detection limits dominate or the non-precipitation claim is not robust across reactors/conditions.

### 1 Unaccounted for

  * No provided dataset contains quantitative formation energies comparing substitutional C vs SiC precipitate in Si0.8Ge0.2 (the mission’s H6 asks for this but evidence here does not provide numbers). [Hall et al., 2004] [Wasyluk et al., 2010] [Stephenson et al., 2016]

* * *

**Related Artifacts:**

  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys]

* * *

## Entities

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

[Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys](<https://www.semanticscholar.org/paper/14320628>)

C. Stephenson, Miriam M Gillett-Kunnath, William A. O'Brien et al. | 2016 | [Semantic Scholar](<https://www.semanticscholar.org/paper/14320628>)

## Citation

Cite this artifact as `\cite{ast-carbon-2026-10-09-2}`.
[code] 
    @misc{ast-carbon-2026-10-09-2,
      title        = {Carbon can stay substitutional during growth, but later heat treatments can drive it into clusters or SiC if kinetics allow},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/carbon-can-stay-substitutional-during-growth-but-later-heat-treatments-can-drive.md},
      note         = {asta-artifact id: theory-4},
    }
[/code]

## Carbon’s local bonding preferences decide whether it stays dissolved or turns into SiC

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Metastable substitutional-carbon regime with 3nn ordering before precipitates

Under suitable growth conditions, carbon mostly sits on lattice sites and forms some ordered C–C pairs, without forming SiC precipitates.

**Supporting evidence:**

  * RTCVD Si1-x-yGexCy films (x≈9–16%, y≈0–1.8%) show a ~605 cm^-1 Si–C local vibrational mode attributed exclusively to substitutional carbon; integrated IR intensity and Raman ratios scale linearly with substitutional C content and are essentially independent of Ge content up to 16%. [Wasyluk et al., 2010]

  * A Raman satellite near ~630 cm^-1 increases with carbon content and is attributed to 3nn substitutional C–C pairs; satellite/local intensity ratio increases linearly with y up to 1.8%, consistent with short-range ordering rather than precipitation. [Wasyluk et al., 2010]

  * FTIR inspection in the 750–800 cm^-1 region finds no SiC stretching-mode absorption (~800 cm^-1) in any measured RTCVD samples; authors explicitly conclude absence of SiC precipitate phase under these growth conditions. [Wasyluk et al., 2010]

  * Ge1-xCx grown by MBE using a Ge4C-core precursor shows no detectable C–C clusters by TEM/HRTEM/Raman/NRA-RBS/STEM-EDX at dilute concentrations, consistent with kinetically stabilized substitutional/sp3-like incorporation when chemistry prevents exposed carbon on the growth surface. [Stephenson et al., 2016]

  * Process-focused discussion emphasizes substitutional carbon is achievable under far-from-equilibrium growth and can be a small fraction of total C; also stresses that Cs is metastable and can be lost/redistributed under later thermal processing. [Hall et al., 2004]

### Thermal-budget-activated transition from substitutional C to mobile C and clustering/precipitation tendency

After growth, thermal processing—especially steps that create lots of defects—tends to push carbon out of substitutional sites and toward clustering/precipitation.

**Supporting evidence:**

  * Process discussion distinguishes total carbon (SIMS) from substitutional carbon (HRXRD/Raman/FTIR) and notes discrepancies arise and must be interpreted as differing Cs/Ci ratios; HRTEM is suggested if XRD and SIMS diverge after annealing (indicative of redistribution/clustering). [Hall et al., 2004]

  * Process discussion states oxidation produces higher carbon loss rates than vacuum/inert anneals; carbon retention depends strongly on Si-cap thickness and overall thermal budget, implying strong processing sensitivity of carbon stability. [Hall et al., 2004]

  * Process discussion states clustering and redistribution can occur during post-growth thermal processing, with interstitial carbon (Ci) as a consequence of clustering/redistribution during processing. [Hall et al., 2004]

  * RTCVD as-grown films at 550 °C show substitutional C with no SiC precipitates, providing a baseline that thermal processing (not present there) is a plausible differentiator for precipitation outcomes. [Wasyluk et al., 2010]

### Predictions

### 2 Likely outcomes

  * For Si1-x-yGexCy films in the RTCVD-like substitutional regime, modest changes in Ge fraction within x≈0.09–0.16 will not significantly change the proportionality between IR Si–C integrated intensity and substitutional C, but will change Si–Si Raman shift slopes with y (as observed), allowing decoupled calibration of y and strain.

  * Introducing a post-growth oxidation step (vs inert anneal at similar temperature/time) will produce a larger increase in SIMS-total-C vs substitutional-C-proxy disparity and stronger emergence of nonsubstitutional signatures (e.g., additional FTIR/Raman features) than an inert anneal alone.

### 2 Unknown outcomes

  * If local Si chemical potential can be engineered (e.g., by creating Si-rich nanoscale regions in SiGe), carbon will concentrate there even without forming SiC, enabling designed 'C segregation templates' detectable by APT.

  * At sufficiently high y but still below gross precipitation, the 3nn-pair satellite/local intensity ratio will deviate from linearity due to higher-order C ordering motifs; this would provide a spectroscopic route to infer the onset of medium-range order before precipitates appear.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * If in as-grown RTCVD samples with y up to ~1.8% a reproducible ~800 cm^-1 SiC band appears without post-anneal, the 'substitutional/3nn regime before precipitates' statement is false or too broad.

  * If oxidation steps do not increase the SIMS vs substitutional-proxy disparity relative to inert anneals at the same thermal budget, then defect-rich processing is not the primary lever controlling carbon redistribution.

### 1 Unaccounted for

  * No direct evidence in the provided dataset quantifies energetic preference of C for Si vs Ge nearest neighbors in mixed SiGe, nor does it provide formation energies for SiC precipitation in SiGe; thus the theory cannot assign numeric neighbor-preference energies or precipitation driving forces. [Hall et al., 2004] [Wasyluk et al., 2010] [Stephenson et al., 2016]

* * *

**Related Artifacts:**

  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys]

* * *

## Entities

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

[Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys](<https://www.semanticscholar.org/paper/14320628>)

C. Stephenson, Miriam M Gillett-Kunnath, William A. O'Brien et al. | 2016 | [Semantic Scholar](<https://www.semanticscholar.org/paper/14320628>)

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

## Citation

Cite this artifact as `\cite{ast-carbon-2026-10-09-4}`.
[code] 
    @misc{ast-carbon-2026-10-09-4,
      title        = {Carbon’s local bonding preferences decide whether it stays dissolved or turns into SiC},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/carbons-local-bonding-preferences-decide-whether-it-stays-dissolved-or-turns-int.md},
      note         = {asta-artifact id: theory-7},
    }
[/code]

## Carbon’s location in SiGe is set by a competition between elastic strain (metastable dissolved C) and the stability of SiC, mediated by processing-created point defects

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Metastable Cs retention requires kinetically limited growth and low interstitial injection

Low-temperature epitaxy can lock carbon onto lattice sites, but oxidation and implantation steps can shake it loose into interstitials/clusters that can seed precipitation.

**Supporting evidence:**

  * Process paper: achieving and retaining substitutional C requires controlled low-temperature epitaxial growth (MBE/CVD) with 2D growth conditions and careful thermal-budget management; oxidation and implant damage increase interstitial fluxes and can cause C loss or clustering; oxidation generates higher carbon loss rates than vacuum/inert anneals. [Hall et al., 2004]

  * Ge:C MBE study: incorporation is kinetically limited; effective incorporation appears above ~450 °C, while above ~475 °C surface roughening and Ge–C bond breakage indicates kinetic/chemical destabilization; multiple probes show no detectable C–C clusters at dilute concentrations when using a Ge4C-core precursor. [Stephenson et al., 2016]

### Precursor-imposed local coordination suppresses C–C clustering at dilute levels

If the precursor keeps carbon bonded to host atoms, carbon atoms are less likely to find each other and cluster, so they stay substitutional at low concentrations.

**Supporting evidence:**

  * Ge:C study: Ge4C-core precursor designed such that C is fully surrounded by Ge; authors report no detectable C–C clusters by HRTEM/Raman/NRA-RBS/STEM-EDX and infer substitutional/sp3-like incorporation; a direct bandgap reduction consistent with dilute substitutional C is observed. [Stephenson et al., 2016]

  * Background mentions E4C-core precursor strategies previously applied to Si1−xCy and SiGeC to encourage substitutional carbon and reduce graphitic clustering (contextual prior art). [Stephenson et al., 2016]

### Predictions

### 2 Likely outcomes

  * If SiGe:C is grown with an E4C-core precursor under a temperature window that preserves surface host–C bonds, Raman/FTIR signatures of substitutional C will dominate with minimal evidence of C–C clustering at comparable dilute y.

  * Increasing oxidation time/temperature at fixed initial Cs in SiGe:C will increase SIMS–HRXRD (or SIMS–FTIR) discrepancies by converting Cs into non-substitutional carbon that is invisible to Cs-specific strain/vibrational markers.

### 2 Unknown outcomes

  * There exists a sharp crossover in post-growth annealing where interstitial injection flips the dominant sink for C from point-defect complexes to SiC nuclei, producing a time–temperature–interstitial-flux ‘precipitation map’ even at the same total C content.

  * In Si1−xGex with high Ge fractions, a sufficiently strong preference of C for Si neighbors could produce spontaneous nanoscale Si enrichment around C-rich regions even before SiC nucleation, creating a measurable Ge-depleted shell signature by APT.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * Grow two SiGe:C sets at identical y and x: one with an E4C-core-like precursor and one with a conventional carbon precursor. If both show equal levels of C–C clustering (TEM/Raman) under identical conditions, the precursor-imposed coordination mechanism is weakened.

  * If oxidation/implant anneals do not measurably change the Cs fraction (as inferred by Cs-sensitive probes) relative to inert anneals at the same thermal budget, the interstitial-injection-driven Cs→Ci/Cn conversion hypothesis is weakened.

### 1 Unaccounted for

  * No quantitative formation energies, diffusion coefficients, or nucleation barriers are provided in the evidence set, so this theory cannot yet parameterize rates or energetic thresholds for SiC precipitation in SiGe. [Hall et al., 2004] [Li et al., 2021] [Stephenson et al., 2016] [Wasyluk et al., 2010]

* * *

**Related Artifacts:**

  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art]
  * [Extraction: Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys]

* * *

## Entities

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

[Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys](<https://www.semanticscholar.org/paper/14320628>)

C. Stephenson, Miriam M Gillett-Kunnath, William A. O'Brien et al. | 2016 | [Semantic Scholar](<https://www.semanticscholar.org/paper/14320628>)

[Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art](<https://www.semanticscholar.org/paper/232358380>)

You-Dong Li, Guilei Wang, Mehdi Akbari-Saatlu et al. | 2021 | Frontiers in Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/232358380>)

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

## Citation

Cite this artifact as `\cite{ast-carbon-2026-10-09-3}`.
[code] 
    @misc{ast-carbon-2026-10-09-3,
      title        = {Carbon’s location in SiGe is set by a competition between elastic strain (metastable dissolved C) and the stability of SiC, mediated by processing-created point defects},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/carbons-location-in-sige-is-set-by-a-competition-between-elastic-strain-metastab.md},
      note         = {asta-artifact id: theory-5},
    }
[/code]

## Carbon’s location in SiGe is set by a trade between strain, bonding, and processing kinetics

**Contents:**

  * 4 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 4 Theory Statements

### Kinetic trapping yields predominantly substitutional C and suppresses detectable SiC in as-grown films

If growth is sufficiently kinetically constrained, carbon stays on lattice sites (substitutional) and doesn’t show SiC precipitates in as-grown material, within the experiments’ detection limits.

**Supporting evidence:**

  * RTCVD Si1-x-yGexCy: a Si–C local vibrational mode near ~605 cm−1 is stated to originate only from substitutional carbon; linear scaling of IR/Raman C signals with y is consistent with predominant Cs incorporation up to y=1.8%. [Wasyluk et al., 2010]

  * RTCVD Si1-x-yGexCy: FTIR inspection in the 750–800 cm−1 region finds no absorption peak near ~800 cm−1; authors explicitly conclude absence of SiC precipitate phase in all studied as-grown samples. [Wasyluk et al., 2010]

  * Ge1-xCx MBE with (H3Ge)4C precursor: multiple structural/spectroscopic probes (TEM/HRTEM/Raman/NRA-RBS/STEM-EDX) report no detectable C–C clusters/graphitic inclusions at dilute C; authors interpret incorporation as substitutional/sp3-like and observe a 24 meV direct-gap reduction consistent with dilute substitutional C effects. [Stephenson et al., 2016]

  * Process-focused SiGe:C discussion: emphasizes growth far from equilibrium (metastable alloys, C supersaturation possible) and that substitutional carbon is desired/obtained under appropriate growth conditions but can be lost/redistributed under subsequent thermal processing. [Hall et al., 2004]

### Substitutional carbon exhibits increasing 3nn C–C short-range order with increasing Cs fraction

As substitutional carbon increases (up to ~1.8%), more of it forms preferred, spaced substitutional pairs (3rd-nearest neighbors) rather than precipitating as SiC in the as-grown state.

**Supporting evidence:**

  * RTCVD Si1-x-yGexCy: a Raman satellite near ~630 cm−1 is reported; its intensity relative to the local Si–C mode increases linearly with y and is attributed to 3nn substitutional C–C pairs; authors cite theory that 3nn is most strongly bound because short Si–C bonds can be accommodated without strong bond-bending. [Wasyluk et al., 2010]

  * RTCVD Si1-x-yGexCy: despite increasing y to 1.8%, FTIR shows no SiC precipitate band near ~800 cm−1, supporting that increasing carbon first manifests as substitutional ordering rather than detectable SiC precipitation in as-grown samples. [Wasyluk et al., 2010]

### Defect-injecting thermal processing increases carbon redistribution/clustering propensity relative to inert anneals

Processing that generates many defects (oxidation, implantation) makes carbon move and cluster more than inert annealing does, enabling precipitation routes.

**Supporting evidence:**

  * Process discussion reports that oxidation produces higher carbon loss rates than vacuum/inert anneals and that carbon redistribution/clustering can occur during thermal processing; clustering can produce interstitial carbon (Ci) as an outcome of redistribution under processing steps (qualitative). [Hall et al., 2004]

### SiC-like precipitation requires (and promotes) Si-rich local environments; Ge-depleted shells are a plausible but not yet evidenced consequence

Mobile carbon is expected to form SiC-like environments when it precipitates, so precipitation should favor Si-rich regions and may push Ge away locally—though that shell effect isn’t directly shown in the provided evidence.

**Supporting evidence:**

  * Provided evidence establishes that under certain as-grown RTCVD conditions, SiC precipitates are not observed up to y=1.8% Cs, implying precipitation is not inevitable and requires access to additional pathways (mobility/kinetics), consistent with the need for a mobility-enabling step before precipitation. [Wasyluk et al., 2010]

  * Process discussion emphasizes carbon metastability/supersaturation and that thermal processing can cause clustering/redistribution and possible precipitate formation (not directly observed here), consistent with a thermodynamic driving force that is only realized when kinetics allow. [Hall et al., 2004]

  * This statement was inferred abductively from: (i) the strong empirical emphasis on substitutional Si–C bonding signatures in SiGeC without SiC precipitates in as-grown films (e5.0), (ii) the general materials-chemistry fact that SiC is a robust stable compound in the Si–C system whereas diamond-structured GeC is far less commonly stable under typical semiconductor processing conditions, and (iii) the mission context (external to the listed evidence) that modeling assumes carbon prefers Si neighbors and explores Si-rich shells around SiC inclusions. The provided sources themselves do not quantify C–Si vs C–Ge preference or report shells.

### Predictions

### 3 Likely outcomes

  * If RTCVD Si1-x-yGexCy films (e.g., x≈0.1–0.2, y≈0.5–1.5%) are subjected to an oxidation step versus an inert anneal at comparable peak temperature, then Cs proxies (e.g., 605 cm−1 Si–C local-mode strength per unit total C) will decrease more in the oxidized samples, and SIMS(total C) vs XRD-inferred Cs will diverge more strongly after oxidation than after inert anneal.

  * For as-grown RTCVD Si1-x-yGexCy up to y=1.8%, FTIR will continue to show no ~800 cm−1 SiC band while the Raman ~630 cm−1 satellite/local ratio increases approximately linearly with y (within the same growth window).

  * In Ge1-xCx grown with the Ge4C-core precursor, raising substrate temperature beyond the reported roughening/bond-breakage threshold (>~475 °C) will increase the likelihood of carbon clustering signatures (Raman/TEM), consistent with loss of kinetic control.

### 3 Unknown outcomes

  * If a SiGe:C sample is annealed under conditions that intentionally inject interstitials (e.g., oxidation or engineered interstitial injection without oxidation), then APT or STEM-EELS/EDS will reveal nanoscale carbon-rich regions; whether these become crystalline SiC and whether they display a Ge-depleted shell will depend sensitively on x (Ge fraction) and defect flux—this could validate or refute the proposed shell corollary.

  * A controlled experiment holding total C fixed but patterning local Si/Ge ratio (e.g., compositional modulation) will show that precipitation onset correlates more strongly with local Si availability than with global x, implying a local-neighborhood-controlled nucleation barrier rather than a purely bulk-composition criterion.

  * Rapid quench from melt/near-melt conditions (additive-manufacturing-like) could trap non-crystalline ‘carbidic’ clusters whose vibrational signatures fall between substitutional Si–C modes and crystalline SiC; confirming such intermediates would expand the pathway set beyond Cs/Ci/SiC.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * If oxidation steps do not measurably increase Cs loss/redistribution relative to inert anneals (no change in SIMS-vs-XRD/FTIR/Raman Cs proxies), then the ‘defect-injection switch’ mechanism would be undermined.

  * If annealed SiGe:C samples with confirmed SiC precipitates show no preference for Si-rich neighborhoods (e.g., precipitates occur equally in Si-poor regions) and no systematic Ge depletion near inclusions, then the ‘Si-seeking precipitation + shell corollary’ would be weakened.

  * If as-grown RTCVD samples at y≤1.8% show a clear ~800 cm−1 SiC FTIR band under the same nominal growth window, then the kinetic-trapping boundary conditions in this theory are incorrect or incomplete.

### 1 Unaccounted for

  * No quantitative eV-scale energetics are provided in the evidence for (i) C preference for Si vs Ge nearest neighbors or (ii) the free-energy difference between substitutional C in SiGe and C in a SiC precipitate; thus this theory cannot supply the requested numerical preference magnitudes from the provided sources. [Hall et al., 2004] [Wasyluk et al., 2010] [Stephenson et al., 2016]

* * *

**Related Artifacts:**

  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys]

* * *

## Entities

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

[Gas Source Techniques for Molecular Beam Epitaxy of Highly Mismatched Ge Alloys](<https://www.semanticscholar.org/paper/14320628>)

C. Stephenson, Miriam M Gillett-Kunnath, William A. O'Brien et al. | 2016 | [Semantic Scholar](<https://www.semanticscholar.org/paper/14320628>)

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

## Citation

Cite this artifact as `\cite{ast-carbon-2026-10-09}`.
[code] 
    @misc{ast-carbon-2026-10-09,
      title        = {Carbon’s location in SiGe is set by a trade between strain, bonding, and processing kinetics},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/carbons-location-in-sige-is-set-by-a-trade-between-strain-bonding-and-processing.md},
      note         = {asta-artifact id: theory-1},
    }
[/code]

## SiC inclusions change heat flow both by scattering phonons and by changing the nearby alloy composition

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Inclusion scattering strength rises sharply when inclusion size approaches dominant phonon MFPs

A few-nanometer SiC particle is big enough to strongly scatter heat-carrying phonons, so κ can drop a lot and depends on particle size.

**Supporting evidence:**

  * Mission context states that for two 3C-SiC spheres of radius R embedded in Si0.8Ge0.2 at 300 K, a continuum scattering model brackets κ reduction at R=2.0 nm between 40% (density-contrast-only) and 75% (stiffness-contrast-only) relative to the same alloy without the particle (with surrounding composition held equal).

  * Review of SiC nanowires reports strong size dependence of κ and large reductions at nanoscale (e.g., MD/NEMD predicting very low κ for ~4 nm diameter SiC NWs), consistent with strong boundary/interface scattering when dimensions are nanometric. [Li et al., 2021]

### Si-rich/Ge-depleted shells reduce alloy-disorder scattering but add gradient/interface scattering

A Si-rich shell can make the material locally more ‘Si-like’ (less alloy scattering) but also adds extra boundaries; either effect can win.

**Supporting evidence:**

  * Mission context specifies that in control runs carbon prefers Si neighbours, so each particle is placed inside a Si-rich (Ge-free) shell about 7 Å thick, implying a chemically reconstructed region around SiC inclusions is physically plausible/considered in simulations.

  * RTCVD SiGeC spectroscopy shows substitutional C causes pronounced local bond distortions (phonon frequency shifts), indicating that compositional/chemical perturbations at the atomic scale can significantly modify phonon properties; by extension, a reconstructed shell around an inclusion is expected to influence phonon scattering/velocities. [Wasyluk et al., 2010]

  * AM study proposes nanoprecipitates (including SiC) to scatter phonons and improve TE properties, aligning with the idea that inclusions and their surrounding microstructure (grain size/nucleation agents) influence κ, though without quantification. [Baudry et al., 2024]

### Predictions

### 2 Likely outcomes

  * At fixed SiC radius, making the surrounding shell more Si-rich (reducing Ge content) will reduce alloy-disorder scattering in the shell and can partially offset inclusion scattering for short-MFP phonons, producing a smaller κ reduction than a bare inclusion if interfaces are relatively smooth/coherent.

  * If the shell is made compositionally graded rather than abrupt, κ will decrease relative to an abrupt coherent shell at the same average composition because gradient scattering broadens phonon reflection across frequencies.

### 2 Unknown outcomes

  * There exists an optimal shell thickness (order several Å to ~1 nm) that maximizes κ reduction by simultaneously maintaining strong inclusion scattering while avoiding too much 'matrix purification'; beyond this thickness κ reduction weakens.

  * Engineered Ge-enriched shells (opposite of Si-rich) could further reduce κ by increasing alloy disorder near the interface, but may be thermodynamically/kinetically difficult; if achievable, it would outperform Si-rich shells for κ suppression.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * If adding a Ge-free Si-rich shell around SiC inclusions always increases κ relative to a precipitate-free SiGe alloy (rather than sometimes decreasing), then the added-interface/gradient scattering channel is overestimated.

  * If κ reduction is nearly insensitive to inclusion radius in the 1–5 nm range at 300 K, then the assumed MFP-scale matching is wrong for the simulated/experimental conditions.

### 1 Unaccounted for

  * The provided evidence does not include direct measurements/simulations of κ for SiGe with SiC inclusions or with Si-rich shells; thus the theory cannot be numerically calibrated within this dataset. [Baudry et al., 2024] [Hall et al., 2004] [Wasyluk et al., 2010] [Li et al., 2021]

* * *

**Related Artifacts:**

  * [Extraction: Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing]
  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art]

* * *

## Entities

[Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art](<https://www.semanticscholar.org/paper/232358380>)

You-Dong Li, Guilei Wang, Mehdi Akbari-Saatlu et al. | 2021 | Frontiers in Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/232358380>)

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

[Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing](<https://www.semanticscholar.org/paper/273902266>)

M. Baudry, Guillaume Savelli, Guilhem Roux | 2024 | 2024 IEEE 14th International Conference Nanomaterials: Applications & Properties (NAP) | [Semantic Scholar](<https://www.semanticscholar.org/paper/273902266>)

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

## Citation

Cite this artifact as `\cite{ast-sic-2026-10-09-3}`.
[code] 
    @misc{ast-sic-2026-10-09-3,
      title        = {SiC inclusions change heat flow both by scattering phonons and by changing the nearby alloy composition},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/sic-inclusions-change-heat-flow-both-by-scattering-phonons-and-by-changing-the-n.md},
      note         = {asta-artifact id: theory-8},
    }
[/code]

## SiC inclusions lower SiGe thermal conductivity mainly through interface scattering, and Si-rich/Ge-depleted shells can either amplify or partially ‘match’ the interface depending on their stiffness/mass contrast

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Nanoinclusion κ reduction is interface-dominant and sensitive to chemistry, not bracketed by single-contrast continuum bounds

At nanometer sizes, what matters is the real interface, so simple density- or stiffness-only bounds can miss the MD outcome.

**Supporting evidence:**

  * Additive-manufacturing study proposes nanoprecipitates (including SiC) to scatter phonons and lower lattice thermal conductivity, implying a mechanism beyond point-defect scattering and emphasizing precipitate/interface effects. [Baudry et al., 2024]

  * SiC nanowire literature summarized shows strong size/boundary scattering effects leading to large κ reductions at nanoscale dimensions, indicating interfaces/boundaries dominate thermal transport at few-nm scales. [Li et al., 2021]

### Si-rich shell tradeoff law: reduced alloy disorder vs increased inclusion/interface scattering

A Si-rich shell can either help heat flow (less alloy disorder) or hurt it (more interface scattering); which happens depends on shell thickness and particle size.

**Supporting evidence:**

  * No direct shell data are provided in the evidence set; however, the general premise that nanoprecipitates scatter phonons (e3.0) and that boundaries at nanoscale dominate κ (e6.1) supports the competing-mechanisms framing for core–shell regions. [Baudry et al., 2024] [Li et al., 2021]

### Predictions

### 2 Likely outcomes

  * For fixed SiC radius R in SiGe, introducing a thin Si-rich shell will change κ non-monotonically with shell thickness t: small t may increase κ slightly (disorder reduction dominates) but larger t will decrease κ (effective inclusion/interface scattering dominates).

  * Atomistic simulations that explicitly include interfacial mixing/roughness will show κ reductions larger than smooth-interface continuum predictions at R ~ few nm.

### 2 Unknown outcomes

  * A carefully tuned graded shell (continuous SiGe composition gradient) could maximize phonon backscattering over a broader spectrum than a sharp shell, producing κ reductions exceeding both sharp-shell and no-shell cases at the same total Ge content.

  * If SiC inclusions induce local ordering (reduced short-range disorder) in surrounding SiGe, κ could rise locally enough that inclusion-containing material has higher κ than homogeneous alloy at certain x and temperature ranges.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * If MD with explicit interfaces consistently falls strictly within density-only and stiffness-only continuum bounds for R ~2 nm across multiple interface chemistries, the interface-dominant/out-of-bracket claim is undermined.

  * If adding a Si-rich shell always increases κ regardless of t and R (or always decreases), the proposed competition/tradeoff mechanism is incomplete.

### 1 Unaccounted for

  * No direct measurements or simulations of κ for SiGe with embedded SiC precipitates/shells are provided in the evidence set; this theory is mechanistic and awaits quantitative validation. [Baudry et al., 2024] [Li et al., 2021] [Hall et al., 2004] [Wasyluk et al., 2010]

* * *

**Related Artifacts:**

  * [Extraction: Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing]
  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art]

* * *

## Entities

[Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing](<https://www.semanticscholar.org/paper/273902266>)

M. Baudry, Guillaume Savelli, Guilhem Roux | 2024 | 2024 IEEE 14th International Conference Nanomaterials: Applications & Properties (NAP) | [Semantic Scholar](<https://www.semanticscholar.org/paper/273902266>)

[Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art](<https://www.semanticscholar.org/paper/232358380>)

You-Dong Li, Guilei Wang, Mehdi Akbari-Saatlu et al. | 2021 | Frontiers in Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/232358380>)

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

## Citation

Cite this artifact as `\cite{ast-sic-2026-10-09-2}`.
[code] 
    @misc{ast-sic-2026-10-09-2,
      title        = {SiC inclusions lower SiGe thermal conductivity mainly through interface scattering, and Si-rich/Ge-depleted shells can either amplify or partially ‘match’ the interface depending on their stiffness/mass contrast},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/sic-inclusions-lower-sige-thermal-conductivity-mainly-through-interface-scatteri.md},
      note         = {asta-artifact id: theory-6},
    }
[/code]

## SiC nanoparticles lower SiGe heat flow mostly through interface scattering, not just mass contrast

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Nanoinclusion boundary scattering dominates kappa reduction when inclusion radius is comparable to dominant phonon mean free paths

At a few nanometers, SiC particle interfaces scatter heat-carrying phonons so much that thermal conductivity can drop more than simple mass/density arguments predict.

**Supporting evidence:**

  * SiC nanowire review: MD/NEMD and experiments show strong size dependence of SiC nanowire thermal conductivity, attributed to boundary scattering and mean-free-path truncation, supporting the general principle that nanoscale boundaries strongly reduce lattice kappa. [Li et al., 2021]

  * Additive manufacturing study motivation: proposes nanoprecipitates (including SiC) to scatter phonons and lower lattice thermal conductivity in SiGe, consistent with boundary/interface scattering as a dominant lever (qualitative). [Baudry et al., 2024]

### Si-rich / Ge-depleted shells can partially counteract inclusion scattering by reducing alloy disorder and grading impedance

A Si-rich shell can make the matrix around a particle conduct better by removing Ge disorder, but it also changes interface scattering, so the net effect can go either way and depends on shell thickness.

**Supporting evidence:**

  * No direct shell evidence is present in the provided experimental papers; this law is inferred from general alloy-disorder scattering principles plus the mission context that carbon prefers Si neighbors and control runs place particles in Ge-free Si-rich shells.

  * RTCVD SiGeC: carbon incorporation perturbs local bonds and phonon frequencies (Si–Si softening; Si–C hardening), indicating that local chemistry can substantially modify vibrational properties, consistent with shells potentially altering local phonon scattering/impedance. [Wasyluk et al., 2010]

### Predictions

### 2 Likely outcomes

  * For SiGe at 300 K with SiC inclusions of R~2 nm at low volume fraction, atomistic MD will show a kappa reduction substantially larger than a density-contrast-only bound and closer to a stiffness-contrast-including bound, because elastic mismatch and interface disorder dominate scattering at nm scales.

  * Adding a Ge-free Si shell around SiC inclusions will change kappa relative to bare SiGe in a way that depends on shell thickness; thin shells may further reduce kappa (added scattering volume), while intermediate shells may partially recover kappa (reduced alloy disorder near the interface).

### 2 Unknown outcomes

  * Spectral decomposition (e.g., frequency-resolved heat flux in MD) will show that mid-frequency phonons are most strongly suppressed by SiC inclusions, while low-frequency long-MFP modes are partially transmitted if the shell provides impedance grading; verifying this would enable predictive shell engineering.

  * At fixed inclusion size and volume fraction, varying inclusion crystallographic coherency/roughness (coherent vs incoherent interface) will change whether kappa aligns closer to stiffness-contrast or density-contrast bounds; the sign and magnitude could be large.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * If MD shows R~2 nm inclusions reduce kappa only at or below the density-contrast-only bound even with stiff inclusions, then the claim that stiffness mismatch dominates at this scale is incorrect.

  * If adding a Ge-free Si shell always decreases (or always increases) kappa monotonically with thickness across a wide range, then the predicted competing-mechanism/non-monotonic behavior is wrong.

### 1 Unaccounted for

  * The provided evidence set contains no direct thermal conductivity measurements or simulations for SiGe containing SiC precipitates or shells; thus this theory cannot be directly validated against included data and is built from general principles plus qualitative motivation sources. [Baudry et al., 2024] [Hall et al., 2004] [Wasyluk et al., 2010] [Li et al., 2021]

* * *

**Related Artifacts:**

  * [Extraction: Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing]
  * [Extraction: Recent developments in vertical MOSFETs and SiGe HBTs]
  * [Extraction: Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si]
  * [Extraction: Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art]

* * *

## Entities

[Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art](<https://www.semanticscholar.org/paper/232358380>)

You-Dong Li, Guilei Wang, Mehdi Akbari-Saatlu et al. | 2021 | Frontiers in Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/232358380>)

[Innovative Developpement of Silicon Germanium Alloy Enhanced with Nanoprecipitates by Additive Manufacturing](<https://www.semanticscholar.org/paper/273902266>)

M. Baudry, Guillaume Savelli, Guilhem Roux | 2024 | 2024 IEEE 14th International Conference Nanomaterials: Applications & Properties (NAP) | [Semantic Scholar](<https://www.semanticscholar.org/paper/273902266>)

[Raman and Fourier transform infrared study of substitutional carbon incorporation in rapid thermal chemical vapor deposited Si1−x−yGexCy on (1 0 0) Si](<https://www.semanticscholar.org/paper/31806986>)

Joanna Wasyluk, T. Perova, François Meyer | 2010 | [Semantic Scholar](<https://www.semanticscholar.org/paper/31806986>)

[Recent developments in vertical MOSFETs and SiGe HBTs](<https://www.semanticscholar.org/paper/137240377>)

S. Hall, P. Ashburn, O. Buiu et al. | 2004 | Journal of Telecommunications and Information Technology | [Semantic Scholar](<https://www.semanticscholar.org/paper/137240377>)

## Citation

Cite this artifact as `\cite{ast-sic-2026-10-09}`.
[code] 
    @misc{ast-sic-2026-10-09,
      title        = {SiC nanoparticles lower SiGe heat flow mostly through interface scattering, not just mass contrast},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/sic-nanoparticles-lower-sige-heat-flow-mostly-through-interface-scattering-not-j.md},
      note         = {asta-artifact id: theory-2},
    }
[/code]

# Theorizer run `r2b_strained_films` (task d36b67d8-578a-4441-9de7-9c5e5a5a3d48)

Papers extracted (5): Effect of strain on the thermoelectric properties of silicon: an ab initio study; Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.; Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain; Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<; Topological surface phonons modulate thermal transport in semiconductor thin films

## At 50/50 SiGe, alloy disorder dominates; coherent strain only tweaks thermal conductivity (anisotropically)

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Alloy-scattering dominance bounds intrinsic coherent-strain sensitivity of κ near x≈0.5

Near 50/50 SiGe, alloy disorder already limits heat flow, so coherent strain alone usually changes κ by only ~a few to ~10% unless it also creates defects or changes interface/boundary scattering.

**Supporting evidence:**

  * Cheaito et al. model cross-plane κ of epitaxial Si1-xGex thin films using Matthiessen’s rule with an explicit alloy-scattering term τ_α^{-1} ∝ x(1−x)ω^4 and conclude that boundary scattering of long-wavelength phonons dominates thin-film reductions while alloy scattering remains an essential term (especially at higher frequencies). This supports that alloy scattering is a major baseline limiter in SiGe alloys and that additional perturbations (like strain) act on top of an already-strong scattering background. [Cheaito et al., 2012]

  * Cheaito et al. show that in thin films (39–427 nm) κ is already strongly suppressed (≈1.8–2.8 W/m·K for x=0.2) and that dislocation density trends with thickness do not straightforwardly explain κ trends, implying that boundary/alloy scattering dominate; this is consistent with a picture where moderate changes to intrinsic anharmonicity/velocities would yield only modest fractional changes in κ compared with dominant alloy/boundary limits. [Cheaito et al., 2012]

  * Raman/XRD analysis for epitaxial Ge/Si indicates the explicit anharmonic coefficient A3 is only slightly larger in epitaxial Ge/Si than bulk Ge (A3 bulk ≈0.77 cm−1 vs A3 Ge/Si ≈1.0 cm−1) and authors argue A3 is insensitive to large ranges of threading dislocation density and to alloying in related GeSn samples, suggesting that in similar group-IV alloys variations in κ are often more controlled by disorder/defect scattering than by strong shifts in intrinsic anharmonicity parameters. [Corley-Wiciak et al., 2024]

  * The strained-Si electronic-transport paper notes (from literature) that tensile strain can reduce lattice κ by up to ~15% in bulk silicon and silicon thin films, providing a magnitude context that intrinsic strain leverage in a pure crystal is typically O(10%) even at sizeable strains; in a strong-scattering alloy, the fractional leverage is expected to be no larger and often smaller. [Hinsche et al., 2011]

  * The same paper cites Parrish et al. as predicting ~10% κ reduction for bulk Si under 3% isotropic tensile strain, supporting the notion that even fairly large elastic deformations can yield only ~10% κ shifts when no new extrinsic scattering is introduced. [Vega-Flick et al., 2019] [Hinsche et al., 2011]

### Anisotropic sign tendency under coherent biaxial compression on Si(001) for midrange SiGe

With coherent in-plane compression on Si, in-plane κ usually stays the same or rises a bit, while through-thickness κ usually stays the same or drops a bit, making κ more anisotropic.

**Supporting evidence:**

  * The cited tensile-strain literature in the strained-Si electronic study (and its citations) indicates tensile strain reduces κ in Si by up to ~10–15%, commonly attributed to reduced phonon group velocities and/or modified harmonic properties. By inversion, compression tends to increase stiffness/velocities in the compressed directions, motivating Δκ∥≥0 under in-plane compression as a tendency. [Hinsche et al., 2011] [Vega-Flick et al., 2019]

  * Epitaxial Ge/Si Raman/XRD analysis shows biaxial epitaxial constraint produces anisotropic Grüneisen parameters (γ∥ and γ⊥ reported) and modified anharmonic coefficient A3 relative to bulk, demonstrating that coherent biaxial strain can change anharmonic-related parameters and thus scattering in an anisotropic (tetragonal) fashion, supporting the mechanism that κ components can respond differently along ∥ and ⊥. [Corley-Wiciak et al., 2024]

  * The biaxially strained Si thin-film computational study explicitly shows biaxial strain tunes in-plane κ through strain-driven changes in phonon group velocities and lifetimes (via PBTE with third-order IFCs), supporting the general causal link 'biaxial strain → changes in v and τ → changes in κ', even though those results are for ultrathin freestanding films and only in-plane κ. [Su et al., 2025]

  * This law’s directional sign pattern for midrange SiGe under coherent compression is a synthesis/inference combining (i) tensile-strain κ reductions in Si (harmonic softening) and (ii) biaxial strain causing anisotropic phonon-parameter changes (γ, A3) in epitaxial group-IV films; direct SiGe strain-resolved κ data are not present in the provided evidence.

### Predictions

### 3 Likely outcomes

  * H7 prediction (intrinsic lattice κ): For a coherently compressed Si0.5Ge0.5 film on Si(001) (~2% in-plane compression) at 300 K, cross-plane κ decreases relative to relaxed bulk Si0.5Ge0.5 by about 5–12% (nominal −8%); in-plane κ is unchanged to mildly increased (0 to +8%, nominal +3 to +5%).

  * If the same Si0.5Ge0.5 alloy is simulated in a virtual-crystal (mass-disorder removed) but with the same coherent biaxial strain, the magnitude of strain-induced Δκ/κ will increase substantially (because τ becomes controlled more by strain-sensitive anharmonicity rather than alloy disorder).

  * The anisotropy ratio κ∥/κ⊥ increases under coherent biaxial compression on Si(001) for x≈0.5, even if the average κ changes only weakly.

### 2 Unknown outcomes

  * There exists a composition window near x≈0.5 where cross-plane κ shows near-cancellation (|Δκ⊥|<5%) under ~2% coherent compression, while in-plane κ still increases measurably; this would imply unusually strong compensation between v⊥ and τ⊥ changes.

  * If coherent strain biases local chemical environments (strain-coupled SRO) in Si0.5Ge0.5, alloy scattering may become correlation-dependent (deviating from simple x(1−x) scaling), amplifying Δκ/κ beyond the attenuation bound without introducing dislocations.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * In PBTE or spectral MD for coherently strained Si0.5Ge0.5, decompose κ into mode-resolved v^2 and τ: if strain changes τ by factors comparable to or larger than the baseline alloy scattering across heat-carrying modes at 300 K, the attenuation/bound claim is falsified.

  * Prepare coherent vs relaxed Si0.5Ge0.5 samples with comparable thickness and defect densities (confirmed by XRD/TEM): if coherent biaxial strain alone systematically produces >25% changes in intrinsic κ⊥ at 300 K, the bounded-change statement fails.

  * Compute κ for coherent strain but with artificially increased TDD/dislocation density: if κ changes remain small despite strong added defect scattering, then the model’s emphasis on extrinsic scattering as an override is incorrect.

### 1 Unaccounted for

  * No direct strain-dependent κ data for coherently strained Si1-xGex are present in the provided evidence set; the theory relies on inferred scattering hierarchy (alloy/boundary) and strain–phonon-parameter sensitivity from related systems (strained Si, strained Ge). [Cheaito et al., 2012] [Hinsche et al., 2011] [Vega-Flick et al., 2019] [Corley-Wiciak et al., 2024]

* * *

**Related Artifacts:**

  * [Extraction: Effect of strain on the thermoelectric properties of silicon: an ab initio study]
  * [Extraction: Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.]
  * [Extraction: Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain]
  * [Extraction: Topological surface phonons modulate thermal transport in semiconductor thin films]
  * [Extraction: Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<]

* * *

## Entities

[Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.](<https://www.semanticscholar.org/paper/9397977>)

R. Cheaito, J. Duda, T. Beechem et al. | 2012 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/9397977>)

[Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<](<https://www.semanticscholar.org/paper/267413189>)

A. Corley-Wiciak, D. Ryzhak, M. Zoellner et al. | 2024 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/267413189>)

[Effect of strain on the thermoelectric properties of silicon: an ab initio study](<https://www.semanticscholar.org/paper/26897241>)

N. F. Hinsche, I. Mertig, P. Zahn | 2011 | Journal of Physics: Condensed Matter | [Semantic Scholar](<https://www.semanticscholar.org/paper/26897241>)

[Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain](<https://www.semanticscholar.org/paper/119044537>)

A. Vega-Flick, D. Jung, Sheng-Ying Yue et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119044537>)

[Topological surface phonons modulate thermal transport in semiconductor thin films](<https://www.semanticscholar.org/paper/284077394>)

Zhenzhong Su, Shuoran Song, Qi Wang et al. | 2025 | Materials today physics | [Semantic Scholar](<https://www.semanticscholar.org/paper/284077394>)

## Citation

Cite this artifact as `\cite{ast-at-2026-10-09}`.
[code] 
    @misc{ast-at-2026-10-09,
      title        = {At 50/50 SiGe, alloy disorder dominates; coherent strain only tweaks thermal conductivity (anisotropically)},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/at-5050-sige-alloy-disorder-dominates-coherent-strain-only-tweaks-thermal-conduc.md},
      note         = {asta-artifact id: theory-3},
    }
[/code]

## Biaxial strain changes which phonons can scatter, differently in-plane vs cross-plane

**Contents:**

  * 1 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 1 Theory Statements

### Cubic-to-tetragonal symmetry breaking splits modes and alters three-phonon phase space anisotropically

Making the lattice tetragonal by biaxial strain changes which phonons can scatter, and that effect is direction-dependent.

**Supporting evidence:**

  * The biaxially strained Si thin-film PBTE study computes mode-resolved weighted phase space (WPS) and lifetimes and shows that biaxial strain tunes κ through changes in velocities and scattering phase space/lifetimes (even if reported primarily for in-plane κ). [Su et al., 2025]

  * Epitaxial Ge/Si Raman/XRD analysis extracts anisotropic Grüneisen parameters (γ∥, γ⊥) under biaxial constraint, evidencing anisotropic phonon-strain coupling consistent with tetragonal symmetry breaking affecting phonon properties relevant to scattering. [Corley-Wiciak et al., 2024]

### Predictions

### 2 Likely outcomes

  * For coherently strained SiGe, the anisotropy κ∥/κ⊥ will increase with |ε∥| even when the average κ changes weakly, because WPS changes are anisotropic under tetragonal distortion.

  * Mode-resolved PBTE for strained Si0.5Ge0.5 will show larger relative lifetime changes for subsets of acoustic modes with polarization aligned to the strain-relaxed direction (out-of-plane) than for purely in-plane polarized modes.

### 2 Unknown outcomes

  * There exists a strain magnitude at which avoided crossings induced by tetragonal splitting create a sharp change in WPS for a narrow frequency window, producing a nonmonotonic κ⊥(ε∥) even in relatively thick films.

  * In SiGe, tetragonal strain may shift the balance between Normal and Umklapp processes differently for ∥ and ⊥ heat flux, leading to different hydrodynamic-like signatures (second sound windows) in-plane vs cross-plane at intermediate temperatures.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * Compute strained vs unstrained Si0.5Ge0.5 PBTE and explicitly compare WPS(ω) and matrix elements: if WPS changes are negligible while κ anisotropy changes substantially, the phase-space mechanism is insufficient.

  * If κ anisotropy changes track only elastic constants/sound speeds with no additional lifetime anisotropy, then the symmetry-driven scattering-channel reshaping is not a primary mechanism.

### 1 Unaccounted for

  * No direct κ∥ and κ⊥ data under coherent biaxial strain in SiGe are provided; evidence is indirect via Raman-derived parameters in Ge and PBTE thin-film Si results. [Corley-Wiciak et al., 2024] [Su et al., 2025]

* * *

**Related Artifacts:**

  * [Extraction: Topological surface phonons modulate thermal transport in semiconductor thin films]
  * [Extraction: Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<]

* * *

## Entities

[Topological surface phonons modulate thermal transport in semiconductor thin films](<https://www.semanticscholar.org/paper/284077394>)

Zhenzhong Su, Shuoran Song, Qi Wang et al. | 2025 | Materials today physics | [Semantic Scholar](<https://www.semanticscholar.org/paper/284077394>)

[Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<](<https://www.semanticscholar.org/paper/267413189>)

A. Corley-Wiciak, D. Ryzhak, M. Zoellner et al. | 2024 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/267413189>)

## Citation

Cite this artifact as `\cite{ast-biaxial-2026-10-09}`.
[code] 
    @misc{ast-biaxial-2026-10-09,
      title        = {Biaxial strain changes which phonons can scatter, differently in-plane vs cross-plane},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/biaxial-strain-changes-which-phonons-can-scatter-differently-in-plane-vs-cross-p.md},
      note         = {asta-artifact id: theory-4},
    }
[/code]

## Biaxial strain makes phonon speeds and phonon-phonon scattering direction-dependent, creating κ anisotropy

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Tetragonal distortion induces directional sound-speed changes that bias κ|| vs κ⊥

Biaxial strain makes phonon speeds different in-plane vs out-of-plane, so κ becomes anisotropic because κ scales like speed-squared times lifetime.

**Supporting evidence:**

  * The strain state in epitaxial (001) group-IV layers is explicitly described as biaxial/tetragonal distortion under substrate constraint (epilayer thermal expansion anisotropic; a|| constrained). [Corley-Wiciak et al., 2024]

  * Prior isotropic tensile-strain predictions cited in the provided materials attribute κ reductions mainly to reduced phonon group velocities and/or specific heat (harmonic-property changes). [Vega-Flick et al., 2019] [Hinsche et al., 2011]

  * In strained Si thin-film PBTE/HNEMD work, biaxial strain modulates phonon dispersions and group velocities (mode-resolved velocities computed) and tunes in-plane κ, demonstrating that strain-driven dispersion/velocity changes can control κ in group-IV Si systems. [Su et al., 2025]

### Alloy/boundary dominated regimes suppress κ sensitivity to modest anharmonic-parameter shifts

If alloy disorder or film thickness already limits phonon lifetimes, changing intrinsic anharmonicity a bit won’t move κ much; velocities and extrinsic scattering matter more.

**Supporting evidence:**

  * Measured cross-plane κ of epitaxial Si1−xGex films is strongly reduced relative to bulk and is explained by a model dominated by boundary scattering of long-wavelength phonons (τb = d/v) plus alloy scattering (∝ ω^4) and Umklapp; authors conclude boundary scattering dominates reductions in thin films. [Cheaito et al., 2012]

  * Raman/XRD study concludes A3 (anharmonic coefficient) is relatively insensitive to TDD and modest alloying; authors infer disorder/alloy scattering likely dominates κ variations rather than changes in anharmonicity in similar systems. [Corley-Wiciak et al., 2024]

  * Thin-film Si under biaxial strain shows κ tunability linked to strain-modulated surface states/reconstructions, highlighting a special-case mechanism beyond bulk anharmonic renormalization. [Su et al., 2025]

### Predictions

### 2 Likely outcomes

  * For coherently strained Si0.5Ge0.5 on Si(001) (~2% in-plane compression), the cross-plane κ change at 300 K will be modest (within ~±10%) because alloy and film-size scattering dominate, unless strain significantly modifies low-frequency acoustic dispersion; κ anisotropy (κ|| ≠ κ⊥) will increase relative to relaxed bulk.

  * In a Debye/RTA fit of strained vs unstrained SiGe film data at fixed thickness, the best-fit change needed to match κ shifts will mainly appear as a change in effective sound speeds (v||, v⊥) rather than large changes in Umklapp prefactors.

### 2 Unknown outcomes

  * At x≈0.5, biaxial strain may push an acoustic-optical avoided crossing to lower frequency, sharply increasing three-phonon phase space and causing an unexpectedly large κ⊥ drop (>15%) even in an alloy-dominated regime.

  * If coherent strain modifies local short-range order tendencies in SiGe (not included in simple alloy models), κ may change more strongly than predicted by purely harmonic anisotropy.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * PBTE with strain-dependent 3rd-order IFCs for Si0.5Ge0.5: if τU changes by >20% at 2% biaxial strain while v changes are small, then the theory’s emphasis on harmonic anisotropy/extrinsic dominance fails for this composition.

  * MD or PBTE separating κ|| and κ⊥: if κ remains isotropic under tetragonal distortion in a defect-free coherent cell, then the claimed inevitable κ anisotropy from v||≠v⊥ is incorrect.

### 1 Unaccounted for

  * No direct experimental κ measurements for coherently strained Ge/Si or GeSn/Ge/Si are provided; evidence links strain to phonon parameter shifts (γ, A3) but not to measured κ. [Corley-Wiciak et al., 2024]

* * *

**Related Artifacts:**

  * [Extraction: Effect of strain on the thermoelectric properties of silicon: an ab initio study]
  * [Extraction: Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.]
  * [Extraction: Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain]
  * [Extraction: Topological surface phonons modulate thermal transport in semiconductor thin films]
  * [Extraction: Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<]

* * *

## Entities

[Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<](<https://www.semanticscholar.org/paper/267413189>)

A. Corley-Wiciak, D. Ryzhak, M. Zoellner et al. | 2024 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/267413189>)

[Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain](<https://www.semanticscholar.org/paper/119044537>)

A. Vega-Flick, D. Jung, Sheng-Ying Yue et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119044537>)

[Effect of strain on the thermoelectric properties of silicon: an ab initio study](<https://www.semanticscholar.org/paper/26897241>)

N. F. Hinsche, I. Mertig, P. Zahn | 2011 | Journal of Physics: Condensed Matter | [Semantic Scholar](<https://www.semanticscholar.org/paper/26897241>)

[Topological surface phonons modulate thermal transport in semiconductor thin films](<https://www.semanticscholar.org/paper/284077394>)

Zhenzhong Su, Shuoran Song, Qi Wang et al. | 2025 | Materials today physics | [Semantic Scholar](<https://www.semanticscholar.org/paper/284077394>)

[Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.](<https://www.semanticscholar.org/paper/9397977>)

R. Cheaito, J. Duda, T. Beechem et al. | 2012 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/9397977>)

## Citation

Cite this artifact as `\cite{ast-biaxial-2026-10-09-2}`.
[code] 
    @misc{ast-biaxial-2026-10-09-2,
      title        = {Biaxial strain makes phonon speeds and phonon-phonon scattering direction-dependent, creating κ anisotropy},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/biaxial-strain-makes-phonon-speeds-and-phonon-phonon-scattering-direction-depend.md},
      note         = {asta-artifact id: theory-5},
    }
[/code]

## Coherent biaxial strain makes thermal conductivity direction-dependent by changing phonon speeds and scattering differently in-plane vs cross-plane

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Coherent biaxial constraint implies tetragonal distortion and potential κ anisotropy

Coherent biaxial strain makes the lattice tetragonal, so phonon speeds (and thus thermal conductivity) can differ in-plane and cross-plane.

**Supporting evidence:**

  * Epitaxial Ge on Si(001) is described as biaxially strained with tetragonal distortion confirmed by high-resolution XRD reciprocal-space maps; the analysis explicitly treats anisotropic (parallel vs perpendicular) thermal expansion under epitaxial constraint. [Corley-Wiciak et al., 2024]

  * Ge1-xSnx layers grown on Ge/Si are likewise treated as tetragonally distorted biaxial epilayers under substrate/buffer constraint; Raman and XRD strains are compared and modeled with an anisotropic epitaxial-constraint framework. [Corley-Wiciak et al., 2024]

  * A computational study applies biaxial in-plane strain to Si thin films and finds strain-tunable in-plane κ with mode-resolved changes in phonon properties, consistent with strain-induced alteration of phonon transport properties under biaxial constraint (though in a freestanding geometry). [Su et al., 2025]

### Directional κ change under biaxial strain is governed by velocity renormalization versus scattering renormalization

Strain changes thermal conductivity by changing phonon speeds and phonon lifetimes; direction-by-direction, whichever changes more determines whether κ goes up or down, and alloy scattering often makes the total change small.

**Supporting evidence:**

  * The strained-Ge epilayer analysis extracts anisotropic Grüneisen parameters (γ∥, γ⊥) and an explicit anharmonic coefficient A3, indicating that epitaxial strain changes phonon frequency–strain response and explicit anharmonic renormalization parameters that would affect three-phonon scattering and thus τ. [Corley-Wiciak et al., 2024]

  * For Ge/Si, A3 is larger in the epitaxial strained layer than in bulk Ge (A3 bulk ≈ 0.77 cm−1; A3 epilayer ≈ 1.0 cm−1), consistent with potentially stronger intrinsic anharmonic effects (shorter τ) in strained material, all else equal. [Corley-Wiciak et al., 2024]

  * For GeSn epilayers, fitted γ values are similar (≈1.3) and A3 shows little dependence on composition and threading dislocation density, supporting the notion that changes in κ across similar alloys are more governed by disorder scattering than by large changes in intrinsic anharmonicity parameters. [Corley-Wiciak et al., 2024]

  * The electronic-transport paper cites prior computational literature that tensile strain reduces κ in bulk Si (e.g., ~10% reduction at 3% isotropic tensile strain) and attributes reductions to reduced phonon group velocities and/or specific heat—consistent with the velocity/lifetime decomposition framework. [Vega-Flick et al., 2019] [Hinsche et al., 2011]

  * The biaxially strained Si thin-film computational study explicitly computes mode-resolved group velocities and lifetimes and shows κ is strain-tunable, directly supporting the principle that κ changes can be decomposed into v and τ changes under biaxial strain (though for freestanding thin films). [Su et al., 2025]

  * Cheaito et al. show that in SiGe thin films, boundary scattering can dominate low-frequency heat-carrying phonons (size effects) and alloy scattering dominates high frequencies; this supports the special case that when extrinsic/boundary/alloy scattering caps τ, additional intrinsic strain-induced τ changes will have muted impact on κ magnitude. [Cheaito et al., 2012]

  * This law/statement was logically inferred by combining the standard kinetic form κ ~ Σ C v^2 τ with evidence that (i) strain modifies phonon parameters linked to anharmonicity (γ, A3) and (ii) literature attributes strain effects to group-velocity/specific-heat changes; the directional form under biaxial strain is an anisotropic extension of these elements.

### Predictions

### 3 Likely outcomes

  * For coherently compressed Si0.5Ge0.5 on Si(001) at 300 K, κ⊥ (cross-plane) will fall slightly relative to relaxed bulk (category: decrease), with a likely magnitude of ~5–12% decrease, while κ∥ increases modestly (few to ~10%) due to in-plane stiffening.

  * For coherently strained Ge on Si(001), if one could isolate an otherwise defect-free epilayer, an increased A3 relative to bulk would correlate with reduced intrinsic τ and thus reduced κ compared with unstrained bulk at the same T, despite any stiffness-related v increases.

  * In SiGe films where thickness/boundary scattering is already the shortest scattering time (as in Cheaito’s thin films), imposing additional coherent biaxial strain will change κ less (smaller |Δκ|) than in thicker, bulk-like samples at the same composition.

### 2 Unknown outcomes

  * A sign change with temperature for κ⊥ under coherent compression near x≈0.5: κ⊥ may decrease at 300 K but show weaker decrease or even slight increase at cryogenic temperatures if intrinsic three-phonon scattering becomes weak and velocity anisotropy dominates over strain-modified anharmonicity.

  * At sufficiently large coherent biaxial strain (few percent) in SiGe, tetragonal splitting could nonlinearly increase three-phonon phase space for particular cross-plane polarized modes, producing a larger κ anisotropy than predicted by linear-elastic velocity changes alone.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * Perform spectral (mode-resolved) analysis for coherently strained Si0.5Ge0.5 and test whether strain changes (i) v∥ vs v⊥ and/or (ii) τ in a directionally correlated way; if neither v nor τ show meaningful anisotropy but κ does, the mechanism assignment is incomplete.

  * Compare a coherently strained film to a plastically relaxed film of the same composition and thickness: if both show the same κ anisotropy, then coherence-induced tetragonal distortion is not the dominant cause (microstructure/interface effects would be implicated).

  * In an alloy composition where τ is known to be alloy-scattering-limited, measure Δκ under strain; if Δκ is as large as in pure Si/Ge under comparable strain, then the 'alloy-scattering mutes strain response' component is falsified.

### 1 Unaccounted for

  * Direct measurements or simulations of κ∥ and κ⊥ in coherently strained Si1-xGex (especially x=0.5) are not present in the provided evidence; therefore, magnitude calibration for the predicted percent changes remains uncertain.

* * *

**Related Artifacts:**

  * [Extraction: Effect of strain on the thermoelectric properties of silicon: an ab initio study]
  * [Extraction: Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.]
  * [Extraction: Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain]
  * [Extraction: Topological surface phonons modulate thermal transport in semiconductor thin films]
  * [Extraction: Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<]

* * *

## Entities

[Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<](<https://www.semanticscholar.org/paper/267413189>)

A. Corley-Wiciak, D. Ryzhak, M. Zoellner et al. | 2024 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/267413189>)

[Topological surface phonons modulate thermal transport in semiconductor thin films](<https://www.semanticscholar.org/paper/284077394>)

Zhenzhong Su, Shuoran Song, Qi Wang et al. | 2025 | Materials today physics | [Semantic Scholar](<https://www.semanticscholar.org/paper/284077394>)

[Reduced thermal conductivity of epitaxial GaAs on Si due to symmetry-breaking biaxial strain](<https://www.semanticscholar.org/paper/119044537>)

A. Vega-Flick, D. Jung, Sheng-Ying Yue et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119044537>)

[Effect of strain on the thermoelectric properties of silicon: an ab initio study](<https://www.semanticscholar.org/paper/26897241>)

N. F. Hinsche, I. Mertig, P. Zahn | 2011 | Journal of Physics: Condensed Matter | [Semantic Scholar](<https://www.semanticscholar.org/paper/26897241>)

[Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.](<https://www.semanticscholar.org/paper/9397977>)

R. Cheaito, J. Duda, T. Beechem et al. | 2012 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/9397977>)

## Citation

Cite this artifact as `\cite{ast-coherent-2026-10-09}`.
[code] 
    @misc{ast-coherent-2026-10-09,
      title        = {Coherent biaxial strain makes thermal conductivity direction-dependent by changing phonon speeds and scattering differently in-plane vs cross-plane},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/coherent-biaxial-strain-makes-thermal-conductivity-direction-dependent-by-changi.md},
      note         = {asta-artifact id: theory-1},
    }
[/code]

## In SiGe alloys, strain tweaks phonons but alloy/boundary scattering sets the baseline

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Matthiessen-limited strain leverage on κ in alloy/thin-film regime

When alloy and boundary scattering already dominate, strain can only change thermal conductivity a little because lifetimes are already short.

**Supporting evidence:**

  * Cheaito et al. model Si1-xGex thin films with Matthiessen’s rule combining Umklapp, alloy scattering τ_α = [x(1-x)A ω^4]^{-1}, and boundary scattering τ_b = d/v, and conclude boundary scattering of long-wavelength phonons dominates κ reductions in thin films; alloy scattering dominates at high frequencies. [Cheaito et al., 2012]

  * Cheaito et al. measure very low cross-plane κ in SiGe thin films (e.g., ~1.8–2.8 W/m-K for Si0.8Ge0.2 across 39–427 nm), illustrating that κ is already strongly suppressed by alloying/size compared with bulk, implying limited headroom for additional modest strain effects. [Cheaito et al., 2012]

  * Raman/XRD analysis of GeSn indicates A3 and γ show little dependence on composition or threading dislocation density in the studied range, supporting the idea that disorder/alloy scattering dominates κ variations rather than large strain-induced changes to intrinsic anharmonicity parameters. [Corley-Wiciak et al., 2024]

### Thickness control can mask strain dependence in cross-plane κ measurements

If thickness is the main limiter of cross-plane heat flow, strain won’t change the measured cross-plane κ very much.

**Supporting evidence:**

  * Cheaito et al. conclude boundary scattering of long-wavelength phonons dominates κ reductions in epitaxial SiGe thin films; their spectral analysis indicates τ_b is the shortest (limiting) for modes carrying most heat in the thinnest films. [Cheaito et al., 2012]

  * Cheaito et al. compare thin-film alloys and superlattices and argue total sample thickness controls κ similarly, consistent with size-limited scattering of long-wavelength phonons dominating over other mechanisms in many thin samples. [Cheaito et al., 2012]

### Predictions

### 3 Likely outcomes

  * For Si0.5Ge0.5 films where alloy scattering dominates, coherent biaxial strain of ~2% will change κ by at most low-teens percent at 300 K, even if anisotropic (κ∥ and κ⊥ can shift in opposite directions).

  * If two SiGe films have the same thickness and composition but different coherent strain states (within the elastic stability range) and remain dislocation-free, κ differences will be smaller than differences caused by changing thickness by a factor of ~2 in the size-limited regime.

  * In TDTR-style cross-plane measurements, the strain dependence of extracted κ⊥ will be weakest in the thinnest films (tens of nm), where τ_b dominates.

### 2 Unknown outcomes

  * In mid-alloy SiGe, sufficiently large coherent strain might shift the dominant heat-carrying spectrum toward frequencies where alloy scattering is weaker/stronger, producing a non-intuitive strain dependence (including potential nonmonotonic κ vs strain).

  * If coherent strain significantly changes the acoustic–optical gap in SiGe alloys, it could alter the relative importance of Umklapp channels and amplify strain effects beyond the Matthiessen-limited expectation.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * If a mid-alloy SiGe film (x≈0.5) with strong alloy scattering exhibits a >30% κ change under modest coherent strain without introducing dislocations, this theory’s 'limited leverage' claim is falsified.

  * If thinning a SiGe film does not reduce κ in the manner predicted by τ_b ≈ d/v dominance (holding composition constant), then the assumed dominance of boundary scattering for long-wavelength phonons is incorrect for that system.

  * If mode-resolved analysis shows τ_U dominates over τ_alloy for the heat-carrying spectrum at x≈0.5 and 300 K, then intrinsic strain-induced changes to τ_U could be large and this theory’s hierarchy would not apply.

### 1 Unaccounted for

  * The provided evidence does not include any direct strained/coherent Si0.5Ge0.5 κ data (in-plane or cross-plane) to numerically validate the magnitude bounds suggested here.

* * *

**Related Artifacts:**

  * [Extraction: Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.]
  * [Extraction: Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<]

* * *

## Entities

[Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.](<https://www.semanticscholar.org/paper/9397977>)

R. Cheaito, J. Duda, T. Beechem et al. | 2012 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/9397977>)

[Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<](<https://www.semanticscholar.org/paper/267413189>)

A. Corley-Wiciak, D. Ryzhak, M. Zoellner et al. | 2024 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/267413189>)

## Citation

Cite this artifact as `\cite{ast-sige-2026-10-09}`.
[code] 
    @misc{ast-sige-2026-10-09,
      title        = {In SiGe alloys, strain tweaks phonons but alloy/boundary scattering sets the baseline},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/in-sige-alloys-strain-tweaks-phonons-but-alloyboundary-scattering-sets-the-basel.md},
      note         = {asta-artifact id: theory-2},
    }
[/code]

## In thin SiGe films, boundary and alloy scattering choose the heat-carrying modes; strain matters mostly by shifting those modes

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Boundary filtering sets a strain-sensitive spectral window for κ in thin SiGe

Thickness pushes heat conduction to different phonon frequencies; strain matters most when those frequencies sit near where scattering mechanisms switch dominance.

**Supporting evidence:**

  * Cheaito et al. model uses τb=d/v and concludes boundary scattering of long-wavelength phonons dominates κ reduction in thin SiGe films; spectral integrand peak shifts with thickness (lower frequency for thicker films, higher frequency for thinner films). [Cheaito et al., 2012]

### Alloy scattering attenuates strain-driven κ changes at x≈0.5 by shortening τ across much of the spectrum

At around 50% alloying, disorder scattering is so strong that small strain effects are usually muted, except possibly for the very low-frequency modes.

**Supporting evidence:**

  * Cheaito et al. explicitly includes alloy scattering τa=[x(1−x)Aω^4]−1 in a Matthiessen model and finds thin-film κ is only weakly dependent on composition across broad x ranges compared to bulk, consistent with strong extrinsic limitations. [Cheaito et al., 2012]

  * Ge/Si and GeSn/Ge/Si Raman/XRD analysis suggests thermal-conductivity variations in similar alloys are more controlled by alloy/disorder scattering than by changes in anharmonic coefficient A3. [Corley-Wiciak et al., 2024]

### Predictions

### 2 Likely outcomes

  * If the same Si0.5Ge0.5 film is simulated at multiple thicknesses under the same coherent biaxial strain, the percent change in κ with strain will be thickness-dependent, peaking at an intermediate thickness where the κ integrand peak lies near the boundary/alloy crossover.

  * For a fixed thickness, strain will change κ more at lower temperatures (e.g., 150–250 K) than at 300–400 K if boundary filtering makes the contribution more sensitive to small dispersion shifts (while Umklapp grows at high T).

### 2 Unknown outcomes

  * A small strain (≈2%) could shift the spectral peak enough to change which branch dominates (LA vs TA) in the filtered spectrum, flipping the sign of the strain-induced κ change as thickness varies.

  * If coherent strain modifies phonon localization tendencies in random SiGe (e.g., via strain-induced force-constant disorder amplification), κ could drop sharply beyond what ω^4 alloy scattering predicts.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * Mode-resolved PBTE for strained/unstrained Si0.5Ge0.5 at fixed thickness: if the κ spectral integrand peak does not shift with thickness as in Cheaito-like trends, the boundary-filtering premise is wrong for the simulation conditions/potential.

  * If κ strain sensitivity is independent of thickness over a wide thickness range, the proposed crossover-controlled sensitivity mechanism is falsified.

### 1 Unaccounted for

  * The evidence base does not contain direct measurements/simulations of strain-dependent κ in SiGe alloys; it only contains unstrained thin-film κ and strain-sensitive phonon parameters in Ge/GeSn. [Cheaito et al., 2012] [Corley-Wiciak et al., 2024]

* * *

**Related Artifacts:**

  * [Extraction: Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.]
  * [Extraction: Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<]

* * *

## Entities

[Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.](<https://www.semanticscholar.org/paper/9397977>)

R. Cheaito, J. Duda, T. Beechem et al. | 2012 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/9397977>)

[Thermal expansion and temperature dependence of Raman modes in epitaxial layers of Ge and <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mrow><mml:msub><mml:mi>Ge</mml:mi><mml:mrow><mml:mn>1</mml:mn><mml:mtext>−</mml:mtext><mml:mi>x</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mi>Sn<](<https://www.semanticscholar.org/paper/267413189>)

A. Corley-Wiciak, D. Ryzhak, M. Zoellner et al. | 2024 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/267413189>)

## Citation

Cite this artifact as `\cite{ast-thin-2026-10-09}`.
[code] 
    @misc{ast-thin-2026-10-09,
      title        = {In thin SiGe films, boundary and alloy scattering choose the heat-carrying modes; strain matters mostly by shifting those modes},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/in-thin-sige-films-boundary-and-alloy-scattering-choose-the-heat-carrying-modes.md},
      note         = {asta-artifact id: theory-6},
    }
[/code]

## In ultrathin freestanding Si, strain tunes surface phonons that can raise or lower in-plane thermal conductivity nonmonotonically

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Surface-phonon fraction controls strain sensitivity in ultrathin Si

In a few-nanometer Si membrane, surface phonons carry a big share of heat, and strain changes them, so κ can change a lot and not necessarily in one direction.

**Supporting evidence:**

  * Mode-resolved PBTE/HNEMD results for Si thin films show that topological-surface-state-dominated phonons contribute ≥20% for Si(001) films when thickness t < 3.02 nm and ≥30% for Si(111) films when t < 4.5 nm, indicating a large surface-mode fraction in the ultrathin regime. [Su et al., 2025]

  * The same study reports biaxial strain from −3% to +3% tunes in-plane κ and shows nonmonotonic behavior (reported explicitly for Si(111) a-type in strain-dependent plots), attributing strain sensitivity primarily to strain-driven changes in surface reconstruction and corresponding modulation of low-frequency surface phonon states. [Su et al., 2025]

  * Mode-resolved quantities (group velocities, lifetimes, weighted phase space) are computed and presented for ~3 nm films, supporting the premise that certain low-frequency surface-dominated modes can have relatively large group velocities and long lifetimes and thus substantial κ contribution. [Su et al., 2025]

  * The computational setup uses free surfaces in cross-plane direction with reconstructions (not substrate interfaces), consistent with the domain where surface-mode physics can dominate strain response. [Su et al., 2025]

### Nonmonotonic κ(ε) as a diagnostic fingerprint of surface-reconstruction-controlled transport

If κ changes nonmonotonically with strain and depends strongly on surface structure, surface phonons are likely controlling heat flow; if not, bulk-like phonons and other scattering dominate.

**Supporting evidence:**

  * The thin-film Si study explicitly attributes strain sensitivity primarily to strain-driven changes in surface reconstruction and modulation of low-frequency surface phonon states rather than a simple bulk stiffening/softening picture. [Su et al., 2025]

  * Observed strain dependence includes nonmonotonic behavior of surface-mode contribution (reported for Si(111) as strain varies −3% to +3%), consistent with using nonmonotonicity as a fingerprint of reconstruction-controlled transport. [Su et al., 2025]

  * The study provides mode-resolved group velocities/lifetimes/WPS, supporting the mechanism that strain can change scattering phase space and modal participation rather than only changing an average sound speed. [Su et al., 2025]

### Predictions

### 3 Likely outcomes

  * Capping an ultrathin (≈2–4 nm) strained Si membrane with an amorphous layer or chemically terminating the surface to suppress reconstruction should substantially reduce both (i) the magnitude of strain tunability of in-plane κ and (ii) any nonmonotonic κ(ε) behavior; κ(ε) should become more monotonic and weaker.

  * At fixed thickness in the ultrathin regime, surfaces/orientations with larger reported surface-mode κ fractions (e.g., Si(111) vs some Si(001) cases in the cited study) should exhibit larger strain tunability and a higher likelihood of nonmonotonic κ(ε) under similar biaxial strain sweeps.

  * In simulations, if surface reconstruction is artificially constrained (atoms fixed to an unstrained reconstructed pattern while applying strain), the strain dependence of κ should be reduced compared to fully relaxed surfaces, indicating reconstruction as the primary mediator.

### 2 Unknown outcomes

  * A substrate-supported but ultrathin Si film with one free reconstructed top surface and one clamped bottom interface could show a mixed response: nonmonotonic strain dependence in in-plane κ from the free surface, but reduced amplitude compared to a fully freestanding membrane; the sign and strength would depend sensitively on interface bonding and whether the substrate damps surface-localized modes.

  * In SiGe ultrathin membranes (few nm) with free surfaces, there may be a crossover where alloy disorder suppresses surface-mode channeling enough that κ(ε) becomes monotonic; identifying the critical Ge fraction for this crossover could reveal an interaction between surface-mode physics and mass-disorder scattering.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * If a 2–3 nm freestanding Si membrane with reconstructed surfaces shows strictly monotonic in-plane κ versus biaxial strain over −3% to +3% and negligible dependence on surface termination/reconstruction, then the proposed surface-reconstruction control mechanism is incomplete or not dominant.

  * If mode-resolved decomposition in the ultrathin regime finds surface-localized/topological-surface-state-dominated modes contribute <5% of in-plane κ (contradicting the reported order-tens-of-percent), then the central premise of surface-mode channeling fails for that system/conditions.

  * If modifying surface reconstruction (e.g., by controlled passivation) changes κ at zero strain but does not change κ(ε) trends, then nonmonotonic strain dependence would require an alternative mechanism (e.g., purely bulk-like dispersion/lifetime changes).

### 2 Unaccounted for

  * This theory does not address cross-plane thermal conductivity or strain response in thick, substrate-clamped epitaxial SiGe films (e.g., Si0.5Ge0.5 coherently grown on Si) where alloy scattering and epitaxial constraint dominate; it is intentionally specialized to freestanding/free-surface ultrathin Si membranes.

  * Through-thickness TDTR data on epitaxial Si1-xGex films emphasizing boundary scattering and thickness effects (rather than explicit strain effects) are outside this theory’s scope. [Cheaito et al., 2012]

* * *

**Related Artifacts:**

  * [Extraction: Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.]
  * [Extraction: Topological surface phonons modulate thermal transport in semiconductor thin films]

* * *

## Entities

[Topological surface phonons modulate thermal transport in semiconductor thin films](<https://www.semanticscholar.org/paper/284077394>)

Zhenzhong Su, Shuoran Song, Qi Wang et al. | 2025 | Materials today physics | [Semantic Scholar](<https://www.semanticscholar.org/paper/284077394>)

[Experimental investigation of size effects on the thermal conductivity of silicon-germanium alloy thin films.](<https://www.semanticscholar.org/paper/9397977>)

R. Cheaito, J. Duda, T. Beechem et al. | 2012 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/9397977>)

## Citation

Cite this artifact as `\cite{ast-ultrathin-2026-10-09}`.
[code] 
    @misc{ast-ultrathin-2026-10-09,
      title        = {In ultrathin freestanding Si, strain tunes surface phonons that can raise or lower in-plane thermal conductivity nonmonotonically},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/in-ultrathin-freestanding-si-strain-tunes-surface-phonons-that-can-raise-or-lowe.md},
      note         = {asta-artifact id: theory-7},
    }
[/code]

# Theorizer run `r2b_potentials` (task 492b3075-2118-4b5b-90d5-8f9dbfa84efe)

Papers extracted (11): A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices; An Iterative Machine Learning Approach for Discovering Unexpected Thermal Conductivity Enhancement in Aperiodic Superlattices; Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches; Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids; First-principles phonon physics using the Pheasy code; Significant reduction of lattice thermal conductivity by the electron-phonon interaction in silicon with high carrier concentrations: a first-principles study.; Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential; Thermal conductivity engineering of bulk and one-dimensional Si-Ge nanoarchitectures; Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction; Transport simulations in hierarchically disordered nanostructures for thermoelectric material design; Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity

## Each method behaves like it adds/removes phonon-scattering channels and reshapes phonons

**Contents:**

  * 3 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 3 Theory Statements

### Effective-scattering-operator decomposition of method bias

Method-to-method κ differences can usually be explained by which scattering mechanisms are included or missing (plus any artificial scattering from the simulation setup).

**Supporting evidence:**

  * First-principles Si PBTE shows adding 4-phonon scattering lowers κ at 300 K by ~8% (3ph-only overestimates); and 4ph importance grows with T, with stated scaling τ_3ph ~ T^-1 and τ_4ph ~ T^-2, producing increasing high-T corrections. [Gu et al., 2020]

  * First-principles Si PBTE (Pheasy+ShengBTE iterative for 3ph; FourPhonon RTA for 4ph) reports κ_3ph(300 K) ≈125.4 W/mK and κ_3+4ph(300 K) ≈115.4 W/mK (7.9% drop), demonstrating an omitted channel changes κ systematically. [Lin et al., 2025]

  * Electron–phonon interaction (EPI) in Si at 300 K can reduce lattice κ by up to ~45% at extreme carrier concentrations (~1e21 cm^-3), showing that adding an additional scattering channel can strongly reduce κ when relevant (doped case). [Liao et al., 2014]

  * Empirical Tersoff-IFCs used in ALD/BTE for bulk diamond Si yield κ_Q(300 K)=305 W/mK versus DFT-PBTE inversion κ(300 K)=147 W/mK, consistent with a method/potential that effectively yields weaker scattering and/or higher velocities (i.e., different effective collision operator/spectrum). [Barbalinardo et al., 2020]

  * A SW force-matched potential used in EMD-GK MD for pristine bulk Si gives κ(300 K)=207±12 W/mK and the authors attribute overprediction vs experimental literature primarily to the potential choice, illustrating method bias due to effective spectrum/scattering differences set by the force field. [Oliveira et al., 2018]

  * First-principles PBTE literature/review emphasizes that empirical potentials can deviate due to dispersion/anharmonicity errors; MD has finite-size issues and classical statistics; PBTE differs by RTA vs iterative solution choices—explicitly linking method discrepancies to spectrum/scattering/operator approximations. [Gu et al., 2020] [Tian et al., 2014] [Puligheddu et al., 2019]

  * Si PBTE direct inversion vs RTA differs by ~5% at 300 K (147 vs 140 W/mK), showing that even within PBTE, solver approximations change the effective collision-operator treatment and κ. [Barbalinardo et al., 2020]

  * ALD/PBTE with DFT forces vs HDNNP forces yields nearly identical κ(300 K) for Si (112.1 vs 110.4 W/mK) within the same PBTE-RTA workflow, indicating that if the force/IFC source preserves the scattering operator and spectrum, κ agreement follows—supporting the MESO focus on operator/spectrum fidelity rather than implementation brand. [Minamitani et al., 2019]

### High-T divergence law: omission of 4ph causes increasing κ overprediction with T

Leaving out four-phonon scattering makes κ too high, and the error grows as temperature increases.

**Supporting evidence:**

  * First-principles Si PBTE study reports τ_3ph ~ T^-1 and τ_4ph ~ T^-2; inclusion of 4ph becomes significant above ~500–700 K and 3ph-only at 900 K gives κ≈43 W/mK and is ~20% larger than measurement, i.e., omission yields growing high-T overprediction. [Gu et al., 2020]

  * Independent first-principles PBTE study shows at 300 K 4ph already reduces κ by ~7.9% (125.4→115.4 W/mK), establishing a nonzero correction that is expected to grow with T. [Lin et al., 2025]

  * Review-level discussion notes four-phonon scattering can be comparable to three-phonon even for low-anharmonicity materials like Si and Ge near/above ΘD, implying increasing relevance at high T and thus growing bias if omitted. [Puligheddu et al., 2019]

### Empirical-force-field bias law: κ inflation via (v, τ) co-bias in bulk Si

If the force field makes phonons too fast or too long-lived (or both), κ comes out too large, sometimes by about a factor of two.

**Supporting evidence:**

  * Tersoff-based ALD/BTE for diamond Si yields κ_Q(300 K)=305 W/mK (and κ_classical=260 W/mK) while DFT-PBTE inversion yields κ_Q,Inv(300 K)=147 W/mK (and DFT classical limit ≈123 W/mK), demonstrating large κ inflation from Tersoff-derived lattice dynamics. [Barbalinardo et al., 2020]

  * Pristine Si EMD-GK using a force-matched SW potential yields κ(300 K)=207±12 W/mK and authors state overprediction vs experimental reference is mainly due to the interatomic potential, supporting the idea that force-field choice changes effective spectrum/scattering and thus κ. [Oliveira et al., 2018]

  * First-principles uncertainty study shows κ(300 K) is strongly sensitive to phonon properties like TA sound speed and Grüneisen parameters (correlations R^2 up to 0.89), consistent with the mechanism that biases in velocities/anharmonicity produce large κ shifts; it also shows XC functional choice shifts κ from ~122 (LDA) to ~171 (BEEF-vdW) W/mK at 300 K for isotopically pure Si (3ph-only), indicating multiplicative sensitivity to spectrum/anharmonicity descriptors. [Parks et al., 2020]

### Predictions

### 3 Likely outcomes

  * For bulk diamond Si at 300 K, a well-converged MD (EMD or homogeneous NEMD with finite-size handled) using Tersoff-1989 will predict κ larger than an ab initio PBTE benchmark that includes at least isotope scattering (and especially if it includes 4ph), with κ_Tersoff/κ_DFT likely >1.3; a factor near ~2 is plausible if the MD result reflects the same Tersoff spectral/anharmonic biases seen in Tersoff-ALD/BTE.

  * For bulk Si at ~1100 K, if the ab initio reference includes 4ph scattering, a Tersoff-1989 MD prediction is likely to be higher by >30% unless NEMD setup artifacts (strong gradients/short length) artificially suppress κ.

  * For Si PBTE workflows, swapping DFT forces for a high-quality surrogate trained to DFT (e.g., HDNNP) while keeping the same ALD/BTE settings will preserve κ(T) within a few percent over the training-valid range (e.g., 200–500 K), as long as the surrogate reproduces both harmonic and cubic IFCs accurately.

### 2 Unknown outcomes

  * In bulk Si1-xGex near x≈0.5 at 300–500 K, the spread between empirical-potential MD and first-principles DFPT+VCA/Tamura PBTE may shrink in relative terms compared to pure Si because alloy disorder dominates scattering; however, if force-constant disorder/localization is strong, explicit-disorder methods (large-supercell QHGK/MD) could predict substantially lower κ than VCA/Tamura PBTE.

  * For Ge, empirical-potential bias sign may be less consistent than for Si because TA branch features are sensitive to force-constant range; potentials that misplace TA(X) could either increase or decrease κ relative to ab initio even if they are reasonable for Si.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * Compute Tersoff-1989 vs DFT mode-resolved group velocities and anharmonic indicators (e.g., Grüneisen parameters or 3ph phase space) for bulk Si; if Tersoff does not systematically increase v and/or increase τ (via reduced anharmonicity) yet still yields much larger κ, then the “(v,τ) co-bias” mechanism is incomplete and implementation/solver effects dominate.

  * Run size- and time-converged EMD and homogeneous NEMD for bulk Si with the same Tersoff-1989 potential; if both converge to κ within ~10–20% of DFT-PBTE (3ph+isotope or 3ph+4ph+isotope), then the theory’s claim that the potential’s effective operator/spectrum is the dominant bias source for Tersoff must be revised (suggesting ALD/BTE extraction or other workflow differences are the main source).

  * For Si PBTE, compare κ from iterative PBTE vs RTA across 200–500 K for the same IFCs; if differences become large (>15–20%) already at 300 K, then MESO must weight solver-induced operator errors more strongly than currently assumed for Si.

### 1 Unaccounted for

  * No direct bulk Tersoff-1989 MD κ values for _bulk_ Si at 300 K and 1100 K are provided in the evidence set; thus quantitative calibration for the specific 'GPUMD homogeneous NEMD' scenario is not directly supported here (only indirect evidence from Tersoff-ALD/BTE and other potentials).

* * *

**Related Artifacts:**

  * [Extraction: Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches]
  * [Extraction: Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids]
  * [Extraction: Significant reduction of lattice thermal conductivity by the electron-phonon interaction in silicon with high carrier concentrations: a first-principles study.]
  * [Extraction: First-principles phonon physics using the Pheasy code]
  * [Extraction: Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity]
  * [Extraction: Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction]
  * [Extraction: A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices]
  * [Extraction: Transport simulations in hierarchically disordered nanostructures for thermoelectric material design]
  * [Extraction: Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential]

* * *

## Entities

[Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction](<https://www.semanticscholar.org/paper/211987717>)

Xiaokun Gu, Shouhang Li, Hua Bao | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/211987717>)

[First-principles phonon physics using the Pheasy code](<https://www.semanticscholar.org/paper/280421449>)

Changpeng Lin, Jian Han, Ben Xu et al. | 2025 | npj Computational Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/280421449>)

[Significant reduction of lattice thermal conductivity by the electron-phonon interaction in silicon with high carrier concentrations: a first-principles study.](<https://www.semanticscholar.org/paper/5754250>)

B. Liao, Bo Qiu, Jia-Wei Zhou et al. | 2014 | Physical Review Letters | [Semantic Scholar](<https://www.semanticscholar.org/paper/5754250>)

[Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids](<https://www.semanticscholar.org/paper/221507928>)

G. Barbalinardo, Zekun Chen, Nicholas W. Lundgren et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/221507928>)

[Transport simulations in hierarchically disordered nanostructures for thermoelectric material design](<https://www.semanticscholar.org/paper/57762337>)

Laura Rita de Sousa Oliveira, Vassillios Vargiamidis, N. Neophytou | 2018 | Nanotechnology Materials and Devices Conference | [Semantic Scholar](<https://www.semanticscholar.org/paper/57762337>)

[A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices](<https://www.semanticscholar.org/paper/111146233>)

Zhiting Tian, Sangyeop Lee, Gang Chen | 2014 | [Semantic Scholar](<https://www.semanticscholar.org/paper/111146233>)

[Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches](<https://www.semanticscholar.org/paper/119231887>)

Marcello Puligheddu, Yi Xia, Maria K. Y. Chan et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119231887>)

[Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential](<https://www.semanticscholar.org/paper/160009739>)

E. Minamitani, Masayoshi Ogura, Satoshi Watanabe | 2019 | Applied Physics Express | [Semantic Scholar](<https://www.semanticscholar.org/paper/160009739>)

[Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity](<https://www.semanticscholar.org/paper/218674110>)

Holden L Parks, Hyun-Young Kim, V. Viswanathan et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/218674110>)

## Citation

Cite this artifact as `\cite{ast-each-2026-10-09}`.
[code] 
    @misc{ast-each-2026-10-09,
      title        = {Each method behaves like it adds/removes phonon-scattering channels and reshapes phonons},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/each-method-behaves-like-it-addsremoves-phonon-scattering-channels-and-reshapes.md},
      note         = {asta-artifact id: theory-1},
    }
[/code]

## For SiGe alloys, how you model disorder dominates the answer

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Long-range randomness can suppress generalized diffusivity far beyond periodic substituted-cell predictions

A truly random alloy can conduct heat far worse than a small repeating ‘ordered alloy pattern’, mainly because long-range randomness destroys how vibrations carry energy across the structure.

**Supporting evidence:**

  * For nominally identical composition Si0.85Ge0.15 (clathrate), a periodically replicated substituted-cell model yields κ≈31 W/mK (QHGK on a 5×5×5 replicated supercell of the 136-atom substituted cell), while a truly random 17000-atom alloy realization yields κ≈1.7 W/mK; the authors attribute the large difference mainly to strong suppression of generalized diffusivity/velocities (especially for <3 THz modes), with DOS and lifetimes not changing comparably. [Barbalinardo et al., 2020]

  * The same study reports that the periodically substituted 15% Ge case has κ≈33 W/mK from BTE-RTA on the 136-atom substituted cell, and κ≈31 W/mK from QHGK on its periodic replica, indicating that the very low κ (1.7 W/mK) is specifically tied to long-range randomness rather than solver choice for the periodic model. [Barbalinardo et al., 2020]

### In strong-disorder alloys, disorder-model uncertainty can exceed solver-choice uncertainty

For strongly alloyed SiGe, whether you model real atomic randomness (and force-constant disorder) matters more than whether you compute κ with GK, NEMD, or BTE.

**Supporting evidence:**

  * A review/discussion of Si/Ge/SiGe methods notes: (i) pure Si and Ge can show consistency between GK-MD and BTE in prior work, but (ii) BTE becomes problematic for Si–Ge alloys, pointing to alloy/disorder treatment—not merely solver choice—as a key divergence source. [Puligheddu et al., 2019]

  * Another review discussion states that empirical-potential NEMD studies can show large discrepancies with experiment for SiGe alloys, while DFPT+VCA/Tamura-type approaches (e.g., Garg et al.) can reproduce experiments, highlighting disorder-model adequacy as a controlling factor in alloys. [Tian et al., 2014] [Kandemir et al., 2017]

  * In explicit-disorder calculations (QHGK) at fixed composition, switching only the disorder realization from periodic substituted to truly random changes κ from ~31 W/mK to ~1.7 W/mK, dwarfing the difference between BTE-RTA and QHGK for the periodic substituted model (~33 vs ~31 W/mK). [Barbalinardo et al., 2020]

  * Classical MD with explicit alloying (Tersoff EMD) reports very strong κ suppression and in some strongly suppressed nanowire/superlattice cases nearly temperature-independent κ over 200–500 K, consistent with a regime where detailed solver refinements are less influential than the presence of strong disorder/interface scattering; while these are nanostructured cases, they illustrate the broader ‘strong scattering reduces solver sensitivity’ mechanism. [Kandemir et al., 2017]

### Predictions

### 2 Likely outcomes

  * For bulk diamond Si1-xGex near x≈0.5, keeping the same interatomic model (e.g., one empirical potential or one DFT/ML force model), κ computed for (i) a periodic small-cell substitution pattern (or its periodic replicas) will exceed κ computed for (ii) a large explicitly random alloy supercell with converged disorder correlations, even when using the same transport solver.

  * If two studies use the same solver (e.g., PBTE-RTA) but one uses VCA+mass-disorder (Tamura/Abeles) and the other uses an explicit-disorder supercell including force-constant disorder, the explicit-disorder result will generally produce lower κ at intermediate compositions, with the largest deviation coming from low-to-mid frequency contributions.

### 2 Unknown outcomes

  * In diamond SiGe, there exists a temperature/composition window where force-constant disorder (beyond mass disorder) changes κ by >2× relative to mass-only models; the window shifts with T because increasing anharmonic broadening partially masks disorder-induced diffusivity suppression.

  * A convergence criterion based on a disorder correlation length (from pair/multisite correlations of alloy configurations) will predict when periodic alloy models approach random-alloy κ; for SiGe at 300 K this length may exceed typical MD-accessible cells, implying many published MD results are effectively ‘short-correlation’ disorder models.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * Compute κ for a sequence of SiGe explicit-alloy models with increasing supercell size and increasingly randomized correlations (e.g., SQS-like to fully random) using identical solver and identical force model; if κ converges quickly to the periodic-substitution value rather than decreasing toward a lower random-alloy value, DRD’s long-range-randomness dominance is weakened for diamond SiGe.

  * For the same harmonic spectrum, compare PBTE(VCA+Tamura mass disorder) to an explicit-disorder PBTE/QHGK that includes force-constant disorder; if they agree closely across x at 300 K (within ~10–20%), then DRD overstates the importance of force-constant/long-range disorder for diamond SiGe (even if it remains true for clathrates).

### 1 Unaccounted for

  * The clearest quantitative evidence for the ‘periodic substituted vs truly random’ order-of-magnitude κ gap is for a SiGe clathrate alloy rather than diamond SiGe; the magnitude of the effect could be smaller in diamond-structure SiGe alloys. [Barbalinardo et al., 2020]

* * *

**Related Artifacts:**

  * [Extraction: Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches]
  * [Extraction: Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids]
  * [Extraction: Thermal conductivity engineering of bulk and one-dimensional Si-Ge nanoarchitectures]
  * [Extraction: A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices]

* * *

## Entities

[Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids](<https://www.semanticscholar.org/paper/221507928>)

G. Barbalinardo, Zekun Chen, Nicholas W. Lundgren et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/221507928>)

[Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches](<https://www.semanticscholar.org/paper/119231887>)

Marcello Puligheddu, Yi Xia, Maria K. Y. Chan et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119231887>)

[A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices](<https://www.semanticscholar.org/paper/111146233>)

Zhiting Tian, Sangyeop Lee, Gang Chen | 2014 | [Semantic Scholar](<https://www.semanticscholar.org/paper/111146233>)

[Thermal conductivity engineering of bulk and one-dimensional Si-Ge nanoarchitectures](<https://www.semanticscholar.org/paper/5718073>)

A. Kandemir, Ayberk Ozden, T. Çagin et al. | 2017 | Science and Technology of Advanced Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/5718073>)

## Citation

Cite this artifact as `\cite{ast-sige-2026-10-09}`.
[code] 
    @misc{ast-sige-2026-10-09,
      title        = {For SiGe alloys, how you model disorder dominates the answer},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/for-sige-alloys-how-you-model-disorder-dominates-the-answer.md},
      note         = {asta-artifact id: theory-3},
    }
[/code]

## Some DFT-based BTE workflows can predict too-low κ because of solver and convergence choices

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### SMRTA/RTA bias: κ_RTA ≤ κ_iter/inv, with a temperature-dependent gap

Using RTA instead of a full PBTE solution usually makes κ a bit too small; the difference is small near room temperature for Si but gets larger at lower temperatures.

**Supporting evidence:**

  * For bulk diamond Si at 300 K, a DFT PBTE calculation reports κ_Q,Inv = 147 W/mK (direct inversion with quantum statistics) and κ_Q,RTA = 140 W/mK, i.e., RTA is ~5% lower than inversion at the same IFC level. [Barbalinardo et al., 2020]

  * A separate first-principles Si study (including 3ph, 4ph, isotopes) states that prior literature indicates the iterative vs RTA difference is <4% for Si at room temperature (consistent with a modest systematic underestimation from RTA near 300 K). [Gu et al., 2020]

  * A review of first-principles PBTE notes that iterative solutions can differ from RTA and that RTA neglect of coupling between modes can cause quantitative differences; this frames the mechanism as general across PBTE implementations. [Tian et al., 2014]

### Finite-displacement IFC range/supercell inadequacy can bias κ downward via dispersion and scattering errors

If the force-constant supercell or cutoff is too small, the phonon dispersion and scattering will be wrong and κ often comes out too low.

**Supporting evidence:**

  * A phono3py PBTE study explicitly reports that small IFC supercell sizes can underestimate κ (discussed for GaN: using a 32-atom cell vs 108-atom in a prior study, with underestimation attributed to supercell size). This provides direct evidence that IFC supercell inadequacy can depress κ in finite-displacement PBTE workflows. [Minamitani et al., 2019]

  * Uncertainty-quantification work notes that predicting TA branch frequencies near the X-point is challenging for both Si and Ge and that the discrepancy has been ascribed to the number of neighbor shells included in harmonic force-constant calculations—linking IFC range/cutoff choices mechanistically to dispersion errors that can shift κ. [Parks et al., 2020]

  * A first-principles uncertainty study for isotopically pure Si shows κ at 300 K depends strongly on DFT functional and correlates with TA[100] sound speed and TA X-point frequency (R^2=0.77 for TA X-point frequency correlation), supporting the claim that errors in TA-branch characteristics (which can arise from underconverged IFC range) propagate into κ variability. [Parks et al., 2020]

  * A first-principles PBTE study for Si emphasizes careful convergence practices (large supercells, q-grids up to 30x30x30) and highlights that insufficient convergence (supercell/q-grid) can affect κ; while not isolating supercell-size error numerically for Si, it supports the general necessity of converged IFC extraction to avoid κ bias. [Lin et al., 2025]

### Predictions

### 3 Likely outcomes

  * For bulk Si near 300 K, a PBTE workflow that switches from SMRTA/RTA to iterative or direct inversion while holding the same IFCs fixed will increase κ by a few percent (order 3–6%), consistent with the 147 vs 140 W/mK evidence gap.

  * At temperatures below ~200 K in high-purity bulk Si (where normal processes are more influential), the relative increase κ_iter/inv − κ_RTA will be larger than at 300 K (directionally: RTA becomes progressively less accurate).

  * If two DFT-PBTE workflows differ mainly by underconverged IFC real-space range (smaller supercells/cutoffs) versus converged IFC range, the underconverged workflow will tend to predict lower κ for Si/Ge, with the discrepancy correlating with errors in TA branch features (e.g., TA X-point frequency).

### 2 Unknown outcomes

  * For bulk Ge, correcting harmonic IFC range (more neighbor shells / larger supercell) will change κ more strongly than for Si (because of potentially greater TA-edge sensitivity), possibly changing the ordering of which DFT functional appears 'best' against experiment once convergence is enforced.

  * In explicit-supercell PBTE modeling of Si1-xGex (not VCA), insufficient supercell size will not only depress κ but also alter the apparent composition dependence by artificially suppressing long-wavelength contributions, potentially shifting the κ(x) minimum away from x≈0.5 in a size-dependent way.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * For a fixed bulk-Si DFT IFC set, compute κ(T) using both SMRTA/RTA and direct inversion/iterative PBTE across a temperature sweep. If κ_RTA exceeds κ_iter/inv at any temperature with identical inputs, the assumed systematic directionality (RTA underestimation) would be called into question (suggesting inconsistent scattering implementation or numerical issues).

  * Within a finite-displacement PBTE workflow for Si or Ge, vary harmonic/anharmonic IFC supercell sizes and neighbor cutoffs while keeping q-mesh convergence tight. If κ is invariant within ~1% across these changes and TA(X) frequencies are also stable, the proposed IFC-range-driven κ underestimation mechanism is likely negligible for that workflow/material.

### 1 Unaccounted for

  * No provided evidence gives a direct numerical example (for bulk Si or Ge) where a too-small IFC supercell quantitatively lowers κ; the explicit documented magnitude example is for GaN, so the size of this bias for Si/Ge remains uncertain from the current evidence set. [Minamitani et al., 2019]

* * *

**Related Artifacts:**

  * [Extraction: Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids]
  * [Extraction: First-principles phonon physics using the Pheasy code]
  * [Extraction: Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity]
  * [Extraction: Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction]
  * [Extraction: A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices]
  * [Extraction: Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential]

* * *

## Entities

[Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids](<https://www.semanticscholar.org/paper/221507928>)

G. Barbalinardo, Zekun Chen, Nicholas W. Lundgren et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/221507928>)

[Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction](<https://www.semanticscholar.org/paper/211987717>)

Xiaokun Gu, Shouhang Li, Hua Bao | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/211987717>)

[A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices](<https://www.semanticscholar.org/paper/111146233>)

Zhiting Tian, Sangyeop Lee, Gang Chen | 2014 | [Semantic Scholar](<https://www.semanticscholar.org/paper/111146233>)

[Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential](<https://www.semanticscholar.org/paper/160009739>)

E. Minamitani, Masayoshi Ogura, Satoshi Watanabe | 2019 | Applied Physics Express | [Semantic Scholar](<https://www.semanticscholar.org/paper/160009739>)

[Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity](<https://www.semanticscholar.org/paper/218674110>)

Holden L Parks, Hyun-Young Kim, V. Viswanathan et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/218674110>)

[First-principles phonon physics using the Pheasy code](<https://www.semanticscholar.org/paper/280421449>)

Changpeng Lin, Jian Han, Ben Xu et al. | 2025 | npj Computational Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/280421449>)

## Citation

Cite this artifact as `\cite{ast-some-2026-10-09}`.
[code] 
    @misc{ast-some-2026-10-09,
      title        = {Some DFT-based BTE workflows can predict too-low κ because of solver and convergence choices},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/some-dft-based-bte-workflows-can-predict-too-low-κ-because-of-solver-and-converg.md},
      note         = {asta-artifact id: theory-5},
    }
[/code]

## Tersoff tends to give too-high thermal conductivity for bulk silicon, and the mismatch tends to worsen at high temperature

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Room-temperature bulk Si: Tersoff IFC-based transport overestimates κ by ~2× vs DFT PBTE (anchor law)

Around 300 K, using Tersoff for bulk silicon tends to give about twice the thermal conductivity that DFT-based BTE gives.

**Supporting evidence:**

  * DFT PBTE (direct inversion, quantum statistics) for diamond Si reports κ(300 K)=147 W/mK; the same study reports Tersoff-based ALD/BTE κ_Q(300 K)=305 W/mK (and κ_classical=260 W/mK), i.e., ≈2.1× higher than DFT inversion at 300 K. [Barbalinardo et al., 2020]

  * The same DFT PBTE study shows RTA vs inversion differences are modest at 300 K (quantum: 140 vs 147 W/mK; ~5%), implying the ≈2× Tersoff-vs-DFT gap is not explainable by RTA vs inversion alone. [Barbalinardo et al., 2020]

  * A separate first-principles PBTE/DFT workflow (phono3py, RTA) gives κ(300 K)=112.1 W/mK for Si, further indicating that first-principles PBTE values cluster far below ~300 W/mK at 300 K; Tersoff ≈305 W/mK is therefore an outlier high relative to multiple DFT-based PBTE pipelines. [Minamitani et al., 2019]

  * Another first-principles PBTE/DFT study for bulk Si (iterative 3ph with isotopes; optional 4ph) reports κ_3ph(300 K)≈125.4 W/mK and κ_3+4ph(300 K)≈115.4 W/mK, again far below ~300 W/mK and consistent with Tersoff-based transport being high relative to DFT-based transport at 300 K. [Lin et al., 2025]

  * A first-principles uncertainty-quantification study reports a range of DFT-PBTE κ(300 K) values depending on XC functional (e.g., PBE 154, PBEsol 128, LDA 122 W/mK; BEEF-vdW best-fit 171 W/mK for isotopically pure Si with only 3ph). Even the high end of these DFT predictions is well below 260–305 W/mK from Tersoff transport, supporting the conclusion that Tersoff is systematically high at 300 K versus DFT PBTE. [Parks et al., 2020]

### High-temperature amplification: 4-phonon-aware DFT references reduce κ faster with T than Tersoff-1989 is expected to (categorical forecast at ~1100 K)

At ~1100 K, a DFT reference that includes four-phonon scattering drops κ strongly; Tersoff-1989 MD is therefore expected to come out noticeably higher (often >30% higher) unless the NEMD setup artificially lowers κ.

**Supporting evidence:**

  * A first-principles Si study spanning 100–1500 K reports that omitting 4ph overestimates κ by ~8% at 300 K and that 4ph becomes increasingly important above ~500–700 K; at 900 K, 3ph-only κ is reported as 43 W/mK and is ~20% larger than measurement, implying that 4ph-inclusive κ is substantially lower at high T than 3ph-only. [Gu et al., 2020]

  * The same first-principles high-T study states (as a mechanistic scaling rule) that 3ph lifetimes scale roughly ~T^-1 while 4ph lifetimes scale roughly ~T^-2, indicating an accelerating relative importance of 4ph with increasing temperature. [Gu et al., 2020]

  * Independent first-principles PBTE for Si at 300 K shows 4ph reduces κ from ~125.4 to ~115.4 W/mK (~7.9%), consistent with the claim that 4ph corrections are non-negligible already at 300 K and grow with T. [Lin et al., 2025]

  * Tersoff-based ALD/BTE for diamond Si at 300 K strongly overpredicts κ relative to DFT inversion (305 vs 147 W/mK), supporting the premise that the potential can yield insufficient effective resistive scattering and/or inflated transport quantities; this provides the abductive anchor that the bias remains upward unless canceled by NEMD artifacts. [Barbalinardo et al., 2020]

  * General methodological discussion notes empirical-potential MD results can be strongly affected by interatomic potential quality and MD finite-size effects, consistent with the stated caveat that NEMD artifacts can move comparisons toward apparent agreement. [Gu et al., 2020]

  * This statement was logically inferred (abduction) by combining: (i) evidence that Tersoff produces large upward bias at 300 K in bulk Si transport (Tersoff ALD/BTE vs DFT PBTE), and (ii) evidence that DFT PBTE κ decreases more strongly with T when 4ph scattering is included (increasingly important at high T).

### Predictions

### 2 Likely outcomes

  * H5 @300 K: For size-converged bulk Si, κ_Tersoff-1989(homogeneous NEMD)/κ_almaBTE(3ph/4ph+isotopes as implemented) will be >1.0; a plausible prior range is ~1.3–2.1, with the upper end corresponding to the ≈2× Tersoff-vs-DFT transport anchor (305 vs 147 W/mK).

  * H5 @1100 K: If the almaBTE reference includes strong high-T resistive physics (especially 4ph), then the comparison category is most likely “Tersoff higher by more than 30%”, unless NEMD length/gradient artifacts reduce κ_Tersoff.

### 2 Unknown outcomes

  * If a carefully converged homogeneous NEMD calculation with Tersoff-1989 at 1100 K produces κ within 30% of a 4ph-inclusive DFT PBTE reference, it would imply a strong, temperature-dependent cancellation between (i) Tersoff’s intrinsic overconductivity and (ii) NEMD finite-size/nonequilibrium artifacts, suggesting that method agreement can be accidental rather than indicating correct physics.

  * If replacing Tersoff-1989 with a DFT-trained ML potential (or force-matched empirical potential) and then running homogeneous NEMD yields κ close to 4ph-inclusive DFT PBTE at 1100 K, it would support the claim that the dominant error source is the potential’s anharmonic coefficients rather than NEMD methodology itself.

### Conflicting & Unaccounted Evidence

### 3 Negative experiments

  * Perform homogeneous NEMD with Tersoff-1989 for bulk Si at 300 K and 1100 K while systematically increasing sample length and cross-section; if κ converges to within ±30% of the DFT PBTE reference at both temperatures, the claimed intrinsic Tersoff overconductivity prior is weakened.

  * Compute ALD/PBTE for bulk diamond Si using Tersoff-1989 IFCs but compare RTA vs full inversion; if full inversion reduces κ by a factor comparable to the observed ~2× gap to DFT, then solver approximation (not potential) would be the main driver—contradicting the theory’s emphasis on potential-derived scattering/dispersion errors.

  * Extract effective Grüneisen parameters and phonon lifetimes from Tersoff-1989 (via ALD) and from DFT IFCs and test whether Tersoff systematically yields longer lifetimes for heat-carrying acoustic modes; absence of such lifetime inflation would undermine the “underdamped phonon gas” mechanism.

### 2 Unaccounted for

  * No direct bulk diamond Si κ(T) dataset from Tersoff-1989 MD (EMD or homogeneous NEMD) is provided in the evidence; the anchor is Tersoff ALD/BTE at 300 K, not MD, and not specifically labeled as Tersoff-1989 in that source entry. [Barbalinardo et al., 2020]

  * An SW force-matched potential used with EMD-GK for pristine Si yields κ(300 K)=207±12 W/mK, showing that not all empirical potentials underpredict scattering; however, this theory is about Tersoff-1989 specifically and does not model SW behavior. [Oliveira et al., 2018]

* * *

**Related Artifacts:**

  * [Extraction: Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids]
  * [Extraction: First-principles phonon physics using the Pheasy code]
  * [Extraction: Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity]
  * [Extraction: Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction]
  * [Extraction: Transport simulations in hierarchically disordered nanostructures for thermoelectric material design]
  * [Extraction: Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential]

* * *

## Entities

[Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids](<https://www.semanticscholar.org/paper/221507928>)

G. Barbalinardo, Zekun Chen, Nicholas W. Lundgren et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/221507928>)

[Simulating lattice thermal conductivity in semiconducting materials using high-dimensional neural network potential](<https://www.semanticscholar.org/paper/160009739>)

E. Minamitani, Masayoshi Ogura, Satoshi Watanabe | 2019 | Applied Physics Express | [Semantic Scholar](<https://www.semanticscholar.org/paper/160009739>)

[First-principles phonon physics using the Pheasy code](<https://www.semanticscholar.org/paper/280421449>)

Changpeng Lin, Jian Han, Ben Xu et al. | 2025 | npj Computational Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/280421449>)

[Uncertainty quantification in first-principles predictions of phonon properties and lattice thermal conductivity](<https://www.semanticscholar.org/paper/218674110>)

Holden L Parks, Hyun-Young Kim, V. Viswanathan et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/218674110>)

[Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction](<https://www.semanticscholar.org/paper/211987717>)

Xiaokun Gu, Shouhang Li, Hua Bao | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/211987717>)

[Transport simulations in hierarchically disordered nanostructures for thermoelectric material design](<https://www.semanticscholar.org/paper/57762337>)

Laura Rita de Sousa Oliveira, Vassillios Vargiamidis, N. Neophytou | 2018 | Nanotechnology Materials and Devices Conference | [Semantic Scholar](<https://www.semanticscholar.org/paper/57762337>)

[Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches](<https://www.semanticscholar.org/paper/119231887>)

Marcello Puligheddu, Yi Xia, Maria K. Y. Chan et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119231887>)

## Citation

Cite this artifact as `\cite{ast-tersoff-2026-10-09}`.
[code] 
    @misc{ast-tersoff-2026-10-09,
      title        = {Tersoff tends to give too-high thermal conductivity for bulk silicon, and the mismatch tends to worsen at high temperature},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/tersoff-tends-to-give-too-high-thermal-conductivity-for-bulk-silicon-and-the-mis.md},
      note         = {asta-artifact id: theory-4},
    }
[/code]

## κ differences come from phonon spectrum errors and wrong thermal populations

**Contents:**

  * 2 Theory Statements
  * Predictions
  * Conflicting & Unaccounted Evidence

### 2 Theory Statements

### Statistics-convergence law: quantum vs classical κ discrepancy shrinks with T

Classical methods are most wrong at low temperature; they get closer to quantum results at high temperature.

**Supporting evidence:**

  * DFT PBTE study reports κ_Q,Inv(300 K)=147 W/mK and κ_Cl,Inv(300 K)=123 W/mK and notes quantum and classical results converge as T increases (Fig. 2 trend). [Barbalinardo et al., 2020]

  * Review discussion emphasizes classical MD uses equipartition and requires quantum corrections at low T; prior quantum-correction attempts can fail, highlighting a statistics-driven method discrepancy at low T. [Puligheddu et al., 2019] [Tian et al., 2014]

### Solver-fidelity law: RTA underestimates κ relative to inversion/iterative PBTE when mode coupling matters

RTA is usually a little low for Si at room temperature and can be more wrong at low temperature.

**Supporting evidence:**

  * For diamond Si at 300 K, inversion gives 147 W/mK while RTA gives 140 W/mK (~5% lower), demonstrating solver-dependent κ differences in Si. [Barbalinardo et al., 2020]

  * The Si 3ph-only PBTE study notes literature indicating iterative vs RTA differences <4% for Si at room temperature, consistent with modest solver bias at RT. [Gu et al., 2020]

  * For the Si136 clathrate, authors report RTA corrections beyond RTA are <1%, illustrating a boundary condition where RTA error is very small due to collision-operator structure in that material. [Barbalinardo et al., 2020]

### Predictions

### 2 Likely outcomes

  * If a PBTE κ(T) curve for bulk Si is recomputed with inversion/iterative instead of RTA using identical IFCs and scattering mechanisms, κ will increase by only a few percent near 300 K but by a larger fraction at lower T (e.g., <200 K).

  * Two workflows with identical scattering physics but different harmonic dispersion fidelity (e.g., different potentials) will show κ differences that correlate with acoustic sound speeds and TA-branch features (SSC predicts stronger correlation than with details like IFC extraction algorithm).

### 2 Unknown outcomes

  * For Ge, if a potential reproduces acoustic sound speeds but mispredicts TA(X), SSC predicts that κ differences will show up primarily through changes in phase space and lifetimes rather than group-velocity magnitude alone; this could invert the sign of κ bias depending on how phase space shifts.

  * In Si1-xGex, SSC predicts the temperature at which classical and quantum κ converge depends on alloy-induced spectral broadening; strong disorder may make classical MD appear ‘closer’ to quantum PBTE at lower T than in pure Si because high-frequency modes are already suppressed.

### Conflicting & Unaccounted Evidence

### 2 Negative experiments

  * Compare κ(T) from PBTE using DFT IFCs with κ(T) from classical-limit PBTE using the same IFCs; if the difference does not decrease with T, SSC’s statistics-convergence premise is violated for the tested regime.

  * For Si, test whether κ differences across XC functionals correlate with TA sound speed and Grüneisen parameter as reported; if correlations fail in an expanded dataset, SSC’s spectrum-dominance claim needs revision.

### 1 Unaccounted for

  * The provided evidence set includes many nanowire/superlattice κ values dominated by boundary/interface scattering; SSC is formulated for bulk crystalline comparisons and does not attempt to explain these boundary-dominated results. [Kandemir et al., 2017]

* * *

**Related Artifacts:**

  * [Extraction: Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches]
  * [Extraction: Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids]
  * [Extraction: Thermal conductivity engineering of bulk and one-dimensional Si-Ge nanoarchitectures]
  * [Extraction: Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction]
  * [Extraction: A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices]

* * *

## Entities

[Efficient anharmonic lattice dynamics calculations of thermal transport in crystalline and disordered solids](<https://www.semanticscholar.org/paper/221507928>)

G. Barbalinardo, Zekun Chen, Nicholas W. Lundgren et al. | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/221507928>)

[Computational prediction of lattice thermal conductivity: A comparison of molecular dynamics and Boltzmann transport approaches](<https://www.semanticscholar.org/paper/119231887>)

Marcello Puligheddu, Yi Xia, Maria K. Y. Chan et al. | 2019 | PHYSICAL REVIEW MATERIALS | [Semantic Scholar](<https://www.semanticscholar.org/paper/119231887>)

[A Comprehensive Review of Heat Transfer in Thermoelectric Materials and Devices](<https://www.semanticscholar.org/paper/111146233>)

Zhiting Tian, Sangyeop Lee, Gang Chen | 2014 | [Semantic Scholar](<https://www.semanticscholar.org/paper/111146233>)

[Thermal conductivity of intrinsic semiconductor at elevated temperature: role of four-phonon scattering and electronic heat conduction](<https://www.semanticscholar.org/paper/211987717>)

Xiaokun Gu, Shouhang Li, Hua Bao | 2020 | [Semantic Scholar](<https://www.semanticscholar.org/paper/211987717>)

[Thermal conductivity engineering of bulk and one-dimensional Si-Ge nanoarchitectures](<https://www.semanticscholar.org/paper/5718073>)

A. Kandemir, Ayberk Ozden, T. Çagin et al. | 2017 | Science and Technology of Advanced Materials | [Semantic Scholar](<https://www.semanticscholar.org/paper/5718073>)

## Citation

Cite this artifact as `\cite{ast-differences-2026-10-09}`.
[code] 
    @misc{ast-differences-2026-10-09,
      title        = {κ differences come from phonon spectrum errors and wrong thermal populations},
      author       = {{Asta Theorizer}},
      year         = {2026},
      month        = {10},
      howpublished = {Asta Theorizer artifact},
      url          = {theories/κ-differences-come-from-phonon-spectrum-errors-and-wrong-thermal-populations.md},
      note         = {asta-artifact id: theory-2},
    }
[/code]

