# Inventory functions

← [WoW API Docs](../index.md)

**30** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#inventory)

---

## AutoEquipCursorItem

Equips the item on the cursor. The item is automatically equipped in the first available slot in which it fits. To equip an item in a specific slot, see [`EquipCursorItem()`](Cursor.md#equipcursoritem).

Causes an error message ([`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE)) if the item on the cursor cannot be equipped. Does nothing if the cursor does not contain an item.

**Signature:**

```lua
AutoEquipCursorItem()
```

---

## BankButtonIDToInvSlotID

Returns the [`inventoryID`](../types/inventoryID.md) corresponding to a bank item or bag slot

**Signature:**

```lua
inventoryID = BankButtonIDToInvSlotID(buttonID [, isBag])
```

**Arguments:**

- `buttonID` - Numeric ID of an item or bag slot in the bank UI (`number`)
- `isBag` - 1 if the given ID corresponds to a bank bag slot; nil if the ID corresponds to an item slot (`1nil`)

**Returns:**

- `inventoryID` - An inventory slot ID usable with various Inventory API functions (`number`, [inventoryID](../types/inventoryID.md))

**Examples:**

```lua
-- While mousing over a button in the bank
local button = GetMouseFocus()
print("Inventory Slot:", BankButtonIDToInvSlotID(button:GetID(), button.isBag))
```

---

## CancelPendingEquip

Cancels equipping a bind-on-equip item. When the player attempts to equip a bind-on-equip item, the default UI displays a dialog warning that equipping the item will cause it to become soulbound; this function is called when canceling that dialog.

**Signature:**

```lua
CancelPendingEquip(index)
```

**Arguments:**

- `index` - Index of a pending equip warning; currently always 0 as only one equip warning will be given at a time (`number`)

---

## ContainerIDToInventoryID

Returns the [`inventoryID`](../types/inventoryID.md) corresponding to a given [`containerID`](../types/containerID.md)

**Signature:**

```lua
inventoryID = ContainerIDToInventoryID(container)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))

**Returns:**

- `inventoryID` - Identifier for the container usable with Inventory APIs (`number`, [inventoryID](../types/inventoryID.md))

**Examples:**

```lua
-- Switches the player's first bag (the one immediately left of the backpack)
-- with the first bank bag (or puts the bag into the bank if the bank bag slot is empty)
local firstBagSlot = ContainerIDToInventoryID(1)
local firstBankBagSlot = ContainerIDToInventoryID(5)
PickupInventoryItem(firstBagSlot)
PickupInventoryItem(firstBankBagSlot)
```

---

## CursorCanGoInSlot

Returns whether the item on the cursor can be equipped in an inventory slot. Returns `nil` if the cursor is empty or contains something other than an item.

**Signature:**

```lua
canBePlaced = CursorCanGoInSlot(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `canBePlaced` - 1 if the item on the cursor can be equipped in the given slot; otherwise nil (`1nil`)

---

## EquipCursorItem

Puts the item on the cursor into a specific equipment slot. If the item on the cursor can be equipped but does not fit in the given slot, the item is automatically equipped in the first available slot in which it fits (as with [`AutoEquipCursorItem()`](Cursor.md#autoequipcursoritem)). Thus, this function is most useful when dealing with items which can be equipped in more than one slot: containers, rings, trinkets, and (for dual-wielding characters) one-handed weapons.

Causes an error message ([`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE)) if the item on the cursor cannot be equipped. Does nothing if the cursor does not contain an item.

**Signature:**

```lua
EquipCursorItem(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## EquipItemByName

Attempts to equip an arbitrary item. The item is automatically equipped in the first available slot in which it fits. To equip an item in a specific slot, see [`EquipCursorItem()`](Cursor.md#equipcursoritem).

Causes an error message ([`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE)) if the specified item cannot be equipped. Does nothing if the specified item does not exist or is not in the player's possession.

**Signature:**

