# Inspect functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#inspect)

---

## CanInspect

Returns whether a unit can be inspected. Returns `nil` if the unit is out of inspect range, if the unit is an NPC, or if the unit is flagged for PvP combat and hostile to the player.

**Signature:**

```lua
canInspect = CanInspect("unit", showError)
```

**Arguments:**

- `unit` - A unit to inspect (`string`, [unitID](../types/unitID.md))
- `showError` - True to fire a [`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md) event (causing the default UI to display an error message) if the unit cannot be inspected; otherwise false (`boolean`)

**Returns:**

- `canInspect` - 1 if the unit can be inspected; otherwise nil (`1nil`)

---

## ClearInspectPlayer

Ends inspection of another character. After this function is called, data about the inspected unit may not be available or valid.

Used in the default UI when the InspectFrame is hidden.

**Signature:**

```lua
ClearInspectPlayer()
```

---

## GetInspectArenaTeamData

Returns arena team information about the currently inspected unit. Only available if data has been downloaded from the server; see [`HasInspectHonorData()`](Inspect.md#hasinspecthonordata) and [`RequestInspectHonorData()`](Inspect.md#requestinspecthonordata-server).

**Signature:**

```lua
teamName, teamSize, teamRating, teamPlayed, teamWins, playerPlayed, playerRating, bg_red, bg_green, bg_blue, emblem, emblem_red, emblem_green, emblem_blue, border, border_red, border_green, border_blue = GetInspectArenaTeamData(team)
```

**Arguments:**

- `team` - Index of one of the unit's arena teams (`number`, [arenaTeamID](../types/arenaTeamID.md))

**Returns:**

- `teamName` - Name of the arena team (`string`)
- `teamSize` - Size of the team (2 for 2v2, 3 for 3v3, or 5 for 5v5) (`number`)
- `teamRating` - The team's current rating (`number`)
- `teamPlayed` - Number of games played by the team in the current week (`number`)
- `teamWins` - Number of games won by the team in the current week (`number`)
- `playerPlayed` - Number of games in which the unit has participated in the current week (`number`)
- `playerRating` - The unit's personal rating with this team (`number`)
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

## GetInspectHonorData

Returns PvP honor information about the currently inspected unit. Only available if data has been downloaded from the server; see [`HasInspectHonorData()`](Inspect.md#hasinspecthonordata) and [`RequestInspectHonorData()`](Inspect.md#requestinspecthonordata-server).

**Signature:**

```lua
todayHK, todayHonor, yesterdayHK, yesterdayHonor, lifetimeHK, lifetimeRank = GetInspectHonorData()
```

**Returns:**

- `todayHK` - Number of honorable kills on the current day (`number`)
- `todayHonor` - Amount of honor points earned on the current day (`number`)
- `yesterdayHK` - Number of honorable kills on the previous day (`number`)
- `yesterdayHonor` - Amount of honor points earned on the previous day (`number`)
- `lifetimeHK` - Lifetime total of honorable kills scored (`number`)
- `lifetimeRank` - Highest rank earned in the pre-2.0 PvP reward system; see [`GetPVPRankInfo()`](PvP.md#getpvprankinfo) for rank display information (`number`)

---

## HasInspectHonorData

Returns whether PvP honor and arena data for the currently inspected unit has been downloaded from the server. See [`RequestInspectHonorData()`](Inspect.md#requestinspecthonordata-server) to request PvP data from the server.

**Signature:**

```lua
hasData = HasInspectHonorData()
```

**Returns:**

- `hasData` - 1 if the client has PvP data for the currently inspected player; otherwise nil (`1nil`)

---

## NotifyInspect `server`

Marks a unit for inspection and requests talent data from the server. Information about the inspected item's equipment can be retrieved immediately using Inventory APIs (e.g. [`GetInventoryItemLink("target",1)`](Hyperlink.md#getinventoryitemlink)). Talent data is not available immediately; the [`INSPECT_READY`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/INSPECT_READY) event fires once the inspected unit's talent information can be retrieved using Talent APIs (e.g. [`GetTalentInfo(1,1,true)`](Talent.md#gettalentinfo)).

**Signature:**

```lua
NotifyInspect("unit")
```

**Arguments:**

- `unit` - A unit to inspect (`string`, [unitID](../types/unitID.md))

---

## RequestInspectHonorData `server`

Requests PvP honor and arena data from the server for the currently inspected unit. Once the [`INSPECT_HONOR_UPDATE`](../events/INSPECT_HONOR_UPDATE.md) event fires, PvP honor and arena information can be retrieved using [`GetInspectHonorData(team)`](Inspect.md#getinspecthonordata) and [`GetInspectArenaTeamData()`](Inspect.md#getinspectarenateamdata).

**Signature:**

```lua
RequestInspectHonorData()
```

---

← [WoW API Docs](../index.md)
