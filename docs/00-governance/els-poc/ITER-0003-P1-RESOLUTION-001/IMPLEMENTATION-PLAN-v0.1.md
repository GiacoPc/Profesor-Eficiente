# ITER-0003-P1-RESOLUTION-001 — Controlled Implementation Plan v0.1

**Status:** APPROVED-DIRECTION / EXECUTION GATE OPEN
**Risk:** L2
**Governing specification:** `P1-RESOLUTION-CONTRACT-v0.2.md`
**Machine-readable acceptance:** `ACCEPTANCE-MATRIX-v0.2.yaml`
**Human approval:** ELS-DEC-002, 2026-09-09
**Implementation authorization:** This plan authorizes execution of the approved implementation sequence only; it does not close any P1 finding or authorize ELS operational/autonomous readiness.

## Objective

Resolve P1-001 through P1-005 under the approved v0.2 contract using evidence-first, independently auditable implementation increments.

## Mandatory sequence

1. P1-001: formalize evidence schema and partial-write decision table.
2. P1-002: define/implement adversarial matrix and same-path tests.
3. P1-005: implement immutable checkpoint content/provenance binding.
4. P1-004: implement the deny-by-default continuation gate around the verified properties.
5. P1-003: integrate exact-head CI evidence.
6. Execute full regression and negative suites.
7. Capture exact evidence.
8. Self-audit.
9. Independent L2 audit.
10. Reconcile and seek human closure.

## Protected constraints

- ELS-CHECKPOINT v0.2 semantics remain unchanged.
- `tools/els/checkpoint_integrity_verifier.py` is modified only through implementation work explicitly governed by this approved contract.
- No P1 is closed by model assertion, test count, or implementation presence alone.
- `UNKNOWN`, `CONFLICT`, and `FAIL` remain blocking.
- `CONTINUE_AUTHORIZED` remains inadmissible until all five P1 closure gates are satisfied.
- No autonomous continuation is authorized by this plan.
- Exact repository identity and exact engineering HEAD must be captured for every evidence-bearing increment.

## Current execution increment

**Increment:** P1-001-IMPLEMENTATION-001

**Authorized work:** formalize the machine-readable evidence schema and explicit partial-write decision table required by P1-001-A and P1-001-C.

**Not yet authorized in this increment:** verifier behavior changes for P1-005/P1-004, closure claims, continuation authorization, or ELS readiness claims.

## Evidence gate

Every increment must produce:

- exact branch/ref;
- exact engineering HEAD;
- changed artifact identities;
- executable tests/oracles where applicable;
- observed outputs;
- evidence artifact identifiers;
- self-audit status;
- explicit remaining UNKNOWN/CONFLICT items.

A passing implementation test does not by itself close the corresponding P1 criterion.
