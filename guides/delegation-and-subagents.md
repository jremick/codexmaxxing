---
title: Delegation And Subagents
status: draft
audience: Codex users deciding when to split work across agents
updated: 2026-06-04
verified_against: OpenAI Codex docs on 2026-06-04
---

# Delegation And Subagents

Subagents help when the split is real. They hurt when they duplicate the main agent's judgment loop.

## Delegate When

- Independent questions can be answered in parallel.
- Different agents can own disjoint files or modules.
- A verifier can review while implementation continues.
- A research thread can gather sources while the main thread builds.
- A specialist can summarize a large surface into a bounded result.

## Keep It Local When

- The next step is blocked on the answer.
- The work is tightly coupled.
- The task is small.
- The risk is in integration judgment, not raw throughput.
- The delegated scope cannot be stated precisely.

## Good Delegation Brief

```markdown
Task:
Source of truth:
Allowed files or systems:
Do not touch:
Expected output:
Verification:
Stop condition:
```

For code edits, give clear file ownership and remind agents not to revert unrelated work.

## Integration Is The Parent's Job

Delegation does not remove responsibility. The parent agent must review results, resolve conflicts, verify the integrated state, and write the final answer.

## Failure Modes

- Delegating the immediate blocker and waiting anyway.
- Asking two agents to inspect the same surface.
- Accepting a subagent summary without checking fit.
- Splitting work by role name instead of by ownership boundary.
- Letting delegated agents write overlapping files.

## Verification

Delegation worked when it shortened the path to evidence or improved review quality without increasing merge risk.
