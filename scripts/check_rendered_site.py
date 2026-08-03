import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "docs/assets/catalog.json").read_text())
errors = []

targets = {
    "datasets": "dataset-table",
    "methods": "method-table",
    "portals": "portal-table",
    "ecosystem": "ecosystem-table",
}

filter_kinds = {"datasets", "methods", "ecosystem"}

for kind, target in targets.items():
    page = ROOT / "site" / "catalog" / kind / "index.html"
    if not page.exists():
        errors.append(f"missing rendered page: {page.relative_to(ROOT)}")
        continue

    html = page.read_text(encoding="utf-8")

    if "<table" not in html:
        errors.append(f"{kind}: rendered HTML table missing")
    if "|---|" in html:
        errors.append(f"{kind}: raw Markdown table remains")
    wrapper_tokens = (
        f'id="{target}"',
        f"id='{target}'",
        f"id={target}",
    )
    if not any(token in html for token in wrapper_tokens):
        errors.append(f"{kind}: table wrapper #{target} missing")

    if "atlas-table-wrap" not in html:
        errors.append(f"{kind}: full-width table class missing")

    if kind in filter_kinds:
        filter_tokens = (
            f'data-atlas-filter="{target}"',
            f"data-atlas-filter='{target}'",
            f"data-atlas-filter={target}",
        )
        if not any(token in html for token in filter_tokens):
            errors.append(f"{kind}: filter target missing")

for kind, noun in (("datasets", "dataset"), ("methods", "method")):
    html = (ROOT / "site" / "catalog" / kind / "index.html").read_text()
    items = catalog[kind]
    counts = Counter(item["verification"]["status"] for item in items)

    expected = [
        (len(items), f"{noun} records"),
        (counts["verified"], "verified"),
        (counts["partial"], "partial"),
        (counts["discovery_only"], "discovery-only"),
    ]

    for value, label in expected:
        token = f"<strong>{value}</strong><span>{label}</span>"
        if token not in html:
            errors.append(f"{kind}: missing card {value} {label}")

eco_html = (ROOT / "site/catalog/ecosystem/index.html").read_text()
if "atlas-stat-grid--ecosystem" not in eco_html:
    errors.append("ecosystem: dedicated responsive card grid missing")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    raise SystemExit(1)

print("Rendered-site integrity check passed")
