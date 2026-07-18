# Container functions

← [WoW API Docs](../index.md)

**24** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#container)

---

## ContainerIDToInventoryID

Returns the [`inventoryID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#inventoryID) corresponding to a given [`containerID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID)

**Signature:**

```lua
inventoryID = ContainerIDToInventoryID(container)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))

**Returns:**

- `inventoryID` - Identifier for the container usable with Inventory APIs (`number`, [inventoryID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#inventoryID))

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

## ContainerRefundItemPurchase

Sells an item purchased with alternate currency back to a vendor. Items bought with alternate currency (honor points, arena points, or special items such as Emblems of Heroism and Dalaran Cooking Awards) can be returned to a vendor for a full refund, but only within a limited time after the original purchase.

**Signature:**

```lua
ContainerRefundItemPurchase(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

---

## EquipmentManager_UnpackLocation

Unpacks an inventory location bitfield into usable components

**Signature:**

```lua
player, bank, bags, location or slot, bag = EquipmentManager_UnpackLocation(location)
```

**Arguments:**

- `location` - A bit field that represents an item's location in the player's possession. This bit field can be obtained using the [`GetInventoryItemsForSlot`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInventoryItemsForSlot) function. (`number`)

**Returns:**

- `player` - A flag indicating whether or not the item exists in the player's inventory (i.e. an equipped item). (`boolean`)
- `bank` - A flag indicating whether or not the item exists in the payer's bank. (`boolean`)
- `bags` - A flag indicating whether or not the item exists in the player's bags. (`boolean`)
- `location or slot` - The inventory slot that contains the item, or the container slot that contains the item, if the item is in the player's bags. (`number`)
- `bag` - The bagID of the container that contains the item. (`number`)

---

## GetBagName

Returns the name of one of the player's bags. Returns nil for the bank and keyring, for bank bags while the player is not at the bank, and for empty bag or bank bag slots.

**Signature:**

```lua
name = GetBagName(container)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))

**Returns:**

- `name` - Name of the container (`string`)

**Examples:**

```lua
-- Print the names of the player's bags to chat
for i=0,4 do
  local name = GetBagName(i)
  if name then
    print("Bag", i, ":", name)
  end
end
```

---

## GetContainerFreeSlots

Returns a list of open slots in a container. The optional argument `returnTable` allows for performance optimization in cases where this function is expected to be called repeatedly. Rather than creating new tables each time the function is called (eventually requiring garbage collection), an existing table can be recycled. (Note, however, that this function does not clear the table's contents; use [`wipe()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/wipe) first to guarantee consistent results.)

**Signature:**

```lua
slotTable = GetContainerFreeSlots(container [, returnTable])
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `returnTable` - Reference to a table to be filled with return values (`table`)

**Returns:**

- `slotTable` - A table listing the indices of open slots in the given container (`table`)

---

## GetContainerItemCooldown

Returns cooldown information about an item in the player's bags

**Signature:**

```lua
start, duration, enable = GetContainerItemCooldown(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `start` - The value of [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) at the moment the cooldown began, or 0 if the item is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the item is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the item is ready.) (`number`)

---

## GetContainerItemDurability

Returns durability status for an item in the player's bags

**Signature:**

