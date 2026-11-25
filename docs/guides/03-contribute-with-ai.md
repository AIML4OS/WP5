# 3. Contribute with an AI assistant

AI assistants (Claude Code, GitHub Copilot, ChatGPT, Cursor, a local model, …) can help a lot: turning meeting notes into a node, splitting a long text, fixing language, checking links, building a derived document. They can also add plausible content that nobody agreed on. The repository is set up to keep the benefits and avoid that risk.

## What the assistant is told

Assistants that work in the repository read [AGENTS.md](../../AGENTS.md) (Claude reads it through `CLAUDE.md`). In short:

- Use only the cited sources, existing nodes, or what *you* explicitly give in the conversation.
- Do not fill gaps, invent references, or infer links. Ask instead.
- Put new wording in a **PROPOSED block**. Proposed blocks are left out of all outputs until a reviewer accepts them.
- Set `ai_assisted: true` on nodes it touched.
- Never approve or merge.

If your tool does not read `AGENTS.md` automatically (e.g. a chat assistant in the browser), paste the content of `AGENTS.md` at the start of the conversation.

## Typical tasks and example prompts

| Task | Example prompt |
|---|---|
| Turn source text into a node | "Create a Level 2 implementation node from Section 4.2 of the paper. Use only that text. Cite it with a locator. Link it to `L1-IMP-PROCESS-WORKFLOW-AUTOMATION`." |
| Split a long node | "Split this node into two nodes without changing the wording. Propose ids and links, and show me before you write." |
| Language and consistency | "Fix language and terminology in this node. Do not change the meaning; list every change in substance you considered and did not make." |
| Find gaps | "List Level 1 principles that no Level 2 node realises. Do not write any content." |
| Check a PR | "Check this pull request against AGENTS.md: are there claims without sources, or links not supported by the text?" |
| Derived document | Follow [outputs/derived/README.md](../../outputs/derived/README.md). |

## When you *want* to add something new with AI help

That is fine, and it is how most expert knowledge will enter. The assistant will:

1. ask where the content comes from,
2. cite a source if there is one, or
3. put the text in a PROPOSED block with your name as proposer.

The task group then confirms, edits or rejects it in the pull request. Only after the reviewer removes the PROPOSED markers does the text appear in reports.

## Your responsibility

You are the author of what you commit, regardless of the tool. Before you open a pull request, read the diff and check that:

- every statement is backed by the listed sources or is inside a PROPOSED block,
- no reference was invented (titles, years, URLs),
- the links (`relations`) are ones the source or the group actually makes.
