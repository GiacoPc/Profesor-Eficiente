# P1-001 Real Process Interruption Evidence — 001

**Source path:** `docs/00-governance/els-poc/ITER-0003-P1-RESOLUTION-001/P1-001-REAL-PROCESS-INTERRUPTION-001-EVIDENCE.md`
**Source Git blob SHA:** `9ccae73a9de7a39e2d3a22525b22884aea2d7f11`

**Evidence ID:** `P1-001-REAL-PROCESS-INTERRUPTION-001`
**Oracle:** `PASS`
**Failure class:** `process_interruption`
**Fidelity boundary:** POSIX process interruption via `SIGTERM` only
**Execution date:** 2026-09-09

## Repository identity

- Repository: `GiacoPc/Profesor-Eficiente`
- Ref: `els/iter-0003-p1-implementation-001`
- Exact engineering HEAD tested: `7ce7115a0a4d061b4bfd9fdd648eea2a18c2cfed`
- CI workflow: `Governance`
- CI run: `34393234221` (run #294)
- CI job: `102606492355`
- CI conclusion: `success`

## Controller / target separation

- Controller PID: `2134`
- Controller executable: `/usr/bin/python3`
- Controller role: `controller`
- Target PID: `2139`
- Target executable: `/usr/bin/python3`
- Target role: `target`
- Controller and target were distinct OS processes.

## Interruption protocol

1. Controller spawned target process.
2. Target created the checkpoint file.
3. Target wrote the deterministic checkpoint payload.
4. Target flushed the file and called `fsync`.
5. Target signalled readiness.
6. Controller recorded the pre-interruption SHA-256.
7. Controller sent `SIGTERM` to the target PID.
8. Controller waited for target termination.
9. Controller re-opened the persisted checkpoint.
10. Controller recomputed the persisted SHA-256 and compared it with the expected and pre-interruption values.

**Interruption point:** after target `fsync` and readiness signal; before target normal exit.

## Persisted bytes

- Persisted byte length: `153`
- Persisted SHA-256: `c471c4e0836885a0533fab560993b8f818d210f84fc4a9416dca7266dd46e11f`
- Expected SHA-256: `c471c4e0836885a0533fab560993b8f818d210f84fc4a9416dca7266dd46e11f`
- Match expected: `true`
- Stable across interruption: `true`
- Checkpoint existed after interruption: `true`

## Observed result

- Target return code: `-15`
- `SIGTERM` termination observed: `true`
- Bytes matched expected: `true`
- Bytes stable across interruption: `true`
- Checkpoint persisted after interruption: `true`

Therefore the bounded oracle for this test is `PASS`.

## CI artifact provenance

- Artifact name: `p1-001-process-interruption-evidence`
- Artifact ID: `10120465482`
- Artifact ZIP SHA-256: `50da01812cd5952f18b9a1b4b40938c5fe86c51ce4a5ceb1a5181c34d01878c8`
- Evidence JSON SHA-256: `6cd1f68df9e9ff0c466a8d7d7b6648bc7962f7f20ed11fd1e9a6abd37a2d9b15`

## Evidence boundary

This evidence proves only the executed POSIX process-interruption scenario described above.

It does **not** prove:

- workstation crash recovery;
- power-loss recovery;
- Android process-death recovery;
- provider/IDE quota exhaustion;
- full ELS continuation-gate enforcement;
- P1-004 closure;
- P1-001 closure by itself.

## CI note

The first CI attempt on commit `9fb38acfa488a9a5a88ad19f661fee33e40d3637` failed before reaching the P1-001 tests because the existing Ruby YAML validation invoked unsafe class loading for a `Date` value. That CI infrastructure issue was corrected with a syntax-only `YAML.parse_file` validation in the next commit. The final execution above ran all listed governance and P1-001 steps successfully.

A separate pre-existing secret-hygiene regex in the workflow emitted an invalid-regex diagnostic during the successful run; because that shell condition is inside an `if` and does not fail the step, the step proceeded. This is not used as evidence for the P1-001 oracle and should be treated as a separate CI hardening issue.

## Closure status

`P1-001 = OPEN`

This artifact is execution evidence for the P1-001 criteria. Self-audit, independent L2 review, reconciliation, and human closure remain required by the governing contract.
