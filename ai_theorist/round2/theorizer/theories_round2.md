# Theorizer run `sige_transport` (task a3cdd4bd-d1ed-4fef-9e61-a2450c7263ee)

Papers extracted (5): Diameter dependence of SiGe nanowire thermal conductivity; The best nanoparticle size distribution for minimum thermal conductivity; Mode localization and suppressed heat transport in amorphous alloys; Precise control of thermal conductivity at the nanoscale through individual phonon-scattering barriers.; Si and SiGe Nanowire for Micro-Thermoelectric Generator: A Review of the Current State of the Art


## theory-1: Lowest thermal conductivity comes from scattering that covers both high- and low-frequency phonons

Alloying mostly blocks short-wavelength phonons; larger defects and interfaces mostly block long-wavelength phonons. The lowest heat conduction happens when the microstructure includes both kinds of scattering so that the whole phonon spectrum is impeded.


### Complementary spectral selectivity enables sub-limit kappa in crystalline Si/Ge systems

Alloy disorder and larger features block different phonons; using both can reduce thermal conductivity more than either alone at the same overall composition.

**Supporting evidence:**

- Compositionally modulated Si1-xGex multilayers exhibit cross-plane kappa values below bulk-alloy values and below a thin-film alloy limit; the accompanying first-principles BTE model explicitly decomposes the scattering potential into a mean mass-density profile M(z) (barrier-like, effective for low-frequency/long-MFP modes) plus local random fluctuations ΔM (alloy-like, effective for high-frequency modes), and attributes the enhanced suppression to simultaneous spectral coverage.  [Chen et al., 2013]

- Ge nanodot multilayers in Si reach very low room-temperature cross-plane kappa (~0.9 W/mK) and behave close to a DMM-like diffusive limit; the work interprets transport as ballistic within Si spacers with additive, highly diffusive barrier resistances, consistent with strong suppression of long-MFP/low-frequency carriers by nanodot layers.  [Pernot et al., 2010]

- AGF simulations comparing nanodot-barrier multilayers vs flat Si0.5Ge0.5 alloy barriers find nanodot systems give significantly lower kappa and are closer to DMM than flat barriers; the interpretation is that dot-induced large-scale roughness increases scattering over a wider (especially low-frequency) range than flat disordered barriers.  [Pernot et al., 2010]

- Theory for Si1-xGex nanowires states alloy scattering strongly suppresses high-frequency phonons and leaves low-frequency phonons relatively unaffected, shifting heat to low-frequency long-MFP modes; this explains weaker diameter dependence and stronger length dependence in alloys compared to pure Si, highlighting the need for additional low-frequency suppression mechanisms to further reduce kappa.  [Wang et al., 2010] [Li et al., 2021]

- Nanocrystalline Si and nanocrystalline SiGe (2% Ge) ab-initio-based Monte Carlo modeling shows grain boundaries transmit low-frequency phonons with near-unity transmission below ~2–3 THz while higher-frequency modes are more strongly blocked; this implies GBs alone may not fully suppress the low-frequency band and motivates combining GBs with alloy/defect scattering for broader spectral coverage.  [Yang et al., 2017]

- A first-principles-informed design study for Si with Ge allocated between point defects and nanoparticles (plus optional grain-boundary scattering) shows much lower kappa when multiple scattering channels are combined and tuned to target different spectral regions; the reported strong drop at fixed total Ge fraction when adding nanoparticles (and further with grain boundaries) is consistent with the principle that broader spectral/MFP coverage yields lower kappa than homogeneous alloying alone.  [Zhang et al., 2014]

- In a single-crystal Si0.934Ge0.066 film, DFT-BTE + TTG interpretation emphasizes that alloy disorder shifts heat to longer-MFP modes, making size/geometry suppression of those modes important; this supports the idea that different mechanisms act on different parts of the spectrum and must be treated spectrally (not by a single gray cutoff).  [Huberman et al., 2017]


### Non-Born (T-matrix) heavy/light inclusion asymmetry for low-frequency-dominated transport

Once the remaining heat is mostly carried by low-frequency phonons, heavier nanoparticles can block those phonons more strongly than equally sized lighter nanoparticles, lowering thermal conductivity more.

**Supporting evidence:**

- First-principles iterative BTE + exact atomistic T-matrix scattering for nanoparticles in Si0.5Ge0.5 reports that Ge (heavy) nanoparticles can yield up to ~20% lower kappa than Si (light) nanoparticles at the same size and concentration, and explicitly notes this asymmetry is not captured by the Born approximation (which is symmetric).  [Kundu et al., 2011]


### 3 Likely outcomes

- In crystalline Si-rich SiGe (e.g., x~0.2), adding a small volume fraction of nm-scale inclusions will reduce kappa more if the inclusions are heavier-than-host (Ge-rich) than if they are lighter-than-host (Si-rich), provided the inclusion radius is large enough to exit the Born regime (order ~1–5 nm).
- In compositionally modulated multilayers, deliberately combining a graded mean Ge profile M(z) with residual atomic-scale randomness (not perfectly ordered layers) will yield lower cross-plane kappa than either (i) a perfectly abrupt superlattice with minimal interdiffusion (mostly barrier scattering) or (ii) a homogeneous alloy film (mostly ΔM scattering) at the same average Ge fraction.
- For SiGe nanowires, increasing Ge content from very small x will weaken diameter dependence but strengthen length dependence of kappa as the dominant heat-carrying spectrum shifts to low-frequency long-MFP modes, making suppression depend more on axial length/feature spacing than on diameter alone.


### 2 Unknown outcomes

- A three-way combination in bulk-like crystalline SiGe—(i) intermediate x to maximize alloy suppression of high-frequency modes, (ii) heavy nanoparticles sized to maximize low-frequency scattering, and (iii) grain boundaries engineered for low-frequency transmission loss—could push room-temperature kappa toward ~1 W/mK without amorphization; success depends on whether low-frequency transmission can be sufficiently reduced without creating percolating high-kappa paths.
- In coherently strained, compositionally modulated SiGe multilayers, biaxial strain could shift which frequencies dominate heat conduction (via group-velocity and anharmonicity changes) and therefore alter the optimal modulation length scale needed for spectral coverage; the direction/magnitude is uncertain without explicit strain-renormalized phonons.


### 3 Negative experiments

- Construct two samples with identical average Ge fraction and identical mesoscale feature density, but one with (near) perfect ordering (minimal ΔM) and one with strong local randomness (large ΔM). If the more random sample does not show lower kappa (after controlling for porosity/defects), the claimed complementarity of ΔM with mesoscale scattering is weakened.
- Compare heavy vs light nanoparticle inclusions of identical radius and volume fraction in a regime where nm-scale inclusions should be non-Born. If the kappa reductions are equal within uncertainty, the heavy/light asymmetry claim fails (or indicates force-constant/strain effects dominate).
- If a nanodot-barrier system with strong roughness shows no approach toward DMM-like behavior (i.e., remains closer to flat-barrier conductivities), then the claim that mesoscale morphology primarily suppresses low-frequency/long-MFP carriers is called into question.


### 1 Unaccounted for

- Absolute kappa values and quantitative offsets across methods (AGF with mass-difference approximation, empirical-potential MD, and DFT-BTE) are not explained; the theory focuses on qualitative trends and design conditions rather than method-dependent calibration errors.  [Pernot et al., 2010] [Huberman et al., 2017] [Kundu et al., 2011] [Zhang et al., 2014]


## theory-2: Different simulation models change which scattering physics is present, shifting both kappa and trends

If your model ignores some kinds of disorder or uses an imperfect potential, it will predict the wrong thermal conductivity and sometimes the wrong trend. You should judge results based on which scattering mechanisms the model really includes.


### Mass-only disorder models systematically miss force-constant/strain scattering and bias kappa comparisons

If you model Ge only by changing its mass, you miss other important scattering mechanisms and can get biased thermal conductivity values and trends.

**Supporting evidence:**

- AGF study of SiGe barriers uses Tersoff for Si but treats Ge in the mass-difference approximation (mass disorder only), and explicitly notes limitations from this approximation and from Tersoff dispersion inaccuracies.  [Pernot et al., 2010]

- First-principles nanoparticle study in Si0.5Ge0.5 treats mass-difference as dominant but explicitly discusses that force-constant differences and strain were neglected and estimated as smaller; it also reports computed alloy kappa ~30% higher than experiment, indicating sensitivity to omitted scattering channels and/or approximations (e.g., VCA).  [Kundu et al., 2011]

- DFT-BTE + TTG study uses VCA plus impurity scattering and emphasizes that fully spectral solutions are needed; it highlights that simplified heuristics fail, underscoring model-form dependence of inferred kappa suppression when mechanisms are omitted or simplified.  [Huberman et al., 2017]


### When alloying shifts heat to long-MFP modes, geometry/size effects become more influential and require spectral treatment

Alloying can make long-traveling phonons matter more, so size and geometry matter more, and you need spectral (not gray) models to predict the result.

**Supporting evidence:**

- TTG + DFT-BTE study of Si0.934Ge0.066 explains that alloy scattering suppresses high-frequency phonons and shifts dominance to longer-MFP modes, leading to strong grating-period dependence and failure of simple MFP-cutoff/gray heuristics; spectral solutions are required.  [Huberman et al., 2017]