```lua
durability, max = GetContainerItemDurability(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `durability` - The item's current durability (`number`)
- `max` - The item's maximum durability (`number`)

---

## GetContainerItemGems

Returns the gems socketed in an item in the player's bags. The IDs returned refer to the gems themselves (not the enchantments they provide), and thus can be passed to `GetItemInfo()` to get a gem's name, quality, icon, etc.

**Signature:**

```lua
gem1, gem2, gem3 = GetContainerItemGems(container, slot)
```

**Arguments:**

- `container` - The index of the container (`bagID`)
- `slot` - The slot within the given container; slots are numbered left-to-right, top-to-bottom, starting with the leftmost slot on the top row (`number`)

**Returns:**

- `gem1` - Item ID of the first gem socketed in the item (`itemID`)
- `gem2` - Item ID of the second gem socketed in the item (`itemID`)
- `gem3` - Item ID of the third gem socketed in the item (`itemID`)

---

## GetContainerItemID

Returns the item ID of an item in the player's bags

**Signature:**

```lua
id = GetContainerItemID(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `id` - Numeric ID of the item in the given slot (`itemID`)

---

## GetContainerItemInfo

Returns information about an item in the player's bags

**Signature:**

```lua
texture, count, locked, quality, readable, lootable, link = GetContainerItemInfo(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `texture` - Path to the icon texture for the item (`string`)
- `count` - Number of items in the slot (`number`)
- `locked` - 1 if the item is locked; otherwise nil. Items become locked while being moved, split, or placed into other UI elements (such as the mail, trade, and auction windows). (`1nil`)
- `quality` - Quality (or rarity) of the item (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))
- `readable` - 1 if the item is readable; otherwise nil. This value is used by the default UI to show a special cursor over items such as books and scrolls which can be read by right-clicking. (`1nil`)
- `lootable` - 1 if the item is a temporary container containing items that can be looted; otherwise nil. Examples include the Bag of Fishing Treasures and Small Spice Bag rewarded by daily quests, lockboxes (once unlocked), and the trunks occasionally found while fishing. (`1nil`)
- `link` - A hyperlink for the item (`itemLink`)

---

## GetContainerItemLink

Returns a hyperlink for an item in the player's bags

**Signature:**

```lua
link = GetContainerItemLink(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetContainerItemPurchaseInfo

Returns information about alternate currencies refunded for returning an item to vendors.

Items bought with alternate currency (honor points, arena points, or special items such as Emblems of Heroism and Dalaran Cooking Awards) can be returned to a vendor for a full refund, but only within a limited time after the original purchase.

If the given container slot is empty, contains an item which cannot be returned for an alternate currency refund, or contains an item for which the refund grace period has expired, all returns are `nil`.

**Signature:**

```lua
money, itemCount, refundSec, currecycount, hasEnchants = GetContainerItemPurchaseInfo(container, slot, IsEquipped)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))
- `IsEquipped` - wheather to get an equipped item info (`boolean`)

**Returns:**

- `money` - Amount of copper to be refunded (`number`)
- `itemCount` - Number of different item currencies to be refunded (e.g. the price a PvP mount is in 3 currencies, as it requires multiple battlegrounds' Marks of Honor) (`number`)
- `refundSec` - Seconds remaining until this item is no longer eligible to be returned for a refund (`number`)
- `currecycount` - Amount of currency to be refunded (`number`)
- `hasEnchants` - weather the item is enchanted (`number`)

---

## GetContainerItemPurchaseItem

Returns information about a specific currency refunded for returning an item to vendors. See [`GetContainerItemPurchaseInfo`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetContainerItemPurchaseInfo) for more information about alternate currency refunds.

**Signature:**

```lua
texture, quantity, link = GetContainerItemPurchaseItem(container, slot, index)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))
- `index` - Index of the currency type; between 1 and `itemCount`, where `itemCount` is the 4th return from `GetContainerItemPurchaseInfo()` for the same container and slot (`number`)

**Returns:**

- `texture` - Path to an icon texture for the currency item (`string`)
- `quantity` - Quantity of the currency item to be refunded (`number`)
- `link` - Hyperlink for the currency item (`itemLink`)

---

## GetContainerNumFreeSlots

Returns the number of free slots in a container and the types of items it can hold

**Signature:**

```lua
freeSlots, bagType = GetContainerNumFreeSlots(container)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))

**Returns:**

- `freeSlots` - Number of empty slots in the bag (`number`)
- `bagType` - Bitwise OR of the item families that can be put into the container; see [`GetItemFamily`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetItemFamily) for details (`number`, [bitfield](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#bitfield))

---

## GetContainerNumSlots

Returns the number of slots in one of the player's bags

**Signature:**

```lua
numSlots = GetContainerNumSlots(container)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))

**Returns:**

- `numSlots` - Number of item slots in the container (`number`)

---

## GetItemFamily

Returns information about special bag types that can hold a given item. The meaning of `bagType` varies depending on the item:

- If the item is a container, `bagType` indicates which kinds of items the container is limited to holding; a `bagType` of 0 indicates the container can hold any kind of item.
- If the item is not a container, `bagType` indicates which kinds of specialty containers can hold the item; a `bagType` of 0 indicates the item can only be put in general-purpose containers.

**Signature:**

