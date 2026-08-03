# Security policy

Report suspected credentials, malicious links, unsafe downloads, compromised provider pages, or supply-chain concerns privately through GitHub Security Advisories when possible. Do not place secrets or exploit details in public issues.

## Supported version

The latest published release and the current `main` branch are supported. Scheduled Dependabot version-update pull requests are disabled to avoid unattended dependency churn; dependency changes are reviewed manually and validated before merge. GitHub Actions validation and a scheduled source-link audit remain enabled.

## Repository safety boundary

The repository must never contain third-party datasets, point-cloud archives, labels, executable downloads from unverified sources, model weights, credentials, signed URLs, or access tokens. The restricted-file scanner is a defense-in-depth control and does not replace human review.
