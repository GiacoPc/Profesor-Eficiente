# ELS-POC-002G — Failure/Continuity Simulation

## Purpose
Exercise two ELS controls that can be tested without external provider access: process interruption/restart semantics and deterministic budget-exhaustion stopping semantics.

## Test A — Process interruption/restart

A disposable CI process writes a durable checkpoint containing an iteration identifier and exact `state_head`, exits unexpectedly, and a subsequent process reads the checkpoint and resumes only from the recorded state identity.

**Classification:** executable process-level simulation.

**It does not prove:** workstation power loss recovery, filesystem corruption recovery, Android process death behavior, or recovery across an actual machine restart.

## Test B — Budget exhaustion

A deterministic budget guard consumes a finite synthetic budget. When the remaining budget crosses the configured stop condition, the process must persist a checkpoint and stop rather than continue speculative work.

**Classification:** executable synthetic-budget simulation.

**It does not prove:** remaining quota reported by any external model provider, billing system, IDE, or ZCode account.

## Required semantics

1. Failure/interruption is recorded as information, not silently converted into success.
2. Resume requires exact repository/state identity verification.
3. Budget exhaustion produces a controlled stop/checkpoint.
4. No continuation is authorized from an unverified or conflicting checkpoint.
5. No claim may exceed the evidence actually produced by the test.
