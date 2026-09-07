# ELS-POC-002G — Secondary Audit Pack

## Audit purpose
Independent red-team review of the ELS continuity-control POC. The auditor must not rely on conversation history and must not treat another AI verdict as evidence.

## Scope
Review only:
- ELS-CHECKPOINT v0.2 approved contract;
- POC-002E checkpoint verifier evidence;
- POC-002F exact-head CI evidence;
- POC-002G executable continuity-control tests;
- checkpoint identity and ancestry semantics;
- claims about crash/restart and quota exhaustion.

## Required evidence
Repository ref: `recovery/els-poc-002G`
POC-002G test commit: `1c1eb393891d79b7d9d00debe4a5cec3b5ac921c`
POC-002G evidence commit: `7a2dfcc5db4b43ff7df0985bf827a4a14d26f711`
POC-002G checkpoint commit: `21aef45664e860f2e11a6e4e7d0b0291c72087ed`

## Audit questions
1. Does ELS-CHECKPOINT v0.2 avoid self-referential checkpoint-storage identity?
2. Is `state_head` correctly treated as the resumable engineering state?
3. Is checkpoint storage metadata derived rather than trusted from payload?
4. Do the executable POC tests actually test the stated semantics?
5. Are the process-interruption claims correctly bounded?
6. Are the synthetic-budget claims correctly bounded and explicitly distinguished from provider quota behavior?
7. Does any artifact overclaim production readiness?
8. Are prior conflicting POC-002B artifacts preserved rather than silently rewritten?
9. Are there hidden continuation paths that bypass checkpoint verification?
10. What P0/P1 defects remain before ELS operational readiness?

## Auditor independence requirement
A genuinely independent secondary audit requires a different model/provider or otherwise independent execution context from the primary agent. A self-review by the same agent does not satisfy this requirement.

## Allowed verdicts
`PASS`, `PASS_WITH_LIMITATIONS`, `FAIL`, `UNKNOWN`, `CONFLICT`.

## Hard rule
If evidence is unavailable, return `UNKNOWN`; do not infer successful execution.
