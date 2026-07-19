# WEAR_EQUIPMENT_SET

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/WEAR_EQUIPMENT_SET)

---

Fires when the player's current equipment set changes. The firing of this event indicates the moment when the player's "current equipment set" state (as returned by [`GetEquipmentSetInfo()`](../categories/Equipment Manager.md#getequipmentsetinfo)) changes -- at that time, the process of equipping/unequipping the set's items may not yet be complete.

See [`EQUIPMENT_SWAP_PENDING`](EQUIPMENT_SWAP_PENDING.md) and [`EQUIPMENT_SWAP_FINISHED`](EQUIPMENT_SWAP_FINISHED.md) for monitoring the beginning and end of the equipment swap process.

**Signature:**

```lua
()
```
