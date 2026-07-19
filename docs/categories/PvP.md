# PvP functions

← [WoW API Docs](../index.md)

**26** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#pvp)

---

## CanHearthAndResurrectFromArea

Returns whether the player is in a world PvP zone offering an exit option.

Used by the default UI to show the MiniMapBattlefieldFrame and provide a menu option for leaving if the player is in a world PvP combat zone (i.e. Wintergrasp).

**Signature:**

```lua
status = CanHearthAndResurrectFromArea()
```

**Returns:**

- `status` - 1 if in a world PvP zone with an exit option; otherwise nil (`1nil`)

---

## CanQueueForWintergrasp

Returns whether the player can queue for Wintergrasp

**Signature:**

```lua
canQueue = CanQueueForWintergrasp()
```

**Returns:**

- `canQueue` - Can the player queue for Wintergrasp (`boolean`)

---

## GetHolidayBGHonorCurrencyBonuses

Returns the awarded honor and arena points for a Call to Arms battleground win or loss

**Signature:**

```lua
unk, honorWinReward, arenaWinReward, honorLossReward, arenaLossReward = GetHolidayBGHonorCurrencyBonuses()
```

**Returns:**

- `unk` - Unknown (`boolean`)
- `honorWinReward` - Honor points rewarded for a win (`number`)
- `arenaWinReward` - Arena points rewarded for a win (`number`)
- `honorLossReward` - Honor points rewarded for a loss (`number`)
- `arenaLossReward` - Arena points rewarded for a loss (`number`)

---

## GetHonorCurrency

Returns the player's amount of honor points

**Signature:**

```lua
honorPoints, maxHonor = GetHonorCurrency()
```

**Returns:**

- `honorPoints` - The player's current amount of honor points (`number`)
- `maxHonor` - The maximum amount of honor currency the player can accrue (`number`)

---

## GetNumWorldStateUI

