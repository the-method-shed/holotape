---
up: "[[Projects/_projects|Projects]]"
related: []
aliases: []
description:
author:
created:
modified:
leads: []
team: []
priority:
status: proposed
tags:
  - type/project
urls: []
---
# Project - [Project name]

> **Draft template:** Replace placeholders and obtain review before presenting this page as current team knowledge.
>
> **Intensity and status:** Place the page under `Projects/on/`, `ongoing/`, `simmering/`, or `sleeping/` according to current attention. Separately set the lifecycle `status` to `proposed` (default), `planning`, `ready`, `active`, or `complete`; use `paused` while work is on hold. Do not infer one from the other.
>
> **Project priority:** Set `priority` to 1–5 for current relative urgency across projects: **5 is most urgent, 1 is least urgent**. Leave it empty if not yet assessed, and update it as priorities change.

## Purpose and outcome

[What is this project trying to achieve? How will we know it is done?]

## Where to act

*Do not duplicate issue assignments or issue status here. The project `status` property describes the project as a whole.*

- Repository: [link]
- Issues: [link]

## Open actions

*Lightweight coordination follow-ups without a GitHub issue belong here. For repository work, create or link an issue instead. Record who, what, and a due date only if one has been agreed; move completed follow-ups into the dated log below.*

- [ ] [Who] — [What] (by [date, if agreed])

## Context and knowledge

[Links to the lead and team people pages, relevant maps, notes, and sources. Separate verified facts from hypotheses. Use relative Markdown links in the body so they work on GitHub.]

> [!info]- Child projects
> ```base
> views:
>   - type: table
>     name: Child projects
>     filters:
>       and:
>         - file.hasProperty("up")
>         - file.properties.up == this.file.name
>     order:
>       - file.name
>       - status
>       - priority
>     sort:
>       - property: status
>         direction: ASC
>     columnSize:
>       file.name: 289
>       note.status: 193
>     indentProperties: true
> ```

## Decisions

[Link to reviewed decisions, including who agreed and when. Mark open questions as open.]

## Project log

*Record dated developments and completed follow-ups, newest first. Link to sources and GitHub issues rather than copying issue updates; distinguish proposals from agreed decisions.*

### [YYYY-MM-DD]

[What happened, who was involved, and what remains open.]
