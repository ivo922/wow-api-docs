# ITEM_LOCK_CHANGED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ITEM_LOCK_CHANGED)

---

Fires when an item in the player's bags or equipped inventory is locked for moving or unlocked afterward

**Signature:**

```lua
(bagID, slotID)
```

**Arguments:**

- `bagID` - The bag id that the slot is in. (`number`)
- `slotID` - The slot id that's lock is changing. (`number`)
