# Release checklist

- [ ] Confirm `git status --short` is empty.
- [ ] Run catalog generation, export, schema validation, internal-link checks, tests, and restricted-file scanning.
- [ ] Run `mkdocs build --strict` in an environment with the declared dependencies.
- [ ] Review all new `discovery_only`, `source_listed`, and `partial` records for accurate status labeling.
- [ ] Review third-party notices, media provenance, disclaimer, correction/takedown process, and licenses.
- [ ] Run the external URL audit and manually review failures, redirects, bot blocks, and provider-term changes.
- [ ] Rebuild `PACKAGE_MANIFEST.json` after all file changes.
- [ ] Create the archive from the exact intended commit and publish its SHA-256 checksum.
- [ ] Create an annotated version tag and matching GitHub release.
- [ ] After Zenodo assigns a DOI, update `CITATION.cff`, `.zenodo.json`, citation docs, and README.
