<div align="center">
  <img src="docs/assets/images/logo.svg" width="108" alt="LiDAR Research Atlas logo">
  <h1>LiDAR Research Atlas</h1>
  <p><strong>Indoor and outdoor 2D/3D datasets, methods, benchmarks, and lawful access guides.</strong></p>
  <p>
    <a href="https://github.com/das-swagat/lidar-research-atlas/actions/workflows/validate.yml"><img alt="Validation" src="https://img.shields.io/github/actions/workflow/status/das-swagat/lidar-research-atlas/validate.yml?branch=main&label=catalog%20validation"></a>
    <a href="https://github.com/das-swagat/lidar-research-atlas/releases"><img alt="Release" src="https://img.shields.io/github/v/release/das-swagat/lidar-research-atlas?include_prereleases"></a>
    <a href="LICENSE"><img alt="Code license" src="https://img.shields.io/badge/code-Apache--2.0-blue"></a>
    <a href="LICENSE-CONTENT.md"><img alt="Content license" src="https://img.shields.io/badge/docs%20%26%20metadata-CC%20BY%204.0-green"></a>
    <a href="CITATION.cff"><img alt="Citation" src="https://img.shields.io/badge/citation-CFF-orange"></a>
  </p>
</div>

![LiDAR Research Atlas overview](docs/assets/images/hero.svg)

## Purpose

LiDAR research is fragmented across provider portals, benchmark sites, papers, repositories, cloud buckets, and institution-specific agreements. This atlas organizes those sources into a provenance-tracked scholarly catalog while preserving the authorship, licenses, and access controls of the original contributors.

The project **links; it does not redistribute**. Each record identifies authoritative sources, original contributors, sensor/domain scope, legal access route, commercial-use and redistribution status, required citations, implementation relationship, and verification date.

## Coverage

| Dimension | Included examples |
|---|---|
| Geometry | 2D planar laser scans; 3D mobile, terrestrial, airborne, and automotive point clouds |
| Environments | Indoor, outdoor, urban, road, campus, off-road, aerial, industrial-adjacent |
| Tasks | SLAM, odometry, mapping, localization, registration, segmentation, detection, tracking, self-supervised learning |
| Resource types | Datasets, methods, official/author-maintained/community implementations, benchmark portals, access guides |

Adjacent RGB-D or photogrammetric resources are included only where they are widely used in transferable 3D learning, and are explicitly labeled as non-LiDAR.

## Start here

- **Documentation site:** `docs/index.md` or GitHub Pages after deployment.
- **Dataset catalog:** `catalog/datasets/`
- **Method catalog:** `catalog/methods/`
- **Lawful download workflow:** `docs/guides/lawful-download-workflow.md`
- **Provenance policy:** `policies/PROVENANCE_POLICY.md`
- **Corrections/takedowns:** `policies/CORRECTIONS_AND_TAKEDOWNS.md`
- **How to contribute:** `CONTRIBUTING.md`

## Citation principle

Researchers must cite the **original dataset and method publications** used in their work. Cite this atlas additionally only when its taxonomy, metadata, access guide, software, or analysis materially supported the work. See `CITATION.cff` and `docs/guides/citation.md`.

## Local preview

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/build_catalog.py
mkdocs serve
```

## Project status

Version **0.1.0** is a professional starter release, not an exhaustive census. Records marked `partial` are retained transparently and must be re-verified before a stable 1.0 scholarly release.

## Licensing

Original software is Apache-2.0. Original documentation and curated metadata are CC BY 4.0. Third-party resources remain under their respective owners' terms. See `LICENSE`, `LICENSE-CONTENT.md`, `THIRD_PARTY_NOTICES.md`, and `DISCLAIMER.md`.
