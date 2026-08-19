# Local, Worktree, And Cloud Environments

Environment choice determines where files, commands, and state live. It is separate from model choice and separate from whether subagents are used.

## Choose The Environment

| Environment | Best fit | Main risk |
| --- | --- | --- |
| Local | Foreground work that should affect the selected project directory directly. | Changes can overlap with active human work. |
| Worktree | Parallel or background Git work that needs filesystem isolation. | Shared Git metadata and later integration still need care. |
| Cloud | Remote, reproducible, or longer-running work in an isolated configured environment. | The remote environment may differ from the local one. |

Local and Worktree chats run on the computer or development environment containing the project. Cloud work runs remotely.

## Worktrees Are Filesystem Isolation

A worktree is another checkout of the same Git repository, not another type of agent. Worktrees share repository metadata while keeping file changes separate.

Useful cases include:

- independent writers working in parallel,
- background tasks that should not disturb the main checkout,
- scheduled Git work that needs isolation,
- comparing alternative implementations.

Desktop-created worktrees normally begin at a detached `HEAD`. Review the diff and decide how the work should be integrated before treating it as merged. Handoff can move a chat and its code between Local and Worktree.

## Cloud Is A Separate Runtime

Cloud tasks run in isolated configured environments and can continue in parallel. Configure the dependencies, tools, variables, and setup steps the task actually needs.

Review the resulting summary and diff before opening or merging a pull request. A successful cloud run does not prove that a different local or deployed environment behaves the same way.

## Choosing Between Parallel Surfaces

- Use subagents for bounded, independent reasoning or read-heavy work inside one objective.
- Use separate chats with worktrees for independent writers in the same Git repository.
- Use Cloud when work should run remotely or needs a reproducible configured environment.
- Use Local when tight foreground interaction with the current checkout matters most.

## Verification

Always label the state being reported:

- local source,
- worktree source,
- remote branch,
- merged branch,
- deployed runtime,
- released artifact.

One state does not imply the next.

## Official Sources

Product behavior in this guide was checked on 2026-08-20 against [environment modes](https://learn.chatgpt.com/docs/environments/modes), [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees), and [Codex cloud](https://learn.chatgpt.com/docs/cloud).
