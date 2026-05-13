#!/usr/bin/env bash
# verify_all.sh — orchestrate all CPP-NOTES quality checks.
#
# Runs every script in scripts/ across every chapter, plus link checks
# on README / docs / drawio. Designed for pre-push and for Phase D-review.
#
# Usage:
#   bash scripts/verify_all.sh             # quiet on PASS, verbose on FAIL
#   bash scripts/verify_all.sh -v          # verbose
#
# Exit codes:
#   0  all checks pass
#   1  one or more checks failed
#   2  bad arguments / environment

set -uo pipefail

VERBOSE=0
if [[ "${1:-}" == "-v" ]]; then VERBOSE=1; fi

cd "$(dirname "$0")/.."

FAIL=0
TOTAL=0
PASS=0
log() { [[ $VERBOSE -eq 1 ]] && echo "[ok]   $1"; }
fail() { echo "[FAIL] $1" >&2; FAIL=$((FAIL+1)); }
section() { echo ""; echo "=== $1 ==="; }

# 1. Title fidelity (every legacy chapter must still match in upgraded)
section "title_fidelity (every chapter ≥ 95% legacy heading coverage)"
for f in chapter/*.md; do
  TOTAL=$((TOTAL+1))
  if python3 scripts/title_fidelity.py legacy "$f" >/dev/null 2>&1; then
    PASS=$((PASS+1)); log "$f"
  else
    fail "$f"
  fi
done

# 2. Audit chapter (fidelity ≥ 0.9 + H2 superset)
section "audit_chapter (fidelity ≥ 0.9 + H2 superset)"
for f in chapter/*.md; do
  TOTAL=$((TOTAL+1))
  if python3 scripts/audit_chapter.py "$f" >/dev/null 2>&1; then
    PASS=$((PASS+1)); log "$f"
  else
    fail "$f"
  fi
done

# 3. Cross-link / URL-encode round-trip
section "check_links (URL-encode round-trip + existence)"
for target in README.md CONTRIBUTING.md docs/ chapter/ drawio/; do
  if [[ -e $target ]]; then
    TOTAL=$((TOTAL+1))
    if python3 scripts/check_links.py "$target" "$(pwd)" >/dev/null 2>&1; then
      PASS=$((PASS+1)); log "$target"
    else
      fail "$target"
    fi
  fi
done

# 4. README TOC anchor set ⊇ legacy
section "README anchor set ⊇ legacy README anchor set"
if [[ -f README.md ]]; then
  TOTAL=$((TOTAL+1))
  legacy_set=$(git show legacy:README.md 2>/dev/null | python3 scripts/anchor_set.py - 2>/dev/null | sort -u)
  new_set=$(python3 scripts/anchor_set.py README.md | sort -u)
  if [[ -z $legacy_set ]] || diff <(echo "$legacy_set") <(echo "$new_set" | grep -F -x -f <(echo "$legacy_set")) >/dev/null; then
    PASS=$((PASS+1)); log "README"
  else
    fail "README (missing anchors vs legacy)"
  fi
fi

# 5. drawio SVG sanity
section "drawio SVG xml parse"
if compgen -G "drawio/*.svg" > /dev/null; then
  for f in drawio/*.svg; do
    TOTAL=$((TOTAL+1))
    if python3 -c "import xml.etree.ElementTree as ET; ET.parse('$f')" >/dev/null 2>&1; then
      PASS=$((PASS+1)); log "$f"
    else
      fail "$f"
    fi
  done
fi

# 6. Branch invariants
section "branch invariants"
TOTAL=$((TOTAL+1))
legacy_rev=$(git rev-parse legacy 2>/dev/null || true)
if [[ $legacy_rev == "d204347814323e7c76ec032a24a0a9a9b081b355" ]]; then
  PASS=$((PASS+1)); log "legacy == d204347"
else
  fail "legacy != d204347 (was $legacy_rev)"
fi

# 7. No accidental push
section "push hygiene"
TOTAL=$((TOTAL+1))
if ! git reflog 2>/dev/null | grep -q push; then
  PASS=$((PASS+1)); log "no push in reflog"
else
  fail "push detected in reflog"
fi

echo ""
echo "===================="
echo "verify_all: $PASS / $TOTAL passed; $FAIL failure(s)"
echo "===================="

exit $(( FAIL == 0 ? 0 : 1 ))
