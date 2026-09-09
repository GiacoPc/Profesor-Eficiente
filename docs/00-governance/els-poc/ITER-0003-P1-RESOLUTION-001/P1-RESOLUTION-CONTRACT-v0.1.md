# ITER-0003-P1-RESOLUTION-001 — P1 Resolution Technical Contract v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Risk:** L2
**Implementation:** NOT AUTHORIZED
**Scope:** P1-001 through P1-005

## 1. Authority and boundary

This contract defines what must be proven before the five open P1 findings may be considered for closure. It does not authorize implementation.

The repository is the engineering source of truth. Audit findings are evidence inputs, not authority. No P1 may be closed by assertion, model verdict alone, or a passing test that does not establish the required property.

The verifier implementation is frozen during contract review. In particular, `tools/els/checkpoint_integrity_verifier.py` is not modified by this iteration.

## 2. Common acceptance semantics

A P1 is `SATISFIED` only when its acceptance criteria have direct evidence and all mandatory dependencies are satisfied.

Possible evidence outcomes:

- `PASS` — required property demonstrated by the prescribed evidence.
- `FAIL` — prescribed test/evidence demonstrates violation.
- `UNKNOWN` — required evidence is unavailable or inconclusive.
- `CONFLICT` — authoritative or repository evidence disagrees.

`UNKNOWN` and `CONFLICT` block P1 closure.

A regression-suite PASS is not equivalent to verification of the current checkpoint. The latter is a distinct property and must have an explicit evidence record.

## 3. Dependency graph

```text
P1-001 ───────────────┐
                      ├──> P1-004 ───> operational continuation gate
P1-002 ───> P1-005 ───┤
                      │
P1-003 ───────────────┘

P1-002 ───> P1-005
P1-005 ───> P1-004
P1-001 ───> P1-004
P1-003 ───> P1-004

P1-001, P1-002, P1-003, P1-005 are evidence/integrity prerequisites for the gate. P1-004 consumes the resulting verification properties; it does not replace them.
```

Dependency interpretation:

- P1-002 establishes the adversarial test envelope needed to trust verifier behavior.
- P1-005 establishes content/provenance integrity that the verifier must preserve.
- P1-001 establishes recovery semantics and failure-boundary evidence.
- P1-003 establishes CI evidence at the exact engineering state being claimed.
- P1-004 integrates these properties into a non-bypassable continuation decision.

No dependency permits one P1 to be declared closed merely because another P1 is satisfied.

## 4. P1-001 — Continuity/recovery evidence fidelity

**Problem:** Existing continuity evidence is a process-level/synthetic simulation, not evidence of workstation, power-loss, Android process-death, or real provider quota behavior.

### Required property

The project must explicitly distinguish process-level recovery simulation from higher-fidelity failure/restart evidence and must not represent one as the other.

### Acceptance criteria

**P1-001-A:** The test specification identifies the failure class, environment, interruption point, persisted artifact, expected recovery behavior, and evidence boundary.

**P1-001-B:** At least one independently executed process interruption test demonstrates durable checkpoint recovery after unexpected process termination, with exact repository identity captured.

**P1-001-C:** Partial-write or interrupted-write behavior is tested and the resulting state is classified deterministically as recoverable, invalid, `CONFLICT`, or `UNKNOWN` according to the approved contract.

**P1-001-D:** Real workstation/power-loss and Android process-death claims remain explicitly `UNVERIFIED` unless actually executed and evidenced; synthetic tests cannot satisfy those claims by inference.

**P1-001-E:** Quota exhaustion remains a separate evidence class. Synthetic budget exhaustion cannot be promoted to real provider/IDE quota evidence.

### Closure evidence

Test specification + execution evidence + exact source identity + self-audit + required independent review for L2.

## 5. P1-002 — Verifier adversarial coverage

**Problem:** Existing verifier regression coverage is insufficient for the identified repository/Git adversarial surface.

### Required property

The verifier must deterministically classify supported adversarial states without accepting an inconsistent checkpoint as valid.

### Mandatory test classes

1. detached HEAD;
2. shallow history;
3. rewritten/divergent history;
4. missing Git object;
5. malformed checkpoint;
6. truncated/partial checkpoint;
7. duplicate keys or ambiguous scalar representation;
8. wrong checkpoint path;
9. worktree execution;
10. alternate object database where supported/declared;
11. path-boundary / repository-root escape attempt;
12. state-head/tree mismatch;
13. unreachable storage commit;
14. storage commit not descending from state head;
15. incorrect declared storage metadata;
16. diagnostic reason correctness;
17. current-checkpoint verification versus generic fixture regression.

### Acceptance criteria

**P1-002-A:** Every mandatory class has a reproducible fixture and expected `PASS`, `CONFLICT`, or `UNKNOWN` outcome.

