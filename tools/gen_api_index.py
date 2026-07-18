#!/usr/bin/env python3
"""Generate docs/api-index.json from category/type markdown headings.

Run from repo root: python3 tools/gen_api_index.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUT = DOCS / "api-index.json"

HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")
BADGE_RE = re.compile(r"`([^`]+)`")
SIG_RE = re.compile(
    r"\*\*Signature:\*\*\s*\n+```(?:lua)?\n(.*?)```",
    re.DOTALL | re.IGNORECASE,
)


def slugify(heading: str) -> str:
    """Approximate Python-Markdown / MkDocs toc slug."""
    s = heading.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s


def parse_heading(raw: str) -> tuple[str, list[str]]:
    badges = BADGE_RE.findall(raw)
    name = BADGE_RE.sub("", raw).strip()
    return name, badges


def extract_signature(block: str) -> str | None:
    m = SIG_RE.search(block)
    if not m:
        return None
    return " ".join(m.group(1).strip().split())


def split_sections(text: str) -> list[tuple[str, str]]:
    """Return (heading_text, body) for each ## section."""
    lines = text.splitlines()
    sections: list[tuple[str, str]] = []
    i = 0
    while i < len(lines):
        m = HEADING_RE.match(lines[i])
        if not m:
            i += 1
            continue
        heading = m.group(1)
        i += 1
        body_lines: list[str] = []
        while i < len(lines) and not HEADING_RE.match(lines[i]):
            body_lines.append(lines[i])
            i += 1
        sections.append((heading, "\n".join(body_lines)))
    return sections


def load_functions() -> dict[str, list[dict]]:
    by_name: dict[str, list[dict]] = {}
    for path in sorted((DOCS / "categories").glob("*.md")):
        category = path.stem
        rel = path.relative_to(DOCS).as_posix()
        text = path.read_text(encoding="utf-8")
        for heading, body in split_sections(text):
            name, badges = parse_heading(heading)
            if not name or name.lower() in {"notes", "see also"}:
                continue
            entry = {
                "name": name,
                "category": category,
                "path": rel,
                "heading": heading,
                "anchor": slugify(heading),
                "badges": badges,
                "signature": extract_signature(body),
            }
            by_name.setdefault(name, []).append(entry)
    return by_name


def load_types() -> dict[str, dict]:
    types: dict[str, dict] = {}
    for path in sorted((DOCS / "types").glob("*.md")):
        rel = path.relative_to(DOCS).as_posix()
        types[path.stem] = {
            "name": path.stem,
            "path": rel,
            "anchor": "",
        }
    return types


def main() -> None:
    by_name = load_functions()
    types = load_types()
    total = sum(len(v) for v in by_name.values())
    payload = {
        "meta": {
            "description": (
                "Cataclysm-era World of Warcraft API reference "
                "(wowprogramming.com archive, ~2010). Not retail/modern WoW."
            ),
            "unique_functions": len(by_name),
            "function_entries": total,
            "types": len(types),
            "lookup": (
                "Use by_name[<FunctionName>][0].path and .anchor to open the "
                "markdown file and jump to the ## heading."
            ),
        },
        "by_name": by_name,
        "types": types,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ponytail: fail if catalog is empty or CastSpell missing
    assert total > 2000, total
    assert "CastSpell" in by_name, "CastSpell missing"
    assert by_name["CastSpell"][0]["signature"], "CastSpell signature missing"

    print(f"wrote {OUT.relative_to(ROOT)} ({len(by_name)} unique, {total} entries)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"gen_api_index self-check failed: {e}", file=sys.stderr)
        sys.exit(1)
