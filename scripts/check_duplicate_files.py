import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".venv", "site", "__pycache__", ".pytest_cache"}

duplicates = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in SKIP for part in path.parts):
        continue
    if re.search(r" \d+(?=\.[^.]+$)", path.name):
        duplicates.append(path.relative_to(ROOT))

if duplicates:
    print("Accidental duplicate-copy filenames found:")
    for path in duplicates:
        print(f"  - {path}")
    raise SystemExit(1)

print("Duplicate-copy filename check passed")
