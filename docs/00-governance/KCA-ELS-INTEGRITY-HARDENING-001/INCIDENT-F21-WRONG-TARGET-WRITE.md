# Incident F21 — Wrong-target write / branch parameter omission

**Iteration:** KCA-ELS-INTEGRITY-HARDENING-001
**Classification:** PROCESS / INTEGRITY INCIDENT
**Status:** RESOLVED AND ISOLATED
**Risk:** L2

## Incident

Draft hardening artifacts were accidentally written to `main` because write operations omitted the explicit target-branch parameter.

## Containment

1. The intended iteration branch is `kca/els-integrity-hardening-001`.
2. The branch was verified at its pre-incident base state before this containment record was created.
3. Accidental draft artifacts were removed from `main` through auditable deletion commits.
4. The remaining accidental `CHECKPOINT.yaml` on `main` was converted into a quarantine-only forensic record; it no longer asserts iteration authority or active checkpoint state.
5. No implementation, verifier modification, P1 closure, KCA readiness, ELS readiness, or autonomous continuation was authorized by the incident.

## Verified target-state identity

The isolated iteration branch was verified at:

- ref: `kca/els-integrity-hardening-001`
- state HEAD before this incident record: `f784961382121b42f3de2e0cd31caa7641d53498`
- tree: `76adbb55a9ad00f6a2dc1ae225645cf45637d1cf`

This record is the first new artifact intentionally written to that branch after containment.

## New mandatory control

Before every future repository write:

`TARGET REF DECLARED → TARGET REF RESOLVED → TARGET HEAD VERIFIED → WRITE WITH EXPLICIT BRANCH → RE-FETCH TARGET → VERIFY RESULT`

Omission of the branch parameter is a hard failure. No write may proceed when target identity is implicit.

## Non-actions

This incident record does not authorize reconstruction of the hardening draft, implementation, self-audit, P1 closure, or readiness promotion. Those actions remain subject to the existing approval gates.