**P1-002-B:** No test relies on a manually asserted result; the expected result is encoded in the test oracle.

**P1-002-C:** Any unsupported repository topology is explicitly classified rather than silently accepted.

**P1-002-D:** A clean control case remains `PASS`.

**P1-002-E:** A tampered/inconsistent case cannot produce `PASS`.

## 6. P1-003 — Exact-head CI evidence

**Problem:** Historical CI runs exist, but exact-head CI for the final claimed checkpoint state was not demonstrated in the reconciliation.

### Required property

Every engineering claim that depends on CI must identify the exact commit tested and provide durable evidence that the CI run executed that commit.

### Acceptance criteria

**P1-003-A:** The claimed checkpoint/implementation commit SHA is recorded.

**P1-003-B:** CI evidence records workflow/run identity, branch/ref, exact head SHA, conclusion, and relevant test job.

**P1-003-C:** The observed run head equals the claimed engineering head byte-for-byte.

**P1-003-D:** A successful run on an ancestor or sibling commit cannot satisfy exact-head evidence for the current claim.

**P1-003-E:** Missing or inaccessible CI evidence yields `UNKNOWN`, not `PASS`.

## 7. P1-004 — Non-bypassable current-checkpoint continuation gate

**Problem:** Current evidence demonstrates tests but not a universal authorization gate requiring fresh verification of the current checkpoint before continuation.

### Required property

Continuation of governed engineering work must be blocked unless the current checkpoint identity has been explicitly verified and the required P1/gate conditions are satisfied.

### Acceptance criteria

**P1-004-A:** There is one explicit continuation decision with machine-checkable outcome.

**P1-004-B:** `CURRENT CHECKPOINT VERIFICATION = PASS` is a required precondition for continuation.

**P1-004-C:** `CONFLICT`, `UNKNOWN`, missing checkpoint, stale checkpoint, or identity mismatch blocks continuation.

**P1-004-D:** Passing the verifier regression suite alone cannot authorize continuation.

**P1-004-E:** The gate cannot be bypassed merely by choosing another command path, branch name, or manual assertion inside the same workflow.

**P1-004-F:** Gate evidence records the exact repository identity evaluated and the decision outcome.

**P1-004-G:** The gate has negative tests proving that blocked states remain blocked.

## 8. P1-005 — Immutable checkpoint content/provenance binding

**Problem:** The verifier currently reads checkpoint content from the working tree while deriving storage identity from Git history. This can create a provenance mismatch between the bytes parsed and the Git artifact used to establish identity.

### Required property

The checkpoint bytes being validated and the immutable repository object used as their provenance must be cryptographically/logically bound to the same artifact before integrity is declared.

### Acceptance criteria

**P1-005-A:** Verification operates on an immutable content identity or otherwise proves content-to-object correspondence before accepting the checkpoint.

**P1-005-B:** Working-tree modification after the claimed commit cannot result in `PASS` for the modified content.

**P1-005-C:** Concurrent/partial modification is detected or conservatively classified as `UNKNOWN`/`CONFLICT`.

**P1-005-D:** The provenance identity is independently derivable from repository evidence and is not trusted solely because it appears inside the checkpoint payload.

**P1-005-E:** Tests demonstrate mismatch between working-tree content and committed content is rejected.

**P1-005-F:** The implementation does not create a new self-referential checkpoint identity requirement that makes the checkpoint impossible to author or verify.

## 9. Cross-P1 acceptance gates

The following are mandatory before any P1 closure recommendation:

- all P1-specific acceptance criteria PASS;
- no mandatory criterion UNKNOWN or CONFLICT;
- exact repository identity recorded;
- exact-head CI evidence available where required;
- self-audit complete;
- independent secondary audit performed for L2 changes;
- reconciliation performed against repository evidence;
- human authority approves closure.

## 10. Implementation sequencing

Recommended order:

1. Freeze and formalize P1-001 evidence semantics.
2. Define P1-002 adversarial verifier matrix.
3. Design P1-005 content/provenance binding using the approved checkpoint contract.
4. Design P1-004 continuation gate around the resulting verified property.
5. Integrate P1-003 exact-head CI evidence into the acceptance pipeline.
6. Implement only after the relevant specification/contract is approved.
7. Run tests and capture evidence.
8. Perform self-audit.
9. Obtain independent secondary audit.
10. Reconcile and seek human closure decision.

## 11. Explicit non-actions

This contract does not:

- modify the verifier;
- modify verifier tests;
- alter ELS-CHECKPOINT v0.2;
- close P1-001..P1-005;
- authorize ELS operational readiness;
- authorize autonomous continuation.

## 12. Contract decision

**PROPOSED / REQUIRES HUMAN APPROVAL.**

Implementation must remain blocked until this contract is approved and any mandatory independent review required for this L2 change is complete.
