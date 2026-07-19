# WoW API Docs

Late Wrath of the Lich King (≈3.3.5) World of Warcraft API reference, scraped from the [wowprogramming.com archive](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories) (July 2010 — still WotLK live; Cataclysm launched Dec 2010).

## Browse locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Open http://127.0.0.1:8000/

## Publish (GitHub Pages)

Push to `main`. The [Deploy docs](.github/workflows/docs.yml) workflow builds with MkDocs Material and deploys to GitHub Pages.

After the first push: **Settings → Pages → Source: GitHub Actions**

Site URL: `https://<user>.github.io/<repo>/`

## For AI agents

- [`AGENTS.md`](AGENTS.md) — lookup recipe
- [`docs/api-index.json`](docs/api-index.json) — function/type catalog
- [`llms.txt`](llms.txt) — short machine map (also served at `/llms.txt` on Pages)

Regenerate the catalog after editing API pages:

```bash
python3 tools/gen_api_index.py
```

## Sources

- [API categories](docs/index.md) (2010-07-26)
- [API types](docs/API Types.md) (2010-03-24)
- [Events](docs/Events.md) (2010-07-26)
- [Widgets](docs/Widgets.md) (2010-07-26)
