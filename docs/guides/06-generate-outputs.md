# 6. Generate reports and other outputs

There are two kinds of outputs:

| | Mechanical | AI-derived |
|---|---|---|
| How | `tools/wp5.py` assembles node text according to an outline | An AI assistant rewrites node text for a specific audience |
| Text | identical to the nodes | new wording, based on the nodes |
| Verification | review the nodes | review each paragraph against the cited nodes |
| Examples | final report, practitioner guide, wiki | summary for managers, one-pager for IT architects |

## Mechanical reports

A report is defined by an **outline** (`outputs/<name>/outline.yaml`). The outline only says *what goes where*; it contains no framework content.

```bash
pip install -r requirements.txt
python tools/wp5.py report outputs/final-report/outline.yaml                 # Markdown
python tools/wp5.py report outputs/final-report/outline.yaml --formats docx  # also Word (needs pandoc)
```

The result is written to `build/outputs/final-report/`. You can also download it from the latest **Validate** or **Build outputs** run on GitHub (*Actions → run → Artifacts*), without installing anything.

### Outline building blocks

```yaml
sections:
  - title: "3.1.1 Quality dimensions"
    select: {level: 1, task: "5.1", group: quality-dimension}   # all matching nodes
  - title: "4.4 Cross-cutting"
    include: [L2-X-AI-CARDS]                                    # explicit list
  - title: "1. Introduction"
    static: static/01-introduction.md                           # non-node chapter text
  - title: "5. Practical guidance"
    hierarchy:                                                  # Level 3 structure
      lead: {level: 1, task: "5.1", group: quality-dimension}
      from_tasks: ["5.2", "5.3"]
      levels: [2, 3]
      unlinked_heading: "Guidance without intersection to Task 1 principles"
  - title: "6. Assessment"
    assessment_table: true                                      # table from `assessment`
```

**Chapter 5 of the final report** is built from the links. For each Task 5.1 principle, it lists the Level 2 and 3 nodes from Tasks 5.2 and 5.3 that `realise` or `support` it, directly or through a Level 2 node. Nodes that do not reach any Task 5.1 principle go in the "without intersection" section. Set `through_principles: true` to also follow links between principles. A node that would appear more than once is written out the first time and referred to afterwards.

### A new perspective, mechanically

Copy an outline (e.g. `outputs/practitioner-guide/outline.yaml`), change the order and selection, and build it. The practitioner guide is a first sketch of the bottom-up "What do I need to do?" view: practical guidance first, principles last.

## AI-derived documents

When a different audience needs different wording (shorter, simpler, another emphasis), an AI assistant can draft it from the nodes. The process is in [outputs/derived/README.md](../../outputs/derived/README.md):

1. Write a **brief** (audience, purpose, which node ids or selection to use).
2. Build the AI-ready export (`python tools/wp5.py export`) and give the assistant the brief, the listed nodes and `AGENTS.md`.
3. The assistant writes the draft with a node-id citation after every paragraph and a provenance header (commit, node ids, date, tool).
4. Open a pull request; reviewers check every paragraph against its cited nodes before the "not verified" label is removed.

## Everything at once

```bash
python tools/wp5.py all --formats docx
```

runs validation, builds every outline in `outputs/*/outline.yaml`, the AI exports and the wiki pages.
