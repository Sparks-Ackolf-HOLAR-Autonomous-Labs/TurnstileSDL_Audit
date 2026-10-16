# Hash-committed pre-registration and exact unlearning make belief revisions in autonomous SiGeC semiconductor campaigns checkable

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23413467.svg)](https://doi.org/10.5281/zenodo.23413467)

Code, data and figure scripts for the paper "Hash-committed pre-registration and exact unlearning make belief revisions in autonomous SiGeC semiconductor campaigns checkable" (Advanced Intelligent Discovery (Wiley)). The manuscript itself is not part of this folder.

Licences: code (Python, shell and SLURM scripts) under the MIT License (`LICENSE`); data, result files, figures and text under CC BY 4.0 (`LICENSE-CC-BY-4.0.txt`). Archived third-party datasets keep their own terms and are cited in the paper: the Starrydata slice is CC BY 4.0 (Katsura et al., Sci. Technol. Adv. Mater.: Methods 5, 2506976 (2025), doi:10.1080/27660400.2025.2506976; cite it and the source paper of each curve used), and the Citrine release keeps its published terms.

Every path below is relative to this folder, and every script runs from it. The folder depends on no other folder or repository.

Analysis, figure and checker scripts run on any machine with the Python packages in `requirements.txt`. Acquisition scripts (SLURM job files and run generators) name the cluster paths and simulation binaries (LAMMPS, GPUMD, almaBTE, MACE) used at the time, so re-running a simulation needs those paths edited to the local installation. The recorded outputs of those runs are included, so no simulation has to be repeated to check a result.

Files whose SHA-256 the campaign record stores (designs, pre-registration digests, the scripts and raw outputs they name, and some notes) are kept byte-for-byte as they ran, because any edit would break verification. They keep their original wording, which includes operator decisions with dates, internal step numbers and the run paths of the time. Raw simulation logs are also kept as written.

Terms used in folder names and notes: a *party* is one evidence source of the campaign (for example Tersoff MD, MACE-MP rNEMD, almaBTE first-principles transport or a curated database); a *gate* is the acceptance check a run must pass before its result enters the campaign record; `phase_c/` holds the main campaign and `pilot/` the campaign-record library and the first trial campaign.

## Campaign material

| path | what it holds |
|---|---|
| `phase_c/ledger_campaign.jsonl` | the campaign record (the object the paper verifies) |
| `pilot/src` | campaign-record library |
| `gpumd/production` | first pre-registered GPUMD endpoint campaign, raw evidence, verifier |
| `gpumd/production_v2` | v2 endpoint campaign on CHPC guest GPUs, raw evidence |
| `gpumd/sizefree` | size-free HNEMD campaign, raw evidence |
| `gpumd/validation_results.json` | GPUMD validation gate |
| `nano_sigec/PREREGISTERED_SHA256` | SiGeC design digest |
| `nano_sigec/sigec_design.json` | SiGeC design |
| `nano_sigec/preregister_sigec.py` | SiGeC pre-registration |
| `nano_sigec/results` | SiGeC analysis outputs named by the campaign record |
| `nano_sigec/m1` | first MACE carbon-site run (failed gate) |
| `nano_sigec/m1c` | converged MACE rerun (strengthen decision) |
| `party5_databases/open_db` | Starrydata pinned slice |
| `party5_databases/version_bump` | database version-bump revision demo |
| `ai_theorist` | AI-theorist rounds 1 and 2: brief, rubric, answers, grades (campaign-record entries 122-125, 128-129) |
| `phase_c` | retrospective SiGe campaign: evidence tables, fitted law, record signatures and time-stamp anchors, second detector version (detector_v2) |
| `party5_databases` | pinned database releases (Citrine, Starrydata) and the release-update record |
| `pilot/results/pilot_summary.json` | pilot revision-action campaign |
| `nano_sigec/small_sic` | atomistic SiC checks: designs, raw outputs, decisions |
| `nano_sigec/si_zone` | Si-rich-zone follow-up: design, raw outputs, decision |

Files outside these folders that a script reads (traced):

- `p2_exceptional/exceptional_criteria.json`
- `pilot/kg/extracted_points.json`

## Figures

Each figure is drawn by one script at its print size and written to `paper/figure_code/figures/` (plus a 600 dpi PNG). Run from this folder with a Python that has numpy, scipy, matplotlib, scikit-learn and ase:

| figure | command |
|---|---|
| `fig_endpoint_campaign` | `python3 paper/figure_code/regen_figs/fig_endpoint_campaign.py` |
| `fig_planted` | `python3 paper/figure_code/regen_figs/fig_planted.py` |
| `fig_record_schematic` | `python3 paper/figure_code/regen_figs/fig_record_schematic.py` |
| `fig_sigec_timeline` | `python3 paper/figure_code/regen_figs/fig_sigec_timeline.py` |
| `fig_sizefree` | `python3 paper/figure_code/regen_figs/fig_sizefree.py` |
| `fig_stack_cost` | `python3 paper/figure_code/regen_figs/fig_stack_cost.py` |

## Checkers and analyses

| command |
|---|
| `python3 paper/figure_code/verify_record.py --json /tmp/mat_theory_verify.json` |

`traced_inputs.json` lists every file each command opened when the folder was built; `FILES.sha256` lists the digest of every file in the folder.