- SiGe nanowire transport theory/review states alloy scattering suppresses high-frequency modes and leads to stronger length dependence and weaker diameter/roughness dependence compared to pure Si, consistent with dominance of low-frequency long-MFP carriers and the need for proper spectral/size treatment.  [Wang et al., 2010] [Li et al., 2021]


### 3 Likely outcomes

- For the same SiGe nanostructure, an AGF or MD model that uses a mass-difference approximation (or otherwise suppresses chemistry-dependent force constants) will predict weaker sensitivity to stiffness-contrast features (e.g., SiC-like stiff inclusions) than a model that includes chemistry-dependent bonding, even if both predict similar trends for purely mass-contrast features.
- Fitted low-order empirical laws for kappa(x,T) derived from finite-size MD boxes will show composition-dependent breakdown near end members more readily than DFT-BTE/VCA curves, because finite-size and potential-dispersion errors are amplified when intrinsic scattering is weak (near pure Si or pure Ge).
- In lightly alloyed SiGe films, spectral BTE models will predict stronger dependence on characteristic experimental length scales (TTG period, film thickness) than gray models, whereas at high alloy fractions (near minimum kappa region) the difference between spectral and gray predictions will shrink.


### 2 Unknown outcomes

- A machine-learned potential trained on diverse Si/Ge/C configurations could reconcile both correct dispersion/anharmonicity and correct defect energetics, yielding kappa predictions that match DFT-BTE for bulk while also matching MD for complex nanostructures; whether current foundation models achieve this for SiGeC without retraining is uncertain.
- Cross-method calibration might reveal that some apparent 'sub-alloy-limit' kappa reports in certain geometries are partially attributable to model-form omissions or boundary-condition artifacts, not only to physical spectral coverage; disentangling would require matched phonon spectra and transmission calculations across methods.


### 2 Negative experiments

- If a mass-only approximation model reproduces experimentally observed stiffness-contrast trends (e.g., stiff inclusions outperforming mass-only predictions) without tuning, then the claim that force-constant/strain omission biases those comparisons is weakened.
- If spectral and gray models agree quantitatively across TTG periods or nanowire lengths even in lightly alloyed SiGe where long-MFP modes should matter, then the asserted necessity of spectral treatment is challenged.


### 1 Unaccounted for

- No direct evidence in the provided dataset links a specific machine-learned potential to kappa predictions for SiGeC; thus, quantitative claims about ML potentials remain untested here.


## theory-3: Thermal conductivity depends on which physics your model actually includes (mass-only vs bonding/roughness/anharmonicity)

If your model only changes masses but not bonds, or if your potential has the wrong phonons, you can get the wrong κ. DFT-BTE gives a good ‘perfect-crystal’ baseline, but real microstructures (interfaces, grains, nanodots) usually reduce κ further—especially when they scatter low-frequency phonons.


### Mass-only disorder models undercount stiffness/chemistry/topology scattering and therefore tend to overpredict κ when those channels matter

If you only change masses and not bonds/chemistry, you miss scattering and usually predict too-high thermal conductivity—especially for interfaces and SiC-like inclusions.

**Supporting evidence:**

- AGF calculations for SiGe barriers and nanodot barriers use Tersoff for Si but treat Ge via a mass-difference approximation (mass disorder only, no Ge force-constant differences). The paper flags this as an approximation/limitation and notes Tersoff dispersion inaccuracies; nevertheless, nanodot-induced roughness drives κ close to DMM-like diffusive limits compared with flatter barriers.  [Pernot et al., 2010]

- In epitaxial Ge nanodot multilayers, experiments show very low cross-plane κ (~0.9 W/mK) and interpret transport as highly diffusive/additive barrier resistance (DMM-like), indicating strong scattering from interface morphology/topography that goes beyond a simple homogeneous alloy mass-disorder picture.  [Pernot et al., 2010]

- Compositionally modulated SiGe multilayers achieve κ below thin-film alloy limits; first-principles BTE modeling explains this by combining scattering from a mean mass-density profile M(z) (barrier-like) with local random fluctuations ΔM (alloy-like), i.e., multiple scattering channels across different frequencies are needed to match experiment.  [Chen et al., 2013]

- First-principles Si0.5Ge0.5 + nanoparticles study models elastic scattering primarily via mass perturbations (alloy disorder and nanoparticles) and neglects IFC/strain contributions after estimating them small; yet it reports computed κ about ~30% higher than experiment, consistent with missing real-structure scattering (and/or missing IFC/topology disorder).  [Kundu et al., 2011]

- The ‘best nanoparticle size distribution’ model explicitly assumes mass-difference dominance and neglects IFC differences between Si and SiGe; it still predicts very large κ reductions by combining point defects + nanoparticles + (optional) grain-boundary scattering, underscoring that when additional scattering channels are included (even phenomenologically) κ can drop far below bulk baselines.  [Zhang et al., 2014]


### Bulk-perfect-crystal DFT-BTE is a baseline upper envelope; microstructure adds a low-frequency filter that depresses κ

Perfect-crystal calculations give the high end. Real microstructures usually lower κ, and they do so more when grains/interfaces are small enough to block the long-traveling phonons.

**Supporting evidence:**

- Nanocrystalline SiGe (2% Ge) VRMC BTE: bulk SiGe κ ≈ 34.3 W/mK at 300 K; nanocrystalline 550 nm grains κ ≈ 18.8 W/mK; 20 nm grains κ ≈ 4.6 W/mK—demonstrating monotonic κ suppression with decreasing grain size (increased GB density).  [Yang et al., 2017]

- Nanocrystalline Si VRMC BTE: 20 nm grain size yields κ ≈ 8.4 W/mK at 300 K, far below bulk Si values (~155–166 W/mK used as bulk references in other modeling contexts), consistent with strong low-frequency/MFP filtering by GBs.  [Yang et al., 2017] [Singh et al., 2010] [Zhang et al., 2014]

- Epitaxial Ge nanodot multilayers: cross-plane κ as low as ~0.9 W/mK at room temperature; interpretation is additive, highly diffusive nanodot-layer resistances with ballistic spacers, i.e., dense barriers suppress the long-MFP contribution and push toward a DMM-like limit.  [Pernot et al., 2010]

- Compositionally modulated SiGe multilayers: measured cross-plane κ down to ~2.3 W/mK as mean Ge rises (~12%); first-principles BTE explains κ below alloy limits via combined barrier-like and alloy-like scattering across the spectrum (broadband suppression).  [Chen et al., 2013]

- Single-crystal Si0.934Ge0.066 TTG + DFT-BTE/VCA: parameter-free BTE matches measured effective κ versus grating period, supporting DFT-BTE as a credible ideal-crystal spectral baseline; size (finite length scale) suppresses κ by reducing contributions from long-MFP modes.  [Huberman et al., 2017]


### 3 Likely outcomes

- If a SiGe nanocomposite contains chemistry-distinct inclusions (e.g., SiC) rather than isomorphous Si/Ge inclusions, then a mass-only inclusion model will systematically underpredict the inclusion’s κ suppression relative to chemistry-aware (DFT/ML) models because stiffness/topology scattering is missing.
- For a fixed SiGe composition, introducing a microstructure length scale ℓ (grain size, barrier spacing, dot-layer period) that is reduced from >1 µm toward tens of nm will monotonically reduce κ until approaching a diffusive limit; the strongest marginal drop will occur when ℓ crosses the modal MFP range dominating κ in the alloy (shifted toward low-frequency modes by alloy scattering).
- If two models match the same experiment without including microstructure, the one using a more approximate potential/form (e.g., empirical potential with known dispersion issues or mass-only disorder) is more likely achieving agreement by error cancellation; adding explicit microstructure scattering to that model will then overshoot the experimental κ reduction.


### 2 Unknown outcomes

- A modern foundation ML potential for Si–Ge–C trained on diverse bonding environments will predict a materially different balance between substitutional C and SiC precipitation under strain than older ML/empirical approaches; if it predicts strong SiC driving force, κ will be dominated by precipitate/interface scattering rather than isolated point-defect scattering even at 1 at% C.
- Including strain-altered force constants (beyond mass-density profiles) in first-principles BTE for coherently strained compositionally modulated SiGe multilayers could change κ in either direction depending on whether strain increases anharmonicity more than it reduces spectral mismatch; the sign may flip with period thickness and Ge profile shape.


### 2 Negative experiments

- Construct two otherwise identical Si/Ge barrier simulations: one mass-only (Ge as mass substitution in Si) and one chemistry-aware (explicit Si–Ge IFC contrast). If κ does not decrease (or increases) when chemistry-aware force constants are included, the claimed upward bias of mass-only models is falsified for that regime.
- Measure or simulate κ_real/κ_bulk,ideal versus grain size for a SiGe composition while independently characterizing GB transmission; if κ does not decrease as grain size is reduced into the dominant MFP range (without a compensating increase in specularity/transmission), the ‘length-scale low-frequency filter’ rule fails.


### 2 Unaccounted for

- Nanowire-specific diameter/roughness scaling laws and the reported plateau-like κ(x) behavior in some NW theories are not explicitly derived here; this theory focuses on model-form/potential bias and microstructure filtering rather than nanowire confinement formalisms.  [Wang et al., 2010] [Li et al., 2021]

