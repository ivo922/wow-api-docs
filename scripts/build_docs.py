#!/usr/bin/env python3
"""Scrape wowprogramming.com API pages and rebuild Obsidian category docs."""

from __future__ import annotations

import html
import json
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "_cache"
API_CACHE = CACHE / "api"
CAT_HTML = CACHE / "api_categories.html"
OUT_DIR = ROOT / "docs" / "categories"
INDEX = ROOT / "docs" / "WoW API Docs.md"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
WORKERS = 4
RETRIES = 2
UNDOC_RE = re.compile(
    r"not yet documented|has not been documented|could document this function",
    re.I,
)


def is_undocumented_page(text: str) -> bool:
    return bool(UNDOC_RE.search(text))


def curl_fetch(url: str) -> bytes:
    """Fetch URL with curl (-L follows Wayback redirects)."""
    last_err = ""
    for attempt in range(RETRIES):
        try:
            proc = subprocess.run(
                [
                    "curl",
                    "-sL",
                    "--max-time",
                    "90",
                    "-A",
                    UA,
                    "-H",
                    "Accept: text/html,application/xhtml+xml",
                    url,
                ],
                capture_output=True,
                check=False,
            )
            data = proc.stdout or b""
            if proc.returncode != 0 or len(data) < 800:
                last_err = f"curl rc={proc.returncode} len={len(data)}"
                time.sleep(1.5 * (attempt + 1))
                continue
            body = data.decode("utf-8", errors="replace")
            if 'class="api-listing"' in body or is_undocumented_page(body):
                return data
            # Wayback soft-404 calendar pages are large HTML without api-listing
            if "Wayback Machine" in body[:2000] and 'class="api-listing"' not in body:
                last_err = "wayback soft-404"
                time.sleep(1.0)
                continue
            # Some pages may still be valid with different markup
            if "<div id='content'>" in body or '<div id="content">' in body:
                return data
            last_err = "unexpected body"
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(last_err)


