# Auction functions

← [WoW API Docs](../index.md)

**29** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#auction)

---

## CalculateAuctionDeposit

Returns the deposit amount for the item currently being set up for auction. Only returns useful information once an item has been placed in the Create Auction UI's "auction item" slot (see [`ClickAuctionSellItemButton()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ClickAuctionSellItemButton)).

Deposit amount for an auction varies based on the item being auction, the auction's proposed run time, and the auction house being used (i.e. faction or neutral).

**Signature:**

```lua
deposit = CalculateAuctionDeposit(runTime)
```

**Arguments:**

- `runTime` - Run time of the proposed auction (`number`)
  - `720` - 12 hours
  - `1440` - 24 hours
  - `2880` - 48 hours

**Returns:**

- `deposit` - Amount of the deposit (in copper) (`number`)

---

## CanCancelAuction

Returns whether one of the player's auctions can be canceled. Generally, non-cancelable auctions are those which have completed but for which payment has not yet been delivered.

**Signature:**

```lua
canCancel = CanCancelAuction(index)
```

**Arguments:**

- `index` - Index of an auction in the "owner" listing (`number`)

**Returns:**

- `canCancel` - 1 if the auction can be canceled; otherwise nil (`1nil`)

---

## CanSendAuctionQuery

Returns whether the player can perform an auction house query. All auction query types are throttled, preventing abuse of the server by clients sending too many queries in short succession. Normal queries can be sent once every few seconds; mass queries return all results in the auction house instead of one "page" at a time, and can only be sent once every several minutes.

**Signature:**

```lua
canQuery, canMassQuery = CanSendAuctionQuery("list")
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed

**Returns:**

- `canQuery` - 1 if the player can submit an auction query; otherwise nil (`1nil`)
- `canMassQuery` - 1 if the player can submit a mass auction query; otherwise nil (`1nil`)

---

## CancelAuction `confirmation` `hardware`

Cancels an auction created by the player. When canceling an auction, the deposit amount is not refunded.

**Signature:**

```lua
CancelAuction(index)
```

**Arguments:**

- `index` - Index of an auction in the "owner" listing (`number`)

---

## ClickAuctionSellItemButton

Picks up an item from or puts an item into the "Create Auction" slot. If the cursor is empty and the slot contains an item, that item is put onto the cursor. If the cursor contains an item and the slot is empty, the item is placed into the slot. If both the cursor and the slot contain items, the contents of the cursor and the slot are exchanged.

Only has effect if the player is interacting with an auctioneer (i.e. between the [`AUCTION_HOUSE_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_HOUSE_SHOW) and [`AUCTION_HOUSE_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_HOUSE_CLOSED) events). Causes an error message ([`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE)) if the item on the cursor cannot be put up for auction (e.g. if the item is soulbound).

**Signature:**

```lua
ClickAuctionSellItemButton()
```

---

## CloseAuctionHouse

Ends interaction with the Auction House UI. Causes the [`AUCTION_HOUSE_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_HOUSE_CLOSED) event to fire, indicating that Auction-related APIs may be unavailable or no longer return valid data.

**Signature:**

```lua
CloseAuctionHouse()
```

---

## GetAuctionHouseDepositRate `deprecated`

Returns the deposit rate for the current auction house. Obsolete (returns different values for faction and neutral auction houses, but these values do not describe the ratio of auction deposit to an item's vendor buy or sell price); use [`CalculateAuctionDeposit()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/CalculateAuctionDeposit) instead.

**Signature:**

```lua
rate = GetAuctionHouseDepositRate()
```

**Returns:**

- `rate` - The current auction house deposit rate (`number`)

---

## GetAuctionInvTypes

Returns a list of the inventory subtypes for a given auction house item subclass. Inventory types are the second level of hierarchy seen when browsing item classes (categories) and subclasses at the Auction House: `Head`, `Neck`, `Shirt`, et al for `Miscellaneous`; `Head`, `Shoulder`, `Chest`, `Wrist`, et al for `Cloth`; etc.

This function still returns valid information if the player is not interacting with an auctioneer.

**Signature:**

```lua
token, display, ... = GetAuctionInvTypes(classIndex, subClassIndex)
```

**Arguments:**

