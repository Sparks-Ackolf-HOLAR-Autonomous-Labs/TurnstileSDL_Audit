#!/usr/bin/env python3
"""Verifier step for any committed batch: every file named in a raw
manifest must exist, be tracked (not git-ignored), and match its hash;
and the manifest's Merkle root must equal the ledger entry's. This is the
check that would have caught an earlier .gitignore loss of raw files at
commit time. Usage: python3 verify_raw.py  (exit 1 on any failure)
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import leaf_hash, merkle_root  # noqa: E402

led = {e["payload"].get("stage"): e for e in
       (json.loads(l) for l in open(os.path.join(MT, "phase_c", "ledger_campaign.jsonl")))
       if e["kind"] == "batch_result" and e["payload"].get("stage")}
bad = 0
for m in sorted(glob.glob(os.path.join(HERE, "raw", "manifest_*.json"))):
    stage = os.path.basename(m)[len("manifest_"):-5]
    man = json.load(open(m))
    leaves = []
    for rid in man:  # manifest order is sorted; ledger leaves follow design order
        for f, h in man[rid].items():
            p = os.path.join(HERE, "raw", rid, f)
            ok = os.path.exists(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() == h
            ign = subprocess.run(["git", "check-ignore", "-q", p], cwd=HERE).returncode == 0
            if not ok or ign:
                bad += 1
                print("FAIL", stage, rid, f, "missing/mismatch" if not ok else "git-ignored")
    design = json.load(open(os.path.join(HERE, "endpoint_campaign_design.json")))
    order = [r["run_id"] for r in design["runs"] if r["stage"] == stage]
    root = merkle_root([leaf_hash({"run_id": rid, "files": man[rid]}) for rid in order])
    same = root == led[stage]["payload"]["merkle_root"]
    print(stage, "files ok" if not bad else "", "merkle root matches ledger seq",
          led[stage]["seq"], same)
    bad += 0 if same else 1
sys.exit(1 if bad else 0)