- Amorphous SiGe shows κ reductions dominated by mode localization and generalized-velocity suppression rather than crystalline mass-scattering pictures; how potential choice biases amorphous κ is only touched on via special cases, not modeled as a separate law here.  [Lundgren et al., 2020]


## theory-4: Lowest κ happens when you scatter both high- and low-frequency phonons with different features

Alloying kills mainly higher-frequency phonons. To cut κ even more, you must also block the long-traveling low-frequency phonons using boundaries, barriers, or the right nanoparticle sizes.


### Alloy scattering shifts dominant heat flow toward low-frequency modes; added interfaces/GBs then become disproportionately effective

As you alloy Si with Ge, the remaining heat is carried more by low-frequency phonons—so boundaries and interfaces that block those phonons become especially powerful.

**Supporting evidence:**

- Nanocrystalline SiGe (2% Ge): mass-defect scattering plus GB transmission produces large κ reductions with decreasing grain size, indicating remaining heat flow includes long-MFP modes that GBs can suppress.  [Yang et al., 2017]

- Nanocrystalline Si: at 300 K, low-frequency phonons contribute strongly; GB models emphasize transmission near unity at low ω and reduced transmission at higher ω, showing spectral filtering matters.  [Yang et al., 2017]

- SiGe nanowire modeling and reviews state alloy scattering suppresses high-frequency phonons, making low-frequency phonons dominate and causing stronger length dependence but weaker diameter/roughness dependence in alloys than in pure Si.  [Wang et al., 2010] [Li et al., 2021]

- Compositionally modulated SiGe multilayers: combining barrier-like (low-frequency effective) scattering with alloy-like (high-frequency effective) scattering yields κ below both perfect superlattice and homogeneous alloy limits, consistent with complementary spectral targeting.  [Chen et al., 2013]

- Ge nanodot multilayers achieve κ close to DMM-like limits; nanodot roughness broadens the scattering influence relative to flat barriers, consistent with enhanced suppression of longer-MFP/low-frequency modes.  [Pernot et al., 2010]


### Broadband design rule: combining M(z) barriers with ΔM randomness (or multi-scale inclusions) can undercut homogeneous-alloy κ

If you mix ‘barrier-like’ structure with ‘alloy-like’ randomness, you can scatter a wider range of phonons and get κ even lower than a plain alloy.

**Supporting evidence:**

- Compositionally modulated multilayers paper explicitly decomposes scattering into mean mass-density profile M(z) (barrier scattering) plus random ΔM (alloy scattering) and reports that combined presence can lower κ below both homogeneous alloy and ideal sharp-interface superlattice limits.  [Chen et al., 2013]

- Experimental Ge nanodot multilayers show additive barrier resistances and κ near DMM-like limits, consistent with an incoherent/diffusive regime where adding structured barriers reduces κ beyond what flat alloy barriers achieve.  [Pernot et al., 2010]

- AGF simulations comparing flat SiGe barriers vs nanodot barriers show nanodot systems yield lower κ and are closer to DMM than flat barriers, supporting that adding mesoscale morphology (a form of M(z) complexity) increases scattering breadth.  [Pernot et al., 2010]

- MD on compositionally graded SiGe nanowires reports substantially reduced κ versus abrupt interfaces (review cites ~57% reduction), consistent with broadened scattering from grading + disorder.  [Li et al., 2021]


### 3 Likely outcomes

- For Si0.8Ge0.2, introducing nanodot/nanoparticle layers (or GBs) will reduce κ more than the same interface density in pure Si because alloying shifts heat carriage toward long-MFP low-frequency modes that interfaces can filter.
- A compositionally graded profile with residual random alloy disorder will yield lower κ than either (i) a fully homogeneous alloy of the same mean x or (ii) a perfectly abrupt, perfectly periodic superlattice of the same mean x, provided interfaces are sufficiently diffuse/incoherent.
- Adding a second length scale (e.g., nanoparticles + grain boundaries) will produce a super-additive reduction relative to adding either alone if the two target different parts of the phonon spectrum.


### 2 Unknown outcomes

- In SiGeC, an engineered tri-modal spectrum of scatterers (substitutional C + SiC precipitates + nanoscale GBs) could push κ below amorphous-Si benchmarks while retaining crystallinity, if stiffness-disorder scattering from SiC is as broadband as hypothesized.
- There may exist an optimal correlated arrangement (not random) of graded composition + nanodots that maximizes broadband suppression without invoking coherent interference, potentially outperforming purely random microstructures.


### 2 Negative experiments

- If a controlled experiment/simulation shows that adding interfaces/barriers to an alloy reduces κ by the same fraction as in pure Si (after matching interface density and roughness), the predicted alloy-amplified marginal effect is false.
- If graded profiles consistently show higher κ than abrupt interfaces at the same mean composition and defect density in the incoherent regime, the broadband-scattering/inequality rule is falsified.


### 1 Unaccounted for

- This theory does not directly address the detailed potential-dependence or endpoint-composition anomalies that can arise in empirical MD fits; it focuses on physical spectral complementarity rather than numerical artifacts.  [Pernot et al., 2010]


## theory-5: In amorphous SiGe, small Ge amounts mainly kill the lowest-frequency heat carriers

For amorphous SiGe, a little Ge quickly localizes (or otherwise de-extends) the vibrations that carry most heat. After that, adding more Ge helps less. Small simulation cells mainly fail by not representing these lowest-frequency contributions well.


### Early-drop law: low-x Ge suppresses low-frequency heat-carrying modes in a-Si

Adding a few percent Ge to amorphous Si knocks out the most important low-frequency heat carriers first; later Ge additions reduce heat flow more slowly and via broader-band damping.

**Supporting evidence:**

- Room-temperature amorphous SiGe: a-Si κ ≈ 2.2 W/mK; 5% Ge reduces κ by ~0.6 W/mK (to ~1.6 W/mK) and 15% Ge reduces it by an additional ~0.55 W/mK (to ~1.05 W/mK), implying a steep initial drop then diminishing returns at higher x.  [Lundgren et al., 2020]

- Mode-resolved contribution: in a-Si the lowest ~8% of modes (0–4 THz in a-Si) contribute ~half of κ; these low-frequency contributions are the ones most strongly suppressed by small Ge concentrations.  [Lundgren et al., 2020]

- Mechanism attribution at low x: κ reduction at low x is reported to be dominated by localization and reduced generalized velocities/spatial overlap rather than a large reduction in lifetimes (i.e., not primarily a crystalline-like mass-scattering-MFP picture).  [Lundgren et al., 2020]

- Mechanism attribution at higher x: at higher Ge concentrations, spectral broadening (linewidth increase) reduces resonant transport and mode diffusivity; high-frequency localization contributes little to total κ due to small heat-carrying weight.  [Lundgren et al., 2020]


### Low-frequency convergence law: finite-size dependence in amorphous κ is dominated by the lowest-frequency sector

If an amorphous SiGe simulation box is too small, the missing piece is mainly the lowest-frequency heat transport, so κ looks size-dependent for that reason.

**Supporting evidence:**

- Finite-size effects reported: low-frequency modal contributions (<4 THz in a-Si) show the largest finite-size sensitivity; 1728-atom models differ from converged 13824-atom results mostly in the <4 THz region.  [Lundgren et al., 2020]

- Convergence statement: small cells are adequate for qualitative trends but underconverged for low-frequency quantitative contributions, indicating that κ size dependence is a low-frequency convergence issue.  [Lundgren et al., 2020]


### 2 Likely outcomes

- Reverse-NEMD (or EMD) κ for amorphous Si0.5Ge0.5 will show substantially weaker length dependence than crystalline Si0.5Ge0.5 in comparable cell geometries; any residual length dependence should primarily appear as κ increasing with length as the low-frequency sector becomes better represented.
- For amorphous Si1-xGex near 300 K, κ(x) will be locally concave upward near x=0 (steep initial drop then diminishing returns), and the composition at which the slope noticeably flattens will correlate with when the lowest-frequency sector’s contribution has already been strongly suppressed.


### 2 Unknown outcomes

- Introducing nanometer-scale stiff inclusions (e.g., SiC) into amorphous SiGe could either increase κ (if inclusions create percolating extended vibrational pathways) or decrease κ (if interfaces create additional localization/broadening); the sign should depend on inclusion connectivity and interface bonding strength.
- If an ML potential reproduces the amorphous vibrational spectrum more accurately than Tersoff (especially low-frequency modes), it may shift the predicted crossover composition between localization-dominated and broadening-dominated regimes, changing κ(x) curvature while preserving the qualitative early-drop behavior.


### 3 Negative experiments

- If mode-resolved analysis in amorphous SiGe shows that the lowest-frequency modes remain similarly extended and retain their generalized velocities up to ~10–15% Ge while κ still drops sharply, then localization/reduced generalized-velocity suppression is not the dominant low-x mechanism and the theory fails.
- If κ computed in amorphous SiGe decreases systematically with increasing simulation cell size after robust statistical convergence (contrary to the claim that missing low-frequency contributions are added with size), the finite-size law is wrong or incomplete.
- If κ(x) in amorphous SiGe is found to be nearly linear in x over 0–20% Ge (no strong early drop), the proposed two-regime compositional mechanism is undermined.


