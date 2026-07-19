# Battle.net functions

← [WoW API Docs](../index.md)

**12** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#bnet)

---

## BNGetFriendInfo

Returns information about a RealID friend by index

**Signature:**

```lua
presenceID, givenName, surname, toonName, toonID, client, isOnline, lastOnline, isAFK, isDND, messageText, noteText, isFriend, unknown = BNGetFriendInfo(friendIndex)
```

**Arguments:**

- `friendIndex` - Index (between 1 and [`BNGetNumFriends()`](Battle.net.md#bngetnumfriends)) (`number`)

**Returns:**

- `presenceID` - auto incrementing ID, reset at each login. Persists across reload of UI, but not change of character (`number`)
- `givenName` - First name of the friend, as a new form of chatlink. Visually looks like a string, but only when rendered (`|K string`, [Kstring](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#Kstring))
- `surname` - Last name (surname) of the friend, as a new form of chatlink. Visually looks like a string, but only when rendered (`|K string`, [Kstring](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#Kstring))
- `toonName` - Name of the active character tied to the BNet account (`string`)
- `toonID` - (`number`)
- `client` - The name of the game the friend is currently playing, if any; Returns nil if not online. Returns initialism for World of Warcraft ('WoW') (`string`)
- `isOnline` - Online status (`boolean`)
- `lastOnline` - (`number`)
- `isAFK` - (`boolean`)
- `isDND` - (`boolean`)
- `messageText` - RealID broadcast message displayed below the user on your friends list (`string`)
- `noteText` - The player's personal note for the friend; nil for no note (`string`)
- `isFriend` - (`boolean`)
- `unknown` - (`number`)

---

## BNGetFriendInfoByID

Returns information about a RealID friend

**Signature:**

```lua
presenceID, givenName, surname, toonName, toonID, client, isOnline, lastOnline, isAFK, isDND, messageText, noteText, isFriend, unknown = BNGetFriendInfoByID(presenceID)
```

**Arguments:**

- `presenceID` - (`number`, [presenceID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#presenceID))

**Returns:**

- `presenceID` - (`number`, [presenceID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#presenceID))
- `givenName` - First name of the friend (`|K string`, [Kstring](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#Kstring))
- `surname` - Last name (surname) of the friend (`|K string`, [Kstring](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#Kstring))
- `toonName` - Name of the active character tied to the BNet account (`string`)
- `toonID` - (`number`)
- `client` - The name of the game the friend is currently playing, if any; Returns nil if not online. Returns initialism for World of Warcraft ('WoW') (`string`)
- `isOnline` - Online status (`boolean`)
- `lastOnline` - (`number`)
- `isAFK` - (`boolean`)
- `isDND` - (`boolean`)
- `messageText` - RealID broadcast message displayed below the user on your friends list (`string`)
- `noteText` - The player's personal note for the friend; nil for no note (`string`)
- `isFriend` - (`boolean`)
- `unknown` - (`number`)

---

## BNGetFriendToonInfo

Returns information about a particular online toon tied to a RealID friend

**Signature:**

```lua
unknown, toonName, client, realmName, faction, race, class, unknown, zoneName, level, gameText, broadcastText, broadcastTime = BNGetFriendToonInfo(friendIndex, toonIndex)
```

**Arguments:**

- `friendIndex` - Index (between 1 and [`BNGetNumFriends()`](Battle.net.md#bngetnumfriends)) (`number`)
- `toonIndex` - Index (between 1 and [`BNGetNumFriendToons(friendIndex)`](Battle.net.md#bngetnumfriendtoons)) (`number`)

**Returns:**

- `unknown` - (`boolean`)
- `toonName` - The toon's name (`string`)
- `client` - The name of the game the friend is currently playing, if any; Returns initialism for World of Warcraft ('WoW') (`string`)
- `realmName` - The toon's realm name (`string`)
- `faction` - The toon's faction. Returns -1 for offline, 0 for Horde, 1 for Alliance (`number`)
- `race` - The toon's race (`string`)
- `class` - The toon's class (`string`)
- `unknown` - (`string`)
- `zoneName` - The toon's zone (location) (`string`)
- `level` - The toon's character level (`string`)
- `gameText` - The zone and server of the active toon separated by a hyphen (`string`)
- `broadcastText` - The user's RealID broadcast message (`string`)
- `broadcastTime` - The time the broadcast message was first set (`string`)

---

## BNGetInfo

Returns information about the player's RealID settings

**Signature:**

```lua
unknown, unknown, broadcastText, bnetAFK, bnetDND = BNGetInfo()
```

**Returns:**

- `unknown` - (`number`)
- `unknown` - (`number`)
- `broadcastText` - The player's current broadcast message (entered at the top of the friends tab) (`string`)
- `bnetAFK` - (`boolean`)
- `bnetDND` - (`boolean`)

---

## BNGetMatureLanguageFilter

Returns boolean for the Mature Language Filter option's state.

**Signature:**

```lua
isEnabled = BNGetMatureLanguageFilter()
```

**Returns:**

- `isEnabled` - Returns true if the Mature Language Filter interface option is enabled, otherwise false. (`boolean`)

---

## BNGetNumFriendToons

Returns the number of online toons for a friend

**Signature:**

```lua
numToons = BNGetNumFriendToons(friendIndex)
```

**Arguments:**

- `friendIndex` - The index of the friend to query (`number`)

**Returns:**

- `numToons` - The number of toons (`number`)

---

## BNGetNumFriends

Returns total number of RealID friends and currently online number of RealID friends

**Signature:**

```lua
totalBNet, numBNetOnline = BNGetNumFriends()
```

**Returns:**

- `totalBNet` - Total number of RealID friends (`number`)
- `numBNetOnline` - Number of currently online RealID friends (`number`)

---

## BNGetSelectedFriend

Returns the index of the selected user on your friend's list

**Signature:**

```lua
friendIndex = BNGetSelectedFriend()
```

**Returns:**

- `friendIndex` - The index of the friend in the list (`number`)

---

## BNGetToonInfo

Returns information about the active toon tied to a RealID friend

**Signature:**

```lua
unknown, toonName, client, realmName, realmID, faction, race, class, unknown, zoneName, level, gameText, broadcastText, broadcastTime = BNGetToonInfo(presenceID)
```

**Arguments:**

- `presenceID` - (`number`)

**Returns:**

- `unknown` - (`boolean`)
- `toonName` - The toon's name (`string`)
- `client` - The name of the game the friend is currently playing, if any; Returns initialism for World of Warcraft ('WoW') (`string`)
- `realmName` - The toon's realm name (`string`)
- `realmID` - The toon's realm ID (not sure if unique per realm, or a weekly/session realmID identifier) (`number`)
- `faction` - The toon's faction. Returns -1 for offline, 0 for Horde, 1 for Alliance (`number`)
- `race` - The toon's race (`string`)
- `class` - The toon's class (`string`)
- `unknown` - (`string`)
- `zoneName` - The toon's zone (location) (`string`)
- `level` - The toon's character level (`string`)
- `gameText` - The zone and server of the active toon separated by a hyphen (`string`)
- `broadcastText` - The user's RealID broadcast message (`string`)
- `broadcastTime` - The time the broadcast message was first set (`string`)

---

## BNSetCustomMessage

Sets the player's current RealID broadcast message.

**Signature:**

```lua
BNSetCustomMessage("broadcastText")
```

**Arguments:**

- `broadcastText` - Value that becomes your new broadcast message (`string`)

---

## BNSetFriendNote

Changes the private note for a RealID friend

**Signature:**

```lua
BNSetFriendNote(presenceID, "note")
```

**Arguments:**

- `presenceID` - The presenceID of the friend whose note you want to change (`number`)
- `note` - The new note for the friend (`string`)

---

## BNSetMatureLanguageFilter

Sets the Mature Language Filter option

**Signature:**

```lua
BNSetMatureLanguageFilter(enabled)
```

**Arguments:**

- `enabled` - true to enable the Mature Language Filter; otherwise false (`boolean`)

---

← [WoW API Docs](../index.md)
