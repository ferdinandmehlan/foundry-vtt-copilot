---
name: atlas-manage
description: Manage atlas/ entries — nations, cities, districts, and points of interest — in the Markdown TTRPG campaign vault.
---

# Atlas

The `atlas/` directory catalogs **geography and places**: nations, cities, districts, and points of interest (POI). Use this skill when creating, editing, or organizing atlas entries.

Generic rules — file naming, wikilinks, frontmatter requirements, content conventions, GM secret blocks, and the vault directory hierarchy — are defined in the **`vault-core`** skill and apply to every atlas entry. This skill only covers what atlas entries are and how to work with them.

## When to Use

- Creating, updating, or organizing a nation, city, district, or POI.
- Deciding what counts as an atlas entry, or where a place belongs in the hierarchy.
- Cross-referencing locations from other categories (`cast/`, `factions/`, `campaign/`, etc.).

## Atlas Entries

An atlas entry is a single Markdown file describing one place at one of four scales:

| Scale      | What it represents                                                |
|------------|-------------------------------------------------------------------|
| `country`  | Nations, kingdoms, large regions                                  |
| `city`     | Major settlements                                                 |
| `district` | Quarters, wards, and neighborhoods **within a city**              |
| `poi`      | Specific points of interest: inns, landmarks, ruins, dungeons     |

### Scale Rules

- **Every atlas entry has a `scale`** in frontmatter (`country` | `city` | `district` | `poi`). Nothing else goes in `atlas/`.
- **Each entity gets its own file.** Never inline a location into another entry.
- **Parents vs. children:** A nation contains cities; a city contains districts; a district or city contains POI. Children link up to their parent; parents link down to their notable children.

## Editing & Creating Entries

When creating or editing an entry:

1. **Use the template** `references/atlas-template.md` as the reference shape for overall structure.
2. **Keep the entry self-contained and link-driven.** Describe the place in the context of its parent if present and cross-link every related entity.
3. **Reuse existing slugs.** Check the vault for an existing entry before creating a new one; link to existing entities rather than introducing duplicates.

### File Name Slugs

Filenames must be lowercase, kebab-case and reflect the place name. Examples by scale:

- **country:** `northern-reach.md`, `sunken-coast.md`, `iron-plains.md`
- **city:** `iron-market.md`, `riverwatch.md`, `stonecrest.md`
- **district:** `mill-district.md`, `dockside.md`, `upper-quarter.md`
- **poi:** `deep-woods-inn.md`, `old-watchtower.md`, `broken-bridge.md`


