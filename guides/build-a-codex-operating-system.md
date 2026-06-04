# Build A Codex Operating System

Codex gets stronger when the surrounding setup tells it what matters.

That setup does not need to be heavy. Most of the time it is just a few files, a few habits, and one or two checks that stop the agent from wandering off into the bushes.

## The Six Layers

### 1. Task contract

Every non-trivial task needs an outcome, source of truth, constraints, verification, and stop conditions. Without that, Codex can produce effort without proof.

### 2. Context map

Name the context that matters:

- repo files and tests,
- current user instruction,
- official docs,
- live APIs or deployed surfaces,
- issue trackers or planning docs,
- prior memory or decisions.

Also name what does not matter. Excluding stale or adjacent context is part of the job.

### 3. Local instructions

Use project instructions for repo-level defaults: coding style, useful commands, privacy boundaries, browser routes, and release gates. Keep them practical. If a rule applies to only one workflow, make it a checklist or skill instead.

### 4. Tool surface

Give Codex the tools needed for the work: shell, git, browser, GitHub, docs, database, or MCP servers. Start read-only when the state is uncertain. Allow writes only when the source of truth and rollback boundary are clear.

### 5. Verification loop

Define the check before claiming completion. The right check is the one most likely to catch the wrong plausible result.

### 6. Learning layer

Repeated lessons should become reusable artifacts:

- instructions,
- templates,
- validators,
- scripts,
- skills,
- decision records,
- examples.

Do not preserve private one-off detail as a global rule.

## Minimal Setup For A Repo

Start with:

1. `README.md` that names the project and start paths.
2. project instructions with local conventions and checks.
3. one obvious verification command.
4. a task contract template.
5. a fixture, demo, or tiny example if other people need to try it.

That is enough for many projects. Add CI, skills, MCP, and subagents when they remove real friction.

## Failure Modes

- Treating Codex like a generic chatbot instead of a repo-aware worker.
- Adding broad instructions that never get used.
- Giving tool access without source-of-truth clarity.
- Verifying with a command unrelated to the change.
- Capturing every session note as permanent memory.

## Verification

The operating system is working when a new task starts with less explanation, touches fewer unrelated files, and finishes with better proof.
