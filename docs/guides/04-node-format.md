# 4. How to write a node

A node is a Markdown file with a YAML header (*front matter*) between two `---` lines, followed by the text. Start from [templates/node-template.md](../../templates/node-template.md).

## Where to put the file

```
framework/level-<n>-<name>/<quality|methodology|implementation>/<short-name>.md
framework/cross-cutting/<short-name>.md      # nodes owned by all tasks
```

The file name is for humans; the `id` is what links use.

## Front matter fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Stable identifier `L<level>-<TASK>-<SLUG>`, TASK = `QUA` (5.1), `MET` (5.2), `IMP` (5.3), `X` (cross). Never change after merge. |
| `title` | yes | Shown as heading in all outputs. Can be changed. |
| `level` | yes | `0`, `1`, `2` or `3`. |
| `task` | yes | `"5.1"`, `"5.2"`, `"5.3"` or `cross`. |
| `group` | no | Sub-grouping used by outlines, e.g. `quality-dimension`, `ethics`, `legal`. |
| `status` | yes | `stub`, `draft`, `in-review`, `agreed`. |
| `owners` | yes | GitHub handles of the authors (may be empty while seeding). |
| `reviewers` | for `in-review`/`agreed` | GitHub handles of the reviewers. |
| `sources` | yes unless `stub` | List of `{ref, locator}`. `ref` must be a key in `references/references.yaml`. |
| `relations` | no | Links, see below. |
| `assessment` | Level 3 only | `not-relevant`, `research-gap`, `C`, `B`, `A` (chapter 6 of the final report). |
| `example` | no | `true` for illustrative content from the repository setup. |
| `ai_assisted` | no | `true` if an AI assistant drafted or substantially edited the node. |
| `order` | no | Sort order within a section in outputs (default 100). |

## Links (`relations`)

Write links only on the more concrete node, pointing up or sideways:

| Relation | From → to | Use when |
|---|---|---|
| `derives_from` | L1 → L0 | a principle comes from a foundation |
| `realises` | L2 → L1, L3 → L2 (or L3 → L1) | this node helps achieve a higher-level node, of any task |
| `supports` | any → same or higher level, usually another task | e.g. an implementation principle supports a quality dimension |
| `related` | any → any | loose connection, no direction |

Only add a link that the sources or the group actually make. The validator checks that targets exist and point in the right direction.

## The text

- Aim for one to two pages; the validator warns above 1,500 words.
- Start with the core statement; a principle can begin with **Principle:** …, a quality dimension with **Short description:** ….
- Use `##` for subheadings; outputs shift heading levels automatically.
- Tables are fine (e.g. checklists).
- Notes for editors go in HTML comments: `<!-- TODO: ... -->`, `<!-- GAP: ... -->`, `<!-- Review note: ... -->`. They are kept out of all outputs.
- New wording that is not yet confirmed goes in a PROPOSED block (see [AGENTS.md](../../AGENTS.md#2-when-the-person-asks-you-to-add-something-new)).

## Example

```markdown
---
id: L2-IMP-MODEL-REGISTRIES
title: "Model registries"
level: 2
task: "5.3"
status: draft
owners: [some-handle]
reviewers: []
sources:
  - ref: wp53-paper-tech-perspectives
    locator: "Sections 2, 5, 7"
relations:
  realises: [L1-IMP-FIT-FOR-PURPOSE]
  related: [L2-IMP-REPRODUCIBILITY-ENABLERS]
---

Model registries support traceability by storing information about model versions, ...
```

## Adding a source

Add an entry to `references/references.yaml` with a short `key`, `type` (`wp5-draft` or `literature`), `title` and what else you know (author, date, url). Write `(to be completed)` rather than guessing.
