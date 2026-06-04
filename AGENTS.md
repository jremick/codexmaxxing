# AGENTS.md

Version: 0.1.0
Last updated: 2026-06-04
Purpose: Project-level instructions for Codexmaxxing publishing work.

## Scope

These instructions apply to this repository. Higher-level system, runtime, and user instructions still take precedence.

## Project Intent

Codexmaxxing is a private-first source repo for publishing practical Codex and agentic-working guidance. Treat the repo as a content product, not a scratch note dump.

## Editing Defaults

- Keep content Markdown-first unless the user asks for another publishing surface.
- Prefer durable working patterns over fragile product-feature claims.
- When writing about current Codex, OpenAI APIs, SDKs, or model behavior, verify against current official docs before making specific claims.
- Keep examples generic and portable. Do not include local usernames, home paths, private hostnames, client names, tokens, credentials, or machine-specific auth flows.
- Do not add a static site generator, package manager, or build stack unless a concrete publishing target requires it.
- Preserve the content taxonomy unless the user explicitly asks to reshape it:
  - `guides/` for narrative guides and playbooks.
  - `resources/` for checklists, templates, and reference material.
  - `docs/` for project planning and publishing notes.

## Quality Bar

- Every guide should name the reader, the problem, the operating pattern, and the verification loop.
- Every checklist or template should be immediately usable without private context.
- Avoid advice that cannot be tested, demonstrated, or reviewed.
- If a piece depends on current product behavior, include a clear "verified against" note with the exact date and source.

## Verification

Before claiming the repo is ready or publishable:

```bash
python3 scripts/validate_content.py
```

Also inspect the diff for private details before any public release.
