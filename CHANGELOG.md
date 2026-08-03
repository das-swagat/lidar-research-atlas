# Changelog

## [0.2.0] - 2026-08-03

### Added
- Expanded the dataset catalog from 27 to 85 records.
- Expanded the method catalog from 27 to 53 records.
- Added 69 ecosystem records covering manufacturers, libraries, frameworks, simulators, tools, and related lists.
- Added searchable catalog tables, source-list comparison, coverage report, ecosystem CSV export, and monthly source-link audit workflow.
- Added explicit discovery-only verification and conservative provider-controlled access labels.

### Changed
- Updated the homepage and README with a futuristic original LiDAR illustration and broader search-oriented scope.
- Regenerated source register, JSON/CSV exports, documentation pages, and validation tests.

### Legal and provenance
- Added upstream source-list acknowledgements without reproducing abstracts, figures, screenshots, or README prose.
- Added discovery-layer rules to provenance and contribution policies.

All notable changes are documented here. This project follows Semantic Versioning where practical.

## [0.1.0] — 2026-08-03

### Added
- Professional MkDocs Material documentation site and static preview.
- Starter catalog spanning indoor/outdoor, 2D/3D, mobile, terrestrial, aerial, and adjacent RGB-D/photogrammetric resources.
- Method catalog spanning SLAM, odometry, registration, segmentation, detection, and self-supervised learning.
- Per-entry provenance, access, license, redistribution, citation, and verification fields.
- Original explanatory SVG diagrams; no copied paper figures or dataset files.
- Validation, restricted-file scanning, URL auditing, tests, issue templates, and GitHub Actions.
- Release, GitHub Pages, Zenodo, ResearchGate, attribution, correction, and takedown guidance.

### Fixed
- Anchored protected storage-directory rules at the repository root so curated `catalog/datasets/` records and generated `docs/catalog/datasets/` pages are tracked normally.
- Removed local test and bytecode caches from the distributable archive.
- Rebuilt the package manifest from the complete clean file tree.

### Status
This is a curated starter release, not an exhaustive census. Records marked `partial` require source re-verification before a stable 1.0 release.
