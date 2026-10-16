#!/usr/bin/env python3
"""Ledger entry for AI-theorist round 2b, written before any round-2b output exists."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); AT = os.path.dirname(HERE); MT = os.path.dirname(AT)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
files = ["round2/PROTOCOL_2b.md", "round2/theorizer/payload_r2b_carbon_sic.json",
         "round2/theorizer/payload_r2b_strained_films.json", "round2/theorizer/payload_r2b_potentials.json",
         "round2/mapper_prompt.md", "theorist_brief.md", "grading_rubric.md"]
e = led.append("commitment", {
    "op_id": "ai-theorist-round2b-registration",
    "rests_on": [122, 124, 125, 128, 129],
    "files_sha256": {f: sha(os.path.join(AT, f)) for f in files},
    "theorist": "Asta Theorizer, three narrow runs, knowledge cut-off 2026-01",
    "items": ["H1b", "H5", "H6", "H7"],
    "statement": "Round 2b fixed before any Theorizer output: payloads with a pre-2026 cut-off, the round-2 mapping rule and the unchanged rubric",
})
assert led.verify_chain(); print("seq", e["seq"], e["entry_hash"])
