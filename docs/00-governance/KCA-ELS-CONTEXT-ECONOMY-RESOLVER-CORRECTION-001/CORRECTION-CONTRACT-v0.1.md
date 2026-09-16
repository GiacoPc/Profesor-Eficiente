# KCA-ELS Context Economy — Resolver Correction Contract v0.1

Status: PROPOSED — IMPLEMENTATION AUTHORIZED ON ISOLATED CORRECTION BRANCH ONLY

## Objective
Correct the resolver so it cannot emit an apparently valid governed context package when source identity, dependencies, blockers, or continuation conditions are unresolved.

## Scope
- Resolver source validation
- Repository identity verification
- Required-field validation
- Dependency and blocker handling
- Fail-closed continuation decision
- F21 target-verification test contract
- Adversarial test cases

## Normative requirements

### R1 — Explicit source-state identity
The resolver MUST verify repository identity, target ref, HEAD, and tree before using repository artifacts as authoritative input.

### R2 — Required-source integrity
Missing, unreadable, or unverifiable required sources MUST produce `UNKNOWN` or `FAIL`; the resolver MUST NOT silently continue.

### R3 — Dependency resolution
The resolver MUST distinguish selected artifacts from unresolved dependencies. Unresolved dependencies MUST be represented as blockers.

### R4 — Blocker derivation
The `blockers` field MUST be derived from actual validation results. It MUST NOT be hard-coded to an empty list.

### R5 — Fail-closed gate
Any `FAIL`, `UNKNOWN`, or `CONFLICT` affecting a governed task MUST result in a non-authorized continuation state.

### R6 — Provenance preservation
Every authoritative source retained in a package MUST include stable path and content identity. The package MUST distinguish observed facts from unresolved or inferred information.

### R7 — F21 write safety
This correction MUST NOT perform repository writes implicitly. Any future governed write requires: target declared, target resolved, target HEAD verified, explicit branch/ref supplied, target re-fetched, and result verified.

## Acceptance evidence required
- Unit tests for missing core source, missing dependency, conflicting identity, and malformed source metadata.
- Adversarial test proving `blockers` cannot remain empty when a required dependency is absent.
- Adversarial test proving unresolved target identity blocks continuation.
- Exact target-branch and post-write verification record for every repository mutation.

## Exit conditions
This contract is not closed by implementation alone. Closure requires test evidence, self-audit, independent validation, reconciliation, and explicit human approval for governance promotion.
