# AI-theorist round 2b: narrow Asta Theorizer runs on the topics round 2 never read

Registered on the campaign ledger before any round-2b output exists
(operator go, issue 55, 9 Oct 2026: "the ASTA token is working again, do we
still need anything from it? If so, include them").

Why: round 2 answered 4 of 10 items. The six it left blank were withheld by
the quote rule because its SiGe run downloaded 5 of 15 papers, none on
carbon in SiGe, strained films, or method comparisons (`WHY_4_OF_10.md`).

What changes from round 2 (everything else is unchanged):
- Three narrow runs instead of one broad one, each with its own question
  and with the brief's items for that topic copied word for word as the
  mission statement:
  - `payload_r2b_carbon_sic.json`: H1b, H6 (H1 text included as context;
    H1 was answered in round 2 and is not re-graded);
  - `payload_r2b_strained_films.json`: H7;
  - `payload_r2b_potentials.json`: H5.
- Knowledge cut-off: papers published before January 2026 only, so the H9
  case (the Theorizer finding the paper that holds the outcome) cannot recur.
- Not asked: H3 (a single code's number at one point; no literature-only
  theorist can supply it) and H9 (disqualified in round 2).
- Same service settings: 15 papers per run, accuracy-focused, novelty
  evaluation off, service-default models (gpt-5.2 generation, gpt-5-mini
  extraction).

Mapping and grading: the round-2 mapper rule (Claude subagent without
tools, every answer must quote the theory statement it rests on, else "no
basis") and the round-1 rubric (`../grading_rubric.md`, ledger 122). Round
2b answers are reported as a separate row; they do not overwrite round 2's
4 of 10.

Blindness: the outcome key is public (ledger 124). Blindness rests on the
cut-off date (all outcomes are unpublished campaign results from Sept-Oct
2026) and on the mapper having no file or network access.
