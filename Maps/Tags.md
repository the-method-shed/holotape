---
up: "[[HOME]]"
related: []
aliases: []
author:
created: 2026-10-07
modified: 2026-10-07T16:11:42+08:00
tags:
  - type/map
urls: []
---
# Tags (draft)

This is a **proposed navigation guide**, not approved team policy. Map links and relative Markdown links remain the primary way to find material; tags supplement them when a page belongs in more than one context. The earlier prototype guidance avoided a tag taxonomy altogether. The owner has since asked for a small hierarchical tag vocabulary where maps alone are insufficient.

## When to use a tag

- Use a tag for a useful cross-folder or cross-map view, not merely to repeat a folder name or a property. Keep project lifecycle in the `status` property, not tags.
- Prefer a short hierarchy with `/` separators and add a new branch only when several real pages need it. Obsidian's [nested tags](https://help.obsidian.md/tags#Nested%20tags) are searchable by parent; keep `tags` as a YAML list.
- Link a useful page from a map even when it has a tag. Tags do not replace plain Markdown navigation on GitHub.

## Tags in use

- `type/map` — a page that navigates related knowledge or components: [Areas](Areas.md), [Resources](Resources.md), [People](People.md), and this page. New map pages start from the [map template](../_assets/templates/tpl%20-%20Map.md), which also has this tag. An umbrella project page can use `type/map` when it serves as a map of independent subprojects; ordinary project pages do not need it.

The earlier `map` tag on Areas has been replaced by `type/map` to make room for other content types under `type/`. This list records reviewed uses, not an automatically generated count; use Obsidian's Tags view to browse every tag currently in the vault.

## Possible additions (not in use)

- `on/<theme>` — for a subject that crosses several projects or maps and needs a shared navigation path. Choose a real theme with the team before adding a specific tag; don't pre-create a topic tree.

Do not add `type/project` or `type/person` just to restate the `Projects/` or `Notes/People/` folder, or `status/*` to duplicate the project `status` property.
