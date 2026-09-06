# AI BOOTSTRAP PACK — PROFESOR EFICIENTE

**Version:** 0.1-recovery
**Status:** RECOVERY ARTIFACT / NOT APPROVED
**Purpose:** allow any future AI/IDE session to resume work without relying on conversation memory.

## 1. Mandatory reading order

1. `docs/00-governance/PRCP.md`
2. `docs/00-governance/RECOVERY-MANIFEST.yaml`
3. `docs/architecture/ARCHITECTURE-BIBLE.md`
4. `docs/architecture/CROSS-P1-RECONCILIATION-v0.1.md`
5. Relevant contract/specification files only after their repository status is verified.

## 2. Project authority model

The intended authority chain is:

`Curriculum / governed policies → CLM / FDM → accepted Evidence → Assessment → MasteryPolicy → MasteryRecord → ProgressionEligibility → APE → PedagogicalDecision → controlled learner-facing action`

Bounded capability outputs follow:

`learner response/speech → processing → candidate artifact → validation + provenance → FDM authoritative record`

LLM, STT, speech analysis, linguistic analysis, SDT and candidate artifacts do not constitute independent authority.

## 3. Core architectural boundaries

- APE: pedagogical decision authority.
- FDM: domain truth and invariant enforcement boundary.
- SDT: learner-state representation/projection; non-authoritative.
- LPH: proposed linguistic/pedagogical constraint and validation boundary; not superior to APE/FDM.
- LLM: replaceable probabilistic capability; not curriculum, mastery, progression, or authoritative-state authority.
- MasteryPolicy: governed policy; consumers reference identity/version and do not redefine it.

## 4. Integrity rules

- NO EVIDENCE → NO CLAIM.
- Never state that a file, screenshot, test, CI run, branch, or commit was reviewed unless the exact evidence was inspected.
- Never infer tree completeness from a commit message.
- Never treat conversation memory as repository state.
- Preserve uncertainty as `UNKNOWN`, `UNVERIFIED`, or `CONFLICT` when appropriate.
- Do not promote recovered material to `APPROVED` without evidence and required review.
- Do not modify the forensic preservation ref.
- Do not authorize implementation while recovery is open.

## 5. Current known repository state

At recovery start, branch `architecture/pad-clm-fdm-ape-v1.0` pointed to commit `90f1a31dce45ae7e1a13d42fb5ff09dcd9a0fee4`. Recursive tree inspection showed exactly two blobs: `docs/architecture/ARCHITECTURE-BIBLE.md` and `docs/architecture/CROSS-P1-RECONCILIATION-v0.1.md`.

The branch was not protected at that observation.

A forensic branch was created at that exact SHA before recovery modifications. A separate recovery branch was then created for continuity work.

## 6. Architectural knowledge recoverable from project history

C-001 through C-011 were compositionally reconciled at contract level. The reconciliation explicitly states that it is not executable proof and not approval. Remaining risks include schemas/events, MasteryPolicy final semantics, executable uncertainty/conflict semantics, SDT concurrency, curriculum traceability, compatibility/invariant suites, exact-head CI, secondary audit, and performance/thermal validation.

## 7. Recovery operating procedure

For every future task:

1. Identify the exact task and governing artifact.
2. Fetch the exact branch/ref and HEAD.
3. Inspect only the required files plus their normative dependencies.
4. Record observed evidence before making claims.
5. Make changes on a non-protected working branch.
6. Commit with a descriptive message.
7. Re-fetch the resulting exact HEAD.
8. Verify recursive tree and changed blob SHAs for critical changes.
9. Run applicable automated checks.
10. Produce an audit pack for P0/P1 changes.
11. Request/perform independent secondary audit when mandatory.
12. Obtain human approval before promotion.

## 8. Explicit recovery status

**RECOVERY REQUIRED — ARCHITECTURAL KNOWLEDGE RECOVERABLE — GIT DOCUMENT STATE UNTRUSTED UNTIL RECONCILED.**

No implementation authorization is granted.
