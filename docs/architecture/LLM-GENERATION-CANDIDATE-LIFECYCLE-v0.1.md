# LLMGenerationCandidate Lifecycle / Acceptance Boundary — v0.1

**Document ID:** C-010-GENERATION-CANDIDATE
**Version:** 0.1-draft
**Status:** PROPOSED / REQUIRES APPROVAL
**Scope:** Lifecycle and authority boundary for probabilistic LLM-generated candidates.

## 0. Governance status

This document resolves C-010 at contract level. It does not approve a specific LLM, runtime, model, prompt format, persistence technology, or implementation.

The LLM is a replaceable probabilistic capability. `LLMGenerationCandidate` is explicitly non-authoritative.

## 1. Problem being resolved

A generated response may contain text that looks like a correction, linguistic assessment, learner diagnosis, evidence claim, mastery judgment, or pedagogical recommendation.

That appearance must never grant the generated content domain authority.

The system therefore separates:

```text
LLM generation
      ↓
LLMGenerationCandidate
      ↓
validation / acceptance
      ↓
controlled use
      ↓
(optional) separate evidence / assessment path
      ↓
authoritative domain state only through governed contracts
```

## 2. Canonical terminology

### 2.1 LLMRequest

A bounded request sent through the LLM capability boundary. It contains only the context, task, constraints and output contract required for the requested generation.

### 2.2 LLMGenerationCandidate

A non-authoritative output candidate produced by an LLM capability.

It may contain generated instructional language, examples, explanations, dialogue, reformulations, or structured candidate fields. It is not itself evidence, assessment, mastery, progression eligibility, or authoritative learner state.

### 2.3 CandidateValidationResult

A validation result describing whether a candidate satisfies the applicable structural, linguistic, pedagogical and governance constraints.

Validation success means only that the candidate is permitted for the specific bounded use. It does not promote the candidate into domain authority.

### 2.4 ControlledDelivery

Learner-facing use of an accepted candidate within the action and constraints established by APE/LPH/domain contracts.

### 2.5 Assessment / Evidence

Separate authoritative domain records created through the evidence/assessment contract when a generated candidate legitimately contributes to an assessment workflow. Such records must not reuse the candidate as if it were raw learner evidence.

## 3. Authority boundary

```text
Curriculum / CLM / FDM / SDT
              ↓
             APE
              ↓
             LPH
              ↓
        LLM Gateway
              ↓
   LLMGenerationCandidate
              ↓
      Candidate validation
         /          \
     REJECT          ACCEPTABLE
       ↓                  ↓
 discard/repair       controlled use
 regenerate               │
                           └──→ separate governed evidence/assessment path when applicable
```

No arrow from `LLMGenerationCandidate` directly to authoritative mastery, progression, SDT, CLM state, curriculum or FDM state is permitted.

## 4. Candidate lifecycle

Proposed states:

```text
REQUESTED
   ↓
GENERATED
   ↓
VALIDATING
   ├── REJECTED
   │      ↓
   │   TERMINAL
   │
   └── ACCEPTED_FOR_USE
          ↓
     CONTROLLED_DELIVERY
          ↓
     COMPLETED / SUPERSEDED
```

An accepted candidate may subsequently be found unsuitable for a later context. Historical state must not be rewritten merely to hide that outcome.

Repair/regeneration creates a new candidate with a new stable identity and provenance to the prior candidate where applicable.

## 5. Candidate identity and provenance

A persisted candidate should contain, conceptually:

```yaml
generation_id: <stable-id>
request_id: <stable-id>
learner_id: <id-or-scoped-reference>
session_id: <id>
decision_id: <ape-decision-id>
lesson_id: <id>
objective_ids: [<id>]
competency_ids: [<id>]
llm_capability_id: <capability>
model_identity: <model/provider metadata where available>
model_version: <version where available>
input_context_fingerprint: <optional deterministic reference>
output_schema_version: <version>
content: <candidate content>
validation_status: <state>
validation_reference: <id>
mastery_policy_reference: <id/version when relevant>
created_at: <timestamp>
parent_generation_id: <optional>
```

