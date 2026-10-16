#!/usr/bin/env python3
"""Pre-registered design of the v2 GPUMD endpoint campaign (paper 2's own
materials experiment, second attempt; run 2026-09-29 on CHPC guest
partitions in multiple batches).

v2 is a NEW experiment, not an edit of v1 (gpumd/production/, closed at
ledger seq 18 with the restore refused). v1 outputs are never pooled
with v2. What v2 changes, each fixed here before any v2 run exists:

  * power: 20 ns production at 300 K (v1: 5 ns), 5 seeds per point (v1: 2-3);
  * uncertainty rule: point SE is floored at the pooled within-run block
    SEM, so a chance agreement of few seeds cannot collapse the gate
    (the disclosed v1 design flaw);
  * driving forces at 300 K: {1e-5, 2e-5} 1/A for both elements (v1 Si
    used 5e-6, which was under-powered at 5 ns);
  * restore decisions are per temperature: 300 K, 700 K and 1100 K are
    each judged on their own gates (v1 made the high-T additions
    conditional on the 300 K restore);
  * execution: CHPC guest GPU partitions (notchpeak-gpu-guest,
    granite-gpu-guest; free, preemptible), one SLURM array per stage,
    one run per array task, GPU model recorded per run; a preempted run
    restarts from scratch with the same seed (declared here, so not a
    deviation); the DGX is not used.

Deterministic: writes endpoint_v2_design.json byte-identically; its
SHA-256 is the commitment appended to the ledger by preregister_v2.py
and pushed to git before make_runs_v2.py builds any run directory.
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "endpoint_v2_design.json")

CHPC_ROOT = "/uufs/chpc.utah.edu/common/home/u1496771/mat_theory/gpumd_v2"
POT_DIR = f"{CHPC_ROOT}/GPUMD/potentials/tersoff"
POT = {"Si": f"{POT_DIR}/Si_Tersoff_1989.txt",
       "Ge": f"{POT_DIR}/Ge_Tersoff_1989.txt"}
A0 = {"Si": 5.432, "Ge": 5.657}
FE = {("Si", 300): [1e-5, 2e-5], ("Ge", 300): [1e-5, 2e-5],
      ("Si", 700): [1e-5, 2e-5], ("Ge", 700): [2e-5, 4e-5],
      ("Si", 1100): [2e-5, 4e-5], ("Ge", 1100): [4e-5, 8e-5]}
SEED_BASE = 56000
N_SEEDS = 5


def run_row(stage, system, T, fe, seed, cells, prod_ns):
    size = "x".join(str(c) for c in cells)
    name = f"{system}_T{T}_fe{fe:.0e}_{size}_s{seed}".replace("e-0", "e-")
    return {"run_id": name, "stage": stage, "system": system, "T_K": T,
            "Fe_per_A": fe, "seed": seed, "cells": cells,
            "n_atoms": 8 * cells[0] * cells[1] * cells[2],
            "potential": POT[system], "a0_A": A0[system],
            "production_ns": prod_ns}


def build_runs():
    runs, seed = [], SEED_BASE
    for system in ("Si", "Ge"):
        for fe in FE[(system, 300)]:
            for _ in range(N_SEEDS):
                seed += 1
                runs.append(run_row("V1-anchor-300K", system, 300, fe, seed,
                                    [8, 8, 8], 20.0))
    for _ in range(3):
        seed += 1
        runs.append(run_row("V2-size-check", "Si", 300, 1e-5, seed,
                            [16, 8, 8], 20.0))
    for system in ("Si", "Ge"):
        for T in (700, 1100):
            for fe in FE[(system, T)]:
                for _ in range(N_SEEDS):
                    seed += 1
                    runs.append(run_row("V3-highT", system, T, fe, seed,
                                        [8, 8, 8], 10.0))
    return runs


DESIGN = {
    "campaign": "gpumd-endpoint-v2-2026-09-29",
    "supersedes_nothing": "v1 (gpumd-endpoint-production-2026-09-28) stays "
                          "closed with its negative verdict (ledger seq 18); "
                          "v1 outputs are never pooled with v2",
    "paper": "P2 (verifiable revision), own materials experiment, v2",
    "purpose": "bulk Tersoff-1989 kappa of pure Si and Ge via HNEMD at "
               "adequate power, to decide per temperature whether the "
               "scope-limit-alloys-2026-09-27 endpoint exclusion is lifted",
    "code": {"engine": "GPUMD master aab525f1 (same commit as v1), built on "
                       "CHPC with CUDA 12.8.1 as a fat binary for sm_75/80/"
                       "86/89/90/120 (+compute_90 PTX); build log "
                       "gpumd/production_v2/BUILD.md",
             "binary": f"{CHPC_ROOT}/GPUMD/src/gpumd",
             "potential_files": "GPUMD potentials/tersoff/{Si,Ge}_Tersoff_"
                                "1989.txt, identical content to v1 (sha256 "
                                "recorded in BUILD.md)"},
    "protocol": {
        "time_step_fs": 1,
        "npt_equilibration": "ensemble npt_ber T T 100 0 100 1000 for 100 ps",
        "nvt_equilibration": "ensemble nvt_nhc T T 100 for 50 ps",
        "production": "ensemble nvt_nhc T T 100 + compute_hnemd 1000 Fe 0 0 "
                      "+ dump_thermo 10000, for production_ns",
        "velocity": "velocity T seed <seed>",
        "driving_direction": "x (kappa = kx_in + kx_out)",
        "model": "diamond conventional cells (gpumd/make_model.py)",
        "execution": "CHPC guest GPU partitions only (notchpeak-gpu-guest / "
                     "granite-gpu-guest, account owner-gpu-guest); one SLURM "
                     "array per stage, one run per task, 1 GPU per task; "
                     "grn061 / sparks-gpu-grn and the DGX are not used",
        "hardware_heterogeneity": "whatever guest GPU SLURM assigns; the "
                                  "GPU model is recorded per run "
                                  "(nvidia-smi) and reported, never gated",
        "preemption": "a preempted or node-failed task is requeued and "
                      "restarts from scratch with the same seed; attempts "
                      "are counted per run and reported",
        "stage_order": ["V1-anchor-300K", "V2-size-check", "V3-highT"],
    },
    "analysis": {
        "per_run": "kx = kx_in + kx_out per 1000-step interval; discard "
                   "first 20%; 10 contiguous blocks; run value = mean of "
                   "block means; run SEM = std(block means)/sqrt(10)",
        "per_point": "point = (system, T, Fe, cells). Estimate = mean of "
                     "passing run values; SE = max(std over runs/sqrt(n), "
                     "sqrt(sum run SEM^2)/n) (seed SE floored at the pooled "
                     "within-run SEM); FAILED if fewer than 3 runs pass "
                     "(2 for the 3-run size point)",
        "per_state": "state = (system, T). Reported kappa = mean of the two "
                     "Fe point estimates; SE = 0.5*sqrt(SE1^2+SE2^2)",
    },
    "acceptance": {
        "R1_exit": "exit status 0 and kappa.out has >= 90% of expected lines",
        "R2_temperature": "mean production temperature within 2% of T",
        "R3_no_runaway": "drift z = (mean of last 20% of retained series - "
                         "mean of first 20%) / (run SEM*sqrt(2)) < 3",
        "R4_physical": "0 < run value < 2000 W/mK",
        "P1_linearity": "at each (system, T), 8x8x8: |k(Fe_low)-k(Fe_high)| "
                        "<= 2*sqrt(SE_low^2+SE_high^2), SE as per_point",
        "P2_size": "Si 300 K, Fe 1e-5: |k(16x8x8)-k(8x8x8)| <= "
                   "2*sqrt(SE^2+SE^2), SE as per_point",
    },
    "restore_rule": {
        "op": "restore",
        "lifts": "scope-limit-alloys-2026-09-27 (endpoint part only, per T)",
        "T300": "all four V1 points have >= 3 passing runs AND P1 Si 300 "
                "AND P1 Ge 300 AND P2 -> endpoint domain restored at 300 K",
        "T700_T1100": "each of 700 K and 1100 K is judged independently: "
                      "all four points at that T have >= 3 passing runs AND "
                      "P1 passes for both Si and Ge -> endpoint domain "
                      "restored at that T",
        "scope_label": "every restored state carries the label 'Tersoff-"
                       "1989-parented' plus its measured ratio to the "
                       "BTE-DFT party (Si 160.5/63.8/40.5, Ge 57.1/25.7/16.7 "
                       "W/mK at 300/700/1100 K); the ratio is reported, "
                       "not gating: the gates decide numerical validity of "
                       "the Tersoff-family number, the label carries its "
                       "known method bias into every downstream claim",
        "if_condition_fails": "that temperature stays scope-limited; a "
                              "ledger entry records the failing gate; the "
                              "negative result is published, not rerun "
                              "silently",
    },
    "predictions": {
        "stated_before_outcomes": [
            "P1 passes at 300 K for both elements (v1 post-hoc SE-floor "
            "variant passed there)",
            "k_Si(300 K, Fe 1e-5) within 20% of v1's 284 W/mK",
            "Tersoff/BTE-DFT ratio at 300 K between 1.4 and 2.2 for both "
            "elements (v1: about 1.6-1.8)",
            "Tersoff and BTE-DFT agree within 30% at 1100 K for both elements",
            "k(300) > k(700) > k(1100) for both elements",
        ],
        "status": "reported pass/fail; not gating",
    },
    "deviation_policy": [
        "requeue after preemption/node failure is declared protocol, not a "
        "deviation; a run failing R1 for any other infrastructure reason may "
        "be rerun once with the same seed, logged on the ledger",
        "any change to Fe, length, seeds, gates, or stages after this "
        "commitment is a deviation with its own ledger entry BEFORE the "
        "affected run starts, reported in the paper",
        "each stage's raw outputs are copied into the repo, hashed, and "
        "their Merkle root appended to the ledger BEFORE the stage is "
        "analysed; commit refuses git-ignored evidence",
    ],
}


def main():
    d = dict(DESIGN)
    d["runs"] = build_runs()
    d["n_runs"] = len(d["runs"])
    ns = sum(r["production_ns"] * r["n_atoms"] / 4096 for r in d["runs"])
    d["cost_estimate"] = {"ns_equiv_4096_atoms": ns,
                          "gpu_h_at_GB10_rate_4min_per_ns": round(ns * 4 / 60, 1)}
    blob = json.dumps(d, indent=1, sort_keys=True).encode() + b"\n"
    open(OUT, "wb").write(blob)
    print(f"{d['n_runs']} runs, {ns} ns-equiv, sha256",
          hashlib.sha256(blob).hexdigest())


if __name__ == "__main__":
    main()
