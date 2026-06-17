# Contributing

Thanks for improving Codexmaxxing. This repo is a public guide, so changes should make the material clearer, safer, easier to reuse, or better grounded in real verification.

## Good Contributions

- Fix unclear guidance, broken links, typos, or outdated examples.
- Add compact examples that are public-safe and easy to adapt.
- Improve templates, checklists, and source-of-truth maps.
- Tighten safety guidance around tools, secrets, permissions, and verification.

## Keep It Public-Safe

Do not include:

- real secrets, tokens, private keys, or `.env` files
- customer, employer, or private workspace details
- raw session exports with private context
- proprietary prompts or copied internal instructions
- machine-specific paths unless they are clearly generic examples

## Validation

Before opening a pull request, run:

```bash
python3 scripts/validate_content.py
```
