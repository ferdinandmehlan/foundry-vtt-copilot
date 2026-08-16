---
name: races-manage
description: Manage races/ entries — playable races, ancestral lineages, and species lore — in the Markdown TTRPG campaign vault.
---

# Races

The `races/` directory catalogs **ancestries and species**: playable races, lineages, and their cultural and biological traits. Use this skill when creating, editing, or organizing race entries.

Generic rules — file naming, wikilinks, frontmatter requirements, content conventions, GM secret blocks, and the vault directory hierarchy — are defined in the **`vault-core`** skill and apply to every race entry. This skill only covers what race entries are and how to work with them.

## When to Use

- Creating, updating, or organizing a playable race or ancestral lineage.
- Deciding what counts as a race entry, or how races relate to each other.
- Cross-referencing races from other categories (`cast/`, `factions/`, `codex/`, etc.).

## Race Entries

A race entry is a single Markdown file describing one race or ancestry.

| Field      | Purpose                                                                    |
|------------|----------------------------------------------------------------------------|
| `type`     | The kind of ancestry (e.g. `humanoid`, `beastfolk`, `elemental`, `undead`) |
| `origin`   | Where this race comes from, via wikilink                                   |
| `homeland` | Primary territory or region, via wikilink                                  |

### Entry Rules

- **Each race gets its own file.** Never inline a race into another entry.
- **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.
- **Link outward.** Every mentioned place, faction, or related race should be wikilinked.

## Editing & Creating Entries

When creating or editing an entry:

1. **Use the template** `references/races-template.md` as the reference shape for overall structure.
2. **Keep the entry self-contained and link-driven.** Describe the race in context with its history and culture.
3. **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.

### File Name Slugs

Filenames must be lowercase, kebab-case and reflect the race name:

- `ashborn-dwarves.md`
- `thorn-elves.md`
- `river-folk.md`
- `skywarden-gnomes.md`


