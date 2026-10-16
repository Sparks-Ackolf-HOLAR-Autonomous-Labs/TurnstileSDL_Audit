#!/usr/bin/env python3
"""Grade the theorists and the data-only baseline against the outcome key, per grading_rubric.md."""
import hashlib, json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); MT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
reg = led.entries[122]["payload"]
key_path = os.path.join(HERE, "outcome_key.json")
assert hashlib.sha256(open(key_path, "rb").read()).hexdigest() == reg["outcome_key_sha256"], "key changed since seq 122"
for f, h in led.entries[123]["payload"]["answers_sha256"].items():
    assert hashlib.sha256(open(os.path.join(HERE, "answers", f), "rb").read()).hexdigest() == h, f
key = json.load(open(key_path)); base = key["baselines"]
Q = ["H1", "H1b", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]

def value_hit(k, v):
    if v is None: return None
    o = key[k]
    if "tol_abs" in o: return int(abs(v - o["value"]) <= o["tol_abs"])
    return int(v > 0 and abs(math.log(v / o["value"])) <= o["tol_logratio"])

def grade(ans):
    rows = {}
    for k in Q:
        a = ans[k]; hit = int(a["category"] == key[k]["category"])
        r = a.get("value_range")
        rows[k] = {"category": a["category"], "cat_hit": hit, "brier": round((a["p_category"] - hit) ** 2, 3),
                   "value": a["value"], "value_hit": value_hit(k, a["value"]),
                   "covered": None if not r else int(r[0] <= key[k]["value"] <= r[1])}
    s = lambda f: sum(v[f] for v in rows.values() if v[f] is not None)
    n = lambda f: sum(1 for v in rows.values() if v[f] is not None)
    return {"per_question": rows, "category_hits": f"{s('cat_hit')}/{n('cat_hit')}", "value_hits": f"{s('value_hit')}/{n('value_hit')}",
            "interval_coverage": f"{s('covered')}/{n('covered')}", "mean_brier": round(s('brier') / n('brier'), 3)}

out = {"outcome_key_seq": 122, "answers_seq": 123}
for f in sorted(os.listdir(os.path.join(HERE, "answers"))):
    out[f] = grade(json.load(open(os.path.join(HERE, "answers", f))))
brow = {}
for k in Q:
    b = base[k]
    if b["category"] is None: continue
    brow[k] = {"category": b["category"], "cat_hit": int(b["category"] == key[k]["category"]), "value": b["value"], "value_hit": value_hit(k, b["value"])}
out["baseline"] = {"per_question": brow, "category_hits": f"{sum(v['cat_hit'] for v in brow.values())}/{len(brow)}",
                   "value_hits": f"{sum(v['value_hit'] for v in brow.values())}/{len(brow)}"}
json.dump(out, open(os.path.join(HERE, "grades.json"), "w"), indent=1)
for name in [f for f in out if f.endswith(".json")] + ["baseline"]:
    g = out[name]; print(name, {k: v for k, v in g.items() if k != "per_question"})
    print("   ", {k: (v["cat_hit"], v.get("value_hit")) for k, v in g["per_question"].items()})
