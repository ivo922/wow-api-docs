# Battlefield functions

← [WoW API Docs](../index.md)

**51** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#battlefield)

---

## AcceptAreaSpiritHeal

Accepts the next upcoming periodic resurrection from a battleground spirit healer. Automatically called in the default UI in response to the [`AREA_SPIRIT_HEALER_IN_RANGE`](https://web.archive.org/web/20111212170856/http://wowprogramming.com/docs/events/AREA_SPIRIT_HEALER_IN_RANGE) event which fires when the player's ghost is near a battleground spirit healer.

**Signature:**

```lua
AcceptAreaSpiritHeal()
```

---

## AcceptBattlefieldPort `hardware`

Accepts the offered teleport to a battleground/arena or leaves the battleground/arena or queue. This function requires a hardware event when used to accept a teleport; it can be called without a hardware event for leaving a battleground/arena or its queue.

**Signature:**

```lua
AcceptBattlefieldPort(index, accept)
```

**Arguments:**

- `index` - Index of a battleground or arena type for which the player is queued (`number`)
- `accept` - `1` to accept the offered teleport; `nil` to exit the queue or leave the battleground/arena match in progress (`1nil`)

---

## CanJoinBattlefieldAsGroup

Returns whether the battleground for which the player is queueing supports joining as a group

**Signature:**

```lua
canGroupJoin = CanJoinBattlefieldAsGroup()
```

**Returns:**

- `canGroupJoin` - 1 if the currently displayed battlefield supports joining as a group (`1nil`)

---

## CancelAreaSpiritHeal

Declines the next upcoming periodic resurrection from a battleground spirit healer. Usable in response to the [`AREA_SPIRIT_HEALER_IN_RANGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/AREA_SPIRIT_HEALER_IN_RANGE) event which fires when the player's ghost is near a battleground spirit healer.

**Signature:**

```lua
CancelAreaSpiritHeal()
```

---

## CloseBattlefield

Ends interaction with the battleground queueing UI. Causes the [`BATTLEFIELDS_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/BATTLEFIELDS_CLOSED) event to fire, indicating that Battlefield queueing-related APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseBattlefield()
```

---

## GetAreaSpiritHealerTime

Returns the time remaining until a nearby battleground spirit healer resurrects all players in its area

**Signature:**

```lua
timeleft = GetAreaSpiritHealerTime()
```

**Returns:**

- `timeleft` - Seconds remaining before the next area resurrection (`number`)

---

## GetBattlefieldArenaFaction `deprecated`

This function is deprecated and should no longer be used

---

## GetBattlefieldEstimatedWaitTime

Returns the estimated wait time on a battleground or arena queue

**Signature:**

```lua
waitTime = GetBattlefieldEstimatedWaitTime(index)
```

**Arguments:**

- `index` - Index of a battleground/arena queue the player has joined (between 1 and `MAX_BATTLEFIELD_QUEUES`) (`number`)

**Returns:**

- `waitTime` - Estimated wait time to join the battleground/arena (in milliseconds) (`number`)

---

## GetBattlefieldFlagPosition

Returns the position of a flag in a battleground

**Signature:**

```lua
flagX, flagY, flagToken = GetBattlefieldFlagPosition(index)
```

**Arguments:**

- `index` - Index of a flag (between 1 and [`GetNumBattlefieldFlagPositions()`](Battlefield.md#getnumbattlefieldflagpositions)) (`number`)

**Returns:**

- `flagX` - Horizontal (X) coordinate of the flag's position relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `flagY` - Vertical (Y) coordinate of the flag's position relative to the zone map (0 = bottom edge, 1 = top edge) (`number`)
- `flagToken` - Unique portion of the path to a texure for the flag; preface with `"Interface\\WorldStateFrame\"` for the full path (`string`)

---

## GetBattlefieldInfo

Returns information about a battleground for which the player can queue

---

## GetBattlefieldInstanceExpiration

Returns the amount of time remaining before all players are removed from the instance, if in a battleground instance where the match has completed

**Signature:**

```lua
timeLeft = GetBattlefieldInstanceExpiration()
```

**Returns:**

- `timeLeft` - Amount of time remaining (in milliseconds) before all players are removed from the instance, if in a battleground instance where the match has completed; otherwise 0. (`number`)

---

## GetBattlefieldInstanceInfo

Returns a numeric ID for a battleground instance in the battleground queueing list. This number is seen in the instance names in said listings and elsewhere in the Battlegrounds UI (e.g. the 13 in "You are eligible to enter Warsong Gulch 13").

**Signature:**

```lua
instanceID = GetBattlefieldInstanceInfo(index)
```

**Arguments:**

- `index` - Index in the battleground queue listing (1 for the first available instance, or between 2 and [`GetNumBattlefields()`](Battlefield.md#getnumbattlefields) for other instances) (`number`)

**Returns:**

- `instanceID` - Numeric ID of the battleground instance (`number`)

---

## GetBattlefieldInstanceRunTime

Returns the amount of time since the current battleground instance opened

**Signature:**

```lua
time = GetBattlefieldInstanceRunTime()
```

**Returns:**

- `time` - Amount of time since the current battleground instance opened (in milliseconds) (`number`)

---

## GetBattlefieldMapIconScale

Returns the scale to be used for displaying battleground map icons. Used in the default UI to determine the size of the point of interest icons (towers, graveyards, etc.) on the zone map (the small battle minimap). The default size of the icons is set by `DEFAULT_POI_ICON_SIZE` and the scale is used to grow or shrink them depending on the size of the map.

**Signature:**

```lua
scale = GetBattlefieldMapIconScale()
```

**Returns:**

- `scale` - Scale factor for map icons (between 0 and 1) (`number`)

---

## GetBattlefieldPortExpiration

Returns the time left on a battleground or arena invitation

**Signature:**

```lua
expiration = GetBattlefieldPortExpiration(index)
```

**Arguments:**

- `index` - Index of a battleground/arena queue the player has joined (between 1 and `MAX_BATTLEFIELD_QUEUES`) (`number`)

**Returns:**

- `expiration` - Time remaining before the player's invitation to enter the battleground/arena expires (in seconds); 0 if the player has not yet been invited to enter or is already in the battleground/arena instance (`number`)

---

## GetBattlefieldPosition

Returns the position of a battleground team member not in the player's group. Still used in the default UI but no longer useful; as all team members in a battleground match are automatically joined into a raid group. See [`GetPlayerMapPosition()`](Map.md#getplayermapposition) instead.

**Signature:**

```lua
unitX, unitY, name = GetBattlefieldPosition(index)
```

**Arguments:**

- `index` - Index of a team member (between 1 and [`GetNumBattlefieldPositions()`](Battlefield.md#getnumbattlefieldpositions)) (`number`)

**Returns:**

- `unitX` - Horizontal (X) coordinate of the unit's position relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `unitY` - Vertical (Y) coordinate of the unit's position relative to the zone map (0 = bottom edge, 1 = top edge) (`number`)
- `name` - Name of the unit for display on the map (`string`)

---

## GetBattlefieldScore

Returns basic scoreboard information for a battleground/arena participant. Does not include battleground-specific score data (e.g. flags captured in Warsong Gulch, towers assaulted in Alterac Valley, etc); see [`GetBattlefieldStatData()`](Battlefield.md#getbattlefieldstatdata) for such information.

**Signature:**

```lua
name, killingBlows, honorableKills, deaths, honorGained, faction, race, class, classToken, damageDone, healingDone, bgRating, ratingChange, preMatchMMR, mmrChange, talentSpec = GetBattlefieldScore(index)
```

**Arguments:**

- `index` - Index of a participant in the battleground/arena scoreboard (between 1 and [`GetNumBattlefieldScores()`](Battlefield.md#getnumbattlefieldscores)) (`number`)

**Returns:**

- `name` - Name of the participant (`string`)
- `killingBlows` - Number of killing blows scored by the participant during the match (`number`)
- `honorableKills` - Number of honorable kills scored by the participant during the match (`number`)
- `deaths` - Number of times the participant died during the match (`number`)
- `honorGained` - Amount of honor points gained by the participant during the match (`number`)
- `faction` - Faction or team to which the participant belongs (`number`)
  - `0` - Horde (Battleground) / Green Team (Arena)
  - `1` - Alliance (Battleground) / Gold Team (Arena)
- `race` - Localized name of the participant's race (`string`)
- `class` - Localized token representing the participant's class (`string`)
- `classToken` - Non-localized token representing the participant's class (`string`)
- `damageDone` - Total amount of damage done by the participant during the match (`number`)
- `healingDone` - Total amount of healing done by the participant during the match (`number`)
- `bgRating` - Personal battleground rating at the start of the match (`number`)
- `ratingChange` - Amount of rating gained/lost during the match (`number`)
- `preMatchMMR` - After 4.2 update is always zero (`number`)
- `mmrChange` - After 4.2 update is always zero (`number`)
- `talentSpec` - Localized name of player build (`string`)

---

## GetBattlefieldStatData

Returns battleground-specific scoreboard information for a battleground participant. Battleground-specific statistics include flags captured in Warsong Gulch, towers assaulted in Alterac Valley, etc. For the name and icon associated with each statistic, see [`GetBattlefieldStatInfo()`](Battlefield.md#getbattlefieldstatinfo). For basic battleground score information, see [`GetBattlefieldScore()`](Battlefield.md#getbattlefieldscore).

**Signature:**

```lua
columnData = GetBattlefieldStatData(index, statIndex)
```

**Arguments:**

- `index` - Index of a participant in the battleground/arena scoreboard (between 1 and [`GetNumBattlefieldScores()`](Battlefield.md#getnumbattlefieldscores)) (`number`)
- `statIndex` - Index of a battleground-specific statistic (between 1 and [`GetNumBattlefieldStats()`](Battlefield.md#getnumbattlefieldstats)) (`number`)

**Returns:**

- `columnData` - The participant's score for the statistic (`number`)

---

## GetBattlefieldStatInfo

Returns information about a battleground-specific scoreboard column. Battleground-specific statistics include flags captured in Warsong Gulch, towers assaulted in Alterac Valley, etc.

**Signature:**

```lua
text, icon, tooltip = GetBattlefieldStatInfo(statIndex)
```

**Arguments:**

- `statIndex` - Index of a battleground-specific statistic (between 1 and [`GetNumBattlefieldStats()`](Battlefield.md#getnumbattlefieldstats)) (`number`)

**Returns:**

- `text` - Name to display for the statistic's scoreboard column header (`string`)
- `icon` - Path to an icon texture for the statistic (`string`)
- `tooltip` - Text to be displayed as a tooltip when mousing over the scoreboard column (`string`)

---

## GetBattlefieldStatus

Returns information about an active or queued battleground/arena instance

**Signature:**

```lua
status, mapName, instanceID, bracketMin, bracketMax, teamSize, registeredMatch = GetBattlefieldStatus(index)
```

**Arguments:**

- `index` - Index of a battleground/arena queue the player has joined (between 1 and [`GetMaxBattlefieldID()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMaxBattlefieldID)) (`number`)

**Returns:**

- `status` - Status of the player with respect to the battleground (`string`)
  - `active` - The player is currently playing in this battleground
  - `confirm` - The player has been invited to enter this battleground but has not done so yet
  - `none` - No battleground or queue at this index
  - `queued` - The player is queued for this battleground
- `mapName` - Name of the battleground (e.g. "Alterac Valley") or arena ("All Arenas" while `queued`; "Eastern Kingdoms" regardless of destination while status is `confirm`, e.g. "Dalaran Sewers" while `active`) (`string`)
- `instanceID` - If in a battleground or queued for a specific instance, the number identifying that instance (e.g. 13 in "Warsong Gulch 13"); otherwise 0 (`number`)
- `bracketMin` - Lowest level of characters in the player's level bracket for the battleground (`number`)
- `bracketMax` - Highest level of characters in the player's level bracket for the battleground (`number`)
- `teamSize` - Number of players per team for an arena match (`number`)
  - `0` - Not an arena match
  - `2` - 2v2 Arena
  - `3` - 3v3 Arena
  - `5` - 5v5 Arena
- `registeredMatch` - 1 if a rated arena match; otherwise nil (`1nil`)

---

## GetBattlefieldTeamInfo

Returns info about teams and their ratings in a rated arena match.. Usable following the [`UPDATE_BATTLEFIELD_SCORE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UPDATE_BATTLEFIELD_SCORE) event.

**Signature:**

```lua
teamName, teamRating, newTeamRating = GetBattlefieldTeamInfo(index)
```

**Arguments:**

- `index` - Index of a team in the arena match (`number`)
  - `0` - Green Team
  - `1` - Gold Team

**Returns:**

- `teamName` - Name of the team (`string`)
- `teamRating` - The team's rating at the start of the match (`number`)
- `newTeamRating` - New rating for the team when the match is complete (`number`)

---

## GetBattlefieldTimeWaited

Returns the amount of time elapsed since the player joined the queue for a battleground/arena

**Signature:**

```lua
timeInQueue = GetBattlefieldTimeWaited(index)
```

**Arguments:**

- `index` - Index of a battleground/arena queue the player has joined (between 1 and `MAX_BATTLEFIELD_QUEUES`) (`number`)

**Returns:**

- `timeInQueue` - Time elapsed since the player joined the queue (in milliseconds) (`number`)

---

## GetBattlefieldVehicleInfo

Returns information about special vehicles in the current zone. Used only for certain vehicles in certain zones: includes the airships in Icecrown as well as vehicles used in Ulduar, Wintergrasp, and Strand of the Ancients.

**Signature:**

```lua
vehicleX, vehicleY, unitName, isPossessed, vehicleType, orientation, isPlayer, isAlive = GetBattlefieldVehicleInfo(index)
```

**Arguments:**

- `index` - Index of a special vehicle (between 1 and [`GetNumBattlefieldVehicles()`](Battlefield.md#getnumbattlefieldvehicles)) (`number`)

**Returns:**

- `vehicleX` - Horizontal position of the vehicle relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `vehicleY` - Vertical position of the vehicle relative to the zone map (0 = top, 1 = bottom) (`number`)
- `unitName` - Localized name of the vehicle (`string`)
- `isPossessed` - True if the vehicle is controlled by another unit (`boolean`)
- `vehicleType` - Token indicating type of vehicle; some types can be used as keys to the global `VEHICLE_TEXTURES` table to get display texture information for the vehicle (`string`)
  - `Airship Alliance` - The Alliance flying quest hub in Icecrown
  - `Airship Horde` - The Horde flying quest hub in Icecrown
  - `Drive` - A land vehicle such as a siege engine
  - `Fly` - A flying vehicle
  - `Idle` - A non-moving vehicle (e.g. an artillery turret)
- `orientation` - Facing angle of the vehicle ((in radians, 0 = north, values increasing counterclockwise) (`number`)
- `isPlayer` - True if the vehicle is controlled by the player (`boolean`)
- `isAlive` - True if the vehicle has not been destroyed (`boolean`)

---

## GetBattlefieldWinner

Returns the winner of the current battleground or arena match

**Signature:**

```lua
winner = GetBattlefieldWinner()
```

**Returns:**

- `winner` - Index of the winning team if in a completed match; otherwise nil (`number`)
  - `0` - Horde (Battleground) / Green Team (Arena)
  - `1` - Alliance (Battleground) / Gold Team (Arena)

---

## GetBattlegroundInfo

Returns information about available battlegrounds

**Signature:**

```lua
name, canEnter, isHoliday, minlevel = GetBattlegroundInfo(index)
```

**Arguments:**

- `index` - Index of a battleground (between 1 and `NUM_BATTLEGROUNDS`) (`number`)

**Returns:**

- `name` - Localized name of the battleground (Alterac Valley, Warsong Gulch, etc.) (`string`)
- `canEnter` - 1 if the player can enter the battleground; otherwise nil (`1nil`)
- `isHoliday` - 1 if a "holiday" offering bonus honor is currently active for the battleground; otherwise nil (`1nil`)
- `minlevel` - Minimum character level required to enter the battleground (`number`)

---

## GetNumBattlefieldFlagPositions

Returns the number of battleground flags for which map position information is available

**Signature:**

```lua
numFlags = GetNumBattlefieldFlagPositions()
```

**Returns:**

- `numFlags` - Number of battleground flags for which map position information is available (`number`)

---

## GetNumBattlefieldPositions

Returns the number of team members in the battleground not in the player's group. Still used in the default UI but no longer useful; always returns 0, as all team members in a battleground match are automatically joined into a raid group.

**Signature:**

```lua
numTeamMembers = GetNumBattlefieldPositions()
```

**Returns:**

- `numTeamMembers` - Number of team members in the battleground not in the player's party or raid (`number`)

---

## GetNumBattlefieldScores

Returns the number of participant scores available in the current battleground

**Signature:**

```lua
numScores = GetNumBattlefieldScores()
```

**Returns:**

- `numScores` - Number of participant scores available in the current battleground; 0 if not in a battleground (`number`)

---

## GetNumBattlefieldStats

Returns the number of battleground-specific statistics on the current battleground's scoreboard. Battleground-specific statistics include flags captured in Warsong Gulch, towers assaulted in Alterac Valley, etc. For the name and icon associated with each statistic, see [`GetBattlefieldStatInfo()`](Battlefield.md#getbattlefieldstatinfo).

**Signature:**

```lua
numStats = GetNumBattlefieldStats()
```

**Returns:**

- `numStats` - Number of battleground-specific scoreboard columns (`number`)

---

## GetNumBattlefieldVehicles

Returns the number of special vehicles in the current zone. Used only for certain vehicles in certain zones: includes the airships in Icecrown as well as vehicles used in Ulduar, Wintergrasp, and Strand of the Ancients.

**Signature:**

```lua
numVehicles = GetNumBattlefieldVehicles()
```

**Returns:**

- `numVehicles` - Number of special vehicles (`number`)

---

## GetNumBattlefields

Returns the number of instances available for a battleground

**Signature:**

```lua
numBattlefields = GetNumBattlefields([index])
```

**Arguments:**

- `index` - Index of a battleground (between 1 and `NUM_BATTLEGROUNDS`), if using the queue-anywhere UI; not used when choosing an instance for a single battleground (e.g. at a battlemaster or battleground portal) (`number`)

**Returns:**

- `numBattlefields` - Number of instances currently available for the battleground (`number`)

---

## GetNumBattlegroundTypes

Returns the number of different battlegrounds available. Refers to distinct battlegrounds, not battleground instances. Does not indicate the number of battlegrounds the player can enter: for that, see [`GetBattlegroundInfo`](Battlefield.md#getbattlegroundinfo).

As of WoW 3.2, should always return 6: for Alterac Valley, Warsong Gulch, Arathi Basin, Eye of the Storm, Strand of the Ancients, and Isle of Conquest. If a future patch adds a new battleground, this function will reflect that.

**Signature:**

```lua
numBattlegrounds = GetNumBattlegroundTypes()
```

**Returns:**

- `numBattlegrounds` - Number of different battlegrounds available (`number`)

---

## GetRealNumPartyMembers

Returns the number of members in the player's non-battleground party. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
numMembers = GetRealNumPartyMembers()
```

**Returns:**

- `numMembers` - Number of members in the player's non-battleground party (`number`)

---

## GetRealNumRaidMembers

Returns the number of members in the player's non-battleground raid. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
numMembers = GetRealNumRaidMembers()
```

**Returns:**

- `numMembers` - Number of members in the player's non-battleground raid (`number`)

---

## GetSelectedBattlefield

Returns the index of the selected battleground instance in the queueing list. Selection in the battleground instance list is used only for display in the default UI and has no effect on other Battlefield APIs.

**Signature:**

```lua
index = GetSelectedBattlefield()
```

**Returns:**

- `index` - Index of the selection in the battleground queue listing (1 for the first available instance, or between 2 and [`GetNumBattlefields()`](Battlefield.md#getnumbattlefields) for other instances) (`number`)

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

## IsBattlefieldArena

Returns whether the player is interacting with an entity that allows queueing for arena matches

---

## IsRealPartyLeader

Returns whether the player is the leader of a non-battleground party. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
isLeader = IsRealPartyLeader()
```

**Returns:**

- `isLeader` - 1 if the player is the leader of a non-battleground party; otherwise nil (`1nil`)

---

## IsRealRaidLeader

Returns whether the player is the leader of a non-battleground raid. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
isLeader = IsRealRaidLeader()
```

**Returns:**

- `isLeader` - 1 if the player is the leader of a non-battleground raid; otherwise nil (`1nil`)

---

## JoinBattlefield

Joins the queue for a battleground instance

**Signature:**

```lua
JoinBattlefield(index, asGroup)
```

**Arguments:**

- `index` - Index in the battleground queue listing (1 for the first available instance, or between 2 and [`GetNumBattlefields()`](Battlefield.md#getnumbattlefields) for other instances) (`number`)
- `asGroup` - True to enter the player's entire party/raid in the queue; false to enter the player only (`boolean`)

---

## LeaveBattlefield

Immediately exits the current battleground instance. Returns the player to the location from which he or she joined the battleground and applies the Deserter debuff.

**Signature:**

```lua
LeaveBattlefield()
```

---

## PlayerIsPVPInactive

Returns whether a battleground participant is inactive (and eligible for reporting as AFK)

**Signature:**

```lua
isInactive = PlayerIsPVPInactive("name") or PlayerIsPVPInactive("unit")
```

**Arguments:**

- `name` - Name of a friendly player unit in the current battleground (`string`)
- `unit` - A friendly player unit in the current battleground (`string`, [unitID](../types/unitID.md))

**Returns:**

- `isInactive` - True if the unit can be reported as AFK; otherwise false (`boolean`)

---

## ReportPlayerIsPVPAFK

Reports a battleground participant as AFK

**Signature:**

```lua
ReportPlayerIsPVPAFK("name") or ReportPlayerIsPVPAFK("unit")
```

**Arguments:**

- `name` - Name of a friendly player unit in the current battleground (`string`)
- `unit` - A friendly player unit in the current battleground (`string`, [unitID](../types/unitID.md))

---

## RequestBattlefieldPositions `server`

Requests information from the server about team member positions in the current battleground. Automatically called in the default UI by UIParent's and WorldMapFrame's OnUpdate handlers.

**Signature:**

```lua
RequestBattlefieldPositions()
```

---

## RequestBattlefieldScoreData `server`

Requests battlefield score data from the server. Score data is not returned immediately; the [`UPDATE_BATTLEFIELD_SCORE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UPDATE_BATTLEFIELD_SCORE) event fires once information is available and can be retrieved by calling [`GetBattlefieldScore()`](Battlefield.md#getbattlefieldscore) and related functions.

**Signature:**

```lua
RequestBattlefieldScoreData()
```

---

## RequestBattlegroundInstanceInfo `server`

Requests information about available instances of a battleground from the server. The [`PVPQUEUE_ANYWHERE_SHOW`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PVPQUEUE_ANYWHERE_SHOW) event fires once information is available; data can then be retrieved by calling [`GetNumBattlefields()`](Battlefield.md#getnumbattlefields) and [`GetBattlefieldInstanceInfo()`](Battlefield.md#getbattlefieldinstanceinfo).

**Signature:**

```lua
RequestBattlegroundInstanceInfo(index)
```

**Arguments:**

- `index` - Index of a battleground (between 1 and `NUM_BATTLEGROUNDS`) (`number`)

---

## SetBattlefieldScoreFaction

Filters the battleground scoreboard by faction/team

**Signature:**

```lua
SetBattlefieldScoreFaction(faction)
```

**Arguments:**

- `faction` - Faction for which to show battleground participant scores (`number`)
  - `0` - Horde
  - `1` - Alliance
  - `nil` - All

---

## SetSelectedBattlefield

Selects a battleground instance in the queueing list. Selection in the battleground instance list is used only for display in the default UI and has no effect on other Battlefield APIs.

**Signature:**

```lua
SetSelectedBattlefield(index)
```

**Arguments:**

- `index` - Index in the battleground queue listing (1 for the first available instance, or between 2 and [`GetNumBattlefields()`](Battlefield.md#getnumbattlefields) for other instances) (`number`)

---

## ShowMiniWorldMapArrowFrame

Shows or hides the battlefield minimap's player arrow

**Signature:**

```lua
ShowMiniWorldMapArrowFrame(show)
```

**Arguments:**

- `show` - If the battlefield minimap's player arrow should be shown (`boolean`)

---

## SortBattlefieldScoreData

Sorts the battleground scoreboard. Battleground-specific statistics include flags captured in Warsong Gulch, towers assaulted in Alterac Valley, etc. For the name and icon associated with each statistic, see [`GetBattlefieldStatInfo()`](Battlefield.md#getbattlefieldstatinfo).

**Signature:**

```lua
SortBattlefieldScoreData("sortType")
```

**Arguments:**

- `sortType` - Criterion for sorting the scoreboard data (`string`)
  - `class` - Sort by character class
  - `cp` - Sorts by honor points gained
  - `damage` - Sorts by damage done
  - `deaths` - Sort by number of deaths
  - `healing` - Sorts by healing done
  - `hk` - Sorts by number of honor kills
  - `kills` - Sort by number of kills
  - `name` - Sort by participant name
  - `stat1` - Battlefield-specific statistic 1
  - `stat2` - Battlefield-specific statistic 2
  - `stat3` - Battlefield-specific statistic 3
  - `stat4` - Battlefield-specific statistic 4
  - `stat5` - Battlefield-specific statistic 5
  - `stat6` - Battlefield-specific statistic 6
  - `stat7` - Battlefield-specific statistic 7
  - `team` - Sort by team name

---

## UnitInBattleground

Returns whether a unit is in same battleground instance as the player

**Signature:**

```lua
raidNum = UnitInBattleground("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `raidNum` - Numeric portion of the unit's `raid` [`unitID`](../types/unitID.md) (e.g. 13 for `raid13`) (`number`)

---

← [WoW API Docs](../index.md)