Exact persistence schema is `PENDING`.

The candidate must be attributable to the request and bounded pedagogical decision that produced it. Raw learner-sensitive context should not be duplicated unnecessarily.

## 6. What validation must establish

Validation is context-specific and may include:

- schema validity;
- required-field completeness;
- output-length/format constraints;
- curriculum alignment;
- objective/competency alignment;
- prohibited-content/policy constraints;
- linguistic constraints;
- task-specific pedagogical constraints;
- referenced-knowledge validity where applicable;
- required uncertainty/refusal handling;
- candidate provenance integrity.

The exact validation rule set is `PENDING` and belongs to the applicable contracts.

## 7. What validation does NOT establish

A validation pass does **not** establish that:

- the learner has mastered a competency;
- the learner made an error;
- a pronunciation judgment is true;
- an assessment is authoritative;
- progression is allowed;
- the generated claim is a new curriculum fact;
- an inferred learner trait is true.

These require their own governed evidence and domain contracts.

## 8. Generated feedback versus learner evidence

A generated correction such as a proposed reformulation is an instructional artifact.

It must not be confused with evidence about the learner.

```text
Generated correction
        ≠
Learner response evidence
```

If the learner subsequently responds to the correction, that new learner response is independently observed and enters the normal evidence pipeline.

## 9. Generated assessment-like content

An LLM may be asked to produce a linguistic interpretation or candidate assessment.

The output remains a candidate:

```text
LLM
 ↓
LinguisticAssessmentCandidate / GenerationCandidate
 ↓
validation
 ↓
assessment contract
 ↓
authoritative Assessment only if accepted through that contract
```

The conversion must preserve provenance and must identify the validating/accepting component and applicable policy. The generated text itself is not silently promoted to authoritative evidence.

## 10. Mastery boundary

The following is prohibited:

```text
LLM: "The learner has mastered this."
             ↓
        MasteryRecord
```

The permitted route is:

```text
Learner evidence
      ↓
Evidence validation
      ↓
Assessment
      ↓
MasteryPolicy(identity + version)
      ↓
Mastery evaluation
      ↓
MasteryRecord
```

An LLM candidate may support a bounded interpretation step only when the relevant evidence/assessment contract explicitly permits it. It cannot redefine the MasteryPolicy or bypass its requirements.

## 11. Progression boundary

`LLMGenerationCandidate` cannot establish `ProgressionEligibility`.

The domain must independently evaluate prerequisites, mastery gates, evidence sufficiency, policy validity, snapshot consistency and conflicts.

Therefore conversational statements such as "you are ready for the next lesson" are not progression evidence.

## 12. Error boundary

An LLM candidate may propose an `ErrorObservationCandidate`, but it cannot create authoritative `ErrorObservation` state directly.

The governed path remains:

```text
Learner observation
 ↓
Evidence
 ↓
Assessment
 ↓
ErrorObservationCandidate (optional)
 ↓
FDM validation/acceptance
 ↓
ErrorObservation
```

## 13. Rejection and repair

A candidate must be rejected when it violates an applicable hard constraint or cannot be validated with sufficient confidence for the requested use.

Repair or regeneration must create a new candidate rather than mutate the rejected candidate's historical content.

Examples of rejection causes:

- malformed schema;
- missing required fields;
- curriculum/objective mismatch;
- unsupported linguistic claim;
- prohibited policy violation;
- invalid referenced knowledge;
- unresolved required uncertainty;
- candidate attempts to issue unauthorized domain state changes.

## 14. Candidate acceptance is scoped

Acceptance is not a universal trust promotion.

A candidate can be:

- accepted for learner-facing wording;
- rejected for assessment use;
- accepted for one activity type but rejected for another;
- accepted for generation but not accepted as evidence.

The acceptance record must therefore identify the intended use and applicable validation contract.

## 15. Model replacement invariant

Replacing, removing, downgrading, or upgrading the LLM must not change authoritative curriculum, mastery or progression rules.

