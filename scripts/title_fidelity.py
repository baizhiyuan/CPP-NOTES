#!/usr/bin/env python3
"""title_fidelity.py — verify every section heading from the legacy chapter
still appears (possibly rephrased) in the upgraded chapter.

Usage:
  python scripts/title_fidelity.py <legacy_ref> <chapter_md>

Exit codes:
  0  coverage >= 95%
  1  coverage < 95%
  2  bad arguments / git error

Match threshold = ratio >= 0.80.
Uses python-Levenshtein when available; otherwise stdlib difflib (plan A.5
allows that single pip dep, but stdlib path keeps verification runnable on
fresh clones without extra installs).
"""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

try:
    import Levenshtein  # type: ignore

    def ratio(a: str, b: str) -> float:
        return Levenshtein.ratio(a, b)
except ImportError:
    from difflib import SequenceMatcher

    def ratio(a: str, b: str) -> float:
        return SequenceMatcher(None, a, b).ratio()


HEADING_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")


def extract_headings(text: str) -> list[str]:
    return [m.group(2).strip() for m in (HEADING_RE.match(l) for l in text.splitlines()) if m]


def fetch_legacy(ref: str, path: str) -> str:
    out = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return out.stdout


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write("usage: title_fidelity.py <legacy_ref> <chapter_md>\n")
        return 2
    ref, chapter_path = argv[1], argv[2]
    chapter = Path(chapter_path)
    if not chapter.exists():
        sys.stderr.write(f"not found: {chapter}\n")
        return 2

    try:
        legacy_text = fetch_legacy(ref, str(chapter))
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"git show failed: {exc.stderr}\n")
        return 2

    legacy = extract_headings(legacy_text)
    current = extract_headings(chapter.read_text(encoding="utf-8"))

    if not legacy:
        sys.stdout.write("legacy has 0 headings; trivially pass\n")
        return 0

    missing: list[str] = []
    for lh in legacy:
        if any(ratio(lh, ch) >= 0.80 for ch in current):
            continue
        missing.append(lh)

    matched = len(legacy) - len(missing)
    coverage = matched / len(legacy)
    sys.stdout.write(f"{chapter}: {matched}/{len(legacy)} legacy headings matched ({coverage:.0%})\n")
    if missing:
        sys.stderr.write("missing headings:\n")
        for m in missing:
            sys.stderr.write(f"  - {m}\n")
    return 0 if coverage >= 0.95 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
