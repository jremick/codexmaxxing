#!/usr/bin/env python3
"""Validate Codexmaxxing content without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "resources" / "catalog.json"
REQUIRED_GUIDE_FIELDS = {"title", "status", "audience", "updated"}
CATALOGED_DIRS = {"guides", "resources"}
PRIVATE_PATTERNS = [
    re.compile(r"/Users/[A-Za-z0-9._-]+"),
    re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"(?<![A-Za-z0-9])gh[opsu]_[A-Za-z0-9_]{20,}"),
]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONT_MATTER_PATTERN = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def markdown_files() -> list[Path]:
    ignored = {".git"}
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in ignored for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_PATTERN.match(text)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_catalog(errors: list[str]) -> None:
    if not CATALOG.exists():
        errors.append("resources/catalog.json is missing")
        return

    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"resources/catalog.json is invalid JSON: {exc}")
        return

    items = catalog.get("items")
    if not isinstance(items, list) or not items:
        errors.append("resources/catalog.json must contain a non-empty items list")
        return

    catalog_paths: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"catalog item {index} must be an object")
            continue
        rel_path = item.get("path")
        if not rel_path:
            errors.append(f"catalog item {index} is missing path")
            continue
        catalog_paths.add(rel_path)
        target = ROOT / rel_path
        if not target.exists():
            errors.append(f"catalog path does not exist: {rel_path}")

    for dirname in CATALOGED_DIRS:
        for path in sorted((ROOT / dirname).glob("*.md")):
            if path.name == "README.md":
                continue
            rel = str(path.relative_to(ROOT))
            if rel not in catalog_paths:
                errors.append(f"{rel} is missing from resources/catalog.json")


def validate_guide_metadata(errors: list[str]) -> None:
    for path in sorted((ROOT / "guides").glob("*.md")):
        if path.name == "README.md":
            continue
        fields = parse_front_matter(path)
        missing = REQUIRED_GUIDE_FIELDS.difference(fields)
        if missing:
            rel = path.relative_to(ROOT)
            errors.append(f"{rel} missing front matter fields: {', '.join(sorted(missing))}")


def is_external_link(target: str) -> bool:
    return (
        "://" in target
        or target.startswith("#")
        or target.startswith("mailto:")
        or target.startswith("tel:")
    )


def validate_markdown_links(errors: list[str]) -> None:
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if is_external_link(target):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} links outside repo: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} has broken link: {target}")


def validate_private_patterns(errors: list[str]) -> None:
    for path in markdown_files() + [CATALOG]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)} contains private-looking value: {pattern.pattern}")


def validate_code_fences(errors: list[str]) -> None:
    fence_pattern = re.compile(r"^`{3,}")
    for path in markdown_files():
        fence_count = 0
        for line in path.read_text(encoding="utf-8").splitlines():
            if fence_pattern.match(line):
                fence_count += 1
        if fence_count % 2:
            errors.append(f"{path.relative_to(ROOT)} has an unbalanced code fence")


def main() -> int:
    errors: list[str] = []
    validate_catalog(errors)
    validate_guide_metadata(errors)
    validate_markdown_links(errors)
    validate_private_patterns(errors)
    validate_code_fences(errors)

    if errors:
        for error in errors:
            fail(error)
        return 1

    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
