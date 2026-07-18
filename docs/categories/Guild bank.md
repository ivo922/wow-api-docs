# Guild bank functions

← [WoW API Docs](../index.md)

**35** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#guildbank)

---

## AutoStoreGuildBankItem

Withdraws the item(s) from a slot in the guild bank, automatically adding to the player's bags

**Signature:**

```lua
AutoStoreGuildBankItem(tab, slot)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `slot` - Index of an item slot in the guild bank tab (between 1 and `MAX_GUILDBANK_SLOTS_PER_TAB`) (`number`)

---

## BuyGuildBankTab `confirmation`

Purchases the next available guild bank tab

**Signature:**

```lua
BuyGuildBankTab()
```

---

## CanEditGuildTabInfo

Returns whether the player is allowed to edit a guild bank tab's information

**Signature:**

```lua
canEdit = CanEditGuildTabInfo(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

**Returns:**

- `canEdit` - 1 if the player can edit the guild bank tab; otherwise nil (`1nil`)

---

## CanGuildBankRepair

Returns whether the player is allowed to pay for repairs using guild bank funds

**Signature:**

```lua
canRepair = CanGuildBankRepair()
```

**Returns:**

- `canRepair` - 1 if the player can use guild bank funds for repair; otherwise nil (`1nil`)

---

## CanWithdrawGuildBankMoney

Returns whether the player is allowed to withdraw money from the guild bank

**Signature:**

```lua
canWithdraw = CanWithdrawGuildBankMoney()
```

**Returns:**

- `canWithdraw` - 1 if the player can withdraw money from the guild bank; otherwise nil (`1nil`)

---

## CloseGuildBankFrame

Ends interaction with the guild bank vault. Fires the [`GUILDBANKFRAME_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANKFRAME_CLOSED) event, indicating that APIs related to the Guild Bank vault may no longer have effects or return valid data. (APIs related to guild bank permissions are still usable.)

**Signature:**

```lua
CloseGuildBankFrame()
```

---

## DepositGuildBankMoney `confirmation`

Deposits money into the guild bank

**Signature:**

```lua
DepositGuildBankMoney(money)
```

**Arguments:**

- `money` - Amount of money to deposit (in copper) (`number`)

---

## GetCurrentGuildBankTab

Returns the currently selected guild bank tab

**Signature:**

```lua
GetCurrentGuildBankTab(currentTab)
```

**Arguments:**

- `currentTab` - Index of the selected guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

---

## GetGuildBankItemInfo

Returns information about the contents of a guild bank item slot

**Signature:**

```lua
texture, count, locked = GetGuildBankItemInfo(tab, slot)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `slot` - Index of an item slot in the guild bank tab (between 1 and `MAX_GUILDBANK_SLOTS_PER_TAB`) (`number`)

**Returns:**

- `texture` - Path to an icon texture for the item (`string`)
- `count` - Number of stacked items in the slot (`number`)
- `locked` - 1 if the slot is locked (as when a guild member has picked up an item and not yet deposited it elsewhere); otherwise nil (`1nil`)

---

## GetGuildBankItemLink

Returns a hyperlink for an item in the guild bank

**Signature:**

```lua
item = GetGuildBankItemLink(tab, slot)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `slot` - Index of an item slot in the guild bank tab (between 1 and `MAX_GUILDBANK_SLOTS_PER_TAB`) (`number`)

**Returns:**

- `item` - A hyperlink for the contents of the slot (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetGuildBankMoney

Returns the amount of money in the guild bank. The return value is cached and returns the last value seen when not interacting with a guild bank vault. This cache works across characters, and is updated when the [`GUILDBANK_UPDATE_MONEY`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANK_UPDATE_MONEY) or [`GUILDBANKFRAME_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANKFRAME_OPENED) event fires. If no player character has accessed a guild bank since the game client was launched, this function returns 0.

**Signature:**

```lua
guildBankMoney = GetGuildBankMoney()
```

**Returns:**

- `guildBankMoney` - Amount of money in the guild bank (in copper) (`number`)

---

## GetGuildBankMoneyTransaction

Returns information about a transaction in the guild bank money log

**Signature:**

```lua
type, name, year, month, day, hour = GetGuildBankMoneyTransaction(index)
```

**Arguments:**

- `index` - Index of a transaction in the money log (between 1 and [`GetNumGuildBankMoneyTransactions()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankMoneyTransactions)) (`number`)

**Returns:**

- `type` - Type of log event (`string`)
  - `deposit` - Deposit into the guildbank
  - `repair` - Repair cost withdrawal from the guildbank
  - `withdraw` - Withdrawal from the guildbank
- `name` - Name of the guild member responsible for the event, or nil if the name is unknown (`string`)
- `year` - Number of years since the event occurred (`number`)
- `month` - Number of months since the event occurred (`number`)
- `day` - Number of days since the event occurred (`number`)
- `hour` - Number of hours since the event occurred (`number`)

---

## GetGuildBankTabCost

Returns the cost of the next available guild bank tab

**Signature:**

```lua
tabCost = GetGuildBankTabCost()
```

**Returns:**

- `tabCost` - Cost to purchase the next guild bank tab (in copper) (`number`)

---

## GetGuildBankTabInfo

Returns information about a guild bank tab

**Signature:**

```lua
name, icon, isViewable, canDeposit, numWithdrawals, remainingWithdrawals = GetGuildBankTabInfo(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

**Returns:**

- `name` - Name of the tab (`string`)
- `icon` - Path to the icon texture for the tab (`string`)
- `isViewable` - 1 if the player is allowed to view the contents of the tab; otherwise nil (`1nil`)
- `canDeposit` - 1 if the player is allowed to deposit items into the tab; otherwise nil (`1nil`)
- `numWithdrawals` - Maximum number of items (stacks) the player is allowed to withdraw from the tab per day (`number`)
- `remainingWithdrawals` - Maximum number of items (stacks) the player is currently allowed to withdraw from the tab (`number`)

---

## GetGuildBankTabPermissions

Returns information about guild bank tab privileges for the guild rank currently being edited. Used in the default UI's guild control panel.

**Signature:**

```lua
canView, canDeposit, canUpdateText, numWithdrawls = GetGuildBankTabPermissions(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

**Returns:**

- `canView` - 1 if the guild rank has permission to view the tab's contents; otherwise nil. (`1nil`)
- `canDeposit` - 1 if the guild rank has permission to deposit items into the tab; otherwise nil. (`1nil`)
- `canUpdateText` - 1 if the guild rank can update the tab's info text; otherwise nil. (`1nil`)
- `numWithdrawls` - Maximum number of withdrawals per day the guild rank is allowed for the given tab. (`number`)

---

## GetGuildBankText

Returns text associated with a guild bank tab. Only returns valid data after [`QueryGuildBankText()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/QueryGuildBankText) has been called to retrieve the text from the server and the following [`GUILDBANK_UPDATE_TEXT`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANK_UPDATE_TEXT) event has fired.

**Signature:**

```lua
text = GetGuildBankText(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

**Returns:**

- `text` - Info text provided for the tab (`string`)

---

## GetGuildBankTransaction

Returns information about a transaction in the log for a guild bank tab. Only returns valid information following the [`GUILDBANKLOG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANKLOG_UPDATE) event which fires after calling [`QueryGuildBankLog()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/QueryGuildBankLog).

**Signature:**

```lua
type, name, itemLink, count, tab1, tab2, year, month, day, hour = GetGuildBankTransaction(tab, index)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `index` - Index of a log entry (between 1 and [`GetNumGuildBankTransactions(tab)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTransactions)) (`number`)

**Returns:**

- `type` - Type of transaction (`string`)
  - `deposit`
  - `move`
  - `repair`
  - `withdraw`
- `name` - Name of the guild member responsible for the transaction (`string`)
- `itemLink` - A hyperlink for the item involved in the transaction (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))
- `count` - Number of stacked items involved in the transaction (`number`)
- `tab1` - Index of the source tab, if the item was moved between tabs (`number`)
- `tab2` - Index of the destination tab, if the item was moved between tabs (`number`)
- `year` - Number of years since the event occurred (`number`)
- `month` - Number of months since the event occurred (`number`)
- `day` - Number of days since the event occurred (`number`)
- `hour` - Number of hours since the event occurred (`number`)

---

## GetGuildBankWithdrawLimit

Returns the guild bank money withdrawal limit for the guild rank currently being edited

**Signature:**

```lua
goldWithdrawLimit = GetGuildBankWithdrawLimit()
```

**Returns:**

- `goldWithdrawLimit` - Amount of money the guild rank is allowed to withdraw from the guild bank per day (in copper), or -1 if the guild rank has unlimited withdrawal privileges (`number`)

---

## GetGuildBankWithdrawMoney

Returns the amount of money the player is allowed to withdraw from the guild bank per day

**Signature:**

```lua
withdrawLimit = GetGuildBankWithdrawMoney()
```

**Returns:**

- `withdrawLimit` - Amount of money the player is allowed to withdraw from the guild bank per day (in copper), or -1 if the player has unlimited withdrawal privileges (`number`)

---

## GetNumGuildBankMoneyTransactions

Returns the number of transactions in the guild bank money log

**Signature:**

```lua
numTransactions = GetNumGuildBankMoneyTransactions()
```

**Returns:**

- `numTransactions` - Number of transactions in the money log (`number`)

---

## GetNumGuildBankTabs

Returns the number of purchased tabs in the guild bank. Returns valid information even if the player is not interacting with a guild bank vault.

**Signature:**

```lua
numTabs = GetNumGuildBankTabs()
```

**Returns:**

- `numTabs` - Number of active tabs in the guild bank (`number`)

---

## GetNumGuildBankTransactions

Returns the number of entries in a guild bank tab's transaction log. Only returns valid information following the [`GUILDBANKLOG_UPDATE`](https://web.archive.org/web/20111212161357/http://wowprogramming.com/docs/events/GUILDBANKLOG_UPDATE) event which fires after calling [`QueryGuildBankLog()`](https://web.archive.org/web/20111212161357/http://wowprogramming.com/docs/api/QueryGuildBankLog).

**Signature:**

```lua
numTransactions = GetNumGuildBankTransactions(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20111212161357/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

**Returns:**

- `numTransactions` - Number of transactions in the tab's log (`number`)

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

Puts money from the guild bank onto the cursor. Money is not actually withdrawn from the guild bank; in the default UI, when the cursor "puts" the money into one of the player's bags, it calls [`WithdrawGuildBankMoney()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/WithdrawGuildBankMoney).

**Signature:**

```lua
PickupGuildBankMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to pick up (in copper) (`number`)

---

## QueryGuildBankLog `server`

Requests the item transaction log for a guild bank tab from the server. Fires the [`GUILDBANKLOG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANKLOG_UPDATE) event when transaction log information becomes available.

**Signature:**

```lua
QueryGuildBankLog(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

---

## QueryGuildBankTab `server`

Requests information about the contents of a guild bank tab from the server. Fires the [`GUILDBANKBAGSLOTS_CHANGED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANKBAGSLOTS_CHANGED) event when information about the tab's contents becomes available.

**Signature:**

```lua
QueryGuildBankTab(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

---

## QueryGuildBankText `server`

Requests guild bank tab info text from the server. The text is not returned immediately; the [`GUILDBANK_UPDATE_TEXT`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANK_UPDATE_TEXT) event fires when text is available for retrieval by the [`GetGuildBankText()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetGuildBankText) function.

**Signature:**

```lua
QueryGuildBankText(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

---

## SetCurrentGuildBankTab

Selects a tab in the guild bank

**Signature:**

```lua
SetCurrentGuildBankTab(tab)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)

---

## SetGuildBankTabInfo

Sets the name and icon for a guild bank tab

**Signature:**

```lua
SetGuildBankTabInfo(tab, "name", iconIndex)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `name` - New name for the tab (`string`)
- `iconIndex` - Index of an icon for the tab (between 1 and [`GetNumMacroItemIcons()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumMacroItemIcons)) (`number`)

