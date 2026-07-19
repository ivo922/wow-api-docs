# Arena functions

← [WoW API Docs](../index.md)

**29** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#arena)

---

## AcceptArenaTeam

Accepts an invitation to join an arena team

**Signature:**

```lua
AcceptArenaTeam()
```

---

## ArenaTeamDisband

Disbands an arena team. Only has effect if the player is captain of the given team.

**Signature:**

```lua
ArenaTeamDisband(team)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

---

## ArenaTeamInviteByName

Invites a character to one of the player's arena teams

**Signature:**

```lua
ArenaTeamInviteByName(team, "name")
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))
- `name` - Name of a character to invite (`string`)

---

## ArenaTeamLeave `confirmation`

Leaves an arena team

**Signature:**

```lua
ArenaTeamLeave(team)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

---

## ArenaTeamRoster `server`

Requests arena team roster information from the server. Does not return information directly: the [`ARENA_TEAM_ROSTER_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ARENA_TEAM_ROSTER_UPDATE) event fires when information from the server becomes available, which can then be retrieved using [`GetNumArenaTeamMembers()`](Arena.md#getnumarenateammembers) and [`GetArenaTeamRosterInfo()`](Arena.md#getarenateamrosterinfo).

Roster update requests are limited to once every 10 seconds *per team*. For example, calling `ArenaTeamRoster(1)` twice within ten seconds will not result in a second `ARENA_TEAM_ROSTER_UPDATE` event, but calling `ArenaTeamRoster(1)` and `ArenaTeamRoster(2)` within ten seconds will result in two `ARENA_TEAM_ROSTER_UPDATE` events (one for each team).

**Signature:**

```lua
ArenaTeamRoster(team)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

---

## ArenaTeamSetLeaderByName `confirmation`

Promotes an arena team member to team captain. Only has effect if the player is captain of the given team.

**Signature:**

```lua
ArenaTeamSetLeaderByName(team, "name")
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))
- `name` - Name of a team member to promote (`string`)

---

## ArenaTeamUninviteByName `confirmation`

Removes a member from an arena team

**Signature:**

```lua
ArenaTeamUninviteByName(team, "name")
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))
- `name` - Name of a team member to remove (`string`)

---

## ArenaTeam_GetTeamSizeID

Converts an arena team size to the appropriate numeric arena team identifier

**Signature:**

```lua
teamID = ArenaTeam_GetTeamSizeID(teamSize)
```

**Arguments:**

- `teamSize` - The size of the arena team (i.e. 2 for 2v2, 3 for 3v3, etc.) (`number`)

**Returns:**

- `teamID` - The numeric identifier for the arena team of the given size (`number`, [arenaTeamID](../types/arenaTeamID.md))

---

## CloseArenaTeamRoster

Ends interaction with the Arena Team Roster. Called in the default UI when closing the Arena Team Roster frame. After this function is called, roster information functions may no longer return valid data.

**Signature:**

```lua
CloseArenaTeamRoster()
```

---

## DeclineArenaTeam

Declines an arena team invitation

**Signature:**

```lua
DeclineArenaTeam()
```

---

## GetArenaCurrency

Returns the player's amount of arena points

---

## GetArenaTeam

Returns information about one of the player's arena teams

**Signature:**

```lua
teamName, teamSize, teamRating, teamPlayed, teamWins, seasonTeamPlayed, seasonTeamWins, playerPlayed, seasonPlayerPlayed, teamRank, playerRating, bg_red, bg_green, bg_blue, emblem, emblem_red, emblem_green, emblem_blue, border, border_red, border_green, border_blue = GetArenaTeam(team)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

**Returns:**

- `teamName` - Name of the arena team (`string`)
- `teamSize` - Size of the team (2 for 2v2, 3 for 3v3, or 5 for 5v5) (`number`)
- `teamRating` - The team's current rating (`number`)
- `teamPlayed` - Number of games played by the team in the current week (`number`)
- `teamWins` - Number of games won by the team in the current week (`number`)
- `seasonTeamPlayed` - Number of games played by the team in the current arena season (`number`)
- `seasonTeamWins` - Number of games won by the team in the current arena season (`number`)
- `playerPlayed` - Number of games in which the player has participated in the current week (`number`)
- `seasonPlayerPlayed` - Number of games in which the player has participated in the current arena season (`number`)
- `teamRank` - The team's current rank among same-size teams in its battlegroup (`number`)
- `playerRating` - The player's personal rating with this team (`number`)
- `bg_red` - Red component of the color value for the team banner's background (`number`)
- `bg_green` - Green component of the color value for the team banner's background (`number`)
- `bg_blue` - Blue component of the color value for the team banner's background (`number`)
- `emblem` - Index of the team's emblem graphic; full path to the emblem texture can be found using the format `"Interface\PVPFrame\Icons\PVP-Banner-Emblem-"..emblem` (`number`)
- `emblem_red` - Red component of the color value for the team banner's emblem (`number`)
- `emblem_green` - Green component of the color value for the team banner's emblem (`number`)
- `emblem_blue` - Blue component of the color value for the team banner's emblem (`number`)
- `border` - Index of the team's border graphic; full path to the border texture can be found by using the format `"Interface\PVPFrame\PVP-Banner-"..teamSize.."-Border-"..border` (`number`)
- `border_red` - Red component of the color value for the team banner's border (`number`)
- `border_green` - Green component of the color value for the team banner's border (`number`)
- `border_blue` - Blue component of the color value for the team banner's border (`number`)

---

## GetArenaTeamGdfInfo `internal`

This is a Blizzard internal function

---

## GetArenaTeamRosterInfo

Returns information about an arena team member

**Signature:**

