# Duel functions

← [WoW API Docs](../index.md)

**3** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#duel)

---

## AcceptDuel

Accepts a proposed duel

**Signature:**

```lua
AcceptDuel()
```

---

## CancelDuel

Cancels an ongoing duel, or declines an offered duel

**Signature:**

```lua
CancelDuel()
```

---

## StartDuel

Challenges another player to a duel

**Signature:**

```lua
StartDuel("unit") or StartDuel("name" [, exactMatch])
```

**Arguments:**

- `unit` - A unit to target (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit to target (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

← [WoW API Docs](../index.md)
