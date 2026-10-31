"""Adversarial regression tests for the KCA context resolver fail-closed gate."""
import hashlib
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "kca_context_resolver.py"
SPEC = importlib.util.spec_from_file_location("kca_context_resolver", MODULE_PATH)
resolver = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(resolver)


class ResolverFailClosedTests(unittest.TestCase):
    def test_missing_governance_and_c0_sources_block(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(resolver, "ROOT", Path(directory)), patch.object(
                resolver, "identity",
                return_value={"branch": "test", "head": "abc", "tree": "def"},
            ):
                package = resolver.resolve("bounded task", 8)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertTrue(package["blockers"])
        self.assertTrue(all(item["state"] in {"FAIL", "UNKNOWN", "CONFLICT"}
                            for item in package["blockers"]))

    def test_missing_objective_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(resolver, "ROOT", Path(directory)), patch.object(
                resolver, "identity",
                return_value={"branch": "test", "head": "abc", "tree": "def"},
            ):
                package = resolver.resolve("   ", 8)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertIn("MISSING_OBJECTIVE", {item["code"] for item in package["blockers"]})

    def test_invalid_limit_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(resolver, "ROOT", Path(directory)), patch.object(
                resolver, "identity",
                return_value={"branch": "test", "head": "abc", "tree": "def"},
            ):
                package = resolver.resolve("bounded task", 0)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertIn("INVALID_LIMIT", {item["code"] for item in package["blockers"]})

    def test_unverifiable_repository_identity_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(resolver, "ROOT", Path(directory)), patch.object(
                resolver, "identity", side_effect=resolver.ResolverError("dirty worktree"),
            ):
                package = resolver.resolve("bounded task", 8)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertIn("SOURCE_IDENTITY_UNVERIFIED",
                      {item["code"] for item in package["blockers"]})

    def test_dirty_git_worktree_is_rejected_by_real_identity_check(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-b", "test-branch"], cwd=root,
                           check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.invalid"],
                           cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=root,
                           check=True, capture_output=True)
            source = root / "tracked.txt"
            source.write_text("committed", encoding="utf-8")
            subprocess.run(["git", "add", "tracked.txt"], cwd=root, check=True,
                           capture_output=True)
            subprocess.run(["git", "commit", "-m", "baseline"], cwd=root, check=True,
                           capture_output=True)
            with patch.object(resolver, "ROOT", root):
                self.assertEqual(resolver.identity()["branch"], "test-branch")
                source.write_text("modified", encoding="utf-8")
                with self.assertRaises(resolver.ResolverError):
                    resolver.identity()

    def test_c0_paths_match_repository_topology(self):
        repo_root = Path(__file__).resolve().parents[1]
        self.assertEqual(
            resolver.CORE,
            (
                Path("PROJECT-CONSTITUTION.md"),
                Path("PROJECT-STATE.yaml"),
                Path("docs/ARCHITECTURE-BIBLE.md"),
            ),
        )
        self.assertTrue(all((repo_root / path).is_file() for path in resolver.CORE))

    def test_working_file_mismatch_with_head_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.md").write_bytes(b"working bytes")
            committed = b"committed bytes"
            with (
                patch.object(resolver, "ROOT", root),
                patch.object(resolver, "CORE", ()),
                patch.object(resolver, "REQUIRED_GOVERNANCE", ()),
                patch.object(resolver, "candidate_files", return_value=[Path("sample.md")]),
                patch.object(resolver, "identity",
                              return_value={"branch": "test", "head": "abc", "tree": "def"}),
                patch.object(resolver, "git", return_value="blob123"),
                patch.object(resolver, "git_bytes", return_value=committed),
            ):
                package = resolver.resolve("sample", 8)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertIn("WORKTREE_HEAD_CONTENT_CONFLICT",
                      {item["code"] for item in package["blockers"]})

    def test_source_mutation_during_resolution_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "sample.md").write_bytes(b"committed bytes")
            committed_sha = hashlib.sha256(b"committed bytes").hexdigest()
            with (
                patch.object(resolver, "ROOT", root),
                patch.object(resolver, "CORE", ()),
                patch.object(resolver, "REQUIRED_GOVERNANCE", ()),
                patch.object(resolver, "candidate_files", return_value=[Path("sample.md")]),
                patch.object(resolver, "identity",
                              return_value={"branch": "test", "head": "abc", "tree": "def"}),
                patch.object(resolver, "git", return_value="blob123"),
                patch.object(resolver, "git_bytes", return_value=b"committed bytes"),
                patch.object(resolver, "sha256_file",
                              side_effect=[committed_sha, "changed-during-resolution"]),
            ):
                package = resolver.resolve("sample", 8)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertIn("SOURCE_IDENTITY_CONFLICT",
                      {item["code"] for item in package["blockers"]})

    def test_repository_head_change_during_resolution_blocks(self):
        first = {"branch": "test", "head": "abc", "tree": "def"}
        second = {"branch": "test", "head": "changed", "tree": "changed-tree"}
        with tempfile.TemporaryDirectory() as directory:
            with (
                patch.object(resolver, "ROOT", Path(directory)),
                patch.object(resolver, "CORE", ()),
                patch.object(resolver, "REQUIRED_GOVERNANCE", ()),
                patch.object(resolver, "candidate_files", return_value=[]),
                patch.object(resolver, "identity", side_effect=[first, second]),
            ):
                package = resolver.resolve("bounded task", 8)
        self.assertEqual(package["gate"], "BLOCKED")
        self.assertIn("SOURCE_STATE_CHANGED",
                      {item["code"] for item in package["blockers"]})


if __name__ == "__main__":
    unittest.main()
