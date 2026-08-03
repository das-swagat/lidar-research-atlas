# LiDAR Research Atlas v0.2.1

v0.2.1 is a site-integrity and release-quality hotfix for the 207-record v0.2.0 expansion.

## Fixed

- Catalog tables now render as HTML on the deployed MkDocs site.
- Dataset, method, and ecosystem filters are operational.
- Dataset and method status cards include verified, partial, and discovery-only counts.
- Ecosystem statistics use a responsive dedicated layout.
- Generated CSV exports use consistent LF line endings.

## Reliability and maintenance

- Added duplicate-copy filename detection.
- Added rendered-site regression checks.
- CI now detects stale generated pages and exports.
- GitHub Pages deployment repeats the full validation gate.
- Obsolete setup artifacts and the unused static preview were removed.
- The homepage hero was reduced from 2.6 MB to approximately 429 KB using WebP.

Catalog scope remains unchanged at 85 datasets, 53 methods, and 69 ecosystem resources.
