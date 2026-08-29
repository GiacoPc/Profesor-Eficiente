# Secondary AI Auditor Protocol v1.0

**Status:** PROPOSED — PENDING GOVERNANCE APPROVAL
**Scope:** High-impact architecture, security, performance, hardware/runtime, pedagogical, and release gates.

## Objective
Provide an independent semantic review layer that attempts to detect unsupported claims, contradictions, missing evidence, and design weaknesses without becoming a second source of truth.

## Independence requirements

1. The secondary auditor MUST receive the defined audit pack, not the primary agent's conclusion as authoritative context.
2. The audit pack MUST identify the immutable evidence set and applicable policy/specification.
3. The secondary auditor MUST be read-only against the audited baseline.
4. The secondary auditor MUST produce an independent verdict.
5. The secondary auditor MUST identify evidence gaps explicitly.
6. A disagreement MUST be recorded as `EVIDENCE CONFLICT` or `ARCHITECTURAL CONFLICT` as applicable.
7. The human remains the final decision authority.

## Audit pack

Minimum contents:

- claim(s) under review;
- immutable commit/ref;
- relevant specification(s);
- applicable ADR(s);
- evidence references;
- deterministic test/CI results;
- audit scope and exclusions.

## Verdicts

- `PASS` — evidence supports the claim within scope.
- `PASS_WITH_LIMITATIONS` — supported, but explicit limitations remain.
- `FAIL` — evidence contradicts or materially undermines the claim.
- `UNKNOWN` — insufficient evidence.
- `CONFLICT` — authoritative evidence or auditor conclusions disagree.

## Anti-collusion rule

The secondary auditor MUST NOT be instructed to "confirm" the primary conclusion. Its task is to independently test the claim, including attempts to falsify it.

## Red-team mode

For P0/P1 decisions, the secondary auditor SHOULD operate in red-team mode:

> Find the strongest technically defensible reason this claim, design, or decision could be wrong.

It must distinguish discovered defects from speculative concerns.

## Deterministic boundary

The secondary auditor cannot replace deterministic validation. Compilation, unit tests, schema validation, cryptographic hashes, benchmark measurements, repository state, and CI remain machine-verifiable evidence where applicable.

## Gate rule

`PRIMARY + SECONDARY + DETERMINISTIC EVIDENCE -> HUMAN DECISION`

No single AI verdict can close a critical gate by itself.