```lua
bagType = GetItemFamily(itemID) or GetItemFamily("itemName") or GetItemFamily("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemString) portion of an item link (`string`)

**Returns:**

- `bagType` - Bitwise OR of bag type flags: (`number`, [bitfield](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#bitfield))
  - `0x0001` - Quiver
  - `0x0002` - Ammo Pouch
  - `0x0004` - Soul Bag
  - `0x0008` - Leatherworking Bag
  - `0x0010` - Inscription Bag
  - `0x0020` - Herb Bag
  - `0x0040` - Enchanting Bag
  - `0x0080` - Engineering Bag
  - `0x0100` - Keyring
  - `0x0200` - Gem Bag
  - `0x0400` - Mining Bag
  - `0x0800` - Unused
  - `0x1000` - Vanity Pets

---

## PickupBagFromSlot

Puts an equipped container onto the cursor

**Signature:**

```lua
PickupBagFromSlot(slot)
```

**Arguments:**

- `slot` - An inventory slot containing a bag (see [`GetInventorySlotInfo()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInventorySlotInfo), [`ContainerIDToInventoryID()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ContainerIDToInventoryID)) (`number`, [inventoryID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#inventoryID))

---

## PickupContainerItem

Picks up an item from or puts an item into a slot in one of the player's bags or other containers. If the cursor is empty and the referenced container slot contains an item, that item is put onto the cursor. If the cursor contains an item and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the container slot are exchanged.

An item picked up from a container is not removed from its slot (until put elsewhere); when an item is picked up, the slot becomes locked, preventing other changes to its contents until the disposition (movement, trade, mailing, auctioning, destruction, etc) of the picked-up item is resolved.

**Signature:**

```lua
PickupContainerItem(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

---

## PutItemInBackpack

Puts the item on the cursor into the player's backpack. The item will be placed in the lowest numbered slot ([`containerSlotID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID)) in the player's backpack.

Causes an error message ([`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE)) if the backpack is full.

**Signature:**

```lua
hadItem = PutItemInBackpack()
```

**Returns:**

- `hadItem` - 1 if the cursor had a item; otherwise nil (`1nil`)

---

## PutItemInBag

Puts the item on the cursor into one of the player's bags or other containers. The item will be placed in the lowest numbered slot ([`containerSlotID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID)) in the container.

Causes an error message ([`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE)) if the container is full. Cannot be used to place an item into the player's backpack; see [`PutItemInBackpack()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PutItemInBackpack).

**Signature:**

```lua
hadItem = PutItemInBag(inventory)
```

**Arguments:**

- `inventory` - Index of one of the player's equipment or container slots (`number`, [inventoryID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#inventoryID))

**Returns:**

- `hadItem` - 1 if the cursor had a item; otherwise nil (`1nil`)

---

## SetBagPortraitTexture

Sets a Texture object to display the icon of one of the player's bags. Adapts the square item icon texture to fit within the circular "portrait" frames used in many default UI elements.

**Signature:**

```lua
SetBagPortraitTexture(texture, container)
```

**Arguments:**

- `texture` - A Texture object (`table`)
- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))

---

## SocketContainerItem

Opens an item from the player's bags for socketing

**Signature:**

```lua
SocketContainerItem(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

---

## SplitContainerItem

Picks up only part of a stack of items from one of the player's bags or other containers. Has no effect if the given `amount` is greater than the number of items stacked in the slot.

**Signature:**

```lua
SplitContainerItem(container, slot, amount)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))
- `amount` - Number of items from the stack to pick up (`number`)

---

## UseContainerItem `protected`

Activate (as with right-clicking) an item in one of the player's bags. Has the same effect as right-clicking an item in the default UI; therefore, results may vary by context. In cases of conflict, conditions listed first override those below:

- If the bank, guild bank or reagent bank UI is open, moves the item into the bank, guild bank or reagent bank (or if the item is in the bank, guild bank or reagent bank, moves it into the player's inventory).
- If the trade UI is open, puts the item into the first available trade slot (or if the item is soulbound, into the "will not be traded" slot).
- If the merchant UI is open and not in repair mode, attempts to sell the item to the merchant.
- If the Send Mail UI is open, puts the item into the first available slot for message attachments.
- If an item is readable (e.g. [Lament of the Highborne](http://www.wowhead.com/?item=30632)), opens it for reading.
- If an item is lootable (e.g. [Magically Wrapped Gift](http://www.wowhead.com/?item=41426)), opens it for looting
- If an item can be equipped, attempts to equip the item (placing any currently equipped item of the same type into the container slot used).
- If an item has a "Use:" effect, activates said effect. *Under this condition **only**, the function is protected and can only be called by the Blizzard UI.*
- If none of the above conditions are true, nothing happens.

**Signature:**

```lua
UseContainerItem(container, slot [, "target" [, reagentBankAccessible]])
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))
- `target` - A unit to be used as target for the action (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `reagentBankAccessible` - Indicates if the reagent bank is accessible right now (so bank frame open and switched to reagent tab) (`boolean`)

---

← [WoW API Docs](../index.md)