### 1 Unaccounted for

- All crystalline SiGe phenomena in the evidence set (e.g., nanodot barriers, planar superlattices, nanocrystalline grain-boundary transmission, nanoparticle scattering in crystals) are outside this theory’s scope, which is limited to fully amorphous networks.  [Pernot et al., 2010] [Chen et al., 2013] [Singh et al., 2010] [Yang et al., 2017] [Kundu et al., 2011] [Zhang et al., 2014] [Huberman et al., 2017] [Wang et al., 2010] [Li et al., 2021]


## theory-6: Nanodot layers act like separate diffuse scattering barriers that add up

Each nanodot layer behaves like a strong, diffuse phonon-scattering wall. Heat resistance is roughly the sum of the walls, and nanodots reduce thermal conductivity more than flat alloy layers because they scatter long-wavelength phonons better.


### Independent-resistor additivity for highly diffusive nanodot barriers

If each nanodot layer scatters diffusively, adding more layers adds resistance almost linearly, so thermal conductivity drops as the barrier layers get denser—until spacer resistance or saturation limits further drops.

**Supporting evidence:**

- Experiments on epitaxial Si with vertically stacked Ge nanodot layers report that transport is ballistic in Si spacers (due to long phonon MFPs) while scattering is dominated by independent nanodot layers, so total resistance is interpreted as the sum of barrier resistances; measured κ_cross-plane reaches (0.9 ± 0.1) W/m-K for a ~15.5 nm region with 5 nanodot layers and ~3.7 nm period, and per-barrier resistances are discussed as additive and DMM-like.  [Pernot et al., 2010]

- AGF simulations of nanodot-barrier multilayers yield conductivities close to the DMM limit and in reasonable agreement with experiment, supporting the assumption that each nanodot barrier behaves as a highly diffusive scatterer whose resistance can be treated in an incoherent/additive manner at the device scale (within modeling approximations).  [Pernot et al., 2010]


### Nanodot morphology enhances low-frequency scattering relative to flat disordered alloy barriers

Nanodots scatter long-wavelength phonons better than flat alloy layers, so they reduce thermal conductivity more and push behavior toward a diffuse-interface limit.

**Supporting evidence:**

- AGF calculations explicitly comparing flat Si0.5Ge0.5 barriers to lens-shaped nanodot barriers show the nanodot systems yield significantly lower κ and are close to DMM and experiments, while flat barriers yield higher κ. The mechanism attributed is that nanodots introduce larger-scale roughness features that reduce low-frequency phonon mean free paths relative to flat disordered interfaces; high-frequency behavior is more similar between flat and nanodot cases.  [Pernot et al., 2010]

- Experiments on epitaxial Ge nanodot multilayers in Si report very low κ_cross-plane (down to ~0.9 W/m-K) and interpret the nanodot layers as highly diffusive barriers consistent with DMM-like limits; the paper contrasts this with prior flat-barrier superlattice literature that exhibits higher κ/less diffusive behavior.  [Pernot et al., 2010]

- Compositionally modulated SiGe multilayers (graded/interdiffused planar profiles) are predicted and measured to achieve κ lower than abrupt-barrier or homogeneous-alloy limits because combining barrier-like scattering (effective at low frequencies) with alloy disorder (effective at high frequencies) broadens the scattered frequency range. This supports the broader principle that adding structural nonuniformity that targets low-frequency phonons can outperform purely planar composition disorder alone.  [Chen et al., 2013]


### 3 Likely outcomes

- Keeping total Ge volume fraction fixed (<~20%) in an epitaxial Si matrix, converting planar SiGe barrier layers into nanodot (3D topographic) barrier layers will reduce κ_cross-plane and move the measured per-barrier resistance closer to full-dispersion DMM estimates; the effect will be strongest at room temperature where long-MFP acoustic modes contribute substantially.
- At fixed dot morphology and similar dot size distribution, κ_cross-plane will approximately follow R_tot ≈ N·R_barrier + R_spacers: doubling the number of nanodot layers (at similar spacers) will increase total resistance approximately linearly until spacer resistance becomes non-negligible.
- If dot morphology is progressively smoothed (e.g., annealing that rounds features and reduces height variation without changing average Ge content much), κ_cross-plane will increase toward the planar-barrier trend, with the largest relative recovery in contributions from low-frequency modes.


### 2 Unknown outcomes

- If nanodot barrier layers are partially amorphized (confined to dot regions) while spacers remain crystalline, per-barrier resistance may increase beyond the DMM-like crystalline-interface limit by adding localized vibrational states; whether κ decreases further or saturates depends on whether the current nanodot layers are already near the maximum diffusive scattering attainable for the dominant low-frequency modes.
- Applying coherent biaxial strain to the Si spacer regions (without introducing dislocations) could either increase or decrease R_barrier depending on how strain shifts acoustic mismatch and mode conversion at the dot/spacer interface; a sign change with temperature is possible if different spectral regions dominate at different T.


### 3 Negative experiments

- Measure κ_cross-plane for otherwise identical multilayers while varying only the number of nanodot layers N at fixed total thickness (compensating spacer thickness accordingly). If R_tot is not approximately linear in N in the regime where barriers are claimed to be independent, the additivity assumption is falsified.
- Create a planar-barrier multilayer engineered to have similar roughness amplitude/correlation lengths as the nanodot case (e.g., intentionally roughened planar interfaces). If κ matches the nanodot case, then nanodot-specific morphology is not the controlling factor; if κ remains higher, it supports the unique low-frequency scattering role of true 3D topography.
- Perform spectral/size-sensitive measurements (e.g., varying spacer thickness systematically) to see whether the inferred per-barrier resistance is constant. Strong spacer-thickness dependence of extracted R_barrier would indicate non-independent barriers or coherent effects.


### 2 Unaccounted for

- The theory does not address substitutional carbon in SiGe, SiC nanoinclusions, or carbon-driven local chemical ordering (Si-rich shells), which are central to other hypotheses in the mission statement but absent from the nanodot evidence base here.  [Li et al., 2021]

- The theory does not attempt to explain amorphous SiGe thermal conductivity trends or localization physics in glasses, which involve different mechanisms than interface/barrier-dominated crystalline multilayers.  [Lundgren et al., 2020]

# Theorizer run `gesn_kinetics` (task 6bca228d-d035-4c30-a2cc-9f9f939e0f14)

Papers extracted (8): Controlling barrier height and spectral responsivity of p–i–n based GeSn photodetectors via arsenic incorporation; Structural changes in Ge1-xSnx and Si1-x-yGeySnx thin films on SOI substrates treated by pulse laser annealing; Monolithic infrared silicon photonics: The rise of (Si)GeSn semiconductors; The thermal stability of epitaxial GeSn layers; Free-running Sn precipitates: an efficient phase separation mechanism for metastable Ge1−xSnx epilayers; Source/Drain Materials for Ge nMOS Devices: Phosphorus Activation in Epitaxial Si, Ge, Ge1−x Sn x and Si y Ge1−x−y Sn x; Thermally activated diffusion and lattice relaxation in (Si)GeSn materials; Vacancy complexes in nonequilibrium germanium-tin semiconductors


## theory-1: Substitutional Sn is stable until fast paths connect it to a strong surface sink

Sn stays substitutional unless it can rapidly travel to a surface that irreversibly removes it. Oxide caps work mainly by blocking that surface escape route; Ge caps block the free surface but allow Sn to spread into the surrounding Ge instead.


### Surface-sink boundary condition law

A free surface lets Sn escape; oxide caps largely stop the escape; Ge caps stop surface escape but let Sn spread into nearby Ge.

**Supporting evidence:**

- At 550 °C isothermal anneal of Si0.08Ge0.88Sn0.04, uncapped sample shows ~50 min incubation then rapid collapse (t0 = 74.2 ± 0.5 min; collapse width 1.86 ± 0.15 min), large E2 blueshift (+423 meV), ~60% thickness loss, voids with oxygen, filamentary Sn-enriched paths, and formation of a Ge0.99Sn0.01 segregation layer; with a 3 nm SiO2 cap, compositional change <1 at.% Sn over 140 min, |ΔE2| < 20 meV, no voids, limited strain relaxation, and much lower contact resistivity degradation.  [Attiaoui et al., 2026]

- Screening result: 5 nm Al2O3 also suppresses segregation after 550 °C / 30 min (ex situ SE), consistent with nm-scale oxide capping acting as a strong throttle of surface-mediated loss.  [Attiaoui et al., 2026]

- In RP-CVD pseudomorphic diffusion experiments, uncapped samples show surface segregation above ~600 °C, whereas Ge/GeSn/Ge and Ge/SiGeSn/Ge sandwiches with thick in-situ Ge caps suppress surface segregation and instead exhibit Sn redistribution into cap/buffer (e.g., >2× reduction of Sn peak after 10 min @ 600 °C).  [Driesch et al., 2019]

- Thermal stability study of GeSn: relaxed (dislocated) layers show Sn-rich clusters at both free surface and GeSn/Ge interface (MD cores as sinks/fast paths), while pseudomorphic layers show Sn accumulation mainly at the surface; segregation occurs above a composition-dependent critical temperature T_C(x).  [Zaumseil et al., 2018]

