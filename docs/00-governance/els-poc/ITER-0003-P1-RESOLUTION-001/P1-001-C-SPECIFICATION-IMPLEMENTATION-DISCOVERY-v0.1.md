# P1-001-C — Specification / Implementation Discovery v0.1

**Status:** DISCOVERY_COMPLETE_WITH_BOUNDARY / TEST EXECUTION NOT STARTED
**Finding:** P1-001-C
**Governing contract:** `P1-RESOLUTION-CONTRACT-v0.2.md`
**Engineering ref:** `els/iter-0003-p1-implementation-001`
**Engineering HEAD inspected:** `7ce7115a0a4d061b4bfd9fdd648eea2a18c2cfed`

## 1. Objective

Determine, from repository evidence, which write boundaries are actually implemented/supported and therefore must be exercised under P1-001-C. This discovery must not invent unsupported write mechanisms or infer support merely from the existence of a decision table.

## 2. Governing requirement

P1-001-C requires partial/interrupted writes to be exercised through at least one reproducible test for **each supported write boundary**, with deterministic oracle outcomes `RECOVERABLE`, `INVALID`, `CONFLICT`, or `UNKNOWN`.

The evidence schema defines the required oracle inputs as `write_boundary`, `persisted_bytes_identity`, `expected_artifact_identity`, `parse_or_integrity_result`, and `repository_identity`.

## 3. Repository evidence inspected

### 3.1 P1-001 implementation increment

`P1-001-IMPLEMENTATION-NOTE-v0.1.md` states that the increment formalized the evidence schema, failure-class vocabulary, fidelity rules, controller independence, and the partial-write decision table. It explicitly lists as a next evidence step: execute reproducible tests for each supported write boundary. It does not enumerate those boundaries.

### 3.2 P1-001 evidence schema

`P1-001-EVIDENCE-SCHEMA-v0.1.yaml` defines `partial_write` as a failure class and defines the deterministic oracle states. It does not enumerate concrete supported write mechanisms/boundaries.

### 3.3 Existing P1-001 process-interruption implementation

`tools/els/test_p1_001_process_interruption.py` contains one concrete persistence operation:

1. open a checkpoint path in binary write mode;
2. write the complete payload;
3. flush the Python file buffer;
4. call `os.fsync()` on the file descriptor;
5. signal readiness;
6. remain alive;
7. controller sends SIGTERM after the durable-write point;
8. controller reads the persisted bytes and compares their SHA-256 identity.

This is direct evidence of a **single-file, overwrite/create, fully-written-then-fsync persistence boundary** in the P1-001 test fixture. The test does not exercise interruption during the write itself.

### 3.4 Existing checkpoint verifier

`tools/els/checkpoint_integrity_verifier.py` reads the supplied checkpoint using `Path.read_text()`, then derives Git storage metadata using repository history. The verifier therefore is not itself a partial-write persistence implementation. Its current working-tree read is also a known P1-005 concern and must not be silently treated as evidence that the verifier supports a particular write boundary.

### 3.5 Existing verifier regression tests

`tools/els/test_checkpoint_integrity_verifier.py` creates a complete `checkpoint.yaml` with `Path.write_text()` and then commits it. The tests cover identity/conflict cases, not interrupted-write behavior. They do not establish a partial-write test envelope.

### 3.6 Historical ELS checkpoint records

`ITER-0002D/CHECKPOINT-CONTRACT-v0.2-DRAFT.yaml` and its reconciliation record establish the approved ELS-CHECKPOINT v0.2 identity model: `state_head` identifies engineering state; storage identity is derived repository metadata; storage commit is not a self-authored validity prerequisite. These records do not define a catalogue of partial-write mechanisms.

`ITER-0002G/FAILURE-SIMULATION.md` documents executable process interruption/restart and synthetic budget exhaustion simulations, but it does not establish concrete partial-write boundaries.

## 4. Boundary determination

| Candidate boundary | Classification | Evidence basis | P1-001-C test authorization from current evidence |
|---|---|---|---|
| Single-file complete write followed by `flush()` + `fsync()` | **FACT / EVIDENCE** | `tools/els/test_p1_001_process_interruption.py` | Yes — concrete existing write path can be used as a reference boundary, but an interruption-during-write test has not yet been executed |
| Single-file partial write during `write()` before completion | **INFERENCE / IMPLEMENTATION TARGET** | Natural interruption point implied by the existing file-write operation | Not yet authorized as an existing supported boundary; requires explicit test design against the actual implementation path |
| Temporary-file + atomic rename/replace | **UNKNOWN** | No implementation evidence found in the inspected repository tree | No |
| Append-based checkpoint persistence | **UNKNOWN** | No implementation evidence found | No |
| Multi-file checkpoint transaction | **UNKNOWN** | No implementation evidence found | No |
| Android-specific persistence boundary | **UNKNOWN / OUT OF CURRENT IMPLEMENTATION** | No Android implementation exists in the inspected tree; P1-001 fixture is POSIX Python | No |
| Workstation/power-loss persistence boundary | **UNKNOWN / HIGHER-FIDELITY FAILURE CLASS** | Explicitly outside current POSIX fixture evidence | No |
| Provider/IDE quota write boundary | **UNKNOWN / DISTINCT FAILURE CLASS** | Contract treats quota exhaustion separately | No |

## 5. Discovery result

The repository currently provides **evidence of one concrete file-persistence mechanism in the P1-001 process-interruption fixture**, but it does **not** provide a normative catalogue of all supported write boundaries for the broader ELS system.

Therefore:

- it is incorrect to claim that the complete set of supported write boundaries has been discovered;
- it is incorrect to invent atomic-rename, append, multi-file, Android, power-loss, or quota boundaries as supported mechanisms;
- the existing fixture establishes a concrete reference persistence path, not completion of P1-001-C;
- an interruption-during-write test may be designed around that concrete path only after the test's intended interruption point and deterministic oracle are explicitly specified;
- any broader claim remains `UNKNOWN` until implementation evidence establishes the corresponding write boundary.

## 6. Decision

**P1-001-C remains OPEN.**

**Current control state:** `BLOCKED_FOR_COMPLETE_BOUNDARY_CATALOGUE`.

The correct next engineering action is not to execute a broad matrix of invented mechanisms. The next action is to formalize the supported-boundary inventory from the actual persistence implementation surface, then define reproducible interruption points and execute only those evidenced boundaries.

No P1-002, P1-004, or ELS continuation authorization is affected by this discovery.

## 7. Evidence boundary

This discovery is based on repository artifacts and the exact tree of engineering HEAD `7ce7115a0a4d061b4bfd9fdd648eea2a18c2cfed`. It does not claim inspection of an Android runtime implementation, workstation crash behavior, power loss, provider quota behavior, or unobserved external persistence systems.
