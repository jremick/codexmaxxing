# Delegation And Subagents

Subagents are great when the split is real.

They are annoying when they create three summaries of the same problem and now you have to manage a tiny meeting.

Thinking altitude changes delegation. At high altitude, Codex may first design the work breakdown, then decide whether subagents are useful. You do not always need to specify the subagent plan up front.

For larger parallel setups, treat this as an [agentic harness topology](parallel-projects-and-agent-teams.md) problem: choose the shape, define the status contracts, then delegate.

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
Mission:
Source of truth:
Allowed files or systems:
Do not touch:
Expected output:
Verification:
Stop condition:
```

Or, one level higher:

```markdown
Goal:
Success criteria:
Constraints:

Decide whether delegation helps. If it does, define the subtask boundaries and verification checks before spawning or assigning work.
```

For code edits, give clear file ownership and remind agents not to revert unrelated work.

## Integration Is The Parent's Job

Delegation does not remove responsibility. The main thread still has to review results, resolve conflicts, verify the integrated state, and explain what happened.

## Failure Modes

- Delegating the immediate blocker and waiting anyway.
- Asking two agents to inspect the same surface.
- Accepting a subagent summary without checking fit.
- Splitting work by role name instead of by ownership boundary.
- Letting delegated agents write overlapping files.

## Verification

Delegation worked when it shortened the path to evidence or improved review quality without making integration worse.
