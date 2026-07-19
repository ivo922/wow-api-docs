# Merchant functions

← [WoW API Docs](../index.md)

**24** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#merchant)

---

## BuyMerchantItem `confirmation`

Purchases an item available from a vendor

**Signature:**

```lua
BuyMerchantItem(index, quantity)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)
- `quantity` - Number of items to purchase (between 1 and [`GetMerchantItemMaxStack(index)`](Merchant.md#getmerchantitemmaxstack)) (`number`)

---

## BuybackItem

Repurchases an item recently sold to a vendor

**Signature:**

```lua
BuybackItem(index)
```

**Arguments:**

- `index` - Index of an item in the buyback listing (between 1 and [`GetNumBuybackItems()`](Merchant.md#getnumbuybackitems)) (`number`)

---

## CanMerchantRepair

Returns whether the vendor with whom the player is currently interacting can repair equipment

**Signature:**

```lua
canRepair = CanMerchantRepair()
```

**Returns:**

- `canRepair` - 1 if the vendor can repair equipment; otherwise nil (`1nil`)

---

## CloseMerchant

Ends interaction with a vendor. Causes the [`MERCHANT_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MERCHANT_CLOSED) event to fire, indicating that Merchant APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseMerchant()
```

---

## ContainerRefundItemPurchase

Sells an item purchased with alternate currency back to a vendor. Items bought with alternate currency (honor points, arena points, or special items such as Emblems of Heroism and Dalaran Cooking Awards) can be returned to a vendor for a full refund, but only within a limited time after the original purchase.

**Signature:**

```lua
ContainerRefundItemPurchase(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))

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

## GetBuybackItemInfo

Returns information about an item recently sold to a vendor and available to be repurchased

**Signature:**

```lua
name, texture, price, quantity, numAvailable, isUsable = GetBuybackItemInfo(index)
```

**Arguments:**

