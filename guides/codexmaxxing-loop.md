# The Codexmaxxing Loop

Codex gets much more useful when the work is shaped into a loop instead of a wish.

The loop is simple:

1. Name the outcome.
2. Load the right context.
3. Let Codex make the smallest useful move.
4. Check the real surface.
5. Save the part that will help next time.

## Why It Matters

Agentic work fails when it looks busy but does not move the real system. The loop gives Codex a target, keeps the blast radius sane, and makes "done" mean something.

## Pattern

Treat every non-trivial request as an operating contract:

- What is the intended outcome?
- What evidence would prove it?
- What context is authoritative?
- What would be overkill?
- What should be remembered for next time?

## Workflow

Start by translating the request into an observable result. For code, that might be a passing test, a clean diff, or a browser screenshot. For writing, it might be a sharp outline, a source-backed claim list, or a draft that actually sounds like you.

Then gather only the context needed to act. Read the files, docs, or live surfaces that can change the decision. Skip broad research unless the outcome depends on it.

Make the smallest change that can satisfy the outcome. After that, run the check that would catch the most likely failure.

Close by capturing only reusable learning. A one-off detail does not need to become a permanent rule. A repeated failure mode probably does.

## Tiny Example

Bad shape:

```markdown
Make this repo better.
```

Better shape:

```markdown
Review this repo for the three highest-leverage changes that would make it easier for a new contributor to run locally.

Do not edit yet. Check the README, package scripts, tests, and any fixture/demo path. Return a short plan with the exact files you would change and how you would verify it.
```

## Failure Modes

- Starting with implementation before defining success.
- Reading too widely and losing the task boundary.
- Trusting model confidence instead of a check.
- Turning a simple task into a framework.
- Saving private or stale session detail as if it were reusable knowledge.

## Verification

A good loop leaves you able to answer:

- What changed?
- Why was that the right scope?
- What proof exists?
- What remains unknown?
