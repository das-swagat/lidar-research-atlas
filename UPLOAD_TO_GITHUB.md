# Upload or update the GitHub repository

## Existing v0.1.x repository

Use [UPDATE_FROM_V0.1.0.md](UPDATE_FROM_V0.1.0.md). Its `rsync` command preserves the existing `.git` directory, remotes, branch tracking, and repository-local Git identity. Review the diff before committing.

## New repository

```bash
git init -b main
git add -A
git commit -m "Initial LiDAR Research Atlas release"
git remote add origin git@github.com:das-swagat/lidar-research-atlas.git
git push -u origin main
```

Do not initialize the remote with a separate README, license, or `.gitignore`. Enable GitHub Pages with **GitHub Actions** as the source. Add the repository description, homepage URL, relevant topics, and `docs/assets/images/social-card.png` as the social preview.

## Release

After validation passes, create the intended version tag and attach a clean `git archive` package plus its SHA-256 checksum. Do not describe `discovery_only` or `source_listed` records as independently verified.
