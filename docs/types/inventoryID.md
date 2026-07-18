# Type: inventoryID

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

This is a numeric identifier that is used by the the inventory system to identify a slot in the player's inventory. In World of Warcraft all items that the player 'owns' are part of the player's inventory, including the items they have equipped, the items in the player's bank, the bags that the player has equipped and equipped in the bank, and the keys stored in the player's key ring.

There is a system of API functions that allow you to map from one of these types of locations into an 'inventorySlot' which uniquely identifies that location. For example:

```lua
 GetInventorySlotInfo("MainHand")   -- The player's mainhand weapon
 BankButtonIDToInvSlotID(3, 1)      -- The third bag in the player's bank
 BankButtonIDToInvSlotID(5, nil)    -- The fifth slot in the player's bank (not bags)
 ContainerIDToInventoryID(1)        -- The player's first bag slot
 KeyRingButtonIDToInvSlotId(4)      -- The fourth slot in the player's key-ring
```

In addition and for convenience there are a set of constants defined by the user interface that can be used for the items in the player's 'paper doll' frame. These are defined in FrameXML/Constants.lua and are currently as follows:

```lua
 -- Inventory slots
 INVSLOT_AMMO       = 0;
 INVSLOT_HEAD       = 1; INVSLOT_FIRST_EQUIPPED = INVSLOT_HEAD;
 INVSLOT_NECK       = 2;
 INVSLOT_SHOULDER   = 3;
 INVSLOT_BODY       = 4;
 INVSLOT_CHEST      = 5;
 INVSLOT_WAIST      = 6;
 INVSLOT_LEGS       = 7;
 INVSLOT_FEET       = 8;
 INVSLOT_WRIST      = 9;
 INVSLOT_HAND       = 10;
 INVSLOT_FINGER1        = 11;
 INVSLOT_FINGER2        = 12;
 INVSLOT_TRINKET1   = 13;
 INVSLOT_TRINKET2   = 14;
 INVSLOT_BACK       = 15;
 INVSLOT_MAINHAND   = 16;
 INVSLOT_OFFHAND        = 17;
 INVSLOT_RANGED     = 18;
 INVSLOT_TABARD     = 19;
 INVSLOT_LAST_EQUIPPED = INVSLOT_TABARD;
```

If you choose to use these instead of the appropriate API, you should use the constant name, not the number itself. This ensures that if Blizzard later updates their constants your code should continue to work.

The following are the convenience functions that can be used to obtain inventoryIds:

- [`GetInventorySlotInfo`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/GetInventorySlotInfo)
- [`BankButtonIDToInvSlotID`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/BankButtonIDToInvSlotID)
- [`ContainerIDToInventoryID`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/ContainerIDToInventoryID)
- [`KeyRingButtonIDToInvSlotID`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/KeyRingButtonIDToInvSlotID)

---

← [API Types](../API Types.md)
