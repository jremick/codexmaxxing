"""Focused regression tests for the public-content validator."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_content.py"
SPEC = importlib.util.spec_from_file_location("validate_content", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load validator")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ValidatorSafeguardTests(unittest.TestCase):
    def test_private_pattern_categories_do_not_return_matched_values(self) -> None:
        text = "Contact " + "reader" + "@example.com from 192.168.1.20."
        self.assertEqual(
            validator.private_pattern_names(text),
            ["email address", "private IPv4 address"],
        )

    def test_external_url_policy_is_allowlist_based(self) -> None:
        self.assertIsNone(
            validator.external_url_issue("https://learn.chatgpt.com/docs/models")
        )
        self.assertEqual(
            validator.external_url_issue("https://example.com/profile"),
            "uses a host outside the reviewed allowlist",
        )

    def test_action_references_require_full_commit_sha(self) -> None:
        self.assertTrue(
            validator.is_pinned_action_reference(
                "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1"
            )
        )
        self.assertFalse(validator.is_pinned_action_reference("actions/checkout@v5"))

    def test_fenced_prompt_voice_is_excluded_from_editorial_prose(self) -> None:
        text = "Neutral introduction.\n\n```text\nI want a synthetic example.\n```\n"
        self.assertEqual(validator.without_fenced_code(text), "Neutral introduction.\n")

    def test_svg_active_content_is_detected(self) -> None:
        self.assertEqual(
            validator.svg_security_issues('<svg onload="run()"><script/></svg>'),
            ["script content", "event-handler attribute"],
        )

    def test_png_metadata_and_trailing_payloads_are_detected(self) -> None:
        def chunk(kind: bytes, payload: bytes = b"") -> bytes:
            return len(payload).to_bytes(4, "big") + kind + payload + b"\x00\x00\x00\x00"

        signature = b"\x89PNG\r\n\x1a\n"
        image_end = chunk(b"IEND")
        self.assertEqual(
            validator.png_forbidden_chunks(
                signature + chunk(b"tEXt", b"synthetic") + image_end
            ),
            {"tEXt"},
        )
        with self.assertRaisesRegex(ValueError, "trailing data"):
            validator.png_forbidden_chunks(signature + image_end + b"payload")


if __name__ == "__main__":
    unittest.main()
