# GPUMD on CHPC for the v2 endpoint campaign (2026-09-29)

Decision 2026-09-29: the P2 v2 endpoint campaign runs on CHPC guest
partitions, in batches, because the DGX was needed for other work. So v2
moves from the DGX GB10 to CHPC guest GPUs.

- Source: GPUMD master `aab525f1ac4af9bad38414f7f33b1f13ee153b2d`, the same
  commit v1 used on the DGX, cloned to `mat_theory/gpumd_v2/GPUMD` in the
  CHPC home directory.
- Build: `build_gpumd.sbatch` (notchpeak-guest CPU job 15890758, 16 cores,
  `module load cuda/12.8.1`, `-std=c++14` -> `-std=c++17`), fat binary with
  `-gencode` for sm_75, 80, 86, 89, 90, 120 plus compute_90 PTX, so one binary
  runs on every guest GPU generation (2080 Ti through H200 and RTX PRO
  Blackwell). `src/gpumd` sha256 `ff94af94...9bc0`.
- Potential files are byte-identical to the ones v1 used:
  Si_Tersoff_1989.txt `52a2e8e2...48a5`, Ge_Tersoff_1989.txt `6e6a8222...cd6a`.
- Guest access verified: notchpeak GPUs via `-A owner-gpu-guest -p
  notchpeak-gpu-guest`; granite GPUs via `-A sparks --qos granite-gpu-guest
  -p granite-gpu-guest` (the granite association is `sparks` with guest QOS;
  grn061 / `sparks-gpu-grn` never requested).
- Protocol smoke test before pre-registration (not campaign data, never
  pooled): `make_runs_v2.py --smoke` (every length / 1000), one run per
  (system, cell), all exit 0 on an RTX 2080 Ti (notchpeak-gpu-guest job
  15890762, driver 580.173.02). A granite smoke (job 2078972) was queued at
  pre-registration time.
