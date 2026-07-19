# Social functions

← [WoW API Docs](../index.md)

**22** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#social)

---

## AddFriend

Adds a character to the friends list

**Signature:**

```lua
AddFriend("name")
```

**Arguments:**

- `name` - Name of a character to add to the friends list (`string`)

---

## AddIgnore

Adds a character to the ignore list

**Signature:**

```lua
AddIgnore("name")
```

**Arguments:**

- `name` - Name of a character to add to the ignore list (`string`)

---

## AddOrDelIgnore

Adds the named character to the ignore list, or removes the character if already in the ignore list

**Signature:**

```lua
AddOrDelIgnore("fullname")
```

**Arguments:**

- `fullname` - Name of a character to add to or remove from the ignore list (`string`)

---

## AddOrRemoveFriend

Adds the named character to the friends list, or removes the character if already in the friends list

**Signature:**

```lua
AddOrRemoveFriend("name", "note")
```

**Arguments:**

- `name` - Name of a character to add to or remove from the friends list (`string`)
- `note` - Note text to be associated with the friends list entry created (`string`)

---

## DelIgnore

Removes a player from the ignore list

**Signature:**

```lua
DelIgnore("name")
```

**Arguments:**

- `name` - Name of a character to remove from the ignore list (`string`)

---

## GetFriendInfo

Returns information about a character on the player's friends list

**Signature:**

```lua
name, level, class, area, connected, status, note, RAF = GetFriendInfo(index)
```

**Arguments:**

