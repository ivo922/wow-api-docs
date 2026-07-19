# CombatLog functions

← [WoW API Docs](../index.md)

**12** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#combatlog)

---

## CombatLogAddFilter

Adds a filter to the combat log system. Each time this function is called a new filter is added to the combat log system. Any combat log entry that passes the filter will be fired as a [`COMBAT_LOG_EVENT`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/event/COMBAT_LOG_EVENT) event in order from oldest to newest.

**Signature:**

```lua
CombatLogAddFilter("events", "srcGUID", ["destGUID"] or [destMask]) or CombatLogAddFilter("events", srcMask, ["destGUID"] or [destMask]) or CombatLogAddFilter("events", ["srcGUID"] or [srcMask], "destGUID") or CombatLogAddFilter("events", ["srcGUID"] or [srcMask], destMask)
```

**Arguments:**

- `events` - Name of a combat log event type to include in the filtered list, or a comma-separated list of multiple names (`string`)
- `srcGUID` - GUID of the source unit (`string`, [guid](../types/guid.md))
- `srcMask` - Bit mask of the source unit (`number`, [bitfield](../types/bitfield.md))
- `destGUID` - GUID of the destination unit (`string`, [guid](../types/guid.md))
- `destMask` - Bit mask of the destination unit (`number`, [bitfield](../types/bitfield.md))

---

## CombatLogAdvanceEntry