- `classIndex` - Index of an item class (in the list returned by [`GetAuctionItemClasses()`](https://web.archive.org/web/20110524013705/http://wowprogramming.com/docs/api/GetAuctionItemClasses)); currently, inventory types are only applicable in class `2` (armor) (`number`)
- `subClassIndex` - Index of an item subclass (in the list returned by [`GetAuctionItemSubClasses(classIndex)`](https://web.archive.org/web/20110524013705/http://wowprogramming.com/docs/api/GetAuctionItemSubClasses)); currently, inventory types are only applicable in the armor subclasses listed below: (`number`)
  - `1` - Miscellaneous
  - `2` - Cloth
  - `3` - Leather
  - `4` - Mail
  - `5` - Plate

**Returns:**

- `token` - Name of a global variable containing the localized name of the inventory type (e.g. `INVTYPE_FINGER`) (`string`)
- `display` - 1 if the inventory type should be displayed; otherwise nil (used in the default auction UI to hide subclass/invType combinations that don't exist in the game; e.g. Plate/Back, Leather/Trinket, etc) (`1nil`)
- `...` - Additional `token, display` pairs for each inventory type listed (`list`)

---

## GetAuctionItemClasses

Returns a list of localized item class (category) names. Item classes are the first level of hierarchy seen when browsing at the Auction House: `Weapon`, `Armor`, `Container`, `Consumable`, etc.

This function still returns valid information if the player is not interacting with an auctioneer.

**Signature:**

```lua
... = GetAuctionItemClasses()
```

**Returns:**

- `...` - A list of strings, each the name of an item class (`list`)

---

## GetAuctionItemInfo

Returns information about an auction listing

**Signature:**

```lua
name, texture, count, quality, canUse, level, minBid, minIncrement, buyoutPrice, bidAmount, highestBidder, owner, sold = GetAuctionItemInfo("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `count` - Number of items in the stack (`number`)
- `quality` - The quality (rarity) level of the item (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))
- `canUse` - 1 if the player character can use or equip the item; otherwise nil (`1nil`)
- `level` - Required character level to use or equip the item (`number`)
- `minBid` - Minimum cost to bid on the item (in copper) (`number`)
- `minIncrement` - Minimum bid increment to become the highest bidder on the item (in copper) (`number`)
- `buyoutPrice` - Buyout price of the auction (in copper) (`number`)
- `bidAmount` - Current highest bid on the item (in copper); 0 if no bids have been placed (`number`)
- `highestBidder` - 1 if the player is currently the highest bidder; otherwise nil (`1nil`)
- `owner` - Name of the character who placed the auction (`string`)
- `sold` - 1 if the auction has sold (and payment is awaiting delivery; applies only to `owner` auctions); otherwise nil (`number`)

---

## GetAuctionItemLink

Returns a hyperlink for an item in an auction listing

**Signature:**

```lua
link = GetAuctionItemLink("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetAuctionItemSubClasses

Returns a list of localized subclass names for a given item class. Item subclasses are the second level of hierarchy seen when browsing item classes (categories) at the Auction House: `One-Handed Axes`, `Two-Handed Axes`, `Bows`, `Guns`, et al for `Weapon`; `Cloth`, `Leather`, `Plate`, `Shields`, et al for `Armor`; `Food & Drink`, `Potion`, `Elixir` et al for `Consumable`; `Red`, `Blue`, `Yellow`, et al for `Gem`; etc.

This function still returns valid information if the player is not interacting with an auctioneer.

**Signature:**

```lua
... = GetAuctionItemSubClasses(classIndex)
```

**Arguments:**

- `classIndex` - Index of an item class (in the list returned by [`GetAuctionItemClasses()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemClasses)) (`number`)

**Returns:**

- `...` - A list of strings, each the name of an item subclass; or nil if the class contains no subclasses (`list`)

**Examples:**

```lua
-- prints a list of the subclasses for each item class
function printSubClasses(...)
  for class = 1, select("#", ...) do
    print(select(class, ...).. ":", strjoin(", ", GetAuctionItemSubClasses(class)))
  end
end
printSubClasses(GetAuctionItemClasses())
```

---

## GetAuctionItemTimeLeft

Returns the time remaining before an auction listing expires

**Signature:**

```lua
duration = GetAuctionItemTimeLeft("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)

**Returns:**

- `duration` - General indication of the amount of time remaining on the auction (`number`)
  - `1` - Short (less than 30 minutes)
  - `2` - Medium (30 minutes to 2 hours)
  - `3` - Long (2 hours to 12 hours)
  - `4` - Very Long (more than 12 hours)

---

## GetAuctionSellItemInfo

Returns information about the item currently being set up for auction. Only returns useful information once an item has been placed in the Create Auction UI's "auction item" slot (see [`ClickAuctionSellItemButton()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ClickAuctionSellItemButton)).

**Signature:**

```lua
name, texture, count, quality, canUse, price = GetAuctionSellItemInfo()
```

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `count` - Number of items in the stack (`number`)
- `quality` - Quality (rarity) level of the item (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))
- `canUse` - 1 if the player character can use or equip the item; otherwise nil (`1nil`)
- `price` - Price to sell the item to a vendor (in copper) (`number`)

---

## GetAuctionSort

Returns the current sort settings for auction data. The `index` argument describes priority order for sort criteria: e.g. if `GetAuctionSort("list",1)` returns `quality` and `GetAuctionSort("list",2)` returns `level,1`, items are sorted first by [`itemQuality`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality) and items with the same quality are sorted by required level.

**Signature:**

```lua
criterion, reverse = GetAuctionSort("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of a sorting priority (`number`)

**Returns:**

- `criterion` - Non-localized string naming the criterion (or column in the default UI) by which listings are sorted (`string`)
- `reverse` - 1 if listings are sorted in reverse order; otherwise nil. "Reverse" here is relative to the default order, not to absolute value: e.g. the default order for `quality` is descending (Epic, Rare, Uncommon, etc), but the default order for `level` is ascending (1-80) (`1nil`)

---

## GetBidderAuctionItems `server`

Requests data from the server for the list of auctions bid on by the player. The [`AUCTION_BIDDER_LIST_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_BIDDER_LIST_UPDATE) event fires if new data is available; listing information can then be retrieved using [`GetAuctionItemInfo()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemInfo) or other Auction APIs.

**Signature:**

```lua
GetBidderAuctionItems()
```

---

## GetInboxInvoiceInfo

Returns auction house invoice information for a mail message

**Signature:**

```lua
invoiceType, itemName, playerName, bid, buyout, deposit, consignment, moneyDelay, etaHour, etaMin = GetInboxInvoiceInfo(index)
```

**Arguments:**

- `index` - Index of the mail message in the inbox (between 1 and [`GetInboxNumItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInboxNumItems)) (`number`)

**Returns:**

- `invoiceType` - Type of invoice (`string`)
  - `buyer` - An invoice for an item the player won
  - `seller` - An invoice for an item the player sold
  - `seller_temp_invoice` - A temporary invoice for an item sold by the player but for which payment has not yet been delivered
- `itemName` - Name of the item (`string`)
- `playerName` - Name of the player who bought or sold the item (`string`)
- `bid` - Amount of the winning bid or buyout (`number`)
- `buyout` - Amount of buyout (if the auction was bought out) (`number`)
- `deposit` - Amount of money paid in deposit (`number`)
- `consignment` - Amount withheld from the deposit by the auction house as charge for running the auction (`number`)
- `moneyDelay` - Delay for delivery of payment on a temporary invoice (in minutes; generally 60) (`number`)
- `etaHour` - Hour portion (on a 24-hour clock) of the estimated time for delivery of payment on a temporary invoice (`number`)
- `etaMin` - Minute portion of the estimated time for delivery of payment on a temporary invoice (`number`)

---

## GetNumAuctionItems

Returns the number of auction items in a listing

**Signature:**

```lua
numBatchAuctions, totalAuctions = GetNumAuctionItems("list")
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed

**Returns:**

- `numBatchAuctions` - Number of auctions in the current page of the listing (`number`)
- `totalAuctions` - Total number of auctions available for the listing (`number`)

---

## GetOwnerAuctionItems `server`

Requests data from the server for the list of auctions created by the player. The [`AUCTION_OWNED_LIST_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_OWNED_LIST_UPDATE) event fires if new data is available; listing information can then be retrieved using [`GetAuctionItemInfo()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemInfo) or other Auction APIs.

**Signature:**

```lua
GetOwnerAuctionItems()
```

---

## GetSelectedAuctionItem

Returns the index of the currently selected item in an auction listing. Auction selection is used only for display and internal recordkeeping in the default UI; it has no direct effect on other Auction APIs.

**Signature:**

```lua
index = GetSelectedAuctionItem("list")
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed

**Returns:**

- `index` - Index of the currently selected auction item (`number`)

---

## IsAuctionSortReversed `deprecated`

Returns whether a sort criterion is applied in reverse order. No longer used in the default UI; see [`GetAuctionSort()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionSort) instead.

**Signature:**

```lua
isReversed, isSorted = IsAuctionSortReversed("list", "sort")
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `sort` - A sort criterion (`string`)

**Returns:**

- `isReversed` - 1 if the criterion is applied in reverse order; otherwise nil (`1nil`)
- `isSorted` - 1 if the criterion is currently used for the given listing; otherwise nil (`1nil`)

---

## PlaceAuctionBid `confirmation`

Places a bid on (or buys out) an auction item. Attempting to bid an amount equal to or greater than the auction's buyout price will buy out the auction (spending only the exact buyout price) instead of placing a bid.

**Signature:**

```lua
PlaceAuctionBid("list", index, bid)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)
- `bid` - Amount to bid (in copper) (`number`)

---

## QueryAuctionItems `server`

Requests data from the server for the list of auctions meeting given search criteria. If any search criterion is omitted or `nil`, the search will include all possible values for that criterion.

Search queries are throttled, preventing abuse of the server by clients sending too many queries in short succession. Normal queries can be sent once every few seconds; mass queries return all results in the auction house instead of one "page" at a time, and can only be sent once every several minutes.

Query results are not returned immediately: the [`AUCTION_ITEM_LIST_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_ITEM_LIST_UPDATE) event fires once data is available; listing information can then be retrieved using [`GetAuctionItemInfo()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemInfo) or other Auction APIs.

**Signature:**

```lua
QueryAuctionItems(["name" [, minLevel [, maxLevel [, invTypeIndex [, classIndex [, subClassIndex [, page [, isUsable [, minQuality [, getAll]]]]]]]]]])
```

**Arguments:**

- `name` - Full or partial item name to limit search results; will match any item whose name contains this string (`string`)
- `minLevel` - Minimum required character level of items to limit search results (`number`)
- `maxLevel` - Maximum required character level of items to limit search results (`number`)
- `invTypeIndex` - Index of an item inventory type to limit search results (note that [`GetAuctionInvTypes(classIndex, subClassIndex)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionInvTypes) returns a list of `token, display` pairs for each inventory type; thus, to convert a token index from that list for use here, divide by 2 and round up) (`number`)
- `classIndex` - Index of an item class to limit search results (in the list returned by [`GetAuctionItemClasses()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemClasses)) (`number`)
- `subClassIndex` - Index of an item subclass to limit search results (in the list returned by [`GetAuctionItemSubClasses(classIndex)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemSubClasses)) (`number`)
- `page` - Which "page" of search results to list, if more than `NUM_AUCTION_ITEMS_PER_PAGE` (50) auctions are available; nil to query the first (or only) page (`number`)
- `isUsable` - True to limit search results to only items which can be used or equipped by the player character; otherwise false (`boolean`)
- `minQuality` - Minimum quality (rarity) level of items to limit search results (`itemQuality`)
- `getAll` - True to perform a mass query (returning all listings at once); false to perform a normal query (returning a large number of listings in "pages" of `NUM_AUCTION_ITEMS_PER_PAGE` [50] at a time) (`boolean`)

---

## SetSelectedAuctionItem

Selects an item in an auction listing. Auction selection is used only for display and internal recordkeeping in the default UI; it has no direct effect on other Auction APIs.

**Signature:**

```lua
SetSelectedAuctionItem("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)

---

## SortAuctionApplySort

Applies a set of auction listing sort criteria set via [`SortAuctionSetSort`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SortAuctionSetSort). Sort criteria are applied server-side, affecting not only the order of items within one "page" of listings but the order in which items are collected into pages.

Any currently displayed listings are re-sorted server-side: the [`AUCTION_ITEM_LIST_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_ITEM_LIST_UPDATE), [`AUCTION_BIDDER_LIST_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_BIDDER_LIST_UPDATE), or [`AUCTION_OWNED_LIST_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AUCTION_OWNED_LIST_UPDATE) event fires once the re-sorted data is available to the client; listing information can then be retrieved using [`GetAuctionItemInfo()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetAuctionItemInfo) or other Auction APIs.

**Signature:**

```lua
SortAuctionApplySort("list")
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed

---

## SortAuctionClearSort

Clears any current sorting rules for an auction house listing

**Signature:**

```lua
SortAuctionClearSort("list")
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed

---

## SortAuctionItems `deprecated`

Sorts the auction house listing. No longer used in the default UI; see [`SortAuctionClearSort()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SortAuctionClearSort), [`SortAuctionSetSort()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SortAuctionSetSort), and [`SortAuctionApplySort()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SortAuctionApplySort) instead.

**Signature:**

```lua
SortAuctionItems("type", "sort")
```

**Arguments:**

- `type` - The type of auction listing to sort (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Standard auction house listing
  - `owner` - Auctions the player has placed
- `sort` - Criterion for sorting the list (`string`)
  - `bid` - Amount of the current or minimum bid on the item
  - `buyout` - Buyout price of the item
  - `duration` - Time remaining before the auction expires
  - `level` - Required character level to use or equip the item
  - `minbidbuyout` - Buyout price, or minimum bid if no buyout price is available
  - `name` - Name of the item
  - `quality` - [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality) of the item
  - `quantity` - Number of stacked items in the auction
  - `seller` - Name of the character who created of the auction (or in the `owner` listing, the current high bidder)
  - `status` - Status of the auction (e.g. in the `bidder` listing, whether the player has been outbid)

---

## SortAuctionSetSort

Builds a list of sort criteria for auction listings. Has no effect until [`SortAuctionApplySort(type)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SortAuctionApplySort) is called; thus, this function can be called repeatedly to build a complex set of sort criteria. Sort criteria are applied server-side, affecting not only the order of items within one "page" of listings but the order in which items are collected into pages.

Criteria are applied in the order set by this function; i.e. the last criterion set becomes the primary sort criterion (see example).

**Signature:**

```lua
SortAuctionSetSort("list", "sort", reversed)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `sort` - Criterion to add to the sort (`string`)
  - `bid` - Amount of the current or minimum bid on the item
  - `buyout` - Buyout price of the item
  - `duration` - Time remaining before the auction expires
  - `level` - Required character level to use or equip the item
  - `minbidbuyout` - Buyout price, or minimum bid if no buyout price is available
  - `name` - Name of the item
  - `quality` - [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality) of the item
  - `quantity` - Number of stacked items in the auction
  - `seller` - Name of the character who created of the auction (or in the `owner` listing, the current high bidder)
  - `status` - Status of the auction (e.g. in the `bidder` listing, whether the player has been outbid)
- `reversed` - True to sort in reverse order; otherwise false. "Reverse" here is relative to the default order, not to absolute value: e.g. the default order for `quality` is descending (Epic, Rare, Uncommon, etc), but the default order for `level` is ascending (1-80) (`boolean`)

---

## StartAuction

Creates an auction for the item currently in the "auction item" slot. Has no effect unless an item has been placed in the Create Auction UI's "auction item" slot (see [`ClickAuctionSellItemButton()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ClickAuctionSellItemButton)). With patch 3.3.3 the runTime arg was changed from minutes to an index and the stackSize/numStacks args were added for batch posting.

**Signature:**

```lua
StartAuction(minBid, buyoutPrice, runTime, stackSize, numStacks)
```

**Arguments:**

- `minBid` - Minimum bid for the auction (in copper) (`number`)
- `buyoutPrice` - Buyout price for the auction (in copper) (`number`)
- `runTime` - Run time until the auction expires (an index indicating number of hours) (`number`)
  - `1` - 12 hours
  - `2` - 24 hours
  - `3` - 48 hours
- `stackSize` - Number of items to post in each auction (`number`)
- `numStacks` - Number of auctions (stacks) to post (`number`)

---

← [WoW API Docs](../index.md)
