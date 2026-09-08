# ITER-0003-P1-RESOLUTION-001 — Plan

**Status:** PLANNING ONLY
**Risk:** L2
**Implementation:** NOT STARTED

## Phase 0 — Evidence freeze

- Verify branch and exact HEAD.
- Re-read the approved reconciliation and decision ledger entry.
- Preserve Grok audit and prior POC evidence unchanged.

## Phase 1 — Contract/specification

Produce an implementation contract covering P1-001..P1-005 with explicit acceptance criteria, failure semantics, provenance rules, and authority boundaries.

P1-001: define the evidence boundary between process-level simulation and real failure recovery.

P1-002: define adversarial verifier cases and expected PASS/CONFLICT/UNKNOWN behavior.

P1-003: define exact-head CI evidence requirements for the final checkpoint state.

P1-004: define the non-bypassable continuation gate and distinguish regression-suite PASS from current-checkpoint verification PASS.

P1-005: define an immutable checkpoint-content/provenance binding that cannot validate working-tree content against a different Git artifact.

## Phase 2 — Independent review of contract

Because this is L2 governance/integrity work, obtain independent secondary review of the contract before implementation where required by PGKI/ELS policy.

## Phase 3 — Implementation

Only after Phase 1 approval and required review. Changes must remain isolated to the authorized scope.

## Phase 4 — Verification

Run adversarial regression tests, exact-head CI, self-audit, and evidence capture.

## Phase 5 — Secondary audit and reconciliation

Submit an updated audit pack to an independent auditor. Reconcile every finding against exact repository evidence. Do not close P1 findings by assertion.

## Phase 6 — Promotion decision

Human authority decides whether each P1 may be closed. ELS operational readiness remains blocked until all mandatory gates are satisfied.

## Explicit non-action

Do not modify `tools/els/checkpoint_integrity_verifier.py` during this planning phase.