Returns the number of world state UI elements. World State UI elements include PvP, instance, and quest objective information (displayed at the top center of the screen in the default UI) as well as more specific information for "control point" style PvP objectives. Examples: the Horde/Alliance score in Arathi Basin, the tower status and capture progress bars in Hellfire Peninsula, the progress text in the Black Morass and Violet Hold instances, and the event status text for quests [The Light of Dawn](http://www.wowhead.com/?quest=12801) and [The Battle For The Undercity](http://www.wowhead.com/?quest=13267).

**Signature:**

```lua
numUI = GetNumWorldStateUI()
```

**Returns:**

- `numUI` - Returns the number of world state elements (`number`)

---

## GetPVPDesired

Returns whether the player has manually enabled PvP status. Only indicates whether the player has manually and directly enabled his PvP flag (e.g. by typing "/pvp" or using the default UI's menu when right-clicking the player portrait); returns 0 if the player only became PvP flagged by attacking an enemy player, entering an enemy zone, etc.

**Signature:**

```lua
isPVPDesired = GetPVPDesired()
```

**Returns:**

- `isPVPDesired` - 1 if the PVP flag was toggled on by the player manually; otherwise 0 (`number`)

---

## GetPVPLifetimeStats

Returns the player's lifetime total of honorable kills and highest rank achieved. Highest rank achieved applies only to the older PvP rewards system that was abandoned with the WoW 2.0 patch, but is still accurate for players who participated in it.

**Signature:**

```lua
hk, highestRank = GetPVPLifetimeStats()
```

**Returns:**

- `hk` - Number of honorable kills the player has scored (`number`)
- `highestRank` - Highest rank the player ever achieved in the pre-2.0 PvP rewards system (`number`)

---

## GetPVPRankInfo

Returns information about a given PvP rank index. These ranks are no longer in use, as they were part of the older PvP rewards system that was abandoned with the WoW 2.0 patch.

**Signature:**

```lua
rankName, rankNumber = GetPVPRankInfo(index [, "unit"])
```

**Arguments:**

- `index` - Index of a rank (begins at 1, corresponding to a never-used "Pariah" rank; actual ranks start at 5) (`number`)
- `unit` - A unit to use as basis for the rank name (i.e. to return Horde rank names for Horde units and Alliance rank names for Alliance units); if omitted, uses the player's faction (`string`, [unitID](../types/unitID.md))

**Returns:**

- `rankName` - Name of the rank (`string`)
- `rankNumber` - Index of the rank relative to unranked status (positive values for ranks earned through honorable kills, negative values for the unused dishonorable ranks) (`number`)

---

## GetPVPRankProgress `deprecated`

**Signature:**

```lua
GetPVPRankProgress()
```

---

## GetPVPSessionStats

Returns the number of kills and honor points scored by the player since logging in

**Signature:**

```lua
honorKills, honorPoints = GetPVPSessionStats()
```

**Returns:**

- `honorKills` - Number of honorable kills scored (`number`)
- `honorPoints` - Amount of honor currency earned (`number`)

---

## GetPVPTimer

Returns the amount of time until the player's PVP flag expires. Returns 300000 or higher if the player's PvP flag is manually enabled or if the player is in a PvP or enemy zone.

**Signature:**

```lua
timer = GetPVPTimer()
```

**Returns:**

- `timer` - Milliseconds remaining until the player's PvP flag expires (`number`)

---

## GetPVPYesterdayStats

Returns the number of kills and honor points scored by the player on the previous day

**Signature:**

```lua
honorKills, honorPoints = GetPVPYesterdayStats()
```

**Returns:**

- `honorKills` - Number of honorable kills scored (`number`)
- `honorPoints` - Amount of honor currency earned (`number`)

---

## GetWintergraspWaitTime

Returns the amount of time remaining until the next PvP event in the Wintergrasp zone

---

## GetWorldPVPQueueStatus

Returns information on the players queue for a world PvP zone

**Signature:**

```lua
status, mapName, queueID = GetWorldPVPQueueStatus(index)
```

**Arguments:**

- `index` - Index of the queue to get data for (between 1 and `MAX_WORLD_PVP_QUEUES`) (`number`)

**Returns:**

- `status` - Returns the status of the players queue (`string`)
  - `confirm` - The player can enter the pvp zone
  - `none` - No world pvp queue at this index
  - `queued` - The player is queued for this pvp zone
- `mapName` - Map name they are queued for (e.g Wintergrasp) (`string`)
- `queueID` - Queue ID, used for [BattlefieldMgrExitRequest()](Uncategorized.md#battlefieldmgrexitrequest) and [BattlefieldMgrEntryInviteResponse()](Uncategorized.md#battlefieldmgrentryinviteresponse) (`number`)

---

## GetWorldStateUIInfo

Returns information about a world state UI element. World State UI elements include PvP, instance, and quest objective information (displayed at the top center of the screen in the default UI) as well as more specific information for "control point" style PvP objectives. Examples: the Horde/Alliance score in Arathi Basin, the tower status and capture progress bars in Hellfire Peninsula, the progress text in the Black Morass and Violet Hold instances, and the event status text for quests [The Light of Dawn](https://web.archive.org/web/20100106001949/http://www.wowhead.com/?quest=12801) and [The Battle For The Undercity](https://web.archive.org/web/20100106001949/http://www.wowhead.com/?quest=13267).

**Signature:**

```lua
uiType, state, text, icon, dynamicIcon, tooltip, dynamicTooltip, extendedUI, extendedUIState1, extendedUIState2, extendedUIState3 = GetWorldStateUIInfo(index)
```

**Arguments:**

- `index` - Index of a world state UI element (between 1 and [`GetNumWorldStateUI()`](Instance.md#getnumworldstateui)) (`number`)

**Returns:**

- `uiType` - 1 if the element should be conditionally displayed (based on the state of the "Show World PvP Objectives" setting and the player's location); any other value if the element is always displayed (`number`)
- `state` - State of the element: 0 always indicates the element should be hidden; other possible states vary by context (e.g. in Warsong Gulch, state 2 indicates the team holds the enemy flag) (`number`)
- `text` - Text to be displayed for the element (`string`)
- `icon` - Path to a texture for the element's main icon (usually describing the element itself: e.g. a Horde or Alliance icon for elements displaying a battleground score) (`string`)
- `dynamicIcon` - Path to a texture for a secondary icon (usually describing transient status: e.g. a flag icon in Warsong Gulch) (`string`)
- `tooltip` - Text to be displayed when mousing over the UI element (`string`)
- `dynamicTooltip` - Text to be displayed when mousing over the element's `dynamicIcon` (`string`)
- `extendedUI` - Identifies the type of additional UI elements to display if applicable (`string`)
  - `""` - No additional UI should be displayed
  - `"CAPTUREPOINT"` - A capture progress bar should be displayed for the element
- `extendedUIState1` - Index of the capture progress bar corresponding to the element (`number`)
- `extendedUIState2` - Position of the capture bar (0 = left/Horde edge, 100 = right/Alliance edge) (`number`)
- `extendedUIState3` - Width of the neutral section of the capture bar: e.g. if 50, the `extendedUIState2` values 0-25 correspond to Horde ownership of the objective, values 76-100 to Alliance ownership, and values 26-75 to no ownership (`number`)

---

## GetZonePVPInfo

Returns PVP information about the current area. Information returned may apply to the current subzone, not the entire zone.

**Signature:**

```lua
pvpType, isSubZonePVP, factionName = GetZonePVPInfo()
```

**Returns:**

- `pvpType` - PvP status for the area (`string`)
  - `arena` - Arena or outdoor free-for-all area (e.g. Gurubashi Arena)
  - `combat` - Combat zone (e.g. Wintergrasp)
  - `contested` - Horde/Alliance PvP is enabled for all players
  - `friendly` - Zone is controlled by the player's faction; PvP status is optional for the player but mandatory for enemy players
  - `hostile` - Zone is controlled by the enemy's faction; PvP status is optional for the enemy but mandatory for the player
  - `nil` - PvP status is not automatically enabled for either faction (used for "contested" zones on Normal servers)
  - `sanctuary` - PvP activity is not allowed (e.g. Dalaran)
- `isSubZonePVP` - 1 if the current area allows free-for-all PVP; otherwise nil (`1nil`)
- `factionName` - Name of the faction that controls the zone (only applies if `pvpType` is friendly or hostile) (`string`)

---

## HearthAndResurrectFromArea

Instantly exits the current world PvP zone, returning to the player's Hearthstone location.

Resets the player's Hearthstone cooldown, and also returns the player to life if dead. Only usable if the player is in a world PvP combat zone (i.e. Wintergrasp).

**Signature:**

```lua
HearthAndResurrectFromArea()
```

---

## IsPVPTimerRunning

Returns whether the player's PvP flag will expire after a period of time.

If in a zone that flags the player for PvP, or if the player has manually enabled PvP, the flag will not expire. Once not in such a zone, or once the player has manually disabled PvP, or if the player has been flagged by attacking an enemy unit, the timer starts running and the player's PvP flag will expire after some time.

**Signature:**

```lua
isRunning = IsPVPTimerRunning()
```

**Returns:**

- `isRunning` - 1 if the player's PvP flag will expire; otherwise nil (`1nil`)

---

## IsSubZonePVPPOI

Returns whether the current area has PvP (or other) objectives to be displayed. Used in the default UI when the "Display World PVP Objectives\ setting is set to \Dynamic\, in which case objective information is only shown when the player is near an objective. Examples include the towers in Eastern Plaguelands and Hellfire Peninsula as well as non-PvP objectives such as in the Old Hillsbrad instance, the Death Knight starter quests, and the Battle for Undercity quest event.

**Signature:**

```lua
isPVPPOI = IsSubZonePVPPOI()
```

**Returns:**

- `isPVPPOI` - 1 if the current subzone has objectives to display (`1nil`)

---

## QuestFlagsPVP

Returns whether accepting the offered quest will flag the player for PvP. Only valid when the questgiver UI is showing the accept/decline stage of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events); otherwise may return nil or a value from the most recently displayed quest.

**Signature:**

```lua
questFlag = QuestFlagsPVP()
```

**Returns:**

- `questFlag` - 1 if accepting the quest will flag the player for PvP for as long as it remains in the quest log; otherwise nil (`1nil`)

---

## SetPVP

Enables or disables the player's desired PvP status. Enabling PvP takes effect immediately; disabling PvP begins a five-minute countdown after which PvP status will be disabled (if the player has taken no PvP actions).

**Signature:**

```lua
SetPVP(state)
```

**Arguments:**

- `state` - 1 to enable PVP, nil to disable (`1nil`)

---

## TogglePVP

Switches the player's desired PvP status. If PvP is currently disabled for the player, it becomes enabled immediately. If PvP is enabled, it will become disabled after five minutes of no PvP activity.

**Signature:**

```lua
TogglePVP()
```

---

## UnitIsPVPFreeForAll

Returns whether a unit is flagged for free-for-all PvP. Free-for-all PvP allows all players to attack each other regardless of faction; used in certain outdoor areas (such as Gurubashi Arena and "The Maul" outside Dire Maul).

**Signature:**

```lua
isFreeForAll = UnitIsPVPFreeForAll("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `isFreeForAll` - 1 if the unit is enabled for free-for-all PvP; otherwise nil (`1nil`)

---

## UnitIsPVPSanctuary

Returns whether a unit is in a Sanctuary area preventing PvP activity

**Signature:**

```lua
state = UnitIsPVPSanctuary("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `state` - 1 if the unit is in a PVP Sanctuary; otherwise nil (`1nil`)

---

## UnitPVPName

Returns the name of a unit including the unit's current title. Titles are no longer specific to PvP; this function returns a unit's name with whichever title he or she is currently displaying (e.g. "Gladiator Spin", "Keydar Jenkins", "Ownsusohard, Champion of the Frozen Wastes", etc).

**Signature:**

```lua
name = UnitPVPName("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `name` - Name of the unit including the unit's current title (`string`)

---

## UnitPVPRank `deprecated`

Returns a unit's PVP rank as a number. Returns 0 for all units; was only applicable in the older PvP rewards system that was abandoned with the WoW 2.0 patch.

**Signature:**

```lua
rank = UnitPVPRank("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `rank` - The numeric PvP rank of the unit, or 0 if the unit has no PvP rank (`number`)

---

← [WoW API Docs](../index.md)
