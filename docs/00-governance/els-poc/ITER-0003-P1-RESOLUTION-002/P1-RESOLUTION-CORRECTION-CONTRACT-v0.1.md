# ITER-0003-P1-RESOLUTION-002 — P1 Resolution Correction Contract v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL
**Risk:** L2
**Parent contract:** `ITER-0003-P1-RESOLUTION-001 / P1-RESOLUTION-CONTRACT-v0.1`
**Purpose:** Correct the contract-level defects identified by the independent substantive audit of ITER-0003-P1-RESOLUTION-001.
**Implementation:** NOT AUTHORIZED
**Verifier modification:** NOT AUTHORIZED
**P1 closure:** NOT AUTHORIZED

## 1. Authority and correction boundary

This correction contract is a specification-change proposal. It does not itself approve, implement, or close P1-001 through P1-005.

The authoritative target remains the P1 Resolution contract and its machine-readable acceptance matrix. The two representations MUST express the same dependency graph, criteria, and closure semantics.

The verifier and verifier tests remain frozen during this correction review. No implementation work is authorized by this document.

The correction is based on the independent substantive audit of the supplied ITER-0003 package, whose principal finding was `P1-C-001`: the Markdown contract and YAML matrix disagreed on the dependency edge `P1-001 -> P1-002`.

## 2. Correction objectives

This iteration MUST:

1. remove the Markdown/YAML dependency conflict identified as `P1-C-001`;
2. preserve the minimal logical dependency graph already expressed by the prose contract;
3. define `independently executed` for P1-001-B sufficiently to make the criterion falsifiable without prescribing a particular implementation;
4. make unsupported repository topologies fail closed as `UNKNOWN` or `CONFLICT` rather than permitting silent acceptance;
5. extend the P1-004 anti-bypass property beyond a single named workflow to the governed continuation surface;
6. require an explicit, versioned declaration of verifier-supported repository topologies;
7. keep implementation, verifier changes, P1 closure, and ELS readiness outside this iteration's authority.

## 3. Canonical dependency graph

The canonical graph for P1-001 through P1-005 is:

```text
P1-001 ───────────────┐
                      ├──> P1-004 ───> operational continuation gate
P1-002 ───> P1-005 ───┤
                      │
P1-003 ───────────────┘
```

Equivalent edge set:

```text
P1-001 -> P1-004
P1-002 -> P1-005
P1-005 -> P1-004
P1-003 -> P1-004
```

**There is NO dependency `P1-001 -> P1-002`.**

Rationale:

- P1-001 governs continuity/recovery evidence fidelity.
- P1-002 governs adversarial verifier coverage.
- P1-002 is a prerequisite for P1-005 because adversarial coverage establishes the envelope within which verifier behavior is trusted.
- P1-005 establishes content/provenance integrity consumed by P1-004.
- P1-001 and P1-003 independently provide evidence properties consumed by P1-004.

No P1 may be considered satisfied solely because another P1 is satisfied.

## 4. P1-001-B independence definition

For this contract, **independently executed** means that the interruption test is executed as a separately identifiable test execution against the target process/state, using a procedure and evidence record that are not merely a manual assertion by the authoring agent or by the artifact under test.

The evidence record MUST identify:

- the test actor or execution context;
- the target process/state being interrupted;
- the interruption mechanism;
- the execution timestamp or equivalent ordering identity;
- the persisted checkpoint artifact examined after interruption;
- the exact repository identity associated with the recovery state;
- the observed recovery result.

Independence does NOT require a different model/provider by itself, and does NOT require a particular operating system, process supervisor, CI system, or implementation technique. Those properties are separate evidence questions.

A test report written after the fact without durable execution evidence does not satisfy the criterion merely because it claims that an interruption occurred.

Real workstation/power-loss, Android process-death, and provider/IDE quota evidence remain distinct evidence classes and retain the original `UNVERIFIED` boundaries.

## 5. P1-002-C unsupported topology rule

The verifier-supported repository topology MUST be explicit and versioned before adversarial coverage can be considered complete.

For any topology encountered by a test or verification request:

- if it is declared supported, the corresponding behavior MUST be covered by an applicable acceptance test;
- if it is declared unsupported, the verifier MUST classify it conservatively as `UNKNOWN` or `CONFLICT` and MUST NOT silently accept it as a valid supported state;
- if support status is not declared or cannot be determined, the result is `UNKNOWN` and cannot satisfy a PASS criterion.

The phrase `where supported/declared` MUST NOT be interpreted as permission for silent acceptance of an undeclared topology.

## 6. P1-002 topology declaration

A versioned topology declaration is part of the admissibility contract for verifier testing.

At minimum, the declaration MUST identify:

- declaration identity/version;
- repository topology classes intentionally supported;
- topology classes intentionally unsupported;
- required conservative outcome for unsupported/undeclared classes;
- relationship to the verifier version under test.

