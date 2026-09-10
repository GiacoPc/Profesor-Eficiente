#!/usr/bin/env python3
"""P1-001-C WB-001 reproducible interrupted-write test.

The target executes the evidenced single-file binary write path, but writes the
payload in deterministic chunks. It pauses after a deterministic partial write;
the independent controller then terminates the target. The controller inspects
persisted bytes and applies the P1-001-C oracle.

This test intentionally proves only the WB-001 POSIX Python file-write boundary.
It does not claim atomic rename, append, multi-file transactions, Android
process-death recovery, workstation crash recovery, power-loss recovery, or
provider/IDE quota behavior.
"""
from __future__ import annotations

import hashlib
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PAYLOAD = ("schema_version: '0.1'\n" + "payload_marker: 'WB-001-partial-write'\n" + ("x" * 8192) + "\n").encode("utf-8")
CHUNK_SIZE = 256
PARTIAL_CHUNKS = 3


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def process_identity(pid: int, role: str) -> dict[str, object]:
    return {"pid": pid, "python": sys.executable, "role": role}


def target(checkpoint: Path, ready: Path) -> None:
    with checkpoint.open("wb") as f:
        for index in range(PARTIAL_CHUNKS):
            start = index * CHUNK_SIZE
            end = start + CHUNK_SIZE
            f.write(PAYLOAD[start:end])
            f.flush()
            if index + 1 == PARTIAL_CHUNKS:
                # This is the deterministic interruption point: bytes have been
                # written and flushed, but the payload is deliberately incomplete.
                ready.write_text("partial-write-ready\n", encoding="utf-8")
                while True:
                    time.sleep(0.05)
        # Unreachable in the interrupted test; retained to document the same
        # complete-write path used by the existing P1-001 fixture.
        f.flush()
        os.fsync(f.fileno())


def oracle(*, repository_identity_ok: bool, boundary_supported: bool,
           artifact_exists: bool, observed_len: int, expected_len: int,
           observed_sha: str, expected_sha: str) -> str:
    if not repository_identity_ok:
        return "CONFLICT"
    if not boundary_supported:
        return "UNKNOWN"
    if not artifact_exists:
        return "UNKNOWN"
    if observed_len == expected_len and observed_sha == expected_sha:
        return "RECOVERABLE"
    if 0 < observed_len < expected_len:
        return "INVALID"
    return "UNKNOWN"


def controller() -> int:
    repo = git("rev-parse", "--show-toplevel")
    ref = git("symbolic-ref", "--short", "HEAD")
    head = git("rev-parse", "HEAD")
    remote = git("remote", "get-url", "origin")

    with tempfile.TemporaryDirectory(prefix="p1-001-c-wb001-") as td:
        root = Path(td)
        checkpoint = root / "checkpoint.yaml"
        ready = root / "ready.flag"
        artifact = Path("artifacts/p1-001-c-wb001-partial-write-evidence.json")
        artifact.parent.mkdir(parents=True, exist_ok=True)

        child = subprocess.Popen(
            [sys.executable, __file__, "--target", str(checkpoint), str(ready)],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        controller_pid = os.getpid()
        target_pid = child.pid
        interruption_point = (
            f"after deterministic partial write of {PARTIAL_CHUNKS * CHUNK_SIZE} "
            "bytes and flush, before payload completion and fsync"
        )

        deadline = time.monotonic() + 10
        while not ready.exists() and time.monotonic() < deadline:
            if child.poll() is not None:
                break
            time.sleep(0.01)
        if not ready.exists():
            child.kill()
            stdout, stderr = child.communicate(timeout=2)
            raise RuntimeError(
                f"target did not reach deterministic partial-write point: "
                f"stdout={stdout!r} stderr={stderr!r}"
            )

        pre_sha = hashlib.sha256(checkpoint.read_bytes()).hexdigest()
        pre_len = checkpoint.stat().st_size

        os.kill(target_pid, signal.SIGTERM)
        return_code = child.wait(timeout=5)

        persisted = checkpoint.read_bytes() if checkpoint.exists() else b""
        observed_sha = hashlib.sha256(persisted).hexdigest()
        expected_sha = hashlib.sha256(PAYLOAD).hexdigest()
        repository_identity_ok = bool(repo and ref and head and remote)
        boundary_supported = True

        oracle_result = oracle(
            repository_identity_ok=repository_identity_ok,
            boundary_supported=boundary_supported,
            artifact_exists=checkpoint.exists(),
            observed_len=len(persisted),
            expected_len=len(PAYLOAD),
            observed_sha=observed_sha,
            expected_sha=expected_sha,
        )

        observed = {
            "target_return_code": return_code,
            "target_terminated_by_sigterm": return_code == -signal.SIGTERM,
            "checkpoint_exists_after_interruption": checkpoint.exists(),
            "pre_interruption_byte_length": pre_len,
            "pre_interruption_sha256": pre_sha,
            "persisted_byte_length": len(persisted),
            "persisted_sha256": observed_sha,
            "expected_byte_length": len(PAYLOAD),
            "expected_sha256": expected_sha,
            "bytes_match_expected": persisted == PAYLOAD,
            "partial_write_observed": 0 < len(persisted) < len(PAYLOAD),
            "bytes_stable_after_termination": hashlib.sha256(checkpoint.read_bytes()).hexdigest() == observed_sha if checkpoint.exists() else False,
        }

        evidence = {
            "evidence_id": "P1-001-C-WB001-PARTIAL-WRITE-001",
            "failure_class": "partial_write",
            "environment": "POSIX Python process on GitHub Actions Ubuntu runner",
            "interruption_method": "SIGTERM",
            "interruption_point": interruption_point,
            "write_boundary": "WB-001",
            "persisted_artifact": "temporary checkpoint.yaml",
            "expected_recovery": "Deterministically classify interrupted artifact; do not assume recoverability.",
            "evidence_boundary": [
                "POSIX Python single-file write boundary only.",
                "Does not prove atomic rename, append, multi-file transaction, Android process death, workstation crash, power loss, or provider/IDE quota recovery.",
            ],
            "repository": repo,
            "remote": remote,
            "ref": ref,
            "engineering_head": head,
            "controller_identity": process_identity(controller_pid, "controller"),
            "target_identity": process_identity(target_pid, "target"),
            "pre_interruption_checkpoint_identity": {
                "length": pre_len,
                "sha256": pre_sha,
            },
            "post_interruption_recovery_result": "partial artifact persisted after target termination",
            "expected_artifact_identity": {
                "length": len(PAYLOAD),
                "sha256": expected_sha,
            },
            "observed_artifact_identity": {
                "length": len(persisted),
                "sha256": observed_sha,
            },
            "parse_or_integrity_result": {
                "complete_payload_match": persisted == PAYLOAD,
                "partial_write": 0 < len(persisted) < len(PAYLOAD),
            },
            "observed_result": observed,
            "oracle_result": oracle_result,
            "timestamp_unix": time.time(),
        }
        artifact.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(evidence, indent=2, sort_keys=True))
        # INVALID is an expected deterministic oracle for this intentionally
        # truncated artifact, so only unexpected oracle behavior fails the test.
        return 0 if oracle_result == "INVALID" and observed["partial_write_observed"] else 1


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--target":
        target(Path(sys.argv[2]), Path(sys.argv[3]))
        raise SystemExit(0)
    raise SystemExit(controller())
