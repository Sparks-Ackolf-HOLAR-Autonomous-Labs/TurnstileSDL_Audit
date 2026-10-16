#!/usr/bin/env python3
"""Third-party check of the three pre-registered campaigns reported in P2.

CPU only, no network, repository files only. For each campaign it checks
  (a) the design file re-hashes to the SHA-256 pinned in its
      PREREGISTERED_SHA256 file and in the ledger pre-registration entry;
  (b) every raw output file re-hashes to its committed value and is tracked
      by git (not dropped by an ignore rule);
  (c) the recomputed Merkle root of every committed batch equals the ledger's;
  (d) every analysis/summary file named by a later ledger entry re-hashes;
  (e) the ledger timestamps put pre-registration before the first raw commit;
  (f) exceptional labels: the committed criteria re-hash, every label cites
      them, prospective labels follow label < replication < raw < decision,
      retrospective labels are reported separately, and no downweight or
      value change targets a value whose exceptional label is unresolved.
Plus the full ledger hash chain, the per-entry Ed25519 signatures
(ssh-keygen -Y verify) and the RFC 3161 time anchors (openssl ts -verify). Prints one line per check, per-campaign
file counts and wall-clock time. Exit 1 on any failure.
Usage: python3 verify_record.py [--json out.json] [--root DIR]
  --root DIR  check the record stored under DIR (laid out like the mat_theory
              folder) instead of the folder this script sits in; the checking
              code itself is always imported from this script's own folder.
"""
import hashlib, json, os, platform, shutil, subprocess, sys, time

T0 = time.perf_counter()
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.abspath(os.path.join(HERE, "..", ".."))
MT = os.path.abspath(sys.argv[sys.argv.index("--root") + 1]) if "--root" in sys.argv else CODE
sys.path.insert(0, os.path.join(CODE, "pilot", "src"))
from ledger import Ledger, leaf_hash, merkle_root  # noqa: E402

def sha(p):
    return hashlib.sha256(open(os.path.join(MT, p), "rb").read()).hexdigest()

GIT = shutil.which("git") is not None and subprocess.run(
    ["git", "rev-parse", "--is-inside-work-tree"], cwd=MT, capture_output=True).returncode == 0

def ignored(paths):
    """Subset of paths git would ignore (one git call for all); skipped
    when the record is checked outside a git clone (e.g. a zip download)."""
    if not GIT:
        return set()
    r = subprocess.run(["git", "check-ignore", "--stdin"], cwd=MT, input="\n".join(paths),
                       capture_output=True, text=True)
    return set(r.stdout.split("\n")) - {""}

led = Ledger(os.path.join(MT, "phase_c", "ledger_campaign.jsonl"))
E = {e["seq"]: e for e in led.entries}
rows, report = [], {}

def check(campaign, name, ok):
    rows.append((campaign, name, bool(ok)))

t = time.perf_counter()
check("ledger", f"hash chain over {len(led.entries)} entries", led.verify_chain())
# added after the mutation test (planted_violations/): a decision must not cite a
# registration, raw batch or criteria entry that comes after it or does not exist
# registrations are recorded as "preregistration" or, for designs hashed as files, "commitment"
KIND = {"prereg_seq": {"preregistration", "commitment"}, "raw_seq": {"batch_result", "batch_commitment"}}
bad = []
for e in led.entries:
    p = e["payload"]
    for src in (p, p.get("evidence") if isinstance(p.get("evidence"), dict) else {}):
        for k in ("prereg_seq", "raw_seq", "registration_seq", "criteria_seq", "rests_on"):
            v = src.get(k)
            for x in ([] if v is None else v if isinstance(v, list) else [v]):
                if not (isinstance(x, int) and x in E and x < e["seq"] and E[x]["kind"] in KIND.get(k, {E[x]["kind"]})):
                    bad.append((e["seq"], k, x))
check("ledger", "cited entries (prereg_seq, raw_seq, registration_seq, criteria_seq, rests_on) "
      "exist, precede the citing entry and have the expected kind", not bad)
report["ledger"] = {"entries": len(led.entries), "seconds": time.perf_counter() - t}

def design(campaign, seq, pinfile):
    p = E[seq]["payload"]
    pinned = open(os.path.join(MT, pinfile)).read().split()[0]
    check(campaign, f"design {os.path.basename(p['design_file'])} re-hash (ledger seq {seq})",
          sha(p["design_file"]) == p["design_sha256"] == pinned)
    return E[seq]["time"]

