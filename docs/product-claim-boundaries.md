# Product Claim Boundaries

Codex changes quickly. Product claims in this repository should be dated, linked to current official documentation, and scoped to the surface being described.

## Surface Matters

ChatGPT on the web, the desktop app, Codex CLI, and the IDE extension do not expose identical controls or previews. Account, plan, workspace policy, operating system, and rollout state can also affect availability.

Do not turn one observed environment into a universal product claim.

## Evidence Must Match The Claim

| Claim | Supporting evidence |
| --- | --- |
| Source changed | Diff plus intended-file read-back |
| Remote branch changed | Live remote read-back |
| Service state changed | Authoritative API or control-plane read-back |
| Page rendered | Browser inspection or screenshot |
| Workflow completed end to end | Evidence across the actual input and output path |
| Artifact is reviewable | Open or render it in an appropriate viewer |
| Site is live | Deployment read-back plus the production URL |

A screenshot cannot establish backend mutation, identity, accessibility conformance, or end-to-end delivery by itself. An API response cannot establish visual quality.

## Security Claims

- Sandbox boundaries and approval policy are separate controls.
- Command network restrictions do not automatically govern Browser, Computer Use, plugins, or MCP connections.
- Rules are experimental and should not be described as a complete security boundary.
- Hooks execute trusted code and require review; they are not merely documentation.
- Content from webpages, documents, issues, and tool output is untrusted evidence, not authoritative instruction.
- Self-generated tests and agreement between agents are not independent acceptance.

## Drift-Prone Claims

Keep model names, retirement dates, preview status, rollout availability, and host-specific controls in dated references rather than treating them as timeless principles.

## Public-Safety Boundary

Examples must be synthetic or composite. Do not publish an actual environment's profiles, capability counts, tool inventory, connected systems, paths, task identifiers, prompts, logs, security controls, or configuration.

## Official Sources

These boundaries were checked on 2026-08-20 against [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security), [Permissions](https://learn.chatgpt.com/docs/permission-modes), [Browser](https://learn.chatgpt.com/docs/browser), [Computer Use](https://learn.chatgpt.com/docs/computer-use), [Hooks](https://learn.chatgpt.com/docs/hooks), and [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules).
