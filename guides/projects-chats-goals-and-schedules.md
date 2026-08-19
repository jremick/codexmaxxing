# Projects, Chats, Goals, And Scheduled Tasks

These surfaces organize different kinds of continuity. They should not be treated as interchangeable names for one agent run.

## Core Terms

| Surface | Use it for |
| --- | --- |
| Project | Related chats, files, instructions, and sources that should share context over time. |
| Chat | One conversation and execution history. Product interfaces and tools may also call it a task or thread. |
| Goal | A completion-oriented outcome inside one chat. |
| Scheduled task | A recurring or delayed invocation with its own cadence and run history. |

Use a standalone chat for self-contained work. Use a project when several chats need the same sources or instructions.

## Plan Before Goal

Use planning when the outcome, constraints, or success criteria still need to be discovered. Start a goal when the result can be stated clearly enough for Codex to decide whether it is complete.

```markdown
Outcome:
<what should be true>

Constraints:
<scope, permissions, privacy, compatibility>

Definition of done:
<observable checks>
```

A goal does not broaden permissions. Keep steering and status questions in the same chat so the goal retains its context.

## When To Use Separate Chats

Use separate chats when workstreams are independent. Do not give two chats overlapping write access to the same source unless an explicit integration process owns the conflict risk.

Related chats can stay in one project without sharing a single execution history.

## Scheduled Tasks

Use a scheduled task when time or recurrence is part of the requirement:

- a one-time follow-up,
- a recurring review,
- a monitor with a stop condition,
- a skill-driven maintenance workflow.

Test the prompt manually first. Review the first few runs before trusting unattended behavior.

Recurrence alone does not make a workflow compounding. A schedule repeats the work; the workflow compounds only when evidence leads to a reviewed, testable improvement in later runs.

Local scheduled tasks need the computer and desktop app running when they depend on local files. In Git repositories, an isolated worktree can keep scheduled changes away from active work. Web scheduled tasks can use uploaded context and connected tools, but cannot directly operate on a folder on a local computer. The CLI can help prepare a workflow but does not provide the Scheduled management interface.

## Standalone Or Same-Chat Schedule

- Use a standalone scheduled task when each run should start independently.
- Schedule inside an existing chat when later runs need that chat's context.
- Put durable behavior in the saved prompt or an explicit skill rather than relying on incidental conversation history.

## Safety Checks

- Use the narrowest permissions that let an unattended run succeed.
- Prefer worktree isolation for recurring writers in Git repositories.
- Define what should be reported, ignored, retried, or escalated.
- Include a stop condition for monitors and follow-up loops.
- Never assume recurrence grants authority for new side effects.

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [Projects and chats](https://learn.chatgpt.com/docs/projects), [Long-running work](https://learn.chatgpt.com/docs/long-running-work), and [Scheduled tasks](https://learn.chatgpt.com/docs/automations).
