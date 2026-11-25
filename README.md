# AIML4OS WP5: a common framework for AI/ML in official statistics

This repository is where the three WP5 task groups write the common framework together:

| Task | Perspective |
|---|---|
| 5.1 | Quality (incl. ethics and legal aspects) |
| 5.2 | Methodology |
| 5.3 | Implementation |

We do **not** write one long document. Each principle, guideline or piece of practical guidance is a **small Markdown file** (a *node*). The nodes are the single source. Everything else is built from them: the final report, other reports, the wiki and the AI-ready exports.

> **Status:** first proposal for the structure (November 2026). The content in `framework/` is **example content** taken from WP5 working documents to show how the structure works. It has not been reviewed by the task groups.

## The four levels

```
Level 0  Foundations        where we derive our principles from (FPOS, CoP, QAF, EU law, GSBPM, MLOps ...)
   ▲ derives_from
Level 1  Principles         what we want to achieve
   ▲ realises
Level 2  Guidelines         how to achieve it: concepts, ways of working, checklists
   ▲ realises
Level 3  Practical guidance what it means in practice: hints, components, examples
```

All three tasks contribute on all levels. Links are not a strict tree: one Level 3 node can help realise guidelines from both quality and implementation. Each file only records its links **upwards** (or sideways). The tooling computes the reverse links ("what supports this principle?").

## Where things are

```
framework/                     the content (one node per file)
  level-0-foundations/{quality,methodology,implementation}/
  level-1-principles/{quality,methodology,implementation}/
  level-2-guidelines/{quality,methodology,implementation}/
  level-3-practical-guidance/{quality,methodology,implementation}/
  cross-cutting/               nodes shared by all tasks (e.g. AI Cards)
references/references.yaml     every source a node may cite
templates/node-template.md     copy this to start a new node
outputs/
  final-report/outline.yaml    structure of the final report (top-down)
  practitioner-guide/          "What do I need to do?" (bottom-up sketch)
  derived/                     AI-assisted documents for other audiences, with provenance
docs/guides/                   how-to guides (start here)
tools/wp5.py                   validate, build reports, wiki and AI exports
AGENTS.md                      rules for AI assistants (CLAUDE.md points here)
```

## Start here

1. [Overview: how the framework is organised](docs/guides/01-overview.md)
2. [Contribute directly with Git and Markdown](docs/guides/02-contribute-with-git.md)
3. [Contribute with an AI assistant](docs/guides/03-contribute-with-ai.md)
4. [How to write a node (front matter and links)](docs/guides/04-node-format.md)
5. [Review and verification](docs/guides/05-review-and-verification.md)
6. [Generate reports and other outputs](docs/guides/06-generate-outputs.md)
7. [Wiki and AI-ready material](docs/guides/07-wiki-and-ai-ready.md)

## The one rule

**Nothing enters the framework that is not backed by a source or agreed by the task group.** This applies to people and AI assistants alike. Every node lists its `sources`, every change goes through a pull request reviewed by the owning task, and AI assistants follow [AGENTS.md](AGENTS.md).

## Quick commands

```bash
pip install -r requirements.txt
python tools/wp5.py validate                                   # check nodes and links
python tools/wp5.py report outputs/final-report/outline.yaml --formats docx
python tools/wp5.py all                                        # everything, into build/
mkdocs serve                                                   # preview the wiki (after `wp5.py wiki`)
```

The AIML4OS project is co-funded by the European Union and Eurostat (Grant Agreement 101146355).
