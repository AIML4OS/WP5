# Instructions for AI assistants and agents

These instructions apply to every AI assistant or agent working in this repository (Claude, Copilot, ChatGPT, Cursor, local models, …), whether it edits files, drafts text, reviews a pull request or answers questions from the material. `CLAUDE.md` and other tool-specific files point here.

This repository holds a framework that national statistical institutes may rely on. **Its value depends on every statement being traceable to a source or to a decision of the WP5 task groups.** Plausible-sounding additions that nobody agreed on are the main risk. Your job is to help people write, structure, check and reuse *their* material, not to add your own.

## 1. Hard rules

1. **Do not add content of your own.** Do not add facts, recommendations, examples, references, opinions, "best practices" or aspects that are not in the cited sources, in the existing nodes, or explicitly given by the person you are working with in this session.
2. **Do not fill gaps silently.** If something seems missing, say so and ask. You may leave a comment: `<!-- GAP: <what seems missing> -->`. Do not write the missing text.
3. **Do not invent sources.** Every `sources:` entry must exist in `references/references.yaml`. Never invent titles, authors, years, DOIs, URLs, page numbers or quotes. If a reference is incomplete, write `(to be completed)`.
4. **Keep the meaning when you edit.** Shortening, restructuring, fixing language or splitting a file must not change what the text says. If an edit would change the meaning, stop and ask.
5. **Do not change status upwards.** Only people set `status: in-review` or `status: agreed`. You may set `stub` or `draft`.
6. **Mark your work.** Set `ai_assisted: true` in the front matter of every node you create or substantially change, and say what you did in the pull request description.
7. **Do not merge, approve or resolve review threads.** Humans decide.
8. **English only** in the repository, even if the person writes to you in another language.

## 2. When the person asks you to add something new

Sometimes a participant wants new content, for example "add a paragraph on drift monitoring". Then:

1. Ask where the content comes from: a source document, a group decision, their own expertise?
2. If it comes from a **source**, add the source to `references/references.yaml` (only with details the person gives you or that are in the document) and cite it in the node with a `locator` (section/page).
3. If it is the **person's own proposal**, or you drafted wording for them, put it in a proposed block:

   ```markdown
   <!-- PROPOSED - NEEDS PARTICIPANT CONFIRMATION
   proposed-by: <name or GitHub handle of the person>, drafted with AI assistance
   reason: <why it is proposed>
   -->
   The proposed text goes here.
   <!-- END PROPOSED -->
   ```

   Proposed blocks are **left out of every generated output** (reports, wiki, AI exports) until a reviewer from the owning task removes the markers. The validator rejects `status: agreed` while a proposed block remains.
4. Remind the person that the text must be reviewed by the owning task group in the pull request (see `docs/guides/05-review-and-verification.md`).

## 3. Working with the structure

- One node per file, at most about 1,500 words. Split large topics into several nodes.
- Use `templates/node-template.md` and the format in `docs/guides/04-node-format.md`.
- IDs are stable: `L<level>-<QUA|MET|IMP|X>-<SLUG>`. Never rename an existing id; other nodes link to it.
- Record links only **upwards or sideways** in `relations:` (`derives_from`, `realises`, `supports`, `related`). Never duplicate the reverse link.
- Only add a relation if the source or the person says the two things are connected. Do not infer links because topics sound similar. If you think a link is missing, suggest it in your reply or the PR description.
- Review notes and TODOs go in HTML comments (`<!-- ... -->`). They do not appear in outputs.
- Run `python tools/wp5.py validate` before proposing a change and fix all errors.

## 4. Generating outputs

**Mechanical outputs** (reports from `outline.yaml`, wiki, `framework.json`, `llms.txt`) are built by `tools/wp5.py`. Do not write them by hand. To change a report, change the nodes or the outline.

**AI-derived documents** (a summary for managers, a guide for a specific role, a translation of the perspective, …) follow `outputs/derived/README.md`:

- Work only from the nodes listed in the brief. Do not use outside knowledge.
- Every paragraph cites the node id(s) it is based on, e.g. `[L2-QUA-ACCURACY-ROBUSTNESS-GUIDELINES]`.
- Keep the status visible: if a node is `draft`, `stub` or `example: true`, say so in the text.
- Begin the document with the provenance header from the brief template and the label **"AI-generated draft - not verified"**.
- If the nodes do not cover something the brief asks for, write "Not covered by the framework" instead of filling it in.

## 5. Answering questions from the material

When someone uses this repository (or `llms.txt` / `framework.json`) as context to answer questions:

- Answer only from the framework content and cite node ids.
- State the status of what you cite (draft/agreed, example content).
- If the framework does not answer the question, say so. You may add general knowledge only if you label it clearly as **not part of the WP5 framework**.

## 6. Checklist before you hand over

- [ ] No new claims, examples or references beyond the sources or what the person explicitly gave
- [ ] New wording proposed by you or the person is inside a PROPOSED block
- [ ] `ai_assisted: true` set on nodes you touched
- [ ] `python tools/wp5.py validate` passes
- [ ] The PR description lists what you changed and what needs human verification
