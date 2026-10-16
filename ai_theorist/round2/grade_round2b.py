#!/usr/bin/env python3
"""Grade theorist C round 2b (H1b, H5, H6, H7) with the round-1 rubric and the round-2 quote rule
(a category counts only if its quoted basis appears verbatim in theories_round2b.md). Separate row;
round 2's grades_round2.json is not touched."""
import hashlib, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); AT = os.path.dirname(HERE); MT = os.path.dirname(AT)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
p = next(e for e in led.entries if e["payload"].get("op_id") == "ai-theorist-round2b-answers")
for f, h in p["payload"]["files_sha256"].items():
    assert hashlib.sha256(open(os.path.join(AT, f), "rb").read()).hexdigest() == h, f
key = json.load(open(os.path.join(AT, "outcome_key.json")))
assert hashlib.sha256(open(os.path.join(AT, "outcome_key.json"), "rb").read()).hexdigest() == led.entries[122]["payload"]["outcome_key_sha256"]
C = json.load(open(os.path.join(AT, "answers", "theorist_C_asta_theorizer_round2b.json")))["answers"]
A = json.load(open(os.path.join(AT, "answers", "theorist_A_sonnet.json")))
B = json.load(open(os.path.join(AT, "answers", "theorist_B_haiku.json")))
T = re.sub(r"\s+", " ", open(os.path.join(HERE, "theorizer", "theories_round2b.md")).read())
Q = ["H1b", "H5", "H6", "H7"]

def vhit(k, v):
    if v is None: return None
    o = key[k]
    if "tol_abs" in o: return int(abs(v - o["value"]) <= o["tol_abs"])
    return int(v > 0 and abs(math.log(v / o["value"])) <= o["tol_logratio"])

rows = {}
for k in Q:
    c = C[k]; q = c.get("basis")
    quote_ok = bool(q) and re.sub(r"\s+", " ", q).strip()[:120] in T
    cat = c["category"] if quote_ok else None
    rows[k] = {"category": cat, "category_as_mapped": c["category"], "quote_verbatim": quote_ok,
               "cat_hit": None if cat is None else int(cat == key[k]["category"]),
               "value_hit": vhit(k, c["value"]) if cat is not None else None,
               "A_hit": int(A[k]["category"] == key[k]["category"]), "B_hit": int(B[k]["category"] == key[k]["category"]),
               "outcome": key[k]["category"]}
ans = [k for k in Q if rows[k]["cat_hit"] is not None]
s = lambda ks, f: f"{sum(rows[k][f] for k in ks)}/{len(ks)}"
out = {"answers_seq": p["seq"], "registration_seq": 136, "rubric_seq": 122, "per_question": rows,
       "answered": f"{len(ans)}/{len(Q)}", "category_hits_answered": s(ans, "cat_hit"),
       "A_on_same_items": s(ans, "A_hit"), "B_on_same_items": s(ans, "B_hit")}
json.dump(out, open(os.path.join(HERE, "grades_round2b.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "per_question"}, indent=1))
for k in Q: print(k, rows[k]["category_as_mapped"], "quote", rows[k]["quote_verbatim"], "hit", rows[k]["cat_hit"], "outcome", rows[k]["outcome"], "A", rows[k]["A_hit"], "B", rows[k]["B_hit"])
