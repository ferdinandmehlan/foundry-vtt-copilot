---
name: faiths-manage
description: Manage faiths/ entries — deities, pantheons, religious orders, and spiritual traditions — in the Markdown TTRPG campaign vault.
---

# Faiths

The `faiths/` directory catalogs **religions and spiritual traditions**: deities, pantheons, religious orders, temples, and belief systems. Use this skill when creating, editing, or organizing faith entries.

Generic rules — file naming, wikilinks, frontmatter requirements, content conventions, GM secret blocks, and the vault directory hierarchy — are defined in the **`vault-core`** skill and apply to every faith entry. This skill only covers what faith entries are and how to work with them.

## When to Use

- Creating, updating, or organizing a deity, pantheon, or religious tradition.
- Deciding what counts as a faith entry, or how faiths relate to each other.
- Cross-referencing faiths from other categories (`cast/`, `factions/`, `atlas/`, etc.).

## Faith Entries

A faith entry is a single Markdown file describing one deity, pantheon, or religious tradition.

### Entry Rules

- **Each faith gets its own file.** Never inline a faith into another entry.
- **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.
- **Link outward.** Every mentioned place, character, or faction should be wikilinked.

## Editing & Creating Entries

When creating or editing an entry:

1. **Use the template** `references/faiths-template.md` as the reference shape for overall structure.
2. **Keep the entry self-contained and link-driven.** Describe the faith in context with its followers and holy sites.
3. **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.

### File Name Slugs

Filenames must be lowercase, kebab-case and reflect the faith or deity name:

- `the-burning-eye.md`
- `pantheon-of-the-sea.md`
- `order-of-the-dawn.md`
- `church-of-the-last-light.md`


