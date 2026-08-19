# Contributing

Thanks for improving Codexmaxxing. This repo is a public guide, so changes should make the material clearer, safer, easier to reuse, or better grounded in real verification.

## Good Contributions

- Fix unclear guidance, broken links, typos, or outdated examples.
- Add compact examples that are public-safe and easy to adapt.
- Improve templates, checklists, and source-of-truth maps.
- Tighten safety guidance around tools, secrets, permissions, and verification.

## Keep It Anonymous And Public-Safe

Use neutral editorial language and synthetic or composite examples. Examples must not map one-to-one to a real person, repository, organization, or environment.

Do not include:

- real secrets, tokens, private keys, or `.env` files
- names, handles, personal project links, or biographical details
- customer, employer, or private workspace details
- raw session exports with private context
- proprietary prompts or copied internal instructions
- machine-specific paths, hostnames, network details, account identifiers, or raw task IDs
- actual tool inventories, profiles, enabled integrations, hooks, rules, or security controls
- private harness graphs, ontology terms, eval fixtures, traces, state stores, or one-to-one architecture maps

Use explicit placeholders such as `<project-root>` and label every case study as synthetic. Generic skill categories, capability lifecycles, and safe operating principles are welcome when they do not reveal an originating environment.

## Validation

Before opening a pull request, run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py
```

The validator checks catalog coverage, local links, public-safe language and values, reviewed source hosts, current-product citations, asset review hashes, and the validation workflow's least-privilege policy.

When adding or changing a visual asset, inspect the rendered result, remove embedded metadata, and update `assets/review-manifest.json` only after completing the recorded visual, privacy, and metadata checks. New external source hosts require an explicit review before they are added to the validator allowlist.
