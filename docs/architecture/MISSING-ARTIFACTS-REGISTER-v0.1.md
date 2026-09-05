# Missing Artifacts Register — Reconciliation Audit

**Version:** 0.1
**Status:** OBSERVED / ACTION REQUIRED
**Branch:** `architecture/pad-clm-fdm-ape-v1.0`

## Purpose

Prevent a repeat of the previous integrity failure in which documents were treated as existing without direct evidence. This register records repository paths that were directly checked and not found during the PAD/CLM/FDM/APE/LPH reconciliation.

## Observed missing artifacts

| Path checked | Result | Impact |
|---|---|---|
| `docs/01-product/PRD.md` | NOT FOUND | Product requirements are not formalized at this path. Baseline artifacts remain the available authority. |
| `docs/03-cognitive/SDT.md` | NOT FOUND | CLM references SDT, but no standalone formal SDT contract is available. BLOCKER for CLM v1.0. |
| `docs/00-governance/PGKI.md` | NOT FOUND | Governance references PGKI concepts, but the expected standalone artifact is absent. BLOCKER for complete governance traceability. |
| `schemas/project-state.schema.json` | NOT FOUND | Project State schema validation cannot be verified from this path. |
| `schemas/context-manifest.schema.json` | NOT FOUND | Context Manifest schema validation cannot be verified from this path. |
| `tools/validate_governance.py` | NOT FOUND | The expected governance validator is absent at this path. Current CI status must not be inferred from historical runs. |
| `docs/07-ai/RAG.md` | NOT FOUND | RAG contract is referenced conceptually but not available as a formal artifact at this path. |
| `docs/07-ai/LLM-ARCHITECTURE.md` | NOT FOUND | LLM architecture is referenced conceptually but not available as a formal artifact at this path. |

## Existing artifacts directly verified on this branch

- `PROJECT-CONSTITUTION.md`
- `AI-GOVERNANCE.md`
- `PROJECT-STATE.yaml`
- `DECISION-LEDGER.yaml`
- `CONTEXT-MANIFEST.yaml`
- `docs/ARCHITECTURE-BIBLE.md`
- `docs/00-governance/BASELINE-RECONCILIATION-v1.0.md`
- `docs/00-governance/CHANGE-CLASSIFICATION.md`
- `docs/00-governance/REPOSITORY-POLICY.md`
- `docs/00-governance/ADR-POLICY.md`
- `docs/00-governance/PGKI-1.0-SECOND-AUDIT.md`
- `docs/00-governance/TRACEABILITY.md`
- `docs/02-pedagogy/PAD.md`
- `docs/03-cognitive/CLM.md`
- `docs/04-ape/APE.md`
- `docs/05-domain/FDM.md`
- `docs/architecture/LINGUISTIC-PEDAGOGICAL-HARNESS-SPEC.md`

## Integrity rule

A path is considered **verified present** only after a repository read returns the file content. A historical reference to a path is not evidence that the file currently exists.

A missing path is not evidence that the artifact never existed elsewhere. This register is scoped to the inspected branch/ref.

## Required actions

1. Recover or formally create the missing artifacts where they are actual project requirements.
2. Update the Context Manifest only with paths that really exist.
3. Re-run governance validation from the current HEAD; do not rely on historical CI runs.
4. Reconcile SDT formally before CLM v1.0 approval.
5. Formalize PRD before claiming complete requirements traceability.
6. Formalize RAG and LLM architecture before their contracts are consumed by SRA.
7. Restore/replace the governance validator and schemas, or explicitly document their new canonical paths.

**Current gate: BLOCKED / NOT READY FOR APPROVAL.**
