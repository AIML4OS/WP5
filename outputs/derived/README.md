# AI-derived documents

This folder holds documents that an AI assistant has **rewritten** from the framework nodes for a specific audience or need, for example a two-page summary for management or a one-pager for IT architects. Unlike the mechanical reports, the wording here is new, so it has to be verified separately.

Nothing in this folder is a source. If a derived document says something the nodes do not, the derived document is wrong.

## Process

1. **Create a folder** `outputs/derived/<short-name>/` and copy [brief-template.md](brief-template.md) into it as `brief.md`. Fill in audience, purpose, length and the nodes to use (a list of ids or a selection such as "all Level 1 and Level 2 nodes of Task 5.3").
2. **Build the AI-ready export** so the assistant gets clean node text:
   `python tools/wp5.py export` (files in `build/ai/nodes/`).
3. **Run the assistant** with: `AGENTS.md`, the brief, and the node files listed in the brief. Nothing else. The assistant writes `draft.md` in the same folder:
   - the provenance header from the brief template, filled in,
   - the label **AI-generated draft - not verified**,
   - a node-id citation after every paragraph, e.g. `[L1-IMP-FIT-FOR-PURPOSE]`,
   - "Not covered by the framework" where the brief asks for something the nodes do not contain.
4. **Open a pull request.** A reviewer compares every paragraph with the nodes it cites. Wrong or unsupported text is fixed or removed.
5. **When verified**, the reviewer changes the label to **Verified against framework commit `<sha>` by `<name>`, `<date>`**.
6. **When the nodes change**, the derived document is out of date. Re-run from step 2 with the new commit, or mark it as based on the old commit.

## Why the citations matter

The node-id citations make it possible to check each claim in a few seconds, and to find all derived documents affected when a node changes (`grep -r L2-IMP-MODEL-REGISTRIES outputs/derived`).
