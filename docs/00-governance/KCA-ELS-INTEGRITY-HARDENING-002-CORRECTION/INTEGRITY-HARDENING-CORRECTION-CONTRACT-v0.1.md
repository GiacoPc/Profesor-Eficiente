# KCA/ELS Integrity Hardening — Correction Contract v0.1

ID: KCA-ELS-INTEGRITY-HARDENING-002-CORRECTION
Parent: KCA-ELS-INTEGRITY-HARDENING-001
Status: PROPOSED / REQUIRES HUMAN APPROVAL
Risk: L2
Implementation: NOT AUTHORIZED
P1 closure: NOT AUTHORIZED
KCA/ELS readiness: NOT AUTHORIZED

## Accepted findings
P1-F21 and P1-C01-C06 are accepted as valid blockers, not documentation-only defects.

## F21 first-class normative control
Every governed repository write MUST follow:
TARGET REF DECLARED → TARGET REF RESOLVED → TARGET HEAD VERIFIED → WRITE WITH EXPLICIT TARGET → RE-FETCH TARGET → VERIFY RESULT

The target branch/ref MUST be explicit. Omitted or implicit target is a hard failure. The control applies to direct contents writes, Git data operations, automation, agents, IDE integrations, scripts, and future adapters.

## C01–C06 traceability
C01 Canonical Artifact Identity
C02 Context Resolution / Bootstrap
C03 Audit-Pack Manifest
C04 Prompt/Evidence Compatibility
C05 Integrity Validator
C06 Continuation Gate Integration

Each MUST have a one-to-one acceptance criterion defining requirement, PASS evidence, FAIL, UNKNOWN, CONFLICT, blocking semantics, and dependencies.

## KCAH-011
Decompose into:
A exact package-byte identity;
B declared source-state identity;
C reproducible package generation.

## Blocking
For C01–C06 and F21, FAIL/UNKNOWN/CONFLICT block approval.

## Non-bypassability
Continuation MUST consume one machine-checkable current integrity decision. Manual assertions, stale cached PASS, undocumented alternate entry points, direct write surfaces, and agent/IDE-specific bypasses MUST NOT authorize governed continuation.

## Non-actions
No verifier modification, no implementation, no P1 closure, no KCA/ELS readiness, no autonomy.

Decision: PROPOSED / REQUIRES HUMAN APPROVAL.
