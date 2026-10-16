# AI-theorist pilot (9 October 2026)

Question: what can an AI theorist do inside the P1 to P5 campaign, where
concepts and theories are built and then tested with the papers' tools?

What was run: two AI theorists (Claude Sonnet and Claude Haiku subagents, no
tool access, tool calls logged as 0) answered a blinded brief of nine
questions the campaign had already settled (H1 to H9) and three it has not
(O1 to O3). Each answer is a mechanism, a category with a probability, a
number with an 80 % interval, a falsifying run and a stated reach. The Asta
Theorizer was the intended first theorist but could not run (ASTA_TOKEN
expired, HTTP 401).

Order on the campaign record (each step pushed before the next):

| Seq | Entry | File |
|---|---|---|
| 122 | brief, rubric and outcome-key hashes, key kept off the repository | `theorist_brief.md`, `grading_rubric.md`, sha256 of `outcome_key.json` |
| 123 | both answer files hashed | `answers/*.json` |
| 124 | key published, grades recorded | `outcome_key.json`, `grades.json` |

`grade.py` refuses to run if the key or an answer file differs from the
hashes on the campaign record.

## Results

| | Category right | Number within tolerance | Outcome inside own 80 % interval | Mean Brier |
|---|---|---|---|---|
| Theorist A (Sonnet) | 5/10 | 2/10 | 6/10 | 0.225 |
| Theorist B (Haiku) | 7/10 | 4/10 | 5/10 | 0.200 |
| Data-only rule (no theorist) | 2/8 | 1/8 | n/a | n/a |

Per question (category right for A, B; the outcome):

| Q | Topic | A | B | Outcome on the campaign record |
|---|---|---|---|---|
| H1 | 2 nm SiC in SiGe vs continuum bracket | no | no | below the bracket (30 % vs 40 to 75 %) |
| H1b | particle plus Si-rich shell vs bare alloy | no | yes | higher, 4 to 14 % |
| H2 | Ge-rich corner flagged as fault | yes | yes | physics (11.5 W/mK at x = 0.97) |
| H3 | almaBTE at x = 0.7, 1100 K; minimum | yes | yes | 4.95 W/mK; minimum at x = 0.505 |
| H4 | amorphous SiGe size dependence | no | no | rises with length (ratio 1.42) |
| H5 | Tersoff/BTE for pure Si | yes (1100 K) | yes (1100 K) | 1.7x at 300 K, both theorists' numbers wrong (1.3, 0.8) |
| H6 | where carbon goes | yes | yes | SiC favoured by 1.55 eV (theorists 1.0 and 0.5) |
| H7 | cross-plane kappa of strained film | no | no | +12 % at 300 K |
| H8 | sintered/BTE ratio | no | yes | 0.50 |
| H9 | oxide cap on SiGeSn at 550 C | yes | yes | cap suppresses; incubation about 50 min (theorists 20 and 5) |

## What it shows

1. **The theorists know textbook physics and miss what the simulations
   found.** Both get the dilute-limit rise toward pure Ge (H2), the
   mid-composition minimum (H3), SiC precipitation (H6) and surface-driven
   Sn loss (H9). Both miss the three results the campaign found only by
   running: propagon transport in Tersoff amorphous SiGe (H4), the strain
   increase of cross-plane kappa (H7), and a 2 nm particle scattering less
   than the continuum floor (H1). Their numbers for method-specific
   quantities are off (H5: Tersoff overshoots BTE by 1.7x at 300 K; H6
   magnitude).
2. **Two theorists agreeing is not two independent sources.** They agreed
   on 8 of 10 categories and were both wrong on 3 of those 8 (H1, H4, H7),
   with stated confidence 0.4 to 0.75. This is the same lesson as the two
   Tersoff MD sources ("two students with the same textbook").
3. **Where they disagree, a run is worth buying.** They disagreed on H1b and
   H8; one of each pair was right. Disagreement marks a discriminating
   experiment.
4. **On the one decision that cost the campaign runs, a theorist would have
   set the right prior.** The registered detector set aside the Ge-rich
   corner as a fault; both theorists said "physics" (0.7 and 0.8) with the
   right value (12 vs 11.5 W/mK). Under the P1 rules this changes the label
   (candidate exceptional instead of set aside), not the purchase: the
   replication is still bought.

Limits: one brief, ten graded questions, two models from one family, and
the outcomes existed in the repository while the theorists answered
(blindness rests on the theorists having no tool access, which is logged).
The questions were written by the same agent that knew the outcomes, so the
wording may lean towards or away from the answer.

## Open predictions (graded later by the registered rubric)

| Q | Theorist A | Theorist B | Will be tested by |
|---|---|---|---|
| O1 Sn-vacancy binding in Ge0.88Sn0.12, MACE-MP-0 | bound > 0.3 eV (0.35) | bound 0 to 0.3 eV (0.20) | P4 stage T1 static check |
| O2 Sn hop activation energy, MACE-MD 500 to 700 K | below 1.1 eV (0.9) | bulk-like 2.9 to 3.3 eV (2.6) | P4 stage T1 MD |
| O3 carbon location with a newer foundation potential | sign holds, shift > 0.3 eV (1.3) | sign holds, within 0.3 eV (0.4) | P5 model-version revision |

The theorists disagree on all three, so each of these runs discriminates.
