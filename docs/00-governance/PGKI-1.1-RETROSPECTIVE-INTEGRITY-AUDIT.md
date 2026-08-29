# PGKI-1.1 — Retrospective Integrity Audit

**Status:** IN PROGRESS — DOES NOT MODIFY PGKI-1.0
**Audit target:** PGKI-1.0 baseline construction and pre-merge governance workflow
**Trigger:** Evidence Integrity Incident

## 1. Objective

Determine whether the existing governed repository contains additional evidence-integrity defects and define the limits of what can and cannot be concluded about prior AI interactions.

## 2. Important limitation

This audit cannot prove that no unsupported statement ever occurred in the entire historical conversation unless the complete conversation transcript and all referenced evidence are available for deterministic review. A clean repository is not proof that every prior conversational claim was correct.

Therefore the audit reports **findings and coverage**, not absolute absence of failure.

## 3. Evidence surface currently inspected

The following PGKI-1.0 artifacts were directly inspected on branch `baseline/pgki-1.0`:

- `AI-GOVERNANCE.md`
- `AGENTS.md`
- `PROJECT-CONSTITUTION.md`
- `PROJECT-STATE.yaml`
- `CONTEXT-MANIFEST.yaml`
- `DECISION-LEDGER.yaml`
- `docs/ARCHITECTURE-BIBLE.md`
- `docs/00-governance/BASELINE-RECONCILIATION-v1.0.md`
- `docs/00-governance/TRACEABILITY.md`
- `docs/00-governance/REPOSITORY-POLICY.md`
- `docs/00-governance/PGKI-1.0-SECOND-AUDIT.md`
- `.github/workflows/governance.yml`
- PR #1 metadata and changed-file inventory.

## 4. Preliminary findings

### F-001 — Unsupported visual-observation claim

**Severity:** P0
**Status:** CONFIRMED INCIDENT

An agent claimed to have reviewed a screenshot before that screenshot was available in the relevant turn. The claim was not supported by accessible evidence at the time it was made.

**Root control weakness:** existing governance rules prohibited unverified claims but did not define an explicit evidence-availability gate or a machine-checkable claim classification protocol.

**Remediation:** PGKI-1.1 Evidence & Claim Integrity policy.

### F-002 — Existing repository governance already contains relevant safeguards

**Severity:** Informational
**Status:** VERIFIED

PGKI-1.0 already states that repository artifacts/evidence outrank conversation memory, missing information remains `UNKNOWN`, tests and repository state must not be claimed without verification, and minimum-sufficient task context is required.

**Conclusion:** the incident represents an enforcement/process gap, not evidence that the entire PGKI-1.0 governance model was absent.

### F-003 — Historical conversational absence cannot be established

**Severity:** P0 methodological limitation
**Status:** OPEN

The repository does not contain a complete, immutable ledger of every conversational claim made during project development. Therefore it is impossible to prove from the repository alone that no other unsupported claim occurred in prior conversations.

**Remediation:** establish claim/evidence records for future critical gates and perform a bounded retrospective audit whenever an integrity incident occurs.

### F-004 — GitHub platform protection exception is explicitly recorded

**Severity:** Controlled risk
**Status:** VERIFIED

The baseline explicitly records that `main` protection is blocked by the current GitHub plan and defines compensating controls. The project must not claim that `main` is protected until enforcement is enabled and independently verified.

## 5. Required future audit protocol

For every high-impact gate:

1. Freeze the relevant commit/ref.
2. Enumerate critical claims.
3. Attach evidence references to each claim.
4. Independently verify the evidence.
5. Run deterministic CI/tests.
6. Perform secondary-agent review where risk warrants it.
7. Record unresolved `UNKNOWN`/`NOT_AVAILABLE` states.
8. Obtain human approval.
9. Record the resulting commit/tag as the immutable gate anchor.

## 6. Secondary auditor policy

A second AI may be used as an **independent auditor**, but only under these constraints:

- it must receive the evidence set, not merely the primary agent's narrative;
- it must independently inspect the relevant artifacts;
- it must not edit the audited baseline;
- it must produce a separate verdict and findings;
- disagreement must become `EVIDENCE CONFLICT`, not an averaged answer;
- the human remains the final authority.

The secondary AI is an additional control, not a substitute for deterministic tests, CI, source control, or human approval.

## 7. Audit confidence statement

Current conclusion: **PGKI-1.0 repository governance shows no additional integrity defect in the inspected artifacts beyond the confirmed incident and documented platform exception. This is not a proof that no other conversational integrity failures ever occurred.**

Coverage must be expanded through a bounded historical claim audit before the project treats the incident as fully closed.
