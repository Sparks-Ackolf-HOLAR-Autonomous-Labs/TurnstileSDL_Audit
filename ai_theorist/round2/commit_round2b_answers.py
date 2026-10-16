#!/usr/bin/env python3
"""Hash the round-2b Theorizer outputs and the mapped answer file onto the ledger before grading.
Task ids were recovered from the submitting job's log (the run ended before saving them)."""
import hashlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); AT = os.path.dirname(HERE); MT = os.path.dirname(AT)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
sha = lambda p: hashlib.sha256(open(os.path.join(AT, p), "rb").read()).hexdigest()
runs = ("carbon_sic", "strained_films", "potentials")
files = (["answers/theorist_C_asta_theorizer_round2b.json", "round2/mapper_prompt_2b.md", "round2/mapper_raw_output_2b.json",
          "round2/theorizer/theories_round2b.md"] + [f"round2/theorizer/result_r2b_{n}.json" for n in runs])
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
if any(e["payload"].get("op_id") == "ai-theorist-round2b-answers" for e in led.entries):
    sys.exit("already committed")
e = led.append("batch_commitment", {
    "op_id": "ai-theorist-round2b-answers", "registration_seq": 136,
    "files_sha256": {f: sha(f) for f in files},
    "theorizer_tasks": {n: open(os.path.join(HERE, "theorizer", f"submit_r2b_{n}.json")).read().strip() for n in runs},
    "mapper": "claude -p --tools '' --model claude-sonnet-5-5, 1 turn, no tool access; ids H1b, H5, H6, H7 only",
    "statement": "round-2b answers hashed before grading; graded as a separate row, round 2's 4 of 10 unchanged",
})
assert led.verify_chain(); print("seq", e["seq"])
