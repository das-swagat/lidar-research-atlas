# Upload and publish the repository

## 1. Review local identity fields
Search the package for `das-swagat`, `Swagat Das`, and the planned site URL. Update only if your public naming differs.

## 2. Create the repository
On GitHub, create a **public** repository named `lidar-research-atlas`. Do not initialize it with another README, license, or `.gitignore` because this package already contains them.

## 3. Push from Terminal

```bash
git init -b main
git add .
git commit -m "Initial scholarly atlas release v0.1.0"
git remote add origin git@github.com:das-swagat/lidar-research-atlas.git
git push -u origin main
```

## 4. Configure the About panel
Use the description, website, and topics listed in `docs/about/repository-settings.md`. Upload `docs/assets/images/social-card.png` as the social preview.

## 5. Enable GitHub Pages
Open **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**. The included documentation workflow will deploy after a push to `main`.

## 6. Protect `main`
Create a branch ruleset requiring pull requests and the validation workflow. Block force pushes and branch deletion.

## 7. Publish release v0.1.0
After Actions pass, create tag/release `v0.1.0`. Use the changelog text and clearly call it a curated starter release—not exhaustive.

## 8. Connect Zenodo
After the public GitHub repository exists, authorize Zenodo's GitHub integration, enable this repository, then create a new GitHub release to archive it. Add the assigned DOI to `CITATION.cff`, `.zenodo.json`, README badges, and documentation.

## 9. ResearchGate
After the DOI-backed release is frozen, publish only your original atlas metadata, schema, methodology, and charts as a data item or technical report. Do not upload third-party datasets, labels, scans, weights, or copied figures.
