# ITER-0003-P1-RESOLUTION-001 — P1 Resolution Technical Contract v0.2

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Risk:** L2
**Implementation:** NOT AUTHORIZED
**Verifier modification:** NOT AUTHORIZED by this contract
**Supersedes for review:** `P1-RESOLUTION-CONTRACT-v0.1.md`
**Scope:** P1-001 through P1-005

## 1. Purpose and authority boundary

This contract defines the exact properties, evidence, tests, provenance rules, and authorization conditions that an implementation must satisfy before the five open P1 findings may be recommended for closure.

This contract does not authorize implementation. Human approval is required before implementation begins.

The repository is the engineering source of truth. Audit findings are evidence inputs, not authority. No P1 may be closed by assertion, model verdict alone, or a passing test that does not establish the required property.

During contract review, the existing verifier and its tests remain frozen. This contract does not authorize modification of `tools/els/checkpoint_integrity_verifier.py`.

## 2. Evidence semantics

A criterion is `PASS` only when its prescribed evidence directly establishes the required property.

Allowed outcomes:

- `PASS` — required property demonstrated by direct evidence.
- `FAIL` — evidence demonstrates violation.
- `UNKNOWN` — evidence unavailable, inaccessible, or inconclusive.
- `CONFLICT` — authoritative or repository evidence disagrees.

`UNKNOWN` and `CONFLICT` block P1 closure and block continuation authorization.

A regression-suite PASS is never equivalent to current-checkpoint verification.

Evidence records MUST identify, where applicable:

- repository/ref;
- exact engineering HEAD;
- exact artifact path;
- exact Git object identity where relevant;
- test/fixture identifier;
- invocation path;
- environment/failure class;
- expected oracle;
- observed result;
- evidence artifact identifier;
- timestamp or run identity when temporal ordering matters.

A model/agent verdict is never itself an oracle.

## 3. Canonical dependency graph

The v0.1 Markdown/YAML dependency conflict is resolved by declaring the P1 findings as independent integrity prerequisites to P1-004:

```text
P1-001 ───────────────┐
P1-002 ───────────────┤
P1-003 ───────────────┼──> P1-004 ───> continuation authorization
P1-005 ───────────────┘
```

There is **no dependency edge between P1-001 and P1-002**, and no dependency edge from P1-002 to P1-005. Their implementation/test sequencing may be ordered operationally, but sequencing is not dependency.

Interpretation:

- P1-001 establishes continuity/recovery evidence semantics.
- P1-002 establishes adversarial verifier behavior and its test envelope.
- P1-003 establishes exact-head CI evidence.
- P1-005 establishes immutable checkpoint content/provenance binding.
- P1-004 consumes the resulting integrity properties and is the authorization gate; it does not replace them.

The Markdown graph and machine-readable matrix MUST contain exactly this dependency graph.

## 4. P1-001 — Continuity/recovery evidence fidelity

### Required property

Recovery evidence must identify its failure class and evidence boundary and must never promote lower-fidelity simulation to a higher-fidelity claim.

### Acceptance criteria

**P1-001-A:** A machine-readable test specification records `failure_class`, `environment`, `interruption_method`, `interruption_point`, `persisted_artifact`, `expected_recovery`, `evidence_boundary`, and exact repository identity.

**P1-001-B:** At least one independently executed process-interruption test demonstrates durable checkpoint recovery after unexpected process termination. The evidence MUST record process identity, interruption method, pre-interruption checkpoint identity, post-interruption recovery result, and exact repository identity. `independent` means the interruption is performed by a controller distinct from the process being terminated; the controller and target identities MUST be recorded.

**P1-001-C:** Partial/interrupted writes are exercised through at least one reproducible test for each supported write boundary. The oracle MUST deterministically classify the resulting state as `RECOVERABLE`, `INVALID`, `CONFLICT`, or `UNKNOWN` using an explicit decision table.

**P1-001-D:** Claims of workstation crash, power loss, Android process death, or equivalent higher-fidelity failure remain `UNVERIFIED` unless the corresponding failure class is actually executed and evidenced. A process-level simulation cannot satisfy a higher-fidelity claim by inference.

**P1-001-E:** Quota exhaustion is a distinct evidence class. Synthetic budget exhaustion cannot satisfy a real provider/IDE quota claim. A real provider/IDE quota claim requires provider/IDE evidence identifying the relevant quota event.

### Closure evidence

Test specification + execution evidence + exact identity + evidence boundary + self-audit + independent L2 review.

