"""Adversarial regression tests for the KCA context resolver fail-closed gate."""
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

MODULE_PATH = Path(__file__).with_name("kca_context_resolver.py")
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
        self.assertNotEqual(package["blockers"], [])

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


if __name__ == "__main__":
    unittest.main()
