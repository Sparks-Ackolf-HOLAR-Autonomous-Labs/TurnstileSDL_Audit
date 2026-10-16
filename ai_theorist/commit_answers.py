#!/usr/bin/env python3
"""Hash the theorists' answers onto the campaign ledger before the outcome key is published."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); MT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
files = {f: hashlib.sha256(open(os.path.join(HERE, "answers", f), "rb").read()).hexdigest()
         for f in sorted(os.listdir(os.path.join(HERE, "answers")))}
e = led.append("batch_commitment", {
    "op_id": "ai-theorist-pilot-answers", "registration_seq": 122, "answers_sha256": files,
    "theorists": {"theorist_A_sonnet.json": "Claude Sonnet subagent, no tools, blinded brief",
                  "theorist_B_haiku.json": "Claude Haiku subagent, no tools, blinded brief"},
    "statement": "answers hashed before the outcome key is opened; O1-O3 stay open for later runs"})
assert led.verify_chain(); print("seq", e["seq"])
