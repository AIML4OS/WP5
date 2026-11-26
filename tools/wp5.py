#!/usr/bin/env python3
"""WP5 framework tooling.

One small script, no magic. It reads every node file under ``framework/``,
checks it, and builds the outputs from the same source:

    python tools/wp5.py validate              # check all nodes and links
    python tools/wp5.py report <outline.yaml> # assemble a report (Markdown)
    python tools/wp5.py export                # AI-ready exports (JSON, llms.txt)
    python tools/wp5.py wiki                  # source pages for the MkDocs wiki
    python tools/wp5.py all                   # validate + every output

Everything is written to ``build/`` (not committed). The script never writes
or changes framework content: outputs are assembled mechanically from the
nodes, so every sentence in an output can be traced back to a node file.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FRAMEWORK = ROOT / "framework"
BUILD = ROOT / "build"
REFERENCES = ROOT / "references" / "references.yaml"

TASKS = {
    "5.1": "Quality (Task 5.1)",
    "5.2": "Methodology (Task 5.2)",
    "5.3": "Implementation (Task 5.3)",
    "cross": "Cross-cutting (all tasks)",
}
TASK_CODES = {"5.1": "QUA", "5.2": "MET", "5.3": "IMP", "cross": "X"}
LEVEL_NAMES = {
    0: "Foundations (Level 0)",
    1: "Principles (Level 1)",
    2: "Guidelines (Level 2)",
    3: "Practical guidance (Level 3)",
}
KINDS = {0: "foundation", 1: "principle", 2: "guideline", 3: "practical-guidance"}
STATUSES = ["stub", "draft", "in-review", "agreed"]
ASSESSMENTS = ["not-relevant", "research-gap", "C", "B", "A"]
# Relation types. All of them are stored on the *lower* (more concrete) node
# and point to the higher or sibling node; reverse links are computed.
RELATIONS = {
    "realises": "helps achieve a node on a higher level (e.g. L2 -> L1)",
    "derives_from": "a principle derives from a foundation (L1 -> L0)",
    "supports": "supports a node of another task on the same or a higher level",
    "related": "loosely related, no direction implied",
}
REQUIRED = ["id", "title", "level", "task", "status", "owners", "sources"]
MAX_WORDS = 1500
PROPOSED_MARKER = "PROPOSED - NEEDS PARTICIPANT CONFIRMATION"


@dataclass
class Node:
    path: Path
    meta: dict
    body: str
    reverse: dict = field(default_factory=dict)  # relation -> [ids pointing here]

    @property
    def id(self) -> str:
        return self.meta["id"]

    @property
    def title(self) -> str:
        return self.meta["title"]

    @property
    def level(self) -> int:
        return int(self.meta["level"])

    @property
    def task(self) -> str:
        return str(self.meta["task"])

    @property
    def status(self) -> str:
        return self.meta.get("status", "stub")

    def rel(self, name: str) -> list[str]:
        return list((self.meta.get("relations") or {}).get(name) or [])

    def upward(self) -> list[str]:
        return self.rel("realises") + self.rel("derives_from") + self.rel("supports")

    @property
    def rel_path(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)


def parse(path: Path) -> Node:
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        raise ValueError(f"{path}: missing YAML front matter")
    meta = yaml.safe_load(m.group(1)) or {}
    return Node(path=path, meta=meta, body=m.group(2).strip() + "\n")


def load_nodes() -> dict[str, Node]:
    nodes: dict[str, Node] = {}
    for path in sorted(FRAMEWORK.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        node = parse(path)
        nodes.setdefault(node.meta.get("id", str(path)), node)
    for node in nodes.values():
        for rel in RELATIONS:
            for target in node.rel(rel):
                if target in nodes:
                    nodes[target].reverse.setdefault(rel, []).append(node.id)
    return nodes


def load_references() -> dict:
    if not REFERENCES.exists():
        return {}
    data = yaml.safe_load(REFERENCES.read_text(encoding="utf-8")) or {}
    return {r["key"]: r for r in data.get("references", [])}


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------


def validate(nodes: dict[str, Node] | None = None) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    seen: dict[str, Path] = {}
    refs = load_references()

    paths = [p for p in sorted(FRAMEWORK.rglob("*.md")) if p.name.lower() != "readme.md"]
    for path in paths:
        try:
            node = parse(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(str(exc))
            continue
        where = node.rel_path
        meta = node.meta
        for key in REQUIRED:
            if key not in meta:
                errors.append(f"{where}: missing field '{key}'")
        if "id" not in meta:
            continue
        nid = meta["id"]
        if nid in seen:
            errors.append(f"{where}: duplicate id {nid} (also in {seen[nid]})")
        seen[nid] = path
        level = meta.get("level")
        task = str(meta.get("task"))
        if level not in LEVEL_NAMES:
            errors.append(f"{where}: level must be 0-3, got {level!r}")
        if task not in TASKS:
            errors.append(f"{where}: task must be one of {list(TASKS)}, got {task!r}")
        if level in LEVEL_NAMES and task in TASKS:
            prefix = f"L{level}-{TASK_CODES[task]}-"
            if not nid.startswith(prefix):
                errors.append(f"{where}: id {nid} should start with {prefix}")
        status = meta.get("status")
        if status not in STATUSES:
            errors.append(f"{where}: status must be one of {STATUSES}, got {status!r}")
        sources = meta.get("sources") or []
        if status != "stub" and not sources:
            errors.append(f"{where}: status '{status}' requires at least one source")
        for src in sources:
            key = src.get("ref") if isinstance(src, dict) else None
            if not key:
                errors.append(f"{where}: each source needs a 'ref'")
            elif key not in refs:
                errors.append(f"{where}: source ref '{key}' not in references/references.yaml")
        if status in ("in-review", "agreed") and not meta.get("reviewers"):
            errors.append(f"{where}: status '{status}' requires reviewers")
        if PROPOSED_MARKER in node.body and status == "agreed":
            errors.append(f"{where}: an 'agreed' node still contains a proposed block")
        if meta.get("assessment") is not None:
            if level != 3:
                errors.append(f"{where}: 'assessment' is only used on Level 3 nodes")
            elif meta["assessment"] not in ASSESSMENTS:
                errors.append(f"{where}: assessment must be one of {ASSESSMENTS}")
        rels = meta.get("relations") or {}
        for rel in rels:
            if rel not in RELATIONS:
                errors.append(f"{where}: unknown relation '{rel}' (use {list(RELATIONS)})")
        words = len(node.body.split())
        if words > MAX_WORDS:
            warnings.append(f"{where}: {words} words; consider splitting (limit {MAX_WORDS})")
        if status != "stub" and words < 15:
            warnings.append(f"{where}: very short body for status '{status}'")

    nodes = nodes or load_nodes()
    for node in nodes.values():
        for rel in RELATIONS:
            for target in node.rel(rel):
                if target not in nodes:
                    errors.append(f"{node.rel_path}: {rel} -> unknown id {target}")
                    continue
                t = nodes[target]
                if rel == "realises" and not t.level < node.level:
                    errors.append(f"{node.rel_path}: 'realises' must point to a higher level (lower number): {target}")
                if rel == "derives_from" and not (node.level == 1 and t.level == 0):
                    errors.append(f"{node.rel_path}: 'derives_from' is for L1 -> L0 only: {target}")
                if rel == "supports" and t.level > node.level:
                    errors.append(f"{node.rel_path}: 'supports' must not point to a lower level: {target}")
        if node.level >= 2 and not node.rel("realises") and node.status != "stub":
            warnings.append(f"{node.rel_path}: Level {node.level} node does not realise anything")
        if node.level == 1 and not node.reverse and node.status != "stub":
            warnings.append(f"{node.rel_path}: no Level 2/3 node links to this principle yet")

    for w in warnings:
        print(f"WARNING  {w}")
    for e in errors:
        print(f"ERROR    {e}")
    print(f"\n{len(seen)} nodes, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


# --------------------------------------------------------------------------
# Rendering helpers
# --------------------------------------------------------------------------


def shift_headings(body: str, by: int) -> str:
    out = []
    in_code = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r"^#{1,6} ", line):
            hashes, rest = line.split(" ", 1)
            line = "#" * min(6, len(hashes) + by) + " " + rest
        out.append(line)
    return "\n".join(out) + "\n"


def strip_proposed(body: str) -> str:
    """Remove blocks marked as proposed so that unconfirmed text never ends up
    in an assembled output. Blocks look like:
    <!-- PROPOSED - NEEDS PARTICIPANT CONFIRMATION --> ... <!-- END PROPOSED -->
    """
    return re.sub(
        r"<!-- " + re.escape(PROPOSED_MARKER) + r".*?<!-- END PROPOSED -->\s*",
        "",
        body,
        flags=re.S,
    )


def strip_comments(body: str) -> str:
    """HTML comments hold review notes and TODOs for editors; keep them out of outputs."""
    return re.sub(r"<!--.*?-->\s*", "", body, flags=re.S)


def clean(body: str) -> str:
    return strip_comments(strip_proposed(body))


def strip_example_banner(body: str) -> str:
    return re.sub(r"\A> \*\*Example content\*\*.*?\n\n", "", body, flags=re.S)


def provenance(node: Node) -> str:
    parts = [f"`{node.id}`", f"status: {node.status}"]
    if node.meta.get("example"):
        parts.append("example content")
    if node.meta.get("ai_assisted"):
        parts.append("AI-assisted")
    return "*Source node: " + " · ".join(parts) + f" · {node.rel_path}*\n"


# Ids already written out in the report being built. A node that appears a
# second time (e.g. a Level 2 guideline in both chapter 4 and chapter 5) is
# referenced instead of repeated, so every text exists once per output.
WRITTEN: set[str] = set()


def node_section(node: Node, depth: int, nodes: dict[str, Node]) -> str:
    if node.id in WRITTEN:
        return "#" * depth + f" {node.title}\n\n_Described earlier in this document (`{node.id}`)._\n\n"
    WRITTEN.add(node.id)
    body = strip_example_banner(clean(node.body))
    text = "#" * depth + f" {node.title}\n\n"
    text += provenance(node) + "\n"
    if node.status == "stub":
        text += "_This part has not been written yet._\n\n"
    text += shift_headings(body, depth) + "\n"
    ups = [u for u in node.upward() if u in nodes]
    if ups:
        text += "_Links to: " + "; ".join(f"{nodes[u].title} (`{u}`)" for u in ups) + "_\n\n"
    return text


def select(nodes: dict[str, Node], spec: dict) -> list[Node]:
    out = list(nodes.values())
    if "level" in spec:
        out = [n for n in out if n.level == spec["level"]]
    if "task" in spec:
        tasks = spec["task"] if isinstance(spec["task"], list) else [spec["task"]]
        out = [n for n in out if n.task in [str(t) for t in tasks]]
    if "group" in spec:
        out = [n for n in out if n.meta.get("group") == spec["group"]]
    if spec.get("exclude_stubs"):
        out = [n for n in out if n.status != "stub"]
    return sorted(out, key=lambda n: (n.meta.get("order", 100), n.id))


def ancestors(node: Node, nodes: dict[str, Node], through_principles: bool = True) -> set[str]:
    """All nodes reachable upwards from ``node``.

    With ``through_principles=False`` the walk stops at Level 1: links between
    principles (e.g. an implementation principle that *supports* a quality
    dimension) are not followed. The report hierarchy uses this so that a
    Level 2/3 node is placed under a leading principle only when it, or a
    Level 2 node it realises, links to that principle directly.
    """
    seen: set[str] = set()
    stack = list(node.upward())
    while stack:
        nid = stack.pop()
        if nid in seen or nid not in nodes:
            continue
        seen.add(nid)
        if through_principles or nodes[nid].level >= 2:
            stack.extend(nodes[nid].upward())
    return seen


# --------------------------------------------------------------------------
# Report assembly
# --------------------------------------------------------------------------


def render_hierarchy(spec: dict, nodes: dict[str, Node], depth: int) -> str:
    """Practical guidance grouped under each leading principle.

    For every lead node (e.g. each Task 5.1 principle) list the nodes from the
    other tasks that reach it through realises/supports links. A node that
    reaches several lead nodes is written out in full the first time and
    referenced afterwards, so nothing is duplicated.
    """
    leads = select(nodes, spec["lead"])
    from_tasks = [str(t) for t in spec.get("from_tasks", ["5.2", "5.3"])]
    levels = spec.get("levels", [2, 3])
    candidates = [n for n in nodes.values() if n.task in from_tasks and n.level in levels]
    through = bool(spec.get("through_principles", False))
    out = ""
    for lead in leads:
        out += "#" * depth + f" {lead.title}\n\n"
        out += f"*Leading principle `{lead.id}`*\n\n"
        any_hit = False
        for task in from_tasks:
            hits = sorted(
                (c for c in candidates if c.task == task and lead.id in ancestors(c, nodes, through)),
                key=lambda n: (n.level, n.meta.get("order", 100), n.id),
            )
            if not hits:
                continue
            any_hit = True
            out += "#" * (depth + 1) + f" Practical guidance from {TASKS[task]}\n\n"
            for h in hits:
                out += node_section(h, depth + 2, nodes)
        if not any_hit:
            out += "_No linked guidance from the other tasks yet._\n\n"
    if spec.get("unlinked_heading"):
        lead_ids = {lead.id for lead in leads}
        rest = [c for c in candidates if not (ancestors(c, nodes, through) & lead_ids)]
        out += "#" * depth + f" {spec['unlinked_heading']}\n\n"
        if not rest:
            out += "_None at the moment._\n\n"
        for r in sorted(rest, key=lambda n: (n.task, n.level, n.id)):
            out += node_section(r, depth + 1, nodes)
    return out


def render_assessment(nodes: dict[str, Node]) -> str:
    rows = [n for n in nodes.values() if n.level == 3]
    out = "| Practical guidance | Task | Assessment | Node |\n|---|---|---|---|\n"
    for n in sorted(rows, key=lambda n: (n.task, n.id)):
        out += f"| {n.title} | {n.task} | {n.meta.get('assessment') or 'not yet assessed'} | `{n.id}` |\n"
    return out + "\n"


def render_section(sec: dict, nodes: dict[str, Node], depth: int, outline_dir: Path) -> str:
    out = "#" * depth + f" {sec['title']}\n\n"
    if "text" in sec:
        out += sec["text"].strip() + "\n\n"
    if "static" in sec:
        out += shift_headings((outline_dir / sec["static"]).read_text(encoding="utf-8"), depth) + "\n"
    for nid in sec.get("include", []):
        out += node_section(nodes[nid], depth + 1, nodes)
    if "select" in sec:
        found = select(nodes, sec["select"])
        if not found:
            out += "_No content yet._\n\n"
        for n in found:
            out += node_section(n, depth + 1, nodes)
    if "hierarchy" in sec:
        out += render_hierarchy(sec["hierarchy"], nodes, depth + 1)
    if sec.get("assessment_table"):
        out += render_assessment(nodes)
    for sub in sec.get("sections", []):
        out += render_section(sub, nodes, depth + 1, outline_dir)
    return out


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:  # noqa: BLE001
        return "unknown"


def build_report(outline_path: Path, nodes: dict[str, Node], formats: list[str]) -> Path:
    outline = yaml.safe_load(outline_path.read_text(encoding="utf-8"))
    name = outline.get("name", outline_path.parent.name)
    out_dir = BUILD / "outputs" / name
    out_dir.mkdir(parents=True, exist_ok=True)
    WRITTEN.clear()
    text = f"# {outline['title']}\n\n"
    text += (
        f"> Assembled mechanically from the WP5 framework files (commit `{git_commit()}`). "
        "Do not edit this file: change the node files in `framework/` instead. "
        "Text marked as example content or with status other than *agreed* is not yet approved.\n\n"
    )
    for sec in outline["sections"]:
        text += render_section(sec, nodes, 2, outline_path.parent)
    md = out_dir / f"{name}.md"
    md.write_text(text, encoding="utf-8")
    print(f"wrote {md.relative_to(ROOT)}")
    for fmt in formats:
        if not shutil.which("pandoc"):
            print("pandoc not found; skipping", fmt)
            break
        target = out_dir / f"{name}.{fmt}"
        subprocess.run(["pandoc", str(md), "-o", str(target), "--toc"], check=True)
        print(f"wrote {target.relative_to(ROOT)}")
    return md


# --------------------------------------------------------------------------
# AI-ready exports
# --------------------------------------------------------------------------


def export(nodes: dict[str, Node]) -> None:
    out = BUILD / "ai"
    out.mkdir(parents=True, exist_ok=True)
    refs = load_references()
    graph = {
        "name": "AIML4OS WP5 framework",
        "commit": git_commit(),
        "levels": LEVEL_NAMES,
        "tasks": TASKS,
        "nodes": [],
        "edges": [],
        "references": list(refs.values()),
    }
    for n in sorted(nodes.values(), key=lambda n: (n.level, n.task, n.id)):
        meta = {k: v for k, v in n.meta.items() if k != "relations"}
        graph["nodes"].append({**meta, "kind": KINDS[n.level], "path": n.rel_path, "body": clean(n.body)})
        for rel in RELATIONS:
            for target in n.rel(rel):
                graph["edges"].append({"from": n.id, "type": rel, "to": target})
    (out / "framework.json").write_text(json.dumps(graph, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    index = [
        "# AIML4OS WP5 framework",
        "",
        "> Common framework for the use of AI/ML in official statistics (quality, methodology, implementation),",
        "> organised in Levels 0-3. Content is work in progress; check each node's status before relying on it.",
        "",
        "Rules for AI assistants using this material: use only what is written here, cite node ids,",
        "and do not present draft or example content as agreed. See AGENTS.md in the repository.",
        "",
    ]
    full = list(index)
    for level, lname in LEVEL_NAMES.items():
        index.append(f"## {lname}")
        index.append("")
        for n in select(nodes, {"level": level}):
            index.append(f"- [{n.title}](nodes/{n.id}.md): {n.id}, {TASKS[n.task]}, status {n.status}")
        index.append("")
    nodes_dir = out / "nodes"
    nodes_dir.mkdir(exist_ok=True)
    for n in nodes.values():
        rels = {r: n.rel(r) for r in RELATIONS if n.rel(r)}
        header = (
            f"# {n.title}\n\nid: {n.id} | level: {n.level} | task: {n.task} | status: {n.status}\n"
            f"relations: {json.dumps(rels)}\nlinked from: {json.dumps(n.reverse)}\n\n"
        )
        (nodes_dir / f"{n.id}.md").write_text(header + clean(n.body), encoding="utf-8")
        full.append(header + clean(n.body))
    (out / "llms.txt").write_text("\n".join(index), encoding="utf-8")
    (out / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}/ (framework.json, llms.txt, llms-full.txt, nodes/)")


# --------------------------------------------------------------------------
# Wiki
# --------------------------------------------------------------------------

STATUS_BADGE = {"stub": "⚪ stub", "draft": "🟡 draft", "in-review": "🟠 in review", "agreed": "🟢 agreed"}


def wiki(nodes: dict[str, Node]) -> None:
    out = BUILD / "wiki"
    if out.exists():
        shutil.rmtree(out)
    (out / "framework").mkdir(parents=True)
    shutil.copytree(ROOT / "docs", out / "docs")
    # Copy the files the guides link to, at the same relative paths, so that
    # links work both on GitHub and in the wiki.
    for rel in ["AGENTS.md", "CONTRIBUTING.md", "templates/node-template.md",
                "outputs/derived/README.md", "outputs/derived/brief-template.md"]:
        (out / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(ROOT / rel, out / rel)
    shutil.copy(ROOT / "README.md", out / "index.md")
    for guide in (out / "docs").rglob("*.md"):
        text = guide.read_text(encoding="utf-8")
        guide.write_text(text.replace("../../README.md", "../../index.md"), encoding="utf-8")

    def link(nid: str) -> str:
        n = nodes.get(nid)
        return f"[{n.title}]({nid}.md) `{nid}`" if n else f"`{nid}` (missing)"

    for n in nodes.values():
        page = f"# {n.title}\n\n"
        page += f"**{n.id}** · {LEVEL_NAMES[n.level]} · {TASKS[n.task]} · {STATUS_BADGE.get(n.status, n.status)}"
        if n.meta.get("example"):
            page += " · example content"
        page += "\n\n"
        page += clean(n.body) + "\n"
        rel_lines = []
        for rel in RELATIONS:
            for t in n.rel(rel):
                rel_lines.append(f"- {rel} → {link(t)}")
        if rel_lines:
            page += "## Links from this node\n\n" + "\n".join(rel_lines) + "\n\n"
        back = []
        for rel, ids in n.reverse.items():
            for s in sorted(ids):
                back.append(f"- {link(s)} ({rel})")
        if back:
            page += "## Linked from\n\n" + "\n".join(back) + "\n\n"
        srcs = n.meta.get("sources") or []
        if srcs:
            page += "## Sources\n\n" + "\n".join(
                f"- `{s.get('ref')}` {s.get('locator', '')}" for s in srcs if isinstance(s, dict)
            ) + "\n\n"
        page += f"*Edit the source: `{n.rel_path}`*\n"
        (out / "framework" / f"{n.id}.md").write_text(page, encoding="utf-8")

    overview = "# Framework overview\n\n"
    for level, lname in LEVEL_NAMES.items():
        overview += f"## {lname}\n\n"
        for task in TASKS:
            items = select(nodes, {"level": level, "task": task})
            if items:
                overview += f"**{TASKS[task]}**\n\n" + "\n".join(
                    f"- {link(i.id)} {STATUS_BADGE.get(i.status, '')}" for i in items
                ) + "\n\n"
    overview += "## Relations (Mermaid)\n\n```mermaid\ngraph BT\n"
    for n in nodes.values():
        overview += f'  {n.id.replace("-", "_")}["{n.title}"]\n'
    for n in nodes.values():
        for rel in RELATIONS:
            for t in n.rel(rel):
                if t in nodes:
                    overview += f'  {n.id.replace("-", "_")} -- {rel} --> {t.replace("-", "_")}\n'
    overview += "```\n"
    (out / "framework" / "index.md").write_text(overview, encoding="utf-8")

    ai = BUILD / "ai"
    if ai.exists():
        shutil.copytree(ai, out / "ai")
        shutil.copy(ai / "llms.txt", out / "llms.txt")
    print(f"wrote {out.relative_to(ROOT)}/ ({len(nodes)} node pages)")


# --------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("validate")
    rp = sub.add_parser("report")
    rp.add_argument("outline", type=Path)
    rp.add_argument("--formats", default="", help="comma-separated pandoc formats, e.g. docx,html")
    sub.add_parser("export")
    sub.add_parser("wiki")
    ap_all = sub.add_parser("all")
    ap_all.add_argument("--formats", default="")
    args = ap.parse_args()

    nodes = load_nodes()
    if args.cmd == "validate":
        return validate(nodes)
    if args.cmd == "report":
        build_report(args.outline, nodes, [f for f in args.formats.split(",") if f])
        return 0
    if args.cmd == "export":
        export(nodes)
        return 0
    if args.cmd == "wiki":
        export(nodes)
        wiki(nodes)
        return 0
    if args.cmd == "all":
        rc = validate(nodes)
        if rc:
            return rc
        for outline in sorted((ROOT / "outputs").glob("*/outline.yaml")):
            build_report(outline, nodes, [f for f in args.formats.split(",") if f])
        export(nodes)
        wiki(nodes)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
