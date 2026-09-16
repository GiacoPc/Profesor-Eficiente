#!/usr/bin/env python3
"""Deterministic, fail-closed KCA/ELS context resolver.

The resolver is read-only. It must never manufacture an authoritative package
when required sources, repository identity, or governance dependencies cannot
be verified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = [
    "docs/00-governance/PROJECT-CONSTITUTION.md",
    "docs/00-governance/PROJECT-STATE-BASELINE-v1.0.md",
    "docs/00-governance/ARCHITECTURE-BIBLE-v1.0.md",
]
KCA_DIR = "docs/00-governance/KCA-ELS-CONTEXT-ECONOMY-v1.0"
REQUIRED_FIELDS = ("project_identity", "current_state", "active_objective", "hard_constraints")
BLOCKING_STATES = {"FAIL", "UNKNOWN", "CONFLICT"}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.STDOUT).strip()


def git_identity() -> dict:
    return {
        "branch": git("branch", "--show-current"),
        "head": git("rev-parse", "HEAD"),
        "tree": git("rev-parse", "HEAD^{tree}"),
    }


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def candidate_files() -> list[Path]:
    result: list[Path] = []
    for rel in CORE:
        path = ROOT / rel
        if path.is_file():
            result.append(path)
    directory = ROOT / KCA_DIR
    if directory.is_dir():
        result.extend(sorted(directory.glob("*.md")))
        result.extend(sorted(directory.glob("*.yaml")))
    return list(dict.fromkeys(result))


def source_record(path: Path) -> dict:
    return {
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }


def validation_errors(objective: str, files: list[Path], limit: int) -> list[dict]:
    errors: list[dict] = []
    if not objective.strip():
        errors.append({"code": "CEC-VAL-001", "state": "FAIL", "detail": "Objective is empty."})
    if limit < 1:
        errors.append({"code": "CEC-VAL-002", "state": "FAIL", "detail": "Limit must be positive."})
    missing_core = [rel for rel in CORE if not (ROOT / rel).is_file()]
    if missing_core:
        errors.append({"code": "CEC-VAL-003", "state": "UNKNOWN", "detail": "Required core sources missing.", "paths": missing_core})
    if not files:
        errors.append({"code": "CEC-VAL-004", "state": "UNKNOWN", "detail": "No candidate sources available."})
    try:
        identity = git_identity()
        if not all(identity.values()):
            errors.append({"code": "CEC-VAL-005", "state": "UNKNOWN", "detail": "Repository identity is incomplete."})
    except (subprocess.CalledProcessError, OSError) as exc:
        errors.append({"code": "CEC-VAL-006", "state": "UNKNOWN", "detail": f"Repository identity unavailable: {exc}"})
    return errors


def resolve(objective: str, limit: int) -> dict:
    files = candidate_files()
    errors = validation_errors(objective, files, limit)
    if errors:
        return {
            "status": "BLOCKED",
            "blockers": errors,
            "objective": objective,
            "context_class": "UNRESOLVED",
            "source_artifacts": [],
            "next_authorized_action": "Resolve every blocker and rerun validation.",
        }

    terms = [term for term in objective.lower().split() if len(term) > 2]

    def score(path: Path) -> int:
        text = path.read_text(encoding="utf-8", errors="strict").lower()
        name = path.name.lower()
        return sum(text.count(term) + 3 * name.count(term) for term in terms)

    ranked = sorted(((score(path), path) for path in files), key=lambda item: (-item[0], str(item[1])))
    selected = [path for points, path in ranked if points > 0][:limit]
    for rel in CORE:
        path = ROOT / rel
        if path not in selected:
            selected.insert(0, path)
    selected = selected[:limit]

    if not selected:
        return {
            "status": "BLOCKED",
            "blockers": [{"code": "CEC-VAL-007", "state": "UNKNOWN", "detail": "No sources selected for objective."}],
            "objective": objective,
            "context_class": "UNRESOLVED",
            "source_artifacts": [],
            "next_authorized_action": "Resolve source selection failure and rerun validation.",
        }

    return {
        "status": "VALIDATION_REQUIRED",
        "package_id": "kca-context-" + hashlib.sha256(objective.encode("utf-8")).hexdigest()[:16],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_state": git_identity(),
        "context_class": "C0+C1",
        "objective": objective,
        "source_artifacts": [source_record(path) for path in selected],
        "blockers": [],
        "next_authorized_action": "Independently verify source relevance, dependencies, provenance and continuation-gate conditions before governed use.",
        "evidence_refs": [],
        "omitted_context": "Unselected chat history, duplicated prose and irrelevant repository material.",
        "validation_note": "This package is not an authorization or proof of governance compliance.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a read-only KCA/ELS context package.")
    parser.add_argument("objective", help="One bounded task objective")
    parser.add_argument("--limit", type=int, default=8, help="Maximum source artifacts")
    parser.add_argument("--output", type=Path, help="Write JSON package to this path")
    args = parser.parse_args()
    package = resolve(args.objective, args.limit)
    payload = json.dumps(package, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0 if package.get("status") != "BLOCKED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
