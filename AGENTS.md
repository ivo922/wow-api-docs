# Agent guide — WoW API Docs

Late WotLK (≈3.3.5 / July 2010) World of Warcraft Lua API reference, archived from wowprogramming.com. **Not** the Cataclysm launch client and **not** modern/retail WoW.

## Lookup recipe

1. Open [`docs/api-index.json`](docs/api-index.json).
2. Read `by_name["ExactFunctionName"]` (array; usually one entry).
3. Open `docs/<path>` and jump to heading anchor `anchor` (MkDocs slug of the `##` heading).
4. For argument types, use `types["spellID"].path` → `docs/types/spellID.md` (prefer local files over Wayback links in the prose).

## Orientation

| File | Use |
|---|---|
| [`docs/api-index.json`](docs/api-index.json) | Function/type catalog (start here) |
| [`docs/index.md`](docs/index.md) | Human category index |
| [`docs/API Types.md`](docs/API%20Types.md) | Type list |
| [`docs/Widgets.md`](docs/Widgets.md) | Widget type index |
| [`docs/widgets/*.md`](docs/widgets/) | Widget methods / script handlers |
| [`docs/categories/*.md`](docs/categories/) | Full function docs (many APIs per file) |
| [`llms.txt`](llms.txt) | Short machine-oriented site map |

## Page shape

Each function is an `## Name` section (optional badges like `` `protected` ``), then description, **Signature** (lua fence), **Arguments** / **Returns**.

## Regenerate catalog

```bash
python3 tools/gen_api_index.py
```
