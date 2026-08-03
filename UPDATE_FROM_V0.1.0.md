# Update an existing v0.1.x working copy to the v0.2.0 candidate

This package is a complete repository snapshot. Preserve the existing `.git` directory and local Git configuration.

On macOS, after downloading and extracting the package:

```bash
cd "$HOME/Desktop/My Github/lidar-research-atlas"
git status --short
```

Commit or back up any local changes before continuing. Then synchronize the extracted package into the working repository:

```bash
rsync -a --delete \
  --exclude='.git/' \
  "/PATH/TO/lidar-research-atlas-v0.2.0-expanded/" \
  "$HOME/Desktop/My Github/lidar-research-atlas/"
```

Validate before committing:

```bash
cd "$HOME/Desktop/My Github/lidar-research-atlas"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/validate_catalog.py
python scripts/build_catalog.py --check
python scripts/check_internal_links.py
python scripts/check_no_restricted_files.py
python -m pytest -q
mkdocs build --strict
```

Review `git diff --stat`, then commit on a feature branch or according to the repository's branch-protection rules. Do not overwrite or move `.git`.
