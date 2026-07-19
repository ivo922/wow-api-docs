# Zone information functions

← [WoW API Docs](../index.md)

**6** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#zone)

---

## GetMinimapZoneText

Returns the name of the current area (as displayed in the Minimap). Matches [`GetSubZoneText()`](Zone information.md#getsubzonetext), [`GetRealZoneText()`](Zone information.md#getrealzonetext) or [`GetZoneText()`](Zone information.md#getzonetext).

**Signature:**

```lua
zoneText = GetMinimapZoneText()
```

**Returns:**

- `zoneText` - Name of the area containing the player's current location (`string`)

---

## GetRealZoneText

Returns the "official" name of the zone or instance in which the player is located. This name matches that seen in the Who, Guild, and Friends UIs when reporting character locations. It may differ from those the default UI displays in other locations ([`GetZoneText()`](Zone information.md#getzonetext) and [`GetMinimapZoneText()`](Zone information.md#getminimapzonetext)), especially if the player is in an instance: e.g. this function returns "The Stockade" when the others return "Stormwind Stockade".

**Signature:**

```lua
zoneName = GetRealZoneText()
```

**Returns:**

- `zoneName` - Name of the zone or instance (`string`)

---

## GetSubZoneText

Returns the name of the minor area in which the player is located. Subzones are named regions within a larger zone or instance: e.g. the Valley of Trials in Durotar, the Terrace of Light in Shattrath City, or the Njorn Stair in Utgarde Keep.

**Signature:**

```lua
subzoneText = GetSubZoneText()
```

**Returns:**

- `subzoneText` - Name of the current subzone (`string`)

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

## GetZoneText

Returns the name of the zone in which the player is located

**Signature:**

```lua
zone = GetZoneText()
```

**Returns:**

- `zone` - Name of the current zone (`string`)

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

← [WoW API Docs](../index.md)
