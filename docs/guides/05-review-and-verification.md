# 5. Review and verification

The framework is only useful if readers can trust that each statement is correct and agreed. Verification happens on three levels: automatic checks, human review of each change, and review of the generated outputs.

## 1. Automatic checks (every pull request)

The **Validate** workflow runs `python tools/wp5.py validate` on every pull request. It fails if:

- a required field is missing, or an `id` is duplicated or does not match its level and task,
- a `sources` ref is not in `references/references.yaml`, or a non-stub node has no sources,
- a relation points to a node that does not exist, or in the wrong direction,
- a node is `in-review` or `agreed` without reviewers,
- an `agreed` node still contains a PROPOSED block.

It warns (but does not fail) about very long nodes, principles that nothing realises yet, and guidelines that realise nothing.

The workflow also builds the outputs and attaches them to the run, so reviewers can see how the change looks in the report.

## 2. Human review of each pull request

Every pull request needs at least one approval from the task that owns the changed folder (`.github/CODEOWNERS`). When a change adds a link to a node of another task, ask a reviewer from that task too.

Reviewers check:

- [ ] **Correctness**: the text says what the cited source says (open the source at the `locator`).
- [ ] **Nothing added**: no claims, examples or recommendations that are neither in the sources nor agreed by the group.
- [ ] **Links**: each relation is one the sources or the group actually make.
- [ ] **PROPOSED blocks**: accept (remove the markers), edit, or reject (delete the block).
- [ ] **AI-assisted changes** (`ai_assisted: true`): read the whole diff, not only the summary.
- [ ] **Status**: set `in-review` or `agreed` only when the group has decided.

Use GitHub's **suggestion** feature for small wording changes and comment threads for questions. Keep the discussion in the PR so the reasoning stays with the text.

## 3. Reviewing generated outputs

- **Mechanical outputs** (reports from `outline.yaml`, wiki, exports) only contain node text. If a sentence is wrong, fix the node. Every section shows its source node id and status.
- **AI-derived documents** in `outputs/derived/` are different: an AI rewrote the text. They carry the label "AI-generated draft - not verified" until a reviewer has compared every paragraph with the node ids it cites. See [outputs/derived/README.md](../../outputs/derived/README.md).

## Status of the content

| Status | Who sets it | Meaning in outputs |
|---|---|---|
| `stub` | anyone | "This part has not been written yet." |
| `draft` | author | Text exists, not reviewed |
| `in-review` | author, with named reviewers | The task group is checking it |
| `agreed` | reviewer from the owning task | Accepted by the task group |

AI assistants may only set `stub` or `draft`.