---

## SetGuildBankTabPermissions

Changes guild bank tab permissions for the guild rank being edited

**Signature:**

```lua
SetGuildBankTabPermissions(tab, permission, enabled)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `permission` - Index of a permission to edit (`number`)
  - `1` - View tab
  - `2` - Deposit items
- `enabled` - True to allow permission for the action to the guild rank; false to deny (`boolean`)

---

## SetGuildBankTabWithdraw

Sets the number of item withdrawals allowed per day for the guild rank being edited

---

## SetGuildBankText

Sets the info text for a guild bank tab

**Signature:**

```lua
SetGuildBankText(tab, "text")
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `text` - New info text for the tab (`string`)

---

## SetGuildBankWithdrawLimit

Sets the maximum amount of money withdrawals per day allowed for the guild rank being edited

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

## WithdrawGuildBankMoney `confirmation`

Attempts to withdraw money from the guild bank. Causes a [`PLAYER_MONEY`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PLAYER_MONEY) event to fire, indicating the amount withdrawn has been added to the player's total (see [`GetMoney()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMoney)). Causes an error or system message if `amount` exceeds the amount of money in the guild bank or the player's allowed daily withdrawal amount.

**Signature:**

```lua
WithdrawGuildBankMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to withdraw (in copper) (`number`)

---

← [WoW API Docs](../index.md)