- Conceptual/literature discussion that capping or H-termination is expected to suppress surface segregation and delay precipitation/phase separation by removing the surface source/sink of Sn and reducing point-defect-assisted pathways (qualitative support for boundary-condition control).  [Groiss et al., 2017]

- PLA studies in air show Sn out-diffusion to the surface and Sn-rich oxide formation at higher pulse energies, highlighting that surface oxidation can be an irreversible sink for Sn when present.  [Steuer et al., 2024]


### Incubation-then-collapse (connectivity-to-sink) kinetics law

Nothing seems to change for a while, then Sn loss suddenly accelerates once a fast escape network effectively connects to the surface sink.

**Supporting evidence:**

- Uncapped SiGeSn at 550 °C shows ~50 min incubation then rapid collapse with a fitted logistic width of ~1.9 min; TEM/EDX show filamentary Sn-enriched paths and widespread voids containing oxygen in the degraded region, consistent with a sudden transition to an efficient short-circuit/sink-coupled transport mode.  [Attiaoui et al., 2026]

- Relaxed/dislocated GeSn layers exhibit sudden segregation above a critical temperature T_C(x), with clustering at surfaces and interfaces around dislocation cores (fast paths/sinks), consistent with threshold-like onset behavior when channels become effective.  [Zaumseil et al., 2018]

- In uncapped MBE GeSn at higher Sn, rapid surface segregation and substitutional Sn loss can appear already at 400–600 °C for 60 s anneals depending on composition, consistent with a threshold in the effective transport/instability pathway versus composition and temperature (although the detailed channel physics differs by microstructure).  [Zhou et al., 2025]

- This connectivity interpretation is consistent with (but distinct from) the droplet-mediated rapid transformation observed above the eutectic in high-Sn MBE GeSn, where once a new fast transport state (liquid droplet) nucleates, transformation proceeds quickly after a short onset.  [Groiss et al., 2017]


### Cap-induced sink relocation and two-regime activation law

With a thick Ge cap, Sn doesn’t form surface piles; it spreads into the surrounding Ge, and the measured diffusion shows a high-T ‘normal’ regime and a low-T ‘enhanced’ regime.

**Supporting evidence:**

- Ge/GeSn/Ge and Ge/SiGeSn/Ge capped sandwiches suppress surface segregation and show two Arrhenius regimes for Sn: high-T EA = 3.10 ± 0.07 eV (Ge/GeSn/Ge) and 2.87 ± 0.03 eV (Ge/SiGeSn/Ge); low-T EA = 1.81 ± 0.09 eV (Ge/GeSn/Ge) and 1.13 ± 0.11 eV (Ge/SiGeSn/Ge).  [Driesch et al., 2019]

- In capped Ge0.94Sn0.06, the Sn peak concentration decreases by >2× after 10 min at 600 °C, indicating redistribution into adjacent Ge layers rather than surface pile-up.  [Driesch et al., 2019]

- Uncapped counterparts show surface segregation above ~600 °C, demonstrating that the cap changes the boundary condition and thus where Sn accumulates (surface vs buried Ge sinks).  [Driesch et al., 2019]

- Oxide-capped SiGeSn at 550 °C maintains composition uniformity (<1 at.% Sn change) over 140 min and avoids voiding/segregation, showing that some caps can largely suppress not only surface pile-up but also catastrophic redistribution on these timescales.  [Attiaoui et al., 2026]

- The diffusion study itself notes that the low-T enhanced regime cannot be explained by vacancy-mediated diffusion alone and invokes metastability/chemical potential gradients as major drivers (supports the ‘effective’ low-T EA interpretation).  [Driesch et al., 2019]


### 4 Likely outcomes

- H9: For Si0.08Ge0.88Sn0.04 held at 550 °C, a continuous 3 nm SiO2 cap will suppress the near-surface substitutional Sn-loss signal relative to uncapped. The uncapped film will show a visible change after an incubation time on the order of tens of minutes (∼50 min scale), whereas the capped film will show no visible change (or a much longer incubation) over the same observation window.
- If dislocation density is increased (partially relaxed vs pseudomorphic) in uncapped films at fixed T (e.g., 550 °C), incubation time will decrease and near-surface Sn loss will accelerate; with a high-quality oxide cap, this dependence will be strongly reduced because the surface sink is throttled.
- Replacing 3 nm SiO2 with ~5 nm Al2O3 on the same SiGeSn stack will similarly suppress near-surface Sn-loss kinetics at 550 °C provided the layer is continuous and stable (consistent with the screening result).
- In Ge/GeSn/Ge sandwiches, changing the Ge cap thickness primarily changes the spatial redistribution/symmetry of the final Sn profile (sink capacity), not the existence of surface segregation; surface pile-up should remain suppressed as long as no free surface is exposed.


### 3 Unknown outcomes

- A nominally continuous oxide cap with a controlled density of engineered pinholes will restore incubation-then-collapse kinetics; the incubation time will scale inversely with pinhole density and pinhole opening size (a percolation-to-sink problem).
- A cap stack that blocks Sn transport but allows efficient vacancy/interstitial exchange (e.g., via a defect-rich interlayer) could allow voiding/degradation without large net Sn loss, yielding a decoupled ‘voiding-without-Sn-depletion’ mode detectable by TEM/SE line broadening.
- Applying an oxygen-gettering interlayer below an oxide cap (e.g., ultrathin Si) could either stabilize further (suppress oxidation-assisted sink irreversibility) or destabilize (create interdiffusion-driven defect injection), producing a non-monotonic stability vs interlayer thickness.


### 3 Negative experiments

- If a verified-continuous 3 nm oxide cap (no pinholes, no delamination) produces the same incubation time and collapse amplitude at 550 °C as an uncapped sample, then the boundary-condition/surface-sink premise is falsified for that system.
- If oxide-capped samples still develop the same Ge0.99Sn0.01 surface segregation layer and surface Sn clusters as uncapped samples without cap failure, then the proposed cap-throttled surface sink mechanism is wrong or incomplete.
- If a very-low-dislocation-density uncapped film still shows a short-incubation rapid collapse identical to a highly dislocated film, then channel connectivity via dislocations/short-circuits is not the controlling variable as proposed.


### 1 Unaccounted for

- DFT/NEB work in uncapped MBE GeSn reports very low derived activation energies (~0.83–0.93 eV) for vacancy-mediated Sn hops in VSnV-containing supercells, whereas SIMS-based interdiffusion in capped sandwiches yields much larger high-T activation energies (~2.9–3.1 eV). The present theory treats these as different ‘effective’ regimes/contexts (local hop vs macroscopic interdiffusion with vacancy formation contributions), but does not quantitatively reconcile them.  [Zhou et al., 2025] [Driesch et al., 2019]


## theory-2: Vacancies can either lock Sn in place or help it move, depending on temperature and composition

As Sn and temperature rise, Sn increasingly teams up with vacancies to form complexes that can move Sn around, so substitutional Sn becomes unstable.


### VSnV favorability increases with total Sn concentration

More Sn in the alloy makes Sn–vacancy clustering easier and more likely.

**Supporting evidence:**

- DFT/PBE formation energies for VSnV become more negative as total Sn increases (Table 3): from −4.244 eV at 3.2% to −6.279 eV at 16.1% Sn; binding-energy trend in Fig.11 increases with Sn concentration; charge-density maps show increased electron density around VSnV with higher Sn.  [Zhou et al., 2025]

- Experimentally (uncapped MBE GeSn), the inferred fraction of substitutional Sn converted to VSnV increases with anneal temperature and with higher initial Sn concentration, including complete loss of measurable substitutional Sn by 600 °C for the highest-Sn sample (8.6% Sn_s) after 60 s.  [Zhou et al., 2025]


### Vacancy-mediated Sn hop activation decreases with increasing Sn content (local mechanism)

Higher Sn content can make Sn-via-vacancy hops easier.

**Supporting evidence:**

- DFT/NEB: migration barrier decreases from 0.286 eV (Ge60Sn2-VSnV) to 0.179 eV (Ge55Sn7-VSnV); derived activation energies 0.927 eV to 0.832 eV for these models.  [Zhou et al., 2025]


### 3 Likely outcomes

- O1: In Ge0.88Sn0.12, a substitutional Sn adjacent to a vacancy will be bound (positive binding) by at least 0–0.3 eV and plausibly >0.3 eV if VSnV-like stabilization dominates at this composition; the binding tendency should increase relative to lower Sn alloys.
- O2: In MD of Ge0.88Sn0.12 with vacancies at 500–700 K, observed Sn hops mediated by nearby vacancies will show an effective activation energy well below bulk Ge substitutional diffusion (2.9–3.3 eV), more consistent with the low-energy metastable/defect-assisted range (≈1.1–1.8 eV or below for local hops), depending on whether vacancy formation is implicit or fixed.
- Increasing total Sn content at fixed anneal temperature (e.g., 550–600 °C) will increase the fraction of Sn converted to non-substitutional Sn–vacancy clusters (VSnV-like) and will lower the temperature at which surface segregation features become visible in uncapped films.


### 2 Unknown outcomes

