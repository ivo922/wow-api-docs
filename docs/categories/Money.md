# Money functions

← [WoW API Docs](../index.md)

**21** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#money)

---

## AddTradeMoney

Adds the money currently on the cursor to the trade window

**Signature:**

```lua
AddTradeMoney()
```

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

## CursorHasMoney

Returns whether an amount of the player's money is on the cursor. Returns `nil` if the cursor holds guild bank money. See [`GetCursorInfo()`](Cursor.md#getcursorinfo) for more detailed information.

**Signature:**

```lua
hasMoney = CursorHasMoney()
```

**Returns:**

- `hasMoney` - 1 if the cursor is currently holding an amount of the player's money; otherwise nil (`1nil`)

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

## DropCursorMoney

Drops any money currently on the cursor, returning it to where it was taken from

**Signature:**

```lua
DropCursorMoney()
```

---

## GetCoinIcon

Returns an icon representing an amount of money

**Signature:**

```lua
icon = GetCoinIcon(amount)
```

**Arguments:**

- `amount` - Amount of money in copper (`number`)

**Returns:**

- `icon` - Path to an icon texture representing the amount (`string`)
  - `Interface\Icons\INV_Misc_Coin_01` - Small amount of Gold
  - `Interface\Icons\INV_Misc_Coin_02` - Large amount of Gold
  - `Interface\Icons\INV_Misc_Coin_03` - Small amount of Silver
  - `Interface\Icons\INV_Misc_Coin_04` - Large amount of Silver
  - `Interface\Icons\INV_Misc_Coin_05` - Small amount of Copper
  - `Interface\Icons\INV_Misc_Coin_06` - Large amount of Copper

---

## GetCoinText

Returns a localized string describing an amount of money

**Signature:**

```lua
coinText = GetCoinText(amount, "separator")
```

**Arguments:**

- `amount` - Amount of money in copper (`number`)
- `separator` - String to use as separator (', ' is used if nil) (`string`)

**Returns:**

- `coinText` - Text description of the amount using localized names for 'Gold', 'Silver' and 'Copper' (`string`)

**Examples:**

```lua
GetCoinTextureString(10000)
-- returns "1 Gold"

GetCoinTextureString(500050)
-- returns "50 Gold, 50 Copper"

GetCoinTextureString(123456, " / ")
-- returns "12 Gold / 4 Silver / 56 Copper"
```

---

## GetCoinTextureString

Returns a string with embedded coin icons describing an amount of money. As in most places where money amounts are shown in the UI, lesser denominations are only shown when non-zero.

**Signature:**

```lua
coinText = GetCoinTextureString(amount [, fontSize])
```

**Arguments:**

- `amount` - Amount of money in copper (`number`)
- `fontSize` - Size of the money icons. Defaults to 14. (`number`)

**Returns:**

- `coinText` - Text description of the amount using embedded texture codes for gold, silver, and copper coin icons (`string`)

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

## GetMoney

Returns the total amount of money currently in the player's possession

**Signature:**

```lua
money = GetMoney()
```

**Returns:**

- `money` - Amount of money currently in the player's possession (in copper) (`number`)

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

## GetQuestLogRequiredMoney

Returns the amount of money required for the selected quest in the quest log

**Signature:**

```lua
money = GetQuestLogRequiredMoney()
```

**Returns:**

- `money` - The amount of money required to complete the quest (in copper) (`number`)

---

## GetQuestLogRewardMoney

Returns the money reward for the selected quest in the quest log

**Signature:**

```lua
money = GetQuestLogRewardMoney()
```

**Returns:**

- `money` - Amount of money rewarded for completing the quest (in copper) (`number`)

---

## GetSendMailMoney

Returns the amount of money to be sent with the outgoing message. Returns the amount set via [`SetSendMailMoney()`](Mail.md#setsendmailmoney), which in the default UI is only called once its Send button has been clicked (immediately before sending the message). Thus, does not return the Send Money amount set in the default UI's Send Mail window.

**Signature:**

```lua
amount = GetSendMailMoney()
```

**Returns:**

- `amount` - Amount of money to be sent (in copper) (`number`)

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

## PickupGuildBankMoney

Puts money from the guild bank onto the cursor. Money is not actually withdrawn from the guild bank; in the default UI, when the cursor "puts" the money into one of the player's bags, it calls [`WithdrawGuildBankMoney()`](Guild bank.md#withdrawguildbankmoney-confirmation).

**Signature:**

```lua
PickupGuildBankMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to pick up (in copper) (`number`)

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

## PickupTradeMoney

Puts money offered by the player for trade onto the cursor. Money put onto the cursor is subtracted from the amount offered for trade (see [`GetPlayerTradeMoney()`](Money.md#getplayertrademoney)).

**Signature:**

```lua
PickupTradeMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to take from the trade window (in copper) (`number`)

---

## SetSendMailMoney

Sets the amount of money to be sent with the outgoing message. Called in the default UI when clicking its Send button, immediately before sending the mail. Causes an error message if the `amount` plus postage exceeds the player's total money.

**Signature:**

```lua
success = SetSendMailMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to send (in copper) (`number`)

**Returns:**

- `success` - 1 if the player has enough money to send the mail; otherwise nil (`1nil`)

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

## WithdrawGuildBankMoney `confirmation`

Attempts to withdraw money from the guild bank. Causes a [`PLAYER_MONEY`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PLAYER_MONEY) event to fire, indicating the amount withdrawn has been added to the player's total (see [`GetMoney()`](Money.md#getmoney)). Causes an error or system message if `amount` exceeds the amount of money in the guild bank or the player's allowed daily withdrawal amount.

**Signature:**

```lua
WithdrawGuildBankMoney(amount)
```

**Arguments:**

- `amount` - Amount of money to withdraw (in copper) (`number`)

---

← [WoW API Docs](../index.md)
