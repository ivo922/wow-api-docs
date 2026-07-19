# Petition functions

← [WoW API Docs](../index.md)

**19** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#petition)

---

## BuyGuildCharter

Purchases a guild charter. Usable if the player is interacting with a guild registrar (i.e. between the [`GUILD_REGISTRAR_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_SHOW) and [`GUILD_REGISTRAR_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_CLOSED) events).

**Signature:**

```lua
BuyGuildCharter("guildName")
```

**Arguments:**

- `guildName` - Name of the guild to be created (`string`)

---

## BuyPetition

Purchases an arena team charter

---

## CanSignPetition

Returns whether the player can sign the currently offered petition. Petitions can only be signed once per account, rather than once per character.

**Signature:**

```lua
canSign = CanSignPetition()
```

**Returns:**

- `canSign` - 1 if the player can sign the offered petition; otherwise nil (`1nil`)

---

## ClickPetitionButton `deprecated`

**Signature:**

```lua
ClickPetitionButton()
```

---

## ClosePetition

Ends interaction with a petition. Fires the [`PETITION_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PETITION_CLOSED) event, indicating that Petition APIs may no longer have effects or return valid data.

**Signature:**

```lua
ClosePetition()
```

---

## ClosePetitionVendor

Ends interaction with an arena registrar

---

## GetGuildCharterCost

Returns the cost to purchase a guild charter. Usable if the player is interacting with a guild registrar (i.e. between the [`GUILD_REGISTRAR_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_SHOW) and [`GUILD_REGISTRAR_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_CLOSED) events).

**Signature:**

```lua
cost = GetGuildCharterCost()
```

**Returns:**

- `cost` - Cost to purchase a guild charter (in copper) (`number`)

---

## GetNumPetitionItems `deprecated`

**Signature:**

```lua
GetNumPetitionItems()
```

---

## GetNumPetitionNames

Returns the number of people who have signed the open petition

**Signature:**

```lua
numNames = GetNumPetitionNames()
```

**Returns:**

- `numNames` - Number of characters that have signed the petition (`number`)

---

## GetPetitionInfo

Returns information about the currently open petition

**Signature:**

```lua
petitionType, title, bodyText, maxSignatures, originatorName, isOriginator, minSignatures = GetPetitionInfo()
```

**Returns:**

- `petitionType` - Type of the petition (`string`)
  - `arena` - An arena team charter
  - `guild` - A guild charter
- `title` - Title of the petition (`string`)
- `bodyText` - Body text of the petition (`string`)
- `maxSignatures` - Maximum number of signatures allowed (`number`)
- `originatorName` - Name of the character who initially purchased the charter (`string`)
- `isOriginator` - 1 if the player is the petition's originator; otherwise nil (`1nil`)
- `minSignatures` - Minimum number of signatures required to establish the charter (`number`)

---

## GetPetitionItemInfo

Returns information about a purchasable arena team charter

---

## GetPetitionNameInfo

Returns the name of a character who has signed the currently offered petition

**Signature:**

```lua
name = GetPetitionNameInfo(index)
```

**Arguments:**

- `index` - Index of a signature slot on the petition (between 1 and `minSignatures`, where `minSignatures = select(7,`[`GetPetitionInfo()`](Petition.md#getpetitioninfo)`)`) (`number`)

**Returns:**

- `name` - Name of the signatory character, or nil if the slot has not yet been signed (`string`)

---

## HasFilledPetition

Returns whether the player has a completed petition

---

## OfferPetition

Requests an arena or guild charter signature from the targeted unit

**Signature:**

```lua
OfferPetition()
```

---

## RenamePetition

Renames the guild or arena team to be created by the open petition

**Signature:**

```lua
RenamePetition("name")
```

**Arguments:**

- `name` - New name for the guild or arena team (`string`)

---

## SignPetition

Signs the currently offered petition

**Signature:**

```lua
SignPetition()
```

---

## TurnInArenaPetition

Turns in a petition creating an arena team

---

## TurnInGuildCharter

Turns in a completed guild charter. Usable if the player is interacting with a guild registrar (i.e. between the [`GUILD_REGISTRAR_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_SHOW) and [`GUILD_REGISTRAR_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_CLOSED) events).

**Signature:**

```lua
TurnInGuildCharter()
```

---

## TurnInPetition `deprecated`

**Signature:**

```lua
TurnInPetition()
```

---

← [WoW API Docs](../index.md)
