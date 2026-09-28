# P1-001 — EVIDENCE IDENTITY RECONCILIATION v0.1

## Status

`RECONCILED_WITH_DOCUMENTARY_CORRECTION_PENDING`

This document records a read-only forensic reconciliation of the primary GitHub Actions identity chain for the historical P1-001 execution.

It does not close P1-001, authorize continuation, or alter the historical execution evidence.

## Scope

Reconciled execution:

- Workflow: `Governance`
- Run ID: `35743631536`
- Pull request: `#10`
- PR head SHA: `95225c5fd17c9d94a09fb76c75fbc4f2792063b2`
- Execution ref: `refs/pull/10/merge`
- Engineering execution HEAD: `6ddb9d4e88800c399e52d3ea20da3bc8fb832776`
- Branch: `els/iter-0003-p1-001-c-wb001-execution-001`

## Identity chain

The CI runner checked out the pull-request merge ref.

The runner log records:

1. checkout of `refs/remotes/pull/10/merge`;
2. `HEAD is now at 6ddb9d4 Merge 95225c5... into 31c406f...`;
3. `git log -1 --format=%H` returned `6ddb9d4e88800c399e52d3ea20da3bc8fb832776`.

Therefore:

- `95225c5...` is the PR head SHA;
- `6ddb9d4...` is the engineering HEAD actually checked out and tested by the runner.

These values are not contradictory.

## CI identity helper

The execution identity helper resolves:

- repository from `git rev-parse --show-toplevel`;
- engineering HEAD from `git rev-parse HEAD`;
- symbolic ref when available;
- GitHub Actions environment variables when the checkout is detached;
- execution ref from GitHub Actions ref metadata.

The observed detached-HEAD condition is therefore expected for the merge-ref execution and was covered by the identity regression test.

## WB-001 job identity

The primary workflow job executing the P1-001 test sequence is:

`106799462365`

The job contains the identity regression, schema validation, real controller-target SIGTERM test, WB-001 interrupted-write test, and evidence artifact upload.

### Documentary discrepancy

Existing P1-001-C documentation recorded:

`106799420430`

This job ID does not match the primary job returned for workflow run `35743631536`.

This is classified as a **DOCUMENTARY PROVENANCE DEFECT**.

It does not by itself invalidate the execution evidence because the primary workflow run and actual job can be independently resolved.

## Artifact identity

The workflow artifact is:

- Name: `p1-001-process-and-partial-write-evidence`
- Artifact ID: `10701051356`
- Digest: `sha256:315f81a0047ad5d1ee16df1b5939e26c328277aadec0d3d455df69dd7fb9d710`

The upload log for the same job reports the same artifact ID and digest.

## WB-001 primary result

The primary execution log records:

- interruption after deterministic partial write of 768 bytes and flush;
- interruption before payload completion and fsync;
- expected length: 8254 bytes;
- observed length: 768 bytes;
- expected SHA-256:
  `f3f8655b3909dec9ca6451454804ea9c048b04da2557af9b971e0dc0d93bc2c8`;
- observed SHA-256:
  `e5079e8d1342842845ff804f44c134f0e2f177c83a14d476c21758bc3a720d375a6`;
- partial write observed: true;
- bytes stable after termination: true;
- target return code: `-15`;
- target terminated by SIGTERM: true;
- oracle result: `INVALID`.

Both recorded SHA-256 values are 64-character hexadecimal digests.

## Correction to prior external-package representation

A prior external L3 package contained an incorrectly represented observed SHA-256 value for WB-001. The primary CI record contains the 64-character digest documented above.

Therefore:

- the prior package representation was defective;
- the primary WB-001 SHA-256 record is not shown to be defective by this reconciliation.

## Artifact scope

This reconciliation confirms the identity chain and primary execution metadata.

It does not independently prove behavior outside the executed WB-001 boundary.

It does not establish:

- workstation crash behavior;
- power-loss behavior;
- Android process-death behavior;
- other persistence mechanisms;
- real provider or IDE quota exhaustion.

## Reconciliation conclusion

The primary execution identity chain is internally coherent:

`PR head -> merge execution ref -> engineering HEAD -> actual CI job -> artifact -> WB-001 result`

The only confirmed identity defect in the reviewed P1-001-C documentation is the recorded CI job ID.

The reconciliation does not authorize P1-001 closure.

## Governance state

`P1-001 = OPEN`

`CLOSURE_AUTHORIZED = NO`

`CONTINUE_AUTHORIZED = NO`

`ELS_OPERATIONAL_READINESS = BLOCKED`

## Required next action

Before using this evidence for closure, the documentary job-ID discrepancy must be corrected on a governed branch and subjected to the normal validation/reconciliation process.

A refreshed independent L3 package should use the reconciled primary identities and include the relevant primary evidence required for external verification.
