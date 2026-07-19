# CHARACTER_POINTS_CHANGED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHARACTER_POINTS_CHANGED)

---

Fires when the player's amount of available talent points changes. Note that since the introduction of Death Knights, who gain 46 of their talent points through questing, this event can fire without the player gaining a character level.

**Signature:**

```lua
(count, levels)
```

**Arguments:**

- `count` - The number of talent points gained or lost. Positive numbers are gains negative numbers are expenditures. (`number`)
- `levels` - The number of levels gained in association to this change. Is 0 if there is no level change. (`number`)
