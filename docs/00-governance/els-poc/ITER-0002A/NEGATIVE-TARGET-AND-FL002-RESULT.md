# ELS-POC-002A — Negative Target and FL-002 Isolation Result

Status: EXECUTED
Risk: L2
Branch under test: `recovery/els-poc-002`
Canonical base under test: `e15b4aaffc67147c677c22ec52bbf0d9a9cdeb33`

## Test 5 — Incorrect-destination rejection / STOP

Attempted destination: `recovery/els-poc-002-NONEXISTENT-TARGET`.
Operation: create a sentinel artifact through the GitHub write interface.
Observed result: write rejected with HTTP 404 because the destination branch does not exist.
No sentinel artifact was created by this operation.
Result: PASS — fail-closed behavior observed for a nonexistent target.

Scope note: this test validates rejection of an invalid/nonexistent destination. It does not prove rejection of every possible wrong-but-existing destination.

## Test 6 — FL-002 divergent-line isolation

Known divergent line: `697c7fab968e7d03246ad08113b589b3b4cd8a45`.
Comparison: base `e15b4aaffc67147c677c22ec52bbf0d9a9cdeb33` → known divergent commit.
Observed status: `diverged`; the divergent line is 2 commits ahead and 93 commits behind the base, with merge base `025d4708fa3230e05984a7b3fdc44654b1841fb4`.

Comparison: base `e15b4aaffc67147c677c22ec52bbf0d9a9cdeb33` → `recovery/els-poc-002`.
Observed status: `ahead`; branch is 2 commits ahead and 0 behind, and the changed files are only the two ITER-0002A integrity artifacts.

Result: PASS — the known FL-002 divergent line is not incorporated into the POC branch by the observed ancestry/compare evidence.

## Gate assessment

ELS-G00 / target-integrity gate: `PASS_WITH_LIMITATIONS`.

Passed:
- correct existing target was used for the controlled write;
- expected parent was preserved;
- invalid/nonexistent target was rejected without creating the sentinel;
- known FL-002 divergent line is not present in the observed compare from the canonical POC base;
- POC branch changes are limited to ITER-0002A artifacts.

Remaining limitation:
- the negative test did not intentionally write to a different existing branch, because doing so would mutate another real ref and would violate the isolation constraint of this POC.

Therefore this POC demonstrates fail-closed behavior for an invalid target and isolation from the known divergent line, but does not establish universal protection against every wrong existing destination.

No production-readiness claim is made.
