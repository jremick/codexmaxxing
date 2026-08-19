# Skills, Plugins, MCP, And Tools

These surfaces solve different reuse and integration problems. Use the smallest layer that changes behavior reliably.

## The Layers

### Instructions

Use project instructions for stable rules that should apply whenever Codex works in a repository: conventions, privacy boundaries, important commands, and verification expectations.

### Briefs And Checklists

Use a Markdown resource when the workflow still needs human judgment and does not need automatic routing or code.

### Scripts And Validators

Use code for exact repeatable work such as parsing, schema checks, link validation, sorting, and release gates.

### Skills

A skill packages instructions and supporting resources for a repeatable task or workflow. It can include templates, examples, schemas, and helper scripts.

Skills use progressive disclosure: compact metadata helps Codex decide when a skill applies, and the full instructions load only when selected. Clear descriptions and boundaries matter more than a large flat inventory.

### Plugins

A plugin is an installable bundle. It can contain skills, connectors backed by MCP, and optional custom UI.

Use a plugin when a capability needs installation, distribution, connected tools, or a shared product surface. Installing a plugin does not mean every bundled capability should be enabled or trusted automatically.

### MCP And Connectors

MCP connects models to structured tools and context. Local Codex clients can connect directly to configured MCP servers; hosted surfaces commonly receive MCP-backed tools through plugins.

Use tool allowlists and approval policies appropriate to the server. Prefer read-only tools for discovery and require review for writes or consequential actions.

### Scheduled Tasks

Use scheduled tasks when time or recurrence is part of the requirement. Put the reusable method in a skill when the scheduled prompt would otherwise duplicate a complex workflow.

## Selection Rule

| Need | Smallest useful layer |
| --- | --- |
| Stable repository rule | Project instruction |
| Human-guided reusable shape | Checklist or template |
| Exact deterministic operation | Script or validator |
| Reusable workflow expertise | Skill |
| Installable bundle or connected capability | Plugin |
| Structured external tools or context | MCP connector |
| Recurring execution | Scheduled task, often invoking a skill |

## Capability State

Do not confuse availability with use. A capability can be available, installed, enabled, visible or retrievable, activated, used, and finally verified. See [Capability Lifecycle And Prompt Visibility](capability-lifecycle.md).

## Security Boundary

- Inspect a plugin's manifest, skills, connectors, and hooks before enabling it.
- Treat third-party tool output as untrusted input.
- Do not put credentials in skills, prompts, examples, or repository configuration.
- Use the narrowest tool set and approval policy that supports the task.
- Read back external writes from the authoritative system.
- Do not publish an actual environment's inventory, endpoints, auth route, or security controls.

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins), [Build skills](https://learn.chatgpt.com/docs/build-skills), [Build plugins](https://learn.chatgpt.com/docs/build-plugins), [MCP](https://learn.chatgpt.com/docs/extend/mcp), and [Scheduled tasks](https://learn.chatgpt.com/docs/automations).
