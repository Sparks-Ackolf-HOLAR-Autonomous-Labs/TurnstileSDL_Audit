#!/usr/bin/env python3
"""Hash the theorist brief, the grading rubric and the (still unpublished)
outcome key onto the campaign ledger before any theorist answers.
Usage: commit_registration.py <path to outcome_key.json>"""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); MT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
e = led.append("commitment", {
    "op_id": "ai-theorist-pilot-registration",
    "brief": "ai_theorist/theorist_brief.md", "brief_sha256": sha(os.path.join(HERE, "theorist_brief.md")),
    "rubric": "ai_theorist/grading_rubric.md", "rubric_sha256": sha(os.path.join(HERE, "grading_rubric.md")),
    "outcome_key_sha256": sha(sys.argv[1]),
    "statement": "AI-theorist pilot: brief, rubric and outcome key fixed before any theorist answer; key published only after answers are hashed",
})
assert led.verify_chain(); print("seq", e["seq"], e["entry_hash"])
