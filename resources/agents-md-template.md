# AGENTS.md Template

Use this as a starting point for a project-level Codex instruction file.

````markdown
# AGENTS.md

Version: 0.1.0
Last updated: YYYY-MM-DD
Purpose: Project-level instructions for Codex in this repo.

## Scope

These instructions apply to this repository. Higher-level system and user instructions take precedence.

## Project Intent

<What this repo is for and what good work looks like.>

## Source Of Truth

- Canonical docs:
- Runtime environment:
- Test or validation command:
- Deployment or release target:

## Editing Rules

- Match existing conventions.
- Touch only files needed for the task.
- Do not refactor adjacent code unless required.
- Do not commit secrets, generated caches, local paths, or machine-specific config.

## Verification

Before claiming completion, run:

```bash
<primary validation command>
```

If the command cannot run, explain why.

## Stop Conditions

- Stop before destructive commands.
- Stop before live external writes unless explicitly approved.
- Stop when source of truth conflicts cannot be resolved locally.
````

## Notes

Keep this file short. If a workflow needs detailed steps, link to a guide, runbook, script, or skill instead of expanding this file indefinitely.
