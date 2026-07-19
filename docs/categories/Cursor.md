# Cursor functions

← [WoW API Docs](../index.md)

**50** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#cursor)

---

## AddTradeMoney

Adds the money currently on the cursor to the trade window

**Signature:**

```lua
AddTradeMoney()
```

---

## AutoEquipCursorItem

Equips the item on the cursor. The item is automatically equipped in the first available slot in which it fits. To equip an item in a specific slot, see [`EquipCursorItem()`](Cursor.md#equipcursoritem).

Causes an error message ([`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md)) if the item on the cursor cannot be equipped. Does nothing if the cursor does not contain an item.

**Signature:**

```lua
AutoEquipCursorItem()
```

---

## ClearCursor

Clears any contents attached to the cursor. If the cursor contains an item picked up from inventory (equipment slots) or a container, the item returns to its point of origin and the inventory or container slot is unlocked. (To destroy an item, see [`DeleteCursorItem()`](Cursor.md#deletecursoritem-confirmation)).

If the cursor contains an action, that action is deleted (but not the spell, item, macro, etc that it represents).

If the cursor contains any other data type, nothing happens other than the cursor being reverted to its default state -- picking up such objects has no effect on their points of origin.

**Signature:**

```lua
ClearCursor()
```

---

## ClickAuctionSellItemButton

Picks up an item from or puts an item into the "Create Auction" slot. If the cursor is empty and the slot contains an item, that item is put onto the cursor. If the cursor contains an item and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the slot are exchanged.

Only has effect if the player is interacting with an auctioneer (i.e. between the [`AUCTION_HOUSE_SHOW`](../events/AUCTION_HOUSE_SHOW.md) and [`AUCTION_HOUSE_CLOSED`](../events/AUCTION_HOUSE_CLOSED.md) events). Causes an error message ([`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md)) if the item on the cursor cannot be put up for auction (e.g. if the item is soulbound).

**Signature:**

```lua
ClickAuctionSellItemButton()
```

---

## ClickSendMailItemButton

Picks up an item from or puts an item into an attachment slot for sending mail. If the cursor is empty and the mail attachment slot contains an item, that item is put onto the cursor. If the cursor contains an item and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the mail attachment slot are exchanged.

Only has effect if the player is interacting with a mailbox (i.e. between the [`MAIL_SHOW`](../events/MAIL_SHOW.md) and [`MAIL_CLOSED`](../events/MAIL_CLOSED.md) events). Causes an error message ([`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md)) if an invalid mail attachment slot is specified or if the item on the cursor cannot be mailed (e.g. if the item is soulbound).

**Signature:**

```lua
ClickSendMailItemButton(index, autoReturn)
```

**Arguments:**

- `index` - Index of a mail attachment slot (between 1 and `ATTACHMENTS_MAX_SEND`) (`number`)
- `autoReturn` - True to automatically return the item in the given attachment slot to the player's bags; false or omitted to put the item on the cursor (`boolean`)

---

## ClickSocketButton

Picks up or places a gem in the Item Socketing UI. If the Item Socketing UI is open and the cursor contains a socketable gem, places the gem into socket `index`. If the cursor does not hold an item and socket `index` is not locked, picks up the gem in that socket.

Only has an effect while the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
ClickSocketButton(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Examples:**

```lua
-- Put the item in the top left slot of the backpack into the first gem socket
PickupContainerItem(0,1)
ClickSocketButton(1)
```

---

## ClickTargetTradeButton

Interacts with an item in a slot offered for trade by the target. Only meaningful when used with the last (7th) trade slot: if an enchantment-type spell is currently awaiting a target (i.e. the glowing hand cursor is showing), targets the item in the given trade slot for the enchantment. (The enchantment to be applied then shows for both parties in the trade, but is not actually performed until both parties accept the trade.)

**Signature:**

```lua
ClickTargetTradeButton(index)
```

**Arguments:**

- `index` - Index of an item slot on the target's side of the trade window (between 1 and `MAX_TRADE_ITEMS`) (`number`)

---

## ClickTradeButton

**Signature:**

```lua
ClickTradeButton(index)
```

**Arguments:**

- `index` - The index of the trade button window to click (`number`)

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

## CursorHasItem

Returns whether an item is on the cursor. See [`GetCursorInfo()`](Cursor.md#getcursorinfo) for more detailed information.

**Signature:**

```lua
hasItem = CursorHasItem()
```

**Returns:**

- `hasItem` - 1 if the cursor is currently holding an item; otherwise nil (`1nil`)

---

## CursorHasMacro

Returns whether a macro is on the cursor. See [`GetCursorInfo()`](Cursor.md#getcursorinfo) for more detailed information.

**Signature:**

```lua
hasMacro = CursorHasMacro()
```

**Returns:**

- `hasMacro` - 1 if the cursor is currently holding a macro; otherwise nil (`1nil`)

---

## CursorHasMoney

Returns whether an amount of the player's money is on the cursor. Returns `nil` if the cursor holds guild bank money. See [`GetCursorInfo()`](Cursor.md#getcursorinfo) for more detailed information.

**Signature:**

```lua
hasMoney = CursorHasMoney()
```

**Returns:**

- `hasMoney` - 1 if the cursor is currently holding an amount of the player's money; otherwise nil (`1nil`)

---

## CursorHasSpell

Returns whether a spell is on the cursor. See [`GetCursorInfo()`](Cursor.md#getcursorinfo) for more detailed information.

**Signature:**

```lua
hasSpell = CursorHasSpell()
```

**Returns:**

- `hasSpell` - 1 if the cursor is currently holding a spell; otherwise nil (`1nil`)

---

## DeleteCursorItem `confirmation`

Destroys the item on the cursor. Used in the default UI when accepting the confirmation prompt that appears when dragging and dropping an item to an empty area of the screen.

**Signature:**

```lua
DeleteCursorItem()
```

---

## DropCursorMoney

Drops any money currently on the cursor, returning it to where it was taken from

**Signature:**

```lua
DropCursorMoney()
```

---

## DropItemOnUnit

"Gives" the item on the cursor to another unit; results vary by context. If the unit is a friendly player, adds the item to the trade window (opening it if necessary, and placing it in the first available trade slot or the "will not be traded" slot depending on whether the item is soulbound). If the unit is the player's pet and the player is a Hunter, attempts to feed the item to the pet (since this casts the Feed Pet spell, in this case this action is protected and can only be called by the Blizzard user interface). For other units, nothing happens and the item remains on the cursor.

**Signature:**

```lua
DropItemOnUnit("unit") or DropItemOnUnit("name")
```

**Arguments:**

- `unit` - A unit to receive the item (`string`, [unitID](../types/unitID.md))
- `name` - Name of a unit to receive the item; only valid for `player`, `pet`, and party/raid members (`string`)

---

## EquipCursorItem

Puts the item on the cursor into a specific equipment slot. If the item on the cursor can be equipped but does not fit in the given slot, the item is automatically equipped in the first available slot in which it fits (as with [`AutoEquipCursorItem()`](Cursor.md#autoequipcursoritem)). Thus, this function is most useful when dealing with items which can be equipped in more than one slot: containers, rings, trinkets, and (for dual-wielding characters) one-handed weapons.

Causes an error message ([`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md)) if the item on the cursor cannot be equipped. Does nothing if the cursor does not contain an item.

**Signature:**

```lua
EquipCursorItem(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## GetCursorInfo

Returns information about the contents of the cursor

**Signature:**

```lua
type, data, subType = GetCursorInfo()
```

**Returns:**

- `type` - Type of data attached to the cursor (`string`)
  - `companion`
  - `equipmentset`
  - `guildbankmoney`
  - `item`
  - `macro`
  - `merchant`
  - `money`
  - `spell`
- `data` - Identifier for the data on the cursor; varies by type: (`value`)
  - `companion` - Index of the companion in the non-combat pet or mount list (`number`)
  - `equipmentset` - Name of the equipment set (`string`)
  - `guildbankmoney` - Amount of the money from the guild bank (in copper) (`number`)
  - `item` - Numeric identifier for the item (`number`, [`itemID`](../types/itemID.md))
  - `macro` - Index of the macro in the macro listing (`number`, [`macroID`](../types/macroID.md))
  - `merchant` - Index of the item in the vendor's listings (`number`)
  - `money` - Amount of the player's money (in copper) (`number`)
  - `spell` - Index of the spell in the player's spellbook (`number`, [`spellbookID`](../types/spellbookID.md))
- `subType` - Secondary identifier for the data on the cursor; used only for certain types: (`string`)
  - `companion` - `"CRITTER"` or `"MOUNT"`, indicating whether the returned `data` is an index in the non-combat pet or mount list
  - `item` - A complete [`hyperlink`](../types/hyperlink.md) for the item
  - `spell` - `"spell"` or `"pet"`, indicating whether the returned `data` is an index in the player's or pet's spellbook

---

## GetCursorMoney

Returns the amount of money currently on the cursor

**Signature:**

```lua
cursorMoney = GetCursorMoney()
```

**Returns:**

- `cursorMoney` - Amount of money currently on the cursor (in copper) (`number`)

---

## GetCursorPosition

Returns the absolute position of the mouse cursor

**Signature:**

```lua
cursorX, cursorY = GetCursorPosition()
```

**Returns:**

- `cursorX` - Scale-independent X coordinate of the cursor's current position (`number`)
- `cursorY` - Scale-independent Y coordinate of the cursor's current position (`number`)

---

## GetMouseFocus

Returns the frame that is currently under the mouse, and has mouse input enabled.

**Signature:**

```lua
frame = GetMouseFocus()
```

**Returns:**

- `frame` - The frame that currently has the mouse focus (`table`)

**Examples:**

```lua
-- Returns the name of the frame under the mouse, if it's named
local frame = GetMouseFocus()
if not frame then
  ChatFrame1:AddMessage("There is no mouse enabled frame under the cursor")
else
  local name = frame:GetName() or tostring(frame)
  ChatFrame1:AddMessage(name .. " has the mouse focus")
end
```

---

## HideRepairCursor

Returns the cursor to normal mode after use of [`ShowRepairCursor()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ShowRepairCursor)

