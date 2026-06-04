# Codexmaxxing

Codexmaxxing is a private-first publishing project for practical guides, templates, and operating patterns about getting more value from Codex in AI-assisted and agentic work.

The focus is not prompt trivia. The focus is turning Codex into a reliable working surface: clear task framing, context control, verification, delegation, repo hygiene, and repeatable feedback loops.

## Start Here

- [Guides index](guides/README.md): narrative guides and durable working patterns.
- [Resources index](resources/README.md): checklists, templates, and reusable field notes.
- [Publishing plan](docs/publishing-plan.md): scope, audience, and release shape.
- [Project instructions](AGENTS.md): how Codex should work in this repo.

## Content Principles

- Make claims operational: every guide should help someone do a task better.
- Prefer examples that are portable across teams, machines, and repos.
- Separate current product behavior from durable agentic-working principles.
- Keep private systems, client details, local paths, secrets, and auth flows out of publishable material.
- Add verification steps wherever a reader would otherwise rely on trust.

## Repo Layout

```text
guides/       Long-form guides and playbooks.
resources/    Checklists, templates, and reference material.
docs/         Project planning and publishing notes.
scripts/      Local validation utilities.
```

## Local Validation

Run the content checks before committing:

```bash
python3 scripts/validate_content.py
```

The validator checks internal Markdown links, catalog paths, required guide metadata, and obvious private-path leakage.

## Status

This repo is private while the first content set is shaped. Licensing and public release packaging are intentionally undecided until the publication surface is clearer.