- `index` - Index of an item in the buyback listing (between 1 and [`GetNumBuybackItems()`](Merchant.md#getnumbuybackitems)) (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `price` - Current cost to repurchase the item from this vendor (in copper) (`number`)
- `quantity` - Number of stacked items per purchase (`number`)
- `numAvailable` - Number of items available for purchase, if the vendor has a limited stock of the item; generally 0 for buyback items (`number`)
- `isUsable` - 1 if the player can use or equip the item; otherwise nil (`1nil`)

---

## GetBuybackItemLink

Returns a hyperlink for an item recently sold to a vendor and available to be repurchased

**Signature:**

```lua
link = GetBuybackItemLink(index)
```

**Arguments:**

- `index` - Index of an item in the buyback listing (between 1 and [`GetNumBuybackItems()`](Merchant.md#getnumbuybackitems)) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](../types/hyperlink.md))

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

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))
- `IsEquipped` - wheather to get an equipped item info (`boolean`)

**Returns:**

- `money` - Amount of copper to be refunded (`number`)
- `itemCount` - Number of different item currencies to be refunded (e.g. the price a PvP mount is in 3 currencies, as it requires multiple battlegrounds' Marks of Honor) (`number`)
- `refundSec` - Seconds remaining until this item is no longer eligible to be returned for a refund (`number`)
- `currecycount` - Amount of currency to be refunded (`number`)
- `hasEnchants` - weather the item is enchanted (`number`)

---

## GetContainerItemPurchaseItem

Returns information about a specific currency refunded for returning an item to vendors. See [`GetContainerItemPurchaseInfo`](Container.md#getcontaineritempurchaseinfo) for more information about alternate currency refunds.

**Signature:**

```lua
texture, quantity, link = GetContainerItemPurchaseItem(container, slot, index)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))
- `index` - Index of the currency type; between 1 and `itemCount`, where `itemCount` is the 4th return from `GetContainerItemPurchaseInfo()` for the same container and slot (`number`)

**Returns:**

- `texture` - Path to an icon texture for the currency item (`string`)
- `quantity` - Quantity of the currency item to be refunded (`number`)
- `link` - Hyperlink for the currency item (`itemLink`)

---

## GetMerchantItemCostInfo

Returns information about alternate currencies required to purchase an item from a vendor

**Signature:**

```lua
currencyCount = GetMerchantItemCostInfo(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

**Returns:**

- `currencyCount` - Number of different currencies required to purchase the item (see [`GetMerchantItemCostItem()`](Merchant.md#getmerchantitemcostitem) for amount of each item currency required) (`number`)

---

## GetMerchantItemCostItem

Returns information about currency items required to purchase an item from a vendor

**Signature:**

```lua
texture, value, link, name = GetMerchantItemCostItem(index, currency)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)
- `currency` - Index of one of the item currencies required to purchase the item (between 1 and [`GetMerchantItemCostInfo(index)`](Merchant.md#getmerchantitemcostinfo)) (`number`)

**Returns:**

- `texture` - Path to an icon texture for the currency item (`string`)
- `value` - Amount of the currency required for purchase (`number`)
- `link` - A hyperlink for the currency item (`string`, [hyperlink](../types/hyperlink.md))
- `name` - The localized name of the currency (`string`)

---

## GetMerchantItemInfo

Returns information about an item available for purchase from a vendor

**Signature:**

```lua
name, texture, price, quantity, numAvailable, isUsable, extendedCost = GetMerchantItemInfo(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `price` - Current cost to purchase the item from this vendor (in copper) (`number`)
- `quantity` - Number of stacked items per purchase (`number`)
- `numAvailable` - Number of items available for purchase, if the vendor has a limited stock of the item; -1 if the vendor has an unlimited supply of the item (`number`)
- `isUsable` - 1 if the player can use or equip the item; otherwise nil (`1nil`)
- `extendedCost` - 1 if the item's price uses one or more alternate currencies (for which details can be found via [`GetMerchantItemCostInfo(index)`](Merchant.md#getmerchantitemcostinfo)); otherwise nil (`1nil`)

---

## GetMerchantItemLink

Returns a hyperlink for an item available for purchase from a vendor

**Signature:**

```lua
link = GetMerchantItemLink(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](../types/hyperlink.md))

---

## GetMerchantItemMaxStack

Returns the maximum number of an item allowed in a single purchase. Determines the largest value usable for the second argument (`quantity`) of [`BuyMerchantItem()`](Merchant.md#buymerchantitem-confirmation) when purchasing the item. For most items, this is the same as the maximum stack size of the item.

**Signature:**

```lua
maxStack = GetMerchantItemMaxStack(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

**Returns:**

- `maxStack` - Largest number of items allowed in a single purchase (`number`)

---

## GetMerchantNumItems

Returns the number of different items available for purchase from a vendor

**Signature:**

```lua
numMerchantItems = GetMerchantNumItems()
```

**Returns:**

- `numMerchantItems` - Number of different items available for purchase (`number`)

---

## GetNumBuybackItems

Returns the number of items recently sold to a vendor and available to be repurchased

**Signature:**

```lua
numBuybackItems = GetNumBuybackItems()
```

**Returns:**

- `numBuybackItems` - Number of items available to be repurchased (`number`)

---

## GetRepairAllCost

Returns the cost to repair all of the player's damaged items. Returns `0, nil` if none of the player's items are damaged. Only returns valid data while interacting with a vendor which allows repairs (i.e. for whom [`CanMerchantRepair()`](Merchant.md#canmerchantrepair) returns `1`).

**Signature:**

```lua
repairAllCost, canRepair = GetRepairAllCost()
```

**Returns:**

- `repairAllCost` - Cost to repair all damaged items (in copper) (`number`)
- `canRepair` - 1 if repairs are currently available; otherwise nil (`1nil`)

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

## PickupMerchantItem

Puts an item available for purchase from a vendor onto the cursor

**Signature:**

```lua
PickupMerchantItem(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](Merchant.md#getmerchantnumitems)) (`number`)

---

## RepairAllItems

Attempts to repair all of the player's damaged items

**Signature:**

```lua
RepairAllItems([useGuildMoney])
```

**Arguments:**

- `useGuildMoney` - 1 to use guild bank money (if available); nil or omitted to use the player's own money (`1nil`)

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

## ShowRepairCursor

Puts the cursor in item repair mode. Unlike most other cursor functions, this functions changes the behavior as well as the appearance of the mouse cursor: while repair mode is active, calling [`PickupContainerItem()`](Container.md#pickupcontaineritem) or [`PickupInventoryItem()`](Cursor.md#pickupinventoryitem) will attempt to repair the item (and deduct the cost of such from the player's savings) instead of putting it on the cursor.

Only has effect while the player is interacting with a vendor which can perform repairs; i.e. between the [`MERCHANT_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MERCHANT_SHOW) and [`MERCHANT_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MERCHANT_CLOSED) events, and only if [`CanMerchantRepair()`](Merchant.md#canmerchantrepair) returns `1`.

**Signature:**

```lua
ShowRepairCursor()
```

---

← [WoW API Docs](../index.md)