## 5. P1-002 — Verifier adversarial coverage

### Required property

The verifier deterministically classifies every supported adversarial state without accepting inconsistent checkpoint content/provenance as `PASS`.

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
11. repository-root/path-boundary escape;
12. state-head/tree mismatch;
13. unreachable storage commit;
14. storage commit not descending from state head;
15. incorrect declared storage metadata;
16. diagnostic reason correctness;
17. current-checkpoint verification versus generic fixture regression.

### Acceptance criteria

**P1-002-A:** Every mandatory class has a reproducible fixture and an encoded expected outcome of `PASS`, `CONFLICT`, or `UNKNOWN`.

**P1-002-B:** Expected outcomes are encoded in executable test oracles; no manually asserted result can satisfy the criterion.

**P1-002-C:** Unsupported repository topology is explicitly classified and cannot silently become `PASS`.

**P1-002-D:** A clean control case is `PASS`.

**P1-002-E:** Every tampered/inconsistent mandatory case cannot produce `PASS`.

**P1-002-F:** Each adversarial fixture MUST execute through the same verifier entry point, configuration contract, and output interpretation used for current-checkpoint verification, or a formally documented equivalence proof MUST be provided and independently reviewed. Fixture-only execution through a different path cannot close P1-002.

**P1-002-G:** Diagnostic reason assertions MUST be checked for every mandatory negative class where the reason is part of the contract; status-only matching is insufficient when distinct failure classes are expected to remain distinguishable.

## 6. P1-003 — Exact-head CI evidence

### Required property

Every engineering claim that depends on CI identifies the exact commit tested and provides durable evidence that the CI run executed that commit.

### Acceptance criteria

**P1-003-A:** The claimed engineering commit SHA is recorded.

**P1-003-B:** CI evidence records workflow/run identity, branch/ref, exact head SHA, conclusion, and relevant test job.

**P1-003-C:** Observed run head equals the claimed engineering head exactly.

**P1-003-D:** A successful run on an ancestor or sibling commit cannot satisfy exact-head evidence.

**P1-003-E:** Missing/inaccessible CI evidence yields `UNKNOWN`, never `PASS`.

## 7. P1-004 — Non-bypassable current-checkpoint continuation gate

### Required property

Governed continuation is deny-by-default. No governed continuation authorization may be produced unless the current checkpoint has been freshly verified and all required integrity prerequisites are satisfied.

### Canonical gate contract

The implementation MUST expose exactly one authoritative continuation-decision function/entry point for governed continuation. The function MUST consume a machine-readable gate input and produce a machine-readable decision bound to the exact repository identity evaluated.

Required decision states:

- `CONTINUE_AUTHORIZED`
- `BLOCKED`
- `UNKNOWN`
- `CONFLICT`

Only `CONTINUE_AUTHORIZED` permits governed continuation.

The gate input MUST include at minimum:

- repository ref;
- exact current HEAD;
- checkpoint artifact identity;
- current-checkpoint verification result;
- P1-001 status;
- P1-002 status;
- P1-003 status where CI is required;
- P1-005 status;
- evidence identifiers;
- gate evaluation timestamp/run identity.

### Acceptance criteria

**P1-004-A:** Exactly one authoritative continuation decision exists for the governed continuation surface.

**P1-004-B:** `CURRENT CHECKPOINT VERIFICATION = PASS` is a mandatory precondition for `CONTINUE_AUTHORIZED`.

**P1-004-C:** `CONFLICT`, `UNKNOWN`, missing checkpoint, stale checkpoint, identity mismatch, or failed mandatory P1 blocks continuation.

**P1-004-D:** Regression-suite PASS alone cannot produce `CONTINUE_AUTHORIZED`.

**P1-004-E:** All documented governed continuation entry points invoke the same gate. An alternate command, branch name, manual assertion, or direct implementation path MUST NOT be able to produce governed continuation authorization.

**P1-004-F:** The decision artifact records exact repository identity, checkpoint content identity, all consumed P1 statuses, evidence IDs, and final decision.

**P1-004-G:** Negative tests demonstrate that every blocked state in the gate contract remains `BLOCKED` and cannot be converted to `CONTINUE_AUTHORIZED` through an alternate entry point.

**P1-004-H:** The gate implementation is deny-by-default: absence, malformedness, staleness, or ambiguity of required gate input cannot produce `CONTINUE_AUTHORIZED`.

