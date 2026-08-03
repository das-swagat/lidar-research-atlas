# Package audit report

**Release candidate:** v0.1.0  
**Audit date:** 2026-08-03

## Passed locally

- Catalog schema validation: 54 records.
- Generated-page parity: 54 resource pages.
- Restricted-file and credential scan.
- Internal Markdown link validation.
- Python syntax compilation.
- Unit tests: 4 passed.
- MkDocs configuration parsing and navigation target verification.
- GitHub Actions workflow YAML parsing.
- CSV/JSON export generation.
- Original SVG-to-PNG social and logo asset rendering.
- Git ignore path audit: all 27 dataset source records and 28 generated dataset pages are included; only root-level private data-storage directories are excluded.
- Clean-package audit: test caches and Python bytecode are absent from the distributable archive.
- Package manifest rebuilt from the complete clean file tree.

## Catalog status

- Dataset records: 27.
- Method records: 27.
- Records labeled `verified`: 43.
- Records labeled `partial`: 11.
- Third-party data files hosted: 0.

## Build limitation in this environment

The local execution environment could not download MkDocs packages from its package index, so `mkdocs build --strict` was not executed locally. The configuration was parsed independently, all navigation paths were checked, and the included GitHub Actions workflows install the declared packages and run the strict build after upload.

## Release condition

Do not describe v0.1.0 as exhaustive. Re-run the URL audit and manually revisit records marked `partial` before a stable 1.0 release or a quantitative publication based on catalog completeness.
