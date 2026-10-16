#!/usr/bin/env python3
"""Hash the round-2 Theorizer outputs and the mapped answer file onto the ledger before grading."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); AT = os.path.dirname(HERE); MT = os.path.dirname(AT)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
sha = lambda p: hashlib.sha256(open(os.path.join(AT, p), "rb").read()).hexdigest()
files = ["answers/theorist_C_asta_theorizer.json", "round2/mapper_prompt.md", "round2/mapper_raw_output.json",
         "round2/theorizer/result_sige_transport.json", "round2/theorizer/result_gesn_kinetics.json",
         "round2/theorizer/theories_round2.md"]
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
e = led.append("batch_commitment", {
    "op_id": "ai-theorist-round2-answers", "registration_seq": 125,
    "files_sha256": {f: sha(f) for f in files},
    "theorizer_tasks": {"sige_transport": "a3cdd4bd-d1ed-4fef-9e61-a2450c7263ee", "gesn_kinetics": "6bca228d-d035-4c30-a2cc-9f9f939e0f14"},
    "mapper": "claude -p --tools '' --model claude-sonnet-5-5, 1 turn, no tool access",
    "statement": "round-2 answers hashed before grading; O1 and O2 open for P4 T1 (ledger 126), O3 open for P5",
})
assert led.verify_chain(); print("seq", e["seq"])