def gpumd(campaign, folder, design_file, seq_pre, pinfile):
    t = time.perf_counter()
    t_pre = design(campaign, seq_pre, pinfile)
    D = json.load(open(os.path.join(MT, folder, design_file)))
    n = nb = 0
    first = None
    for e in led.entries:
        p = e["payload"]
        if e["kind"] != "batch_result" or p.get("campaign") != D["campaign"]:
            continue
        stage = p["stage"]; nb += 1
        first = first or e["time"]
        man = json.load(open(os.path.join(MT, folder, "raw", f"manifest_{stage}.json")))
        paths, ok = [], True
        for rid, files in man.items():
            for f, h in files.items():
                rel = os.path.join(folder, "raw", rid, f)
                paths.append(rel)
                ok &= os.path.exists(os.path.join(MT, rel)) and sha(rel) == h
        ok &= not ignored(paths)
        n += len(paths)
        order = [r["run_id"] for r in D["runs"] if r["stage"] == stage]
        root = merkle_root([leaf_hash({"run_id": rid, "files": man[rid]}) for rid in order])
        check(campaign, f"batch {stage}: {len(paths)} raw files re-hash and tracked", ok)
        check(campaign, f"batch {stage}: Merkle root = ledger seq {e['seq']}", root == p["merkle_root"])
    check(campaign, "pre-registration precedes first raw commit", t_pre < first)
    report[campaign] = {"raw_files": n, "batches": nb, "seconds": time.perf_counter() - t}

gpumd("endpoint v1", "gpumd/production", "endpoint_campaign_design.json", 2,
      "gpumd/production/PREREGISTERED_SHA256")
gpumd("endpoint v2", "gpumd/production_v2", "endpoint_v2_design.json", 30,
      "gpumd/production_v2/PREREGISTERED_SHA256")
gpumd("size-free HNEMD", "gpumd/sizefree", "sizefree_design.json", 85,
      "gpumd/sizefree/PREREGISTERED_SHA256")
c = "size-free HNEMD"
p = E[89]["payload"]; check(c, "analysis results re-hash (seq 89)", sha(p["results_file"]) == p["results_sha256"])
ts = [E[s]["time"] for s in (85, 87, 88, 89, 90)]
check(c, "order: design < raw < analysis < decision", ts == sorted(ts))
gpumd("300 K size check", "gpumd/sizefree/check300", "check300_design.json", 91,
      "gpumd/sizefree/check300/PREREGISTERED_SHA256")
c = "300 K size check"
p = E[97]["payload"]; check(c, "analysis results re-hash (seq 97)", sha(p["results_file"]) == p["results_sha256"])
ts = [E[s]["time"] for s in (91, 96, 97, 98)]
check(c, "order: design < raw < analysis < decision", ts == sorted(ts))
gpumd("300 K level", "gpumd/sizefree/level300", "level300_design.json", 99,
      "gpumd/sizefree/level300/PREREGISTERED_SHA256")
c = "300 K level"
p = E[101]["payload"]; check(c, "analysis results re-hash (seq 101)", sha(p["results_file"]) == p["results_sha256"])
ts = [E[s]["time"] for s in (99, 100, 101, 102)]
check(c, "order: design < raw < analysis < decision", ts == sorted(ts))

gpumd("300 K Green-Kubo", "gpumd/sizefree/gk300", "gk300_design.json", 107,
      "gpumd/sizefree/gk300/PREREGISTERED_SHA256")

t = time.perf_counter()
c = "SiGeC"
design(c, 46, "nano_sigec/PREREGISTERED_SHA256")
design(c, 53, "nano_sigec/m1c/PREREGISTERED_SHA256")
n = 0
for seq, outdir in ((47, "nano_sigec/m1/out"), (54, "nano_sigec/m1c/out")):
    p = E[seq]["payload"]
    paths = [os.path.join(outdir, f) for f in p["files_sha256"]]
    ok = all(os.path.exists(os.path.join(MT, q)) and sha(q) == h
             for q, h in zip(paths, p["files_sha256"].values())) and not ignored(paths)
    n += len(paths)
    root = merkle_root([leaf_hash({"file": k, "sha256": v}) for k, v in sorted(p["files_sha256"].items())])
    check(c, f"batch {p['stage']}: {len(paths)} raw files re-hash and tracked", ok)
    check(c, f"batch {p['stage']}: Merkle root = ledger seq {seq}", root == p["raw_merkle_root"])
p = E[48]["payload"]; check(c, "gate-failure summary re-hash (seq 48)", sha(p["summary_file"]) == p["summary_sha256"])
p = E[49]["payload"]; check(c, "analysis results re-hash (seq 49)", sha(p["results_file"]) == p["results_sha256"])
ev = E[55]["payload"]["evidence"]
check(c, "rerun summary re-hash (seq 55)", sha(ev["summary_file"]) == ev["summary_sha256"])
check(c, "rerun results re-hash (seq 55)", sha(ev["rerun_results_file"]) == ev["rerun_results_sha256"])
ts = [E[s]["time"] for s in (46, 47, 48, 49, 53, 54, 55)]
check(c, "order: design < raw < gate < analysis < re-design < raw < decision",
      ts == sorted(ts) and ts[0] < ts[1] and ts[4] < ts[5])