**Signature:**

```lua
HideRepairCursor()
```

---

## InRepairMode

Returns whether the item repair cursor mode is currently active. Repair mode is entered by calling [`ShowRepairCursor()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ShowRepairCursor) and exited by calling [`HideRepairCursor()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/HideRepairCursor); while in repair mode, calling [`PickupContainerItem()`](Container.md#pickupcontaineritem) or [`PickupInventoryItem()`](Cursor.md#pickupinventoryitem) will attempt to repair the item (and deduct the cost of such from the player's savings) instead of putting it on the cursor.

**Signature:**

```lua
inRepair = InRepairMode()
```

**Returns:**

- `inRepair` - 1 if repair mode is currently active; otherwise nil (`1nil`)

---

## PickupAction `nocombat`

Puts the contents of an action bar slot onto the cursor or the cursor contents into an action bar slot. After an action is picked up via this function, it can only be placed into other action bar slots (with [`PlaceAction()`](Action.md#placeaction-nocombat) or by calling `PickupAction()` again), even if the action is an item which could otherwise be placed elsewhere. Unlike many other "pickup" cursor functions, this function removes the picked-up action from the source slot -- an action slot can be emptied by calling this function followed by [`ClearCursor()`](Cursor.md#clearcursor).

If the action slot is empty and the cursor already holds an action, a spell, a companion (mount or non-combat pet), a macro, an equipment set, or an item (with a "Use:" effect), it is put into the action slot. If both the cursor and the slot hold an action (or any of the above data types), the contents of the cursor and the slot are exchanged.

**Signature:**

```lua
PickupAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](../types/actionID.md))

---

## PickupBagFromSlot

Puts an equipped container onto the cursor

**Signature:**

```lua
PickupBagFromSlot(slot)
```

**Arguments:**

- `slot` - An inventory slot containing a bag (see [`GetInventorySlotInfo()`](Inventory.md#getinventoryslotinfo), [`ContainerIDToInventoryID()`](Container.md#containeridtoinventoryid)) (`number`, [inventoryID](../types/inventoryID.md))

---

## PickupCompanion

Puts a non-combat pet or mount onto the cursor

**Signature:**

```lua
PickupCompanion("type", index)
```

**Arguments:**

- `type` - Type of companion (`string`)
  - `CRITTER` - A non-combat pet
  - `MOUNT` - A mount
- `index` - Index of a companion (between 1 and [`GetNumCompanions(type)`](Companion.md#getnumcompanions)) (`number`)

---

## PickupContainerItem

Picks up an item from or puts an item into a slot in one of the player's bags or other containers. If the cursor is empty and the referenced container slot contains an item, that item is put onto the cursor. If the cursor contains an item and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the container slot are exchanged.

An item picked up from a container is not removed from its slot (until put elsewhere); when an item is picked up, the slot becomes locked, preventing other changes to its contents until the disposition (movement, trade, mailing, auctioning, destruction, etc) of the picked-up item is resolved.

**Signature:**

```lua
PickupContainerItem(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))

---

## PickupGuildBankItem

Picks up an item from or puts an item into the guild bank. If the cursor is empty and the referenced guild bank slot contains an item, that item is put onto the cursor. If the cursor contains an item and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the guild bank slot are exchanged.

**Signature:**

```lua
PickupGuildBankItem(tab, slot)
```

**Arguments:**

- `tab` - Index of a guild bank tab (`number`)
- `slot` - Index of an item slot in the guild bank tab (`number`)

---

## PickupGuildBankMoney

Puts money from the guild bank onto the cursor. Money is not actually withdrawn from the guild bank; in the default UI, when the cursor "puts" the money into one of the player's bags, it calls [`WithdrawGuildBankMoney()`](Guild bank.md#withdrawguildbankmoney-confirmation).

**Signature:**

```lua
PickupGuildBankMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to pick up (in copper) (`number`)

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

## PickupItem

Puts an arbitrary item onto the cursor. Puts an item onto the cursor regardless of its location (equipped, bags, bank or not even in the player's possession); can be used to put an item into an action slot (see [`PlaceAction()`](Action.md#placeaction-nocombat)) even if the player does not currently hold the item. Since the item is not picked up from a specific location, this function cannot be used to move an item to another bag, trade it to another player, attach it to a mail message, destroyed, etc.

**Signature:**

```lua
PickupItem(itemID) or PickupItem("itemName") or PickupItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

---

## PickupMacro

Puts a macro onto the cursor

**Signature:**

```lua
PickupMacro(index) or PickupMacro("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](../types/macroID.md))
- `name` - Name of a macro (`string`)

---

## PickupMerchantItem

Puts an item available for purchase from a vendor onto the cursor

**Signature:**

```lua
PickupMerchantItem(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

---

## PickupPetAction

Puts the contents of a pet action slot onto the cursor or the cursor contents into a pet action slot. Only pet actions and spells from the "pet" portion of the spellbook can be placed into pet action slots.

If the cursor is empty and the referenced pet action slot contains an action, that action is put onto the cursor (but remains in the slot). If the cursor contains a pet action or pet spell and the slot is empty, the action/spell is placed into the slot. If both the cursor and the slot contain pet actions, the contents of the cursor and the pet action slot are exchanged.

**Signature:**

```lua
PickupPetAction(index)
```

**Arguments:**

- `index` - Index of a pet action (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

---

## PickupPlayerMoney

Puts an amount of the player's money onto the cursor. Money is not immediately deducted from the player's total savings (though it appears such on the default UI's money displays, which generally show [`GetMoney()`](Money.md#getmoney)`-`[`GetCursorMoney()`](Cursor.md#getcursormoney)).

**Signature:**

```lua
PickupPlayerMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to put on the cursor (in copper) (`number`)

---

## PickupSpell

Puts a spell onto the cursor

**Signature:**

```lua
PickupSpell(spellID)
```

**Arguments:**

- `spellID` - The spellID of the spell (`number`, [spellID](../types/spellID.md))

---

## PickupStablePet

Puts a pet from the stables onto the cursor. Use with [`ClickStablePet`](Pet Stable.md#clickstablepet) to move pets between stabled and active status.

**Signature:**

```lua
PickupStablePet(index)
```

**Arguments:**

- `index` - Index of a stable slot (`number`)
  - `0` - Active pet
  - `1 to NUM_PET_STABLE_SLOTS` - A stable slot

---

## PickupTradeMoney

Puts money offered by the player for trade onto the cursor. Money put onto the cursor is subtracted from the amount offered for trade (see [`GetPlayerTradeMoney()`](Money.md#getplayertrademoney)).

**Signature:**

```lua
PickupTradeMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to take from the trade window (in copper) (`number`)

---

## PlaceAction `nocombat`

Puts the contents of the cursor into an action bar slot. If the action slot is empty and the cursor already holds an action, a spell, a companion (mount or non-combat pet), a macro, an equipment set, or an item (with a "Use:" effect), it is put into the action slot. If both the cursor and the slot hold an action (or any of the above data types), the contents of the cursor and the slot are exchanged.

Does nothing if the cursor is empty.

**Signature:**

```lua
PlaceAction(slot)
```

**Arguments:**

- `slot` - Destination action bar slot (`number`, [actionID](../types/actionID.md))

---

## PutItemInBackpack

Puts the item on the cursor into the player's backpack. The item will be placed in the lowest numbered slot ([`containerSlotID`](../types/containerSlotID.md)) in the player's backpack.

Causes an error message ([`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md)) if the backpack is full.

**Signature:**

```lua
hadItem = PutItemInBackpack()
```

**Returns:**

- `hadItem` - 1 if the cursor had a item; otherwise nil (`1nil`)

---

## PutItemInBag

Puts the item on the cursor into one of the player's bags or other containers. The item will be placed in the lowest numbered slot ([`containerSlotID`](../types/containerSlotID.md)) in the container.

Causes an error message ([`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md)) if the container is full. Cannot be used to place an item into the player's backpack; see [`PutItemInBackpack()`](Container.md#putiteminbackpack).

**Signature:**

```lua
hadItem = PutItemInBag(inventory)
```

**Arguments:**

- `inventory` - Index of one of the player's equipment or container slots (`number`, [inventoryID](../types/inventoryID.md))

**Returns:**

- `hadItem` - 1 if the cursor had a item; otherwise nil (`1nil`)

---

## ResetCursor

Returns the cursor to its normal appearance (the glove pointer) and behavior. Has effect after the cursor image/mode has been changed via [`SetCursor()`](Cursor.md#setcursor), [`ShowContainerSellCursor()`](Cursor.md#showcontainersellcursor), or similar. Has no immediately visible effect if the cursor is holding an item, spell, or other data.

**Signature:**

```lua
ResetCursor()
```

---

## SetCursor

Changes the mouse cursor image. Changes only the appearance of the mouse cursor, not its behavior (and has no effect if the cursor is holding an item, spell, or other data). Passing `nil` will revert the cursor to its default image.

Normally used in a frame's `OnEnter` handler to change the cursor used while the mouse is over the frame. If used elsewhere, the cursor will likely be immediately reverted to default (due to the mouse handlers of other frames doing the same).

**Signature:**

```lua
SetCursor("cursor")
```

**Arguments:**

- `cursor` - Path to a texture to use as the cursor image (must be 32x32 pixels) or one of the built-in cursor tokens. Valid cursor tokens can be found in the example code. (`string`)

---

## ShowBuybackSellCursor

Changes the cursor to prepare for repurchasing an item recently sold to a vendor. Only changes the cursor image and mode if the given `index` contains an item.

**Signature:**

```lua
ShowBuybackSellCursor(index)
```

**Arguments:**

- `index` - Index of an item in the buyback listing (between 1 and [`GetNumBuybackItems()`](Merchant.md#getnumbuybackitems)) (`number`)

---

## ShowContainerSellCursor

Changes the cursor to prepare for selling an item in the player's bags to a vendor. Only changes the cursor image and mode if the given `container` and `slot` contain an item.

While the cursor is in "sell" mode, [`UseContainerItem()`](Container.md#usecontaineritem-protected) sells the item to the vendor instead of using it.

**Signature:**

```lua
ShowContainerSellCursor(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))

---

## ShowInventorySellCursor

Changes the cursor to prepare for selling an equipped item to a vendor. Only changes the cursor image and mode if the given `slot` contains an item.

(Unlike [`ShowContainerSellCursor()`](Cursor.md#showcontainersellcursor), does not change the behavior of other functions to enable selling of items. Unused in the default UI.)

**Signature:**

```lua
ShowInventorySellCursor(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

## ShowMerchantSellCursor

Changes the cursor to prepare for buying an item from a vendor. Only changes the cursor image and mode if the given `index` contains an item.

**Signature:**

```lua
ShowMerchantSellCursor(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

---

## ShowRepairCursor

Puts the cursor in item repair mode. Unlike most other cursor functions, this functions changes the behavior as well as the appearance of the mouse cursor: while repair mode is active, calling [`PickupContainerItem()`](Container.md#pickupcontaineritem) or [`PickupInventoryItem()`](Cursor.md#pickupinventoryitem) will attempt to repair the item (and deduct the cost of such from the player's savings) instead of putting it on the cursor.

Only has effect while the player is interacting with a vendor which can perform repairs; i.e. between the [`MERCHANT_SHOW`](../events/MERCHANT_SHOW.md) and [`MERCHANT_CLOSED`](../events/MERCHANT_CLOSED.md) events, and only if [`CanMerchantRepair()`](Merchant.md#canmerchantrepair) returns `1`.

**Signature:**

```lua
ShowRepairCursor()
```

---

## SplitContainerItem

Picks up only part of a stack of items from one of the player's bags or other containers. Has no effect if the given `amount` is greater than the number of items stacked in the slot.

**Signature:**

```lua
SplitContainerItem(container, slot, amount)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))
- `amount` - Number of items from the stack to pick up (`number`)

---

## SplitGuildBankItem

Picks up only part of a stack of items from the guild bank. Has no effect if the given `amount` is greater than the number of items stacked in the slot.

**Signature:**

```lua
SplitGuildBankItem(tab, slot, amount)
```

**Arguments:**

- `tab` - Index of a guild bank tab (`number`)
- `slot` - Index of an item slot in the guild bank tab (`number`)
- `amount` - Number of items from the stack to pick up (`number`)

---

← [WoW API Docs](../index.md)
