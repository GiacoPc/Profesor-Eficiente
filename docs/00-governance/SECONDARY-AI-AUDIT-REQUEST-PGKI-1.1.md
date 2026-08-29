# Secondary AI Audit Request — PGKI-1.1

**Purpose:** Independent red-team audit before PGKI-1.1 human approval.
**Audited scope:** PGKI-1.1 governance hardening only.

## Instructions to the secondary auditor

You are an independent auditor. Do NOT assume the primary architect's conclusions are correct. Do NOT confirm the primary conclusion merely because it is plausible.

Review the immutable audit pack and applicable policy/specification. Attempt to falsify each critical claim. Distinguish observed defects from speculative concerns. If evidence is insufficient, return `UNKNOWN`; do not infer success.

## Mandatory review questions

1. Does PGKI-1.1 introduce any contradiction with PGKI-1.0?
2. Is the Claim → Evidence → Verification mechanism internally consistent?
3. Are the claim classification states unambiguous and used consistently?
4. Does the evidence policy actually prevent unsupported observations such as claiming to have seen an unavailable screenshot?
5. Is the bounded retrospective audit explicit about what it did and did not prove?
6. Is the secondary-auditor protocol sufficiently independent to reduce confirmation bias?
7. Is the high-impact gate matrix complete enough for P0/P1 decisions?
8. Does the CI enforce meaningful governance invariants, or merely the presence of text?
9. Are there any false-positive/false-negative risks in the governance checks?
10. Are there any unresolved blockers that must prevent PGKI-1.1 closure?

## Required verdict format

- Overall verdict: `PASS` | `PASS_WITH_LIMITATIONS` | `FAIL` | `UNKNOWN` | `CONFLICT`
- Claims reviewed: list claim IDs
- Evidence reviewed: list exact refs/files
- Findings: severity P0/P1/P2/P3
- Evidence gaps: explicit list
- Contradictions: explicit list
- Required remediations: explicit list
- Closure recommendation: `CLOSE` or `DO_NOT_CLOSE`

## Independence constraint

The auditor must not edit the audited branch or baseline. The human owner remains the final authority.

## Critical rule

A secondary AI verdict is evidence about the review process; it is not itself the source of truth. Deterministic evidence and human approval remain required.
