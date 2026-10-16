#!/usr/bin/env python3
"""Pre-register the v2 GPUMD endpoint campaign (copy of ../production/preregister.py) on the campaign ledger.

Appends one `preregistration` entry to ../../phase_c/ledger_campaign.jsonl
carrying the SHA-256 of endpoint_v2_design.json and a Merkle root
over its run rows (so any single run can later be proven to belong to
the committed design with a membership proof), and writes
PREREGISTERED_SHA256 next to the design. The entry, the design, and
this file are committed and pushed to git before make_runs.py creates
any run directory; the git commit time is the public timestamp.

Idempotent: a second call with the same design hash is a no-op.
Usage: python3 preregister.py
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(MT, "pilot", "src"))

from ledger import Ledger, leaf_hash, merkle_root  # noqa: E402

LEDGER = os.path.join(MT, "phase_c", "ledger_campaign.jsonl")
DESIGN = os.path.join(HERE, "endpoint_v2_design.json")


def main():
    blob = open(DESIGN, "rb").read()
    sha = hashlib.sha256(blob).hexdigest()
    design = json.loads(blob)
    led = Ledger(LEDGER)
    for e in led.entries:
        if e["payload"].get("design_sha256") == sha:
            print("already pre-registered at seq", e["seq"])
            return
    root = merkle_root([leaf_hash(r) for r in design["runs"]])
    entry = led.append("preregistration", {
        "op_id": "prereg-" + design["campaign"],
        "campaign": design["campaign"],
        "paper": design["paper"],
        "design_file": "gpumd/production_v2/endpoint_v2_design.json",
        "design_sha256": sha,
        "runs_merkle_root": root,
        "n_runs": design["n_runs"],
        "gates": sorted(design["acceptance"]),
        "restore_rule": {k: design["restore_rule"][k] for k in ("T300", "T700_T1100")},
        "targets_op": design["restore_rule"]["lifts"],
        "statement": "v2 design, gates, per-temperature restore rule, and "
                     "predictions fixed before any v2 run exists; v1 and smoke "
                     "outputs are never pooled",
    })
    assert led.verify_chain()
    with open(os.path.join(HERE, "PREREGISTERED_SHA256"), "w") as f:
        f.write(f"{sha}  endpoint_v2_design.json  ledger_seq="
                f"{entry['seq']}  entry_hash={entry['entry_hash']}\n")
    print("pre-registered: seq", entry["seq"], "design", sha,
          "runs root", root)


if __name__ == "__main__":
    main()
