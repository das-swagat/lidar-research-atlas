.PHONY: install validate build serve test lint audit clean
install:
	python -m pip install -r requirements-dev.txt
validate:
	python scripts/check_duplicate_files.py
	python scripts/validate_catalog.py
	python scripts/check_no_restricted_files.py
	python scripts/check_internal_links.py
	python scripts/build_manifest.py --check
build:
	python scripts/build_catalog.py
	python scripts/export_catalog.py
	python scripts/build_manifest.py
	mkdocs build --strict
	python scripts/check_rendered_site.py
lint:
	python -m ruff check . --select F
audit:
	python scripts/check_urls.py --report link-audit.json
test:
	pytest
serve:
	python scripts/build_catalog.py
	mkdocs serve
clean:
	rm -rf site .pytest_cache __pycache__ scripts/__pycache__ tests/__pycache__
