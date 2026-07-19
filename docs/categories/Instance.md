# Instance functions

← [WoW API Docs](../index.md)

**17** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#instance)

---

## CanShowResetInstances

Returns whether the player can reset instances. Used to determine whether to display the "Reset Instance" option in the unit popup menu for the player.

Only instances to which the player is not saved may be reset (i.e. normal 5-man dungeons, not heroic dungeons or raids), and only by a solo player or group leader.

**Signature:**

```lua
canResetInstances = CanShowResetInstances()
```

**Returns:**

- `canResetInstances` - 1 if the player can currently reset instances; otherwise nil (`1nil`)

---

## GetDungeonDifficulty

Returns the 5 player selected dungeon difficulty

**Signature:**

```lua
difficulty = GetDungeonDifficulty()
```

**Returns:**

- `difficulty` - The current 5 player dungeon difficulty (`number`)
  - `1` - Normal
  - `2` - Heroic

---

## GetInstanceBootTimeRemaining

Returns the amount of time left until the player is removed from the current instance. Used when the player is in an instance he doesn't own; e.g. if the player enters an instance with a group and is then removed from the group.

**Signature:**

```lua
timeleft = GetInstanceBootTimeRemaining()
```

**Returns:**

- `timeleft` - The number of seconds until the player is booted from the current instance (`number`)

---

## GetInstanceDifficulty

Returns difficulty setting for the current dungeon/raid instance.

This returns the difficulty setting for the instance the player is **currently in**; not to be confused with `GetCurrentDungeonDifficulty()`, which is the current group's setting for entering new instances, nor with `GetDefaultDungeonDifficulty()`, which is the player's preference for dungeon difficulty and may differ from that of the current party leader.

**Signature:**

```lua
difficulty = GetInstanceDifficulty()
```

**Returns:**

- `difficulty` - The current instance's difficulty setting (`number`)
  - `1` - Normal (5 or 10 players)
  - `2` - Heroic (5 players) / Normal (25 players)
  - `3` - Heroic (10 players)
  - `4` - Heroic (25 players)

---

## GetInstanceInfo

Returns instance information about the current area

**Signature:**

```lua
name, type, difficulty, difficultyName, maxPlayers, playerDifficulty, isDynamicInstance = GetInstanceInfo()
```

**Returns:**

- `name` - Name of the instance or world area (`string`)
- `type` - Type of the instance (`string`)
  - `arena` - A PvP Arena instance
  - `none` - Normal world area (e.g. Northrend, Kalimdor, Deeprun Tram)
  - `party` - An instance for 5-man groups
  - `pvp` - A PvP battleground instance
  - `raid` - An instance for raid groups
- `difficulty` - Difficulty setting of the instance (`number`)
  - `1` - In raids, this represents 10 Player. In instances, Normal.
  - `2` - In raids, this represents 25 Player. In instances, Heroic.
  - `3` - In raids, this represents 10 Player Heroic. In instances, Epic (unused for PvE instances but returned in some battlegrounds).
  - `4` - In raids, this represents 25 Player Heroic. No corollary in instances.
- `difficultyName` - String representing the difficulty of the instance. E.g. "10 Player" (`string`)
- `maxPlayers` - Maximum number of players allowed in the instance (`number`)
- `playerDifficulty` - Unknown (`number`)
- `isDynamicInstance` - Unknown (`boolean`)

---

## GetInstanceLockTimeRemaining

Returns time remaining before the player is saved to a recently entered instance.

Applies when the player enters an instance to which other members of her group are saved; if the player leaves the instance (normally or with `RespondInstanceLock(false)`) within this time limit she will not be saved to the instance.

**Signature:**

```lua
seconds = GetInstanceLockTimeRemaining()
```

**Returns:**

- `seconds` - Time remaining before the player is saved to the instance (`number`)

---

## GetNumSavedInstances

Returns the number of instances to which the player is saved

**Signature:**

```lua
savedInstances = GetNumSavedInstances()
```

**Returns:**

- `savedInstances` - Number of instances to which the player is saved (`number`)

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

## GetSavedInstanceInfo

Returns information on a specific instance to which the player is saved

**Signature:**

```lua
instanceName, instanceID, instanceReset, instanceDifficulty, locked, extended, instanceIDMostSig, isRaid, maxPlayers, difficultyName = GetSavedInstanceInfo(index)
```

