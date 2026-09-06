# AI BOOTSTRAP PACK — PROFESOR EFICIENTE

**Version:** 0.2-recovery
**Status:** RECOVERY ARTIFACT / NOT APPROVED
**Purpose:** allow a future AI/IDE session to resume without relying on conversation memory.

## Mandatory bootstrap

1. Read `docs/00-governance/PRCP.md`.
2. Read `docs/00-governance/RECOVERY-MANIFEST.yaml`.
3. Read `docs/00-governance/FORENSIC-RECOVERY-REPORT.md`.
4. Read `PROJECT-STATE.yaml` and `PROJECT-CONSTITUTION.md`.
5. Read `docs/ARCHITECTURE-BIBLE.md`.
6. Load only task-relevant specifications and evidence.

## Authority model

`Curriculum / governed policies → CLM / FDM → accepted Evidence → Assessment → MasteryPolicy → MasteryRecord → ProgressionEligibility → APE → PedagogicalDecision → controlled learner-facing action`

Bounded capability outputs follow:

`learner response/speech → processing → candidate → validation + provenance → FDM authoritative record`

LLM, STT, speech analysis, linguistic analysis, SDT and candidate artifacts are not independent authorities.

## Recovery integrity rules

- **NO EVIDENCE → NO CLAIM.**
- Never claim a file, branch, commit, tree, test or CI result was inspected without exact evidence.
- Never infer tree completeness from a commit message.
- Never treat conversation memory as Git state.
- Preserve `UNKNOWN`, `UNVERIFIED`, and `CONFLICT`.
- Never promote recovered material to `APPROVED` without the required evidence and human/secondary review.
- Do not modify the forensic preservation ref.
- Do not authorize implementation while recovery is open.

## Verified recovery baseline

The historical commit `09baedf0e9622f922969c7bb05e8696b850377a7` contains the broad architecture/governance tree that was subsequently destroyed from the working branch by later isolated-tree commits. Its recursive tree was directly inspected and contains the principal PAD, CLM, SDT, APE, FDM and P1 architecture artifacts.

Three expected artifacts were explicitly checked at that commit and were **not found**: `docs/01-product/PRD.md`, `docs/07-ai/RAG.md`, `docs/07-ai/LLM-ARCHITECTURE.md`, and `schemas/project-state.schema.json`. They remain `UNKNOWN/MISSING_FROM_VERIFIED_BASELINE`, not reconstructed.

## Operating procedure

For every future task: fetch exact ref/HEAD → inspect governing artifacts → record evidence → work on a separate branch → commit → re-fetch exact HEAD → verify tree/blob identities → run applicable checks → secondary audit for P0/P1 → human approval.

**Current status: RECOVERY IN PROGRESS — NO IMPLEMENTATION AUTHORIZATION.**
