# Unit functions

← [WoW API Docs](../index.md)

**80** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#unit)

---

## CanInspect

Returns whether a unit can be inspected. Returns `nil` if the unit is out of inspect range, if the unit is an NPC, or if the unit is flagged for PvP combat and hostile to the player.

**Signature:**

```lua
canInspect = CanInspect("unit", showError)
```

**Arguments:**

- `unit` - A unit to inspect (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `showError` - True to fire a [`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE) event (causing the default UI to display an error message) if the unit cannot be inspected; otherwise false (`boolean`)

**Returns:**

- `canInspect` - 1 if the unit can be inspected; otherwise nil (`1nil`)

---

## CheckInteractDistance

Returns whether the player is close enough to a unit for certain types of interaction

**Signature:**

```lua
canInteract = CheckInteractDistance("unit", distIndex)
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `distIndex` - Number identifying one of the following action types (`number`)
  - `1` - Inspect
  - `2` - Trade
  - `3` - Duel
  - `4` - Follow

**Returns:**

- `canInteract` - 1 if the player is close enough to the other unit to perform the action; otherwise nil (`1nil`)

---

## GetGuildInfo

Returns a unit's guild affiliation

**Signature:**

```lua
guildName, guildRankName, guildRankIndex = GetGuildInfo("unit") or GetGuildInfo("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `guildName` - Name of the character's guild (`string`)
- `guildRankName` - Name of the character's guild rank (`string`)
- `guildRankIndex` - Numeric guild rank of the character (0 = guild leader; higher numbers for lower ranks) (`number`)

---

## GetMuteStatus

Returns whether a character is muted or silenced. If the `channel` argument is specified, this function checks the given character's voice/silence status on the channel as well as for whether the character is on the player's Muted list.

**Signature:**

```lua
muteStatus = GetMuteStatus("unit" [, "channel"]) or GetMuteStatus("name" [, "channel"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a character to query (`string`)
- `channel` - Name of a voice channel (`string`)

**Returns:**

- `muteStatus` - 1 if the character is muted; otherwise nil (`1nil`)

---

## GetPlayerInfoByGUID

Returns information about a player character identified by globally unique identifier. Returns `nil` if given the GUID of a non-player unit. The leading 0x may be omitted.

**Signature:**

```lua
class, classFilename, race, raceFilename, sex, name, realm = GetPlayerInfoByGUID("guid")
```

**Arguments:**

- `guid` - Globally unique identifier of a player unit (`string`, [guid](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#guid))

**Returns:**

- `class` - Localized name of the unit's class (`string`)
- `classFilename` - Non-localized token identifying the unit's class (`string`)
- `race` - Localized name of the unit's race (`string`)
- `raceFilename` - Non-localized token identifying the unit's race (`string`)
- `sex` - Number identifying the unit's gender (`number`)
  - `1` - Neuter / Unknown
  - `2` - Male
  - `3` - Female
- `name` - Unit's name (`string`)
- `realm` - Unit's realm (empty string if from the same realm) (`string`)

---

## GetUnitName `blizzardui`

Returns a string summarizing a unit's name and server

**Signature:**

```lua
nameString = GetUnitName("unit", showServerName)
```

**Arguments:**

- `unit` - Unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `showServerName` - True to include the server name in the return value if the unit is not from the same server as the player; false to only include a short label in such circumstances (`boolean`)

**Returns:**

- `nameString` - The unit's name, possibly followed by the name of the unit's home server or a label indicating the unit is not from the player's server (`string`)

---

## GetUnitSpeed

Returns a unit's current speed. Valid for all observable units. Values returned indicate the current movement speed in yards per second. (It's not relative to facing or ground position; i.e. you won't see a smaller value when flying up at an angle or a negative value when backing up.) Does not indicate falling speed or the speed of boats, zeppelins, and some forms of quest-related transportation, but does indicate current speed on taxi flights and when moving due to combat effects such as Disengage, Death Grip, or various knockback abilities.

Examples: Normal running: 7; Walking: 2.5; Running backwards: 4.5; Epic flying mount: 26.6

**Signature:**

```lua
speed = GetUnitSpeed(unit)
```

**Arguments:**

- `unit` - Unit to query (`unitid`)

**Returns:**

- `speed` - Unit's current speed in yards per second (`number`)

---

## IsIgnoredOrMuted

Returns whether a unit can be heard due to ignored/muted status

**Signature:**

```lua
isIgnoredOrMuted = IsIgnoredOrMuted("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20111212154639/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isIgnoredOrMuted` - 1 if the unit is ignored or muted, nil otherwise (`1nil`)

---

## IsMuted

Returns whether a character has been muted by the player

**Signature:**

```lua
muted = IsMuted("unit") or IsMuted("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `muted` - 1 if the unit is muted; otherwise nil (`1nil`)

---

## IsUnitOnQuest

Checks if a specified unit is on a quest from the players quest log.

**Signature:**

```lua
state = IsUnitOnQuest(index, "unit")
```

**Arguments:**

- `index` - The quest index to query. (`number`)
- `unit` - The name of the unit to query. (`string`)

**Returns:**

- `state` - 1 if the unit is on that quest, nil otherwise (`1nil`)

---

## SetPortraitTexture

Sets a Texture object to show a portrait of a unit. Causes the client to render a view of the unit's model from a standard perspective into a circular 2D image and display it in the given Texture object.

**Signature:**

```lua
SetPortraitTexture(texture, "unit")
```

**Arguments:**

- `texture` - A Texture object (`table`)
- `unit` - A unit for which to display a portrait (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

---

## UnitAffectingCombat

Returns whether a unit is currently in combat

**Signature:**

```lua
inCombat = UnitAffectingCombat("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `inCombat` - 1 if the unit is currently involved in combat; otherwise nil (`1nil`)

---

## UnitAura

Returns information about buffs/debuffs on a unit

**Signature:**

```lua
name, rank, icon, count, dispelType, duration, expires, caster, isStealable, nameplateShowPersonal, spellID, canApplyAura, isBossDebuff, _, nameplateShowAll, timeMod, value1, value2, value3 = UnitAura("unit", index [, "filter"]) or UnitAura("unit", "name", "rank" [, "filter"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player. Defaults to 'HELPFUL' (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `HARMFUL` - Show debuffs only
  - `HELPFUL` - Show buffs only (default)
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - When used with a HELPFUL filter it will show auras the player can cast on party/raid members (as opposed to self buffs). If used with a HARMFUL filter it will return debuffs the player can cure

**Returns:**

- `name` - Name of the aura (`string`)
- `rank` - Secondary text for the aura (often a rank; e.g. "Rank 7") (`string`)
- `icon` - Path to an icon texture for the aura (`string`)
- `count` - The number of times the aura has been applied (`number`)
- `dispelType` - Type of aura (relevant for dispelling and certain other mechanics); nil if not one of the following values: (`string`)
  - `Curse`
  - `Disease`
  - `Magic`
  - `Poison`
- `duration` - Total duration of the aura (in seconds). Zero if the unit is phased or out of range. (`number`)
- `expires` - Time at which the aura will expire; can be compared to [GetTime()](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) to determine time remaining. Zero if the unit is phased or out of range. (`number`)
- `caster` - Unit which applied the aura. If the aura was applied by a unit that does not have a token but is controlled by one that does (e.g. a totem or another player's vehicle), returns the controlling unit. Returns nil if the casting unit (or its controller) has no unitID. (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `isStealable` - true if the aura can be transferred to a player using the Spellsteal spell (`boolean`)
- `nameplateShowPersonal` - true if the aura should be visible above nameplates of affected targets, but only for the player that casted it (`boolean`)
- `spellID` - spellID of the aura (`number`)
- `canApplyAura` - true if the player can apply the aura (not necessarily if the player did apply the aura, just if the player can apply the aura). (`boolean`)
- `isBossDebuff` - true if the aura was cast by a boss. (`boolean`)
- `_` - unknown parameter (`boolean`)
- `nameplateShowAll` - true if the aura should be visible above nameplates of affected targets for all players (`boolean`)
- `timeMod` - the real time remaining on the aura is `(expirationTime - GetTime()) / timeMod`, likely used e.g. on Chronomatic Anomaly (`number`)
- `value1` - Value of variable effect 1 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value2` - Value of variable effect 2 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value3` - Value of variable effect 3 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)

---

## UnitBuff

Returns information about a buff on a unit. This function is an alias for [`UnitAura()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitAura) with a built-in `HELPFUL` filter (which cannot be removed or negated with the `HARMFUL` filter).

**Signature:**

```lua
name, rank, icon, count, dispelType, duration, expires, caster, isStealable, nameplateShowPersonal, spellID, canApplyAura, isBossDebuff, _, nameplateShowAll, timeMod, value1, value2, value3 = UnitBuff("unit", index [, "filter"]) or UnitBuff("unit", "name" [, "rank" [, "filter"]])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

**Returns:**

- `name` - Name of the aura (`string`)
- `rank` - Secondary text for the aura (often a rank; e.g. "Rank 7") (`string`)
- `icon` - Path to an icon texture for the aura (`string`)
- `count` - The number of times the aura has been applied (`number`)
- `dispelType` - Type of aura (relevant for dispelling and certain other mechanics); nil if not one of the following values: (`string`)
  - `Curse`
  - `Disease`
  - `Magic`
  - `Poison`
- `duration` - Total duration of the aura (in seconds). Zero if the unit is phased or out of range. (`number`)
- `expires` - Time at which the aura will expire; can be compared to [GetTime()](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) to determine time remaining. Zero if the unit is phased or out of range. (`number`)
- `caster` - Unit which applied the aura. If the aura was applied by a unit that does not have a token but is controlled by one that does (e.g. a totem or another player's vehicle), returns the controlling unit. Returns nil if the casting unit (or its controller) has no unitID. (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `isStealable` - true if the aura can be transferred to a player using the Spellsteal spell (`boolean`)
- `nameplateShowPersonal` - true if the aura should be visible above nameplates of affected targets, but only for the player that casted it (`boolean`)
- `spellID` - spellID of the aura (`number`)
- `canApplyAura` - true if the player can apply the aura (not necessarily if the player did apply the aura, just if the player can apply the aura). (`boolean`)
- `isBossDebuff` - true if the aura was cast by a boss. (`boolean`)
- `_` - unknown parameter (`boolean`)
- `nameplateShowAll` - true if the aura should be visible above nameplates of affected targets for all players (`boolean`)
- `timeMod` - the real time remaining on the aura is `(expirationTime - GetTime()) / timeMod`, likely used e.g. on Chronomatic Anomaly (`number`)
- `value1` - Value of variable effect 1 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value2` - Value of variable effect 2 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value3` - Value of variable effect 3 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)

---

## UnitCanAssist

Returns whether one unit can assist another

**Signature:**

```lua
canAssist = UnitCanAssist("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `canAssist` - 1 if the first unit can assist the second; otherwise nil (`1nil`)

---

## UnitCanAttack

Returns whether one unit can attack another

**Signature:**

```lua
canAttack = UnitCanAttack("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `canAttack` - 1 if the first unit can attack the second unit; otherwise nil (`1nil`)

---

## UnitCanCooperate

Returns whether two units can cooperate. Two units are considered to be able to cooperate with each other if they are of the same faction and are both players.

**Signature:**

```lua
canCooperate = UnitCanCooperate("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `canCooperate` - 1 if the two units can cooperate with each other; otherwise nil (`1nil`)

---

## UnitCastingInfo

Returns information about the spell a unit is currently casting

**Signature:**

```lua
name, subText, text, texture, startTime, endTime, isTradeSkill, castID, notInterruptible = UnitCastingInfo("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `name` - Name of the spell being cast (`string`)
- `subText` - Secondary text associated with the spell (e.g."Rank 5", "Racial", etc.) (`string`)
- `text` - Text to be displayed on a casting bar (`string`)
- `texture` - Path to an icon texture for the spell (`string`)
- `startTime` - Time at which the cast was started (in milliseconds; can be compared to [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) `* 1000`) (`number`)
- `endTime` - Time at which the cast will finish (in milliseconds; can be compared to [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) `* 1000`) (`number`)
- `isTradeSkill` - 1 if the spell being cast is a trade skill recipe; otherwise nil (`1nil`)
- `castID` - Reference number for this spell; matches the 4th argument of `UNIT_SPELLCAST_*` events for the same spellcast (`number`)
- `notInterruptible` - 1 if the spell can be interrupted; otherwise nil. See the [`UNIT_SPELLCAST_NOT_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_NOT_INTERRUPTIBLE) and [`UNIT_SPELLCAST_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_INTERRUPTIBLE) events for changes to this status. (`1nil`)

---

## UnitChannelInfo

Returns information about the spell a unit is currently channeling

**Signature:**

```lua
name, subText, text, texture, startTime, endTime, isTradeSkill, notInterruptible = UnitChannelInfo("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `name` - Name of the spell being cast (`string`)
- `subText` - Secondary text associated with the spell (e.g."Rank 5", "Racial", etc.) (`string`)
- `text` - Text to be displayed on a casting bar (`string`)
- `texture` - Path to an icon texture for the spell (`string`)
- `startTime` - Time at which the cast was started (in milliseconds; can be compared to [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) `* 1000`) (`number`)
- `endTime` - Time at which the cast will finish (in milliseconds; can be compared to [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) `* 1000`) (`number`)
- `isTradeSkill` - 1 if the spell being cast is a trade skill recipe; otherwise nil (`1nil`)
- `notInterruptible` - Indicates that the spell cannot be interrupted, [`UNIT_SPELLCAST_NOT_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_NOT_INTERRUPTIBLE) and [`UNIT_SPELLCAST_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_INTERRUPTIBLE) are fired to indicate changes in the interruptible status. (`boolean`)

---

## UnitClass

Returns a unit's class. The second return (`classFileName`) can be used for locale-independent verification of a unit's class, or to look up class-related data in various global tables:

- `RAID_CLASS_COLORS` provides a standard color for each class (as seen in the default who, guild, calendar, and raid UIs)
- `CLASS_ICON_TCOORDS` provides coordinates to locate each class' icon within the "Interface\Glues\CharacterCreate\UI-CharacterCreate-Classes" texture

For non-player units, the first return (`class`) will be the unit's name; to always get a localized class name regardless of unit type, use [`UnitClassBase`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitClassBase) instead.

**Signature:**

```lua
class, classFileName, classIndex = UnitClass("unit") or UnitClass("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `class` - The localized name of the unit's class, or the unit's name if the unit is an NPC (`string`)
- `classFileName` - A non-localized token representing the class (`string`)
- `classIndex` - ID of the class (`number`)

---

## UnitClassBase

Returns a unit's class. The second return (`classFileName`) can be used for locale-independent verification of a unit's class, or to look up class-related data in various global tables:

- `RAID_CLASS_COLORS` provides a standard color for each class (as seen in the default who, guild, calendar, and raid UIs)
- `CLASS_ICON_TCOORDS` provides coordinates to locate each class' icon within the "Interface\Glues\CharacterCreate\UI-CharacterCreate-Classes" texture

Unlike [`UnitClass`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitClass), this function returns the same values for NPCs as for players.

**Signature:**

```lua
class, classFileName = UnitClassBase("unit") or UnitClassBase("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `class` - The localized name of the unit's class (`string`)
- `classFileName` - A non-localized token representing the class (`string`)

---

## UnitClassification

Returns a unit's classification

**Signature:**

```lua
classification = UnitClassification("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `classification` - Classification of the unit (`string`)
  - `elite` - Elite
  - `minus` - Minion of another NPC; does not give experience or reputation.
  - `normal` - Normal
  - `rare` - Rare
  - `rareelite` - Rare-Elite
  - `trivial` - Trivial
  - `worldboss` - World Boss

---

## UnitCreatureFamily

Returns the creature family of the unit. Applies only to beasts of the kinds that can be taken as Hunter pets (e.g. cats, worms, and ravagers but not zhevras, talbuks and pterrordax), demons of the types that can be summoned by Warlocks (e.g. imps and felguards, but not demons that require enslaving such as infernals and doomguards or world demons such as pit lords and armored voidwalkers) and Death Knight's pets (ghouls).

**Signature:**

```lua
family = UnitCreatureFamily("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `family` - Localized name of the subtype of creature (e.g. Bear, Devilsaur, Voidwalker, Succubus), or nil if not applicable (`string`)

---

## UnitCreatureType

Returns the creature type of a unit. Note that some creatures have no type (e.g. slimes).

**Signature:**

```lua
type = UnitCreatureType("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `type` - Localized name of the type of creature (e.g. Beast, Humanoid, Undead), or nil if not applicable (`string`)

---

## UnitDebuff

Returns information about a debuff on a unit. This function is an alias for [`UnitAura()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitAura) with a built-in `HARMFUL` filter (which cannot be removed or negated with the `HELPFUL` filter).

**Signature:**

```lua
name, rank, icon, count, dispelType, duration, expires, caster, isStealable, nameplateShowPersonal, spellID, canApplyAura, isBossDebuff, _, nameplateShowAll, timeMod, value1, value2, value3 = UnitDebuff("unit", index [, "filter"]) or UnitDebuff("unit", "name" [, "rank" [, "filter"]])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"CANCELABLE|PLAYER"` will query cancelable debuffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

**Returns:**

- `name` - Name of the aura (`string`)
- `rank` - Secondary text for the aura (often a rank; e.g. "Rank 7") (`string`)
- `icon` - Path to an icon texture for the aura (`string`)
- `count` - The number of times the aura has been applied (`number`)
- `dispelType` - Type of aura (relevant for dispelling and certain other mechanics); nil if not one of the following values: (`string`)
  - `Curse`
  - `Disease`
  - `Magic`
  - `Poison`
- `duration` - Total duration of the aura (in seconds). Zero if the unit is phased or out of range. (`number`)
- `expires` - Time at which the aura will expire; can be compared to [GetTime()](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) to determine time remaining. Zero if the unit is phased or out of range. (`number`)
- `caster` - Unit which applied the aura. If the aura was applied by a unit that does not have a token but is controlled by one that does (e.g. a totem or another player's vehicle), returns the controlling unit. Returns nil if the casting unit (or its controller) has no unitID. (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `isStealable` - true if the aura can be transferred to a player using the Spellsteal spell (`boolean`)
- `nameplateShowPersonal` - true if the aura should be visible above nameplates of affected targets, but only for the player that casted it (`boolean`)
- `spellID` - spellID of the aura (`number`)
- `canApplyAura` - true if the player can apply the aura (not necessarily if the player did apply the aura, just if the player can apply the aura). (`boolean`)
- `isBossDebuff` - true if the aura was cast by a boss. (`boolean`)
- `_` - unknown parameter (`boolean`)
- `nameplateShowAll` - true if the aura should be visible above nameplates of affected targets for all players (`boolean`)
- `timeMod` - the real time remaining on the aura is `(expirationTime - GetTime()) / timeMod`, likely used e.g. on Chronomatic Anomaly (`number`)
- `value1` - Value of variable effect 1 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value2` - Value of variable effect 2 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value3` - Value of variable effect 3 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)

---

## UnitExists

Returns whether a unit exists. A unit "exists" if it can be referenced by the player; e.g. `party1` exists if the player is in a party with at least one other member (regardless of whether that member is nearby), `target` exists if the player has a target, `npc` exists if the player is currently interacting with an NPC, etc.

**Signature:**

```lua
exists = UnitExists("unit") or UnitExists("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, `npc`, and party/raid members (`string`)

**Returns:**

- `exists` - 1 if the unit exists, otherwise nil (`1nil`)

---

## UnitFactionGroup

Returns a unit's primary faction allegiance

**Signature:**

```lua
factionGroup, factionName = UnitFactionGroup("unit") or UnitFactionGroup("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `factionGroup` - Non-localized (English) faction name of the faction (`'Horde'`, `'Alliance'`, or `'Neutral'`) (`string`)
- `factionName` - Localized name of the faction (`string`)

---

## UnitGUID

Returns a unit's globally unique identifier

**Signature:**

```lua
guid = UnitGUID("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `guid` - The unit's GUID (`string`, [guid](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#guid))

---

## UnitHasRelicSlot

Returns whether a unit has a relic slot instead of a ranged weapon slot

**Signature:**

```lua
hasRelic = UnitHasRelicSlot("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `hasRelic` - 1 if the unit has a relic slot; otherwise nil (`1nil`)

---

## UnitHealth

Returns a unit's current amount of health

**Signature:**

```lua
health = UnitHealth("unit") or UnitHealth("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `health` - The unit's current amount of health (hit points) (`number`)

---

## UnitHealthMax

Returns a unit's maximum health value

**Signature:**

```lua
maxValue = UnitHealthMax("unit") or UnitHealthMax("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `maxValue` - The unit's maximum health (hit points) (`number`)

---

## UnitInBattleground

Returns whether a unit is in same battleground instance as the player

**Signature:**

```lua
raidNum = UnitInBattleground("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `raidNum` - Numeric portion of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) (e.g. 13 for `raid13`) (`number`)

---

## UnitInParty

Returns whether a unit is a player unit in the player's party. Always returns 1 for the `player` unit. Returns nil for the player's or party members' pets.

**Signature:**

```lua
inParty = UnitInParty("unit") or UnitInParty("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `inParty` - 1 if the unit is a player unit in the player's party; otherwise nil. (`1nil`)

---

## UnitInRaid

Returns whether a unit is in the player's raid

**Signature:**

```lua
inRaid = UnitInRaid("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `inRaid` - Index of the unit in the raid (matches the numeric part of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) minus 1; e.g. returns 0 for `raid1`, 12 for `raid13`, etc) (`number`)

---

## UnitInRange

Returns whether a party/raid member is nearby. The range check used by this function isn't directly based on the player's abilities (which may have varying ranges); it's fixed by Blizzard at a distance of around 40 yards (which encompasses many common healing spells and other abilities often used on raid members).

Also returns nil for units outside the player's area of view.

**Signature:**

```lua
inRange = UnitInRange("unit") or UnitInRange("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for party/raid members and their pets (`string`)

**Returns:**

- `inRange` - 1 if the unit is close enough to the player to (likely) be in range for helpful spells; otherwise nil (`1nil`)

---

## UnitIsAFK

Returns whether a unit is marked AFK (Away From Keyboard)

**Signature:**

```lua
isAFK = UnitIsAFK("unit") or UnitIsAFK("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `isAFK` - 1 if the unit is AFK; otherwise nil (`1nil`)

---

## UnitIsCharmed

Returns whether a unit is currently charmed. A charmed unit is affected by Mind Control (or a similar effect) and thus hostile to units which are normally his or her allies.

**Signature:**

```lua
isCharmed = UnitIsCharmed("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isCharmed` - 1 if the unit is charmed; otherwise nil (`1nil`)

---

## UnitIsConnected

Returns whether a unit is connected (i.e. not Offline)

**Signature:**

```lua
isConnected = UnitIsConnected("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isConnected` - 1 if the player is connected; otherwise nil (`1nil`)

---

## UnitIsControlling

Returns whether a unit is controlling another unit. Applies to Mind Control and similar cases as well as to players piloting vehicles.

**Signature:**

```lua
isControlling = UnitIsControlling("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isControlling` - 1 if the unit is controlling another unit; otherwise nil (`1nil`)

---

## UnitIsCorpse

Returns whether a unit is a corpse

**Signature:**

```lua
isCorpse = UnitIsCorpse("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isCorpse` - 1 if the unit is a corpse; otherwise nil (`1nil`)

---

## UnitIsDND

Returns whether a unit is marked DND (Do Not Disturb)

**Signature:**

```lua
isDND = UnitIsDND("unit") or UnitIsDND("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `isDND` - 1 if the unit is marked Do Not Disturb, otherwise nil (`1nil`)

---

## UnitIsDead

Returns whether a unit is dead. Only returns 1 while the unit is dead and has not yet released his or her spirit. See [`UnitIsGhost()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitIsGhost) for after the unit has released.

**Signature:**

```lua
isDead = UnitIsDead("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isDead` - 1 if the unit is dead; otherwise nil (`1nil`)

---

## UnitIsDeadOrGhost

Returns whether a unit is either dead or a ghost

**Signature:**

```lua
isDeadOrGhost = UnitIsDeadOrGhost("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isDeadOrGhost` - 1 if the unit is dead or a ghost, otherwise nil (`1nil`)

---

## UnitIsEnemy

Returns whether two units are enemies

**Signature:**

```lua
isEnemy = UnitIsEnemy("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isEnemy` - 1 if the units are enemies; otherwise nil (`1nil`)

---

## UnitIsFeignDeath

Returns whether a unit is feigning death. Only provides valid data for friendly units.

**Signature:**

```lua
isFeign = UnitIsFeignDeath("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isFeign` - 1 if the unit is feigning death; otherwise nil (`1nil`)

---

## UnitIsFriend

Returns whether two units are friendly

**Signature:**

```lua
isFriends = UnitIsFriend("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isFriends` - 1 if the two units are friendly; otherwise nil (`1nil`)

---

## UnitIsGhost

Returns whether a unit is currently a ghost

**Signature:**

```lua
isGhost = UnitIsGhost("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isGhost` - 1 if the unit is a ghost; otherwise nil (`1nil`)

---

## UnitIsInMyGuild

Returns whether a unit is in the player's guild

**Signature:**

```lua
inGuild = UnitIsInMyGuild("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `inGuild` - 1 if the unit is in the player's guild; otherwise nil (`1nil`)

---

## UnitIsPVP

Returns whether a unit is flagged for PvP activity

**Signature:**

```lua
isPVP = UnitIsPVP("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isPVP` - 1 if the unit is flagged for PVP activity; otherwise nil (`1nil`)

---

## UnitIsPVPFreeForAll

Returns whether a unit is flagged for free-for-all PvP. Free-for-all PvP allows all players to attack each other regardless of faction; used in certain outdoor areas (such as Gurubashi Arena and "The Maul" outside Dire Maul).

**Signature:**

```lua
isFreeForAll = UnitIsPVPFreeForAll("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

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

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `state` - 1 if the unit is in a PVP Sanctuary; otherwise nil (`1nil`)

---

## UnitIsPartyLeader

Returns whether a unit is the leader of the player's party

**Signature:**

```lua
leader = UnitIsPartyLeader("unit") or UnitIsPartyLeader("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `leader` - 1 if the unit is the party leader; otherwise nil (`1nil`)

---

## UnitIsPlayer

Returns whether a unit is a player unit (not an NPC)

**Signature:**

```lua
isPlayer = UnitIsPlayer("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isPlayer` - true if the unit is a player unit; otherwise false (`boolean`)

---

## UnitIsPossessed

Returns whether a unit is possessed by another

**Signature:**

```lua
isPossessed = UnitIsPossessed("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isPossessed` - 1 if the given unit is possessed; otherwise nil (`1nil`)

---

## UnitIsRaidOfficer

Returns whether a unit is a raid assistant in the player's raid

**Signature:**

```lua
leader = UnitIsRaidOfficer("unit") or UnitIsRaidOfficer("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `leader` - 1 if the unit is a raid assistant; otherwise nil (`1nil`)

---

## UnitIsSameServer

Returns whether two units are from the same server

**Signature:**

```lua
isSame = UnitIsSameServer("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isSame` - 1 if the two units are from the same server; otherwise nil. (`1nil`)

---

## UnitIsTapped

Returns whether a unit is tapped. Normally, rewards for killing a unit are available only to the character or group who first damaged the unit; once a character has thus established his claim on the unit, it is considered "tapped".

**Signature:**

```lua
UnitIsTapped(unit)
```

**Arguments:**

- `unit` - The unitid to query (`unitId`)

---

## UnitIsTappedByAllThreatList

Returns whether a unit allows all players on its threat list to receive kill credit. Used to override the normal "tapping" behavior for certain mobs -- if this function returns 1, the player does not have to be the first to attack the mob (or in the same party/raid as the first player to attack) in order to receive quest or achievement credit for killing it.

In the default UI, this function can prevent the graying of a unit's name background in the TargetFrame and FocusFrame even if the unit is otherwise tapped, indicating that kill credit is still available if the player attacks.

**Signature:**

```lua
allTapped = UnitIsTappedByAllThreatList("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `allTapped` - 1 if the unit allows all players on its threat list to receive kill credit; otherwise nil (`1nil`)

---

## UnitIsTappedByPlayer

Returns whether a unit is tapped by the player or the player's group. Normally, rewards for killing a unit are available only to the character or group who first damaged the unit; once a character has thus established his claim on the unit, it is considered "tapped".

**Signature:**

```lua
isTapped = UnitIsTappedByPlayer("unit")
```

**Arguments:**

- `unit` - The unit to be queried (`string`)

**Returns:**

- `isTapped` - 1 if the unit is tapped by the player; otherwise nil (`1nil`)

---

## UnitIsTrivial

Returns whether a unit is trivial at the player's level. Killing trivial units (whose level is colored gray in the default UI) does not reward honor or experience.

**Signature:**

```lua
isTrivial = UnitIsTrivial("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isTrivial` - 1 if the unit is trivial at the player's level; otherwise nil (`1nil`)

---

## UnitIsUnit

Returns whether two unit references are to the same unit. Useful for determining whether a composite [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) (such as `raid19target`) also refers to a basic `unitID`; see example.

**Signature:**

```lua
isSame = UnitIsUnit("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isSame` - Returns 1 if the two references are to the same unit; otherwise nil (`1nil`)

---

## UnitIsVisible

Returns whether a unit is in the player's area of interest

**Signature:**

```lua
isVisible = UnitIsVisible("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isVisible` - 1 if the unit is is in the player's area of interest; otherwise nil (`1nil`)

---

## UnitLevel

Returns a unit's level. Returns -1 for boss units and hostile units whose level is ten levels or more above the player's.

**Signature:**

```lua
level = UnitLevel("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `level` - The unit's level (`number`)

---

## UnitMana `deprecated`

This function is deprecated and should no longer be used

---

## UnitManaMax `deprecated`

This function is deprecated and should no longer be used

---

## UnitName

Returns the name of a unit

**Signature:**

```lua
name, realm = UnitName("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `name` - Name of the unit (`string`)
- `realm` - Name of the unit's home realm if the unit is not from the player's realm; otherwise nil (`string`)

---

## UnitOnTaxi

Returns whether a unit is currently riding a flight path (taxi). Valid for any unit in the player's area of interest, but generally useful only for `player` -- taxi flights move quickly, so a taxi-riding unit visible to the player will not remain visible for very long.

**Signature:**

```lua
onTaxi = UnitOnTaxi("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `onTaxi` - 1 if the unit is on a taxi; otherwise nil (`1nil`)

---

## UnitPVPName

Returns the name of a unit including the unit's current title. Titles are no longer specific to PvP; this function returns a unit's name with whichever title he or she is currently displaying (e.g. "Gladiator Spin", "Keydar Jenkins", "Ownsusohard, Champion of the Frozen Wastes", etc).

**Signature:**

```lua
name = UnitPVPName("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

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

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `rank` - The numeric PvP rank of the unit, or 0 if the unit has no PvP rank (`number`)

---

## UnitPlayerControlled

Returns whether a unit is controlled by a player

**Signature:**

```lua
isPlayer = UnitPlayerControlled("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isPlayer` - 1 if the unit is controlled by a player; otherwise nil (`1nil`)

---

## UnitPlayerOrPetInParty

Returns whether a unit is in the player's party or belongs to a party member. Returns nil for the player and the player's pet.

**Signature:**

```lua
inParty = UnitPlayerOrPetInParty("unit") or UnitPlayerOrPetInParty("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `inParty` - 1 if the unit is in the player's party or is a pet belonging to a party member; otherwise nil (`1nil`)

---

## UnitPlayerOrPetInRaid

Returns whether a unit is in the player's raid or belongs to a raid member

**Signature:**

```lua
inParty = UnitPlayerOrPetInRaid("unit") or UnitPlayerOrPetInRaid("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `inParty` - 1 if the unit is in the player's raid or is a pet belonging to a raid member; otherwise nil (`1nil`)

---

## UnitPower

Returns a unit's current level of mana, rage, energy or other power type. Returns zero for non-existent units.

**Signature:**

```lua
power = UnitPower("unitID" [, powerType])
```

**Arguments:**

- `unitID` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `powerType` - A specific power type to query (`number`, [powerType](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#powerType))

**Returns:**

- `power` - The unit's current level of mana, rage, energy, runic power, or other power type (`number`)

---

## UnitPowerMax

Returns a unit's maximum mana, rage, energy or other power type. Returns the units current maximum power, if the unit does not exist then zero is returned. 
When querying with a powerType, as long as the unit exists you will get the maximum untalented power even if the class does not use the power type.

**Signature:**

```lua
maxValue = UnitPowerMax("unitID" [, powerType])
```

**Arguments:**

- `unitID` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `powerType` - Specific power type to query for the unit (`number`, [powerType](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#powerType))

**Returns:**

- `maxValue` - The unit's maximum mana, rage, energy, or other power (`number`)

---

## UnitPowerType

Returns the power type (energy, mana, rage) of the given unit. Does not return color values for common power types (mana, rage, energy, focus, and runic power); the canonical colors for these can be found in the `PowerBarColor` table. Color values may be included for special power types such as those used by vehicles.

**Signature:**

```lua
powerType, powerToken, altR, altG, altB = UnitPowerType("unit") or UnitPowerType("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `powerType` - A number identifying the power type (`number`)
  - `0` - Mana
  - `1` - Rage
  - `2` - Focus
  - `3` - Energy
  - `6` - Runic Power
- `powerToken` - The name of a global variable containing the localized name of the power type (`string`)
- `altR` - Red component of the color used for displaying this power type (`number`)
- `altG` - Green component of the color used for displaying this power type (`number`)
- `altB` - Blue component of the color used for displaying this power type (`number`)

---

## UnitRace

Returns the name of a unit's race

**Signature:**

```lua
race, fileName = UnitRace("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `race` - Localized name of the unit's race (`string`)
- `fileName` - A non-localized token representing the unit's race (`string`)

---

## UnitReaction

Returns the reaction of one unit with regards to another as a number. The returned value often (but not always) matches the unit's level of reputation with the second unit's faction, and can be used with the `UnitReactionColor` global table to return the color used to display a unit's reaction in the default UI.

**Signature:**

```lua
reaction = UnitReaction("unit", "unit")
```

**Arguments:**

- `unit` - A unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `unit` - Another unit (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `reaction` - Reaction of the first unit towards the second unit (`number`)
  - `1` - Hated
  - `2` - Hostile
  - `3` - Unfriendly
  - `4` - Neutral
  - `5` - Friendly
  - `6` - Honored
  - `7` - Revered
  - `8` - Exalted

---

## UnitSelectionColor

Returns a color indicating hostility and related status of a unit. This color is used in various places in the default UI, such as the background behind a unit's name in the target and focus frames. For NPCs, the color reflects hostility and reputation, ranging from red (hostile) to orange or yellow (unfriendly or neutral) to green (friendly). When the unit is a player, a blue color is used unless the player is active for PvP, in which case the color may be red (he can attack you and you can attack him), yellow (you can attack him but he can't attack you) or green (ally). Color component values are floating point numbers between 0 and 1.

**Signature:**

```lua
red, green, blue, alpha = UnitSelectionColor("unit") or UnitSelectionColor("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `red` - The red component of the color. (`number`)
- `green` - The green component of the color. (`number`)
- `blue` - The blue component of the color. (`number`)
- `alpha` - The alpha (opacity) component of the color. (`number`)

---

## UnitSex

Returns the gender of the given unit or player

**Signature:**

```lua
gender = UnitSex("unit") or UnitSex("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `gender` - The unit's gender (`number`)
  - `1` - Neuter / Unknown
  - `2` - Male
  - `3` - Female

---

## UnitUsingVehicle

Returns whether a unit is using a vehicle. Unlike similar functions, `UnitUsingVehicle()` also returns `true` while the unit is transitioning between seats in a vehicle.

**Signature:**

```lua
usingVehicle = UnitUsingVehicle("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `usingVehicle` - `1` if the unit is using a vehicle; otherwise `nil` (`1nil`)

---

← [WoW API Docs](../index.md)
