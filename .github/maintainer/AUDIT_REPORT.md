# LiDAR Research Atlas audit report

**Package:** v0.2.1 site-integrity hotfix
**Audit date:** 2026-08-03
**Structured records:** 207 (85 datasets, 53 methods, 69 ecosystem resources)

## Completed checks

- Catalog schema validation passed for all 207 records.
- Generated-page consistency check passed for datasets, methods, and ecosystem resources.
- Internal Markdown-link validation passed.
- Six automated tests passed.
- Python source compilation passed.
- Restricted-file, archive, model-weight, credential, and signed-URL scanning passed.
- IDs and names are unique across the structured catalog.
- Catalog URLs are syntactically valid HTTP(S) URLs.
- Generated CSV and JSON exports match the structured catalog counts.
- GSeg3D and RESPLE publication/implementation links were corrected after direct source review.

## Build verification

A strict local MkDocs build completed successfully with the declared dependencies. The validation and deployment workflows repeat catalog generation, export consistency, tests, restricted-file scanning, internal-link checks, rendered-site integrity checks, and `mkdocs build --strict`.

## External-link limitation

The package does not claim that every external provider URL was successfully fetched from the packaging container. Provider sites may block automated requests, require JavaScript or registration, move content, or change terms. A scheduled non-failing source-link audit is included, and all audit results require manual interpretation.

## Legal and scholarly boundary

The package does not host third-party datasets, labels, point clouds, archives, model weights, provider logos, copied paper figures, or copied upstream prose. Newly expanded records are conservatively labeled `discovery_only` or `source_listed`; those statuses are discovery leads, not completed license, access, maintenance, or authorship determinations. Provider terms and original citation instructions control.

## Release decision

Prepared and validated as the v0.2.1 site-integrity hotfix. Publication requires successful pull-request checks, merge, GitHub Pages deployment, and live-site verification. Do not describe the catalog as legally guaranteed, exhaustive, or fully verified.