def is_good_cache(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 800:
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("<!-- fetch failed"):
        return False
    if 'class="api-listing"' in text:
        return True
    if is_undocumented_page(text):
        return True
    return False


def strip_tags(s: str) -> str:
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def inline_md(fragment: str) -> str:
    def code_repl(m: re.Match[str]) -> str:
        inner = strip_tags(m.group(1)).replace("`", "\\`")
        return f"`{inner}`"

    def link_repl(m: re.Match[str]) -> str:
        href = m.group(1)
        text = inline_md(m.group(2))
        if href.startswith("/docs/") or href.startswith("http://wowprogramming.com"):
            path = href.replace("http://wowprogramming.com", "")
            href = f"https://web.archive.org/web/20100726112636/http://wowprogramming.com{path}"
        elif href.startswith("/web/"):
            href = "https://web.archive.org" + href
        return f"[{text}]({href})"

    out = fragment
    out = re.sub(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', link_repl, out, flags=re.S | re.I)
    out = re.sub(r"<code>(.*?)</code>", code_repl, out, flags=re.S | re.I)
    out = re.sub(r"<em>(.*?)</em>", r"*\1*", out, flags=re.S | re.I)
    out = re.sub(r"<strong>(.*?)</strong>", r"**\1**", out, flags=re.S | re.I)
    out = strip_tags(out)
    out = re.sub(r"[ \t]+", " ", out)
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out.strip()


def first_ul(section: str) -> str | None:
    m = re.search(r"<ul\b", section, re.I)
    if not m:
        return None
    i = m.start()
    depth = 0
    pos = i
    while True:
        nxt = re.search(r"</?ul\b[^>]*>", section[pos:], re.I)
        if not nxt:
            return section[i:]
        tag = nxt.group(0)
        if tag.lower().startswith("</"):
            depth -= 1
            pos += nxt.end()
            if depth == 0:
                return section[i:pos]
        else:
            depth += 1
            pos += nxt.end()


def list_items_to_md(ul_html: str, indent: int = 0) -> list[str]:
    lines: list[str] = []
    um = re.match(r"<ul\b[^>]*>(.*)</ul>\s*$", ul_html.strip(), re.S | re.I)
    content = um.group(1) if um else ul_html

    items: list[str] = []
    i = 0
    while True:
        start = re.search(r"<li\b[^>]*>", content[i:], re.I)
        if not start:
            break
        open_end = i + start.end()
        pos = open_end
        depth = 1
        end = None
        while pos < len(content):
            nxt = re.search(r"<li\b[^>]*>|</li>", content[pos:], re.I)
            if not nxt:
                break
            tag = nxt.group(0)
            if tag.lower().startswith("</"):
                depth -= 1
                pos += nxt.end()
                if depth == 0:
                    end = pos
                    break
            else:
                depth += 1
                pos += nxt.end()
        if end is None:
            break
        items.append(content[open_end : end - len("</li>")])
        i = end

    pad = "  " * indent
    for inner in items:
        nested = None
        nm = re.search(r"<ul\b", inner, re.I)
        if nm:
            nested = first_ul(inner[nm.start() :])
            if nested:
                inner = inner[: nm.start()] + inner[nm.start() + len(nested) :]
        inner = re.sub(r"^<p>(.*)</p>\s*$", r"\1", inner.strip(), flags=re.S | re.I)
        text = inline_md(inner)
        if text:
            lines.append(f"{pad}- {text}")
        if nested:
            lines.extend(list_items_to_md(nested, indent + 1))
    return lines


def signature_to_code(sig_html: str) -> str:
    text = strip_tags(sig_html)
    return re.sub(r"\s+", " ", text).strip()


def extract_api_block(page_html: str) -> str | None:
    start = page_html.find('<div class="api-listing">')
    if start < 0:
        return None
    footer = re.search(r"<div\s+id=['\"]footer", page_html[start:], re.I)
    end = start + footer.start() if footer else len(page_html)
    return page_html[start:end]


def api_html_to_md(page_html: str) -> str:
    block = extract_api_block(page_html)
    if not block:
        # Leave empty so category short descriptions are used in the note.
        if is_undocumented_page(page_html):
            return ""
        return ""

    parts: list[str] = []

    desc_m = re.search(r'<div class="api-desc">(.*?)</div>', block, re.S | re.I)
    if desc_m:
        desc = desc_m.group(1)
        for chunk in re.split(r"(?=<p\b|<ul\b)", desc):
            chunk = chunk.strip()
            if not chunk:
                continue
            if re.match(r"<ul\b", chunk, re.I):
                ul = first_ul(chunk)
                if ul:
                    parts.extend(list_items_to_md(ul))
                    parts.append("")
            elif re.match(r"<p\b", chunk, re.I):
                text = inline_md(chunk)
                if text:
                    parts.append(text)
                    parts.append("")

    sig_m = re.search(
        r'<p class="label">Signature:</p>\s*<div class="signature">(.*?)</div>',
        block,
        re.S | re.I,
    )
    if not sig_m:
        sig_m = re.search(
            r'<p class="label">Signature:</p>\s*(.*?)(?=<p class="label">|<div class="examples"|$)',
            block,
            re.S | re.I,
        )
    if sig_m:
        sig = signature_to_code(sig_m.group(1))
        if sig:
            parts.append("**Signature:**")
            parts.append("")
            parts.append("```lua")
            parts.append(sig)
            parts.append("```")
            parts.append("")

    for label in ("Arguments", "Returns"):
        lm = re.search(
            rf'<p class="label">{label}:</p>\s*(.*?)(?=<p class="label">|<div class="examples"|<div class="flags"|$)',
            block,
            re.S | re.I,
        )
        if not lm:
            continue
        ul = first_ul(lm.group(1))
        if not ul:
            continue
        items = list_items_to_md(ul)
        if items:
            parts.append(f"**{label}:**")
            parts.append("")
            parts.extend(items)
            parts.append("")

    ex_m = re.search(r'<div class="examples">(.*?)</div>', block, re.S | re.I)
    if ex_m:
        codes = list(re.finditer(r"<pre>\s*<code>(.*?)</code>\s*</pre>", ex_m.group(1), re.S | re.I))
        if codes:
            parts.append("**Examples:**")
            parts.append("")
            for pre in codes:
                code = html.unescape(pre.group(1)).rstrip() + "\n"
                # strip trailing blank indentation only
                code = code.rstrip("\n")
                parts.append("```lua")
                parts.append(code)
                parts.append("```")
                parts.append("")

    flags_m = re.search(r'<div class="flags">(.*?)</div>', block, re.S | re.I)
    if flags_m:
        flag_links = re.findall(r"api_flags#([a-z0-9_-]+)", flags_m.group(1), re.I)
        if flag_links:
            parts.append("**Flags:** " + ", ".join(f"`{f}`" for f in flag_links))
            parts.append("")

    md = "\n".join(parts).strip()
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md + ("\n" if md else "")


def parse_categories(html_text: str) -> list[tuple[str, str, list[dict]]]:
    body = html_text
    start = body.find('<div class="category-listing">')
    if start < 0:
        start = body.find('<a name="achievement"')
    end = body.find("<div id='footer'", start)
    if end < 0:
        end = body.find('<div id="footer"', start)
    body = body[start:end if end > 0 else None]

    body = re.sub(
        r'<ul\s+class="api_badge">.*?</ul>',
        lambda m: " " + " ".join(f"⟦{b}⟧" for b in re.findall(r"api_flags#([a-z0-9_-]+)", m.group(0), re.I)),
        body,
        flags=re.S | re.I,
    )

    parts = re.split(r'<a\s+name="([^"]+)"\s*></a>\s*<h3>(.*?)</h3>', body, flags=re.S | re.I)
    categories: list[tuple[str, str, list[dict]]] = []
    i = 1
    while i + 2 < len(parts):
        slug = parts[i].strip()
        title = html.unescape(re.sub(r"<[^>]+>", "", parts[i + 1])).strip()
        content = parts[i + 2]
        funcs: list[dict] = []
        for lim in re.finditer(
            r'<li>\s*<a\s+href="[^"]*?docs/api/([^"#]+)"[^>]*>(.*?)</a>(.*?)</li>',
            content,
            re.S | re.I,
        ):
            name = html.unescape(re.sub(r"<[^>]+>", "", lim.group(2))).strip()
            rest = lim.group(3)
            badges = re.findall(r"⟦([a-z0-9_-]+)⟧", rest, re.I)
            rest = re.sub(r"⟦([a-z0-9_-]+)⟧", "", rest)
            desc = html.unescape(re.sub(r"<[^>]+>", "", rest))
            desc = re.sub(r"\s+", " ", desc).strip().lstrip("-–— ").strip()
            funcs.append({"name": name, "desc": desc, "badges": badges})
        categories.append((slug, title, funcs))
        i += 3
    return categories


def filename_for(title: str, slug: str) -> str:
    base = re.sub(r"\s+functions$", "", title, flags=re.I)
    base = re.sub(r'[\\/:*?"<>|]', "", base).strip()
    return base or slug


def download_one(name: str) -> tuple[str, str]:
    dest = API_CACHE / f"{name}.html"
    if is_good_cache(dest):
        return name, "cached"

    urls = [
        f"https://web.archive.org/web/20100105222815id_/http://wowprogramming.com/docs/api/{name}",
        f"https://web.archive.org/web/20100726112636id_/http://wowprogramming.com/docs/api/{name}",
        f"https://web.archive.org/web/201005id_/http://wowprogramming.com/docs/api/{name}",
        f"https://web.archive.org/web/200912id_/http://wowprogramming.com/docs/api/{name}",
    ]
    errors: list[str] = []
    for url in urls:
        try:
            data = curl_fetch(url)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            if is_good_cache(dest):
                return name, "ok"
            errors.append(f"{url}: bad body")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{url}: {e}")
            time.sleep(0.5)
    dest.write_text(
        f"<!-- fetch failed: {errors[-1] if errors else 'unknown'} -->\n",
        encoding="utf-8",
    )
    return name, "fail"


def build_markdown(categories: list[tuple[str, str, list[dict]]], md_cache: dict[str, str]) -> tuple[int, int]:
    for p in OUT_DIR.glob("*.md"):
        p.unlink()
    OUT_DIR.mkdir(exist_ok=True)

    file_map: list[tuple[str, str, int, str]] = []
    used: set[str] = set()
    total_entries = 0
    names = {f["name"] for _, _, funcs in categories for f in funcs}

    for slug, title, funcs in categories:
        fname = filename_for(title, slug)
        if fname in used:
            fname = f"{fname} ({slug})"
        used.add(fname)
        file_map.append((title, fname, len(funcs), slug))
        total_entries += len(funcs)

        lines: list[str] = [
            f"# {title}",
            "",
            "← [WoW API Docs](../index.md)",
            "",
            f"**{len(funcs)}** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#{slug})",
            "",
        ]

        for fn in funcs:
            lines.append("---")
            lines.append("")
            badge_str = (" " + " ".join(f"`{b}`" for b in fn["badges"])) if fn["badges"] else ""
            lines.append(f"## {fn['name']}{badge_str}")
            lines.append("")
            body = (md_cache.get(fn["name"]) or "").rstrip()
            if body:
                lines.append(body)
                lines.append("")
            elif fn["desc"]:
                lines.append(fn["desc"])
                lines.append("")
            else:
                lines.append("*No documentation available.*")
                lines.append("")

        lines.append("---")
        lines.append("")
        lines.append("← [WoW API Docs](../index.md)")
        lines.append("")
        (OUT_DIR / f"{fname}.md").write_text("\n".join(lines), encoding="utf-8")

    index_lines = [
        "# WoW API Docs",
        "",
        "Obsidian-style reference of World of Warcraft API functions, scraped from the [wowprogramming.com API Category Listing](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories) (archived July 26, 2010 — Cataclysm-era docs).",
        "",
        f"**{total_entries}** function entries ({len(names)} unique) across **{len(categories)}** categories.",
        "",
        "Also see [API Types](API Types.md) and [Failed Scrapes](Failed Scrapes.md).",
        "",
        "## Categories",
        "",
    ]
    for title, fname, count, _slug in file_map:
        index_lines.append(f"- [{title}](categories/{fname}.md) ({count})")
    index_lines += [
        "",
        "---",
        "",
        "## Notes",
        "",
        "- Browse categories in the left nav, or use search.",
        "- Each category note embeds the archived reference (signature, arguments, returns, examples).",
        "- Signatures and examples use Lua code blocks; identifiers use inline `code`.",
        "- Functions are separated by horizontal rules (`---`).",
        "",
    ]
    text = "\n".join(index_lines)
    INDEX.write_text(text, encoding="utf-8")
    (INDEX.parent / "index.md").write_text(text, encoding="utf-8")
    return total_entries, len(file_map)


def main() -> None:
    API_CACHE.mkdir(parents=True, exist_ok=True)
    if not CAT_HTML.exists() or CAT_HTML.stat().st_size < 1000:
        data = curl_fetch(
            "https://web.archive.org/web/20100726112636id_/http://wowprogramming.com/docs/api_categories"
        )
        CAT_HTML.write_bytes(data)

    categories = parse_categories(CAT_HTML.read_text(encoding="utf-8", errors="replace"))
    names = sorted({f["name"] for _, _, funcs in categories for f in funcs})
    print(f"Categories: {len(categories)}; unique functions: {len(names)}", flush=True)

    # Only download missing / bad cache entries
    todo = [n for n in names if not is_good_cache(API_CACHE / f"{n}.html")]
    print(f"Need to download: {len(todo)} (already cached: {len(names) - len(todo)})", flush=True)

    done = 0
    fails = 0
    oks = 0
    if todo:
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = {pool.submit(download_one, n): n for n in todo}
            for fut in as_completed(futures):
                _name, status = fut.result()
                done += 1
                if status == "fail":
                    fails += 1
                elif status == "ok":
                    oks += 1
                if done % 25 == 0 or done == len(todo):
                    print(
                        f"  progress {done}/{len(todo)} ok={oks} fail={fails}",
                        flush=True,
                    )

    # Convert cache → markdown snippets
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

    print(f"Converted {converted}/{len(names)} pages to markdown", flush=True)
    total_entries, nfiles = build_markdown(categories, md_cache)
    print(f"Wrote {nfiles} category files ({total_entries} entries)", flush=True)

    sample = md_cache.get("SendAddonMessage", "")
    print("--- SendAddonMessage preview ---", flush=True)
    print(sample[:600], flush=True)

    (CACHE / "build_stats.json").write_text(
        json.dumps(
            {
                "unique": len(names),
                "entries": total_entries,
                "converted": converted,
                "download_fails": fails,
            },
            indent=2,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
