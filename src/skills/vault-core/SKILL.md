---
name: vault-core
description: Core conventions for reading, creating, and modifying files in the Markdown TTRPG campaign vault.
---

# Vault Core Conventions

You are operating on a structured, category-organized Markdown TTRPG campaign knowledge vault. 
All generated or edited Markdown files MUST adhere to these global rules.

## 1. Vault Directory Hierarchy
Refer to the directory mapping below when deciding where to place or search for files:

- `atlas/` — Geography & places (nations, cities, districts, POI).
- `campaign/` — Operational play data (campaign hub)
  - `encounters/` — Combat, skill and social encounter designs.
  - `party/` — Player character sheets, party composition, and member details.
  - `quests/` — Quests, hooks, arcs, and objectives (active and completed).
  - `rules/` — House rules, homebrew mechanics, and rulings.
  - `sessions/` — Session logs, recaps, and play notes.
- `cast/` — Named characters.
- `codex/` — Setting lore, world concepts, historic events.
- `factions/` — Organizations, guilds, syndicates.
- `faiths/` — Religions and pantheons.
- `races/` — Races and ancestral lineages.

## 2. File Naming & Slugs
- All filenames MUST be lowercase, kebab-case (`iron-market.md`, `northern-reach.md`).
- File names serve as unique identifiers across the vault.
- Each Resource gets its own file

## 3. Wikilink Conventions
- Always link to existing entities using double brackets: `[[file-slug]]`.
- Use custom display text when needed: `[[file-slug|Display Name]]`.
- Never invent unreferenced files unless creating them.

## 4. Frontmatter Requirements
   Every file MUST begin with clean YAML frontmatter containing at minimum 
   - id
   - name
   - display_name
   - type

## 5. GM Secret Blocks
- Any GM-only information, prep notes, unrevealed plot twists, or secret mechanics MUST be wrapped in:
- Only add the optional secret block if applicable

```html
  <section class="secret" style="background: rgba(220, 38, 38, 0.08); border-left: 4px solid #dc2626; padding: 16px;">
  
  ### GM Secrets
  * Secret information here...
  
  </section>
```

Never strip or modify existing `<section class="secret">` blocks unless explicitly instructed to reveal a secret.

## 6. Content Conventions
- **Summary:** Open with 1–2 sentences: what the entity is, where it belongs, why it matters.
- **Sections:** Use `##` sections suited to the entity. See the template and existing entries for examples.
- **Wikilinks:** Link every mentioned entity. Always link to the parent location or parent entity where applicable.

## 7. Campaign Root File
- `campaign/campaign.md` — Special root file that serves as the campaign hub. It is the canonical overview of the active campaign and MUST contain:
  - Campaign title and premise.
  - Current status: active arc, party location, and immediate goals.
  - Wikilinked overviews of key operational data (`[[quests/...]]`, `[[party/...]]`, `[[sessions/...]]`, etc.).
  - A running log or index of recent session recaps.
  - GM-only campaign secrets in a `<section class="secret">` block (see §5).
