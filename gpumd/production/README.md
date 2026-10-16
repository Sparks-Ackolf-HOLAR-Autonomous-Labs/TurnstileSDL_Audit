# GPUMD endpoint-production campaign (paper 2's pre-registered experiment)

Run 2026-09-28. Order of operations, enforced by code:

1. `design_endpoint_campaign.py` writes `endpoint_campaign_design.json`
   deterministically (33 runs, 4 stages, about 9 h serial on the GB10;
   run matrix, analysis protocol, gates R1-R4 / P1-P3, restore rule,
   predictions, deviation policy).
2. `preregister.py` appends a `preregistration` entry (campaign record seq 2) to
   `../../phase_c/ledger_campaign.jsonl` with the design SHA-256 and a
   Merkle root over the run rows, and writes `PREREGISTERED_SHA256`.
3. Those files are committed and pushed to git **before** step 4.
4. `make_runs.py` refuses to build run directories unless the design on
   disk still matches `PREREGISTERED_SHA256`; it writes a serial
   `driver.sh` that hashes every run's raw outputs as it finishes.
5. Per stage: `commit_stage.py` appends the Merkle root of the stage's
   raw-output hashes to the campaign record BEFORE `analyze_campaign.py` sees it.

Pre-commit protocol smoke test (not campaign data, never pooled): the
first run of each system with every length divided by 1000 ran exit 0
for Si, Ge, SiGe, and the 16x8x8 box (`make_runs.py --smoke`).
Concurrency benchmark (not campaign data): one 4096-atom 50k-step run
11.8 s alone; 4 concurrent 106 s; 8 concurrent 213 s, so the campaign
runs serially.

Design SHA-256: `6bc5c8b688167a93a4c57e5f09d5efaadee3aecaf070d776603cf217d1614317`
