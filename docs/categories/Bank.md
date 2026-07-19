# Bank functions

← [WoW API Docs](../index.md)

**6** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#bank)

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

## CloseBankFrame

Ends interaction with the bank. Causes the `BANKFRAME_CLOSED` event to fire, indicating that APIs querying bank contents may no longer return valid results.

**Signature:**

```lua
CloseBankFrame()
```

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

## GetBankSlotCost

Returns the cost of the next purchasable bank bag slot. Returns `999999999` if the player owns all available slots.

**Signature:**

```lua
cost = GetBankSlotCost()
```

**Returns:**

- `cost` - Cost of the next available bank bag slot (in copper) (`number`)

---

## GetNumBankSlots

Returns information about purchased bank bag slots

**Signature:**

```lua
numSlots, isFull = GetNumBankSlots()
```

**Returns:**

- `numSlots` - Number of bank bag slots the player has purchased (`number`)
- `isFull` - 1 if the player has purchased all available slots; otherwise nil (`1nil`)

---

## PurchaseSlot `confirmation`

Purchases the next available bank slot. Only available while interacting with a banker NPC (i.e. between the `BANKFRAME_OPENED` and `BANKFRAME_CLOSED` events).

**Signature:**

```lua
PurchaseSlot()
```

---

← [WoW API Docs](../index.md)
