# KCA-ELS Context Economy — Resolver Correction Contract v0.1

Status: PROPOSED / IMPLEMENTATION AUTHORIZED ON ISOLATED BRANCH ONLY

## Objective
Correct the resolver so that it cannot emit an apparently valid governed context package when required source identity, dependencies, blockers, or continuation prerequisites are unresolved.

## Mandatory controls

1. Resolve and verify repository, target ref, HEAD, and tree before reading authoritative inputs.
2. Treat missing, unreadable, malformed, or identity-mismatched required sources as `UNKNOWN` or `CONFLICT`.
3. Compute blockers from validation results; never initialize a successful package with an unconditional empty blocker list.
4. Distinguish `OBSERVED`, `VERIFIED`, `INFERRED`, `UNKNOWN`, `NOT_AVAILABLE`, and `CONFLICT`.
5. Emit a governed continuation package only when all required prerequisites pass.
6. Preserve source path, source identity, and status/evidence classification for every authoritative input.
7. Add adversarial tests for missing core files, malformed metadata, conflicting source state, and unresolved write target identity.
8. No write operation may use an implicit target branch.

## Blocking semantics

`FAIL`, `UNKNOWN`, and `CONFLICT` are blocking states for governed continuation. The resolver may emit a diagnostic package describing the block, but must not emit an authorized next action.

## Non-goals

This iteration does not promote the Context Economy contract, close CEC criteria, claim token savings, or replace independent L2 validation.
