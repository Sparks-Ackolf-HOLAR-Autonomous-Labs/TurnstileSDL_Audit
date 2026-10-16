#!/usr/bin/env python3
"""Pre-registered design of the GPUMD endpoint-production campaign
(paper 2's own materials experiment; run 2026-09-28).

This script is deterministic: it writes `endpoint_campaign_design.json`
bit-for-bit identically on every run, and the SHA-256 of that file is
the pre-registration commitment. `preregister.py` appends the hash plus
a Merkle root over the run rows to `../../phase_c/ledger_campaign.jsonl`,
and the design, hash, and ledger entry are committed and pushed to git
BEFORE `make_runs.py` creates any run directory. The driver refuses to
start if the design file on disk no longer matches the committed hash.

Everything a reader needs to judge the campaign is fixed here, before
any production outcome exists: the run matrix (stages, driving forces,
seeds, sizes, lengths), the analysis protocol (discard, blocks,
estimator), the run-level and point-level acceptance gates, the
restore rule that lifts `scope-limit-alloys-2026-09-27`, the stated
predictions, and the deviation policy.

Usage: python3 design_endpoint_campaign.py   (prints the SHA-256)
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "endpoint_campaign_design.json")

POT_DIR = "/home/sparksspark/mat_theory_gpumd/GPUMD/potentials/tersoff"
POT = {"Si": f"{POT_DIR}/Si_Tersoff_1989.txt",
       "Ge": f"{POT_DIR}/Ge_Tersoff_1989.txt",
       "SiGe": f"{POT_DIR}/SiGe_Tersoff_1989.txt"}
A0 = {"Si": 5.432, "Ge": 5.657}          # Tersoff-1989 0 K, LAMMPS gate
A0["SiGe"] = round(0.5 * (A0["Si"] + A0["Ge"]), 4)   # Vegard start, NPT relaxes

# Driving-force pairs (1/A). Linear response needs Fe x MFP << 1; MFPs
# shrink roughly as 1/T and are shorter in Ge than Si, so Fe grows with
# T and is doubled for Ge. Si at 300 K reuses the two gate-validated
# values (5e-6, 1e-5); 1e-4 is the documented nonlinear runaway.
FE = {("Si", 300): [5e-6, 1e-5], ("Si", 700): [1e-5, 2e-5],
      ("Si", 1100): [2e-5, 4e-5],
      ("Ge", 300): [1e-5, 2e-5], ("Ge", 700): [2e-5, 4e-5],
      ("Ge", 1100): [4e-5, 8e-5]}

SEED_BASE = 55000


def run_row(stage, system, T, fe, seed, cells, prod_ns, x_ge=None):
    size = "x".join(str(c) for c in cells)
    name = f"{system}_T{T}_fe{fe:.0e}_{size}_s{seed}".replace("e-0", "e-")
    row = {"run_id": name, "stage": stage, "system": system, "T_K": T,
           "Fe_per_A": fe, "seed": seed, "cells": cells,
           "n_atoms": 8 * cells[0] * cells[1] * cells[2],
           "potential": POT[system], "a0_A": A0[system],
           "production_ns": prod_ns}
    if x_ge is not None:
        row["x_ge"] = x_ge
        row["config_seed"] = seed      # random Ge placement seed
    return row


def build_runs():
    runs, seed = [], SEED_BASE
    # Stage S0: alloy methods cross-check (short, lands first).
    for _ in range(3):
        seed += 1
        runs.append(run_row("S0-alloy-crosscheck", "SiGe", 300, 2e-4, seed,
                            [8, 8, 8], 2.0, x_ge=0.5))
    # Stage S1: the 300 K anchors that decide the restore.
    for system in ("Si", "Ge"):
        for fe in FE[(system, 300)]:
            for _ in range(3):
                seed += 1
                runs.append(run_row("S1-anchor-300K", system, 300, fe, seed,
                                    [8, 8, 8], 5.0))
    # Stage S2: size check, Si only (longest MFPs, the worst case for
    # size artifacts; a Si pass covers Ge a fortiori). HNEMD is
    # homogeneous, so the check doubles the cell count along the
    # driving direction x (16x8x8, 8192 atoms).
    for _ in range(2):
        seed += 1
        runs.append(run_row("S2-size-check", "Si", 300, 1e-5, seed,
                            [16, 8, 8], 5.0))
    # Stage S3: temperature sweep on the rNEMD/BTE grid.
    for system in ("Si", "Ge"):
        for T in (700, 1100):
            for fe in FE[(system, T)]:
                for _ in range(2):
                    seed += 1
                    runs.append(run_row("S3-T-sweep", system, T, fe, seed,
                                        [8, 8, 8], 3.0))
    return runs


DESIGN = {
    "campaign": "gpumd-endpoint-production-2026-09-28",
    "paper": "P2 (verifiable revision), own materials experiment",
    "purpose": "bulk Tersoff-1989 kappa of pure Si and pure Ge via HNEMD "
               "with a valid many-body heat current, to decide the "
               "restore of scope-limit-alloys-2026-09-27",
    "code": {"engine": "GPUMD 5.8 (master, built on the DGX GB10, sm_121)",
             "binary": "/home/sparksspark/mat_theory_gpumd/GPUMD/src/gpumd",
             "gate": "gpumd/BRINGUP.md + gpumd/validation_results.json "
                     "(validation runs are the gate only and are NEVER "
                     "pooled with production)"},
    "protocol": {
        "time_step_fs": 1,
        "npt_equilibration": "ensemble npt_ber T T 100 0 100 1000 for "
                             "100 ps (isotropic, 0 GPa, C_hydro 100 GPa "
                             "rough estimate, p_coup 1000 steps)",
        "nvt_equilibration": "ensemble nvt_nhc T T 100 for 50 ps at the "
                             "NPT-relaxed box",
        "production": "ensemble nvt_nhc T T 100 + compute_hnemd 1000 Fe 0 0 "
                      "+ dump_thermo 10000, for production_ns",
        "velocity": "velocity T seed <seed>",
        "driving_direction": "x (kappa = kx_in + kx_out)",
        "model": "diamond conventional cells, cells[0] along x; alloy "
                 "sites Ge with probability x_ge using config_seed "
                 "(gpumd/make_model.py)",
        "serial_execution": "one run at a time (benchmarked 2026-09-28: "
                            "4 concurrent 4096-atom runs take 9x one run "
                            "on the GB10, so concurrency is a net loss)",
        "stage_order": ["S0-alloy-crosscheck", "S1-anchor-300K",
                        "S2-size-check", "S3-T-sweep"],
    },
    "analysis": {
        "per_run": "kx = kx_in + kx_out per 1000-step interval; discard "
                   "first 20%; 10 contiguous blocks; run value = mean of "
                   "block means; run SEM = std(block means)/sqrt(10)",
        "per_point": "point = (system, T, Fe). Estimate = mean of per-run "
                     "values over seeds; uncertainty SE = std over seeds / "
                     "sqrt(n_seeds) (sample std, ddof=1); if fewer than 2 "
                     "runs pass, the point is FAILED (no estimate)",
        "per_state": "state = (system, T). Reported kappa = mean of the "
                     "two Fe point estimates; SE = 0.5*sqrt(SE1^2+SE2^2)",
    },
    "acceptance": {
        "R1_exit": "exit status 0 and kappa.out has at least 90% of the "
                   "expected lines",
        "R2_temperature": "mean production temperature within 2% of T",
        "R3_no_runaway": "drift z = (mean of last 20% of retained series - "
                         "mean of first 20%) / (run SEM * sqrt(2)) must be "
                         "< 3 (positive runaway is the documented Fe=1e-4 "
                         "failure signature)",
        "R4_physical": "0 < run value < 2000 W/mK",
        "P1_linearity": "at each (system, T): |k(Fe_low) - k(Fe_high)| <= "
                        "2*sqrt(SE_low^2 + SE_high^2)",
        "P2_size": "Si 300 K: |k(16x8x8, Fe 1e-5) - k(8x8x8, Fe 1e-5)| <= "
                   "2*sqrt(SE^2 + SE^2) (seed SEs)",
        "P3_alloy_crosscheck": "x=0.5, 300 K HNEMD point within 2*sqrt(SE^2 "
                               "+ 0.10^2) of the rNEMD 1/L extrapolation "
                               "1.80 W/mK (0.10 = assumed rNEMD fit SE); "
                               "pass -> strengthen witness, fail -> open a "
                               "shard action on the MD party (does NOT "
                               "block the restore, which is about "
                               "endpoints)",
    },
    "restore_rule": {
        "op": "restore",
        "lifts": "scope-limit-alloys-2026-09-27",
        "condition": "S1 passes R1-R4 for >= 2 seeds per point AND P1 for "
                     "BOTH Si and Ge at 300 K AND S2 passes P2",
        "domain_after_restore": "x in [0, 1] at T = 300 K; each S3 "
                                "temperature is added to the endpoint "
                                "domain only if both Si and Ge pass P1 at "
                                "that temperature, otherwise the endpoint "
                                "domain stays scope-limited at that T with "
                                "the failing gate recorded as the reason",
        "if_condition_fails": "no restore; the scope-limit stays live and "
                              "a ledger entry records which gate failed "
                              "(a negative result is published, not "
                              "rerun silently)",
    },
    "predictions": {
        "stated_before_outcomes": [
            "k_Si(300 K) > k_Ge(300 K)",
            "k_Si(300 K) inside the published classical Tersoff-Si HNEMD "
            "band, roughly 150-300 W/mK (gate: 163 +/- 40, 216 +/- 87)",
            "for both elements k(1100 K) < k(700 K) < k(300 K), roughly "
            "1/T (Umklapp-dominated), i.e. k(300)/k(1100) between 2.5 and "
            "4.5",
            "endpoint values agree with the BTE-DFT party (Si 160.5 / 40.5, "
            "Ge 57.1 / 16.7 W/mK at 300 / 1100 K) within 2 SE plus a "
            "method-family allowance of 30% (classical vs quantum "
            "occupation, potential)",
        ],
        "status": "predictions are reported pass or fail; they do NOT gate "
                  "the restore (the gates above do)",
    },
    "deviation_policy": [
        "a run that fails R1 for an infrastructure reason (killed, "
        "node reboot) may be rerun ONCE with the same seed; the rerun is "
        "logged as a deviation entry on the ledger",
        "any change to Fe, length, seeds, or gates after this commitment "
        "is a deviation: it gets its own ledger entry with the reason, "
        "BEFORE the affected run starts, and is reported in the paper",
        "each finished stage's raw outputs (kappa.out, thermo.out, "
        "run.log) are hashed and their Merkle root is appended to the "
        "ledger BEFORE the stage is analysed",
    ],
}


def main():
    design = dict(DESIGN)
    design["runs"] = build_runs()
    design["n_runs"] = len(design["runs"])
    design["cost_estimate"] = {
        "throughput_atom_steps_per_s": 1.74e7,
        "total_atom_steps": sum(r["n_atoms"] * (r["production_ns"] * 1e6 +
                                                150000)
                                for r in design["runs"]),
    }
    design["cost_estimate"]["wall_h_serial"] = round(
        design["cost_estimate"]["total_atom_steps"] / 1.74e7 / 3600, 1)
    blob = json.dumps(design, indent=1, sort_keys=True).encode() + b"\n"
    with open(OUT, "wb") as f:
        f.write(blob)
    print(f"{OUT}: {design['n_runs']} runs, "
          f"~{design['cost_estimate']['wall_h_serial']} h serial")
    print("sha256", hashlib.sha256(blob).hexdigest())


if __name__ == "__main__":
    main()
