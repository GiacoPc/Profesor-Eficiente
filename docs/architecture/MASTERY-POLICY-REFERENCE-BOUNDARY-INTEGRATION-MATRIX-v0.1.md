# Mastery Policy Reference Boundary — Integration Matrix v0.1

**Document ID:** C009-MASTERY-POLICY-REFERENCE-BOUNDARY
**Version:** 0.1-draft
**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** Cross-document integration of P1 C-009

## 1. Normative rule

`MasteryPolicy` is the governed source of authoritative mastery requirements. Runtime consumers reference the applicable policy by stable identity and version; they do not redefine, shadow, infer, or locally override authoritative requirements.

The canonical reference is:

```yaml
mastery_policy:
  id: <mastery_policy_id>
  version: <mastery_policy_version>
```

Where applicable, consumers may additionally receive governed references to required evidence types, criteria, or policy constraints. Such references identify policy-defined requirements; they are not permission to recreate the policy locally.

## 2. Authority chain

```text
Governed MasteryPolicy
        ↓
Evidence + Assessment
        ↓
Mastery evaluation
        ↓
MasteryRecord / learning state
        ↓
ProgressionEligibility
        ↓
APE pedagogical action
```

The chain prevents APE, LPH, LLM, SDT, UI, or conversational preference from becoming an accidental second mastery-policy authority.

## 3. Consumer responsibility matrix

| Component | May reference policy | May interpret/use policy | May define/override policy | May persist authoritative policy definition |
|---|---:|---:|---:|---:|
| Curriculum | Yes | Within governed curriculum contract | No | Yes, as governed curriculum/policy data where applicable |
| MasteryPolicy authority | N/A | Yes | Yes, through governed approval/change process | Yes |
| FDM | Yes | Enforce domain contract | No | Enforce authoritative mutation/provenance |
| CLM | Yes | Interpret learning state under policy | No | Preserve policy provenance on authoritative state |
| SDT | Yes | Represent resulting state/provenance | No | No independent policy definition |
| APE | Yes | Use policy result/reference for decisions | No | No |
| LPH | Yes | Apply bounded linguistic constraints derived from policy | No | No |
| LLM | Via bounded context only | Candidate interpretation/generation only | No | No |
| UI/learner dialogue | Yes, when exposed through governed presentation | No authoritative interpretation | No | No |

## 4. Reference contract

A consumer-facing contract should distinguish:

```yaml
policy_reference:
  mastery_policy_id: <stable-id>
  mastery_policy_version: <version>
```

from an authoritative policy definition such as:

```yaml
policy_definition:
  thresholds: <governed-value>
  required_evidence: <governed-value>
  aggregation: <governed-value>
  stability: <governed-value>
  transfer: <governed-value>
```

Only the governed policy authority owns the latter. Consumers must not synthesize it from partial fields.

## 5. Forbidden patterns

The following are prohibited:

1. APE receives `mastery_threshold: 0.8` and treats it as authoritative without a policy reference.
2. LPH receives a policy reference and converts it into a different local threshold.
3. LLM is prompted to decide what score constitutes mastery.
4. SDT stores an inferred threshold as if it were the policy.
5. UI/user preference overrides a mandatory policy requirement.
6. A consumer silently falls back to a hard-coded threshold when the policy is unavailable.
7. A stale policy version is treated as current without governed compatibility resolution.
8. Two policy versions are silently merged into a new implicit policy.

## 6. Missing/invalid policy behavior

If the applicable policy is:

- `UNDEFINED`;
- unavailable;
- stale beyond an allowed compatibility rule;
- malformed;
- conflicting;
- outside its declared competency/curriculum scope;

the system must enter a controlled policy-resolution/insufficient-evidence/conflict path as appropriate. It must not invent a replacement threshold or requirement.

## 7. Version and reproducibility rule

Every authoritative mastery evaluation must retain the exact `mastery_policy_id` and `mastery_policy_version` used for that evaluation.

Historical evaluation must remain explainable if the current policy later changes, is deprecated, or is superseded.

A policy update creates a new governed version; it does not silently rewrite historical mastery decisions.

## 8. Boundary tests

### C009-T01 — Explicit reference required

A mastery evaluation without an applicable policy identity/version is rejected or placed in controlled `POLICY_UNDEFINED` handling.

### C009-T02 — No ad-hoc threshold

An APE request containing an authoritative threshold without a policy reference is rejected.

### C009-T03 — LPH cannot override

A linguistic task may consume policy-derived constraints but cannot change their authoritative value.

### C009-T04 — LLM cannot define mastery

An LLM response declaring mastery or proposing a threshold cannot mutate mastery state.

### C009-T05 — Historical provenance

A stored authoritative mastery result remains linked to the exact policy identity/version used at evaluation time.

### C009-T06 — Version mismatch

A stale/incompatible policy reference cannot silently be treated as the current policy.

### C009-T07 — Scope mismatch

A policy outside the competency/curriculum scope cannot be applied merely because it exists.

### C009-T08 — Deterministic replay

Given identical evidence, assessment inputs, policy identity/version, and deterministic domain inputs, mastery evaluation must reproduce the same governed result.

### C009-T09 — Consumer isolation

Replacing APE, LPH, SDT, or LLM implementation cannot change the authoritative meaning of an approved policy.

### C009-T10 — No hidden fallback

When policy resolution fails, no hard-coded or LLM-generated threshold may become an implicit substitute.

## 9. Integration gate

C-009 is not considered fully resolved until:

- PAD/CLM/FDM/APE/LPH reference the same boundary;
- policy reference and policy definition are distinguishable in contracts;
- source specifications contain normative references to this boundary;
- executable checks cover identity, version, scope, stale/conflict behavior and no-fallback behavior;
- independent secondary AI audit covers this P1 boundary;
- human approval is recorded.

**Current status:** CONTRACT LEVEL RESOLUTION + SOURCE-SPEC INTEGRATION IN PROGRESS; NOT APPROVED.
