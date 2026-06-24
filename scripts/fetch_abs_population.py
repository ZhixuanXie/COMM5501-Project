"""Locate and download the ABS Regional Population 'by LGA' data cube.

The raw .xlsx is saved unmodified into data/ for traceability (Deliverable 2
requires reputable, citable sources). Run with the project as the working dir.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import requests

RELEASE_URL = (
    "https://www.abs.gov.au/statistics/people/population/"
    "regional-population/latest-release"
)
HEADERS = {"User-Agent": "Mozilla/5.0 (COMM5501 student project; data download)"}
OUT_DIR = Path("data")
OUT_NAME = "abs_regional_population_lga_2024_25.xlsx"


def find_lga_cube_url(html: str) -> str | None:
    """Return the download URL for the 'by LGA' population data cube."""
    candidates = re.findall(r'href="([^"]+\.xlsx)"', html, flags=re.IGNORECASE)
    candidates = [c for c in candidates if c.lower().endswith(".xlsx")]
    # Prefer the file whose surrounding text mentions LGA estimates/components.
    lga = [c for c in candidates if "lga" in c.lower()]
    pool = lga or candidates
    for c in pool:
        print("  candidate:", c)
    if not pool:
        return None
    url = pool[0]
    if url.startswith("/"):
        url = "https://www.abs.gov.au" + url
    return url


def main() -> int:
    OUT_DIR.mkdir(exist_ok=True)
    print("Fetching release page ...")
    html = requests.get(RELEASE_URL, headers=HEADERS, timeout=90).text
    url = find_lga_cube_url(html)
    if not url:
        print("ERROR: no .xlsx links found on release page.", file=sys.stderr)
        return 1
    print("Downloading:", url)
    resp = requests.get(url, headers=HEADERS, timeout=180)
    resp.raise_for_status()
    out = OUT_DIR / OUT_NAME
    out.write_bytes(resp.content)
    print(f"Saved {len(resp.content):,} bytes -> {out}")
    print("SOURCE_URL=" + url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
