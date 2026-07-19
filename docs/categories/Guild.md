# Guild functions

← [WoW API Docs](../index.md)

**59** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#guild)

---

## AcceptGuild

Accepts an invitation to join a guild. Usable in response to the [`GUILD_INVITE_REQUEST`](https://web.archive.org/web/20111212162749/http://wowprogramming.com/docs/events/GUILD_INVITE_REQUEST) event, which fires when the player is invited to join a guild.

**Signature:**

```lua
AcceptGuild()
```

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

## CanEditGuildEvent

Returns whether the player is allowed to edit guild-wide calendar events

**Signature:**

```lua
canEdit = CanEditGuildEvent()
```

**Returns:**

- `canEdit` - 1 if the player can create or edit guild calendar events, otherwise nil (`1nil`)

---

## CanEditGuildInfo

Returns whether the player is allowed to edit the guild information text. This text appears when clicking the "Guild Information" button in the default UI's Guild window.

**Signature:**

```lua
canEdit = CanEditGuildInfo()
```

**Returns:**

- `canEdit` - 1 if the player can edit the guild information; otherwise nil (`1nil`)

---

## CanEditMOTD

Returns whether the player is allowed to edit the guild Message of the Day

**Signature:**

```lua
canEdit = CanEditMOTD()
```

**Returns:**

- `canEdit` - 1 if the player can edit the guild MOTD, otherwise nil (`1nil`)

---

## CanEditOfficerNote

Returns whether the player is allowed to edit guild officer notes

**Signature:**

```lua
canEdit = CanEditOfficerNote()
```

**Returns:**

- `canEdit` - 1 if the player can edit officer notes; otherwise nil (`1nil`)

---

## CanEditPublicNote

Returns whether the player is allowed to edit guild public notes

**Signature:**

```lua
canEdit = CanEditPublicNote()
```

**Returns:**

- `canEdit` - 1 if the player can edit public notes, otherwise nil (`1nil`)

---

## CanGuildDemote

Returns whether the player is allowed to demote lower ranked guild members

**Signature:**

```lua
canDemote = CanGuildDemote()
```

**Returns:**

- `canDemote` - 1 if the player can demote lower ranked guild members; otherwise nil (`1nil`)

---

## CanGuildInvite

Returns whether the player is allowed to invite new members to his or her guild

**Signature:**

```lua
canInvite = CanGuildInvite()
```

**Returns:**

- `canInvite` - 1 if the player can invite members to their guild, otherwise nil (`1nil`)

---

## CanGuildPromote

Returns whether the player is allowed to promote other guild members. The player may promote other members only up to the rank below his or her own.

**Signature:**

```lua
canPromote = CanGuildPromote()
```

**Returns:**

- `canPromote` - 1 if the player can promote other guild members; otherwise nil (`1nil`)

---

## CanGuildRemove

Returns whether the player is allowed to remove members from his or her guild. The player may only remove lower ranked members from the guild.

**Signature:**

```lua
canRemove = CanGuildRemove()
```

**Returns:**

- `canRemove` - 1 if the player can remove a member from their guild, otherwise nil (`1nil`)

---

## CanViewOfficerNote

Returns whether the player is allowed to view guild officer notes

**Signature:**

```lua
canView = CanViewOfficerNote()
```

**Returns:**

- `canView` - 1 if the player can view officer notes, otherwise nil (`1nil`)

---

## CloseGuildRegistrar

Ends interaction with a guild registrar. Fires the [`GUILD_REGISTRAR_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_CLOSED) event, indicating that guild registrar APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseGuildRegistrar()
```

---

## CloseGuildRoster `deprecated`

**Signature:**

```lua
CloseGuildRoster()
```

---

## CloseTabardCreation

Ends interaction with the guild tabard creator. Fires the [`CLOSE_TABARD_FRAME`](https://web.archive.org/web/20100106001314/http://wowprogramming.com/docs/events/CLOSE_TABARD_FRAME) event, indicating that tabard creation APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseTabardCreation()
```

---

## DeclineGuild

Declines an offered guild invitation. Usable in response to the [`GUILD_INVITE_REQUEST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_INVITE_REQUEST) event which fires when the player is invited to join a guild.

**Signature:**

```lua
DeclineGuild()
```

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

## GetGuildEventInfo

Returns information about an entry in the guild event log. Only returns valid data after calling [`QueryGuildEventLog()`](Guild.md#queryguildeventlog-server) and the following [`GUILD_EVENT_LOG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_EVENT_LOG_UPDATE) event has fired.

**Signature:**

```lua
type, player1, player2, rank, year, month, day, hour = GetGuildEventInfo(index)
```

**Arguments:**

- `index` - Index of an entry in the guild event log (between 1 and [`GetNumGuildEvents()`](Guild.md#getnumguildevents)) (`number`)

**Returns:**

- `type` - Type of event (example descriptions from the default UI below) (`string`)
  - `demote` - player1 demotes player2 to rank.
  - `invite` - player1 invites player2 to the guild.
  - `join` - player1 joins the guild.
  - `promote` - player1 promotes player2 to rank.
  - `quit` - player1 has quit the guild.
  - `remove` - player1 removes player2 from the guild.
- `player1` - First actor in the event (`string`)
- `player2` - Second actor in the event, if applicable (`string`)
- `rank` - Name of the rank related to promote/demote events (`string`)
- `year` - Number of years since the event occurred (`number`)
- `month` - Number of months since the event occurred (`number`)
- `day` - Number of days since the event occurred (`number`)
- `hour` - Number of hours since the event occurred (`number`)

---

## GetGuildInfo

Returns a unit's guild affiliation

**Signature:**

```lua
guildName, guildRankName, guildRankIndex = GetGuildInfo("unit") or GetGuildInfo("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `guildName` - Name of the character's guild (`string`)
- `guildRankName` - Name of the character's guild rank (`string`)
- `guildRankIndex` - Numeric guild rank of the character (0 = guild leader; higher numbers for lower ranks) (`number`)

---

## GetGuildInfoText

Returns guild information text. Only returns valid data after calling [`GuildRoster()`](Guild.md#guildroster-server) and the following [`GUILD_ROSTER_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_ROSTER_UPDATE) event has fired.

This text appears when clicking the "Guild Information" button in the default UI's Guild window.

**Signature:**

```lua
guildInfoText = GetGuildInfoText()
```

**Returns:**

- `guildInfoText` - The guild information text (including newline characters) (`string`)

---

## GetGuildRosterInfo

**Signature:**

```lua
name, rank, rankIndex, level, class, zone, note, officernote, online, status, classFileName = GetGuildRosterInfo(index)
```

**Arguments:**

- `index` - The player index in the guild roster. (`number`)

**Returns:**

- `name` - The name of the player (`string`)
- `rank` - The rank of the player (`string`)
- `rankIndex` - The rankIndex of the player (`number`)
- `level` - The level of the player (`number`)
- `class` - The (localized) class of the player (`string`)
- `zone` - The last zone in which the player was seen (`string`)
- `note` - The public note of the player (`string`)
- `officernote` - The officer note of the player, if the player has permission to view it (`string`)
- `online` - 1 if the player is online, nil otherwise (`1nil`)
- `status` - The status of the player (`string`)
  - `` - The player is currently away from keyboard.
  - `` - The player does not want to be disturbed.
- `classFileName` - The class filename of the player - unlocalized (`string`)

---

## GetGuildRosterLastOnline

Returns the amount of time since a guild member was last online. Only returns valid data after calling [`GuildRoster()`](Guild.md#guildroster-server) and the following [`GUILD_ROSTER_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_ROSTER_UPDATE) event has fired.

**Signature:**

```lua
years, months, days, hours = GetGuildRosterLastOnline(index)
```

**Arguments:**

- `index` - Index of a member in the guild roster (between 1 and [`GetNumGuildMembers()`](Guild.md#getnumguildmembers)), or 0 for no selection (`number`)

**Returns:**

- `years` - Number of years since the member was last online (`number`)
- `months` - Number of months since the member was last online (`number`)
- `days` - Number of days since the member was last online (`number`)
- `hours` - Number of hours since the member was last online (`number`)

---

## GetGuildRosterMOTD

Returns the Message of the Day for the player's guild

**Signature:**

```lua
guildMOTD = GetGuildRosterMOTD()
```

**Returns:**

- `guildMOTD` - The guild Message of the Day (`string`)

---

## GetGuildRosterSelection

Returns the index of the selected member in the guild roster. Selection in the guild roster is used only for display in the default UI and has no effect on other Guild APIs.

**Signature:**

```lua
index = GetGuildRosterSelection()
```

**Returns:**

- `index` - Index of the selected member in the guild roster (between 1 and [`GetNumGuildMembers()`](Guild.md#getnumguildmembers)), or 0 for no selection (`number`)

---

## GetGuildRosterShowOffline

Returns whether the guild roster lists offline members

**Signature:**

```lua
showOffline = GetGuildRosterShowOffline()
```

**Returns:**

- `showOffline` - 1 if offline members are included in the guild roster listing; otherwise nil (`1nil`)

---

## GetGuildTabardFileNames

Returns the textures that comprise the player's guild tabard. Returns nil if the player is not in a guild.

**Signature:**

```lua
tabardBackgroundUpper, tabardBackgroundLower, tabardEmblemUpper, tabardEmblemLower, tabardBorderUpper, tabardBorderLower = GetGuildTabardFileNames()
```

**Returns:**

- `tabardBackgroundUpper` - Path to the texture for the upper portion of the tabard's background (`string`)
- `tabardBackgroundLower` - Path to the texture for the lower portion of the tabard's background (`string`)
- `tabardEmblemUpper` - Path to the texture for the upper portion of the tabard's emblem (`string`)
- `tabardEmblemLower` - Path to the texture for the lower portion of the tabard's emblem (`string`)
- `tabardBorderUpper` - Path to the texture for the upper portion of the tabard's border (`string`)
- `tabardBorderLower` - Path to the texture for the lower portion of the tabard's border (`string`)

---

## GetNumGuildEvents

Returns the number of entries in the guild event log. Only returns valid data after calling [`QueryGuildEventLog()`](Guild.md#queryguildeventlog-server) and the following [`GUILD_EVENT_LOG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_EVENT_LOG_UPDATE) event has fired.

**Signature:**

```lua
numEvents = GetNumGuildEvents()
```

**Returns:**

- `numEvents` - Number of entries in the guild event log (`number`)

---

## GetNumGuildMembers

Returns the number of members in the guild roster

**Signature:**

```lua
numGuildMembers = GetNumGuildMembers([includeOffline])
```

**Arguments:**

- `includeOffline` - True to count all members in the guild; false or omitted to count only those members currently online (`boolean`)

**Returns:**

- `numGuildMembers` - Number of members in the guild roster (`number`)

---

## GetTabardCreationCost

Returns the cost to create a guild tabard. Only returns valid data if the player is interacting with a tabard designer (i.e. between the [`OPEN_TABARD_FRAME`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/OPEN_TABARD_FRAME) and [`CLOSE_TABARD_FRAME`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CLOSE_TABARD_FRAME) events).

**Signature:**

```lua
cost = GetTabardCreationCost()
```

**Returns:**

- `cost` - The cost of creating a guild tabard, in copper (`number`)

---

## GetTabardInfo `deprecated`

**Signature:**

```lua
GetTabardInfo()
```

---

## GuildControlAddRank

Adds a new rank to the player's guild. The newly added rank becomes the lowest rank in the guild.

**Signature:**

```lua
GuildControlAddRank("name")
```

**Arguments:**

- `name` - Name of the new rank (`string`)

---

## GuildControlDelRank

Deletes a guild rank

**Signature:**

```lua
GuildControlDelRank("name")
```

**Arguments:**

- `name` - Name of the rank to delete (`string`)

---

## GuildControlGetNumRanks

Returns the number of ranks in the guild

**Signature:**

```lua
numRanks = GuildControlGetNumRanks()
```

**Returns:**

- `numRanks` - Number of guild ranks (including Guild Leader) (`number`)

---

## GuildControlGetRankFlags

Returns the list of privileges for the guild rank being edited. The name of a privilege for an index in this list can be found in the global variable `"GUILDCONTROL_OPTION"..index`.

**Signature:**

```lua
... = GuildControlGetRankFlags()
```

**Returns:**

- `...` - A list of privilege flags (1 = privilege allowed, nil = privilege denied) for the rank being edited (`list`)

---

## GuildControlGetRankName

Returns the name of a guild rank

**Signature:**

```lua
rankName = GuildControlGetRankName(rank)
```

**Arguments:**

- `rank` - Index of a rank to edit (between 1 and [`GuildControlGetNumRanks()`](Guild.md#guildcontrolgetnumranks)) (`number`)

**Returns:**

- `rankName` - Name of the guild rank (`string`)

---

## GuildControlSaveRank

Saves changes to the guild rank being edited

**Signature:**

```lua
GuildControlSaveRank("name")
```

**Arguments:**

- `name` - New name for the guild rank (`string`)

---

## GuildControlSetRank

Chooses a guild rank to edit

**Signature:**

```lua
GuildControlSetRank(rank)
```

**Arguments:**

- `rank` - Index of a rank to edit (between 1 and [`GuildControlGetNumRanks()`](Guild.md#guildcontrolgetnumranks)) (`number`)

---

## GuildControlSetRankFlag

Enables or disables a privilege for the guild rank being edited. Changes are not saved until a call is made to [`GuildControlSaveRank()`](Guild.md#guildcontrolsaverank).

**Signature:**

```lua
GuildControlSetRankFlag(index, enabled)
```

**Arguments:**

- `index` - Index of a privilege to change (`number`)
  - `1` - Guildchat listen
  - `2` - Guildchat speak
  - `3` - Officerchat listen
  - `4` - Officerchat speak
  - `5` - Promote
  - `6` - Demote
  - `7` - Invite Member
  - `8` - Remove Member
  - `9` - Set MOTD
  - `10` - Edit Public Notes
  - `11` - View Officer Note
  - `12` - Edit Officer Note
  - `13` - Modify Guild Info
  - `15` - Use guild funds for repairs
  - `16` - Withdraw gold from the guild bank
  - `17` - Create Guild Event
- `enabled` - True to allow the privilege; false to deny (`boolean`)

---

## GuildDemote

Reduces a guild member's rank by one. The player can only demote members whose rank is below the player's own, and only if the player has permission to demote (i.e. if [`CanGuildDemote()`](Guild.md#canguilddemote) returns 1).

**Signature:**

```lua
GuildDemote("name")
```

**Arguments:**

- `name` - Name of a guild member to demote (`string`)

---

## GuildDisband `confirmation`

Disbands the player's guild. Only has effect if the player is the guild leader

**Signature:**

```lua
GuildDisband()
```

---

## GuildInfo `server`

Requests guild information from the server. Fires two [`CHAT_MSG_SYSTEM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_SYSTEM) events, one containing the name of the guild, followed by one containing the date the guild was created and how many players and accounts belong to the guild.

**Signature:**

```lua
GuildInfo()
```

---

## GuildInvite

Invites a character to join the player's guild

**Signature:**

```lua
GuildInvite("name")
```

**Arguments:**

- `name` - Name of a character to invite (`string`)

---

## GuildLeave `confirmation`

Leaves the player's current guild

**Signature:**

```lua
GuildLeave()
```

---

## GuildPromote

Increases a guild member's rank by one. The player can only promote members up to the rank immediately below the player's own, and only if the player has permission to promote (i.e. if [`CanGuildPromote()`](Guild.md#canguildpromote) returns 1).

**Signature:**

```lua
GuildPromote("name")
```

**Arguments:**

- `name` - Name of a guild member to promote (`string`)

---

## GuildRoster `server`

Requests guild roster information from the server. Information is not returned immediately; the [`GUILD_ROSTER_UPDATE`](https://web.archive.org/web/20111212193423/http://wowprogramming.com/docs/events/GUILD_ROSTER_UPDATE) event fires when data is available for retrieval via [`GetGuildRosterInfo()`](Guild.md#getguildrosterinfo) and related functions. Requests are throttled to reduce server load; the server will only respond to a new request approximately 10 seconds after a previous request.

**Signature:**

```lua
GuildRoster()
```

---

## GuildRosterSetOfficerNote

Sets the officer note for a guild member

**Signature:**

```lua
GuildRosterSetOfficerNote(index, "note")
```

**Arguments:**

- `index` - Index of a member in the guild roster (between 1 and [`GetNumGuildMembers()`](Guild.md#getnumguildmembers)), or 0 for no selection (`number`)
- `note` - Note text to set for the guild member (up to 31 characters) (`string`)

---

## GuildRosterSetPublicNote

Sets the public note for a guild member

**Signature:**

```lua
GuildRosterSetPublicNote(index, "note")
```

**Arguments:**

- `index` - Index of a member in the guild roster (between 1 and [`GetNumGuildMembers()`](Guild.md#getnumguildmembers)), or 0 for no selection (`number`)
- `note` - Note text to set for the guild member (up to 31 characters) (`string`)

---

## GuildSetLeader

Promotes a member to guild leader. Only works if the player is the guild leader and the named character is in the guild and currently online.

**Signature:**

```lua
GuildSetLeader("name")
```

**Arguments:**

- `name` - Name of a guild member to promote to leader (`string`)

---

## GuildSetMOTD

Sets the guild Message of the Day. Guild members see the message of the day upon login and whenever it is changed (and cannot disable its display in the default UI), so keeping the message concise is recommended.

**Signature:**

```lua
GuildSetMOTD("message")
```

**Arguments:**

- `message` - New text for the message of the day (up to 128 characters; embedded newlines allowed) (`string`)

**Examples:**

```lua
-- Set a message of the day
GuildSetMOTD("This is a message of the day")

-- Set a two-line message of the day
GuildSetMOTD("Please vote for the following applicants on our forums:\nCladhaire\nCairthas")
```

---

## GuildUninvite

Removes a character from the player's guild

**Signature:**

```lua
GuildUninvite("name")
```

**Arguments:**

- `name` - Name of a guild member to remove (`string`)

---

## IsGuildLeader

Returns whether or player is leader of his or her guild

**Signature:**

```lua
isLeader = IsGuildLeader()
```

**Returns:**

- `isLeader` - 1 if the player is a guild leader; otherwise nil (`1nil`)

---

## IsInGuild

Returns whether the player is in a guild

**Signature:**

```lua
inGuild = IsInGuild()
```

**Returns:**

- `inGuild` - 1 if the player is in a guild; otherwise nil (`1nil`)

---

## QueryGuildEventLog `server`

Requests guild event log information from the server. Fires the [`GUILD_EVENT_LOG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_EVENT_LOG_UPDATE) event when event log information becomes available.

**Signature:**

```lua
QueryGuildEventLog()
```

---

## SetGuildInfoText

Sets the guild information text.. This text appears when clicking the "Guild Information" button in the default UI's Guild window.

**Signature:**

```lua
SetGuildInfoText("text")
```

**Arguments:**

- `text` - New guild information text (`string`)

---

## SetGuildRosterSelection

Selects a member in the guild roster. Selection in the guild roster is used only for display in the default UI and has no effect on other Guild APIs.

**Signature:**

```lua
SetGuildRosterSelection(index)
```

**Arguments:**

- `index` - Index of a member in the guild roster (between 1 and [`GetNumGuildMembers()`](Guild.md#getnumguildmembers)), or 0 for no selection (`number`)

---

## SetGuildRosterShowOffline

Enables or disables inclusion of offline members in the guild roster listing

**Signature:**

```lua
SetGuildRosterShowOffline(showOffline)
```

**Arguments:**

- `showOffline` - True to include offline members in the guild roster listing; false to list only those members currently online (`boolean`)

---

## SortGuildRoster

Sorts the guild roster. Sorting repeatedly by the same criterion will reverse the sort order. Previous sorts are reused when a new criterion is applied: to sort by two criteria, sort first by the secondary criterion and then by the primary criterion.

**Signature:**

```lua
SortGuildRoster("type")
```

**Arguments:**

- `type` - Criterion by which to sort the roster (`string`)
  - `class` - Sort by class name
  - `level` - Sort by character level
  - `name` - Sort by name
  - `note` - Sort by guild note
  - `online` - Sory by last online time
  - `rank` - Sort by guild rank
  - `zone` - Sort by current zone name

---

## TurnInGuildCharter

Turns in a completed guild charter. Usable if the player is interacting with a guild registrar (i.e. between the [`GUILD_REGISTRAR_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_SHOW) and [`GUILD_REGISTRAR_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILD_REGISTRAR_CLOSED) events).

**Signature:**

```lua
TurnInGuildCharter()
```

---

## UnitIsInMyGuild

Returns whether a unit is in the player's guild

**Signature:**

```lua
inGuild = UnitIsInMyGuild("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `inGuild` - 1 if the unit is in the player's guild; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
