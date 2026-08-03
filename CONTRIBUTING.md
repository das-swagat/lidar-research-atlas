# Contributing

Contributions are welcome through the structured issue forms and pull requests.

## Required evidence
Every dataset or method entry must include an authoritative landing page, primary paper or canonical technical source, original creators, access/implementation relationship, license or terms source, recommended citation, and verification date.

## Prohibited content
Do not upload datasets, labels, scans, model weights, credentials, signed URLs, copied paper figures, proprietary documentation, or archives. Do not mark a community implementation as official.

## Workflow
1. Open the relevant issue form.
2. Add or edit one YAML record.
3. Run `make validate` and `make test`.
4. Generate pages with `python scripts/build_catalog.py`.
5. Submit a focused pull request and identify every primary source used.

By contributing original prose, metadata, or diagrams, you agree that it may be distributed under `LICENSE-CONTENT.md`. Code contributions are under Apache-2.0.

## Expansion-source rule

Do not copy abstracts, README paragraphs, tables, screenshots, figures, or badges from another curated list. A source list may identify a candidate, but the pull request must provide an official project/provider URL and independently written metadata. Add the discovery collection to `discovery_sources` or `source_collections`, and use `discovery_only` until access, citation, and license fields are reviewed directly.
