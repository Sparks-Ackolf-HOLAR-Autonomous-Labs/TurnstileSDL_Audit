# Grading rubric (fixed before any theorist answer was read)

Per hindcast question (H1 to H9):
1. Category score: 1 if the category equals the outcome key, else 0.
2. Brier score on the category: (p_category - hit)^2, lower is better.
3. Value score: 1 if |value - outcome| <= tol_abs, or |ln(value/outcome)| <= tol_logratio.
4. Interval coverage: 1 if the outcome lies inside value_range.
A theorist is compared with the data-only baseline on items 1 and 3.
Open questions O1 to O3 are not graded now; their answers are hashed onto the
ledger and graded by the registered rule when the runs exist (P4 stage T1 and
a later foundation-potential version check).
The outcome key file (outcome_key.json) is hashed onto the ledger with this
rubric before the theorists run and is added to the repository only after
their answers are hashed onto the ledger.
