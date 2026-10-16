# AI-theorist round 2: results (campaign-record entries 125 registration, 128 answers, 129 grades)

## What ran
- Theorist C: the Asta Theorizer (Ai2), two runs (`theorizer/result_*.json`,
  flattened in `theorizer/theories_round2.md`). Theory generation by
  `gpt-5.2`, per-paper extraction by `gpt-5-mini`. It retrieved and extracted
  5 papers for the SiGe transport run and 8 for the GeSn run (15 requested;
  the rest failed to download), and wrote 6 theories per run.
- Mapping onto the brief: one call of Claude Sonnet with every tool disabled
  (`claude -p --tools ""`, 1 turn; `mapper_raw_output.json`). A category
  counts only if the answer quotes, word for word, the theory statement it
  rests on.

## Grades (round-1 rubric, unchanged)

| Q | Theorist C | A (Sonnet) | B (Haiku) | Outcome |
|---|---|---|---|---|
| H1 2 nm SiC vs continuum bracket | above (wrong) | inside (wrong) | inside (wrong) | below |
| H1b particle plus Si-rich shell | no basis | wrong | right | higher |
| H2 Ge-rich corner | physics (right) | right | right | physics |
| H3 BTE minimum at 1100 K | no basis | right | right | 0.4 to 0.6 |
| H4 amorphous SiGe size dependence | rises with length (right) | wrong | wrong | rises with length |
| H5 Tersoff vs BTE, pure Si | no basis | right | right | agree within 30 % at 1100 K |
| H6 carbon location | no basis | right | right | SiC favoured |
| H7 strained film, cross-plane | no basis | wrong | wrong | increase |
| H8 sintered/BTE ratio | below 0.7 (right; outcome is built from published data) | wrong | right | below 0.7 |
| H9 oxide cap on SiGeSn | not counted: quote paraphrased, and the outcome's source preprint was among the papers retrieved | right | right | cap suppresses |

- Answered 4 of 10; 3 of the 4 right (2 of 3 if H8 is set aside as a
  value the literature already contains). On the same 4 items, A had 1 and
  B had 2.
- **The literature-grounded theorist got H4 right, which both round-1
  theorists missed.** Its basis is a published study of mode localisation
  in amorphous alloys: low-frequency modes still propagate, so a longer box
  admits more of them. Of the three results the campaign found only by
  simulation (H1, H4, H7), it got one right, one wrong in a third direction
  (H1: "above", where A and B said "inside" and the result is "below"), and
  abstained on one (H7).
- **It abstains where the literature is silent** (H3, H5, H6, H7 are
  method-specific numbers), which the round-1 theorists never did: they
  answered every question, including the ones they got wrong at stated
  confidence 0.4 to 0.75.
- **A literature-grounded theorist can retrieve the answer instead of
  forecasting it.** For H9 the Theorizer found the very 2026 preprint the
  outcome came from. Any future brief for such a theorist must either set
  `knowledge_cutoff_year/month` before the outcome's publication or drop
  items whose outcome is published.

## Open predictions, now three-way

| Q | A (Sonnet) | B (Haiku) | C (Theorizer) | Tested by |
|---|---|---|---|---|
| O1 Sn-vacancy binding, MACE-MP-0 | > 0.3 eV | 0 to 0.3 eV | > 0.3 eV | P4 T1 statics (CHPC job 16162740) |
| O2 Sn hop activation energy | below 1.1 eV | 2.9 to 3.3 eV | 1.1 to 1.8 eV | P4 T1 MD (CHPC arrays 16162739, 16162856) |
| O3 newer foundation potential | shift > 0.3 eV | within 0.3 eV | no basis | P5 version change |

On O2 the three theorists now take all three categories, so the T1 result
refutes at least two of them whatever it is.

## Limits
One mapper call from the Claude family translated C's theories into the
form; the quote rule bounds but does not remove its influence. The
Theorizer's mission statement carried the brief's questions word for word,
so its theories address them directly. Ten graded items.

## Round 2b (campaign-record entries 136 registration, 140 answers, 141 grades)

Three narrow Theorizer runs (`PROTOCOL_2b.md`, cut-off January 2026) on the
topics round 2 never read. Task ids: carbon_sic 08c7035b, strained_films
d36b67d8, potentials 492b3075 (recovered from the submitting job's log;
the run ended before saving them). Theories flattened in
`theorizer/theories_round2b.md`; same mapper (Claude Sonnet, no tools) and
quote rule (`grade_round2b.py`, `grades_round2b.json`).

| Item | Papers read | Mapped answer | Outcome | Graded |
|---|---|---|---|---|
| H1b SiC particle + Si-rich shell vs bare alloy | 5 (none on SiC in SiGe thermal transport) | no basis | higher | not answered |
| H6 SiC precipitation energy | 5 | no basis (theories say substitutional C is metastable, give no energy) | SiC favoured, 1.55 eV | not answered |
| H5 Tersoff vs DFT-BTE, bulk Si, 1100 K | 11 | Tersoff higher by more than 30 % | agree within 30 % | wrong |
| H7 cross-plane kappa, coherent Si0.5Ge0.5 on Si | 5 | decrease (-8 %) | increase (+12 %) | wrong |

Answered 2 of 4, right 0 of 2. On the same two items the round-1 theorists
scored 1 of 2 each.

Reading:
- Narrowing the search did raise coverage (H5 and H7 now have a quoted
  basis), but the answers it enabled were wrong in both cases, and in the
  direction the general literature points: Tersoff is known to over-predict
  pure-Si kappa at 300 K, and the theorist extended that to 1100 K, where
  this campaign's own HNEMD and almaBTE agree within 25 %; strain in most
  published films lowers kappa through defects, while this campaign's
  coherent, defect-free MD raised it. Both outcomes are simulation-only
  findings, the class the round-1 theorists also missed.
- For H1b and H6 the narrowed search still found no paper that addresses
  the question; the mapper withheld both as the rule requires.
- So literature grounding alone does not supply what this campaign's own
  simulations measured. For P1-P5 the AI theorist stays a source of
  conjectures to be tested, not of values.