- If vacancy concentrations are externally controlled (e.g., by pre-irradiation vs vacancy annihilation treatments), the same GeSn composition could switch between a ‘vacancy-sequestering’ regime (stable substitutional Sn) and a ‘vacancy-mobility’ regime (rapid Sn loss), producing hysteresis in stability vs pre-history.
- In ternary SiGeSn, repulsive Si–Sn interactions combined with Sn–vacancy clustering may create spatial anti-correlations that further lower effective barriers for Sn–vacancy complex migration compared with binary GeSn (beyond what is captured by effective Arrhenius fits).


### 2 Negative experiments

- If direct binding-energy calculations at ~12% Sn show Sn–V is unbound (negative binding), the assumed thermodynamic tendency toward Sn–vacancy association at high Sn would be undermined.
- If varying total Sn at fixed microstructure and anneal temperature does not change the inferred non-substitutional defect fraction (contrary to the DFT+RTA trend), the proposed thermodynamic switch with x would be falsified.


### 1 Unaccounted for

- PAS/DFT on P-doped GeSn indicates Sn_n–V complexes are less favorable than P_n–V complexes, implying dopants can dominate vacancy trapping; the present theory does not explicitly incorporate dopant competition effects into stability predictions.  [Vohra et al., 2020]


## theory-3: More Sn makes vacancy-assisted Sn motion easier, creating a low-barrier diffusion regime

As Sn content rises, Sn more readily forms and moves with vacancy-related defects. That makes Sn leave substitutional lattice sites faster and promotes redistribution toward surfaces/interfaces, producing an apparent low-energy diffusion regime.


### Sn concentration increases thermodynamic stability of VSnV-type complexes

With more Sn in the alloy, Sn–vacancy complexes are easier to form and more stable, so annealing converts more substitutional Sn into these defects.

**Supporting evidence:**

- DFT in GeSn reports VSnV formation energies becoming progressively more favorable with increasing Sn fraction (Table 3 trend from about −4.244 eV at ~3.2% to about −6.279 eV at ~16.1%) and shows increasing VSnV binding strength with Sn concentration (Fig.11 trend).  [Zhou et al., 2025]

- NEB/DFT and accompanying discussion in the same study link increased Sn content to weaker Ge–Sn bonding and to increased tendency for non-substitutional Sn-vacancy clustering, consistent with a thermodynamic shift toward VSnV at higher Sn.  [Zhou et al., 2025]

- Experiment (uncapped MBE GeSn) shows substitutional Sn retention decreases with increasing initial Sn and increasing anneal temperature (60 s RTA): the 8.6% sample loses measurable substitutional Sn already at 400 °C and is fully depleted by 600 °C, while 4.5% and 7.2% samples retain at 400 °C and partially retain at 600–800 °C. This is consistent with higher-x alloys being more susceptible to conversion away from substitutional Sn during anneal.  [Zhou et al., 2025]

- PAS on CVD GeSn (6.5–13 at.% Sn) finds divacancies dominate and the intensity of larger vacancy clusters decreases as Sn increases, interpreted as Sn stabilizing vacancies in specific configurations and suppressing vacancy clustering—consistent with strong Sn–vacancy interactions affecting defect thermodynamics/assembly.  [Assali et al., 2019]

- PAS/CDOBS in GeSn:P detects Sn atoms adjacent to mono-vacancy-sized open volume in mixed Sn_pP_n–V complexes, demonstrating that Sn can occupy vacancy-neighbor environments in epitaxial GeSn.  [Vohra et al., 2020]


### Vacancy-mediated Sn hop barrier decreases with local Sn content

In Sn-richer local environments, it takes less energy for Sn to hop with a vacancy, so diffusion speeds up.

**Supporting evidence:**

- DFT/NEB reports lower migration barriers for higher Sn content supercells: example barriers decrease from 0.286 eV (Ge60Sn2–VSnV) to 0.179 eV (Ge55Sn7–VSnV), with derived activation energies decreasing from 0.927 to 0.832 eV.  [Zhou et al., 2025]

- The same MBE+DFT study reports that higher initial Sn content yields earlier and larger substitutional Sn loss and earlier surface segregation during 400–800 °C RTA (60 s), consistent with faster vacancy-mediated kinetics at higher Sn content.  [Zhou et al., 2025]

- In coherent capped diffusion experiments, SiGeSn shows a lower low-T effective activation energy than GeSn (1.13 eV vs 1.81 eV), consistent with the broader idea that alloy chemistry/local environment can reduce effective barriers and enhance Sn mobility in metastable alloys.  [Driesch et al., 2019]


### Two-branch Arrhenius behavior arises from a defect-population/complexation crossover

At high temperature diffusion looks like ordinary bulk diffusion, but at lower temperature the metastable alloy’s defect population and Sn–vacancy complex dynamics make diffusion appear much easier.

**Supporting evidence:**

- Capped sandwich diffusion experiments report two Arrhenius regimes: Ge/GeSn/Ge high-T EA = 3.10 ± 0.07 eV and low-T EA = 1.81 ± 0.09 eV; Ge/SiGeSn/Ge high-T EA = 2.87 ± 0.03 eV and low-T EA = 1.13 ± 0.11 eV.  [Driesch et al., 2019]

- The diffusion study explicitly notes the low-T activation-energy reduction cannot be explained solely by strain-driven vacancy formation and emphasizes metastability/chemical-potential gradients as key drivers, consistent with an effective-EA crossover interpretation rather than a single-mechanism Arrhenius law.  [Driesch et al., 2019]

- The oxide-capping stability study argues bulk substitutional diffusion is too slow at 550 °C to explain observed transport (estimated diffusion length ~0.3 nm over 50 min), implying that alternative fast paths and defect-controlled kinetics determine observed changes in uncapped samples—consistent with the general idea that measured kinetics can be controlled by defect populations and fast pathways rather than bulk hop barriers.  [Attiaoui et al., 2026]


### 4 Likely outcomes

- O1 (Ge0.88Sn0.12, MACE-MP-0 static): a substitutional Sn adjacent to a vacancy is predicted to be bound (positive binding). Category-level expectation: 'bound by 0 to 0.3 eV' or 'bound by more than 0.3 eV' (leaning >0.3 eV given VSnV stabilization trends at higher Sn, but noting dopant-free context matters).
- O2 (Ge0.88Sn0.12 with vacancies, 500–700 K MD): effective activation energy for observed Sn hops is predicted to be well below bulk Ge substitutional diffusion (2.9–3.3 eV) and more consistent with a low-barrier regime (category: 'close to the low-temperature metastable-film value (1.1 to 1.8 eV)' rather than bulk-like).
- At fixed anneal temperature (e.g., 600 °C) and time (e.g., 60 s), raising initial Sn content from ~4–5% to ~8–9% in uncapped GeSn will increase substitutional Sn loss markedly and produce earlier surface segregation signatures (consistent with the reported 400–600 °C behavior).
- In coherent capped diffusion stacks, SiGeSn will continue to show a lower low-T effective activation energy than GeSn at similar Sn content, reflecting stronger low-T enhancement in the ternary (as already suggested by existing EA_low values).


### 2 Unknown outcomes

- If the low-T regime is truly defect-population-controlled, then independently reducing vacancy availability (e.g., by growth at higher T to reduce vacancy supersaturation or by adding strong vacancy sinks) should selectively suppress the low-T enhanced diffusion branch while leaving the high-T branch relatively unchanged.
- At higher Sn contents (~12–16%), local Sn enrichment could create autocatalytic mobility: once small Sn-rich/vacancy-rich regions form, local barriers drop enough to accelerate further Sn rearrangement, potentially yielding sudden internal clustering even in capped stacks without a free surface sink.


### 3 Negative experiments

- If MACE-MP-0 predicts the Sn–vacancy nearest-neighbor binding in Ge0.88Sn0.12 is unbound (negative binding), then the premise that Sn–V attraction/complexation controls low-T mobility becomes questionable (at least for that potential).
- If MD in Ge0.88Sn0.12 with vacancies yields Sn-hop activation energies close to bulk Ge (2.9–3.3 eV), then the proposed low-barrier complexation-controlled regime is not governing in the 500–700 K window.
- If strong low-T enhanced diffusion persists in samples where PAS (or other defect metrology) confirms very low vacancy-type defect density, then a non-vacancy mechanism must dominate the low-T branch.


### 1 Unaccounted for

- Oxide-capped SiGeSn at 550 °C shows near-complete suppression of near-surface substitutional Sn loss despite the theory focusing primarily on bulk Sn–V complexation; fully explaining the cap effect requires explicit surface-sink blocking and dislocation-pipe transport considerations (handled more directly by a separate surface-mediated degradation theory).  [Attiaoui et al., 2026]


## theory-4: Blocking the free surface changes Sn loss from sudden collapse to slow diffusion

Without a cap, the surface acts like a drain that quickly pulls Sn out through fast paths, leading to sudden damage. A cap blocks that drain, so Sn changes only slowly by bulk interdiffusion.


### Free surface acts as an absorbing sink that enables rapid Sn depletion via fast paths

If the surface is exposed, it can continually remove Sn, so Sn rushes there through fast paths and the film can suddenly degrade after some delay.

**Supporting evidence:**

