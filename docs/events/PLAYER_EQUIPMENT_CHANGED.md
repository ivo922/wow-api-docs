# PLAYER_EQUIPMENT_CHANGED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PLAYER_EQUIPMENT_CHANGED)

---

Fires when the player equips or unequips an item

**Signature:**

```lua
(slot, hasItem)
```

**Arguments:**

- `slot` - The inventory slot affected by the equipment change. (`number`, [inventoryID](../types/inventoryID.md))
- `hasItem` - 1 if the slot contains an item, otherwise `nil`. (`1nil`)
