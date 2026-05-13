#!/usr/bin/env python3
"""audit_chapter.py — static structural audit of an upgraded chapter against
its legacy version. Emits a JSON fidelity report.

Three deterministic checks:
  1. Trigram coverage of legacy non-empty paragraphs in upgraded text (≥ 0.90).
  2. Key API / concept name preservation (loaded from drawio/CONCEPTS.md).
  3. H2 (##) headings: upgraded ⊇ legacy.

Usage:
  python scripts/audit_chapter.py <chapter_md> [--legacy-ref legacy] [--concepts drawio/CONCEPTS.md] [--threshold 0.90]

Output (stdout): JSON document.

Exit codes:
  0  fidelity_score >= threshold and h2_superset == True
  1  one or more checks failed
  2  bad arguments / git error
"""
from __future__ import annotations
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
WORDLIKE_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_:<>]+")


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def trigrams(text: str) -> set[str]:
    text = re.sub(r"\s+", "", text)
    return {text[i:i + 3] for i in range(len(text) - 2)} if len(text) >= 3 else set()


def trigram_coverage(legacy_paras: list[str], upgraded_text: str) -> float:
    upgraded = re.sub(r"\s+", "", upgraded_text)
    covered = 0
    total = 0
    for p in legacy_paras:
        total += 1
        tg = trigrams(p)
        if not tg:
            covered += 1
            continue
        hits = sum(1 for t in tg if t in upgraded)
        if hits / len(tg) >= 0.50:
            covered += 1
    return covered / total if total else 1.0


def load_concepts(path: Path) -> list[str]:
    if not path.exists():
        return []
    out: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("|") or line.startswith("-"):
            continue
        m = WORDLIKE_RE.findall(line)
        out.extend(m)
    return out


def concept_preservation(legacy_text: str, upgraded_text: str, concepts: list[str]) -> tuple[float, list[str]]:
    if not concepts:
        return 1.0, []
    legacy_present = [c for c in concepts if c in legacy_text]
    if not legacy_present:
        return 1.0, []
    missing = [c for c in legacy_present if c not in upgraded_text]
    kept = len(legacy_present) - len(missing)
    return kept / len(legacy_present), missing


def h2_check(legacy_text: str, upgraded_text: str) -> tuple[bool, list[str]]:
    legacy_h2 = {m.strip() for m in H2_RE.findall(legacy_text)}
    upgraded_h2 = {m.strip() for m in H2_RE.findall(upgraded_text)}
    missing = sorted(legacy_h2 - upgraded_h2)
    return (len(missing) == 0), missing


def git_show(ref: str, path: str) -> str:
    out = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    return out.stdout


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="static chapter audit")
    parser.add_argument("chapter")
    parser.add_argument("--legacy-ref", default="legacy")
    parser.add_argument("--concepts", default="drawio/CONCEPTS.md")
    parser.add_argument("--threshold", type=float, default=0.90)
    args = parser.parse_args(argv[1:])

    chapter = Path(args.chapter)
    if not chapter.exists():
        sys.stderr.write(f"not found: {chapter}\n")
        return 2

    try:
        legacy_text = git_show(args.legacy_ref, str(chapter))
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"git show failed: {exc.stderr}\n")
        return 2

    upgraded_text = chapter.read_text(encoding="utf-8")
    concepts = load_concepts(Path(args.concepts))

    cov = trigram_coverage(paragraphs(legacy_text), upgraded_text)
    pres, missing_concepts = concept_preservation(legacy_text, upgraded_text, concepts)
    h2_ok, missing_h2 = h2_check(legacy_text, upgraded_text)

    fidelity = round(0.55 * cov + 0.30 * pres + 0.15 * (1.0 if h2_ok else 0.0), 4)

    report = {
        "chapter": str(chapter),
        "legacy_ref": args.legacy_ref,
        "fidelity_score": fidelity,
        "threshold": args.threshold,
        "trigram_coverage": round(cov, 4),
        "concept_preservation": round(pres, 4),
        "missing_concepts": missing_concepts,
        "h2_superset": h2_ok,
        "missing_h2": missing_h2,
        "pass": fidelity >= args.threshold and h2_ok,
    }
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
