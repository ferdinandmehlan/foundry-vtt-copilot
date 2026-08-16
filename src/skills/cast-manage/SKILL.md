---
name: cast-manage
description: Manage cast/ entries — named characters including NPCs, villains, contacts, and allies — in the Markdown TTRPG campaign vault.
---

# Cast

The `cast/` directory catalogs **named characters**: NPCs, villains, allies, contacts, and other individuals relevant to the campaign. Use this skill when creating, editing, or organizing character entries.

Generic rules — file naming, wikilinks, frontmatter requirements, content conventions, GM secret blocks, and the vault directory hierarchy — are defined in the **`vault-core`** skill and apply to every cast entry. This skill only covers what cast entries are and how to work with them.

## When to Use

- Creating, updating, or organizing a named character.
- Deciding whether a character warrants their own entry or belongs in another entry.
- Cross-referencing characters from other categories (`atlas/`, `factions/`, `campaign/`, etc.).

## Cast Entries

A cast entry is a single Markdown file describing one named character.

| Field      | Purpose                                                                           |
|------------|-----------------------------------------------------------------------------------|
| `role`     | The character's narrative function (e.g. `ally`, `villain`, `neutral`, `contact`) |
| `faction`  | Primary faction affiliation, if any, via wikilink                                 |
| `location` | Where this character is typically found, via wikilink                             |

### Entry Rules

- **Each character gets their own file.** Never inline a character into another entry.
- **Reuse existing slugs.** Check the vault for an existing entry before creating a new one; link to existing entities rather than introducing duplicates.
- **Link outward.** Every mentioned place, faction, or related character should be wikilinked.

## Editing & Creating Entries

When creating or editing an entry:

1. **Use the template** `references/cast-template.md` as the reference shape for overall structure.
2. **Keep the entry self-contained and link-driven.** Describe the character in context with their faction and location.
3. **Reuse existing slugs.** Check the vault for an existing entry before creating a new one; link to existing entities rather than introducing duplicates.

### File Name Slugs

Filenames must be lowercase, kebab-case and reflect the character's name:

- `lord-captain-voss.md`
- `sister-alendra.md`
- `gram-the-fixit.md`
- `commander-thorn.md`


