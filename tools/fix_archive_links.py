#!/usr/bin/env python3
"""Rewrite wowprogramming Wayback links in docs to local relative paths.

Keeps provenance Source links and targets with no local equivalent (events, etc.).
Run from repo root: python3 tools/fix_archive_links.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = DOCS / "api-index.json"

ARCHIVE_RE = re.compile(
    r"https?://web\.archive\.org/web/\d+/"
    r"(?:https?://)?wowprogramming\.com/docs/([^)\s\"]+)"
)
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://web\.archive\.org[^)]+)\)")
HEADING_RE = re.compile(r"^(#{2,3})\s+(.+?)\s*$")

TYPE_ALIASES = {
    "unitid": "unitID",
    "bindings": "binding",
}

# Scrape typos / renamed targets → local name
API_ALIASES = {
    "CalendarNewGuildAnnoucement": "CalendarNewGuildAnnouncement",
    "AbanonQuest": "AbandonQuest",
    "GetNumLanguages_": "GetNumLanguages",
    "IsActionUsable": "IsUsableAction",
    "GetAuctionItemInvTypes": "GetAuctionInvTypes",
    "GetGVarBool": "GetCVarBool",
    "TurnOrActionStart_": "TurnOrActionStart",
}

WIDGET_PATH_ALIASES = {
    "StatuBar": "StatusBar",
}

WIDGET_AS_TYPE = {"AnimationGroup", "Region", "Animation", "Texture", "Frame"}


def slugify(heading: str) -> str:
    s = heading.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[-\s]+", "-", s).strip("-")
    return s


def load_api_index() -> dict[str, dict]:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    out: dict[str, dict] = {}
    for name, entries in data["by_name"].items():
        out[name] = entries[0]
    return out


def load_types() -> set[str]:
    return {p.stem for p in (DOCS / "types").glob("*.md")}


def load_widgets() -> dict[str, dict]:
    """widget -> methods/handlers maps + has_script_handlers flag."""
    widgets: dict[str, dict] = {}
    for path in (DOCS / "widgets").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        methods: dict[str, str] = {}
        handlers: dict[str, str] = {}
        for line in text.splitlines():
            m = HEADING_RE.match(line)
            if not m:
                continue
            level, heading = m.group(1), m.group(2)
            sl = slugify(heading)
            if level == "###":
                if ":" in heading:
                    _, method = heading.split(":", 1)
                    methods[method.strip().lower()] = sl
                else:
                    handlers[heading.strip().lower()] = sl
        widgets[path.stem] = {
            "methods": methods,
            "handlers": handlers,
            "path": path,
            "has_script_handlers": "## Script Handlers" in text,
        }
    return widgets


def rel_link(from_file: Path, docs_rel: str, anchor: str = "") -> str:
    target = DOCS / docs_rel
    rel = Path(os.path.relpath(target, from_file.parent)).as_posix()
    if anchor:
        return f"{rel}#{anchor}"
    return rel


def resolve(
    docs_path: str,
    from_file: Path,
    api_by_name: dict[str, dict],
    types: set[str],
    widgets: dict[str, dict],
) -> str | None:
    """Return local relative link or None to keep archive URL."""
    path = docs_path.split("?", 1)[0]
    frag = ""
    if "#" in path:
        path, frag = path.split("#", 1)

    # api_types / api_types#unitID / api_types/colorString
    if path == "api_types" or path.startswith("api_types/"):
        name = path.split("/", 1)[1] if path.startswith("api_types/") else frag
        if not name:
            return rel_link(from_file, "API Types.md")
        name = TYPE_ALIASES.get(name, name)
        if name in types:
            return rel_link(from_file, f"types/{name}.md")
        if name in WIDGET_AS_TYPE or name in widgets:
            return rel_link(from_file, f"widgets/{name}.md")
        return None

    # api_categories → home (provenance Source category links skipped by caller)
    if path == "api_categories":
        return rel_link(from_file, "index.md")

    # widgets index / hierarchy
    if path in {"widgets", "widgets_hierarchy"}:
        return rel_link(from_file, "Widgets.md")

    # widget/Type/... (singular scrape typo)
    if path.startswith("widget/"):
        path = "widgets/" + path[len("widget/") :]

    # widgets/Type or widgets/Type/Method
    if path.startswith("widgets/"):
        parts = path[len("widgets/") :].split("/")
        wtype = WIDGET_PATH_ALIASES.get(parts[0], parts[0])
        if wtype not in widgets:
            return None
        if len(parts) == 1:
            return rel_link(from_file, f"widgets/{wtype}.md")
        method = parts[1]
        sl = widgets[wtype]["methods"].get(method.lower())
        if sl:
            return rel_link(from_file, f"widgets/{wtype}.md", sl)
        guess = slugify(f"{wtype}:{method}")
        return rel_link(from_file, f"widgets/{wtype}.md", guess)

    # api/Func or api/Widget/Method (mis-filed widget methods)
    if path.startswith("api/"):
        rest = path[len("api/") :]
        parts = rest.split("/")
        if len(parts) == 2 and parts[0] in widgets:
            wtype, method = parts
            sl = widgets[wtype]["methods"].get(method.lower()) or slugify(
                f"{wtype}:{method}"
            )
            return rel_link(from_file, f"widgets/{wtype}.md", sl)
        func = API_ALIASES.get(parts[0], parts[0])
        entry = api_by_name.get(func)
        if entry:
            return rel_link(from_file, entry["path"], entry["anchor"])
        return None

    # scripts / scripts/OnUpdate — prefer same-page handler when present
    if path == "scripts" or path.startswith("scripts/"):
        handler = path.split("/", 1)[1] if "/" in path else ""
        if from_file.parent.name == "widgets":
            w = widgets.get(from_file.stem)
            if w:
                if handler:
                    sl = w["handlers"].get(handler.lower())
                    if sl:
                        return f"#{sl}"
                elif w.get("has_script_handlers"):
                    return "#script-handlers"
        if not handler:
            # no standalone scripts index; Frame hosts the common handler list
            return rel_link(from_file, "widgets/Frame.md", "script-handlers")
        sl = widgets.get("Frame", {}).get("handlers", {}).get(handler.lower())
        if sl:
            return rel_link(from_file, "widgets/Frame.md", sl)
        return None

    # secure_template → closest local category
    if path == "secure_template":
        return rel_link(from_file, "categories/Secure execution utility.md")

    # events / events/UNIT_HEALTH / event/TRADE_SHOW (singular scrape typo)
    if path in {"events", "event"}:
        return rel_link(from_file, "Events.md")
    if path.startswith("events/") or path.startswith("event/"):
        name = path.split("/", 1)[1]
        if (DOCS / "events" / f"{name}.md").exists():
            return rel_link(from_file, f"events/{name}.md")
        return None

    return None


def is_provenance(link_text: str) -> bool:
    t = link_text.strip().lower()
    return t in {"source", "source category"} or t.startswith("wowprogramming.com")


def process_file(
    path: Path,
    api_by_name: dict[str, dict],
    types: set[str],
    widgets: dict[str, dict],
) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    replaced = 0
    kept = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal replaced, kept
        label, url = m.group(1), m.group(2)
        if is_provenance(label):
            kept += 1
            return m.group(0)
        am = ARCHIVE_RE.fullmatch(url)
        if not am:
            kept += 1
            return m.group(0)
        local = resolve(am.group(1), path, api_by_name, types, widgets)
        if local is None:
            kept += 1
            return m.group(0)
        replaced += 1
        return f"[{label}]({local})"

    new_text = MD_LINK_RE.sub(repl, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return replaced, kept


def main() -> int:
    api_by_name = load_api_index()
    types = load_types()
    widgets = load_widgets()

    total_r = total_k = 0
    files = 0
    for path in sorted(DOCS.rglob("*.md")):
        r, k = process_file(path, api_by_name, types, widgets)
        if r or k:
            files += 1
        total_r += r
        total_k += k

    # README at repo root may also have archive refs (leave provenance)
    readme = ROOT / "README.md"
    if readme.exists():
        r, k = process_file(readme, api_by_name, types, widgets)
        total_r += r
        total_k += k

    print(f"files touched scan: {files}")
    print(f"rewrote: {total_r}")
    print(f"kept archive: {total_k}")

    # ponytail: fail if common localizable type links still point at Wayback
    leftover_unit = [
        p
        for p in DOCS.rglob("*.md")
        if "wowprogramming.com/docs/api_types#unitID" in p.read_text(encoding="utf-8")
    ]
    assert not leftover_unit, leftover_unit
    return 0


if __name__ == "__main__":
    sys.exit(main())