- Uncapped Si0.08Ge0.88Sn0.04 at 550 °C shows ~50 min incubation then rapid collapse (midpoint ~74.2 min, collapse width ~1.86 min) in near-surface ellipsometry signal; post-mortem shows Sn depletion, voids with oxygen, filamentary Sn-enriched paths to surface, thickness loss, and formation of a Ge0.99Sn0.01 surface-segregation layer.  [Attiaoui et al., 2026]

- The same study argues bulk substitutional diffusion is far too slow at 550 °C (estimated diffusion length ~0.3 nm in 50 min), implying fast pathways and surface-sink-driven kinetics dominate uncapped degradation.  [Attiaoui et al., 2026]

- In pseudomorphic GeSn, uncapped samples show surface segregation above ~600 °C, whereas capped sandwiches suppress that surface accumulation, consistent with the free surface being the key sink in uncapped cases.  [Driesch et al., 2019]

- In partially relaxed GeSn, Sn-rich clusters form at the surface and at interfaces correlated with dislocation networks; pseudomorphic films show surface accumulation only, supporting the idea that fast paths plus an available sink determine where Sn ends up.  [Zaumseil et al., 2018]


### Oxide caps kinetically block Sn escape and suppress Kirkendall voiding/runaway degradation

A thin oxide cap blocks Sn from reaching the surface and stops the voiding/rapid collapse that happens when Sn can escape.

**Supporting evidence:**

- 3 nm SiO2-capped Si0.08Ge0.88Sn0.04 shows <1 at.% Sn change over 140 min at 550 °C, |ΔE2| < 20 meV, no voids, preserved uniform Sn (EDX/APT), limited strain relaxation, and far lower contact resistivity than uncapped.  [Attiaoui et al., 2026]

- Uncapped counterpart at 550 °C shows voids with oxygen, filamentary Sn-rich paths, Ge0.99Sn0.01 segregation layer, roughening, and severe thickness loss after the incubation/collapse event.  [Attiaoui et al., 2026]

- Screening in the same work indicates 5 nm Al2O3 also suppresses segregation after 550 °C/30 min.  [Attiaoui et al., 2026]

- Conceptual discussions elsewhere propose capping/H termination suppresses surface segregation and delays precipitation/phase separation, consistent with a surface-sink blocking mechanism.  [Groiss et al., 2017]


### 3 Likely outcomes

- H9 prediction (Si0.08Ge0.88Sn0.04 at 550 °C, uncapped vs 3 nm SiO2 cap, monitoring near-surface substitutional Sn loss): category = 'cap suppresses the change'; uncapped incubation time ≈ 50 minutes before the change becomes visible (order-of-magnitude tens of minutes, not seconds).
- Replacing SiO2 with Al2O3 of similar thickness (≈5 nm) will also suppress the near-surface change at 550 °C over at least ~30 min, consistent with screening evidence.
- For otherwise similar films, introducing a free surface (removing cap) will reintroduce incubation-and-collapse behavior, with earlier onset if dislocation density/fast-path density is higher.


### 2 Unknown outcomes

- If an oxide cap is intentionally made leaky (patterned nanopores), degradation will initiate preferentially at those leakage sites and propagate laterally, allowing direct mapping of sink-gated kinetics to cap integrity.
- A cap that strongly getters vacancies (rather than only blocking Sn) could further stabilize the film even when some Sn transport through the cap is possible; distinguishing these would require independent vacancy metrology.


### 2 Negative experiments

- If in-situ SE shows no difference between capped and uncapped at 550 °C (same incubation and collapse), then surface-sink gating is not the controlling factor and the dominant mechanism must be bulk or interface-limited.
- If capped samples still develop voids and rapid collapse without measurable Sn escape pathways, then voiding must be driven by another flux imbalance mechanism unrelated to Sn surface loss.


### 1 Unaccounted for

- In Ge/GeSn/Ge capped diffusion samples, the Ge cap suppresses surface segregation but still allows substantial Sn dilution into the cap/buffer (peak reduction >2× at 600 °C/10 min); the present theory explains this as sink redirection but does not quantify when redirection vs true retention should occur for different cap materials/thicknesses.  [Driesch et al., 2019]


## theory-5: Oxide caps stop Sn escape along fast paths, preventing voids and sudden failure

In uncapped films, Sn travels quickly along dislocations to the surface, where it is permanently removed; this leaves vacancies that form voids, and the voids make the process accelerate suddenly. A thin oxide cap blocks the surface sink and prevents this runaway feedback.


### Pipe-diffusion dominated Sn transport law (voiding/collapse mode)

When collapse behavior happens, Sn mainly travels along dislocations/fast paths rather than slowly through the perfect crystal lattice.

**Supporting evidence:**

- For uncapped Si0.08Ge0.88Sn0.04 at 550 °C, authors argue bulk substitutional diffusion cannot explain the kinetics, estimating a bulk diffusion length of only ~0.3 nm over the ~50 min incubation, while TEM shows filamentary Sn-enriched paths consistent with dislocation-mediated transport to the surface.  [Attiaoui et al., 2026]

- Uncapped Si0.08Ge0.88Sn0.04 shows incubation (~50 min) then abrupt optical collapse; post-mortem TEM/EDX reveals filamentary Sn-enriched features and surface/near-surface segregation consistent with a connected fast-transport network feeding the surface sink.  [Attiaoui et al., 2026]

- GeSn thermal stability study reports that partially relaxed (dislocated) GeSn exhibits much faster Sn transport/segregation and Sn-rich clustering at both surface and interface; pseudomorphic films (lacking dislocations) show surface-only accumulation and slower evolution, supporting a dislocation-enhanced transport picture.  [Zaumseil et al., 2018]

- In uncapped pseudomorphic GeSn/SiGeSn diffusion work, surface segregation appears above ~600 °C, while capped sandwich structures suppress surface segregation and instead show smoother interdiffusion into Ge; this supports the idea that fast pathways plus a free-surface sink can dominate observed Sn redistribution when uncapped.  [Driesch et al., 2019]


### Surface-sink–driven Kirkendall void nucleation and positive feedback

When the surface keeps removing Sn, vacancies pile up and form voids; voids then make Sn loss speed up suddenly.

**Supporting evidence:**

- Uncapped Si0.08Ge0.88Sn0.04 annealed 550 °C/140 min exhibits voids throughout upper region; voids contain oxygen by EDX, and authors interpret voiding as Kirkendall-type vacancy supersaturation caused by unbalanced outward Sn flux along fast paths to the surface.  [Attiaoui et al., 2026]

- The same uncapped sample shows catastrophic thickness loss (~60%), strong ellipsometric E2 blueshift (+423 meV) and rapid collapse after incubation (t0≈74 min; incubation ~50 min; collapse width ~1.9 min), consistent with a nonlinear feedback process rather than steady Fickian diffusion.  [Attiaoui et al., 2026]

- GeSn thermal stability study links enhanced Sn transport/segregation to extended defects (dislocations) and vacancy-mediated dynamics, consistent with a scenario where short-circuit transport can create strong fluxes that could generate vacancy imbalances.  [Zaumseil et al., 2018]


### Nm-scale oxide cap suppresses the sink/void feedback by blocking Sn egress

A thin, intact oxide cap removes the surface as a place for Sn to escape to, so the runaway voiding process never starts.

**Supporting evidence:**

- At 550 °C/140 min under N2 purge, uncapped Si0.08Ge0.88Sn0.04 shows incubation (~50 min) then rapid collapse (t0≈74.2 min; width ~1.86 min), large E2 blueshift (~+423 meV), voids with oxygen, roughening, thickness loss, and formation of a Ge0.99Sn0.01 segregation layer; the 3 nm SiO2-capped sample shows <1 at.% Sn change over 140 min, |ΔE2|<20 meV, no voids, minimal relaxation and preserved uniformity.  [Attiaoui et al., 2026]

- Screening in the same study indicates 5 nm Al2O3 also suppresses segregation after 550 °C/30 min, supporting the idea that an oxide barrier (not only SiO2 specifically) can block the relevant surface-mediated pathway.  [Attiaoui et al., 2026]

- Conceptual discussions in GeSn droplet-mediated decomposition work suggest capping should suppress surface segregation and delay droplet/precipitate formation by reducing surface sink strength (though not experimentally tested there).  [Groiss et al., 2017]

- Capped Ge/GeSn/Ge sandwich diffusion experiments suppress surface segregation and redirect Sn into adjacent Ge rather than allowing surface pile-up, consistent with the general principle that removing the free surface changes the dominant degradation pathway.  [Driesch et al., 2019]


### 3 Likely outcomes

- For Si0.08Ge0.88Sn0.04 annealed isothermally at 550 °C, a thin continuous oxide cap (e.g., 3 nm SiO2) will fall into the category 'cap suppresses the change' in in-situ SE, with the uncapped film showing a finite incubation time before the near-surface substitutional-Sn loss becomes visible (order: tens of minutes, comparable to ~50 min in the referenced 550 °C uncapped case).
- If the dislocation density (or connectivity of dislocations to the surface) is increased in otherwise similar uncapped films, the incubation time before collapse will decrease and the void density in post-anneal TEM will increase; capped films will show a much weaker dependence of kinetics on dislocation density (collapse suppressed).
- If an oxide cap is intentionally patterned with openings, degradation (Sn depletion, voiding) will initiate preferentially at openings and propagate laterally underneath as the local surface sink is reintroduced; capped regions away from openings remain comparatively stable.


