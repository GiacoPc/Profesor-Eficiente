#!/usr/bin/env python3
"""P1-001 real process-interruption evidence test.

Controller process -> spawn target -> target durably writes checkpoint -> controller
sends SIGTERM -> controller verifies persisted bytes -> deterministic oracle ->
evidence artifact.

This test deliberately proves only POSIX process interruption (SIGTERM). It does
not claim workstation crash, power loss, Android process death, or provider quota.
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

from ci_identity import resolve_identity

PAYLOAD = (
    "schema_version: '0.1'\n"
    "evidence_id: 'P1-001-REAL-PROCESS-INTERRUPTION-001'\n"
    "failure_class: 'process_interruption'\n"
    "payload_marker: 'durable-before-sigterm'\n"
)


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def identity(pid: int) -> dict[str, object]:
    return {"pid": pid, "python": sys.executable, "role": "controller" if pid == os.getpid() else "target"}


def target(checkpoint: Path, ready: Path) -> None:
    data = PAYLOAD.encode("utf-8")
    with checkpoint.open("wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    ready.write_text("ready\n", encoding="utf-8")
    # Stay alive until the controller deliberately interrupts this process.
    while True:
        time.sleep(0.05)


def controller() -> int:
    identity_data = resolve_identity(git)
    repo = identity_data["repository"]
    ref = identity_data["ref"]
    head = identity_data["engineering_head"]
    remote = identity_data["remote"]
    execution_ref = identity_data["execution_ref"]

    with tempfile.TemporaryDirectory(prefix="p1-001-interruption-") as td:
        root = Path(td)
        checkpoint = root / "checkpoint.yaml"
        ready = root / "ready.flag"
        artifact = Path("artifacts/p1-001-process-interruption-evidence.json")
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
        interruption_point = "after target fsync and readiness signal; before target normal exit"

        deadline = time.monotonic() + 10
        while not ready.exists() and time.monotonic() < deadline:
            if child.poll() is not None:
                break
            time.sleep(0.02)

        if not ready.exists():
            child.kill()
            stdout, stderr = child.communicate(timeout=2)
            raise RuntimeError(f"target did not reach durable-write boundary: stdout={stdout!r} stderr={stderr!r}")

        before_sha = hashlib.sha256(checkpoint.read_bytes()).hexdigest()
        os.kill(target_pid, signal.SIGTERM)
        return_code = child.wait(timeout=5)

        persisted = checkpoint.read_bytes()
        persisted_sha = hashlib.sha256(persisted).hexdigest()
        expected_sha = hashlib.sha256(PAYLOAD.encode("utf-8")).hexdigest()
        observed = {
            "target_return_code": return_code,
            "target_terminated_by_sigterm": return_code == -signal.SIGTERM,
            "checkpoint_exists_after_interruption": checkpoint.exists(),
            "persisted_byte_length": len(persisted),
            "persisted_sha256": persisted_sha,
            "expected_sha256": expected_sha,
            "bytes_match_expected": persisted == PAYLOAD.encode("utf-8"),
            "bytes_stable_across_interruption": before_sha == persisted_sha,
        }

        oracle = "PASS" if all([
            observed["target_terminated_by_sigterm"],
            observed["checkpoint_exists_after_interruption"],
            observed["bytes_match_expected"],
            observed["bytes_stable_across_interruption"],
        ]) else "FAIL"

        evidence = {
            "evidence_id": "P1-001-REAL-PROCESS-INTERRUPTION-001",
            "failure_class": "process_interruption",
            "fidelity_boundary": "POSIX process interruption via SIGTERM only",
            "repository": repo,
            "remote": remote,
            "ref": ref,
            "ref_source": identity_data["ref_source"],
            "execution_ref": execution_ref,
            "engineering_head": head,
            "controller_identity": identity(controller_pid),
            "target_identity": identity(target_pid),
            "interruption_method": "SIGTERM",
            "interruption_point": interruption_point,
            "persisted_bytes": {
                "length": len(persisted),
                "sha256": persisted_sha,
                "expected_sha256": expected_sha,
                "match_expected": observed["bytes_match_expected"],
            },
            "observed_result": observed,
            "oracle_result": oracle,
            "timestamp_unix": time.time(),
            "evidence_boundary": [
                "Does not prove workstation crash.",
                "Does not prove power loss.",
                "Does not prove Android process death.",
                "Does not prove provider or IDE quota exhaustion.",
            ],
        }
        artifact.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(json.dumps(evidence, indent=2, sort_keys=True))
        return 0 if oracle == "PASS" else 1


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--target":
        target(Path(sys.argv[2]), Path(sys.argv[3]))
        raise SystemExit(0)
    raise SystemExit(controller())
