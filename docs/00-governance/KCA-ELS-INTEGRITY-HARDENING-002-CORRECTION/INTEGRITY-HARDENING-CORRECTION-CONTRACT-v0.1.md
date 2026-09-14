# KCA/ELS Integrity Hardening — Correction Contract v0.1

**ID:** KCA-ELS-INTEGRITY-HARDENING-002-CORRECTION  
**Parent:** KCA-ELS-INTEGRITY-HARDENING-001  
**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Risk:** L2  
**Implementation:** NOT AUTHORIZED  
**P1 closure:** NOT AUTHORIZED  
**KCA/ELS readiness:** NOT AUTHORIZED

## 1. Trigger and accepted findings

This correction iteration formally accepts the two substantive P1 findings raised by the independent L2 audit of KCA-ELS-INTEGRITY-HARDENING-001:

- **P1-F21:** wrong-target write / branch-parameter omission was represented in the threat model and incident record but was not elevated to a first-class normative contract requirement and acceptance criterion.
- **P1-C01-C06:** the contract required six pre-implementation contracts but the acceptance matrix did not provide one-to-one, independently testable acceptance traceability for C01–C06.

The findings are accepted as valid blockers. They are not treated as documentation-only defects.

## 2. Correction objective

Strengthen the contract so that the two P1 findings become explicit, independently testable, blocking requirements without authorizing implementation.

## 3. F21 first-class normative control

Every governed repository write MUST follow this sequence:

`TARGET REF DECLARED → TARGET REF RESOLVED → TARGET HEAD VERIFIED → WRITE WITH EXPLICIT TARGET → RE-FETCH TARGET → VERIFY RESULT`

The target branch/ref MUST be an explicit write parameter or an equivalently machine-bound target. An omitted or implicit target is a hard failure. A write MUST NOT proceed when target identity cannot be resolved or verified.

Post-write verification MUST establish that the intended target moved as expected and that no unintended governed ref was modified.

The control MUST apply to every governed write surface, including direct contents writes, Git data operations, automation, agents, IDE integrations, scripts, and future adapters that can mutate canonical state.

F21 is therefore a normative control, not merely a threat-model entry.

## 4. C01–C06 first-class traceability

The following contracts are mandatory implementation preconditions and MUST each have a one-to-one acceptance criterion:

- C01 — Canonical Artifact Identity
- C02 — Context Resolution / Bootstrap
- C03 — Audit-Pack Manifest
- C04 — Prompt/Evidence Compatibility
- C05 — Integrity Validator
- C06 — Continuation Gate Integration

For each C01–C06, the acceptance criterion MUST define the required artifact/control, PASS evidence, FAIL condition, UNKNOWN condition, CONFLICT condition, blocking semantics, and dependency on prior contracts where applicable.

No aggregate criterion may substitute for the one-to-one identity unless the matrix explicitly preserves the individual acceptance semantics.

## 5. Acceptance semantics

`PASS` = exact criterion demonstrated by direct evidence.  
`FAIL` = tested requirement did not hold.  
`UNKNOWN` = required property cannot be established.  
`CONFLICT` = authoritative/evidentiary inputs materially disagree.

For C01–C06 and F21, `FAIL`, `UNKNOWN`, and `CONFLICT` are blocking states. Documentation existence alone is not PASS.

## 6. KCAH-011 correction

The prior broad KCAH-011 criterion is decomposed into three independently testable properties:

- exact package-byte identity;
- declared source-state identity;
- reproducible package generation.

A package may not pass one property by virtue of passing another.

## 7. Historical scope discrepancy

The historical audit request remains preserved as historical evidence. It does not govern this correction audit. The current correction audit prompt and handoff MUST explicitly identify the correction contract and its exact baseline. Historical requests with different scope or source identity MUST be marked non-governing and, where applicable, SUPERSEDED.

## 8. Non-bypassability requirement

The continuation control MUST consume one machine-checkable integrity decision. Manual assertions, stale cached PASS values, undocumented alternate entry points, direct write surfaces, or agent/IDE-specific bypasses MUST NOT be capable of authorizing governed continuation.

Where implementation is not yet present, the property is `NOT_IMPLEMENTED / UNKNOWN`; it must not be represented as operational PASS.

## 9. Non-actions

This correction iteration does NOT:

- modify the existing checkpoint verifier;
- modify verifier tests;
- implement C01–C06;
- close the two P1 findings;
- declare KCA READY;
- declare ELS READY;
- authorize autonomous continuation;
- install external tools;
- promote this correction to canonical authority.

## 10. Required sequence

`CORRECTION CONTRACT → SELF-AUDIT → INDEPENDENT L2 AUDIT → RECONCILIATION → HUMAN APPROVAL → IMPLEMENTATION`

Implementation remains prohibited until the correction has passed the independent L2 gate and received explicit human approval.

## 11. Decision

**PROPOSED / REQUIRES HUMAN APPROVAL.**
