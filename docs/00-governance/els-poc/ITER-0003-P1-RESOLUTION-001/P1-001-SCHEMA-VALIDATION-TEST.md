# P1-001 Schema Validation Test Plan

**Status:** TEST PLAN / EXECUTION PENDING

## Purpose

Validate that the P1-001 evidence schema and partial-write decision table are machine-readable, complete, and deterministic before runtime evidence is produced.

## Required assertions

- Every required top-level evidence field is represented.
- Failure classes are explicitly enumerated.
- Process interruption requires distinct controller and target identities.
- Fidelity rules prohibit upgrading simulation evidence to higher-fidelity claims.
- Partial-write outcomes are exactly `RECOVERABLE`, `INVALID`, `CONFLICT`, or `UNKNOWN`.
- Each decision-table branch has explicit inputs and one deterministic result.
- No schema validation result is treated as execution evidence for a real interruption.

## Evidence boundary

A successful schema validation establishes only structural readiness of the evidence contract. It does not demonstrate continuity/recovery behavior and cannot close P1-001.
