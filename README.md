# Codexmaxxing

Codexmaxxing is a practical resource for getting more value from Codex in AI-assisted and agentic work.

The point is not clever prompts. The point is engineering the work surface around Codex: clear task contracts, trusted context, useful instructions, tool access, verification loops, delegation boundaries, and durable learning.

## Start Here

- [Guides index](guides/README.md): narrative guides and durable working patterns.
- [Resources index](resources/README.md): checklists, templates, and reusable field notes.
- [Research synthesis](docs/research-synthesis.md): current source-backed findings behind the repo.
- [Field synthesis](docs/field-synthesis.md): public-safe patterns from personal and work usage.
- [Publishing plan](docs/publishing-plan.md): scope, audience, and release shape.
- [Project instructions](AGENTS.md): how Codex should work in this repo.

## Core Framework

Codexmaxxing treats Codex as an operating loop:

1. Frame the task as an outcome with proof.
2. Load the smallest authoritative context set.
3. Give Codex the right instructions, tools, and boundaries.
4. Let it act in the real work surface.
5. Verify against the outcome, not against vibes.
6. Preserve reusable learning without leaking private detail.

That loop applies to code, docs, research, ops, hardware, internal enablement, and public artifact work.

## Content Principles

- Make claims operational: every guide should help someone do a task better.
- Prefer examples that are portable across teams, machines, and repos.
- Separate current product behavior from durable agentic-working principles.
- Keep private systems, client details, local paths, secrets, and auth flows out of publishable material.
- Add verification steps wherever a reader would otherwise rely on trust.
- Verify current Codex product claims against official OpenAI documentation before publishing.

## Repo Layout

```text
guides/       Long-form guides and playbooks.
resources/    Checklists, templates, and reference material.
docs/         Project planning and publishing notes.
scripts/      Local validation utilities.
.github/      Repository validation workflow.
```

## Local Validation

Run the content checks before committing:

```bash
python3 scripts/validate_content.py
```

The validator checks internal Markdown links, catalog paths, required guide metadata, and obvious private-path leakage.

## Status

This repo is private while the first content set is shaped. Licensing, public release packaging, and site shape are intentionally undecided until the publication surface is clearer.
