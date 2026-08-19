# The Codexmaxxing Loop

Codex gets much more useful when the work is shaped into a loop instead of a wish.

At a low abstraction level, that loop can be a task. At a higher abstraction level, it can initialize a persistent harness or orchestration system.

The loop is simple:

1. Name the outcome.
2. Define what success looks like.
3. Let Codex derive the approach.
4. Give it the right context and tools.
5. Check the real surface.
6. Propose the part that should help next time.
7. Promote it only after comparable verification.

## Three Nested Loops

The simple loop contains three different control cycles:

| Loop | Question |
| --- | --- |
| Execution | Was the requested result produced? |
| Verification | Does evidence support the completion claim? |
| Evolution | Should anything about the harness change for future runs? |

Keeping them separate prevents a task-local workaround from becoming a global rule and prevents the system from treating its own confidence as independent evidence. See [Verified Improvement Loops](verified-improvement-loops.md).

## Why It Matters

Agentic work fails when it looks busy but does not move the real system. The loop gives Codex a target, keeps the blast radius sane, and makes "done" mean something.

## Pattern

Treat every non-trivial request as an operating contract, but do not assume you have to handwrite the whole contract yourself.

- What is the intended outcome?
- What evidence would prove it?
- What context is authoritative?
- What would be overkill?
- What should be remembered for next time?

If those answers are clear enough, Codex can usually draft the task contract, plan, delivery slices, and verification path itself.

## Workflow

Start by translating the request into an observable result. For code, that might be a passing test, a clean diff, or a browser inspection. For writing, it might be a sharp outline, a source-backed claim list, or a draft that matches the intended voice.

Then gather only the context needed to act. Read the files, docs, or live surfaces that can change the decision. Skip broad research unless the outcome depends on it.

Make the smallest change that can satisfy the outcome. After that, run the check that would catch the most likely failure.

Close by classifying reusable learning. A one-off detail does not need to become a permanent rule. A repeated failure mode may deserve an eval and a candidate harness change, but promotion still requires review and regression evidence.

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

Derive the task contract and plan before editing.
```

## Failure Modes

- Starting with implementation before defining success.
- Reading too widely and losing the task boundary.
- Trusting model confidence instead of a check.
- Turning a simple task into a framework.
- Saving private or stale session detail as if it were reusable knowledge.
- Editing the active harness in place while using the same run to judge the change.
- Calling a repeated loop "self-improving" without versioning, comparable evals, or rollback.

## Verification

A good loop leaves you able to answer:

- What changed?
- Why was that the right scope?
- What proof exists?
- What remains unknown?
