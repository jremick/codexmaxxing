# Codexmaxxing

Using Codex less like a chatbot and more like an agentic operating system.

Codexmaxxing is my field guide for getting real work done with Codex: apps, firmware, docs, ops, writing, research, repo cleanup, weird little side quests, and the occasional "why is this thing broken at 11pm?" investigation.

The big unlock is altitude. With a strong enough model, the useful move is often not "write a better tiny task." It is "hold the goal at the right level, make success clear, and let Codex design the harness underneath it."

![Codexmaxxing agentic operating system workbench](assets/codexmaxxing-hero.webp)

## Start Here

- [The Codexmaxxing Loop](guides/codexmaxxing-loop.md): the basic loop I keep coming back to.
- [Thinking Altitude](guides/thinking-altitude.md): the biggest unlock: giving Codex bigger goals at the right level.
- [Task Framing For Agents](guides/task-framing.md): how to stop asking vague stuff and start getting useful work back.
- [Context Control](guides/context-control.md): how to stop drowning Codex in the wrong information.
- [Parallel Projects And Agent Teams](guides/parallel-projects-and-agent-teams.md): how to run multiple threads without losing the plot.
- [Verification Before Completion](guides/verification-before-completion.md): the part that turns "seems fine" into "actually done."
- [Example Missions](examples/README.md): a few shapes for real work, including non-code work.
- [Related Projects](docs/related-projects.md): real repos where these ideas show up.

## The Shape Of It

```mermaid
flowchart LR
  A["High-level goal"] --> B["Success criteria"]
  B --> C["Codex designs the harness"]
  C --> D["Tools + context"]
  D --> E["Real execution"]
  E --> F["Real checks"]
  F --> G["Reusable pattern"]
```

That loop works for code, but it is not just a coding thing.

I use the same pattern for:

- turning broad ideas into product-shaped side projects,
- debugging live systems,
- turning messy notes into useful docs,
- researching gear or APIs,
- shaping open-source repos,
- reviewing UI,
- making tiny scripts that replace annoying repeated thinking,
- and generally moving more work out of my head and into a repeatable loop.

## The Fun Part

The fun bit is when Codex stops being a novelty and starts becoming part of the bench:

- a repo has instructions that actually help,
- a goal has success criteria,
- Codex can derive the task contract instead of waiting for me to handwrite every field,
- parallel projects have status contracts instead of vibes,
- a tool call reads the live thing instead of guessing,
- a test or screenshot catches the dumb mistake,
- a repeated workflow turns into a reusable playbook,
- and suddenly the agent can do more than autocomplete code.

This repo is a mix of notes, patterns, templates, and examples for that.

## Grab A Thing

| If you want to... | Start with |
| --- | --- |
| think bigger without going vague | [Thinking Altitude](guides/thinking-altitude.md) |
| get better answers from Codex | [Task Framing For Agents](guides/task-framing.md) |
| stop context chaos | [Context Control](guides/context-control.md) |
| build a repeatable setup around a repo | [Build A Codex Operating System](guides/build-a-codex-operating-system.md) |
| run multiple projects or agents at once | [Parallel Projects And Agent Teams](guides/parallel-projects-and-agent-teams.md) |
| use tools, skills, and MCP without making a mess | [Tools, Skills, And MCP](guides/tools-skills-and-mcp.md) |
| split work across agents without making it worse | [Delegation And Subagents](guides/delegation-and-subagents.md) |
| bring this into a team | [Team Adoption](guides/team-adoption.md) |
| copy a template and go | [Copy-Paste Bits](resources/README.md) |
| see what this looks like in practice | [Example Missions](examples/README.md) |

## Real-World-ish Examples

- [Moodarr](https://github.com/jremick/moodarr): helps Plex + Seerr/Jellyseerr users find something to watch from moods, vibes, and loose natural-language ideas.
- [DragyDash](https://github.com/jremick/dragy-dash): turns Dragy Pro GNSS data into a live iPhone dashboard for speed runs, GPS quality, and session telemetry.
- [DragyDash ESP32](https://github.com/jremick/dragy-dash-esp32): puts Dragy Pro speed and GPS quality on a tiny LilyGO display so the useful telemetry is glanceable.
- [AI Workbench](https://github.com/jremick/ai-workbench): a workbench of reusable AI skills, prompts, harnesses, memory patterns, and agent workflow bits.
- [AI Skills Share](https://github.com/jremick/ai-skills-share): a place to publish, review, discover, install, and use agent skills across web, API, CLI, and MCP.

More notes on those are in [Related Projects](docs/related-projects.md).

## License

[Apache License 2.0](LICENSE) - Copyright 2026 Jarel Remick.
