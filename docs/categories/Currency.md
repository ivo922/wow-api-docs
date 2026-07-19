# Currency functions

← [WoW API Docs](../index.md)

**12** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#currency)

---

## ExpandCurrencyList

Expands or collapses a list header in the Currency UI

**Signature:**

```lua
ExpandCurrencyList(index, shouldExpand)
```

**Arguments:**

- `index` - Index of a header in the currency list (between 1 and GetCurrencyListSize()) (`number`)
- `shouldExpand` - 1 to expand the header, showing its contents; 0 to collapse the header, hiding its contents (`number`)

---

## GetArenaCurrency

Returns the player's amount of arena points

---

## GetBackpackCurrencyInfo

Returns information about a currency marked for watching on the Backpack UI

**Signature:**

```lua
name, count, extraCurrencyType, icon, itemID = GetBackpackCurrencyInfo(index)
```

**Arguments:**

- `index` - Index of a 'slot' for displaying currencies on the backpack (between 1 and `MAX_WATCHED_TOKENS`) (`number`)

**Returns:**

- `name` - Name of the currency type (`string`)
- `count` - Amount of the currency the player has (`number`)
- `extraCurrencyType` - Type of the currency (`number`)
  - `0` - Item-based currency
  - `1` - Arena points
  - `2` - Honor points
- `icon` - Path to an icon texture representing the currency item (for Honor/Arena points, not the icon displayed in the default UI) (`string`)
- `itemID` - ID for the currency item (`number`)

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

## GetCurrencyListInfo

Returns information about a currency type (or headers in the Currency UI)

**Signature:**

```lua
name, isHeader, isExpanded, isUnused, isWatched, count, extraCurrencyType, icon, itemID = GetCurrencyListInfo(index)
```

**Arguments:**

- `index` - Index of a currency type in the currency list (between 1 and [`GetCurrencyListSize()`](Currency.md#getcurrencylistsize)) (`number`)

**Returns:**

- `name` - Name of the currency type or category header (`string`)
- `isHeader` - True if this listing is a category header, false for actual currencies (`boolean`)
- `isExpanded` - True if this listing is a category header whose contents are shown, false for collapsed headers and actual currencies (`boolean`)
- `isUnused` - True if the player has marked this currency as Unused (`boolean`)
- `isWatched` - True if the player has marked this currency to be watched on the backpack UI (`boolean`)
- `count` - Amount of the currency the player has (`number`)
- `extraCurrencyType` - 1 for Arena points, 2 for Honor points, 0 for other currencies (`number`)
- `icon` - Path to a texture representing the currency item (not applicable for Arena/Honor points) (`string`)
- `itemID` - ID for the currency item (`number`)

---

## GetCurrencyListSize

Returns the number of list entries to show in the Currency UI

**Signature:**

```lua
numEntries = GetCurrencyListSize()
```

**Returns:**

- `numEntries` - Number of currency types (including category headers) to be shown in the Currency UI (`number`)

---

## GetHolidayBGHonorCurrencyBonuses

Returns the awarded honor and arena points for a Call to Arms battleground win or loss

**Signature:**

```lua
unk, honorWinReward, arenaWinReward, honorLossReward, arenaLossReward = GetHolidayBGHonorCurrencyBonuses()
```

**Returns:**

- `unk` - Unknown (`boolean`)
- `honorWinReward` - Honor points rewarded for a win (`number`)
- `arenaWinReward` - Arena points rewarded for a win (`number`)
- `honorLossReward` - Honor points rewarded for a loss (`number`)
- `arenaLossReward` - Arena points rewarded for a loss (`number`)

---

## GetHonorCurrency

Returns the player's amount of honor points

**Signature:**

```lua
honorPoints, maxHonor = GetHonorCurrency()
```

**Returns:**

- `honorPoints` - The player's current amount of honor points (`number`)
- `maxHonor` - The maximum amount of honor currency the player can accrue (`number`)

---

## GetMaxArenaCurrency

Returns the maximum amount of arena points the player can accrue

**Signature:**

```lua
amount = GetMaxArenaCurrency()
```

**Returns:**

- `amount` - The maximum amount of arena points the player can accrue (`number`)

---

## SetCurrencyBackpack

Sets a currency type to be watched on the Backpack UI

**Signature:**

```lua
SetCurrencyBackpack(index, watch)
```

**Arguments:**

- `index` - Index of a currency type or header in the currency list (between 1 and GetCurrencyListSize()) (`number`)
- `watch` - 1 to add this currency to the backpack UI; 0 to remove it from being watched (`number`)

---

## SetCurrencyUnused

Moves a currency type to or from the Unused currencies list.

"Unused" currencies behave no differently; the distinction only exists to allow players to hide currencies they don't care about from the main display.

**Signature:**

```lua
SetCurrencyUnused(index, makeUnused)
```

**Arguments:**

- `index` - Index of a currency type or header in the currency list (between 1 and GetCurrencyListSize()) (`number`)
- `makeUnused` - 1 to move this currency to the Unused category; 0 to return it to its original category (`number`)

---

← [WoW API Docs](../index.md)