### 3 Unknown outcomes

- In an uncapped sample annealed under extremely low oxygen chemical potential (e.g., ultra-high purity inert gas with strong oxygen getter), collapse kinetics may slow substantially and voids may show reduced oxygen decoration; if collapse is still rapid, it would imply that oxidation is not required for sink strength (segregation alone suffices).
- Replacing oxide with a mechanically compressive but Sn-impermeable dielectric (e.g., thick SiNx) could either further suppress collapse (by sealing the surface) or accelerate it (if the stress generates cracks/defects that act as new fast paths). Outcome would strongly constrain whether mechanical integrity or chemical impermeability is the limiting factor.
- Electrostatic effects from high fixed-charge caps could modify vacancy charge states and thus vacancy mobility/aggregation; if true, identical impermeability caps with different charge states would yield measurably different incubation times, separating 'barrier' from 'defect-chemistry' contributions.


### 3 Negative experiments

- If uncapped films that show SE collapse at 550 °C do not exhibit voids (confirmed by cross-sectional TEM across the affected region), then Kirkendall voiding is not necessary for collapse and the feedback-loop hypothesis is weakened.
- If capped films with verified continuous caps (no pinholes/cracks, verified by TEM/AFM and perhaps etch tests) still show the same incubation-then-collapse kinetics as uncapped, then suppression cannot be attributed to blocking the surface sink and the theory statements must be revised.
- If a verified dislocation-poor/pseudomorphic film (no connected dislocation network) nevertheless shows the same collapse kinetics and filamentary transport signatures, then pipe/short-circuit transport is not the dominant pathway in this regime.


### 2 Unaccounted for

- Droplet-mediated liquid-phase-epitaxy phase separation in high-Sn MBE Ge0.9Sn0.1 above the eutectic (~231 °C) proceeds by mobile liquid Sn droplets and is not explained by Kirkendall voiding feedback; it is a distinct degradation mode.  [Groiss et al., 2017]

- Two-regime Arrhenius behavior (low-T enhanced diffusion with EA ~1.1–1.8 eV and high-T conventional with EA ~2.9–3.1 eV) in capped Ge/GeSn/Ge sandwich diffusion experiments reflects bulk/interdiffusion kinetics rather than collapse-mode voiding; this theory does not aim to explain those regimes quantitatively.  [Driesch et al., 2019]


## theory-6: Whether Sn can move depends on who captures the vacancies first

Vacancies are needed for tin to move through the lattice. If dopants like phosphorus tie up most vacancies into dopant–vacancy complexes, tin has fewer vacancies to move with, which can slow vacancy-driven tin loss—unless fast dislocation paths or a free surface sink dominate the degradation.


### Vacancy capture hierarchy law (P dominates Sn in Ge/GeSn in studied regime)

With very high phosphorus doping, vacancies mostly bind to phosphorus; tin shows up mainly as an additional neighbor around those vacancy complexes rather than capturing vacancies first.

**Supporting evidence:**

- DFT formation enthalpy ranking: Pn–V complexes are most stable; mixed Sn–Pn–V intermediate; Sn-only vacancy complexes least favorable; authors conclude Sn does not efficiently trap vacancies compared to P and therefore does not improve P activation via vacancy trapping.  [Vohra et al., 2020]

- PAS/coincedence Doppler shows mono-vacancy-sized open-volume defects decorated by multiple P atoms (2–4 depending on P level). In GeSn:P at highest P, PAS indicates at least one Sn atom near some vacancies (Sn_pP_n–V), consistent with Sn acting as a co-decorator around an already P-decorated vacancy complex rather than dominating vacancy capture.  [Vohra et al., 2020]

- PAS/DFT work notes inward Sn relaxation around vacancies (reducing open-volume and positron trapping), consistent with Sn being present around vacancies but not necessarily implying Sn is the dominant vacancy sink compared to Pn–V.  [Vohra et al., 2020]

- Literature cited in the PAS/DFT work indicates undoped low-Sn GeSn (Sn ≤ ~6 at.%) can be stable up to 500 °C for up to 30 min (context that the relevant defect complexes persist without immediate macroscopic decomposition in this composition range).  [Vohra et al., 2020]


### Dopant-controlled vacancy availability modulates vacancy-mediated Sn interdiffusion (under surface-sink-limited conditions)

If the main way tin moves is by exchanging with vacancies in the lattice, then adding a dopant that locks up vacancies should slow tin motion and help keep tin substitutional—provided the surface isn’t acting as an easy escape route.

**Supporting evidence:**

- This statement is logically inferred (abduction/deduction) from: (1) Pn–V complexes are thermodynamically preferred over Sn-only vacancy complexes in Ge/low-Sn GeSn (vacancy capture hierarchy), and (2) vacancy-mediated Sn diffusion requires accessible vacancies as mediators; therefore sequestering vacancies into dopant–V complexes reduces vacancy availability for Sn exchange hops and Sn–V complex formation.

- Vacancy-mediated Sn diffusion is identified as a relevant microscopic mechanism in GeSn stability literature; DFT/NEB in undoped GeSn shows low activation energies for vacancy-mediated Sn hops (~0.83–0.93 eV) and experimental RTA in undoped MBE GeSn shows substitutional Sn loss interpreted via formation of Sn–vacancy complexes (VSnV). These establish that vacancy-mediated routes can control Sn stability when not overridden by surface/pipe mechanisms, motivating why vacancy availability matters.  [Zhou et al., 2025]

- Capped diffusion-sandwich experiments (Ge/GeSn/Ge; Ge/SiGeSn/Ge) demonstrate that removing the free-surface sink shifts behavior to bulk interdiffusion with measurable activation energies (two-regime behavior) rather than immediate surface segregation—consistent with a domain where bulk vacancy-mediated kinetics can matter and therefore where vacancy sequestration by dopants could modulate Sn mobility.  [Driesch et al., 2019]


### 3 Likely outcomes

- In a surface-sink-suppressed geometry (e.g., Ge/GeSn/Ge diffusion sandwich or an oxide-capped stack that blocks free-surface Sn escape), increasing P doping into the high-10^19 cm−3 regime will reduce the effective Sn interdiffusion rate at 500–650 °C relative to an undoped control with similar dislocation density, because vacancies are sequestered into Pn–V complexes.
- PAS/CDOBS vs P concentration in GeSn:P will show systematic increase in P decoration number (P2–V → P3–V/ P4–V) while the incremental Sn contribution around vacancies remains limited (mixed Sn_pP_n–V signal increases weakly or saturates), consistent with P-dominated vacancy trapping.
- If two films have similar Sn content and microstructure but one has much higher P, the higher-P film will show reduced signatures of Sn-only vacancy complexes (or reduced kinetic conversion to such complexes during mild anneals), with vacancies predominantly residing in Pn–V or mixed Sn–P–V states.


### 3 Unknown outcomes

- Fermi-level engineering could change the vacancy charge-state distribution enough to alter the dopant–V vs Sn–V stability ordering; in some doping/strain conditions this could partially invert the hierarchy and enable electrically tunable Sn stability during annealing.
- In SiGeSn, the presence of Si may modify vacancy formation energies and dopant–vacancy binding enough that P trapping is less effective (or more effective) than in GeSn, leading to composition-dependent crossovers where dopant chemistry unexpectedly accelerates Sn loss (if it increases vacancy populations more than it traps them).
- Co-doping strategies (e.g., combining P with another species that preferentially binds vacancies or changes vacancy migration) might create a regime where vacancies are immobilized without generating compensating fast paths, enabling substantially higher thermal budgets for substitutional Sn retention.


### 3 Negative experiments

- Prepare capped (surface-sink-limited) GeSn diffusion-sandwich samples with matched Sn content and dislocation density but different P levels; if heavily P-doped samples show equal or higher Sn interdiffusion rates than undoped samples across 500–650 °C, then vacancy sequestration by P is not limiting Sn mobility (or P increases vacancy supply/fast paths enough to dominate).
- Direct defect spectroscopy/DFT under relevant Fermi-level conditions: if Sn–V (or VSnV precursor) binding becomes stronger than Pn–V stability under the actual charge states in these films, contradicting the assumed hierarchy, the theory’s mechanism fails for that regime.
- If PAS after anneal shows a large increase of Sn-only vacancy complexes in heavily P-doped GeSn compared with undoped controls (at comparable vacancy supply), then P is not the dominant vacancy trap in the kinetic/thermodynamic regime relevant to annealing.


### 2 Unaccounted for

- Oxide capping (3 nm SiO2, 5 nm Al2O3) at 550 °C can suppress surface-mediated degradation/voiding and preserve substitutional Sn in SiGeSn for 140 min; this theory does not explain that effect because it concerns bulk vacancy-trap competition, not surface-sink blocking and pipe-diffusion shutoff.  [Attiaoui et al., 2026]

- Droplet-mediated liquid transport above the Ge–Sn eutectic in high-Sn GeSn (e.g., Ge0.9Sn0.1) dominates decomposition and is not addressed by vacancy-trap competition.  [Groiss et al., 2017]
