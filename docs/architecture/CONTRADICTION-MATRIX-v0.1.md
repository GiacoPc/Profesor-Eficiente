# Contradiction Matrix — PAD / CLM / FDM / APE / LPH

**Version:** 0.8
**Status:** PROPOSED / REQUIRES INTEGRATION + INDEPENDENT AUDIT
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`
**Scope:** Cross-document reconciliation before LPH v1.0 and SRA.

## 1. P1 findings and resolution status

| ID | Severity | Finding | Resolution artifact | Status |
|---|---|---|---|---|
| C-001 | P1 | LPH authority could be interpreted above APE/FDM/CLM. | P1 Contract 1; PAD authority hierarchy | INTEGRATED + VERIFIED |
| C-002 | P1 | Competency/Objectives ownership/cardinality ambiguous. | P1 Contract 2; FDM/PAD | INTEGRATED + VERIFIED |
| C-003 | P1 | MasteryPolicy authority absent/implicit. | P1 Contract 3; MasteryPolicy contract | INTEGRATED + VERIFIED |
| C-004 | P1 | SDT authority/state boundary incomplete. | SDT + integration matrix | INTEGRATED AT CONTRACT LEVEL; SDT PROPOSED |
| C-005 | P1 | Error vs ErrorObservation lifecycle mismatch. | ErrorObservation lifecycle + matrix | INTEGRATED AT CONTRACT LEVEL; SOURCE-SPEC/EXECUTION PENDING |
| C-006 | P1 | Speech evidence → assessment → mastery/SDT sequencing incomplete. | Speech evidence/assessment contract + matrix | INTEGRATED AT CONTRACT LEVEL; SOURCE-SPEC/EXECUTION PENDING |
| C-007 | P1 | ProgressionEligibility vs APE PROGRESS boundary incomplete. | Progression Eligibility contract + matrix | RESOLVED AT CONTRACT LEVEL; SOURCE-SPEC/EXECUTION PENDING |
| C-008 | P1 | Mandatory progression/mastery gates vs APE discretion underspecified. | Progression Eligibility contract + matrix | RESOLVED AT CONTRACT LEVEL; SOURCE-SPEC/EXECUTION PENDING |
| C-009 | P1 | Mastery requirements could be redefined by consumers. | Policy reference boundary + matrix | SOURCE-SPEC BOUNDARY INTEGRATED; AUTOMATION/AUDIT PENDING |
| C-010 | P1 | LLMGenerationCandidate acceptance/persistence boundary incomplete. | Generation candidate lifecycle + matrix | INTEGRATED AT CONTRACT LEVEL; SOURCE-SPEC/EXECUTION PENDING |
| C-011 | P1 | LPH linguistic assessment vs FDM authoritative evidence/assessment ownership ambiguous. | Linguistic assessment ownership + matrix | SOURCE-SPEC BOUNDARY INTEGRATED; EXECUTION/AUDIT PENDING |

## 2. Cross-P1 reconciliation

The transversal reconciliation is recorded in `docs/architecture/CROSS-P1-RECONCILIATION-v0.1.md`.

Its contract-level conclusion is:

```text
Candidate / capability output
          ↓
validated provenance
          ↓
FDM authoritative Evidence / Assessment
          ↓
MasteryPolicy → MasteryRecord
          ↓
ProgressionEligibility
          ↓
APE → PedagogicalDecision
```

No candidate, LPH output, LLM output, SDT projection or pedagogical preference is an alternative authority path.

This is a conceptual/contract finding only; it is not executable proof.

## 3. Transversal gate

**CROSS-P1: PASS AT CONTRACT/CONCEPTUAL LEVEL — NOT READY FOR APPROVAL.**

Required before approval: source-spec direct normative integration, executable tests, schema compatibility checks, exact-head CI, independent secondary AI audit, and human approval.