**Arguments:**

- `index` - Index of a saved instance (between 1 and [`GetNumSavedInstances()`](Instance.md#getnumsavedinstances)) (`number`)

**Returns:**

- `instanceName` - Name of the instance (`string`)
- `instanceID` - Unique identifier of the saved instance (commonly known as a RaidID) (`number`)
- `instanceReset` - Approximate number of seconds remaining until the instance resets (`number`)
- `instanceDifficulty` - Difficulty level of the saved instance (`number`)
  - `1` - Normal ('10 Player' if instance is a raid)
  - `2` - Heroic ('25 Player' if instance is a raid)
  - `3` - 10 Player Heroic
  - `4` - 25 Player Heroic
- `locked` - (`boolean`)
- `extended` - `true` if the reset time has been extended past its normal time; otherwise `false` (`boolean`)
- `instanceIDMostSig` - (`number`)
- `isRaid` - (`boolean`)
- `maxPlayers` - Number of players allowed (`number`)
- `difficultyName` - A string representing the difficulty of the given instance. (`string`)

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

## IsInInstance

Returns whether the player is in an instance (and its type if applicable)

**Signature:**

```lua
isInstance, instanceType = IsInInstance()
```

**Returns:**

- `isInstance` - 1 if the player is in an instance, otherwise nil (`1nil`)
- `instanceType` - The type of instance the player is in (`string`)
  - `arena` - Player versus player arena
  - `none` - Not inside an instance
  - `party` - 5-man instance
  - `pvp` - Player versus player battleground
  - `raid` - Raid instance

---

## LFGTeleport

Teleports the player to or from their current LFG dungeon

**Signature:**

```lua
LFGTeleport(portOut)
```

**Arguments:**

- `portOut` - A boolean flag that indicates if the player is trying to teleport out of the dungeon, or not. (`boolean`)

---

## RequestRaidInfo `server`

Requests information about saved instances from the server. Data is not returned immediately; the [`UPDATE_INSTANCE_INFO`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UPDATE_INSTANCE_INFO) event when the raid information is available for retrieval via [`GetSavedInstanceInfo()`](Instance.md#getsavedinstanceinfo) and related functions.

**Signature:**

```lua
RequestRaidInfo()
```

---

## ResetInstances

Resets all non-saved instances associated with the player. Only instances to which the player is not saved may be reset (i.e. normal 5-man dungeons, not heroic dungeons or raids), and only by a solo player or group leader.

**Signature:**

```lua
ResetInstances()
```

---

## RespondInstanceLock

Allows leaving a recently entered instance to which the player would otherwise be saved.

Applies when the player enters an instance to which other members of her group are saved; if the player leaves the within the time limit (see `GetInstanceLockTimeRemaining()`) she will not be saved to the instance.

**Signature:**

```lua
RespondInstanceLock(response)
```

**Arguments:**

- `response` - Whether the player wishes to remain in the instance (`boolean`)
  - `false` - Exit to the nearest graveyard
  - `true` - Remain in the zone, saving the player to this instance

---

## SetDungeonDifficulty

Sets the player's 5 player dungeon difficulty preference.

Setting dungeon difficulty has no effect on the instance created when entering a portal if the player is not the party/raid leader. Changing difficulty while in an instance also has no effect.

Epic difficulty is currently unused; setting dungeon difficulty to 3 will cause instance portal graphics to disappear and may result in errors upon entering an instance portal.

**Signature:**

```lua
SetDungeonDifficulty(difficulty)
```

**Arguments:**

- `difficulty` - A difficulty level (`number`)
  - `1` - 5 Player (Normal)
  - `2` - 5 Player (Heroic)

---

## SetRaidDifficulty

Sets the player's raid dungeon difficulty preference. The dungeon difficulty has no effect on the instance created if the player is not the raid leader or while you are inside an instance already.

**Signature:**

```lua
SetRaidDifficulty(difficulty)
```

**Arguments:**

- `difficulty` - Difficulty level for raid dungeons
  - `1` - 10 Player
  - `2` - 25 Player
  - `3` - 10 Player (Heroic)
  - `4` - 25 Player (Heroic)

---

← [WoW API Docs](../index.md)
