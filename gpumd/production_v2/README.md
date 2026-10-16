# P2 v2 GPUMD endpoint campaign on CHPC guest GPUs

Run 2026-09-29 on CHPC guest partitions in multiple batches, because the
DGX was needed for other work.
v1 (`../production/`) stays closed with its negative verdict (campaign record seq
18); v2 is a new pre-registered experiment and is never pooled with v1.

## Order of events (campaign record `../../phase_c/ledger_campaign.jsonl`)

| seq | entry |
|---|---|
| 30 | pre-registration: `endpoint_v2_design.json` sha256 `480c8d82...1232`, 63 runs, pushed in commit `361f711` before any run directory existed |
| 31 | deviation (infrastructure): first submission landed partly on broken RTX 2080 Ti guest nodes (GPU not detected); cancelled within 2 min, no output kept; resubmitted with the same matrix, GPU models pinned, CUDA-init guard |
| 39 | deviation (placement): V3-highT sat PENDING on granite (2078979) for 2.5 h with no task started; cancelled and resubmitted on notchpeak-gpu-guest (15891766), same matrix |
| 41 | batch_result V2-size-check (committed before analysis) |
| 42 | batch_result V1-anchor-300K (committed before analysis) |
| 43 | gate_failure T300: **300 K NOT restored**. Si fails P1 linearity (Fe 1e-5: 269 +/- 14; Fe 2e-5: 343 +/- 12 W/mK); P2 size check not evaluable (0/3 Si 16x8x8 runs pass the R3 drift gate, run values 465-569 W/mK). Ge passes (80.9 vs 82.6) |
| 50 | batch_result V3-highT (40 runs, committed before analysis) |
| 51 | **restore T700: 700 K endpoint domain RESTORED** (Si 96.5 +/- 5.4, Ge 32.4 +/- 1.5 W/mK; P1 passes for both; label Tersoff-1989, 1.51x / 1.26x BTE-DFT) |
| 52 | gate_failure T1100: **1100 K NOT restored**, Si fails P1 narrowly (Fe 2e-5: 45.3 +/- 3.9; 4e-5: 54.6 +/- 1.8; diff 9.2 vs limit 8.6). Ge passes (19.7 vs 18.8) |
| 44 | deviation (infrastructure): 32 V3 tasks hit notch204 (V100 not visible to CUDA), guard exited in 8 s with no output; resubmitted as 15892171 with notch204 excluded |

## What changed vs v1 (all fixed in the design before any run)

20 ns production at 300 K (v1 5 ns); 5 seeds per point (v1 2-3); point SE
floored at the pooled within-run SEM (the disclosed v1 flaw); F_e {1e-5,
2e-5} at 300 K for both elements; restore judged per temperature; three
stage batches on CHPC guest GPUs.

## Batches (SLURM arrays, one run per task, `--requeue` on preemption)

| stage | runs | where | array job |
|---|---|---|---|
| V1-anchor-300K | 20 (Si, Ge x 2 F_e x 5 seeds, 20 ns) | notchpeak-gpu-guest: tasks 0-1 on A6000 (15890811), tasks 2-19 first moved to RTX 3090 (15890906), but that idle node (notch299) is broken too: all 18 tasks hit the CUDA-init guard and wrote no exit status; resubmitted as 15890963 with any GPU model and known-bad nodes excluded (notch168, notch294, notch299). Leftovers of the first submission were cleaned from those run dirs before restart (logged in each `attempts` file) | 15890811, 15890963 |
| V2-size-check | 3 (Si 16x8x8, 20 ns) | notchpeak-gpu-guest, A6000 | 15890796 |
| V3-highT | 40 (Si, Ge x 700/1100 K x 2 F_e x 5 seeds, 10 ns) | granite-gpu-guest, H200 | 2078979 |

Runs were written to `mat_theory/gpumd_v2/runs/` in the CHPC home
directory (not purgeable scratch). Measured speed on an A6000: about 0.25 ns
of production per minute for the 8192-atom box.

## Commit and analysis order

1. finished run directories are copied from CHPC to a local staging
   folder (`~/mat_theory_gpumd_v2_stage/`, not the repo)
2. `python3 commit_stage_v2.py <stage> --root ~/mat_theory_gpumd_v2_stage/runs`
   per finished stage (copies raw outputs into `raw/`, hashes, appends the
   Merkle root to the campaign record; refuses unfinished or git-ignored evidence)
3. commit + push, THEN `python3 analyze_v2.py` (reads committed stages only)
4. restore / gate_failure campaign-record entries per temperature as the
   pre-registered rule decides; update `RESULTS.md` and the P2 draft.

## Status 2026-09-29 (interim)

- V1 and V2 collected and analysed (`analysis_v2.json`). 300 K verdict:
  not restored (seq 43). Physics reading: Tersoff-Si at 300 K is neither
  in linear response at Fe = 2e-5 nor size-converged at 8x8x8 (the
  16x8x8 box reads about 500 W/mK against about 270, with running averages
  still drifting after 20 ns). Ge at 300 K is well behaved
  (81.7 +/- 4.9 W/mK, 1.43x BTE-DFT).
- V3-highT: 8/40 done on notchpeak, the other 32 running or queued as
  array 15892171.

## Status 2026-09-29: campaign closed

All 63 runs collected (V3: 32 COMPLETED on notchpeak guest GPUs; 205 attempts
in total across the campaign because of guest preemptions and broken nodes).
*Note 2026-10-04:* the committed per-run `attempts` files hold 137 starts; the 205 came from scheduler accounting that was not committed. Papers use 137 (see `../../p3_limits/README.md`, section 3).
Per-temperature verdicts under the pre-registered rule: **300 K not restored
(seq 43), 700 K restored (seq 51), 1100 K not restored (seq 52)**. The 1100 K
failure is a narrow Si linearity miss (9.2 against an 8.6 W/mK limit); Ge
passes at every temperature. All six predictions in the design except
`P1_passes_300_both` hold, including agreement with BTE-DFT within 30% at
1100 K for both elements (Si 1.23x, Ge 1.16x).
