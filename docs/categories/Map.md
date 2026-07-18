# Map functions

← [WoW API Docs](../index.md)

**27** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#map)

---

## ClickLandmark

Processes a hyperlink associated with a map landmark. Possible landmarks include PvP objectives (both in battlegrounds and in world PvP areas), town and city markers on continent maps, and special markers such as those used during the Scourge Invasion world event. Some landmarks (such as those for towns on a zone map) exist but are not visible in the default UI.

Hyperlinks are not used for any of the landmarks currently in the game; this function does nothing when called with a landmark which does not have a hyperlink.

**Signature:**

```lua
ClickLandmark(mapLinkID)
```

**Arguments:**

- `mapLinkID` - Hyperlink ID associated with a map landmark, as retrieved from GetMapLandmarkInfo() (`number`)

---

## GetBattlefieldVehicleInfo

Returns information about special vehicles in the current zone. Used only for certain vehicles in certain zones: includes the airships in Icecrown as well as vehicles used in Ulduar, Wintergrasp, and Strand of the Ancients.

**Signature:**

```lua
vehicleX, vehicleY, unitName, isPossessed, vehicleType, orientation, isPlayer, isAlive = GetBattlefieldVehicleInfo(index)
```

**Arguments:**

- `index` - Index of a special vehicle (between 1 and [`GetNumBattlefieldVehicles()`](https://web.archive.org/web/20100105220937/http://wowprogramming.com/docs/api/GetNumBattlefieldVehicles)) (`number`)

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

## GetCorpseMapPosition

Returns the position of the player's corpse on the world map. Returns `0,0` if the location of the player's corpse is not visible on the current world map.

**Signature:**

```lua
corpseX, corpseY = GetCorpseMapPosition()
```

**Returns:**

- `corpseX` - Horizontal position of the player's corpse relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `corpseY` - Vertical position of the player's corpse relative to the zone map (0 = top, 1 = bottom) (`number`)

---

## GetCurrentMapAreaID

Returns an ID number for the current map zone.

Currently only used in the default UI to determine whether the Wintergrasp map is showing (and if so, display the time remaining until the next battle).

**Signature:**

```lua
areaID = GetCurrentMapAreaID()
```

**Returns:**

- `areaID` - A number identifying the current map zone (`number`)

---

## GetCurrentMapContinent

Returns the current world map continent

**Signature:**

```lua
continent = GetCurrentMapContinent()
```

**Returns:**

- `continent` - Index of the world map's current continent (in the list returned by [`GetMapContinents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMapContinents), or one of the following values) (`number`)
  - `-1` - Cosmic map
  - `0` - Azeroth
  - `1` - Kalimdor
  - `2` - Eastern Kingdoms
  - `3` - Outland
  - `4` - Northrend
  - `5` - The Maelstrom

---

## GetCurrentMapDungeonLevel

Returns which map image is currently selected on the world map (for zones which use more than one map image). Used in zones with more than one "floor" or area, such as Dalaran and several Wrath of the Lich King dungeons and raids. More than one map image may contain the player's current location; if the world map has not been explicitly set to show a particular area, this returns whichever is the "best" match.

**Signature:**

```lua
level = GetCurrentMapDungeonLevel()
```

**Returns:**

- `level` - Index of the current map image (`number`)

---

## GetCurrentMapZone

Returns the current world map zone

**Signature:**

```lua
zone = GetCurrentMapZone()
```

**Returns:**

- `zone` - Index of a zone within the continent (in the list returned by [`GetMapZones`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMapZones)`(`[`GetCurrentMapContinent()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetCurrentMapContinent)`)`), or 0 for the continent map (`number`)

---

## GetDeathReleasePosition

Returns the location of the graveyard where the player's spirit will appear upon release. Returns `0,0` if the player is not dead or the graveyard's location is not visible on the current world map.

**Signature:**

```lua
graveyardX, graveyardY = GetDeathReleasePosition()
```

**Returns:**

- `graveyardX` - Horizontal position of the graveyard relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `graveyardY` - Vertical position of the graveyard relative to the zone map (0 = top, 1 = bottom) (`number`)

---

## GetMapContinents

Returns a list of map continents names

**Signature:**

```lua
... = GetMapContinents()
```

**Returns:**

- `...` - A list of strings, each the localized name of a map continent (`list`)

---

## GetMapInfo

Returns information about the current world map texture. World map images are broken into several tiles; the full texture paths follow the format `"Interface\\WorldMap\\"..mapFileName.."\\"..mapFileName..i`, where `i` is a number between 1 and `NUM_WORLDMAP_DETAIL_TILES` (or in a zone with multiple area images, `"Interface\\WorldMap\\"..mapFileName.."\\"..mapFileName..dungeonLevel.."_"..i`, where `dungeonLevel` is a number between 1 and [`GetNumDungeonMapLevels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDungeonMapLevels)).

**Signature:**

```lua
mapFileName, textureHeight, textureWidth = GetMapInfo()
```

**Returns:**

- `mapFileName` - Unique part of the path to the world map textures (`string`)
- `textureHeight` - Height of the combined map texture tiles (`number`)
- `textureWidth` - Width of the combined map texture tiles (`string`)

---

## GetMapLandmarkInfo

Returns information about a map landmark. Possible landmarks include PvP objectives (both in battlegrounds and in world PvP areas), town and city markers on continent maps, and special markers such as those used during the Scourge Invasion world event. Some landmarks (such as those for towns on a zone map) exist but are not visible in the default UI.

**Signature:**

```lua
name, description, textureIndex, x, y, mapLinkID, showInBattleMap = GetMapLandmarkInfo(index)
```

**Arguments:**

- `index` - The index of a map landmark, from 1 to GetNumMapLandmarks() (`number`)

**Returns:**

- `name` - Name of the landmark (`string`)
- `description` - Secondary text associated with the landmark; often used to denote current status of PvP objectives (e.g. "Alliance Controlled") (`string`)
- `textureIndex` - The index of the texture to be used for the landmark. These indices map to segments of the Interface/MinimapPOI/Icons.blp graphic; the function WorldMap_GetPOITextureCoords(), defined in FrameXML/WorldMap.lua, can be used to resolve this index to a set of texture coordinates for displaying that segment. (`number`)
- `x` - Horizontal position of the landmark relative to the current world map (0 = left edge, 1 = right edge) (`number`)
- `y` - Vertical position of the landmark relative to the current world map (0 = top, 1 = bottom) (`number`)
- `mapLinkID` - A hyperlink ID allowing the game engine to take an action when the landmark is clicked (currently unused) (`number`)
- `showInBattleMap` - True if the landmark should be shown in the Battle Map (aka Zone Map) UI; false for landmarks which should only be shown on the World Map (`boolean`)

---

## GetMapOverlayInfo

Returns information about a world map overlay. Map overlays correspond to areas which are "discovered" when entered by the player, "filling in" the blank areas of the world map.

**Signature:**

```lua
textureName, textureWidth, textureHeight, offsetX, offsetY, mapPointX, mapPointY = GetMapOverlayInfo(index)
```

**Arguments:**

- `index` - Index of a map overlay (between 1 and [`GetNumMapOverlays()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumMapOverlays)) (`number`)

**Returns:**

- `textureName` - Path to the overlay texture (`string`)
- `textureWidth` - Width of the texture (in pixels) (`number`)
- `textureHeight` - Height of the texture (in pixels) (`number`)
- `offsetX` - Horizontal position of the overlay's top left corner relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `offsetY` - Vertical position of the overlay's top left corner relative to the zone map (0 = top, 1 = bottom) (`number`)
- `mapPointX` - Unused (`number`)
- `mapPointY` - Unused (`number`)

---

## GetMapZones

Returns the map zones for a given continent

**Signature:**

```lua
... = GetMapZones(continentIndex)
```

**Arguments:**

- `continentIndex` - Index of a continent (in the list returned by [`GetMapContinents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMapContinents)) (`number`)

**Returns:**

- `...` - A list of strings, each the localized name of a zone within the continent (`list`)

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

## GetNumDungeonMapLevels

Returns the number of map images for the world map's current zone. Used in zones with more than one "floor" or area such as Dalaran and several Wrath of the Lich King dungeons and raids.

**Signature:**

```lua
numLevels = GetNumDungeonMapLevels()
```

**Returns:**

- `numLevels` - Number of map images (`number`)

---

## GetNumMapLandmarks

Returns the number of landmarks on the world map. Possible landmarks include PvP objectives (both in battlegrounds and in world PvP areas), town and city markers on continent maps, and special markers such as those used during the Scourge Invasion world event. Some landmarks (such as those for towns on a zone map) exist but are not visible in the default UI.

**Signature:**

```lua
numLandmarks = GetNumMapLandmarks()
```

**Returns:**

- `numLandmarks` - The number of landmarks on the current world map (`number`)

---

## GetNumMapOverlays

Returns the number of overlays for the current world map zone. Map overlays correspond to areas which are "discovered" when entered by the player, "filling in" the blank areas of the world map.

**Signature:**

```lua
numOverlays = GetNumMapOverlays()
```

**Returns:**

- `numOverlays` - Number of overlays for the current world map zone (`number`)

---

## GetPlayerFacing

Returns the player's orientation (heading). Indicates the direction the player model is (normally) facing and in which the player will move if he begins walking forward, not the camera orientation.

**Signature:**

```lua
facing = GetPlayerFacing()
```

**Returns:**

- `facing` - Direction the player is facing (in radians, 0 = north, values increasing counterclockwise) (`number`)

---

## GetPlayerMapPosition

Returns the position of a unit in the player's party or raid on the world map. Returns `0,0` if the unit's location is not visible on the current world map.

**Signature:**

```lua
unitX, unitY = GetPlayerMapPosition("unit")
```

**Arguments:**

- `unit` - A unit in the player's party or raid (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `unitX` - Horizontal position of the unit relative to the zone map (0 = left edge, 1 = right edge) (`number`)
- `unitY` - Vertical position of the unit relative to the zone map (0 = top, 1 = bottom) (`number`)

---

## GetWintergraspWaitTime

Returns the amount of time remaining until the next PvP event in the Wintergrasp zone

---

## InitWorldMapPing `internal`

Initializes the frame used to display the character location "ping" on the World Map

**Signature:**

```lua
InitWorldMapPing()
```

---

## ProcessMapClick

Possibly changes the WorldMap based on a mouse click. May change the map zone or zoom based on the click location: e.g. if the world map shows Dragonblight and one clicks in the area labeled "Wintergrasp" on the map, the current map zone changes to show Wintergrasp.

**Signature:**

```lua
ProcessMapClick(clickX, clickY)
```

**Arguments:**

- `clickX` - Horizontal position of the click relative to the current world map (0 = left edge, 1 = right edge) (`number`)
- `clickY` - Vertical position of the click relative to the current world map (0 = top, 1 = bottom) (`number`)

---

## SetDungeonMapLevel

Sets the world map to display a certain map image (for zones that use multiple map images). Used in zones with more than one "floor" or area such as Dalaran and several Wrath of the Lich King dungeons and raids.

**Signature:**

```lua
SetDungeonMapLevel(level)
```

**Arguments:**

- `level` - Index of the map image to show in the world map (`number`)

---

## SetMapToCurrentZone

Sets the world map to show the zone in which the player is located

**Signature:**

```lua
SetMapToCurrentZone()
```

---

## SetMapZoom

Sets the world map to show a specific zone or continent

**Signature:**

```lua
SetMapZoom(continentIndex [, zoneIndex])
```

**Arguments:**

- `continentIndex` - Index of a continent to display (in the list returned by [`GetMapContinents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMapContinents), or one of the following values) (`number`)
  - `-1` - Cosmic map
  - `0` - Entire Azeroth map
  - `1` - Kalimdor
  - `2` - Eastern Kingdoms
  - `3` - Outland
  - `4` - Northrend
  - `5` - The Maelstrom
  - `6` - Pandaria
  - `7` - Draenor
- `zoneIndex` - Index of a zone within the continent to display (in the list returned by [`GetMapZones(continentIndex)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMapZones)), or omitted to show the continent map (`number`)

---

## UpdateMapHighlight

Returns information about the texture used for highlighting zones in a continent map on mouseover

**Signature:**

```lua
name, fileName, texCoordX, texCoordY, textureX, textureY, scrollChildX, scrollChildY = UpdateMapHighlight(cursorX, cursorY)
```

**Arguments:**

- `cursorX` - Horizontal position of the mouse cursor relative to the current world map (0 = left edge, 1 = right edge) (`number`)
- `cursorY` - Vertical position of the unit relative to the current world map (0 = top, 1 = bottom) (`number`)

**Returns:**

- `name` - The name of the zone being highlighted (`string`)
- `fileName` - Unique part of the path to the highlight texture for the zone; full path follows the format `"Interface\\WorldMap\\"..fileName.."\\"..fileName.."Highlight"` (`string`)
- `texCoordX` - Right texCoord value for the highlight texture (`number`)
- `texCoordY` - Bottom texCoord value for the highlight texture (`number`)
- `textureX` - Width of the texture as a proportion of the world map's width (`number`)
- `textureY` - Height of the texture as a proportion of the world map's height (`number`)
- `scrollChildX` - Horizontal position of the texture's top left corner relative to the current world map (0 = left edge, 1 = right edge) (`number`)
- `scrollChildY` - Vertical position of the texture's top left corner relative to the current world map (0 = top, 1 = bottom) (`number`)

---

## ZoomOut

Sets the world map to show the area containing its current area.

Only used by the default UI in certain circumstances: to "zoom out" from a multi-level map (e.g. Dalaran or a dungeon) to the containing zone/continent. May cause problems when not used in such cases.

**Signature:**

```lua
ZoomOut()
```

---

← [WoW API Docs](../index.md)
