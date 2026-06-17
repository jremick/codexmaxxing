# Security Policy

Codexmaxxing is a public guide and resource repo for Codex operating patterns. Most issues will be documentation problems, but security reporting is appropriate when guidance could expose secrets, unsafe auth flows, private workspace details, or dangerous agent/tool behavior.

## Reporting

Use GitHub private vulnerability reporting when available:

<https://github.com/jremick/codexmaxxing/security/advisories/new>

If that path is unavailable, open a minimal public issue asking for a private reporting channel. Do not include exploit details, credentials, tokens, private logs, customer data, or sensitive reproduction steps in public issues.

## Public Issues

Public issues are appropriate for broken links, unclear guidance, outdated examples, and concrete improvements.

Do not post:

- real secrets, tokens, private keys, or `.env` values
- private customer, employer, or workspace details
- raw agent session logs that include private context
- internal incident details or vulnerable infrastructure information
