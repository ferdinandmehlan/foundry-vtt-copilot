---
name: factions-manage
description: Manage factions/ entries — organizations, guilds, syndicates, and power structures — in the Markdown TTRPG campaign vault.
---

# Factions

The `factions/` directory catalogs **organizations and power structures**: guilds, syndicates, political groups, military orders, and other organized bodies. Use this skill when creating, editing, or organizing faction entries.

Generic rules — file naming, wikilinks, frontmatter requirements, content conventions, GM secret blocks, and the vault directory hierarchy — are defined in the **`vault-core`** skill and apply to every faction entry. This skill only covers what faction entries are and how to work with them.

## When to Use

- Creating, updating, or organizing a faction, guild, or organization.
- Deciding what counts as a faction, or how factions relate to each other.
- Cross-referencing factions from other categories (`cast/`, `atlas/`, `campaign/`, etc.).

## Faction Entries

A faction entry is a single Markdown file describing one organization or group.

### Entry Rules

- **Each faction gets its own file.** Never inline a faction into another entry.
- **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.
- **Link outward.** Every mentioned place, character, or related faction should be wikilinked.

## Editing & Creating Entries

When creating or editing an entry:

1. **Use the template** `references/factions-template.md` as the reference shape for overall structure.
2. **Keep the entry self-contained and link-driven.** Describe the faction in context with its members and territory.
3. **Reuse existing slugs.** Check the vault for an existing entry before creating a new one.

### File Name Slugs

Filenames must be lowercase, kebab-case and reflect the faction name:

- `iron-guild.md`
- `silver-hand.md`
- `crows-network.md`
- `order-of-the-flame.md`


