#!/usr/bin/env python3
"""Record the published outcome key and the grades on the campaign ledger."""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); MT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
sha = lambda f: hashlib.sha256(open(os.path.join(HERE, f), "rb").read()).hexdigest()
g = json.load(open(os.path.join(HERE, "grades.json")))
e = led.append("analysis", {"op_id": "ai-theorist-pilot-grades", "rests_on": [122, 123],
    "outcome_key_sha256": sha("outcome_key.json"), "grades_sha256": sha("grades.json"),
    "summary": {k: {kk: v for kk, v in g[k].items() if kk != "per_question"} for k in g if isinstance(g[k], dict)}})
assert led.verify_chain(); print("seq", e["seq"])
