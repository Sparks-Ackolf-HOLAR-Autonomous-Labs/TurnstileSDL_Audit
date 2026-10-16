# AI-theorist round 2: a theorist from another model family, grounded in literature

Registered on the campaign ledger (entry 125) before any round-2 output exists.

## Theorist C: Asta Theorizer (Ai2), literature-grounded
- Service: Asta Theorizer via `asta generate-theories literature-theory-generation`
  (asta CLI 0.104.1). Theory generation model `gpt-5.2`, per-paper extraction
  model `gpt-5-mini` (service defaults), so the family differs from the
  round-1 Claude theorists.
- Two runs, payloads in `theorizer/payload_*.json` (hashed below):
  - `sige_transport`: questions H1 to H8 and O3 (heat transport and carbon in SiGe);
  - `gesn_kinetics`: questions H9, O1 and O2 (Sn and vacancies in GeSn/SiGeSn).
- The payloads carry the brief's questions as the mission statement, word for
  word, but none of the campaign's results. The Theorizer reads published
  papers only; none of this campaign's results is published.
- Settings: 15 papers per run, accuracy-focused, novelty evaluation off.

## Mapping theories onto the brief's answer form
The Theorizer returns theories (laws with supporting papers), not the
brief's JSON form. A mapper fills the form from the theory text only:
- Mapper: a Claude subagent with no tool access, given only
  `theorist_brief.md` and the two Theorizer result files. It must answer
  "no basis" (category null) for any question the theories do not address,
  rather than use its own knowledge.
- The mapper's Claude family is a known limit: its own priors can leak into
  the categories. To bound this, it must quote the theory statement each
  answer rests on (field `basis`); answers without a quote are graded as
  "no basis".

## Grading
The round-1 rubric (`grading_rubric.md`, ledger 122) applies unchanged.
The outcome key is already public (ledger 124), so blindness rests on (a)
the Theorizer reading only published literature and (b) the mapper having
no file or network access. Both are logged.

## Questions this round asks
1. Does a literature-grounded theorist from another model family share the
   round-1 misses (H1, H4, H7: results the campaign found only by simulation)?
2. On the open questions O1 to O3, does it side with theorist A or B, or neither?

## Not done in this round
A non-Claude theorist without literature access (local Qwen on the DGX)
was planned but not run: the DGX GPU was held by another user's vLLM job
(96 % utilisation) and the operator reserved the DGX for other work.
