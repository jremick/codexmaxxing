# The Codexmaxxing Loop

Codex gets much more useful when the work has a clear outcome and a real check at the end.

Most work does not need a framework. Start with the simple loop, then make parts reusable only when the work is likely to happen again.

The loop is simple:

1. Name the outcome.
2. Define what success looks like.
3. Let Codex derive the approach.
4. Give it the right context and tools.
5. Check the actual result.
6. Keep anything that will genuinely help next time.

## When The Work Repeats

Recurring work adds two more questions:

| Loop | Question |
| --- | --- |
| Do the work | Was the requested result produced? |
| Check the work | Does the evidence support that claim? |
| Improve the workflow | Should anything change for future runs? |

Keep those questions separate. A workaround that helped once should not quietly become a global rule, and the system's own confidence is not independent evidence. If the workflow is genuinely recurring, see [Verified Improvement Loops](verified-improvement-loops.md).

## Why It Matters

Agentic work fails when it looks busy but does not move the real system. The loop gives Codex a target, keeps the blast radius sane, and makes "done" mean something.

## Pattern

For non-trivial work, make sure these questions have answers. You do not need to turn them into a form every time.

- What is the intended outcome?
- What evidence would prove it?
- What context is authoritative?
- What would be overkill?
- What should be remembered for next time?

If those answers are clear enough, Codex can usually work out the plan and verification path itself.

## Workflow

Start by translating the request into an observable result. For code, that might be a passing test, a clean diff, or a browser inspection. For writing, it might be a sharp outline, a source-backed claim list, or a draft that matches the intended voice.

Then gather only the context needed to act. Read the files, documents, APIs, or live systems that can change the decision. Skip broad research unless the outcome depends on it.

Make the smallest change that can satisfy the outcome. After that, run the check that would catch the most likely failure.

Close by keeping only what will actually help later. A one-off detail does not need to become a permanent rule. If the same failure keeps returning, turn it into a check and test the smallest workflow change before making that change the new default.

## Tiny Example

Bad shape:

```markdown
Make this repo better.
```

Better shape, but still at a relatively low abstraction level:

```markdown
Review this repo for the three highest-leverage changes that would make it easier for a new contributor to run locally.

Do not edit yet. Check the README, package scripts, tests, and any fixture/demo path. Return a short plan with the exact files you would change and how you would verify it.
```

Higher-abstraction version:

```markdown
Make this repo easier for a new contributor to understand, run, and trust.

Success criteria:
- the first-click path is obvious,
- the local run path is clear,
- private setup is not required for a basic demo,
- the verification path is named,
- the README feels like a real project, not a notes folder.

Work out the plan and checks before editing.
```

## Failure Modes

- Starting with implementation before defining success.
- Reading too widely and losing the task boundary.
- Trusting model confidence instead of a check.
- Turning a simple task into a framework.
- Saving private or stale session detail as if it were reusable knowledge.
- Editing the active workflow in place while using the same run to judge the change.
- Calling a repeated loop "self-improving" without versioning, comparable evals, or rollback.

## Verification

A good loop leaves you able to answer:

- What changed?
- Why was that the right scope?
- What evidence exists?
- What remains unknown?