**P1-004-I:** The governed continuation surface is explicitly enumerated. Any new governed entry point requires the same gate contract and a regression test before it can be considered authorized.

## 8. P1-005 — Immutable checkpoint content/provenance binding

### Required property

The checkpoint bytes validated and the immutable repository object used as their provenance MUST refer to the same artifact before integrity is declared.

The approved `ELS-CHECKPOINT v0.2` contract remains unchanged. Its `state_head` identifies the engineering state; `checkpoint_storage_commit` is derived metadata only and is not a self-authored prerequisite. fileciteturn872file0

### Required binding model

For a committed checkpoint artifact, verification MUST derive the checkpoint content from the immutable Git object addressed by the evaluated repository state/path (for example, the blob reachable at `<HEAD>:<checkpoint-path>`) and parse those exact bytes, or use an independently proven atomic equivalent.

The verifier MUST NOT establish provenance from one byte sequence while parsing another working-tree byte sequence.

### Acceptance criteria

**P1-005-A:** Verification operates on immutable content identity or proves exact content-to-object correspondence before accepting the checkpoint.

**P1-005-B:** Working-tree modification after the claimed commit cannot result in `PASS` for modified bytes.

**P1-005-C:** Concurrent/partial modification is detected or conservatively classified as `UNKNOWN`/`CONFLICT`.

**P1-005-D:** Provenance is independently derived from repository evidence and is never trusted solely because it appears inside the checkpoint payload.

**P1-005-E:** Tests prove that committed bytes versus modified working-tree bytes are distinguished and the modified bytes cannot be accepted as the committed checkpoint.

**P1-005-F:** The implementation does not require a self-authored `checkpoint_storage_commit` to validate itself. `checkpoint_storage_commit` remains derived metadata under ELS-CHECKPOINT v0.2.

**P1-005-G:** The implementation is deterministic with respect to the selected repository state/path: the same exact Git object and path MUST yield the same parsed checkpoint bytes.

## 9. Cross-P1 closure and authorization gates

A P1 closure recommendation requires:

1. every criterion for that P1 = `PASS`;
2. all mandatory dependencies = `PASS`;
3. no mandatory `UNKNOWN` or `CONFLICT`;
4. exact repository identity recorded;
5. required exact-head CI evidence available;
6. self-audit complete;
7. independent L2 secondary audit complete;
8. reconciliation complete;
9. human approval of closure.

A `CONTINUE_AUTHORIZED` decision additionally requires all five P1 findings to be closed under these rules.

## 10. Implementation admissibility conditions

An implementation is admissible for this contract only if all of the following are true:

- it preserves ELS-CHECKPOINT v0.2 semantics;
- it implements the canonical dependency graph in Section 3;
- it implements immutable checkpoint content/provenance binding from Section 8;
- it provides the mandatory adversarial coverage and same-path requirement from Section 5;
- it provides exact-head CI evidence from Section 6;
- it implements the deny-by-default continuation gate from Section 7;
- it provides executable negative tests for all mandatory blocked states;
- it does not rely on model assertions as evidence or authorization;
- it does not silently upgrade UNKNOWN/CONFLICT to PASS;
- it does not introduce self-referential checkpoint validity requirements;
- it provides machine-readable evidence sufficient for independent audit;
- it passes self-audit and the required independent L2 audit before closure recommendation.

## 11. Implementation sequencing

Sequencing is an execution plan, not a dependency declaration:

1. formalize P1-001 evidence schema and partial-write decision table;
2. define/implement P1-002 adversarial matrix and same-path tests;
3. implement P1-005 immutable content/provenance binding;
4. implement P1-004 continuation gate around the verified property;
5. integrate P1-003 exact-head CI evidence;
6. execute full regression and negative suites;
7. capture exact evidence;
8. self-audit;
9. independent L2 audit;
10. reconcile and seek human closure.

No implementation step is authorized until this v0.2 contract is human-approved.

## 12. Protected non-actions

This contract does not:

- approve implementation;
- modify the verifier;
- modify verifier tests;
- alter ELS-CHECKPOINT v0.2;
- close P1-001..P1-005;
- authorize ELS operational readiness;
- authorize autonomous continuation.

## 13. Decision

**PROPOSED / REQUIRES HUMAN APPROVAL.**

`P1-RESOLUTION-CONTRACT-v0.1.md` is rejected for approval by the reconciliation decision. This v0.2 is the corrected candidate and remains unapproved until human authority and the required independent L2 contract audit are complete.
