#!/usr/bin/env python3
"""Close the P2 endpoint campaign on the ledger, exactly per the
pre-registered restore_rule: if analysis_results.json says the restore
condition holds, append a `restore` shard operation lifting
scope-limit-alloys-2026-09-27 over the pre-registered domain; otherwise
append a `gate_failure` entry naming the failing gate(s), and the
scope-limit stays live. Requires all stages committed. Idempotent.
Usage: python3 analyze_campaign.py && python3 restore.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402

design = json.load(open(os.path.join(HERE, "endpoint_campaign_design.json")))
res = json.load(open(os.path.join(HERE, "analysis_results.json")))
need = set(design["protocol"]["stage_order"])
if set(res["committed_stages"]) != need:
    sys.exit(f"REFUSING: stages committed {res['committed_stages']}")
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
op_id = "close-" + design["campaign"]
if any(e["payload"].get("op_id") == op_id for e in led.entries):
    sys.exit("already closed")
r = res["restore"]
if r["condition_met"]:
    e = led.append("shard_operation", {
        "op": "restore", "op_id": op_id,
        "lifts": design["restore_rule"]["lifts"],
        "domain_after": {"x": [0.0, 1.0], "T_K": [300] + r["T_added"],
                         "note": "endpoint temperatures not in T_K stay "
                                 "scope-limited"},
        "evidence": {"states": res["states"], "gates": res["gates"],
                     "analysis_file": "gpumd/production/analysis_results.json"},
        "rule": design["restore_rule"]["condition"]})
else:
    e = led.append("gate_failure", {
        "op_id": op_id, "restore_condition": r,
        "gates": res["gates"],
        "consequence": "no restore; scope-limit-alloys-2026-09-27 stays "
                       "live (negative result reported, not rerun)"})
assert led.verify_chain()
print(e["kind"], "at seq", e["seq"])
