# Type: itemLocation

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

A [`bitfield`](bitfield.md) describing the location of an item owned by the player. The bitfield can be decoded using the [EquipmentManager_UnpackLocation](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/EquipmentManager_UnpackLocation) function, provided by the equipment manager system:

```lua
 local player, bank, bags, slot, bag = EquipmentManager_UnpackLocation(mask)
```

---

← [API Types](../API Types.md)
