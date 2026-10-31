#!/usr/bin/env python3
"""Fail-closed KCA/ELS context resolver.

This tool emits a derived context package only. It never authorizes a governed
write, never mutates Git, and blocks when required governance inputs or source
identity cannot be established.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
KCA_DIR = Path("docs/00-governance/KCA-ELS-CONTEXT-ECONOMY-v1.0")
POLICY = KCA_DIR / "CONTEXT-POLICY.yaml"
SCHEMA = KCA_DIR / "CONTEXT-SCHEMA.yaml"
PROTOCOL = KCA_DIR / "CONTEXT-RESOLUTION-PROTOCOL.md"
BOOTSTRAP = KCA_DIR / "CONTEXT-BOOTSTRAP-TEMPLATE.md"
MATRIX = KCA_DIR / "ACCEPTANCE-MATRIX.yaml"

REQUIRED_GOVERNANCE = (POLICY, SCHEMA, PROTOCOL, BOOTSTRAP, MATRIX)
# Resolve C0 to the repository's actual canonical paths, not the stale paths
# used in the initial v1.0 prototype.
CORE = (
    Path("PROJECT-CONSTITUTION.md"),
    Path("PROJECT-STATE.yaml"),
    Path("docs/ARCHITECTURE-BIBLE.md"),
)


class ResolverError(RuntimeError):
    """Raised when source identity cannot be established."""


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if result.returncode:
        raise ResolverError(
            f"git {' '.join(args)} failed ({result.returncode}): "
            f"{result.stderr.strip() or 'no diagnostic'}"
        )
    return result.stdout.strip()


def git_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, check=False
    )
    if result.returncode:
        diagnostic = result.stderr.decode("utf-8", errors="replace").strip()
        raise ResolverError(
            f"git {' '.join(args)} failed ({result.returncode}): "
            f"{diagnostic or 'no diagnostic'}"
        )
    return result.stdout


def identity() -> dict[str, str]:
    branch = git("branch", "--show-current")
    head = git("rev-parse", "--verify", "HEAD^{commit}")
    tree = git("rev-parse", "--verify", "HEAD^{tree}")
    top = Path(git("rev-parse", "--show-toplevel")).resolve()
    if top != ROOT.resolve():
        raise ResolverError(f"repository root mismatch: expected {ROOT}, got {top}")
    if not branch:
        raise ResolverError("detached HEAD: a named branch/ref is required")
    status = git("status", "--porcelain")
    if status:
        raise ResolverError("working tree is dirty; source state is not reproducible")
    return {"branch": branch, "head": head, "tree": tree}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_record(path: Path) -> dict[str, str]:
    absolute = ROOT / path
    working_sha = sha256_file(absolute)
    committed_bytes = git_bytes("show", f"HEAD:{path.as_posix()}")
    committed_sha = sha256_bytes(committed_bytes)
    git_blob = git("rev-parse", f"HEAD:{path.as_posix()}")
    return {
        "path": path.as_posix(),
        "sha256": working_sha,
        "committed_sha256": committed_sha,
        "git_blob": git_blob,
    }


def candidate_files() -> list[Path]:
    candidates = list(CORE)
    candidates.extend(REQUIRED_GOVERNANCE)
    candidates.extend(sorted((ROOT / KCA_DIR).glob("*.md")))
    candidates.extend(sorted((ROOT / KCA_DIR).glob("*.yaml")))
    unique = list(dict.fromkeys(candidates))
    return [p for p in unique if (ROOT / p).is_file()]


def score(path: Path, terms: list[str]) -> int:
    text = (ROOT / path).read_text(encoding="utf-8").lower()
    name = path.name.lower()
    return sum(text.count(term) + 3 * name.count(term) for term in terms)


def resolve(objective: str, limit: int = 8) -> dict[str, Any]:
    blockers: list[dict[str, str]] = []
    objective = objective.strip()
    if not objective:
        blockers.append({"code": "MISSING_OBJECTIVE", "state": "FAIL",
                         "detail": "A bounded task objective is required."})
    if limit < 1:
        blockers.append({"code": "INVALID_LIMIT", "state": "FAIL",
                         "detail": "Artifact limit must be >= 1."})

    try:
        source_state = identity()
    except ResolverError as exc:
        source_state = {"branch": "", "head": "", "tree": ""}
        blockers.append({"code": "SOURCE_IDENTITY_UNVERIFIED", "state": "UNKNOWN",
                         "detail": str(exc)})

    for rel in REQUIRED_GOVERNANCE:
        if not (ROOT / rel).is_file():
            blockers.append({"code": "MISSING_GOVERNANCE_SOURCE", "state": "UNKNOWN",
                             "detail": f"Required resolver governance source missing: {rel}"})
    for rel in CORE:
        if not (ROOT / rel).is_file():
            blockers.append({"code": "MISSING_C0_CORE_SOURCE", "state": "UNKNOWN",
                             "detail": f"Required C0 core source missing: {rel}"})

    files = candidate_files()
    terms = [term for term in objective.lower().split() if len(term) > 2]
    ranked = sorted(
        ((score(path, terms), path) for path in files),
        key=lambda item: (-item[0], item[1].as_posix()),
    )
    selected = [path for points, path in ranked if points > 0][:max(1, limit)]
    for required in (*REQUIRED_GOVERNANCE, *CORE):
        if (ROOT / required).is_file() and required not in selected:
            selected.append(required)

    sources: list[dict[str, str]] = []
    for path in sorted(set(selected), key=lambda p: p.as_posix()):
        try:
            record = file_record(path)
            sources.append(record)
            if record["sha256"] != record["committed_sha256"]:
                blockers.append({
                    "code": "WORKTREE_HEAD_CONTENT_CONFLICT",
                    "state": "CONFLICT",
                    "detail": f"Working file differs from committed HEAD content: {path}",
                })
        except (OSError, ResolverError, UnicodeError) as exc:
            blockers.append({"code": "SOURCE_IDENTITY_UNVERIFIED", "state": "UNKNOWN",
                             "detail": f"{path}: {exc}"})

    # Re-check selected source bytes and Git blob identities after package assembly.
    for record in sources:
        path = Path(record["path"])
        try:
            current_sha = sha256_file(ROOT / path)
            current_blob = git("rev-parse", f"HEAD:{path.as_posix()}")
            committed_sha = sha256_bytes(git_bytes("show", f"HEAD:{path.as_posix()}"))
            if current_sha != record["sha256"] or current_blob != record["git_blob"]:
                blockers.append({"code": "SOURCE_IDENTITY_CONFLICT", "state": "CONFLICT",
                                 "detail": f"Selected source changed during resolution: {path}"})
            if committed_sha != record["committed_sha256"] or current_sha != committed_sha:
                blockers.append({"code": "WORKTREE_HEAD_CONTENT_CONFLICT", "state": "CONFLICT",
                                 "detail": f"Source bytes do not match committed HEAD: {path}"})
        except (OSError, ResolverError, UnicodeError) as exc:
            blockers.append({"code": "SOURCE_IDENTITY_UNVERIFIED", "state": "UNKNOWN",
                             "detail": f"{path}: {exc}"})

    # The branch/HEAD/tree identity itself must also remain stable during resolution.
    try:
        final_state = identity()
        if final_state != source_state:
            blockers.append({
                "code": "SOURCE_STATE_CHANGED",
                "state": "CONFLICT",
                "detail": "Repository branch, HEAD, or tree changed during context resolution.",
            })
    except ResolverError as exc:
        blockers.append({"code": "SOURCE_IDENTITY_UNVERIFIED", "state": "UNKNOWN",
                         "detail": f"Could not re-verify repository identity: {exc}"})

    gate = "BLOCKED" if blockers else "ELIGIBLE_FOR_HUMAN_REVIEW"
    package_material = {
        "objective": objective,
        "source_state": source_state,
        "source_artifacts": sources,
        "blockers": blockers,
    }
    package_id = "kca-context-" + hashlib.sha256(
        json.dumps(package_material, sort_keys=True).encode("utf-8")
    ).hexdigest()[:16]
    return {
        "package_id": package_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_state": source_state,
        "context_class": "C0+C1",
        "objective": objective,
        "source_artifacts": sources,
        "blockers": blockers,
        "gate": gate,
        "next_authorized_action": (
            "Do not continue governed work until every blocker is resolved and "
            "the package is independently checked."
            if blockers else
            "Human review required; this package does not authorize repository writes."
        ),
        "evidence_refs": [],
        "omitted_context": (
            "Unselected chat history and irrelevant repository material; omission "
            "does not imply that uninspected claims are false."
        ),
        "authority_notice": "Derived context only; Git and approved governance artifacts remain authoritative.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a fail-closed KCA/ELS context package.")
    parser.add_argument("objective", help="One bounded task objective")
    parser.add_argument("--limit", type=int, default=8, help="Maximum task-relevant artifacts")
    parser.add_argument("--output", type=Path, help="Write JSON package to this path")
    args = parser.parse_args()
    package = resolve(args.objective, args.limit)
    payload = json.dumps(package, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 2 if package["gate"] == "BLOCKED" else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ResolverError, UnicodeError) as exc:
        print(json.dumps({
            "gate": "BLOCKED",
            "blockers": [{"code": "RESOLVER_FAILURE", "state": "UNKNOWN", "detail": str(exc)}],
            "next_authorized_action": "Stop and investigate; no governed continuation is authorized.",
        }, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