- `index` - Index of a character in the Friends list (between 1 and [`GetNumFriends()`](Social.md#getnumfriends)) (`number`)

**Returns:**

- `name` - Name of the friend (`string`)
- `level` - Character level of the friend, if online; otherwise 0 (`number`)
- `class` - Localized name of the friend's class, if online; otherwise `UNKNOWN` (`string`)
- `area` - Name of the zone in which the friend is located, if online; otherwise `UNKNOWN` (`string`)
- `connected` - 1 if the friend is online; otherwise nil (`1nil`)
- `status` - A label indicating the friend's status (`""` or `""`), or the empty string (`""`) if not applicable (`string`)
- `note` - Note text associated with the friend (`string`)
- `RAF` - 1 if the friend's account is linked to the player's via the Recruit-A-Friend program; otherwise nil (`1nil`)

---

## GetIgnoreName

Returns the name of a character on the ignore list

**Signature:**

```lua
name = GetIgnoreName("index")
```

**Arguments:**

- `index` - Index of an entry in the ignore list (between 1 and [`GetNumIgnores()`](Social.md#getnumignores)) (`string`)

**Returns:**

- `name` - Name of the ignored character (`string`)

---

## GetNumFriends

Returns the number of characters on the player's friends list

**Signature:**

```lua
numFriends = GetNumFriends()
```

**Returns:**

- `numFriends` - Number of characters currently on the friends list (`number`)

---

## GetNumIgnores

Returns the number of characters on the player's ignore list

**Signature:**

```lua
numIgnores = GetNumIgnores()
```

**Returns:**

- `numIgnores` - Number of characters currently on the ignore list (`number`)

---

## GetNumWhoResults

Returns the number of results from a Who system query

**Signature:**

```lua
numResults, totalCount = GetNumWhoResults()
```

**Returns:**

- `numResults` - Number of results returned (`number`)
- `totalCount` - Number of results to display (`number`)

---

## GetSelectedFriend

Returns the index of the selected character in the player's friends list. Selection in the Friends list is used only for display in the default UI and has no effect on other Friends list APIs.

**Signature:**

```lua
index = GetSelectedFriend()
```

**Returns:**

- `index` - Index of the selected character in the Friends list (between 1 and [`GetNumFriends()`](Social.md#getnumfriends)) (`number`)

---

## GetSelectedIgnore

Returns the index of the selected character in the player's ignore list. Selection in the Ignore list is used only for display in the default UI and has no effect on other Ignore list APIs.

**Signature:**

```lua
index = GetSelectedIgnore()
```

**Returns:**

- `index` - Index of the selected character in the Ignore list (between 1 and [`GetNumIgnores()`](Social.md#getnumignores)) (`number`)

---

## GetWhoInfo

Returns information about a character in the Who system query results

**Signature:**

```lua
name, guild, level, race, class, zone, filename = GetWhoInfo(index)
```

**Arguments:**

- `index` - Index of an entry in the Who system query results (between 1 and [`GetNumWhoResults()`](Social.md#getnumwhoresults)) (`number`)

**Returns:**

- `name` - Name of the character (`string`)
- `guild` - Name of the character's guild (`string`)
- `level` - Level of the character (`number`)
- `race` - Localized name of the character's race (`string`)
- `class` - Localized name of the character's class (`string`)
- `zone` - Name of the zone in which the character was located when the query was performed (`string`)
- `filename` - A non-localized token representing the character's class (`string`)

---

## IsIgnored

Returns whether a unit is on the player's ignore list

**Signature:**

```lua
isIgnored = IsIgnored("unit") or IsIgnored("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `isIgnored` - 1 if the unit is on the player's ignore list; otherwise nil (`1nil`)

---

## RemoveFriend

Removes a character from the friends list

**Signature:**

```lua
RemoveFriend("name")
```

**Arguments:**

- `name` - Name of a character to remove from the friends list (`string`)

---

## SendWho `server`

Requests a list of characters meeting given search criteria from the server. Text in the query will match against any of the six searchable fields unless one of the specifiers below is used; multiple specifiers can be used in one query. Queries are case insensitive.

- `n-"name"` - Search for characters whose name contains `name`
- `c-"class"` - Search for characters whose class name contains `class`
- `g-"guild"` - Search for characters in guilds whose name contains `guild`
- `r-"race"` - Search for characters whose race name contains `race`
- `z-"zone"` - Search for characters in zones whose name contains `zone`
- `X` - Search for characters of level `X`
- `X-` - Search for characters of level `X` or higher
- `-X` - Search for characters of level `X` or lower
- `X-Y` - Search for characters between levels `X` and `Y` (inclusive)

Results are not available immediately; the [`CHAT_MSG_SYSTEM`](../events/CHAT_MSG_SYSTEM.md) or [`WHO_LIST_UPDATE`](../events/WHO_LIST_UPDATE.md) event fires when data is available, as determined by the [`SetWhoToUI()`](Social.md#setwhotoui) function.

**Signature:**

```lua
SendWho("filter")
```

**Arguments:**

- `filter` - A Who system search query (cannot be nil; use the empty string `""` to specify a blank query) (`string`)

---

## SetFriendNotes

Sets note text associated with a friends list entry. Setting a note to `nil` will result in an error; to remove a note, set it to the empty string (`""`).

**Signature:**

```lua
SetFriendNotes(index, "note") or SetFriendNotes("name", "note")
```

**Arguments:**

- `index` - Index of a friends list entry (between 1 and [`GetNumFriends()`](Social.md#getnumfriends)) (`number`)
- `name` - Name of friend to modify (`string`)
- `note` - The note to set (`string`)

---

## SetSelectedFriend

Selects a character in the player's friends list. Selection in the Friends list is used only for display in the default UI and has no effect on other Friends list APIs.

**Signature:**

```lua
SetSelectedFriend(index)
```

**Arguments:**

- `index` - Index of a character in the Friends list (between 1 and [`GetNumFriends()`](Social.md#getnumfriends)) (`number`)

---

## SetSelectedIgnore

Selects a character in the player's ignore list. Selection in the Ignore list is used only for display in the default UI and has no effect on other Ignore list APIs.

**Signature:**

```lua
SetSelectedIgnore(index)
```

**Arguments:**

- `index` - Index of a character in the Ignore list (between 1 and [`GetNumIgnores()`](Social.md#getnumignores)) (`number`)

---

## SetWhoToUI

Changes the delivery method for results from [`SendWho()`](Social.md#sendwho-server) queries. In the default UI, results delivered in [`CHAT_MSG_SYSTEM`](../events/CHAT_MSG_SYSTEM.md) are printed in the main chat window; results delivered in a [`WHO_LIST_UPDATE`](../events/WHO_LIST_UPDATE.md) event cause the FriendsFrame to be shown, displaying the results in its "Who" tab.

**Signature:**

```lua
SetWhoToUI(state)
```

**Arguments:**

- `state` - Number identifying a delivery method (`number`)
  - `0` - Send results of three entries or fewer in [`CHAT_MSG_SYSTEM`](../events/CHAT_MSG_SYSTEM.md) events and results of greater than three entries in a [`WHO_LIST_UPDATE`](../events/WHO_LIST_UPDATE.md) event
  - `1` - Send all results in a [`WHO_LIST_UPDATE`](../events/WHO_LIST_UPDATE.md) event

---

## ShowFriends `server`

Requests friends/ignore list information from the server. Information is not returned immediately; the [`FRIENDLIST_UPDATE`](../events/FRIENDLIST_UPDATE.md) event fires when data becomes available for use by Friends/Ignore API functions.

**Signature:**

```lua
ShowFriends()
```

---

## SortWho

Sorts the Who system query results list. Sorting by the same criterion twice will reverse the sort order.

**Signature:**

```lua
SortWho("sortType")
```

**Arguments:**

- `sortType` - Criterion for sorting the list (`string`)
  - `class` - Sort by class name
  - `guild` - Sort by guild name
  - `level` - Sort by player level
  - `name` - Sort by player name
  - `race` - Sort by race name
  - `zone` - Sort by current zone name

---

← [WoW API Docs](../index.md)
