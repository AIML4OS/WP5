# 7. Wiki and AI-ready material

## The wiki (GitHub Pages)

The wiki is built from the same nodes as the reports. You never edit the wiki directly.

- Every node gets a page with its status, text, sources, the links it makes, and the nodes that link to it ("Linked from").
- The **Framework overview** page lists all nodes by level and task and shows the relations as a diagram.
- The guides are included.

**How it is updated:** the **Publish wiki** workflow rebuilds and publishes the site every time a pull request is merged into `main`. Nothing else is needed.

**Preview locally:**

```bash
pip install -r requirements.txt
python tools/wp5.py wiki     # generates build/wiki
mkdocs serve                 # open http://127.0.0.1:8000
```

> One-time setup by a repository admin: *Settings → Pages → Build and deployment → Source: GitHub Actions*.

## AI-ready exports

`python tools/wp5.py export` writes to `build/ai/` (also published with the wiki under `/ai/`):

| File | Use |
|---|---|
| `llms.txt` | Short index of all nodes with id, task and status, following the `llms.txt` convention. Point an AI assistant to this first. |
| `llms-full.txt` | All node texts in one file, for pasting into an assistant as context. |
| `nodes/<ID>.md` | One clean file per node, with its relations and reverse links in the header. |
| `framework.json` | Nodes, edges and references as JSON, for agents, RAG pipelines or import into a graph tool. |

All exports leave out review comments and PROPOSED blocks, and keep `status`, `example` and `ai_assisted` so a consumer can tell agreed from draft content. `llms.txt` repeats the essential rule for assistants: answer only from the material, cite node ids, state the status.

## Towards a knowledge graph

`framework.json` maps directly onto a property graph: nodes have a type (`foundation`, `principle`, `guideline`, `practical-guidance`), a task and a status, and edges have a type (`derives_from`, `realises`, `supports`, `related`). This makes it possible to load the framework into a graph tool later, for example to explore links between the tasks visually. That is a possible next step and not part of this setup.
