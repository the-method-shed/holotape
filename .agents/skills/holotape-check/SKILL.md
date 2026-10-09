---
name: holotape-check
description: Check this Obsidian team vault for broken relative Markdown links, missing index entries, stale Bases folder filters, invalid project intensity/status conventions, and unreviewed clip markers. Use after ingest, page moves, or navigation edits, and whenever asked to audit or validate the whole vault. Complements Obsidian Linter; does not format notes.
modified: 2026-10-09T12:13:34+08:00
created: 2026-10-09T11:44:23+08:00
---
# Check the vault

1. Resolve the vault root as `../../..` from this skill's directory. From that root run `python3 .agents/skills/holotape-check/scripts/check_vault.py`. No packages or network access are needed. The command exits nonzero and prints paths when a check fails.
2. Read each flagged page and its linked sources before suggesting a repair. Check path moves against inbound links, especially external issue links; an index entry does not imply review or approval. Do not quietly rewrite claims or promote clips to silence a check.
3. If modifying the checker, run `python3 -m unittest discover -s .agents/skills/holotape-check/tests -v` and then the vault check. Report both outcomes, and note anything you cannot verify in Obsidian itself.

The checker is intentionally narrow: it checks local Markdown links, index coverage of `Atlas/`, `Projects/`, and `+/`, project folder/intensity and lifecycle `status`, unreviewed inbox markers and clip citations, and literal path filters in `.base` files. It does **not** parse arbitrary YAML or Obsidian wikilinks, lint Markdown style, evaluate Bases formulas, or prove Obsidian renders a view. Use Obsidian Linter for page formatting and manually inspect views when they change.
