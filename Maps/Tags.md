---
up: "[[HOME]]"
related: []
aliases: []
author:
created: 2026-10-07
modified: 2026-10-08T17:33:00+08:00
tags:
  - type/map
urls: []
---
# Tags (draft)

This is a **proposed navigation guide**, not approved team policy. Map links and relative Markdown links remain the primary way to find material; tags provide a small set of cross-vault views. Keep `tags` as a YAML list.

## Default page types

Use one `type/*` tag for a page's primary role, even when its folder also indicates that role. This deliberate exception keeps type searches consistent if pages move. The map, project, and person templates supply their defaults; the clipping skill adds `type/clip` when using the base template. Existing project and people pages have not been retagged as part of this draft.

- `type/map` — navigation pages such as [Areas](Areas.md), [Resources](Resources.md), and [People](People.md). Use the [map template](../_assets/templates/tpl%20-%20Map.md).
- `type/project` — an effort with a defined outcome, including an umbrella project that links to subprojects. Use the [project template](../_assets/templates/tpl%20-%20Project.md).
- `type/person` — an individual profile, not a map of people. Use the [person template](../_assets/templates/tpl%20-%20Person.md).
- `type/clip` — a captured source in the unreviewed [inbox](../+/_inbox.md), created with the [clipping skill](../.agents/skills/holotape-clip/SKILL.md) and base template. The tag says what kind of page it is, not that its claims are approved.

For example, [People](People.md) is `type/map` only; individual pages under `Notes/People/` use `type/person`. Do not add `type/people` to describe the map's subject.

## Before adding another tag

- Ask what view the new tag would make possible. For a relationship between pages, use links; for project lifecycle, use the `status` property; for unreviewed material, use the inbox. Do not create `status/*` tags or a tag for each project or person.
- A cross-cutting `on/<theme>` tag may be useful when several reviewed pages across contexts need the same view. Propose the specific name and example pages for human review here before using it; do not pre-create a topic tree.
- Keep the hierarchy shallow (`/` separates levels). Obsidian's [nested tags](https://help.obsidian.md/tags#Nested%20tags) can be searched by parent. Even when a page has a tag, link it from a relevant map so GitHub readers can find it without plugins.

This guide records proposed defaults, not an automatically generated tag index. Use Obsidian's Tags view to see which tags are actually in use.
