#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PACKAGE_MANIFEST.json"


def repository_paths():
    raw = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
    )
    paths = [Path(os.fsdecode(item)) for item in raw.split(b"\0") if item]
    return sorted(path for path in paths if path != MANIFEST.relative_to(ROOT))


def build_payload():
    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text())
    entries = []
    total_bytes = 0

    for relative in repository_paths():
        path = ROOT / relative
        if not path.is_file():
            continue
        content = path.read_bytes()
        total_bytes += len(content)
        entries.append(
            {
                "path": relative.as_posix(),
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
            }
        )

    counts = {
        kind: len(list((ROOT / "catalog" / kind).glob("*.yml")))
        for kind in ("datasets", "methods", "ecosystem")
    }
    counts["total"] = sum(counts.values())

    payload = {
        "project": citation["title"],
        "version": str(citation["version"]),
        "package_label": "site-integrity hotfix",
        "package_revision": 1,
        "created": str(citation["date-released"]),
        "manifest_scope": "All packaged files except PACKAGE_MANIFEST.json itself",
        "file_count": len(entries),
        "total_bytes": total_bytes,
        "catalog_counts": counts,
        "files": entries,
    }

    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    payload = build_payload()
    rendered = json.dumps(payload, indent=2) + "\n"

    if args.check:
        if not MANIFEST.exists() or MANIFEST.read_text() != rendered:
            raise SystemExit("Package manifest is stale. Run python scripts/build_manifest.py")
        print(f"Package manifest current for {payload['file_count']} files")
        return

    MANIFEST.write_text(rendered)
    print(f"Manifest generated for {payload['file_count']} files")


if __name__ == "__main__":
    main()
