# Verifier replay on a second machine and operating system (2026-10-04)

The record was checked from the per-paper archive, not from a git clone:

1. `paper_repos/paper2_verifiable_revision/` zipped without PDFs and figures
   (83 MB, SHA-256 `579b5d08...acf8c`), copied to sparksone (Windows 10,
   Intel i9-9900K, x86-64) and re-hashed there before unpacking.
2. Python 3.12.7 from the python.org embeddable zip, unpacked in the
   workspace (no installer, no system change, no third-party packages).
   Tools taken from the machine as found: Windows OpenSSH 9.5
   `ssh-keygen` (signatures) and OpenSSL for Windows (`openssl ts`).
3. `python paper/figure_code/verify_record.py --json ...`

Result (`verify_record_result_windows.json`): 46 of 46 checks pass in
3.3 s, against 46 of 46 in 1.3 s on the DGX (aarch64, Linux). The
git-ignore check is skipped outside a clone (`git_ignore_check: false`);
every other check is identical. The workspace was deleted afterwards.

One portability fault was found and fixed: Windows OpenSSH waits forever
on a message piped from Python, so `ledger_sign.py` now passes the message
as a file handle.

This is a second machine run by the same agent, not the replay by an
outside group that the paper still lists as open.
