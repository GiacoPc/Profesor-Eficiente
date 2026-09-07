# ELS-POC-002F — Execution Evidence

**Status:** PASS_WITH_LIMITATIONS

## Human approval
ELS-CHECKPOINT v0.2 was explicitly approved by the human project authority with:

`APROBADO — ELS-CHECKPOINT v0.2`

The approved scope is limited to ELS-CHECKPOINT v0.2; this does not approve the wider ELS.

## Contract state
The checkpoint contract was promoted from `0.2-draft / PROPOSED` to `0.2 / APPROVED` in commit `46534917644be9cabb80c7d49489fb4fbe51fa57`.

## Exact-head GitHub CI evidence
GitHub Actions run `34072938168` (Governance, run #222) was observed as:

- branch: `recovery/els-poc-002`
- head SHA: `46534917644be9cabb80c7d49489fb4fbe51fa57`
- status: `completed`
- conclusion: `success`

This is exact-head evidence for the contract-approval commit.

## Checkpoint contract validation
The approved contract requires:

- `repository_ref` as required identity;
- `state_head` as the engineering state to resume from;
- optional `state_tree`;
- `checkpoint_storage_commit` as derived metadata only;
- conflicts between derived storage metadata and repository evidence to block continuation;
- preservation of the original conflicting checkpoint artifacts.

The POC-002E verifier regression suite previously demonstrated the four required outcomes: corrected checkpoint `PASS`, historical storage-claim conflict `CONFLICT`, incorrect tree `CONFLICT`, and incorrect repository ref `CONFLICT`.

## Evidence boundary
The verifier's functional execution remains a local isolated Git-fixture test. The exact-head GitHub CI evidence above proves workflow execution for the approval commit; it does not by itself prove real workstation crash/restart recovery, provider quota exhaustion, or genuinely independent secondary-agent execution.

## Safety
No force-update, merge, cherry-pick, repair rewrite, or deletion of prior forensic/POC evidence was performed in this iteration.

## Result
**POC-002F contract approval + exact-head CI checkpoint: PASS_WITH_LIMITATIONS.**

Remaining ELS operational gates include real crash/restart execution, real provider quota-exhaustion execution, genuinely independent secondary-agent execution, and broader ELS operational-readiness review.
