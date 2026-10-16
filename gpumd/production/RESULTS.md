# GPUMD endpoint campaign: results (paper 2's pre-registered experiment)

Closed 2026-09-29. Order of events on the campaign
campaign record (`../../phase_c/ledger_campaign.jsonl`):

| seq | entry |
|---|---|
| 2 | pre-registration: design SHA-256 `6bc5c8b6...`, 33 runs, gates, restore rule, predictions (2026-09-28, pushed before any run directory existed) |
| 8 | stage S0 (alloy cross-check) raw outputs committed |
| 15-17 | stages S1 (300 K anchors), S2 (size check), S3 (temperature sweep) raw outputs committed, before analysis |
| 18 | `gate_failure`: the pre-registered restore condition is **not met**; the alloys-only scope-limit stays live |

All 33 runs finished with exit status 0 (serial, about 20 min per 5 ns
4096-atom run on the GB10). The analysis is `analyze_campaign.py`
exactly as committed; its full output is `analysis_results.json`.

## Point estimates (W/mK; mean over seeds, seed SE)

| state | lower F_e | higher F_e | P1 linearity gate | BTE-DFT party |
|---|---|---|---|---|
| Si 300 K | 423 +/- 67 (F_e 5e-6, n 3) | 284 +/- 9 (1e-5, n 3) | **fail** | 160.5 |
| Si 700 K | 114 +/- 10 (1e-5, n 2) | 89.5 +/- 0.005 (2e-5, n 2) | **fail** | 63.8 |
| Si 1100 K | 48 +/- 19 (2e-5, n 2) | 54 +/- 4 (4e-5, n 2) | pass | 40.5 |
| Ge 300 K | 107 +/- 7 (1e-5, n 3) | 89 +/- 4 (2e-5, n 3) | **fail** | 57.1 |
| Ge 700 K | point failed (one of two runs failed R3, drift z 5.0) | 38 +/- 2 (4e-5, n 2) | **fail** | 25.7 |
| Ge 1100 K | 15 +/- 3 (4e-5, n 2) | 21 +/- 2 (8e-5, n 2) | pass | 16.7 |
| SiGe x 0.5, 300 K | 2.23 +/- 0.22 (2e-4, n 3) | | P3 pass (rNEMD 1.80) | 6.49 |

S2 size check (Si 300 K, F_e 1e-5): the 16x8x8 box gave 287 (seed 55016)
and 350 (seed 55017, failed R3 with drift z 5.3), so the point has one
valid run and P2 cannot be evaluated; the one valid run agrees with the
8x8x8 estimate (284).

Figure: `../../papers/paper2_adv_intell_discov/figures/endpoint_campaign.png`
(`make_endpoint_figure.py`).

## Verdict, as pre-registered

Restore condition = S1 runs valid AND P1 for both Si and Ge at 300 K AND
P2. Here P1 fails for both elements at 300 K and P2 has no estimate, so
**no restore**. The campaign record stores the failing gates (seq 18); the
negative result is reported, not rerun silently. Predictions (reported,
not gating): k_Si > k_Ge at 300 K and monotone decrease with T hold; the
300 K Si value lies above the predicted 150-300 band; the endpoint values
agree with the BTE-DFT party within the pre-stated allowance at 1100 K
only (Si 51 vs 40.5, Ge 18 vs 16.7).

## Diagnosis (post-hoc, clearly separated from the verdict)

1. **The gate's uncertainty model was fragile (a design flaw, ours).**
   The P1 gate width uses the seed standard error from n = 2 or 3 seeds.
   Such an SE is itself very noisy and can collapse by chance: at Si 700 K
   the two seeds agree to 0.01 W/mK, giving SE 0.005 while each run's own
   block SEM is 13 to 17 W/mK. A disclosed post-hoc variant that floors
   each point's SE at the pooled within-run SEM (SE = max(seed SE,
   sqrt(sum of run SEM^2)/n)) passes P1 at 300 K for both Si and Ge and at
   Si 700 K; Ge 700 K still fails (one lower-F_e run left). Even under
   that variant the restore would still fail, because P2 has only one
   valid run. The negative verdict is therefore robust to the flaw; the
   flaw matters for how a v2 is designed.
2. **The 300 K runs are under-powered.** At F_e = 5e-6 a 5 ns Si run has a
   block SEM near 25% of its value; lower-F_e point estimates sit above
   the higher-F_e ones in three of four low-temperature comparisons
   (ratios 1.49, 1.28, 1.20), which is either noise at this power or a
   genuine F_e dependence, and this campaign cannot tell the two apart.
3. **The physics signal that is solid.** At 1100 K both elements pass
   linearity and the HNEMD values agree with the first-principles BTE
   party within about 25%: two independent method families (classical
   Tersoff MD with a valid many-body heat current, and DFT phonons with
   a Boltzmann solution) agree on the high-temperature endpoints. At
   300 K the Tersoff HNEMD values exceed both BTE-DFT and experiment by
   roughly a factor of 1.6 to 1.8 even at the better-behaved higher F_e,
   so a restore at 300 K would have imported a documented potential
   bias into the alloy law's endpoint anchors. The pre-registered
   prediction band (150-300 W/mK) came from this project's own short
   validation runs, not from a verified literature value; the HNEMD
   method paper (Fan et al., Phys. Rev. B 99, 064308, 2019) benchmarks
   crystalline Si and must be read against these numbers before the
   paper states whether Tersoff-1989 Si at 300 K is known to sit this
   high.

## What a v2 would need (not launched at closure)

A new pre-registration (a v2 is a new experiment, never an edit of this
one): 20 ns runs, 5 seeds per point, F_e in {1e-5, 2e-5} for both
elements at 300 K, three seeds for the size check, and an uncertainty
rule fixed in advance that floors the SE at the within-run SEM. Cost at
the measured 4 min per ns: about 35 GPU hours serial on the GB10, or a
few wall-clock hours if GPUMD is built on a CHPC guest GPU partition.
A narrower alternative that the data already support: pre-register a
high-temperature-only restore (T >= 1100 K) with a fresh confirmation
batch, since that is where both method families agree.