Advances the "cursor" position used by other CombatLog functions. Information about the entry at the "cursor" position can be retrieved with [`CombatLogGetCurrentEntry()`](CombatLog.md#combatloggetcurrententry). That function then advances the cursor to the next entry, so calling it repeatedly returns all information in the combat log -- this function can be used to "rewind" the combat log to retrieve information about earlier events or skip entries without retrieving their information.

**Signature:**

```lua
hasEntry = CombatLogAdvanceEntry(count, ignoreFilter)
```

**Arguments:**

- `count` - Number of entries by which to advance the "cursor"; can be negative to move to a previous entry (`number`)
- `ignoreFilter` - True to use the entire saved combat log history; false or omitted to use only events matching the current filter (`boolean`)

**Returns:**

- `hasEntry` - 1 if an entry exists at the new cursor position; otherwise nil (`1nil`)

---

## CombatLogClearEntries

Removes all entries from the combat log

**Signature:**

```lua
CombatLogClearEntries()
```

---

## CombatLogGetCurrentEntry

Returns the combat log event information for the current entry and advances to the next entry. See [`COMBAT_LOG_EVENT`](https://web.archive.org/web/20111212190929/http://wowprogramming.com/docs/event/COMBAT_LOG_EVENT) for details of the event information.

The combat log maintains a "cursor" in the list of entries; this function returns information about the event at the cursor position and advances the cursor to the next entry. Since this function is used by the default UI's combat log display, the cursor position is usually at the end of the log -- calling it thus returns nothing. The function [`CombatLogSetCurrentEntry()`](CombatLog.md#combatlogsetcurrententry) can be used to "rewind" the combat log cursor, enabling retrieval of information about earlier events.

**Signature:**

```lua
timestamp, event, srcGUID, srcName, srcFlags, destGUID, destName, destFlags, ... = CombatLogGetCurrentEntry([ignoreFilter])
```

**Arguments:**

- `ignoreFilter` - True to use the entire saved combat log history; false or omitted to use only events matching the current filter (`boolean`)

**Returns:**

- `timestamp` - Time at which the event occurred (same format as [`time()`](Lua library.md#time-luaapi) and [`date()`](Lua library.md#date-luaapi), but with millisecond precision) (`number`)
- `event` - Type of combat log event (`string`)
- `srcGUID` - GUID of the unit that initiated the event (`string`, [guid](../types/guid.md))
- `srcName` - Name of the unit that initiated the event (`string`)
- `srcFlags` - Flags indicating the nature of the source unit (`number`, [bitfield](../types/bitfield.md))
- `destGUID` - GUID of the unit that was the target of the event (`string`, [guid](../types/guid.md))
- `destName` - Name of the unit that was the target of the event (`string`)
- `destFlags` - Flags indicating the nature of the target unit (`number`, [bitfield](../types/bitfield.md))
- `...` - Additional arguments specific to the event type (`list`)

---

## CombatLogGetNumEntries

Returns the number of available combat log events

**Signature:**

```lua
CombatLogGetNumEntries(ignoreFilter)
```

**Arguments:**

- `ignoreFilter` - True to use the entire saved combat log history; false or omitted to use only events matching the current filter (`boolean`)

---

## CombatLogGetRetentionTime

Returns the amount of time combat log entries are stored

**Signature:**

```lua
seconds = CombatLogGetRetentionTime()
```

**Returns:**

- `seconds` - Amount of time entries remain available (`number`)

---

## CombatLogResetFilter

Removes any filters applied to the combat log

**Signature:**

```lua
CombatLogResetFilter()
```

---

## CombatLogSetCurrentEntry

Sets the "cursor" position used by other CombatLog functions. Information about the entry at the "cursor" position can be retrieved with [`CombatLogGetCurrentEntry()`](CombatLog.md#combatloggetcurrententry). That function then advances the cursor to the next entry, so calling it repeatedly returns all information in the combat log -- this function can be used to "rewind" the combat log to retrieve information about earlier events.

The argument `index` can be positive or negative: positive indices start at the beginning of the combat log (oldest events) and count up to the end (newest events); negative indices start at `-1` for the newest event and count backwards to to `-`[`CombatLogGetNumEntries(ignoreFilter)`](CombatLog.md#combatloggetnumentries) for the oldest.

**Signature:**

```lua
CombatLogSetCurrentEntry(index [, ignoreFilter])
```

**Arguments:**

- `index` - Index of a combat log event (between `1` and [`CombatLogGetNumEntries(ignoreFilter)`](CombatLog.md#combatloggetnumentries), or between `-1` and `-`[`CombatLogGetNumEntries(ignoreFilter)`](CombatLog.md#combatloggetnumentries)) (`number`)
- `ignoreFilter` - True to use the entire saved combat log history; false or omitted to use only events matching the current filter (`boolean`)

---

## CombatLogSetRetentionTime

Sets the amount of time combat log entries will be stored

**Signature:**

```lua
CombatLogSetRetentionTime(seconds)
```

**Arguments:**

- `seconds` - The desired time (`number`)

---

## CombatLog_Object_IsA

Returns whether an entity from the combat log matches a given filter

**Signature:**

```lua
isMatch = CombatLog_Object_IsA(unitFlags, mask)
```

**Arguments:**

- `unitFlags` - Source or destination unit flags from a combat log entry (`number`, [bitfield](../types/bitfield.md))
- `mask` - One of the following global constants: (`number`, [bitfield](../types/bitfield.md))
  - `COMBATLOG_FILTER_EVERYTHING` - Any entity
  - `COMBATLOG_FILTER_FRIENDLY_UNITS` - Entity is a friendly unit
  - `COMBATLOG_FILTER_HOSTILE_PLAYERS` - Entity is a hostile player unit
  - `COMBATLOG_FILTER_HOSTILE_UNITS` - Entity is a hostile non-player unit
  - `COMBATLOG_FILTER_ME` - Entity is the player
  - `COMBATLOG_FILTER_MINE` - Entity is a non-unit object belonging to the player; e.g. a totem
  - `COMBATLOG_FILTER_MY_PET` - Entity is the player's pet
  - `COMBATLOG_FILTER_NEUTRAL_UNITS` - Entity is a neutral unit
  - `COMBATLOG_FILTER_UNKNOWN_UNITS` - Entity is a unit currently unknown to the WoW client

**Returns:**

- `isMatch` - 1 if the entity flags match the given mask (`1nil`)

---

## LoggingCombat

Enables or disables saving combat log data to a file. Combat log data will be saved to the file `Logs/WoWCombatLog.txt` (path is relative to the folder containing the World of Warcraft client); the file is not actually updated until the player logs out.

**Signature:**

```lua
isLogging = LoggingCombat(toggle)
```

**Arguments:**

- `toggle` - True to enable combat logging; false or omitted to disable (`boolean`)

**Returns:**

- `isLogging` - 1 if combat logging is enabled; otherwise nil (`1nil`)

**Examples:**

```lua
-- example log file contents
6/7 17:08:46.784  SPELL_CAST_SUCCESS,0x060000000279E425,"Gundark",0x511,0xF13000482C5462D1,"Timber Worg",0x10a48,49576,"Death Grip",0x1
6/7 17:08:47.089  SPELL_AURA_APPLIED,0x060000000279E425,"Gundark",0x511,0xF13000482C5462D1,"Timber Worg",0x10a48,49560,"Death Grip",0x1,DEBUFF
6/7 17:08:47.886  SWING_DAMAGE,0x060000000279E425,"Gundark",0x511,0xF13000482C5462D1,"Timber Worg",0x10a48,374,0,1,0,0,0,nil,nil,nil
6/7 17:08:47.887  SPELL_DAMAGE,0x060000000279E425,"Gundark",0x511,0xF13000482C5462D1,"Timber Worg",0x10a48,50401,"Razor Frost",0x10,5,0,16,0,0,0,nil,nil,nil
6/7 17:08:47.887  SPELL_AURA_APPLIED,0x060000000279E425,"Gundark",0x511,0xF13000482C5462D1,"Timber Worg",0x10a48,51714,"Frost Vulnerability",0x10,DEBUFF
6/7 17:08:48.207  SPELL_CAST_SUCCESS,0x060000000279E425,"Gundark",0x511,0xF13000482C5462D1,"Timber Worg",0x10a48,49896,"Icy Touch",0x10
6/7 17:08:48.327  SWING_MISSED,0xF13000482C5462D1,"Timber Worg",0x10a48,0x060000000279E425,"Gundark",0x511,DODGE
6/7 17:08:48.328  SPELL_PERIODIC_HEAL,0x060000000279E425,"Gundark",0x511,0x060000000279E425,"Gundark",0x511,50475,"Blood Presence",0x1,15,15,nil
```

---

## UnitGUID

Returns a unit's globally unique identifier

**Signature:**

```lua
guid = UnitGUID("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `guid` - The unit's GUID (`string`, [guid](../types/guid.md))

---

← [WoW API Docs](../index.md)
