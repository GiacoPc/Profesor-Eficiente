# ITER-0003 — Secondary Contract Audit Pack v0.1

**Status:** AUDIT HANDOFF PREPARED / REVIEW PENDING
**Risk:** L2
**Target:** `P1-RESOLUTION-CONTRACT-v0.1.md` + `ACCEPTANCE-MATRIX.yaml`
**Implementation authorization:** NONE

## Purpose

Provide a self-contained handoff specification for a genuinely independent secondary auditor to red-team the P1 resolution contract before implementation is approved.

## Frozen review target

Review the exact files at the audit target commit/ref supplied with this pack. The auditor must report the exact SHA actually reviewed.

Primary contract:
`docs/00-governance/els-poc/ITER-0003-P1-RESOLUTION-001/P1-RESOLUTION-CONTRACT-v0.1.md`

Machine-readable matrix:
`docs/00-governance/els-poc/ITER-0003-P1-RESOLUTION-001/ACCEPTANCE-MATRIX.yaml`

## Required independence

The reviewer must be a different model/provider or a separately controlled execution context. Self-review by the authoring agent does not satisfy this gate.

The auditor is read-only for this gate and must not modify the repository, verifier, tests, contract, or acceptance matrix.

## Audit questions

1. Are P1-001 through P1-005 correctly scoped and non-overlapping?
2. Is the dependency graph logically sound, acyclic, and complete?
3. Are all closure criteria objectively testable?
4. Can any criterion be satisfied without establishing the intended property?
5. Are important adversarial cases or false-positive paths missing?
6. Does P1-004 correctly consume rather than replace the integrity properties of P1-001/P1-002/P1-003/P1-005?
7. Does P1-005 adequately address working-tree/Git-provenance TOCTOU without creating self-reference?
8. Are `UNKNOWN` and `CONFLICT` blocking semantics complete?
9. Are Markdown contract and YAML matrix mutually consistent?
10. Does the contract introduce any P0/P1 defect or unsafe implementation ambiguity?
11. Are any acceptance criteria too weak, circular, non-deterministic, or unverifiable?
12. Are there missing environment, Git topology, concurrency, or provenance assumptions?

## Required verdict

One of:

- `PASS`
- `PASS_WITH_LIMITATIONS`
- `FAIL`
- `UNKNOWN`
- `CONFLICT`

Any unresolved P0/P1 defect blocks implementation approval.

## Evidence discipline

- No evidence → no verified claim.
- If an artifact cannot be accessed, classify the relevant point `UNKNOWN`.
- Do not infer repository state from conversation history.
- Cite exact file paths and, where available, exact commit/object identity.
- Distinguish `OBSERVED`, `VERIFIED`, `INFERRED`, `UNKNOWN`, and `CONFLICT`.
- A passing test must be tied to the property it actually demonstrates.

## Required output

Return a complete audit report containing:

1. reviewed identity;
2. executive verdict;
3. criterion-by-criterion assessment;
4. dependency assessment;
5. contract-vs-matrix consistency assessment;
6. adversarial/false-positive analysis;
7. P0/P1/P2/P3 findings;
8. mandatory corrections before implementation;
9. evidence limitations;
10. explicit statement whether implementation may proceed.

Do not repair findings during the audit. Do not approve implementation implicitly. The audit is an evidence input to the later reconciliation and human decision.

## Current boundary

This pack prepares the independent review only. It does not constitute the independent audit itself and does not authorize implementation.
