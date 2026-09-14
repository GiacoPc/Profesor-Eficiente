# Repository-first / File-upload-last v0.1

**Status:** PROPOSED / REQUIRES HUMAN APPROVAL  
**Scope:** Evidence and context acquisition  
**Authority:** Subordinate to PGKI, KCA, and ELS

## 1. Policy

When a required project artifact already exists in the canonical repository and can be retrieved reliably, retrieve it from the repository rather than asking the user to upload another copy.

User file upload is the fallback when repository retrieval is unavailable, the artifact exists only locally, the user explicitly provides a new external artifact, or binary/local tooling requires the upload.

## 2. Acquisition order

Use this order unless the task explicitly requires otherwise:

1. Current canonical repository state.
2. Specific canonical artifact by path/ref.
3. Specific commit/blob/evidence referenced by the active contract.
4. Independent evidence source when required by the methodology.
5. User-provided file upload.
6. Historical/conversational context only when canonical sources are insufficient.

## 3. Upload avoidance

Do not request or create an upload merely to:
- repeat a document already available in Git;
- transfer the whole repository when only one or two files are required;
- preserve conversational continuity;
- compensate for failure to resolve the correct repository path;
- avoid a targeted repository read.

## 4. When upload is preferred

Upload remains appropriate when:
- the artifact is not in the repository;
- the user is supplying a new authoritative external source for the current task;
- the source is binary and repository tooling cannot provide the required content;
- exact local file bytes are themselves the subject of verification;
- repository access is unavailable or unreliable and the task cannot safely wait.

## 5. Freshness and identity

A repository read must specify the relevant ref when the task depends on a particular branch or state. A file obtained from an unspecified/default ref must not be silently treated as evidence for another ref.

When a user-uploaded file and repository artifact appear to represent the same logical document, identity/version/hash must be reconciled before treating them as interchangeable.

## 6. Evidence discipline

Repository-first is not repository-only. Independent audit evidence, external standards, user-provided originals, or runtime evidence may still be mandatory.

No acquisition strategy can upgrade:
`UNKNOWN → VERIFIED`, `INFERENCE → FACT`, or `PROPOSAL → DECISION`.

## 7. Quota-efficiency objective

This policy is intended to reduce unnecessary file-upload and re-ingestion pressure on constrained client plans. It does not claim to change, bypass, or extend any provider quota.

## 8. Operational status

This policy is proposed. Automatic enforcement, quota measurement, and complete tool coverage remain implementation questions requiring separate verification.
