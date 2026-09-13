# KCA/ELS Integrity Hardening — Independent L2 Audit Prompt v0.1

**Audit scope:** KCA-ELS-INTEGRITY-HARDENING-001 contractual package only.
**Target ref:** `kca/els-integrity-hardening-001`
**Audit level:** L2 independent review.
**Authority:** Audit artifact only; cannot approve, modify, or promote the contract.

## Objective
Independently red-team the hardening contract, acceptance matrix, failure/threat model, and bounded self-audit for semantic correctness, traceability, blocking semantics, and hidden authorization/bypass risks.

## Required inputs
1. `INTEGRITY-HARDENING-CONTRACT-v0.1.md`
2. `ACCEPTANCE-MATRIX.yaml`
3. `FAILURE-THREAT-MODEL-v0.1.md`
4. `SELF-AUDIT-MARKDOWN-YAML-v0.1.md`
5. `INPUT.yaml`
6. `OBJECTIVE.md`
7. `PLAN.md`
8. `INCIDENT-F21-WRONG-TARGET-WRITE.md`

## Audit rules
- Do not infer unavailable repository/runtime evidence.
- Distinguish OBSERVED, VERIFIED, INFERRED, UNKNOWN, and CONFLICT.
- Do not treat the self-audit as authoritative.
- Do not modify repository artifacts.
- Do not approve implementation or readiness.
- A contradiction, unresolved ambiguity affecting safety, or missing required evidence must not be normalized to PASS.

## Mandatory checks

### A. Identity and scope
- Is the audit scope exactly bounded to this iteration?
- Is the target ref explicit?
- Are implementation, verifier modification, P1 closure, readiness, and autonomous continuation correctly prohibited?

### B. Markdown ↔ YAML semantic consistency
- Contract requirements map correctly to matrix criteria.
- No dependency/authority contradiction.
- Closure semantics are identical.
- Status and authorization semantics are identical.
- Non-actions are preserved.
- Criteria do not silently weaken contract requirements.

### C. F21 coverage
Determine whether the contract, matrix, threat model, incident record, and self-audit provide sufficient explicit traceability for wrong-target writes / branch-parameter omission.

### D. C01–C06 traceability
Determine whether the requirement for explicit C01–C06 contracts before implementation is adequately represented by the current acceptance structure, or whether a material traceability gap remains.

### E. Acceptance semantics
Verify that PASS/FAIL/UNKNOWN/CONFLICT semantics are unambiguous and that UNKNOWN/CONFLICT cannot be promoted through documentation-only assertions.

### F. Bypass analysis
Red-team for manual PASS assertions, alternate continuation paths, undocumented entry points, stale artifacts, source substitution, unsupported repository topology, and authority escalation.

### G. Self-audit quality
Determine whether `SELF-AUDIT-MARKDOWN-YAML-v0.1.md` correctly reports the comparison and whether any finding is understated, overstated, or missing.

## Required output
Return:
- Executive verdict: `PASS`, `PASS_WITH_LIMITATIONS`, `FAIL`, `UNKNOWN`, or `CONFLICT`.
- Findings ranked P0/P1/P2/P3.
- For each finding: evidence, affected artifact, exact semantic issue, impact, and recommended correction.
- Explicit determination for SA-001, SA-002, SA-003.
- Explicit determination whether an independent reviewer could safely authorize progression to correction-contract work.
- Explicit statement of unavailable evidence.

**Critical prohibition:** The audit must not authorize implementation. Human approval remains mandatory after reconciliation.
