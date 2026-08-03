# Release checklist

- [ ] Run `make validate`, `make test`, and `mkdocs build --strict`.
- [ ] Resolve or document URL-audit failures.
- [ ] Confirm no dataset files, weights, credentials, signed URLs, or third-party figures are present.
- [ ] Recheck every record changed since the previous release against authoritative sources.
- [ ] Update `CHANGELOG.md`, `CITATION.cff`, `.zenodo.json`, and version fields.
- [ ] Review `THIRD_PARTY_NOTICES.md` and media register.
- [ ] Create an annotated Git tag such as `v0.1.0`.
- [ ] Publish GitHub release notes and attach only atlas-generated metadata/documentation artifacts.
- [ ] After public release, enable Zenodo archival and add the assigned DOI to citation files.
- [ ] Publish a separate ResearchGate data item or technical report only after the archived release is stable.
