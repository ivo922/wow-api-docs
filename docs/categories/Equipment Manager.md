# Equipment Manager functions

← [WoW API Docs](../index.md)

**18** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#equipmgr)

---

## CanUseEquipmentSets

Returns whether the player has enabled the equipment manager. Despite the name, this returns true when the player has enabled the use of the equipment manager through the interface or CVars.

**Signature:**

```lua
enabled = CanUseEquipmentSets()
```

**Returns:**

- `enabled` - Has the player enable the equipment manager (`boolean`)

---

## DeleteEquipmentSet `confirmation`

Deletes an equipment set

**Signature:**

```lua
DeleteEquipmentSet("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

---

## EquipmentManagerClearIgnoredSlotsForSave

Clears the list of equipment slots to be ignored when saving sets

**Signature:**

```lua
EquipmentManagerClearIgnoredSlotsForSave()
```

---

## EquipmentManagerIgnoreSlotForSave

Adds an equipment slot to the list of those ignored when saving sets. Creating or saving a set with [`SaveEquipmentSet()`](Equipment Manager.md#saveequipmentset-confirmation) will ignore any slots on the list, allowing the player to create sets which only switch certain items (e.g. to equip a fishing pole and hat while leaving non-fishing-related items equipped).

**Signature:**

```lua
EquipmentManagerIgnoreSlotForSave(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## EquipmentManagerIsSlotIgnoredForSave

Returns whether the contents of an equipment slot will be included when saving sets

**Signature:**

```lua
isIgnored = EquipmentManagerIsSlotIgnoredForSave(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `isIgnored` - True if the contents of the slot will not be included when next creating or saving an equipment set; otherwise false (`boolean`)

---

## EquipmentManagerUnignoreSlotForSave

Removes an equipment slot from the list of those ignored when saving sets. Creating or saving a set with [`SaveEquipmentSet()`](Equipment Manager.md#saveequipmentset-confirmation) will ignore any slots on the list, allowing the player to create sets which only switch certain items (e.g. to equip a fishing pole and hat while leaving non-fishing-related items equipped).

**Signature:**

```lua
EquipmentManagerUnignoreSlotForSave(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

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

## EquipmentSetContainsLockedItems

Returns whether an equipment set contains locked items. Locked items are those in a transient state -- e.g. on the cursor for moving within the player's bags, placed in the Send Mail or Trade UIs, etc. -- for which the default UI displays the item's icon as grayed out. A set cannot be equipped if it contains locked items.

**Signature:**

```lua
isLocked = EquipmentSetContainsLockedItems("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

**Returns:**

- `isLocked` - True if the equipment set contains locked items (`boolean`)

---

## GetEquipmentSetInfo

Returns information about an equipment set (specified by index)

**Signature:**

```lua
name, icon, setID = GetEquipmentSetInfo(index)
```

**Arguments:**

- `index` - Index of an equipment set (between 1 and [`GetNumEquipmentSets()`](Equipment Manager.md#getnumequipmentsets)) (`number`)

**Returns:**

- `name` - Name of the equipment set (`string`)
- `icon` - Path to an icon texture for the equipment set (`string`)
- `setID` - Internal ID number for the set (not used elsewhere in API) (`number`)

---

## GetEquipmentSetInfoByName

Returns information about an equipment set

**Signature:**

```lua
icon, setID = GetEquipmentSetInfoByName("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

**Returns:**

- `icon` - Unique part of the path to an icon texture for the equipment set; prepend `"Interface\Icons\"` for the full path (`string`)
- `setID` - Internal ID number for the set (not used elsewhere in API) (`number`)

---

## GetEquipmentSetItemIDs

Returns a table listing the items in an equipment set

**Signature:**

```lua
itemIDs = GetEquipmentSetItemIDs("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

**Returns:**

- `itemIDs` - A table listing the [`itemID`](../types/itemID.md)s of the set's contents, keyed by [`inventoryID`](../types/inventoryID.md) (`table`)

---

## GetEquipmentSetLocations

Returns a table listing the locations of the items in an equipment set

**Signature:**

```lua
itemIDs = GetEquipmentSetLocations("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

**Returns:**

- `itemIDs` - A table listing the [`itemLocation`](../types/itemLocation.md)s of the set's contents, keyed by [`inventoryID`](../types/inventoryID.md) (`table`)

---

## GetNumEquipmentSets

Returns the number of saved equipment sets

**Signature:**

```lua
numSets = GetNumEquipmentSets()
```

**Returns:**

- `numSets` - Number of saved equipment sets (`number`)

---

## PickupEquipmentSet

Puts an equipment set (specified by index) on the cursor. Can be used to place an equipment set in an action bar slot.

**Signature:**

```lua
PickupEquipmentSet(index)
```

**Arguments:**

- `index` - Index of an equipment set (between 1 and [`GetNumEquipmentSets()`](Equipment Manager.md#getnumequipmentsets)) (`number`)

---

## PickupEquipmentSetByName

Puts an equipment set on the cursor. Can be used to place an equipment set in an action bar slot.

**Signature:**

```lua
PickupEquipmentSetByName("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

---

## RenameEquipmentSet

Changes the name of a saved equipment set

---

## SaveEquipmentSet `confirmation`

Saves or creates an equipment set with the player's currently equipped items. If a set with the same name already exists, that set's contents are overwritten.

Set names are case sensitive: if a "Fishing" set already exists, saving a "fishing" set will create a new set instead of overwriting the "Fishing" set.

**Signature:**

```lua
SaveEquipmentSet("name", icon)
```

**Arguments:**

- `name` - Name of the set (`string`)
- `icon` - Index of an icon to associate with the set: between `1` and [`GetNumMacroIcons()`](Macro.md#getnummacroicons) for an icon from the set of macro icons; values between `-INVSLOT_FIRST_EQUIPPED` and `-INVSLOT_LAST_EQUIPPED` for the icon of an item in the equipment set at that (negative) [`inventoryID`](../types/inventoryID.md) (`number`)

---

## UseEquipmentSet

Equips the items in an equipment set

**Signature:**

```lua
equipped = UseEquipmentSet("name")
```

**Arguments:**

- `name` - Name of an equipment set (case sensitive) (`string`)

**Returns:**

- `equipped` - true if the set was equipped; otherwise nil (`boolean`)

---

← [WoW API Docs](../index.md)
