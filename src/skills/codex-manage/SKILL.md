---
name: codex-manage
description: Manage codex/ entries — setting lore, world concepts, historic events, and deep knowledge — in the Markdown TTRPG campaign vault.
---

# Codex

The `codex/` directory catalogs **setting lore and world knowledge**: concepts, historic events, deep world truths, and background information. Use this skill when creating, editing, or organizing codex entries.

Generic rules — file naming, wikilinks, frontmatter requirements, content conventions, GM secret blocks, and the vault directory hierarchy — are defined in the **`vault-core`** skill and apply to every codex entry. This skill only covers what codex entries are and how to work with them.

## When to Use

- Creating, updating, or documenting a world concept, historic event, or piece of lore.
- Deciding whether something belongs in `codex/` versus another category.
- Cross-referencing lore from other categories (`atlas/`, `factions/`, `cast/`, etc.).

## Codex Entries

A codex entry is a single Markdown file describing one piece of world knowledge.

| Concept Type | What it represents                                                              |
|--------------|---------------------------------------------------------------------------------|
| `lore`       | Historic events, wars, disasters, pivotal moments                               |
| `concept`    | World rules, magic systems, cosmology, metaphysics                              |

### Entry Rules

- **Each concept gets its own file.** Never inline a lore entry into another entry.
- **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.
- **Link outward.** Every mentioned place, character, or faction should be wikilinked.

## Editing & Creating Entries

When creating or editing an entry:

1. **Use the template** `references/codex-template.md` as the reference shape for overall structure.
2. **Keep the entry self-contained and link-driven.** Describe the lore in context with related entries.
3. **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.

### File Name Slugs

Filenames must be lowercase, kebab-case and reflect the concept name:

- `the-great-schism.md`
- `arcane-weave.md`
- `dawn-age.md`
- `blood-moon-prophecy.md`


