#!/usr/bin/env python3
"""Fail-closed KCA/ELS context resolver.

This tool is read-only. It assembles provenance metadata; it does not grant
governance authority, approve source artifacts, or enforce repository writes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import PurePosixPath

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
DEPENDENCY_MANIFEST = (
    "docs/00-governance/KCA-ELS-CONTEXT-RESOLVER-CORRECTION-001/"
    "DEPENDENCY-MANIFEST.yaml"
)
CORE = [
    "docs/00-governance/PROJECT-CONSTITUTION.md",
    "docs/00-governance/PROJECT-STATE-BASELINE-v1.0.md",
    "docs/00-governance/ARCHITECTURE-BIBLE-v1.0.md",
]
KCA_DIR = "docs/00-governance/KCA-ELS-CONTEXT-ECONOMY-v1.0"
BLOCKING = {"FAIL", "UNKNOWN", "CONFLICT"}


class ResolverError(RuntimeError):
    pass


def git(*args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", *args], cwd=ROOT, text=True, stderr=subprocess.PIPE
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise ResolverError(f"Git identity/source verification failed: {args!r}") from exc


def repository_identity() -> dict:
    branch = git("branch", "--show-current")
    head = git("rev-parse", "HEAD")
    tree = git("rev-parse", "HEAD^{tree}")
    if not branch or len(head) != 40 or len(tree) != 40:
        raise ResolverError("Repository branch, HEAD, or tree identity is unavailable.")
    return {"branch": branch, "head": head, "tree": tree}


def worktree_blockers() -> list[dict]:
    # Strict by design: a package cannot claim canonical source bytes if local
    # changes are not represented by the declared Git commit.
    status = git("status", "--porcelain", "--untracked-files=all")
    if not status:
        return []
    return [{
        "code": "DIRTY_WORKTREE",
        "state": "UNKNOWN",
        "detail": "Working tree contains tracked or untracked changes; source bytes are not frozen to HEAD.",
    }]


def blob_identity(path: str, head: str) -> dict:
    # Validate the path before asking Git to resolve it.
    parsed = PurePosixPath(path)
    if parsed.is_absolute() or ".." in parsed.parts or not path:
        raise ResolverError(f"Unsafe source path: {path!r}")
    try:
        blob = git("rev-parse", f"{head}:{path}")
        raw = subprocess.check_output(
            ["git", "show", f"{head}:{path}"], cwd=ROOT, stderr=subprocess.PIPE
        )
    except (ResolverError, subprocess.CalledProcessError) as exc:
        raise ResolverError(f"Required source is absent from HEAD: {path}") from exc
    return {
        "path": path,
        "git_blob_sha": blob,
        "content_sha256": hashlib.sha256(raw).hexdigest(),
    }


def known_sources() -> list[str]:
    # The manifest is a dependency declaration, not itself a source of authority.
    # Until a YAML parser and schema validator are added, only these explicitly
    # enumerated sources can be selected; unknown dependency expansion is blocked.
    return list(CORE) + [
        DEPENDENCY_MANIFEST,
        f"{KCA_DIR}/KCA-ELS-CONTEXT-ECONOMY-v1.0.md",
        f"{KCA_DIR}/CONTEXT-POLICY.yaml",
        f"{KCA_DIR}/CONTEXT-SCHEMA.yaml",
        f"{KCA_DIR}/CONTEXT-RESOLUTION-PROTOCOL.md",
        f"{KCA_DIR}/CONTEXT-BOOTSTRAP-TEMPLATE.md",
        f"{KCA_DIR}/ACCEPTANCE-MATRIX.yaml",
        f"{KCA_DIR}/SELF-AUDIT.md",
    ]


def resolve(objective: str, limit: int = 8, include_forensic: bool = False) -> dict:
    objective = objective.strip()
    if not objective:
        raise ResolverError("Objective must be non-empty and bounded.")
    if limit < 1:
        raise ResolverError("--limit must be >= 1.")

    ident = repository_identity()
    blockers = worktree_blockers()
    manifest_status = "UNKNOWN"
    sources = []
    candidates = known_sources()

    for path in candidates:
        try:
            item = blob_identity(path, ident["head"])
            item["status"] = "UNKNOWN"
            item["evidence_class"] = "UNKNOWN"
            sources.append(item)
        except ResolverError as exc:
            if path in CORE or path == DEPENDENCY_MANIFEST:
                blockers.append({
                    "code": "REQUIRED_SOURCE_MISSING",
                    "state": "UNKNOWN",
                    "detail": str(exc),
                })

    # The correction manifest is deliberately marked PROPOSED. Do not pretend
    # it is approved policy. This blocks authorization until the manifest has
    # been reviewed, schema-validated, and explicitly approved.
    if any(s["path"] == DEPENDENCY_MANIFEST for s in sources):
        try:
            manifest = subprocess.check_output(
                ["git", "show", f'{ident["head"]}:{DEPENDENCY_MANIFEST}'],
                cwd=ROOT, text=True, stderr=subprocess.PIPE,
            )
            if 'status: "APPROVED"' in manifest or 'status: "DECIDED"' in manifest:
                manifest_status = "APPROVED_OR_DECIDED"
            else:
                manifest_status = "PROPOSED_OR_UNRECOGNIZED"
                blockers.append({
                    "code": "DEPENDENCY_MANIFEST_NOT_APPROVED",
                    "state": "UNKNOWN",
                    "detail": "Dependency manifest is not explicitly APPROVED or DECIDED.",
                })
        except subprocess.CalledProcessError:
            blockers.append({
                "code": "DEPENDENCY_MANIFEST_UNREADABLE",
                "state": "UNKNOWN",
                "detail": "Dependency manifest bytes cannot be verified at HEAD.",
            })

    # This implementation intentionally does not claim that keyword scoring
    # proves relevance, authority, or dependency completeness. Until the
    # manifest is schema-validated and a complete dependency graph resolver is
    # implemented, no package can authorize governed continuation.
    blockers.append({
        "code": "DEPENDENCY_GRAPH_VALIDATION_NOT_IMPLEMENTED",
        "state": "UNKNOWN",
        "detail": "Transitive C2 resolution, cycle detection, status validation, and conflict detection are not yet implemented.",
    })

    if not include_forensic:
        sources = [s for s in sources if "/recovery/" not in s["path"].lower()]
    sources = sources[:limit]
    blocked = bool(blockers) or any(b.get("state") in BLOCKING for b in blockers)
    semantic = {
        "source_state": ident,
        "context_class": "C0+C1" if not include_forensic else "C0+C1+C3",
        "objective": objective,
        "source_artifacts": sources,
        "manifest_status": manifest_status,
        "blockers": blockers,
        "status": "BLOCKED" if blocked else "READY_FOR_REVIEW",
        "next_authorized_action": None if blocked else "Review the bounded context package before use.",
        "write_enforcement": "NOT_APPLICABLE_READ_ONLY_TOOL",
        "limitations": [
            "No automatic governance approval is performed.",
            "No token-savings claim is made.",
            "F21 write enforcement is outside this read-only resolver and must be implemented by any future write adapter.",
        ],
    }
    # Stable identifier excludes the volatile generation timestamp.
    semantic["package_id"] = "kca-context-" + hashlib.sha256(
        json.dumps(semantic, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()[:16]
    semantic["generated_at"] = datetime.now(timezone.utc).isoformat()
    return semantic


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a fail-closed KCA/ELS context package.")
    parser.add_argument("objective", help="One bounded task objective")
    parser.add_argument("--limit", type=int, default=8, help="Maximum source artifacts")
    parser.add_argument("--include-forensic", action="store_true", help="Explicitly request C3 forensic material")
    parser.add_argument("--output", type=__import__("pathlib").Path, help="Write JSON package to this path")
    args = parser.parse_args()
    try:
        package = resolve(args.objective, args.limit, args.include_forensic)
    except ResolverError as exc:
        print(json.dumps({"status": "BLOCKED", "blockers": [{"code": "RESOLUTION_ERROR", "state": "UNKNOWN", "detail": str(exc)}]}, indent=2), file=sys.stderr)
        return 2
    payload = json.dumps(package, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 2 if package["status"] == "BLOCKED" else 0


if __name__ == "__main__":
    raise SystemExit(main())