Different models may produce different candidates. Only candidates satisfying the same governing contracts may enter the same bounded use path.

## 16. Offline-first invariant

The core pedagogical/domain path must remain valid if LLM generation is unavailable.

LLM unavailability must result in a controlled fallback, such as a deterministic activity, stored approved content, retry, or explicit capability-unavailable state, according to future capability policy.

LLM failure must not be converted into learner failure or authoritative state corruption.

## 17. Determinism and replay

The system should preserve sufficient metadata to reproduce or audit a candidate generation event where technically possible, including model/capability identity, schema version, relevant policy references and request provenance.

Reproducibility of the exact token output is not assumed unless the selected runtime provides that guarantee; it remains `PENDING`.

## 18. Security/privacy

Candidate persistence must follow data minimization.

The system should reference learner evidence rather than copying raw audio, full sensitive history or unnecessary personal data into every LLM request/candidate record.

Exact encryption, retention, deletion and access rules remain `PENDING`.

## 19. Proposed invariants

### C010-I01 — Candidate non-authority

`LLMGenerationCandidate` cannot directly mutate authoritative domain state.

### C010-I02 — Provenance

Every persisted candidate must be attributable to its request/context and validation result.

### C010-I03 — Validation gate

A candidate cannot be delivered through a controlled path without passing the applicable hard validation requirements.

### C010-I04 — Scoped acceptance

Acceptance applies to a declared use; it is not blanket trust.

### C010-I05 — Evidence separation

Generated content and learner-generated evidence remain distinct records/concepts.

### C010-I06 — Assessment separation

Assessment authority requires the assessment contract; candidate text alone is insufficient.

### C010-I07 — Mastery isolation

Candidate content cannot bypass MasteryPolicy evaluation.

### C010-I08 — Progression isolation

Candidate content cannot establish progression eligibility.

### C010-I09 — Historical integrity

Rejected or superseded candidates are not rewritten to conceal their original state.

### C010-I10 — Model replaceability

Authoritative rules do not depend on a specific LLM.

### C010-I11 — Offline containment

LLM unavailability cannot corrupt authoritative learner state or make invalid progression possible.

### C010-I12 — Uncertainty preservation

Unknown or unresolved model output remains non-authoritative rather than being silently upgraded to certainty.

## 20. Acceptance tests

### C010-T01 — Direct mutation

Attempting to persist an LLM candidate directly as mastery/progression/SDT state must fail.

### C010-T02 — Malformed candidate

Malformed output must not reach controlled delivery without repair/regeneration or fallback.

### C010-T03 — Candidate containing mastery claim

A candidate containing a mastery statement must remain non-authoritative.

### C010-T04 — Candidate containing error claim

An error classification in a candidate must not create an authoritative `ErrorObservation` without the governed evidence/assessment path.

### C010-T05 — Scoped acceptance

A candidate accepted for learner-facing wording must not automatically be accepted for assessment use.

### C010-T06 — Repair lineage

Repair/regeneration creates a new generation identity and preserves lineage to the rejected candidate where applicable.

### C010-T07 — Model replacement

Two model implementations may produce different candidates, but neither can bypass the same domain gates.

### C010-T08 — LLM unavailable

Removing the LLM must not permit invalid mastery/progression or corrupt learner state.

### C010-T09 — Uncertainty

An unresolved candidate claim remains unresolved and cannot be converted to verified state solely by generation confidence.

### C010-T10 — Provenance replay

A persisted candidate can be traced to its request, validation result and governing context according to the available provenance contract.

## 21. Open decisions

- final candidate persistence schema;
- exact validation taxonomy and severity;
- exact LLM Gateway contract;
- exact model metadata requirements;
- candidate retention policy;
- deterministic replay guarantees;
- approved knowledge/RAG validation mechanism;
- exact fallback matrix;
- assessment conversion contract;
- privacy/encryption requirements;
- executable test implementation.

## 22. Acceptance status

This artifact resolves C-010 at **contract level only**.

It remains **PROPOSED / REQUIRES APPROVAL** until source-spec integration, automated checks, independent audit and human approval are complete.
