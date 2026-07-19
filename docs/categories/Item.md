# Item functions

← [WoW API Docs](../index.md)

**36** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#item)

---

## BindEnchant `confirmation`

Confirms enchanting an item (when the item will become soulbound as a result). Usable following the [`BIND_ENCHANT`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/BIND_ENCHANT) event which fires upon attempting to perform an enchantment that would cause the target item to become soulbound.

**Signature:**

```lua
BindEnchant()
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

## ConfirmBindOnUse `confirmation`

Confirms using an item, if using the item causes it to become soulbound. Usable in response to the [`USE_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/USE_BIND_CONFIRM) which fires when the player attempts to use a "Bind on Use" item.

**Signature:**

```lua
ConfirmBindOnUse()
```

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

## DeleteCursorItem `confirmation`

Destroys the item on the cursor. Used in the default UI when accepting the confirmation prompt that appears when dragging and dropping an item to an empty area of the screen.

**Signature:**

```lua
DeleteCursorItem()
```

---

## EndBoundTradeable `confirmation`

Confirms taking an action which renders a looted Bind on Pickup item non-tradeable. A Bind on Pickup item looted by the player can be traded to other characters who were originally eligible to loot it, but only within a limited time after looting. This period can be ended prematurely if the player attempts certain actions (such as enchanting the item).

**Signature:**

```lua
EndBoundTradeable(id)
```

**Arguments:**

