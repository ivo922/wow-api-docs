# Trade functions

← [WoW API Docs](../index.md)

**18** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#trade)

---

## AcceptTrade

**Signature:**

```lua
AcceptTrade() This function needs to be reviewed
```

---

## AddTradeMoney

Adds the money currently on the cursor to the trade window

**Signature:**

```lua
AddTradeMoney()
```

---

## BeginTrade `deprecated`

This function is deprecated and should no longer be used

---

## CancelTrade

Cancels a trade in progress. Can be used if either party has accepted the trade, but not once both have.

**Signature:**

```lua
CancelTrade()
```

---

## CancelTradeAccept

Cancels the player's acceptance of a trade. If the player has accepted the trade but the target has not, reverts the player to the pre-acceptance state but does not end the trade.

**Signature:**

```lua
CancelTradeAccept()
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

## CloseTrade

Ends interaction with the Trade UI, canceling any trade in progress. Causes the [`TRADE_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TRADE_CLOSED) event to fire, indicating that Trade APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseTrade()
```

---

## GetPlayerTradeMoney

Returns the amount of money offered for trade by the player

**Signature:**

```lua
amount = GetPlayerTradeMoney()
```

**Returns:**

- `amount` - Amount of money offered for trade by the player (in copper) (`number`)

---

## GetTargetTradeMoney

Returns the amount of money offered for trade by the target

**Signature:**

```lua
amount = GetTargetTradeMoney()
```

**Returns:**

- `amount` - Amount of money offered for trade by the target (in copper) (`number`)

---

## GetTradePlayerItemInfo

Returns information about an item offered for trade by the player

**Signature:**

```lua
name, texture, numItems, quality, isUsable, enchantment = GetTradePlayerItemInfo(index)
```

**Arguments:**

- `index` - Index of an item slot on the player's side of the trade window (between 1 and `MAX_TRADE_ITEMS`) (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `numItems` - Number of stacked items in the slot (`number`)
- `quality` - Quality (rarity) level of the item (`number`, [itemQuality](../types/itemQuality.md))
- `isUsable` - 1 if the player character can use or equip the item; otherwise nil (`1nil`)
- `enchantment` - Name of the enchantment being applied to the item through trade; otherwise nil (`string`)

---

## GetTradePlayerItemLink

Returns a hyperlink for an item offered for trade by the player

**Signature:**

```lua
link = GetTradePlayerItemLink(index)
```

**Arguments:**

- `index` - Index of an item offered for trade by the player (between 1 and `MAX_TRADE_ITEMS`) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](../types/hyperlink.md))

---

## GetTradeTargetItemInfo

Returns information about an item offered for trade by the target

**Signature:**

```lua
name, texture, numItems, quality, isUsable, enchantment = GetTradeTargetItemInfo(index)
```

**Arguments:**

- `index` - Index of an item slot on the player's side of the trade window (between 1 and `MAX_TRADE_ITEMS`) (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `numItems` - Number of stacked items in the slot (`number`)
- `quality` - Quality (rarity) level of the item (`number`, [itemQuality](../types/itemQuality.md))
- `isUsable` - 1 if the player character can use or equip the item; otherwise nil (`1nil`)
- `enchantment` - Name of the enchantment being applied to the item through trade; otherwise nil (`string`)

---

## GetTradeTargetItemLink

Returns a hyperlink for an item offered for trade by the target

**Signature:**

```lua
link = GetTradeTargetItemLink(index)
```

**Arguments:**

- `index` - Index of an item offered for trade by the target (between 1 and `MAX_TRADE_ITEMS`) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](../types/hyperlink.md))

---

## InitiateTrade

Offers to trade with a given unit. The trade process does not begin immediately; once the server has determined both clients can trade, the [`TRADE_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/event/TRADE_SHOW) event fires.

**Signature:**

```lua
InitiateTrade("unit") or InitiateTrade("name")
```

**Arguments:**

- `unit` - A unit with which to trade (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit with which to trade; only valid for nearby units in the player's party/raid (`string`)

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

## ReplaceTradeEnchant `confirmation`

Confirms replacement of an existing enchantment when offering an enchantment for trade. After confirming, the enchantment is not actually performed until both parties accept the trade.

**Signature:**

```lua
ReplaceTradeEnchant()
```

---

## SetTradeMoney

Offers an amount of money for trade

**Signature:**

```lua
SetTradeMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to offer for trade (in copper) (`number`)

---

← [WoW API Docs](../index.md)
