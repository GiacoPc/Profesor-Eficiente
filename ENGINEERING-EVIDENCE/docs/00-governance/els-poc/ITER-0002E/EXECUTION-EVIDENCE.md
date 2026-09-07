# ELS-POC-002E — Execution Evidence

**Status:** PASS_WITH_LIMITATIONS

## Functional execution
An isolated temporary Git repository was used to exercise the verifier logic with four regression cases:

| Case | Expected | Observed |
|---|---|---|
| Corrected checkpoint: `state_head` precedes checkpoint commit | PASS | PASS |
| Historical/self-referential storage claim disagrees with Git evidence | CONFLICT | CONFLICT |
| Incorrect `state_tree` | CONFLICT | CONFLICT |
| Current branch differs from checkpoint `repository.ref` | CONFLICT | CONFLICT |

The positive case explicitly demonstrates the required ELS-POC-001 correction: the checkpoint-storage commit advances `HEAD` while `state_head` remains the earlier engineering state.

## Repository implementation
- `tools/els/checkpoint_integrity_verifier.py` implements the read-only verifier.
- `tools/els/test_checkpoint_integrity_verifier.py` contains the four regression cases.
- `.github/workflows/governance.yml` invokes the regression suite on workflow execution.

## Evidence boundary
The functional test was executed in an isolated local Git fixture. A GitHub-hosted workflow result for this exact branch HEAD was not independently observed through the available GitHub run-query surface; therefore CI execution is **NOT CLAIMED**.

## Safety
The verifier performs read-only Git/file inspection and does not repair, rewrite, force-update, merge, cherry-pick, or delete repository state.

## Result
**POC-002E functional verifier: PASS_WITH_LIMITATIONS.**

This does **not** establish ELS production readiness or make the revised checkpoint contract APPROVED. Human approval of the revised checkpoint contract remains required, and real crash/restart, provider quota exhaustion, and genuinely independent secondary-agent execution remain pending.
