.PHONY: install validate build serve test audit clean
install:
	python -m pip install -r requirements-dev.txt
validate:
	python scripts/validate_catalog.py
	python scripts/check_no_restricted_files.py
	python scripts/check_internal_links.py
build:
	python scripts/build_catalog.py
	python scripts/export_catalog.py
	mkdocs build --strict
audit:
	python scripts/check_urls.py --report link-audit.json
test:
	pytest
serve:
	python scripts/build_catalog.py
	mkdocs serve
clean:
	rm -rf site .pytest_cache __pycache__ scripts/__pycache__ tests/__pycache__
