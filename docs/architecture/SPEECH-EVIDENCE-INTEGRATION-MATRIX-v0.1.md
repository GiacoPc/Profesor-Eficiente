# C-006 — Speech Evidence Integration Matrix

**Version:** 0.1-draft  
**Status:** PROPOSED / REQUIRES APPROVAL  
**Purpose:** Verify cross-document ownership and sequencing for speech evidence, assessment, mastery and SDT.

## 1. Canonical chain

```text
Learner speech
 ↓
Audio artifact
 ↓
Bounded speech processing
 ↓
Speech candidate evidence
 ↓
FDM evidence validation/provenance
 ↓
Assessment
 ↓
MasteryPolicy + CLM interpretation
 ↓
MasteryRecord / ErrorObservation / learning state
 ↓
SDT projection
 ↓
APE pedagogical decision
```

## 2. Cross-document responsibilities

| Artifact | C-006 responsibility | Must not do |
|---|---|---|
| PAD | Define pedagogical use of valid speech evidence and reinforcement/assessment consequences | Delegate mastery authority to speech models |
| CLM | Define learning-state semantics for speech-derived evidence, uncertainty and mastery interpretation | Define implementation/model-specific speech scores |
| FDM | Own authoritative evidence/assessment provenance, domain state and invariants | Treat model output as authoritative without governed acceptance |
| SDT | Represent governed speech-derived learner state | Persist raw candidate/model output as equivalent to authoritative state |
| APE | Decide pedagogical action from governed state | Manufacture evidence or override mastery policy |
| LPH | Constrain/interpret linguistic speech candidates and validate candidate outputs | Directly mutate mastery, progression or authoritative SDT |
| Audio/speech components | Capture/measure bounded speech signals | Decide pedagogy or progression |
| LLM | Generate bounded interpretation/feedback candidates | Become evidence, mastery or progression authority |
| MasteryPolicy | Define applicable mastery requirements | Be replaced by ad-hoc component thresholds |

## 3. Critical distinctions

1. Audio artifact ≠ evidence judgment.
2. Transcript ≠ linguistic correctness.
3. Acoustic measurement ≠ pedagogical assessment.
4. Candidate assessment ≠ authoritative assessment.
5. Assessment ≠ mastery.
6. Mastery ≠ progression action.
7. Speech failure ≠ learner failure.
8. SDT projection ≠ raw model output.
9. LLM explanation ≠ evidence.
10. APE decision ≠ evidence creation.

## 4. Authority tests

- **C006-AUTH-01:** STT cannot write authoritative mastery.
- **C006-AUTH-02:** Acoustic/prosodic analysis cannot write authoritative progression.
- **C006-AUTH-03:** Pronunciation analysis cannot bypass evidence/assessment boundaries.
- **C006-AUTH-04:** LPH cannot mutate authoritative SDT/mastery directly.
- **C006-AUTH-05:** LLM cannot convert interpretation into authoritative evidence without governed acceptance.
- **C006-AUTH-06:** APE cannot create or rewrite evidence to justify a decision.
- **C006-AUTH-07:** SDT cannot become an alternative source of truth for speech history.

## 5. Evidence-integrity tests

- **C006-E01:** Every accepted speech evidence record has provenance.
- **C006-E02:** Uncertain/insufficient speech remains uncertain/insufficient.
- **C006-E03:** Component/model versions are attributable where interpretation depends on them.
- **C006-E04:** Independent speech dimensions are not silently conflated.
- **C006-E05:** Historical evidence is not rewritten after reassessment.
- **C006-E06:** Component failure does not create a negative learner judgment.
- **C006-E07:** Policy identity/version is retained for authoritative mastery interpretation.

## 6. Offline tests

- **C006-OFF-01:** Core speech assessment path operates without remote services once required local assets are installed.
- **C006-OFF-02:** Remote enhancement cannot become a hidden prerequisite for mastery/progression.
- **C006-OFF-03:** Missing local capability produces a controlled unavailable/insufficient state, not invented evidence.

Exact runtime and model choices are intentionally deferred to SRA and empirical validation.

## 7. Integration gate

C-006 is considered **source-spec integrated** only when PAD, CLM, FDM, APE, LPH and SDT contain direct normative references to this contract or an equivalent approved contract, and the corresponding acceptance tests are represented in automated checks where applicable.

Until then:

**C-006 = INTEGRATED AT CONTRACT LEVEL / SOURCE-SPEC INTEGRATION PENDING.**
