#!/usr/bin/env python3
"""Grade theorist C (round 2) with the round-1 rubric; abstentions (category null) are counted separately.
Mapping rule (PROTOCOL.md): a category counts only if its quoted basis appears verbatim in the theories."""
import hashlib, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); AT = os.path.dirname(HERE); MT = os.path.dirname(AT)
sys.path.insert(0, os.path.join(MT, "pilot", "src"))
from ledger import Ledger  # noqa: E402
led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
p = led.entries[128]["payload"]
for f, h in p["files_sha256"].items():
    assert hashlib.sha256(open(os.path.join(AT, f), "rb").read()).hexdigest() == h, f
key = json.load(open(os.path.join(AT, "outcome_key.json")))
assert hashlib.sha256(open(os.path.join(AT, "outcome_key.json"), "rb").read()).hexdigest() == led.entries[122]["payload"]["outcome_key_sha256"]
C = json.load(open(os.path.join(AT, "answers", "theorist_C_asta_theorizer.json")))["answers"]
A = json.load(open(os.path.join(AT, "answers", "theorist_A_sonnet.json")))
B = json.load(open(os.path.join(AT, "answers", "theorist_B_haiku.json")))
T = re.sub(r"\s+", " ", open(os.path.join(HERE, "theorizer", "theories_round2.md")).read())
Q = ["H1", "H1b", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9"]
LOOKUP = {"H8": "outcome is a median over published sintered-sample data", "H9": "outcome is from an open 2026 preprint the Theorizer retrieved"}
SIM_ONLY = ["H1", "H4", "H7"]

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
               "outcome": key[k]["category"], "lookup_possible": LOOKUP.get(k)}
ans = [k for k in Q if rows[k]["cat_hit"] is not None]
fore = [k for k in ans if k not in LOOKUP]
s = lambda ks, f: f"{sum(rows[k][f] for k in ks)}/{len(ks)}"
out = {"answers_seq": 128, "rubric_seq": 122, "per_question": rows,
       "answered": f"{len(ans)}/{len(Q)}", "category_hits_answered": s(ans, "cat_hit"),
       "category_hits_forecast_only": s(fore, "cat_hit"),
       "A_on_same_items": s(ans, "A_hit"), "B_on_same_items": s(ans, "B_hit"),
       "simulation_only_items": {k: rows[k]["cat_hit"] for k in SIM_ONLY},
       "open": {k: C[k]["category"] for k in ("O1", "O2", "O3")}}
json.dump(out, open(os.path.join(HERE, "grades_round2.json"), "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "per_question"}, indent=1))
for k in Q: print(k, rows[k]["category"], rows[k]["cat_hit"], "A", rows[k]["A_hit"], "B", rows[k]["B_hit"], rows[k]["lookup_possible"] or "")