```lua
EquipItemByName(itemID) or EquipItemByName("itemName") or EquipItemByName("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

---

## EquipPendingItem `confirmation`

Confirms equipping a bind-on-equip item. Usable following the [`EQUIP_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/EQUIP_BIND_CONFIRM) or [`AUTOEQUIP_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUTOEQUIP_BIND_CONFIRM), which fires when the player attempts to equip a bind-on-equip item

**Signature:**

```lua
EquipPendingItem(index)
```

**Arguments:**

- `index` - Index provided by the [`EQUIP_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/EQUIP_BIND_CONFIRM) or [`AUTOEQUIP_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUTOEQUIP_BIND_CONFIRM) event; currently always 0 (`number`)

---

## EquipmentManager_UnpackLocation

Unpacks an inventory location bitfield into usable components

**Signature:**

```lua
player, bank, bags, location or slot, bag = EquipmentManager_UnpackLocation(location)
```

**Arguments:**

- `location` - A bit field that represents an item's location in the player's possession. This bit field can be obtained using the [`GetInventoryItemsForSlot`](Inventory.md#getinventoryitemsforslot) function. (`number`)

**Returns:**

- `player` - A flag indicating whether or not the item exists in the player's inventory (i.e. an equipped item). (`boolean`)
- `bank` - A flag indicating whether or not the item exists in the payer's bank. (`boolean`)
- `bags` - A flag indicating whether or not the item exists in the player's bags. (`boolean`)
- `location or slot` - The inventory slot that contains the item, or the container slot that contains the item, if the item is in the player's bags. (`number`)
- `bag` - The bagID of the container that contains the item. (`number`)

---

## GetInventoryAlertStatus

Returns the durability warning status of an equipped item. Looking up the status returned by this function in the `INVENTORY_ALERT_COLORS` table provides color values, used in the default UI to highlight parts of the DurabiltyFrame (i.e. the "armored man" image) that appears when durability is low.

**Signature:**

```lua
status = GetInventoryAlertStatus(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `status` - Alert status for the item in the given slot (`number`)
  - `0` - No alert; the slot is empty, contains an item whose durability is above critical levels, or contains an item without a durability value
  - `1` - The item's durability is dangerously low
  - `2` - The item's durability is at zero (the item is broken)

---

## GetInventoryItemBroken

Returns whether an equipped item is broken

**Signature:**

```lua
isBroken = GetInventoryItemBroken("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `isBroken` - 1 if the item is broken (durability zero); otherwise nil (`1nil`)

---

## GetInventoryItemCooldown

Returns cooldown information about an equipped item

**Signature:**

```lua
start, duration, enable = GetInventoryItemCooldown("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the item is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the item is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the item is ready.) (`number`)

---

## GetInventoryItemCount

Returns the number of items stacked in an inventory slot.

Currently only returns meaningful information for the ammo slot.

**Signature:**

```lua
count = GetInventoryItemCount("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `count` - The amount of items stacked in the inventory slot (`number`)

---

## GetInventoryItemDurability

Returns the current durability level of an equipped item. If an item does not have durability (for example, heirlooms, tabards and some other items) then this function will simply return `nil`.

**Signature:**

```lua
durability, max = GetInventoryItemDurability(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `durability` - The item's current durability, the first number listed in the item's tooltip where it displays the durability information: for example 4 in 4/29. (`number`)
- `max` - The item's maximum durability, the first number listed in the item's tooltip where it displays the durability information: for example 29 in 4/29 (`number`)

---

## GetInventoryItemGems

Returns the gems socketed in an equipped item. The IDs returned refer to the gems themselves (not the enchantments they provide), and thus can be passed to `GetItemInfo()` to get a gem's name, quality, icon, etc.

**Signature:**

```lua
gem1, gem2, gem3 = GetInventoryItemGems(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `gem1` - Item ID of the first gem socketed in the item (`itemID`)
- `gem2` - Item ID of the second gem socketed in the item (`itemID`)
- `gem3` - Item ID of the third gem socketed in the item (`itemID`)

---

## GetInventoryItemID

Returns the item ID of an equipped item

**Signature:**

```lua
id = GetInventoryItemID("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `id` - Numeric ID of the item in the given slot (`itemID`)

---

## GetInventoryItemLink

Returns an item link for an equipped item

**Signature:**

```lua
link = GetInventoryItemLink("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `link` - An item link for the given item (`string`, [hyperlink](../types/hyperlink.md))

---

## GetInventoryItemQuality

Returns the quality level of an equipped item

**Signature:**

```lua
quality = GetInventoryItemQuality("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `quality` - The quality level of the item (`number`, [itemQuality](../types/itemQuality.md))

---

## GetInventoryItemTexture

Returns the icon texture for an equipped item

**Signature:**

```lua
texture = GetInventoryItemTexture("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `texture` - Path to an icon texture for the item (`string`)

---

## GetInventoryItemsForSlot

Returns a list of items that can be equipped in a given inventory slot

**Signature:**

```lua
availableItems = GetInventoryItemsForSlot(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `availableItems` - A table listing [`itemID`](../types/itemID.md)s of items which can be equipped in the slot, keyed by [`itemLocation`](../types/itemLocation.md) (`table`)

---

## GetInventorySlotInfo

Returns information about an inventory slot

**Signature:**

```lua
id, texture, checkRelic = GetInventorySlotInfo("slotName")
```

**Arguments:**

- `slotName` - Name of an inventory slot to query (`string`)
  - `AmmoSlot` - Ranged ammunition slot
  - `BackSlot` - Back (cloak) slot
  - `Bag0Slot` - Backpack slot
  - `Bag1Slot` - First bag slot
  - `Bag2Slot` - Second bag slot
  - `Bag3Slot` - Third bag slot
  - `ChestSlot` - Chest slot
  - `FeetSlot` - Feet (boots) slot
  - `Finger0Slot` - First finger (ring) slot
  - `Finger1Slot` - Second finger (ring) slot
  - `HandsSlot` - Hand (gloves) slot
  - `HeadSlot` - Head (helmet) slot
  - `LegsSlot` - Legs (pants) slot
  - `MainHandSlot` - Main hand weapon slot
  - `NeckSlot` - Necklace slot
  - `RangedSlot` - Ranged weapon or relic slot
  - `SecondaryHandSlot` - Off-hand (weapon, shield, or held item) slot
  - `ShirtSlot` - Shirt slot
  - `ShoulderSlot` - Shoulder slot
  - `TabardSlot` - Tabard slot
  - `Trinket0Slot` - First trinket slot
  - `Trinket1Slot` - Second trinket slot
  - `WaistSlot` - Waist (belt) slot
  - `WristSlot` - Wrist (bracers) slot

**Returns:**

- `id` - The numeric slotId usable in other Inventory functions (`number`)
- `texture` - The path to the texture to be displayed when this slot is empty (`string`)
- `checkRelic` - 1 if the slot might be the relic slot; otherwise nil. The ranged slot token is re-used for the relic slot; if this return is 1, [`UnitHasRelicSlot`](Unit.md#unithasrelicslot) should be used to determine how the slot should be displayed. (`1nil`)

---

## IsEquippedItem

Returns whether an item is currently equipped

**Signature:**

```lua
isEquipped = IsEquippedItem(itemID) or IsEquippedItem("itemName") or IsEquippedItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `isEquipped` - 1 if the item is equipped on the player character; otherwise nil (`1nil`)

**Examples:**

```lua
-- Check to see if your Alliance PvP trinket is equipped
IsEquippedItem("Medallion of the Alliance") then
  print("Your PvP trinket is already equipped.")
else
  print("*** Make sure to equip your PvP trinket ***")
end

-- Check to see if Staff of Infinite Mysteries (itemId 28633) is equipped
if IsEquippedItem(28633) then
  print("Your staff is equipped")
else
  print("Your staff is not equipped")
end
```

---

## IsEquippedItemType

Returns whether any items of a given type are currently equipped. Possible arguments include the localized names of item classes (as returned from [`GetAuctionItemClasses`](Auction.md#getauctionitemclasses); e.g. "Weapon", "Armor"), subclasses (as returned from [`GetAuctionItemSubClasses`](Auction.md#getauctionitemsubclasses); e.g. "One-handed axes", "Shields", "Cloth"), and the global tokens or localized names for equip locations (as returned from [`GetAuctionInvTypes`](Auction.md#getauctioninvtypes); e.g. "INVTYPE_WEAPONMAINHAND", "Off Hand").

**Signature:**

```lua
isEquipped = IsEquippedItemType("type")
```

**Arguments:**

- `type` - Name of an item class, subclass, or equip location (`string`)

**Returns:**

- `isEquipped` - 1 if the player has equipped any items of the given type; otherwise nil (`1nil`)

**Examples:**

```lua
-- Check to see if the player currently has a shield equipped
local hasShield = IsEquippedItemType("Shields")
if hasShield then
  print("You currently have a shield equipped")
else
  print("You do not have a shield equipped")
end
```

---

## IsInventoryItemLocked

Returns whether an inventory slot is locked. Items become locked while being moved, split, or placed into other UI elements (such as the mail, trade, and auction windows); the item is unlocked once such an action is completed.

**Signature:**

```lua
isLocked = IsInventoryItemLocked(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `isLocked` - 1 if the item in the inventory slot is locked; otherwise nil (`1nil`)

---

## KeyRingButtonIDToInvSlotID

Returns the [`inventoryID`](../types/inventoryID.md) corresponding to a slot in the keyring. The results of this function can be used with [`GetInventorySlotInfo()`](Inventory.md#getinventoryslotinfo) and other related inventory functions.

**Signature:**

```lua
slot = KeyRingButtonIDToInvSlotID(slot)
```

**Arguments:**

- `slot` - Index of a key slot within the keyring (`number`, [containerSlotID](../types/containerSlotID.md))

**Returns:**

- `slot` - Identifier for the key slot usable with Inventory APIs (`number`, [inventoryID](../types/inventoryID.md))

---

## PickupInventoryItem

Picks up an item from or puts an item into an equipment slot. If the cursor is empty and the referenced inventory slot contains an item, that item is put onto the cursor. If the cursor contains an item (which can be equipped in the slot) and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the inventory slot are exchanged.

An item picked up from an inventory slot is not removed from the slot (until put elsewhere); when an item is picked up, the slot becomes locked, preventing other changes to its contents until the disposition (movement, trade, destruction, etc) of the picked-up item is resolved.

**Signature:**

```lua
PickupInventoryItem(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## SetInventoryPortraitTexture

Sets a Texture object to display the icon of an equipped item. Adapts the square item icon texture to fit within the circular "portrait" frames used in many default UI elements.

**Signature:**

```lua
SetInventoryPortraitTexture(texture, "unit", slot)
```

**Arguments:**

- `texture` - A Texture object (`table`)
- `unit` - A unit whose item should be displayed; only valid for `player` (`string`, [unitID](../types/unitID.md))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## SocketInventoryItem

Opens an equipped item for socketing

**Signature:**

```lua
SocketInventoryItem(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## UpdateInventoryAlertStatus `internal`

This is a Blizzard internal function

---

## UseInventoryItem `protected`

Activate (as with right-clicking) an equipped item. If the `inventoryID` passed refers to an empty slot or a slot containing an item without a "Use:" action, this function is not protected (i.e. usable only by the Blizzard UI), but also has no effect.

**Signature:**

```lua
UseInventoryItem(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

← [WoW API Docs](../index.md)
