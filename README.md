# WoW API Docs

Cataclysm-era World of Warcraft API reference, scraped from the [wowprogramming.com archive](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories).

## Browse locally

**MkDocs (recommended for reading):**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Then open http://127.0.0.1:8000/

**Obsidian:** open the `docs/` folder as the vault. Start from `docs/index.md` (or `docs/WoW API Docs.md`).

## Publish (GitHub Pages)

Push to `main`. The [Deploy docs](.github/workflows/docs.yml) workflow builds with MkDocs Material and deploys to GitHub Pages.

After the first push, enable Pages in the repo settings:

**Settings → Pages → Build and deployment → Source: GitHub Actions**

Site URL will be `https://<user>.github.io/<repo>/`.

## Regenerating nav / links

If you add pages or restore Obsidian `[[wikilinks]]`:

```bash
python3 scripts/prep_mkdocs.py
```

## Sources

- [API categories](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories) (2010-07-26)
- [API types](https://web.archive.org/web/20100324131056/http://wowprogramming.com/docs/api_types) (2010-03-24)
