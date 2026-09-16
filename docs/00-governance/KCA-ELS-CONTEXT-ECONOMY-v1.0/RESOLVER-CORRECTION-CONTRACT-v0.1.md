# KCA-ELS Context Economy — Resolver Correction Contract v0.1

**Status:** PROPOSED — IMPLEMENTATION AUTHORIZED ON ISOLATED CORRECTION BRANCH

## Objective

Correct the resolver so that it cannot emit an apparently valid governed context package when source identity, dependencies, required fields, blockers, or target identity are unresolved.

## Scope

This contract applies only to `tools/kca_context_resolver.py` and directly related tests/evidence.

## Normative requirements

1. **Explicit repository identity:** the resolver MUST establish repository root, current ref, HEAD, and tree; ambiguity or failure MUST produce a blocking result.
2. **Required-source validation:** missing or unreadable required sources MUST be represented as `UNKNOWN` and MUST block governed continuation.
3. **Dependency-aware resolution:** C2 dependencies MUST be derived from declared governance dependencies or explicit resolver inputs; the resolver MUST NOT claim dependency completeness from filename scoring alone.
4. **Honest blockers:** `blockers` MUST be computed from actual validation results. It MUST NOT be hard-coded to an empty list.
5. **Fail-closed behavior:** `FAIL`, `UNKNOWN`, and `CONFLICT` conditions MUST prevent a package from being marked usable for governed continuation.
6. **Provenance:** every selected source MUST include repository-relative path, source-state identity, and content SHA-256.
7. **F21 enforcement boundary:** the resolver MUST never perform repository writes. Any future write adapter MUST require an explicit target ref and target-HEAD verification.
8. **Deterministic behavior:** identical source state, policy, objective, and resolver inputs MUST produce equivalent semantic output, excluding generation timestamps.
9. **Adversarial tests:** tests MUST cover missing sources, conflicting identity, absent dependencies, invalid limits, and attempted implicit-target writes at the adapter boundary.
10. **No authority elevation:** generated summaries or inferred relevance MUST NOT be emitted as authoritative facts.

## Required result states

The resolver MUST expose one of:

- `READY_FOR_REVIEW`
- `BLOCKED`
- `UNKNOWN`
- `CONFLICT`

A result in `BLOCKED`, `UNKNOWN`, or `CONFLICT` MUST NOT provide a positive continuation authorization.

## Acceptance evidence

The correction is not complete until tests and an auditable evidence record demonstrate each requirement above.

## Non-claims

This contract does not claim token savings, independent validation, governance promotion, or closure of the CEC criteria.
