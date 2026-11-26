#!/usr/bin/env python3
"""Compare node text with a source document, sentence by sentence.

Helps reviewers check that nodes reflect a source and add nothing to it.

    # 1. get the source as plain text, e.g. with poppler:  pdftotext -layout source.pdf source.txt
    # 2. compare it with the nodes that cite it
    python tools/source_coverage.py source.txt framework/level-*/quality/*.md

It prints two lists:

- source sentences that do not appear in any of the given nodes (missing content),
- node sentences that do not appear in the source (possible additions or paraphrases).

Matching is on word sequences (6 words) and ignores layout, case and punctuation,
so tables and headings show up as noise. It is a review aid, not a verdict.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

N = 6


def words(text: str) -> list[str]:
    text = re.sub(r"(\w)-\s+(\w)", r"\1-\2", text)
    return re.findall(r"[a-z0-9]+", text.lower())


def grams(ws: list[str]) -> set[tuple[str, ...]]:
    return {tuple(ws[i : i + N]) for i in range(len(ws) - N + 1)}


def sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+|\n\s*\n", re.sub(r"[ \t]+", " ", text)) if len(words(s)) >= N]


def coverage(sentence: str, pool: set) -> float:
    g = [tuple(w) for w in (words(sentence)[i : i + N] for i in range(len(words(sentence)) - N + 1))]
    return sum(x in pool for x in g) / len(g) if g else 1.0


def node_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    body = parts[2] if text.startswith("---") and len(parts) == 3 else text
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    return re.sub(r"^> \*\*(Example content|Stub)\b.*$", "", body, flags=re.M)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="plain-text version of the source document")
    ap.add_argument("nodes", type=Path, nargs="+", help="node files to compare")
    ap.add_argument("--threshold", type=float, default=0.8, help="share of matching word sequences (default 0.8)")
    args = ap.parse_args()

    source = args.source.read_text(encoding="utf-8")
    nodes = {p: node_body(p) for p in args.nodes if p.name.lower() != "readme.md"}
    node_pool = grams(words(" ".join(nodes.values())))
    source_pool = grams(words(source))

    src_sents = sentences(source)
    missing = [s for s in src_sents if coverage(s, node_pool) < args.threshold]
    print(f"## Source sentences not found in the nodes: {len(missing)} of {len(src_sents)}\n")
    for s in missing:
        print("-", s.strip()[:200])

    print("\n## Node sentences not found in the source\n")
    total = 0
    for path, body in nodes.items():
        extra = [s for s in sentences(body) if coverage(s, source_pool) < args.threshold]
        total += len(extra)
        for s in extra:
            print(f"- {path}: {s.strip()[:200]}")
    print(f"\n{total} node sentences not found in the source")


if __name__ == "__main__":
    main()
