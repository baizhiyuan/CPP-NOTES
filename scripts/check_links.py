#!/usr/bin/env python3
"""check_links.py — verify relative links in Markdown/HTML files are URL-encoded
correctly (round-trip safe) and resolve to existing files.

Usage:
  python scripts/check_links.py <file>
  python scripts/check_links.py <dir>
  python scripts/check_links.py <file> <root1> ...

Exit codes:
  0  all links resolved + round-trip stable
  1  one or more links broken or unstable
  2  bad arguments
"""
from __future__ import annotations
import re
import sys
import urllib.parse
from pathlib import Path

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HTML_LINK = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""")


def iter_files(target: Path):
    if target.is_file():
        yield target
        return
    for pattern in ("*.md", "*.html"):
        yield from target.rglob(pattern)


def extract(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    links: list[str] = []
    if path.suffix.lower() in {".md", ".markdown"}:
        links.extend(MD_LINK.findall(text))
    if path.suffix.lower() in {".html", ".htm"}:
        links.extend(HTML_LINK.findall(text))
    return links


def is_external(url: str) -> bool:
    return url.startswith(("http://", "https://", "mailto:", "#", "data:"))


def round_trip_ok(url: str) -> bool:
    enc = urllib.parse.quote(url, safe="/.-_~#?&=")
    return urllib.parse.unquote(enc) == url


def resolve(path: Path, url: str, roots: list[Path]) -> Path | None:
    url = url.split("#", 1)[0].split("?", 1)[0]
    if not url:
        return path
    candidates = [path.parent / urllib.parse.unquote(url)]
    for r in roots:
        candidates.append(r / urllib.parse.unquote(url))
    for c in candidates:
        if c.exists():
            return c
    return None


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        sys.stderr.write("usage: check_links.py <file_or_dir> [<root>...]\n")
        return 2
    target = Path(argv[1])
    roots = [Path(a) for a in argv[2:]]
    if not target.exists():
        sys.stderr.write(f"not found: {target}\n")
        return 2

    fail = 0
    total = 0
    for f in iter_files(target):
        for url in extract(f):
            if is_external(url):
                continue
            total += 1
            if not round_trip_ok(url):
                sys.stderr.write(f"[unstable encoding] {f}: {url}\n")
                fail += 1
                continue
            if resolve(f, url, roots) is None:
                sys.stderr.write(f"[broken]            {f}: {url}\n")
                fail += 1
    sys.stdout.write(f"checked {total} link(s); {fail} failure(s)\n")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