- `id` - Number identifying the item (as provided by the [`END_BOUND_TRADEABLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/END_BOUND_TRADEABLE) event) (`number`)

---

## EndRefund `confirmation`

Confirms taking an action which renders a purchased item non-refundable. Items bought with alternate currency (honor points, arena points, or special items such as Emblems of Heroism and Dalaran Cooking Awards) can be returned to a vendor for a full refund, but only within a limited time after the original purchase. This period can be ended prematurely if the player attempts certain actions (such as enchanting the item).

**Signature:**

```lua
EndRefund(id)
```

**Arguments:**

- `id` - Number identifying the item (as provided by the [`END_REFUND`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/END_REFUND) event) (`number`)

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

## GetItemCooldown

Returns cooldown information about an arbitrary item

**Signature:**

```lua
start, duration, enable = GetItemCooldown(itemID) or GetItemCooldown("itemName") or GetItemCooldown("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the item is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the item is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the item is ready.) (`number`)

---

## GetItemCount

Returns information about how many of a given item the player has or on remaining item charges.

When the third argument `includeCharges` is true, the returned number indicates the total number of remaining charges for the item instead of how many of the item you have; e.g. if you have 3 Wizard Oils and one of them has been used twice, the returned value will be 13.

**Signature:**

```lua
itemCount = GetItemCount(itemId, includeBank, includeCharges) or GetItemCount("itemName", includeBank, includeCharges) or GetItemCount("itemLink", includeBank, includeCharges)
```

**Arguments:**

- `itemId` - An item id (`number`)
- `itemName` - An item name (`string`)
- `itemLink` - An item link (`string`)
- `includeBank` - true to include items in the bank in the returned count, otherwise false (`boolean`)
- `includeCharges` - true to count charges for applicable items, otherwise false (`boolean`)

**Returns:**

- `itemCount` - The number of the given item the player has in possession (possibly including items in the bank), or the total number of charges on those items (`number`)

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
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `bagType` - Bitwise OR of bag type flags: (`number`, [bitfield](../types/bitfield.md))
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

## GetItemGem

Returns information about gems socketed in an item

**Signature:**

```lua
name, link = GetItemGem(itemID, index) or GetItemGem("itemName", index) or GetItemGem("itemLink", index)
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)
- `index` - Index of a socket on the item (`number`)

**Returns:**

- `name` - Name of the gem in the socket (`string`)
- `link` - A hyperlink for the gem in the socket (`string`, [hyperlink](../types/hyperlink.md))

---

## GetItemIcon

Returns the path to an icon texture for the item. Unlike [`GetItemInfo`](Item.md#getiteminfo), this function always returns icons for valid items, even if the item is not in the client's cache.

**Signature:**

```lua
texture = GetItemIcon(itemID) or GetItemIcon("itemName") or GetItemIcon("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `texture` - Path to an icon texture for the item (`string`)

---

## GetItemInfo

Returns information about an item, by name, link or id. Only returns information for items in the WoW client's local cache; returns `nil` for items the client has not seen.

**Signature:**

```lua
name, link, quality, iLevel, reqLevel, class, subclass, maxStack, equipSlot, texture, vendorPrice = GetItemInfo(itemID) or GetItemInfo("itemName") or GetItemInfo("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`, [itemID](../types/itemID.md))
- `itemName` - An item's name. This value will only work if the player has the item in their bags. (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `name` - Name of the item (`string`)
- `link` - A hyperlink for the item (`string`, [hyperlink](../types/hyperlink.md))
- `quality` - Quality (rarity) level of the item. (`number`, [itemQuality](../types/itemQuality.md))
- `iLevel` - Internal level of the item; (`number`)
- `reqLevel` - Minimum character level required to use or equip the item (`number`)
- `class` - Localized name of the item's class/type (as in the list returned by [`GetAuctionItemClasses()`](Auction.md#getauctionitemclasses)) (`string`)
- `subclass` - Localized name of the item's subclass/subtype (as in the list returned by [`GetAuctionItemSubClasses()`](Auction.md#getauctionitemsubclasses)) (`string`)
- `maxStack` - Maximum stack size for the item (i.e. largest number of items that can be held in a single bag slot) (`number`)
- `equipSlot` - Non-localized token identifying the inventory type of the item (as in the list returned by [`GetAuctionItemInvTypes()`](Auction.md#getauctioninvtypes)); name of a global variable containing the localized name of the inventory type (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `vendorPrice` - Price an NPC vendor will pay to buy the item from the player. This value was added in patch 3.2. (`number`)

---

## GetItemQualityColor

Returns color values for use in displaying items of a given quality. Color components are floating-point values between 0 (no component) and 1 (full intensity of the component).

Prior to 4.2 the hexColor return was prefixed with |c now it is just the hex codes for the color.

**Signature:**

```lua
redComponent, greenComponent, blueComponent, hexColor = GetItemQualityColor(quality)
```

**Arguments:**

- `quality` - An numeric item quality (rarity) value (`number`, [itemQuality](../types/itemQuality.md))

**Returns:**

- `redComponent` - Red component of the color (`number`)
- `greenComponent` - Green component of the color (`number`)
- `blueComponent` - Blue component of the color (`number`)
- `hexColor` - Color value of a [`colorString`](../types/colorString.md) for formatting text with the color (`string`)

---

## GetItemSpell

Returns information about the spell cast by an item's "Use:" effect

**Signature:**

```lua
name, rank = GetItemSpell(itemID) or GetItemSpell("itemName") or GetItemSpell("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `name` - Name of the spell (`string`)
- `rank` - Secondary text associated with the spell (often a rank, e.g. "Rank 7"); or the empty string (`""`) if not applicable (`string`)

---

## GetItemStatDelta

Returns a summary of the difference in stat bonuses between two items. Keys in the table returned are the names of global variables containing the localized names of the stats (e.g. `_G["ITEM_MOD_SPIRIT_SHORT"] = "Spirit"`, `_G["ITEM_MOD_HIT_RATING_SHORT"] = "Hit Rating"`).

The optional argument `returnTable` allows for performance optimization in cases where this function is expected to be called repeatedly. Rather than creating new tables each time the function is called (eventually requiring garbage collection), an existing table can be recycled. (Note, however, that this function does not clear the table's contents; use [`wipe()`](Utility.md#wipe) first to guarantee consistent results.)

**Signature:**

```lua
statTable = GetItemStatDelta("item1Link", "item2Link" [, returnTable])
```

**Arguments:**

- `item1Link` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`, [hyperlink](../types/hyperlink.md))
- `item2Link` - Another item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`, [hyperlink](../types/hyperlink.md))
- `returnTable` - Reference to a table to be filled with return values (`table`)

**Returns:**

- `statTable` - A table listing the difference in stat bonuses provided by the items (i.e. if `item1Link` is equipped, what changes to the player's stats would occur if it is replaced by `item2Link`) (`table`)

**Examples:**

```lua
-- links to some early death knight gear for illustrating the example...
local _, ring1Link = GetItemInfo("Valanar's Signet Ring")
local _, ring2Link = GetItemInfo("Keleseth's Signet Ring")

local statDelta = GetItemStatDelta(ring1Link, ring2Link)
for stat, value in pairs(statDelta) do print(value, _G[stat]) end
-- prints (approximately, on enUS client):
--   12 Critical Strike Rating
--   -6 Strength
--   -6 Hit Rating
--   3 Stamina
```

---

## GetItemStats

Returns a summary of an item's stat bonuses. Keys in the table returned are the names of global variables containing the localized names of the stats (e.g. `_G["ITEM_MOD_SPIRIT_SHORT"] = "Spirit"`, `_G["ITEM_MOD_HIT_RATING_SHORT"] = "Hit Rating"`).

The optional argument `returnTable` allows for performance optimization in cases where this function is expected to be called repeatedly. Rather than creating new tables each time the function is called (eventually requiring garbage collection), an existing table can be recycled. (Note, however, that this function does not clear the table's contents; use [`wipe()`](Utility.md#wipe) first to guarantee consistent results.)

**Signature:**

```lua
statTable = GetItemStats("itemLink" [, returnTable])
```

**Arguments:**

- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`, [hyperlink](../types/hyperlink.md))
- `returnTable` - Reference to a table to be filled with return values (`table`)

**Returns:**

- `statTable` - A table listing the stat bonuses provided by the item (`table`)

---

## GetItemUniqueness

Returns information about uniqueness restrictions for equipping an item.

Only applies to items with "Unique Equipped" restrictions upon how many similar items can be equipped -- returns nil for items which for which "Unique" restricts how many the player can have in her possession.

Also returns nil if the queried item is not currently in the WoW client's item cache.

**Signature:**

```lua
uniqueFamily, maxEquipped = GetItemUniqueness(itemID) or GetItemUniqueness("itemName") or GetItemUniqueness("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's link (`string`)

**Returns:**

- `uniqueFamily` - The family of items with special uniqueness restrictions to which the item belongs (`number`)
- `maxEquipped` - The maximum number of items under this restriction that can be equipped (`number`)

**Examples:**

```lua
GetItemUniqueness("Rigid Dragon's Eye")
-- returns 2, 3 if your WoW client has seen this gem
-- up to 3 gems in the Jeweler's Gems family can be equipped at any given time
GetItemUniqueness("Rigid Stormjewel")
-- returns 6, 1 if your WoW client has seen this gem
-- only 1 gem in the Stormjewel family can be equipped at any given time
GetItemUniqueness("Figurine - Ruby Hare")
-- returns -1, 1 if your WoW client has seen this item
-- only 1 Ruby Hare can be equipped at any given time
```

---

## IsConsumableItem

Returns whether an item is consumable. Indicates whether the item is destroyed upon use, not necessarily whether it belongs to the "Consumable" type/class.

**Signature:**

```lua
consumable = IsConsumableItem(itemID) or IsConsumableItem("itemName") or IsConsumableItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `consumable` - 1 if the item is consumable; otherwise nil (`1nil`)

---

## IsCurrentItem

Returns whether an item is being used

**Signature:**

```lua
isItem = IsCurrentItem(itemID) or IsCurrentItem("itemName") or IsCurrentItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `isItem` - 1 if the item's "Use:" action is currently being cast, is waiting for the user to choose a target, or is otherwise in progress; otherwise nil (`1nil`)

---

## IsDressableItem

Returns whether an item's appearance can be previewed using the Dressing Room feature

**Signature:**

```lua
isDressable = IsDressableItem(itemID) or IsDressableItem("itemName") or IsDressableItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `isDressable` - 1 if the item's appearance can be previewed using the Dressing Room feature; otherwise nil (`1nil`)

---

## IsEquippableItem

Returns whether an item can be equipped. Indicates whether an item is capable of being equipped on a character, not necessarily whether the player character is able to wear it.

**Signature:**

```lua
isEquippable = IsEquippableItem(itemID) or IsEquippableItem("itemName") or IsEquippableItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `isEquippable` - 1 if the item can be equipped, otherwise nil (`1nil`)

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

## IsHarmfulItem

Returns whether an item can be used against hostile units. Harmful items include grenades and various quest items ("Use this to zap 30 murlocs!").

**Signature:**

```lua
isHarmful = IsHarmfulItem(itemID) or IsHarmfulItem("itemName") or IsHarmfulItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `isHarmful` - 1 if the item can be used against hostile units; otherwise nil (`1nil`)

---

## IsHelpfulItem

Returns whether an item can be used on the player or friendly units. Helpful items include potions, scrolls, food and drink.

**Signature:**

```lua
isHarmful = IsHelpfulItem(itemID) or IsHelpfulItem("itemName") or IsHelpfulItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `isHarmful` - 1 if the item can be used on the player or friendly units; otherwise nil (`1nil`)

---

## IsItemInRange

Returns whether the player is in range to use an item on a unit

**Signature:**

```lua
inRange = IsItemInRange(itemID, "unit") or IsItemInRange("itemName", "unit") or IsItemInRange("itemLink", "unit")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)
- `unit` - A unit on which to use the item (`string`, [unitID](../types/unitID.md))

**Returns:**

- `inRange` - 1 if the player is near enough to use the item on the unit; 0 if not in range; nil if the unit is not a valid target for the item (`1nil`)

---

## IsUsableItem

Returns whether an item can currently be used. Does not account for item cooldowns (see [`GetItemCooldown()`](Item.md#getitemcooldown) -- returns 1 if other conditions allow for using the item (e.g. if the item can only be used while outdoors).

**Signature:**

```lua
isUsable, notEnoughMana = IsUsableItem(itemID) or IsUsableItem("itemName") or IsUsableItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's link (`string`)

**Returns:**

- `isUsable` - 1 if the item is usable; otherwise nil (`1nil`)
- `notEnoughMana` - 1 if the player lacks the resources (e.g. mana, energy, runes) to use the item; otherwise nil (`1nil`)

---

## ItemHasRange

Returns whether an item has a range limitation for its use. For example, Mistletoe can only be used on another character within a given range of the player, but a Hearthstone has no target and thus no range restriction. Returns nil for items which have a range restriction but are area-targeted and not unit-targeted (e.g. grenades).

**Signature:**

```lua
hasRange = ItemHasRange(itemID) or ItemHasRange("itemName") or ItemHasRange("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `hasRange` - 1 if the item has an effective range; otherwise nil. (`1nil`)

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

## ReplaceEnchant `confirmation`

Confirms replacing an existing enchantment. Usable in response to the [`REPLACE_ENCHANT`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/REPLACE_ENCHANT) event which fires when the player attempts to apply a temporary or permanent enchantment to an item which already has one.

**Signature:**

```lua
ReplaceEnchant()
```

---

## SpellCanTargetItem

Returns whether the spell currently awaiting a target requires an item to be chosen. Only applies when the player has attempted to cast a spell but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
canTarget = SpellCanTargetItem()
```

**Returns:**

- `canTarget` - 1 if the spell can target an item; otherwise nil (`1nil`)

---

## SpellTargetItem `protected`

Casts the spell currently awaiting a target on an item. Usable when the player has attempted to cast a spell (e.g. an Enchanting recipe or the "Use:" effect of a sharpening stone or fishing lure) but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
SpellTargetItem(itemID) or SpellTargetItem("itemName") or SpellTargetItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

---

## UseItemByName `protected`

Uses an arbitrary item (optionally on a specified unit)

**Signature:**

```lua
UseItemByName(itemID [, "target"]) or UseItemByName("itemName" [, "target"]) or UseItemByName("itemLink" [, "target"])
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)
- `target` - A unit on which to use the item, if applicable (`string`, [unitID](../types/unitID.md))

---

← [WoW API Docs](../index.md)
