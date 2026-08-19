# Capability Lifecycle And Prompt Visibility

Having a capability somewhere on disk is not the same as making it useful in a task.

Use this lifecycle:

```mermaid
flowchart LR
  A["Available"] --> B["Installed"]
  B --> C["Enabled"]
  C --> D["Visible or retrievable"]
  D --> E["Activated"]
  E --> F["Used"]
  F --> G["Outcome verified"]
```

## What Each State Means

| State | Meaning |
| --- | --- |
| Available | The capability exists in a marketplace, package, repository, or local library. |
| Installed | Its files or connection are present in the current environment. |
| Enabled | The active host and profile allow it to load. |
| Visible or retrievable | Codex can discover it from prompt-visible metadata or a search route. |
| Activated | The current task explicitly selected it or matched its description. |
| Used | The workflow or tool actually ran. |
| Outcome verified | Evidence supports the result the capability was meant to produce. |

Do not report an installed capability as active, or a successful tool call as a verified outcome.

## Improving A Capability Is A Separate Decision

Verifying one outcome does not prove that a capability should change, become easier to trigger, or gain more access. Treat any reusable change as a separate proposal: isolate it, compare it with the current version, review it, and keep a rollback path.

Permission, tool, connector, and data-access changes need their own review even when the behavior eval passes. A capability becoming more effective is not evidence that it should become more privileged or more visible. See [Verified Improvement Loops](verified-improvement-loops.md) for the full change process.

## Progressive Disclosure

Skills use progressive disclosure. Codex initially sees compact metadata, then loads the full instructions when a skill is selected. A large skill library therefore needs clear names, descriptions, boundaries, and retrieval—not one enormous prompt containing every workflow.

## Router Architecture

A router is a local information architecture, not a special Codex product primitive. It can keep a small set of stable entry points visible while directing tasks to narrower skills only when needed.

A generalized router might expose categories such as:

- engineering delivery,
- research and writing,
- document and spreadsheet production,
- browser and computer interaction,
- connected systems,
- repository operations.

The router should describe when to load a capability and when not to. It should not publish an originating environment's complete inventory, account state, provider configuration, or security controls.

## Profiles Are Overloaded

The word **profile** can refer to different things:

- a model or configuration profile,
- a permission profile,
- an organizational ownership boundary such as personal or work.

Name the kind of profile whenever it matters. Do not assume that choosing a model profile changes permissions, or that a permission profile changes which skills are visible.

## Audit Questions

- Which capabilities are meant to be visible by default?
- Which should be searchable but hidden from the initial prompt?
- Which require explicit invocation?
- Which are enabled only on a particular host or account?
- Which can read data, write data, or trigger external side effects?
- What evidence proves that activation improved the result?
- Which capability descriptions overlap enough to create routing ambiguity?
- Which evals and evidence permit a new version to be adopted?
- Can the prior version be restored without reconstructing private state?

## Safe Public Examples

Public documentation should use generic capability categories and synthetic workflows. Do not publish actual inventories, counts, local paths, server names, enabled integrations, prompt dumps, hook definitions, rules, or authentication routes.

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [Build skills](https://learn.chatgpt.com/docs/build-skills), [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins), and [MCP](https://learn.chatgpt.com/docs/extend/mcp). Availability and host behavior can change.