```lua
name, rank, level, class, online, played, win, seasonPlayed, seasonWin, rating = GetArenaTeamRosterInfo(team, index)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))
- `index` - Index of a team member (between 1 and [`GetNumArenaTeamMembers(team)`](Arena.md#getnumarenateammembers)) (`number`)

**Returns:**

- `name` - Name of the team member (`string`)
- `rank` - Rank of the member in the team (`number`)
  - `0` - Team captain
  - `1` - Member
- `level` - Character level of the team member (`number`)
- `class` - Localized name of the team member's class (`string`)
- `online` - 1 if the team member is currently online; otherwise nil (`1nil`)
- `played` - Number of games played by the team member in the current week (`number`)
- `win` - Number of winning games played by the team member in the current week (`number`)
- `seasonPlayed` - Number of games played by the team member in the current arena season (`number`)
- `seasonWin` - Number of winning games played by the team member in the current arena season (`number`)
- `rating` - The team member's personal rating with this team (`number`)

---

## GetArenaTeamRosterSelection

Returns the currently selected member in an arena team roster. Selection in the arena team roster currently has no effect beyond highlighting list entry in the default UI.

**Signature:**

```lua
index = GetArenaTeamRosterSelection(team)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

**Returns:**

- `index` - Index of the selected member in the roster listing (`number`)

---

## GetArenaTeamRosterShowOffline `deprecated`

Returns whether arena team roster listings should include offline members. The "Show Offline" filter is not used in the default UI; if disabled, offline members are still shown.

**Signature:**

```lua
showOffline = GetArenaTeamRosterShowOffline()
```

**Returns:**

- `showOffline` - 1 if the show offline filter for arena teams is enabled, otherwise nil (`1nil`)

---

## GetCurrentArenaSeason

Returns a number identifying the current arena season. New arena seasons begin every few months, resetting team rankings and providing new rewards.

**Signature:**

```lua
season = GetCurrentArenaSeason()
```

**Returns:**

- `season` - Number identifying the current arena season (`number`)

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

## GetNumArenaOpponents

Returns the number of enemy players in an arena match

**Signature:**

```lua
numOpponents = GetNumArenaOpponents()
```

**Returns:**

- `numOpponents` - Number of enemy players in an arena match (`number`)

---

## GetNumArenaTeamMembers

Returns the number of members in an arena team

**Signature:**

```lua
numMembers = GetNumArenaTeamMembers(teamindex, showOffline)
```

**Arguments:**

- `teamindex` - The index of the arena team, based on the order they are displayed in the PvP tab. (`number`)
- `showOffline` - True to include currently offline members in the count; otherwise false (`boolean`)

**Returns:**

- `numMembers` - Number of characters on the team (`number`)

---

## GetPreviousArenaSeason

Returns a number identifying the previous arena season. New arena seasons begin every few months, resetting team rankings and providing new rewards.

**Signature:**

```lua
season = GetPreviousArenaSeason()
```

**Returns:**

- `season` - Number identifying the previous arena season (`number`)

---

## IsActiveBattlefieldArena

Returns whether the player is currently in an arena match

**Signature:**

```lua
isArena, isRegistered = IsActiveBattlefieldArena()
```

**Returns:**

- `isArena` - 1 if player is in an Arena match; otherwise nil (`1nil`)
- `isRegistered` - 1 if the current arena match is a ranked match; otherwise nil (`1nil`)

---

## IsArenaTeamCaptain

Returns whether the player is the captain of an arena team. Also returns 1 if the player is not on a team of the given `arenaTeamID`.

**Signature:**

```lua
isCaptain = IsArenaTeamCaptain(team)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

**Returns:**

- `isCaptain` - 1 if the player is the captain of the given team; otherwise nil. (`1nil`)

---

## IsBattlefieldArena

Returns whether the player is interacting with an entity that allows queueing for arena matches

---

## IsInArenaTeam

Returns whether the player is on an arena team

**Signature:**

```lua
isInTeam = IsInArenaTeam()
```

**Returns:**

- `isInTeam` - True if the player is on any arena teams; false otherwise (`boolean`)

---

## SetArenaTeamRosterSelection

Selects a member in an arena team roster. Selection in the arena team roster currently has no effect beyond highlighting list entry in the default UI.

**Signature:**

```lua
SetArenaTeamRosterSelection(team, index)
```

**Arguments:**

- `team` - Index of one of the player's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))
- `index` - Index of a team member to select (between 1 and [`GetNumArenaTeamMembers(team)`](Arena.md#getnumarenateammembers)) (`number`)

---

## SetArenaTeamRosterShowOffline `deprecated`

Enables or disables the inclusion of offline members in arena team roster listings. The "Show Offline" filter is not used in the default UI; if disabled, offline members are still shown.

**Signature:**

```lua
SetArenaTeamRosterShowOffline(enable)
```

**Arguments:**

- `enable` - True to enable display of offline members; false to disable (`boolean`)

---

## SortArenaTeamRoster

Sorts the selected arena team's roster. Affects the ordering of member information returned by [`GetArenaTeamRosterInfo`](Arena.md#getarenateamrosterinfo). Sorting by the same criterion repeatedly reverses the sort order.

**Signature:**

```lua
SortArenaTeamRoster("sortType")
```

**Arguments:**

- `sortType` - Criterion for sorting the roster (`string`)
  - `class` - Sort by class
  - `name` - Sort by name
  - `played` - Sort by number of games played in the current week
  - `rating` - Sort by personal rating
  - `seasonplayed` - Sort by number of games played in the current arena season
  - `seasonwon` - Sort by number of games won in the current arena season
  - `won` - Sort by number of games won in the current week

---

## TurnInArenaPetition

Turns in a petition creating an arena team

---

← [WoW API Docs](../index.md)
