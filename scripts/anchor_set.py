#!/usr/bin/env python3
"""anchor_set.py — extract Markdown headings (## and ###) into a sorted anchor set.

Usage:
  python scripts/anchor_set.py README.md
  python scripts/anchor_set.py -          # read from stdin
  git show legacy:README.md | python scripts/anchor_set.py -

Output: one heading text per line (without leading #s), sorted.

Used by Phase G AC-README-TOC verification.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path


HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")
# Markdown link text: capture the [text] portion of [text](url)
LINK_RE = re.compile(r"\[([^\]\n]+)\]\([^)\s]+\)")


def _strip_emoji_and_md(s: str) -> str:
    # remove [text](url) wrapper to expose plain text inside headings
    s = LINK_RE.sub(r"\1", s)
    return s.strip()


def extract(text: str) -> list[str]:
    """Extract anchor-like strings: ## / ### heading text AND any [text](url) link text.

    Both are 'anchors' in different senses; legacy README uses '## [Title](path)'
    style while the upgraded README puts chapter links in a table. Capturing both
    forms keeps AC-README-TOC stable across reorganizations.
    """
    anchors: set[str] = set()
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            anchors.add(_strip_emoji_and_md(m.group(2)))
        for link_text in LINK_RE.findall(line):
            anchors.add(link_text.strip())
    return sorted(anchors)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: anchor_set.py <markdown_file_or_->\n")
        return 2
    arg = argv[1]
    if arg == "-":
        text = sys.stdin.read()
    else:
        p = Path(arg)
        if not p.exists():
            sys.stderr.write(f"file not found: {arg}\n")
            return 2
        text = p.read_text(encoding="utf-8")
    for a in sorted(set(extract(text))):
        print(a)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
