# CONFIRM_LOOT_ROLL

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_LOOT_ROLL)

---

Fires when the player attempts to roll for a loot item which Binds on Pickup

**Signature:**

```lua
(id, rolltype)
```

**Arguments:**

- `id` - The slot id that you're rolling for (`number`)
- `rolltype` - The numeric representing the type of roll you are doing. Pass: 0, Need: 1, Greed: 2. (`number`)