The declaration is a specification artifact. It does not itself prove that the implementation behaves correctly for the declared classes.

## 7. P1-004 governed continuation surface

The non-bypassability property applies to the **governed continuation surface**, not merely to one named workflow.

For this contract, the governed continuation surface means every project-controlled mechanism that can authorize or initiate a subsequent governed engineering mutation on the basis of checkpoint/ELS continuation state.

Acceptance requires that:

1. every registered continuation entry point resolves to the same machine-checkable continuation decision;
2. `CURRENT CHECKPOINT VERIFICATION = PASS` remains a mandatory precondition;
3. `UNKNOWN`, `CONFLICT`, missing, stale, or identity-mismatched checkpoint state blocks continuation;
4. regression-suite success alone cannot authorize continuation;
5. a branch name, command variant, manual assertion, alternate registered entry point, or parallel continuation mechanism cannot bypass the gate;
6. any unregistered or undisclosed continuation mechanism is treated as an unproven bypass surface and prevents a claim of universal non-bypassability until its status is resolved;
7. gate evidence records the exact repository identity and decision evaluated.

This defines the property without prescribing whether enforcement is implemented through hooks, CI, scripts, an orchestrator, or another mechanism.

## 8. P1-005 preservation

The correction does not weaken P1-005.

The checkpoint bytes being validated and the immutable repository object used as provenance MUST remain cryptographically/logically bound to the same artifact before integrity is declared.

The correction MUST preserve:

- immutable content identity or demonstrable content-to-object correspondence;
- rejection of working-tree substitution;
- detection or conservative classification of concurrent/partial modification;
- independently derivable provenance;
- rejection of content/provenance mismatch;
- avoidance of self-referential checkpoint identity requirements.

The concrete binding mechanism remains an implementation decision subject to the approved contract and later audit.

## 9. Acceptance criteria for this correction

**R-001:** Markdown and YAML express exactly the same P1 dependency graph; specifically, neither representation contains `P1-001 -> P1-002`.

**R-002:** The canonical dependency graph is acyclic and contains exactly the four intended edges defined in §3.

**R-003:** P1-001-B contains an operationally testable definition of independent execution and does not conflate test independence with real-world failure classes.

**R-004:** P1-002-C requires unsupported and undeclared repository topologies to resolve conservatively to `UNKNOWN` or `CONFLICT` and forbids silent acceptance.

**R-005:** A versioned declaration of verifier-supported repository topologies is required as an implementation admissibility artifact.

**R-006:** P1-004's non-bypassability property covers the governed continuation surface, including alternate registered and parallel continuation mechanisms, without prescribing a specific enforcement technology.

**R-007:** The correction preserves `UNKNOWN`/`CONFLICT` blocking semantics and does not permit regression-suite PASS to substitute for current-checkpoint verification.

**R-008:** P1-005's content/provenance binding and anti-self-reference requirements remain intact.

**R-009:** The corrected Markdown specification and machine-readable matrix are semantically identical for identity, status, risk, authorization, dependencies, criteria, closure rules, and L2 review requirements.

**R-010:** The correction introduces no implementation authorization, verifier modification authority, P1 closure authority, or ELS operational-readiness authority.

## 10. Required correction sequence

1. Apply the contract correction represented by this document to the P1 Resolution specification and its acceptance matrix.
2. Cross-check Markdown and YAML mechanically or by an equivalent exact review.
3. Produce correction evidence identifying the exact files and repository identity reviewed.
4. Run the contract-level self-audit.
5. Prepare a new independent L2 audit package containing the corrected contract and matrix plus the relevant correction/reconciliation context.
6. Obtain a fresh independent secondary audit.
7. Reconcile the external audit against repository evidence.
8. Seek explicit human approval of the corrected P1 Resolution contract.
9. Only after approval may the project evaluate authorization for L2 implementation.

## 11. Closure rules

This correction iteration is `CONVERGED` only if all R-001 through R-010 are demonstrated by direct evidence and no blocking `UNKNOWN` or `CONFLICT` remains.

An external auditor's PASS does not by itself approve the contract. Human approval remains mandatory.

A failed or incomplete correction returns the iteration to `BLOCKED` and requires a new correction cycle; it does not authorize implementation.

## 12. Explicit non-actions

This iteration does NOT:

- modify `tools/els/checkpoint_integrity_verifier.py`;
- modify verifier tests;
- close P1-001 through P1-005;
- approve ELS-CHECKPOINT v0.2 anew;
- declare ELS operational readiness;
- authorize autonomous continuation;
- authorize implementation before human approval and the required independent L2 review.

## 13. Decision

**PROPOSED / REQUIRES HUMAN APPROVAL.**

The parent P1 Resolution contract remains unapproved until the correction is applied to the authoritative contract/matrix pair, independently audited, reconciled, and approved by the human project authority.
