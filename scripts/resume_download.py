#!/usr/bin/env python3
"""Sequentially download missing API pages (gentle on Wayback)."""

from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

from build_docs import (
    API_CACHE,
    CAT_HTML,
    UA,
    api_html_to_md,
    build_markdown,
    is_good_cache,
    parse_categories,
)

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "_cache"
DELAY = 1.2


def available_timestamp(name: str) -> str | None:
    url = f"https://archive.org/wayback/available?url=http://wowprogramming.com/docs/api/{name}"
    try:
        proc = subprocess.run(
            ["curl", "-sL", "--max-time", "30", "-A", UA, url],
            capture_output=True,
            check=False,
        )
        data = json.loads(proc.stdout.decode("utf-8", errors="replace") or "{}")
        closest = data.get("archived_snapshots", {}).get("closest")
        if closest and closest.get("available"):
            return closest.get("timestamp")
    except Exception:  # noqa: BLE001
        return None
    return None


def fetch_bytes(url: str) -> bytes | None:
    from build_docs import is_undocumented_page

    proc = subprocess.run(
        ["curl", "-sL", "--max-time", "90", "-A", UA, url],
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0 or not proc.stdout or len(proc.stdout) < 800:
        return None
    body = proc.stdout.decode("utf-8", errors="replace")
    if 'class="api-listing"' in body or is_undocumented_page(body):
        return proc.stdout
    return None


def download_one(name: str) -> str:
    dest = API_CACHE / f"{name}.html"
    if is_good_cache(dest):
        return "cached"

    ts = available_timestamp(name)
    urls = []
    if ts:
        urls.append(f"https://web.archive.org/web/{ts}id_/http://wowprogramming.com/docs/api/{name}")
    urls.extend(
        [
            f"https://web.archive.org/web/2010id_/http://wowprogramming.com/docs/api/{name}",
            f"https://web.archive.org/web/2011id_/http://wowprogramming.com/docs/api/{name}",
            f"https://web.archive.org/web/2009id_/http://wowprogramming.com/docs/api/{name}",
        ]
    )

    for url in urls:
        data = fetch_bytes(url)
        if data:
            dest.write_bytes(data)
            return "ok"
        time.sleep(0.4)

    dest.write_text("<!-- fetch failed: not archived or unreachable -->\n", encoding="utf-8")
    return "fail"


def main() -> None:
    categories = parse_categories(CAT_HTML.read_text(encoding="utf-8", errors="replace"))
    names = sorted({f["name"] for _, _, funcs in categories for f in funcs})
    todo = [n for n in names if not is_good_cache(API_CACHE / f"{n}.html")]
    print(f"Missing: {len(todo)} / {len(names)}", flush=True)

    ok = fail = 0
    for i, name in enumerate(todo, 1):
        status = download_one(name)
        if status == "ok":
            ok += 1
        elif status == "fail":
            fail += 1
        if i % 10 == 0 or i == len(todo):
            print(f"  {i}/{len(todo)} ok={ok} fail={fail} last={name}:{status}", flush=True)
            # periodic rebuild so vault stays useful mid-run
            if i % 50 == 0:
                rebuild(categories, names)
        time.sleep(DELAY)

    rebuild(categories, names)
    print("Done.", flush=True)


def rebuild(categories, names) -> None:
    md_cache: dict[str, str] = {}
    converted = 0
    for name in names:
        path = API_CACHE / f"{name}.html"
        if is_good_cache(path):
            md = api_html_to_md(path.read_text(encoding="utf-8", errors="replace"))
            md_cache[name] = md
            if md:
                converted += 1
        else:
            md_cache[name] = ""
    build_markdown(categories, md_cache)
    print(f"  rebuilt docs ({converted} full pages)", flush=True)


if __name__ == "__main__":
    main()
