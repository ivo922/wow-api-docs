# Faction functions

← [WoW API Docs](../index.md)

**14** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#faction)

---

## CollapseAllFactionHeaders

Collapses all headers and sub-headers in the Reputation UI. This function works for both major groups (Classic, Burning Crusade, Wrath of the Lich King, Inactive, etc.) and the sub-groups within them (Alliance Forces, Steamwheedle Cartel, Horde Expedition, Shattrath City, etc.).

**Signature:**

```lua
CollapseAllFactionHeaders()
```

---

## CollapseFactionHeader

Collapses a given faction header or sub-header in the Reputation UI.

Faction headers include both major groups (Classic, Burning Crusade, Wrath of the Lich King, Inactive, etc.) and the sub-groups within them (Alliance Forces, Steamwheedle Cartel, Horde Expedition, Shattrath City, etc.).

**Signature:**

```lua
CollapseFactionHeader(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## ExpandAllFactionHeaders

Expands all headers and sub-headers in the Reputation UI. Expands headers for both major groups (Classic, Burning Crusade, Wrath of the Lich King, Inactive, etc.) and the sub-groups within them (Alliance Forces, Steamwheedle Cartel, Horde Expedition, Shattrath City, etc.).

**Signature:**

```lua
ExpandAllFactionHeaders()
```

---

## ExpandFactionHeader

Expands a given faction header or sub-header in the Reputation UI.

Faction headers include both major groups (Classic, Burning Crusade, Wrath of the Lich King, Inactive, etc.) and the sub-groups within them (Alliance Forces, Steamwheedle Cartel, Horde Expedition, Shattrath City, etc.).

**Signature:**

```lua
ExpandFactionHeader(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## FactionToggleAtWar

Toggles "at war" status for a faction.

"At War" status determines whether members of a faction can be attacked. Normal interactions (as with merchants, questgivers, etc.) are not available if the player is "at war" with an NPC's faction.

This function does nothing for faction headers or factions for which changing "at war" status is not currently allowed; i.e., factions for which the eighth (`canToggleAtWar`) return of `GetFactionInfo `is false or nil.

**Signature:**

```lua
FactionToggleAtWar(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## GetFactionInfo

Returns information about a faction or header listing

**Signature:**

```lua
name, description, standingID, barMin, barMax, barValue, atWarWith, canToggleAtWar, isHeader, isCollapsed, hasRep, isWatched, isChild = GetFactionInfo(index)
```

**Arguments:**

- `index` - The index of the faction in the Reputation window (`number`)

**Returns:**

- `name` - Name of the faction (`string`)
- `description` - Brief description of the faction, as displayed in the default UI's detail window for a selected faction (`string`)
- `standingID` - Current standing with the given faction (`number`, [standingID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#standingID))
  - `1` - Hated
  - `2` - Hostile
  - `3` - Unfriendly
  - `4` - Neutral
  - `5` - Friendly
  - `6` - Honored
  - `7` - Revered
  - `8` - Exalted
- `barMin` - The minimum value of the reputation bar at the given standing (`number`)
- `barMax` - The maximum value of the reputation bar at the given standing (`number`)
- `barValue` - The player's current reputation with the faction (`number`)
- `atWarWith` - 1 if the player is at war with the given faction, otherwise nil (`1nil`)
- `canToggleAtWar` - 1 if the player can declare war with the given faction, otherwise nil (`1nil`)
- `isHeader` - 1 if the index refers to a faction group header (`1nil`)
- `isCollapsed` - 1 if the index refers to a faction group header and currently collapsed (`1nil`)
- `hasRep` - 1 if the index refers to a faction group header whose reputation value should be displayed (`1nil`)
- `isWatched` - 1 if the faction is currently being watched (i.e. displayed above the experience bar) (`1nil`)
- `isChild` - 1 if the index refers to a faction sub-group header within another group, or to an individual faction within a sub-group (`1nil`)

---

## GetNumFactions

Returns the number of entries in the reputation UI.

Entries in the reputation UI can be major group headers (Classic, Burning Crusade, Wrath of the Lich King, Inactive, etc.), the sub-group headers within them (Alliance Forces, Steamwheedle Cartel, Horde Expedition, Shattrath City, etc.), or individual factions (Darkmoon Faire, Orgrimmar, Honor Hold, Kirin Tor, etc.).

This function returns not the total number of factions (and headers) known, but the number which should currently be visible in the UI according to the expanded/collapsed state of headers.

**Signature:**

```lua
numFactions = GetNumFactions()
```

**Returns:**

- `numFactions` - The number of visible factions and headers (`number`)

---

## GetSelectedFaction

Returns which faction entry is selected in the reputation UI.

Selection has no bearing on other faction-related APIs; this function merely facilitates behaviors of Blizzard's reputation UI.

**Signature:**

```lua
index = GetSelectedFaction()
```

**Returns:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## GetWatchedFactionInfo

Returns information about the "watched" faction (displayed on the XP bar in the default UI)

**Signature:**

```lua
name, standingID, barMin, barMax, barValue = GetWatchedFactionInfo()
```

**Returns:**

- `name` - Name of the faction being watched (`string`)
- `standingID` - The player's current standing with the faction (`number`, [standingID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#standingID))
  - `1` - Hated
  - `2` - Hostile
  - `3` - Unfriendly
  - `4` - Neutral
  - `5` - Friendly
  - `6` - Honored
  - `7` - Revered
  - `8` - Exalted
- `barMin` - The minimum value for the faction status bar (`number`)
- `barMax` - The maximum value for the faction status bar (`number`)
- `barValue` - The current value for the faction status bar (`number`)

---

## IsFactionInactive

Returns whether a faction is flagged as "inactive". "Inactive" factions behave no differently; the distinction only exists to allow players to hide factions they don't care about from the main display. Factions thus marked are automatically moved to an "Inactive" group at the end of the faction list.

**Signature:**

```lua
isInactive = IsFactionInactive(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

**Returns:**

- `isInactive` - 1 if the faction is currently flagged as "inactive"; otherwise nil (`1nil`)

---

## SetFactionActive

Removes the "inactive" status from a faction. "Inactive" factions behave no differently; the distinction only exists to allow players to hide factions they don't care about from the main display. Factions thus marked are automatically moved to an "Inactive" group at the end of the faction list.

**Signature:**

```lua
SetFactionActive(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## SetFactionInactive

Flags a faction as inactive. "Inactive" factions behave no differently; the distinction only exists to allow players to hide factions they don't care about from the main display. Factions thus marked are automatically moved to an "Inactive" group at the end of the faction list.

**Signature:**

```lua
SetFactionInactive(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## SetSelectedFaction

Selects a faction in the reputation UI.

Selection has no bearing on other faction-related APIs; this function merely facilitates behaviors of Blizzard's reputation UI.

**Signature:**

```lua
SetSelectedFaction(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

## SetWatchedFactionIndex

Makes a faction the "watched" faction (displayed on the XP bar in the default UI)

**Signature:**

```lua
SetWatchedFactionIndex(index)
```

**Arguments:**

- `index` - Index of an entry in the faction list; between 1 and GetNumFactions() (`number`)

---

← [WoW API Docs](../index.md)
