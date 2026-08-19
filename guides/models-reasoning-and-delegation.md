# Models, Reasoning, And Delegation

Model choice, reasoning effort, and parallelism are separate controls. Use each because the task needs it, not because a higher setting sounds safer.

## Start With The Task Shape

| Task shape | Starting choice |
| --- | --- |
| Narrow, clear, repeatable | Faster model and default or lower reasoning. |
| Ambiguous, multi-step, tool-heavy | Strong general model and higher reasoning when needed. |
| Hard single problem where depth matters most | Max, when supported. |
| Complex work with meaningful independent parts | Ultra or explicit subagents, when supported. |

Available models and controls vary by host, account, and rollout. Keep exact model names in dated references rather than turning them into permanent workflow rules.

## Reasoning Effort

Higher reasoning can improve planning and analysis, but it also takes longer and consumes more usage. Start with the default. Increase effort when the failure mode is shallow analysis, unresolved ambiguity, or a difficult integration decision.

Do not use reasoning effort as a substitute for missing evidence, permissions, tools, or acceptance criteria.

## Max And Ultra

Max gives the selected model more time to reason about one task. Use it when depth matters more than speed or usage.

Ultra goes beyond a single-agent run and uses subagents for separate parts of a complex task. Use it when the work has real parallel structure. Most tasks need neither.

At other reasoning levels, request subagents explicitly when parallel work would materially improve speed, context handling, or review quality.

## Subagent Boundaries

Subagents are a good starting point for read-heavy work such as exploration, testing, triage, and summarization. Parallel write-heavy work creates more conflict and coordination overhead.

Subagent workflows consume more tokens than a comparable single-agent run. The parent remains responsible for boundaries, integration, verification, and the final claim.

When a subagent model or reasoning effort is not set explicitly, local Codex clients can inherit those settings from the parent. Do not assume every host follows the same configuration path.

## Selection Questions

- Is the task hard because it needs deeper reasoning or because it lacks context?
- Can independent work run without overlapping writes?
- Is the expected quality gain worth the additional time and usage?
- Can each delegated result be checked independently?
- Does one focused agent preserve important judgment better than a parallel split?

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [Models](https://learn.chatgpt.com/docs/models) and [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).
