#!/usr/bin/env python3
"""Validate public content and repository policy without external dependencies."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = Path("resources/catalog.json")
ASSET_MANIFEST_PATH = Path("assets/review-manifest.json")
WORKFLOW_PATH = Path(".github/workflows/validate.yml")

IGNORED_DIRS = {".git", ".venv", "__pycache__", "node_modules"}
PUBLIC_TEXT_SUFFIXES = {".json", ".md", ".svg", ".toml", ".txt", ".yaml", ".yml"}
CATALOGED_DIRS = {"docs", "guides", "resources"}
CATALOGED_EXTRA_FILES = {Path("examples/README.md")}
KNOWN_CATALOG_TYPES = {
    "checklist",
    "examples",
    "guide",
    "policy",
    "reference",
    "research",
    "template",
}
KNOWN_CATALOG_STATUSES = {"ready", "reference", "usable"}

CURRENT_PRODUCT_DOCUMENTS = {
    Path("docs/product-claim-boundaries.md"),
    Path("guides/artifacts-sites-and-visualizations.md"),
    Path("guides/browser-computer-use-and-connectors.md"),
    Path("guides/capability-lifecycle.md"),
    Path("guides/environments-worktrees-and-cloud.md"),
    Path("guides/models-reasoning-and-delegation.md"),
    Path("guides/permissions-rules-and-hooks.md"),
    Path("guides/projects-chats-goals-and-schedules.md"),
    Path("guides/skills-plugins-mcp-and-tools.md"),
}

ALLOWED_EXTERNAL_HOSTS = {
    "cookbook.openai.com",
    "developers.openai.com",
    "learn.chatgpt.com",
    "metr.org",
    "openai.com",
    "www.anthropic.com",
    "www.swebench.com",
}
NON_FETCHING_URL_EXCEPTIONS = {"http://www.w3.org/2000/svg"}

PRIVATE_PATTERNS = (
    (
        "local home-directory path",
        re.compile(r"(?i)(?:/Users|/home)/[A-Za-z0-9._-]+"),
    ),
    (
        "Windows user-directory path",
        re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\s]+"),
    ),
    (
        "email address",
        re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"),
    ),
    (
        "private IPv4 address",
        re.compile(
            r"\b(?:10(?:\.[0-9]{1,3}){3}|192\.168(?:\.[0-9]{1,3}){2}|"
            r"172\.(?:1[6-9]|2[0-9]|3[01])(?:\.[0-9]{1,3}){2})\b"
        ),
    ),
    (
        "UUID-like identifier",
        re.compile(
            r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-"
            r"[0-9a-f]{4}-[0-9a-f]{12}\b"
        ),
    ),
    (
        "private-key material",
        re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    ),
    (
        "OpenAI-style API key",
        re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{12,}"),
    ),
    (
        "GitHub-style token",
        re.compile(r"(?<![A-Za-z0-9])gh[oprsu]_[A-Za-z0-9_]{20,}"),
    ),
    (
        "AWS-style access key",
        re.compile(r"(?<![A-Z0-9])AKIA[A-Z0-9]{16}(?![A-Z0-9])"),
    ),
    (
        "Slack-style token",
        re.compile(r"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{10,}"),
    ),
    (
        "npm-style token",
        re.compile(r"(?<![A-Za-z0-9])npm_[A-Za-z0-9]{20,}"),
    ),
)

LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
URL_PATTERN = re.compile(r"https?://[^\s<>\"']+")
ISO_DATE_PATTERN = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})")
FULL_SHA_PATTERN = re.compile(r"[0-9a-f]{40}")
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}")


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_ignored(path: Path) -> bool:
    return any(part in IGNORED_DIRS for part in path.parts)


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not is_ignored(path) and not path.is_symlink()
    )


def public_text_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.suffix.lower() in PUBLIC_TEXT_SUFFIXES
        and not is_ignored(path)
    )


def catalogable_paths(root: Path) -> set[str]:
    paths: set[str] = set()
    for dirname in CATALOGED_DIRS:
        for path in sorted((root / dirname).glob("*.md")):
            if path.name != "README.md":
                paths.add(relative(path, root))
    for rel_path in CATALOGED_EXTRA_FILES:
        if (root / rel_path).exists():
            paths.add(rel_path.as_posix())
    return paths


def valid_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def validate_catalog(root: Path, errors: list[str]) -> None:
    catalog_file = root / CATALOG_PATH
    if not catalog_file.exists() or catalog_file.is_symlink():
        errors.append(f"{CATALOG_PATH.as_posix()} is missing")
        return

    try:
        catalog = json.loads(catalog_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"{CATALOG_PATH.as_posix()} is invalid JSON: {exc}")
        return

    if not isinstance(catalog, dict):
        errors.append(f"{CATALOG_PATH.as_posix()} must contain a JSON object")
        return
    if not valid_iso_date(catalog.get("updated")):
        errors.append(f"{CATALOG_PATH.as_posix()} must contain a valid updated date")

    items = catalog.get("items")
    if not isinstance(items, list) or not items:
        errors.append(f"{CATALOG_PATH.as_posix()} must contain a non-empty items list")
        return

    catalog_paths: set[str] = set()
    titles: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"catalog item {index} must be an object")
            continue

        title = item.get("title")
        rel_path = item.get("path")
        item_type = item.get("type")
        status = item.get("status")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"catalog item {index} is missing title")
        elif title in titles:
            errors.append(f"catalog title is duplicated: {title}")
        else:
            titles.add(title)

        if not isinstance(rel_path, str) or not rel_path:
            errors.append(f"catalog item {index} is missing path")
            continue
        rel = Path(rel_path)
        if rel.is_absolute() or ".." in rel.parts:
            errors.append(f"catalog item {index} has an unsafe path")
            continue
        if rel_path in catalog_paths:
            errors.append(f"catalog path is duplicated: {rel_path}")
        catalog_paths.add(rel_path)
        target = root / rel
        if not target.is_file() or target.is_symlink():
            errors.append(f"catalog path does not exist: {rel_path}")

        if item_type not in KNOWN_CATALOG_TYPES:
            errors.append(f"catalog item {index} has unknown type: {item_type}")
        if status not in KNOWN_CATALOG_STATUSES:
            errors.append(f"catalog item {index} has unknown status: {status}")

    for rel_path in sorted(catalogable_paths(root) - catalog_paths):
        errors.append(f"{rel_path} is missing from {CATALOG_PATH.as_posix()}")


def validate_guide_headings(root: Path, errors: list[str]) -> None:
    for path in sorted((root / "guides").glob("*.md")):
        if path.name == "README.md":
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or not lines[0].startswith("# "):
            errors.append(f"{relative(path, root)} must start with an H1")


def is_external_link(target: str) -> bool:
    return (
        "://" in target
        or target.startswith("#")
        or target.startswith("mailto:")
        or target.startswith("tel:")
    )


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    for path in markdown_files(root):
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
                resolved.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{relative(path, root)} links outside the repository")
                continue
            if not resolved.exists():
                errors.append(f"{relative(path, root)} has a broken local link")


def private_pattern_names(text: str) -> list[str]:
    return [name for name, pattern in PRIVATE_PATTERNS if pattern.search(text)]


def validate_public_safety(root: Path, errors: list[str]) -> None:
    for path in public_text_files(root):
        text = path.read_text(encoding="utf-8")
        for name in private_pattern_names(text):
            errors.append(f"{relative(path, root)} contains a prohibited {name}")
        if re.search(r"\baltitude\b", text, re.IGNORECASE):
            errors.append(
                f"{relative(path, root)} uses the retired term 'altitude'; "
                "use 'abstraction level'"
            )

    for path in root.rglob("*"):
        if is_ignored(path):
            continue
        if re.search(r"\baltitude\b", path.name, re.IGNORECASE):
            errors.append(
                f"{relative(path, root)} uses the retired term in a file or directory name"
            )


def normalize_url(raw_url: str) -> str:
    return raw_url.rstrip(".,;:!?)]}")


def external_url_issue(raw_url: str) -> str | None:
    url = normalize_url(raw_url)
    if url in NON_FETCHING_URL_EXCEPTIONS:
        return None
    parsed = urlsplit(url)
    if parsed.scheme != "https":
        return "must use HTTPS"
    if parsed.username or parsed.password:
        return "must not contain embedded credentials"
    hostname = (parsed.hostname or "").lower()
    if hostname not in ALLOWED_EXTERNAL_HOSTS:
        return "uses a host outside the reviewed allowlist"
    return None


def validate_external_urls(root: Path, errors: list[str]) -> None:
    for path in public_text_files(root):
        text = path.read_text(encoding="utf-8")
        for match in URL_PATTERN.finditer(text):
            issue = external_url_issue(match.group(0))
            if issue:
                errors.append(f"{relative(path, root)} contains an external URL that {issue}")


def validate_current_product_sources(root: Path, errors: list[str]) -> None:
    for rel_path in sorted(CURRENT_PRODUCT_DOCUMENTS):
        path = root / rel_path
        if not path.is_file():
            errors.append(f"current-product document is missing: {rel_path.as_posix()}")
            continue
        text = path.read_text(encoding="utf-8")
        if "## Official Sources" not in text:
            errors.append(f"{rel_path.as_posix()} is missing an Official Sources section")
        dates = ISO_DATE_PATTERN.findall(text)
        if not dates or not any(valid_iso_date(value) for value in dates):
            errors.append(f"{rel_path.as_posix()} is missing a valid verification date")
        if "https://learn.chatgpt.com/" not in text:
            errors.append(f"{rel_path.as_posix()} is missing a current official source")


def png_forbidden_chunks(data: bytes) -> set[str]:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("invalid PNG signature")
    forbidden = {b"eXIf", b"iTXt", b"tEXt", b"zTXt"}
    found: set[str] = set()
    offset = 8
    saw_iend = False
    while offset < len(data):
        if offset + 12 > len(data):
            raise ValueError("truncated PNG chunk")
        length = int.from_bytes(data[offset : offset + 4], "big")
        chunk_type = data[offset + 4 : offset + 8]
        end = offset + 12 + length
        if end > len(data):
            raise ValueError("invalid PNG chunk length")
        if chunk_type in forbidden:
            found.add(chunk_type.decode("ascii"))
        offset = end
        if chunk_type == b"IEND":
            saw_iend = True
            break
    if not saw_iend:
        raise ValueError("missing PNG IEND chunk")
    if offset != len(data):
        raise ValueError("trailing data after PNG IEND chunk")
    return found


def webp_forbidden_chunks(data: bytes) -> set[str]:
    if len(data) < 12 or data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        raise ValueError("invalid WebP header")
    declared_size = int.from_bytes(data[4:8], "little") + 8
    if declared_size != len(data):
        raise ValueError("WebP size does not match its RIFF header")
    forbidden = {b"EXIF", b"XMP "}
    found: set[str] = set()
    offset = 12
    while offset + 8 <= declared_size:
        chunk_type = data[offset : offset + 4]
        length = int.from_bytes(data[offset + 4 : offset + 8], "little")
        end = offset + 8 + length
        if end > declared_size:
            raise ValueError("invalid WebP chunk length")
        if chunk_type in forbidden:
            found.add(chunk_type.decode("ascii"))
        offset = end + (length % 2)
    return found


def svg_security_issues(text: str) -> list[str]:
    checks = {
        "document type or entity declaration": r"<!\s*(?:DOCTYPE|ENTITY)\b",
        "embedded metadata": r"<metadata\b",
        "foreign object": r"<foreignObject\b",
        "script content": r"<script\b",
        "event-handler attribute": r"\son[a-z]+\s*=",
        "active or embedded href": r"(?:href|xlink:href)\s*=\s*['\"]\s*(?:javascript:|data:)",
        "external href": r"(?:href|xlink:href)\s*=\s*['\"]\s*https?://",
    }
    return [label for label, pattern in checks.items() if re.search(pattern, text, re.I)]


def validate_asset_metadata(path: Path, errors: list[str], root: Path) -> None:
    rel_path = relative(path, root)
    try:
        data = path.read_bytes()
        if path.suffix.lower() == ".png":
            found = png_forbidden_chunks(data)
            if found:
                errors.append(f"{rel_path} contains prohibited PNG metadata chunks")
        elif path.suffix.lower() == ".webp":
            found = webp_forbidden_chunks(data)
            if found:
                errors.append(f"{rel_path} contains prohibited WebP metadata chunks")
        elif path.suffix.lower() == ".svg":
            issues = svg_security_issues(data.decode("utf-8"))
            for issue in issues:
                errors.append(f"{rel_path} contains prohibited SVG {issue}")
        else:
            errors.append(f"{rel_path} uses an unreviewed asset format")
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        errors.append(f"{rel_path} failed asset inspection: {exc}")


def validate_asset_manifest(root: Path, errors: list[str]) -> None:
    manifest_file = root / ASSET_MANIFEST_PATH
    if not manifest_file.exists() or manifest_file.is_symlink():
        errors.append(f"{ASSET_MANIFEST_PATH.as_posix()} is missing")
        return
    try:
        manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"{ASSET_MANIFEST_PATH.as_posix()} is invalid JSON: {exc}")
        return
    if not isinstance(manifest, dict):
        errors.append(f"{ASSET_MANIFEST_PATH.as_posix()} must contain a JSON object")
        return
    if not valid_iso_date(manifest.get("reviewed_on")):
        errors.append(f"{ASSET_MANIFEST_PATH.as_posix()} needs a valid reviewed_on date")

    items = manifest.get("assets")
    if not isinstance(items, list) or not items:
        errors.append(f"{ASSET_MANIFEST_PATH.as_posix()} must contain reviewed assets")
        return

    manifest_paths: set[str] = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"asset manifest item {index} must be an object")
            continue
        rel_path = item.get("path")
        digest = item.get("sha256")
        checks = item.get("checks")
        if not isinstance(rel_path, str) or not rel_path.startswith("assets/"):
            errors.append(f"asset manifest item {index} has an invalid path")
            continue
        rel = Path(rel_path)
        if rel.is_absolute() or ".." in rel.parts:
            errors.append(f"asset manifest item {index} has an unsafe path")
            continue
        if rel_path in manifest_paths:
            errors.append(f"asset manifest path is duplicated: {rel_path}")
        manifest_paths.add(rel_path)
        asset = root / rel
        if not asset.is_file() or asset.is_symlink():
            errors.append(f"asset manifest path does not exist: {rel_path}")
            continue
        if not isinstance(digest, str) or not SHA256_PATTERN.fullmatch(digest):
            errors.append(f"asset manifest item {index} has an invalid SHA-256")
        else:
            actual_digest = hashlib.sha256(asset.read_bytes()).hexdigest()
            if digest != actual_digest:
                errors.append(f"{rel_path} changed after its recorded review")
        if not isinstance(checks, list) or set(checks) != {"metadata", "privacy", "visual"}:
            errors.append(
                f"asset manifest item {index} must record metadata, privacy, and visual checks"
            )
        validate_asset_metadata(asset, errors, root)

    assets_dir = root / "assets"
    if not assets_dir.is_dir():
        errors.append("assets directory is missing")
        return
    actual_paths = {
        relative(path, root)
        for path in assets_dir.rglob("*")
        if path.is_file() and path != manifest_file
    }
    for rel_path in sorted(actual_paths - manifest_paths):
        errors.append(f"{rel_path} is missing from {ASSET_MANIFEST_PATH.as_posix()}")
    for rel_path in sorted(manifest_paths - actual_paths):
        errors.append(f"{rel_path} is stale in {ASSET_MANIFEST_PATH.as_posix()}")


def is_pinned_action_reference(reference: str) -> bool:
    if reference.startswith("./"):
        return True
    if "@" not in reference:
        return False
    return bool(FULL_SHA_PATTERN.fullmatch(reference.rsplit("@", 1)[1]))


def top_level_block(text: str, key: str) -> list[str] | None:
    lines = text.splitlines()
    target = f"{key}:"
    for index, line in enumerate(lines):
        if line != target:
            continue
        block: list[str] = []
        for candidate in lines[index + 1 :]:
            if not candidate.strip():
                continue
            if not candidate.startswith((" ", "\t")):
                break
            block.append(candidate.strip())
        return block
    return None


def workflow_job_blocks(text: str) -> dict[str, str]:
    lines = text.splitlines()
    try:
        jobs_index = lines.index("jobs:")
    except ValueError:
        return {}
    job_starts: list[tuple[int, str]] = []
    for index in range(jobs_index + 1, len(lines)):
        line = lines[index]
        if line and not line.startswith((" ", "\t")):
            break
        match = re.fullmatch(r"  ([A-Za-z0-9_-]+):\s*", line)
        if match:
            job_starts.append((index, match.group(1)))
    blocks: dict[str, str] = {}
    for offset, (start, name) in enumerate(job_starts):
        end = job_starts[offset + 1][0] if offset + 1 < len(job_starts) else len(lines)
        blocks[name] = "\n".join(lines[start:end])
    return blocks


def validate_workflow_policy(root: Path, errors: list[str]) -> None:
    path = root / WORKFLOW_PATH
    if not path.is_file() or path.is_symlink():
        errors.append(f"{WORKFLOW_PATH.as_posix()} is missing")
        return
    text = path.read_text(encoding="utf-8")
    if top_level_block(text, "permissions") != ["contents: read"]:
        errors.append(
            f"{WORKFLOW_PATH.as_posix()} must grant only top-level contents: read"
        )

    job_blocks = workflow_job_blocks(text)
    if not job_blocks:
        errors.append(f"{WORKFLOW_PATH.as_posix()} must declare at least one job")
    for job_name, block in job_blocks.items():
        if not re.search(r"(?m)^    runs-on:\s*ubuntu-24\.04\s*$", block):
            errors.append(
                f"{WORKFLOW_PATH.as_posix()} job {job_name} must use the reviewed runner image"
            )
        timeout_match = re.search(r"(?m)^    timeout-minutes:\s*(\d+)\s*$", block)
        if not timeout_match:
            errors.append(
                f"{WORKFLOW_PATH.as_posix()} job {job_name} must set a timeout"
            )
        elif int(timeout_match.group(1)) > 15:
            errors.append(
                f"{WORKFLOW_PATH.as_posix()} job {job_name} timeout must be 15 minutes or less"
            )
    if "pull_request_target" in text:
        errors.append(f"{WORKFLOW_PATH.as_posix()} must not use pull_request_target")
    if re.search(r"\bsecrets?\b", text, re.IGNORECASE):
        errors.append(f"{WORKFLOW_PATH.as_posix()} must not consume repository secrets")

    references = re.findall(r"(?m)^[ \t]*-[ \t]+uses:[ \t]*([^\s#]+)", text)
    if not references:
        errors.append(f"{WORKFLOW_PATH.as_posix()} must declare its actions explicitly")
    for reference in references:
        if not is_pinned_action_reference(reference):
            errors.append(
                f"{WORKFLOW_PATH.as_posix()} uses an action without an immutable SHA pin"
            )

    checkout_match = re.search(
        r"(?m)^[ \t]*-[ \t]+uses:[ \t]*actions/checkout@[0-9a-f]{40}[^\n]*$",
        text,
    )
    if not checkout_match:
        errors.append(f"{WORKFLOW_PATH.as_posix()} must use a pinned checkout action")
    else:
        next_step = re.search(r"(?m)^ {6}-[ \t]+", text[checkout_match.end() :])
        block_end = (
            checkout_match.end() + next_step.start() if next_step else len(text)
        )
        checkout_block = text[checkout_match.start() : block_end]
        if "persist-credentials: false" not in checkout_block:
            errors.append(
                f"{WORKFLOW_PATH.as_posix()} must disable persisted checkout credentials"
            )


def validate_code_fences(root: Path, errors: list[str]) -> None:
    for path in markdown_files(root):
        active_fence: str | None = None
        for line in path.read_text(encoding="utf-8").splitlines():
            match = FENCE_PATTERN.match(line)
            if not match:
                continue
            marker = match.group(1)[0]
            if active_fence is None:
                active_fence = marker
            elif active_fence == marker:
                active_fence = None
        if active_fence is not None:
            errors.append(f"{relative(path, root)} has an unbalanced code fence")


def validate_no_symlinks(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if not is_ignored(path) and path.is_symlink():
            errors.append(f"{relative(path, root)} is a prohibited symbolic link")


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    validate_no_symlinks(root, errors)
    validate_catalog(root, errors)
    validate_guide_headings(root, errors)
    validate_markdown_links(root, errors)
    validate_public_safety(root, errors)
    validate_external_urls(root, errors)
    validate_current_product_sources(root, errors)
    validate_asset_manifest(root, errors)
    validate_workflow_policy(root, errors)
    validate_code_fences(root, errors)
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        for error in errors:
            fail(error)
        return 1

    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
