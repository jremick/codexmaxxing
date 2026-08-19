# Permissions, Rules, Hooks, And Instructions

These controls operate at different layers. Combining them into one idea called "safety" creates false confidence.

## Permission Layers

- The **sandbox** defines which filesystem and network resources local commands can access.
- **Approvals** define when Codex pauses before an action or routes it for review.
- **App and connector approvals** govern tool calls outside ordinary shell execution.
- **Operating-system permissions** govern capabilities such as screen and accessibility access.

Changing who reviews an approval does not expand the sandbox. Start with the narrowest mode that permits the task.

## Project Instructions

`AGENTS.md` supplies durable instructions. Codex builds an instruction chain from broader scope toward the current working directory, with closer project guidance taking precedence.

Keep repository instructions short and public-safe. Put detailed procedures in guides, skills, or scripts. Treat changes to instruction files as behavior changes, not ordinary prose edits.

## Rules

Rules control how matching commands are handled outside the sandbox. Decisions can allow, prompt, or forbid an invocation, with the most restrictive matching decision winning.

Rules are experimental. Test them with their supported checker and do not describe them as a complete security boundary.

## Hooks

Hooks run executable logic at lifecycle events. Multiple matching hooks can run, and some run concurrently. Non-managed hooks require review and trust; changed hook definitions require renewed review.

Hooks can inspect or influence tool activity, but they also create code-execution and data-exposure risk. Avoid secrets in hook output and do not publish an actual environment's hook definitions.

## What Each Layer Is Good At

| Need | Prefer |
| --- | --- |
| Durable repository expectations | Project instructions |
| Filesystem and network boundary | Sandbox or permission profile |
| Human or automatic review point | Approval policy |
| Deterministic command decision | Rule |
| Lifecycle automation or policy check | Hook |
| Repeatable task workflow | Skill |

## Safety Review

Before enabling a new control:

- identify who owns it,
- inspect its source,
- define the exact scope,
- test expected allow and deny cases,
- check what data it can read or emit,
- confirm how it fails,
- keep a recovery path.

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [Permissions](https://learn.chatgpt.com/docs/permission-modes), [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security), [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules), and [Hooks](https://learn.chatgpt.com/docs/hooks).
