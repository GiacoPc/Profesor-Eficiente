# P1-001-C / WB-001 Execution Evidence — 001

**Evidence ID:** `P1-001-C-WB001-PARTIAL-WRITE-001`  
**Criterion:** P1-001-C  
**Write boundary:** WB-001 — evidenced single-file write  
**Oracle result:** `INVALID`  
**Failure class:** `partial_write`  
**Execution status:** EXECUTED

## Governing contract

- Contract: `ITER-0003-P1-RESOLUTION-001`
- Version: `v0.2`
- Criterion: `P1-001-C`
- Test specification: `P1-001-C-TEST-SPEC-v0.1.yaml`
- Scope: WB-001 only

## Repository and CI identity

- Repository: `GiacoPc/Profesor-Eficiente`
- Engineering ref: `els/iter-0003-p1-001-c-wb001-execution-001`
- Exact engineering HEAD observed by the executed test: `6ddb9d4e88800c399e52d3ea20da3bc8fb832776`
- Execution ref: `refs/pull/10/merge`
- Ref source: `github-actions-env`
- Workflow: `Governance`
- CI run: `35743631536`
- CI job: `106799462365`
- Workflow source commit: `95225c5fd17c9d94a09fb76c75fbc4f2792063b2`
- CI conclusion: `success`

The distinction between the workflow source commit, engineering HEAD, and PR merge execution ref is intentional. The workflow source commit is `95225c5fd17c9d94a09fb76c75fbc4f2792063b2`; the executed PR merge commit resolved by the checkout is `6ddb9d4e88800c399e52d3ea20da3bc8fb832776`; the engineering ref is the head branch named above.

## Controller / target separation

The WB-001 test uses an independently controlled target process. The controller waits for the deterministic readiness point and then sends `SIGTERM` to the target. The target does not control its own interruption.

The successful CI run executed both the identity-regression test and the WB-001 test under the detached-HEAD GitHub Actions environment.

## Interruption protocol

1. Open the checkpoint path for binary write.
2. Write a deterministic payload in fixed chunks.
3. Flush after each chunk.
4. Signal readiness after exactly three chunks.
5. Controller sends `SIGTERM` before payload completion and before `fsync`.
6. Controller verifies target termination.
7. Controller independently reads the persisted bytes.
8. Controller computes persisted identity and evaluates the deterministic oracle.

**Interruption point:** after deterministic partial write of 768 bytes and flush, before payload completion and `fsync`.

## Artifact identity

- Expected complete artifact length: `8254` bytes
- Expected complete artifact SHA-256: `f3f8655b3909dec9ca6451454804ea9c048b04da2557af9b971e0dc0d93bc2c8`
- Observed persisted length: `768` bytes
- Observed persisted SHA-256: `e5079e8d1342842845ff804f44c134f0e2f177c83a14d476c21758bc3a720d375a6`

## Observed result

- Partial write observed: `true`
- Checkpoint exists after interruption: `true`
- Persisted bytes match expected complete artifact: `false`
- Persisted bytes stable after termination: `true`
- Persisted byte length: `768`
- Pre-interruption byte length: `768`
- Target return code: `-15`
- Target terminated by SIGTERM: `true`
- Deterministic oracle: `INVALID`

The result establishes that the exercised WB-001 boundary can leave a deterministic partial artifact when interrupted before completion and `fsync`.

## CI artifact provenance

- Artifact name: `p1-001-process-and-partial-write-evidence`
- Artifact ID: `10701051356`
- Artifact ZIP digest: `sha256:315f81a0047ad5d1ee16df1b5939e26c328277aadec0d3d455df69dd7fb9d710`
- Artifact contains:
  - `p1-001-c-wb001-partial-write-evidence.json`
  - `p1-001-process-interruption-evidence.json`

## Evidence boundary

This evidence directly supports execution of WB-001 only. It does not establish behavior for persistence mechanisms that were not executed.

It does **not** prove:

- atomic temporary-file replacement;
- append persistence;
- multi-file transaction semantics;
- Android-specific persistence;
- workstation crash recovery;
- power-loss recovery;
- Android process-death recovery;
- provider/IDE quota exhaustion;
- P1-001 closure;
- P1-004 closure;
- ELS operational readiness.

## Status

This is execution evidence for P1-001-C. It does not by itself close P1-001. Self-audit, independent L2 review, reconciliation, and human closure remain required by the governing contract.
