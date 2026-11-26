---
# Copy this file into the right folder under framework/ and rename it,
# e.g. framework/level-2-guidelines/implementation/drift-monitoring.md
# Delete the comment lines when you are done. See docs/guides/04-node-format.md.

id: L2-IMP-EXAMPLE-SLUG     # L<level>-<QUA|MET|IMP|X>-<SHORT-NAME>, never change once merged
title: "Short descriptive title"
level: 2                    # 0 foundations, 1 principles, 2 guidelines, 3 practical guidance
task: "5.3"                 # "5.1" quality, "5.2" methodology, "5.3" implementation, cross
group:                      # optional sub-grouping used by outlines (e.g. quality-dimension, ethics, legal)
status: stub                # stub -> draft -> in-review -> agreed
owners: []                  # GitHub handles of the authors
reviewers: []               # GitHub handles; required for in-review and agreed
sources:                    # required unless status is stub; keys from references/references.yaml
  - ref: wp53-paper-tech-perspectives
    locator: "Section 5"
relations:                  # links UP or SIDEWAYS only; reverse links are computed
  realises: []              # higher-level nodes this helps achieve (L2 -> L1, L3 -> L2)
  derives_from: []          # L1 only: foundations (L0) this principle comes from
  supports: []              # nodes of another task on the same or a higher level
  related: []               # loose connection, no direction
assessment:                 # Level 3 only: not-relevant | research-gap | C | B | A
ai_assisted: false          # true if an AI assistant drafted or substantially edited this node
order: 100                  # optional: sort order within its section in outputs
---

Write the text here. Keep it short (at most about 1,500 words). Use `##` for subheadings.

<!-- Review notes, TODOs and gaps go in HTML comments like this one.
     They are not included in reports, the wiki or AI exports. -->
