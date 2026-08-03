#!/usr/bin/env python3
"""Audit registered external URLs without treating bot blocks as proof of failure."""
from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "LiDAR-Research-Atlas-Link-Audit/0.2 (+scholarly metadata verification)"

parser = argparse.ArgumentParser()
parser.add_argument("--report", default="link-audit.json")
parser.add_argument("--limit", type=int, default=0)
parser.add_argument("--timeout", type=float, default=15.0)
args = parser.parse_args()

source_rows = list(csv.DictReader((ROOT / "catalog/source-register.csv").open(encoding="utf-8")))
# Audit each unique URL once while retaining all catalog references.
by_url: dict[str, list[dict[str, str]]] = {}
for row in source_rows:
    by_url.setdefault(row["url"], []).append(row)
items = list(by_url.items())
if args.limit:
    items = items[: args.limit]


def request(url: str, method: str) -> tuple[int | str, str, str]:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/json,*/*"}
    if method == "GET":
        headers["Range"] = "bytes=0-2047"
    req = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=args.timeout) as response:
            return response.status, response.geturl(), ""
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl(), f"HTTPError: {exc.reason}"
    except Exception as exc:  # network, TLS, timeout, DNS, bot challenge, etc.
        return f"ERROR:{type(exc).__name__}", url, str(exc)


checked_at = datetime.now(timezone.utc).isoformat()
results = []
for url, references in items:
    status, final_url, error = request(url, "HEAD")
    method = "HEAD"
    # Some valid provider sites reject HEAD or automated clients. Try a tiny GET.
    if status in {403, 405, 406, 429, 501} or (isinstance(status, str) and status.startswith("ERROR:")):
        get_status, get_final, get_error = request(url, "GET")
        method = "HEAD+GET"
        if not (isinstance(get_status, str) and get_status.startswith("ERROR:")):
            status, final_url, error = get_status, get_final, get_error
        elif isinstance(status, str) and status.startswith("ERROR:"):
            status, final_url, error = get_status, get_final, get_error
    result = {
        "url": url,
        "http_status": status,
        "final_url": final_url,
        "method": method,
        "checked_at": checked_at,
        "error": error,
        "references": [
            {
                "resource_type": r.get("resource_type", ""),
                "resource_id": r.get("id", ""),
                "resource_name": r.get("name", ""),
                "source_role": r.get("source_role", ""),
                "verification_status": r.get("verification_status", ""),
            }
            for r in references
        ],
    }
    results.append(result)
    print(status, url)
    time.sleep(0.12)

report_path = ROOT / args.report
report_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

try:
    display_path = report_path.relative_to(ROOT)
except ValueError:
    display_path = report_path
print(f"Wrote {display_path} with {len(results)} unique URLs.")
print("HTTP failures, redirects, and bot blocks require manual review; they do not automatically prove that a source is unavailable.")