report[c] = {"raw_files": n, "batches": 2, "seconds": time.perf_counter() - t}

t = time.perf_counter()
c = "small SiC"
n = 0
for pre, raw, dec, folder, res in ((58, 59, 61, "nano_sigec/small_sic", "md_results.json"),
                                   (78, 79, 80, "nano_sigec/small_sic/x03", "x03_results.json"),
                                   (103, 104, 105, "nano_sigec/small_sic/r30", "r30_results.json"),
                                   (106, 108, 110, "nano_sigec/small_sic/r50", "r50_results.json")):
    design(c, pre, folder + "/PREREGISTERED_SHA256")
    reg = E[pre]["payload"].get("files_sha256", {})  # added after the mutation test: inputs fixed at registration,
    check(c, f"{len(reg)} registered input files re-hash (seq {pre})",  # incl. the declared reach (decision_robustness.json)
          bool(reg) and all(os.path.exists(os.path.join(MT, folder, k)) and sha(folder + "/" + k) == h
                            for k, h in reg.items()))
    p = E[raw]["payload"]
    outdir = folder + ("/md/results" if pre == 58 else "/results")
    paths = [os.path.join(outdir, k) for k in p["files_sha256"]]
    ok = all(os.path.exists(os.path.join(MT, q)) and sha(q) == h
             for q, h in zip(paths, p["files_sha256"].values())) and not ignored(paths)
    n += len(paths)
    root = merkle_root([leaf_hash({"file": k, "sha256": v}) for k, v in sorted(p["files_sha256"].items())])
    check(c, f"batch {p['stage']}: {len(paths)} raw files re-hash and tracked", ok)
    check(c, f"batch {p['stage']}: Merkle root = ledger seq {raw}", root == p["raw_merkle_root"])
    check(c, f"{res} re-hash (seq {dec})", sha(folder + "/" + res) == E[dec]["payload"]["evidence"][res])
    ts = [E[q]["time"] for q in (pre, raw, dec)]
    check(c, f"order: design < raw < decision (seq {pre}, {raw}, {dec})", ts == sorted(ts) and ts[0] < ts[1])
report[c] = {"raw_files": n, "batches": 4, "seconds": time.perf_counter() - t}

t = time.perf_counter()
c = "exceptional labels"
crit = [e for e in led.entries if e["payload"].get("criteria_sha256")]
check(c, "criteria file re-hash (commitment entry)",
      len(crit) == 1 and sha(crit[0]["payload"]["criteria_file"]) == crit[0]["payload"]["criteria_sha256"])
cseq = crit[0]["seq"] if crit else 10 ** 9
labels = [e for e in led.entries if e["payload"].get("label") == "exceptional"]
check(c, f"{len(labels)} exceptional labels cite a criteria commitment that precedes them",
      all(e["payload"].get("criteria_seq") == cseq < e["seq"] for e in labels))
pro = [e for e in labels if not e["payload"].get("retrospective")]
retro = [e for e in labels if e["payload"].get("retrospective")]
for e in pro:  # rule X5: label < replication registration < replicate raw batch < resolving decision
    p = e["payload"]
    order = [e["seq"], p.get("replication_seq") or -1] + list(p.get("raw_seqs") or [-1]) + list(p.get("resolution_seqs") or [-1])
    kinds = (E.get(p.get("replication_seq"), {}).get("kind") == "preregistration"  # X3: replicate registered on the ledger
             and all(E.get(q, {}).get("kind") == "batch_result" for q in p.get("raw_seqs") or [None])
             and all(q in E for q in p.get("resolution_seqs") or [None]))
    check(c, f"prospective label seq {e['seq']}: label < replication < raw < decision, replication is a registration "
          f"and raw a batch result", order == sorted(order) and min(order) >= 0 and kinds)
for e in retro:  # reported separately, historical order shown, never counted as prospective findings
    p = e["payload"]
    if p.get("replication_seq") is not None:
        order = [p["replication_seq"]] + p["raw_seqs"] + p["resolution_seqs"]
        check(c, f"retrospective label seq {e['seq']} ({p['op_id']}): replication < raw < decision (seq {order})",
              order == sorted(order) and E[p["replication_seq"]]["kind"] == "preregistration")
    else:
        check(c, f"retrospective label seq {e['seq']} ({p['op_id']}): recorded as resolved without a replicate",
              p.get("meets_X3_ordering") is False)
