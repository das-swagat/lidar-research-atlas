# LiDAR Research Atlas audit report

**Package:** v0.2.0 expanded candidate
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

## Build limitation

A strict local MkDocs build could not be executed in the packaging container because the container package index did not expose the declared MkDocs distributions. The repository workflows install the declared dependencies and run `mkdocs build --strict` on GitHub Actions. This limitation is environmental and is not represented as a successful local documentation build.

## External-link limitation

The package does not claim that every external provider URL was successfully fetched from the packaging container. Provider sites may block automated requests, require JavaScript or registration, move content, or change terms. A scheduled non-failing source-link audit is included, and all audit results require manual interpretation.

## Legal and scholarly boundary

The package does not host third-party datasets, labels, point clouds, archives, model weights, provider logos, copied paper figures, or copied upstream prose. Newly expanded records are conservatively labeled `discovery_only` or `source_listed`; those statuses are discovery leads, not completed license, access, maintenance, or authorship determinations. Provider terms and original citation instructions control.

## Release decision

Suitable as an expanded v0.2.0 candidate after reviewing the generated diff and running the strict MkDocs build in GitHub Actions. Do not describe the catalog as legally guaranteed, exhaustive, or fully verified.
