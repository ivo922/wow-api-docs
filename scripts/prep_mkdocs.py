#!/usr/bin/env python3
"""Convert Obsidian wikilinks to relative Markdown and write mkdocs.yml nav.

Idempotent. Run from repo root: python3 scripts/prep_mkdocs.py
"""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
WIKI_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
HOME_STEM = "WoW API Docs"


def build_catalog() -> dict[str, Path]:
    catalog: dict[str, Path] = {}
    for p in (DOCS / "categories").glob("*.md"):
        catalog[p.stem] = p
    for p in (DOCS / "types").glob("*.md"):
        catalog[p.stem] = p
    for p in DOCS.glob("*.md"):
        if p.name == "index.md":
            continue
        catalog[p.stem] = p
    catalog[HOME_STEM] = DOCS / "index.md"
    return catalog


def rel_link(from_file: Path, target: Path) -> str:
    return Path(os.path.relpath(target, start=from_file.parent)).as_posix()


def convert_text(text: str, from_file: Path, catalog: dict[str, Path]) -> str:
    def repl(m: re.Match[str]) -> str:
        stem = m.group(1).strip()
        label = (m.group(2) or stem).strip()
        # Scraped archive stubs like docs/api_types#foo — not vault pages
        if "/" in stem or stem.startswith("wowhead:"):
            return label if label.startswith("`") else f"`{label}`"
        target = catalog.get(stem)
        if target is None:
            return m.group(0)
        return f"[{label}]({rel_link(from_file, target)})"

    return WIKI_RE.sub(repl, text)


def iter_doc_files() -> list[Path]:
    files = sorted((DOCS / "categories").glob("*.md"))
    files += sorted((DOCS / "types").glob("*.md"))
    files += sorted(p for p in DOCS.glob("*.md"))
    return files


def write_index_from_home(catalog: dict[str, Path]) -> None:
    home = DOCS / f"{HOME_STEM}.md"
    index = DOCS / "index.md"
    if not home.exists():
        return
    text = convert_text(home.read_text(encoding="utf-8"), index, catalog)
    text = text.replace(
        "- Open this vault in Obsidian; start from this note and follow `[[wikilinks]]` into each category.\n",
        "- Browse categories in the left nav, or use search.\n",
    )
    index.write_text(text, encoding="utf-8")


def convert_all(catalog: dict[str, Path]) -> int:
    changed = 0
    for path in iter_doc_files():
        if path.name == "index.md":
            continue
        original = path.read_text(encoding="utf-8")
        updated = convert_text(original, path, catalog)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def yaml_quote(s: str) -> str:
    if re.search(r'[:#{}[\],&*?|>!%@`]', s) or s.startswith(("-", "?", "'", '"')):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def write_mkdocs_yml(catalog: dict[str, Path]) -> None:
    cats = sorted(
        (stem, path)
        for stem, path in catalog.items()
        if path.parent.name == "categories"
    )
    types = sorted(
        (stem, path)
        for stem, path in catalog.items()
        if path.parent.name == "types"
    )

    lines = [
        "site_name: WoW API Docs",
        'site_description: "Cataclysm-era World of Warcraft API reference (wowprogramming.com archive)"',
        "site_url: !ENV [MKDOCS_SITE_URL, \"http://127.0.0.1:8000/\"]",
        "",
        "docs_dir: docs",
        "site_dir: site",
        "",
        "exclude_docs: |",
        "  WoW API Docs.md",
        "",
        "theme:",
        "  name: material",
        "  palette:",
        "    - scheme: default",
        "      primary: indigo",
        "      toggle:",
        "        icon: material/brightness-7",
        "        name: Dark mode",
        "    - scheme: slate",
        "      primary: indigo",
        "      toggle:",
        "        icon: material/brightness-4",
        "        name: Light mode",
        "  features:",
        "    - navigation.instant",
        "    - navigation.tracking",
        "    - navigation.expand",
        "    - navigation.sections",
        "    - navigation.top",
        "    - search.suggest",
        "    - search.highlight",
        "    - content.code.copy",
        "    - toc.follow",
        "",
        "plugins:",
        "  - search",
        "",
        "markdown_extensions:",
        "  - tables",
        "  - toc:",
        "      permalink: true",
        "  - pymdownx.highlight:",
        "      anchor_linenums: true",
        "  - pymdownx.superfences",
        "  - pymdownx.inlinehilite",
        "",
        "nav:",
        "  - Home: index.md",
        "  - API Types: API Types.md",
        "  - Failed Scrapes: Failed Scrapes.md",
        "  - Categories:",
    ]
    for stem, path in cats:
        lines.append(
            f"      - {yaml_quote(stem)}: {path.relative_to(DOCS).as_posix()}"
        )
    lines.append("  - Types:")
    for stem, path in types:
        lines.append(
            f"      - {yaml_quote(stem)}: {path.relative_to(DOCS).as_posix()}"
        )
    lines.append("")

    (ROOT / "mkdocs.yml").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    catalog = build_catalog()
    write_index_from_home(catalog)
    catalog[HOME_STEM] = DOCS / "index.md"
    n = convert_all(catalog)
    write_index_from_home(catalog)
    write_mkdocs_yml(catalog)
    left = 0
    for p in iter_doc_files():
        left += len(WIKI_RE.findall(p.read_text(encoding="utf-8")))
    print(f"converted files: {n}")
    print(f"wikilinks remaining: {left}")
    print("wrote mkdocs.yml + docs/index.md")


if __name__ == "__main__":
    main()
