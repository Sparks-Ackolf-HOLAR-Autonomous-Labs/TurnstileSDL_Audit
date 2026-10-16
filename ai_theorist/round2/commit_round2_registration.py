#!/usr/bin/env python3
"""Ledger entry for AI-theorist round 2 (third theorist, another model family),
written before any round-2 output exists."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); AT = os.path.dirname(HERE); MT = os.path.dirname(AT)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
files = ["round2/PROTOCOL.md", "round2/theorizer/payload_sige_transport.json",
         "round2/theorizer/payload_gesn_kinetics.json", "theorist_brief.md", "grading_rubric.md"]
e = led.append("commitment", {
    "op_id": "ai-theorist-round2-registration",
    "rests_on": [122, 123, 124],
    "files_sha256": {f: sha(os.path.join(AT, f)) for f in files},
    "theorist": "Asta Theorizer (gpt-5.2 generation, gpt-5-mini extraction), literature-grounded, two runs",
    "mapper": "Claude subagent without tools; answers must quote the theory statement they rest on",
    "statement": "Round 2 fixed before any Theorizer output: payloads, mapping rule and the unchanged round-1 rubric",
})
assert led.verify_chain(); print("seq", e["seq"], e["entry_hash"])