# rule X2: no downweight or value change while a prospective exceptional label is unresolved
blocked = {"downweight", "correct", "replace", "remove", "forget"}  # X2 names remove
viol = [x["seq"] for e in pro for x in led.entries
        if e["seq"] < x["seq"] < min(e["payload"].get("resolution_seqs") or [10 ** 9])
        and x["payload"].get("op") in blocked and x["payload"].get("target") == e["payload"].get("target")]
check(c, "no downweight or value change targets a value with an unresolved exceptional label", not viol)
report[c] = {"prospective": len(pro), "retrospective": len(retro), "criteria_seq": cseq,
             "seconds": time.perf_counter() - t}

# AI-theorist conjectures: brief, rubric and outcome-key hash committed before
# the answers, answers hashed before the key is published, grades last.
t = time.perf_counter(); c = "ai-theorist"
reg = [e for e in led.entries if e["payload"].get("op_id") == "ai-theorist-pilot-registration"]
if reg:
    r = reg[0]; rp = r["payload"]
    ans = [e for e in led.entries if e["payload"].get("op_id") == "ai-theorist-pilot-answers"][0]
    grd = [e for e in led.entries if e["payload"].get("op_id") == "ai-theorist-pilot-grades"][0]
    check(c, f"brief re-hash (seq {r['seq']})", sha(rp["brief"]) == rp["brief_sha256"])
    check(c, f"rubric re-hash (seq {r['seq']})", sha(rp["rubric"]) == rp["rubric_sha256"])
    check(c, f"published outcome key = hash committed before the answers (seq {r['seq']})",
          sha("ai_theorist/outcome_key.json") == rp["outcome_key_sha256"])
    for f, h in sorted(ans["payload"]["answers_sha256"].items()):
        check(c, f"answer {f} re-hash (seq {ans['seq']})", sha("ai_theorist/answers/" + f) == h)
    check(c, f"grades re-hash (seq {grd['seq']})", sha("ai_theorist/grades.json") == grd["payload"]["grades_sha256"])
    check(c, "order: registration < answers < grades", r["seq"] < ans["seq"] < grd["seq"])
    if GIT:  # the key file entered version control only after the answers were hashed
        import calendar
        ct = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ct", "--", "ai_theorist/outcome_key.json"],
                            cwd=MT, capture_output=True, text=True).stdout.split()
        t_ans = calendar.timegm(time.strptime(ans["time"], "%Y-%m-%dT%H:%M:%SZ"))
        check(c, "outcome key first committed after the answer entry", bool(ct) and int(ct[-1]) >= t_ans)
    report[c] = {"registration_seq": r["seq"], "seconds": time.perf_counter() - t}

t = time.perf_counter()
import ledger_sign  # noqa: E402
from pathlib import Path  # noqa: E402
ledger_sign.LEDGER = Path(MT, "phase_c", "ledger_campaign.jsonl")
ledger_sign.SIGS = Path(MT, "phase_c", "ledger_signatures.jsonl")
ledger_sign.SIGNERS = Path(MT, "phase_c", "ledger_allowed_signers")
ledger_sign.ANCH = Path(MT, "phase_c", "anchors")
verify_signatures = ledger_sign.verify
for name, ok in verify_signatures():
    check("ledger", name, ok)
# added after the mutation test: a dropped tail entry leaves its signature behind,
# and deleting the anchor files must not silently remove the anchor checks
check("ledger", "signature file lists no entry missing from the ledger; seq numbers run 0 to N-1",
      set(ledger_sign.signatures()) <= set(E) and [e["seq"] for e in led.entries] == list(range(len(led.entries))))
check("ledger", "at least one RFC 3161 anchor present", any(ledger_sign.ANCH.glob("head_seq*.json")))
report["signatures"] = {"seconds": time.perf_counter() - t}
report["signatures"]["git_ignore_check"] = GIT

total = time.perf_counter() - T0
for camp, name, ok in rows:
    print(f"{'PASS' if ok else 'FAIL'}  [{camp}] {name}")
for k, v in report.items():
    print(k, json.dumps({a: (round(b, 4) if isinstance(b, float) else b) for a, b in v.items()}))
print(f"checks: {sum(ok for *_, ok in rows)}/{len(rows)} pass; total wall-clock {total:.2f} s")
if "--json" in sys.argv:
    json.dump({"checks": [{"campaign": a, "check": b, "pass": o} for a, b, o in rows],
               "timing": report, "total_seconds": total, "host": platform.machine(), "os": platform.system()},
              open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
sys.exit(0 if all(ok for *_, ok in rows) else 1)
