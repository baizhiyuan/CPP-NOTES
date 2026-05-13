# CPP-NOTES Makefile — one-liner orchestration for verification and previews.
# Usage:
#   make verify          # full check suite (chapters, links, anchors, SVGs)
#   make audit-ch CH=02  # audit a single chapter
#   make svg             # regenerate all drawio/*.svg from _mermaid/*.mmd
#   make serve           # python http server for local HTML preview
#   make clean           # remove node_modules / __pycache__ scratch dirs

.DEFAULT_GOAL := verify

PYTHON ?= python3
NPX ?= npx

verify:
	bash scripts/verify_all.sh -v

audit:
	@echo "Audit all chapters:"
	@for f in chapter/*.md; do \
		$(PYTHON) scripts/audit_chapter.py "$$f" 2>&1 | tail -1 ; \
	done

audit-ch:
	@test -n "$(CH)" || (echo "Usage: make audit-ch CH=02"; exit 1)
	$(PYTHON) scripts/audit_chapter.py chapter/$(CH).*.md

title-ch:
	@test -n "$(CH)" || (echo "Usage: make title-ch CH=02"; exit 1)
	$(PYTHON) scripts/title_fidelity.py legacy chapter/$(CH).*.md

links:
	$(PYTHON) scripts/check_links.py README.md .
	$(PYTHON) scripts/check_links.py CONTRIBUTING.md .
	$(PYTHON) scripts/check_links.py docs/ .
	$(PYTHON) scripts/check_links.py chapter/ .
	$(PYTHON) scripts/check_links.py drawio/ .

svg:
	@for f in drawio/_mermaid/*.mmd; do \
		out="drawio/$$(basename $$f .mmd).svg" ; \
		echo "regenerating $$out" ; \
		$(NPX) -y -p @mermaid-js/mermaid-cli mmdc -i "$$f" -o "$$out" --backgroundColor white ; \
	done

serve:
	@echo "Open http://localhost:8000/docs/CPP-NOTES.html in your browser"
	$(PYTHON) -m http.server 8000

clean:
	rm -rf node_modules __pycache__ scripts/__pycache__

.PHONY: verify audit audit-ch title-ch links svg serve clean
