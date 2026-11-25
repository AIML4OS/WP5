# 1. Overview: how the framework is organised

## Why small files instead of one document

The three task groups write in parallel and at different levels of detail. A single long document makes this hard: everyone edits the same file, it is difficult to see who owns what, and it can only be read in one order.

Instead, every **principle**, **guideline** or piece of **practical guidance** is its own small Markdown file, a *node*. Each node says in its header which level and task it belongs to and which other nodes it links to. From these nodes we build:

- the **final report** in the agreed top-down structure,
- **other documents**, e.g. a bottom-up "What do I need to do?" guide,
- a **wiki** (GitHub Pages) for browsing,
- **AI-ready exports** for AI assistants and agents,
- later, possibly, a **graph** in a knowledge-graph tool.

The nodes are the only place where content is written. If something is wrong in a report, fix the node, not the report.

## The four levels

| Level | Name | Question it answers | Example |
|---|---|---|---|
| 0 | Foundations | Where do our principles come from? | ESS quality framework (CoP, QAF); EU legal framework; GSBPM, CRISP-DM, MLOps |
| 1 | Principles | What do we want to achieve? | *Reproducibility*; *Fit-for-purpose technical approach* |
| 2 | Guidelines | How do we achieve it? Concepts, ways of working, checklists | *Quality guidelines R1-R3*; *Technical architecture and hosting choices* |
| 3 | Practical guidance | What does it mean in practice? | *API gateways*; *Compute and hosting environments* |

## How nodes are linked

Links are stored on the **more concrete** node and point **up** (or sideways):

```
L3-IMP-API-GATEWAYS ──realises──▶ L2-IMP-TECHNICAL-ARCHITECTURE-HOSTING ──realises──▶ L1-IMP-FIT-FOR-PURPOSE
                    └─realises──▶ L2-IMP-SECURITY-ACCESS-LOGGING ─────────realises──▶ L1-IMP-FIT-FOR-PURPOSE
L2-IMP-REPRODUCIBILITY-ENABLERS ──realises──▶ L1-QUA-REPRODUCIBILITY   (implementation guidance for a quality principle)
L1-IMP-FIT-FOR-PURPOSE ──supports──▶ L1-QUA-REPRODUCIBILITY            (link between principles of two tasks)
L1-QUA-REPRODUCIBILITY ──derives_from──▶ L0-QUA-ESS-QUALITY-FRAMEWORK
```

This makes the structure a graph, not a tree: one Level 3 node can serve guidelines from several tasks. You never have to maintain links in two places. The tooling computes "what links here", and the wiki shows it on every page.

## Who owns what

Folders are split by task (`quality/`, `methodology/`, `implementation/`). The task that owns the folder reviews changes to it (see `.github/CODEOWNERS`). Nodes that belong to everyone go in `framework/cross-cutting/`.

## How a node matures

`stub` → `draft` → `in-review` → `agreed`

- **stub**: placeholder with a title and links, no text yet. Shows where content is needed.
- **draft**: text written, sources cited, not yet reviewed.
- **in-review**: the author asks the task group to check it. Reviewers are named.
- **agreed**: the task group has accepted the text.

Outputs always show the status, so readers can see what is agreed and what is not. Nodes marked `example: true` were created during the repository setup to illustrate the structure.

## Map of the repository

See the [README](../../README.md#where-things-are).
