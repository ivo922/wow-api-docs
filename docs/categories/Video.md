# Video functions

← [WoW API Docs](../index.md)

**29** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#video)

---

## GetBaseMip `deprecated`

Returns the level of texture resolution rendered by the client

---

## GetCurrentMultisampleFormat

Returns the index of the currently selected multi-sample format

**Signature:**

```lua
index = GetCurrentMultisampleFormat()
```

**Returns:**

- `index` - The index of the currently selected multi-sample format. (`number`)

---

## GetCurrentResolution

Returns the index of the current resolution setting. For the dimensions of a resolution setting, use [`GetScreenResolutions()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetScreenResolutions).

**Signature:**

```lua
index = GetCurrentResolution()
```

**Returns:**

- `index` - Index of the current resolution setting (`number`)

**Examples:**

```lua
-- Print the current resolution to chat
local index = GetCurrentResolution();
local resolution = select(index, GetScreenResolutions());
print("Current resolution:", resolution);
```

---

## GetFarclip `deprecated`

Returns the maximum distance at which terrain is drawn. Corresponds to the "View Distance" slider in the default UI's Video Options pane, which allows settings between 177 and 1277 yards.

Functional but no longer used by the default UI; see the `farclip` CVar instead.

**Signature:**

```lua
distance = GetFarclip()
```

**Returns:**

- `distance` - Maximum distance at which terrain is drawn (in yards) (`number`)

---

## GetFramerate

Returns the number of frames per second rendered by the client

**Signature:**

```lua
framerate = GetFramerate()
```

**Returns:**

- `framerate` - Number of frames per second rendered by the client (`number`)

---

## GetGamma

Returns the current display gamma setting. Gamma value determines the contrast between lighter and darker portions of the game display; for a detailed explanation see [the Wikipedia entry on Gamma correction entry](http://en.wikipedia.org/wiki/Gamma_correction).

**Signature:**

```lua
gamma = GetGamma()
```

**Returns:**

- `gamma` - Current gamma setting (`number`)

---

## GetMultisampleFormats

Returns a list of available multisample settings. Used in the default UI to provide descriptions of multisample settings (e.g. "24-bit color 24-bit depth 6x multisample").

Indices used by [`GetCurrentMultisampleFormat()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetCurrentMultisampleFormat) and [`SetMultisampleFormat()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetMultisampleFormat) refer to the groups of `color`, `depth` and `multisample` values returned by this function; e.g. index 1 refers to values 1 through 3, index 2 to values 4 through 6, etc.

**Signature:**

```lua
color, depth, multisample, ... = GetMultisampleFormats()
```

**Returns:**

- `color` - Color depth (in bits) (`number`)
- `depth` - Video depth (in bits) (`number`)
- `multisample` - Number of samples per pixel (`number`)
- `...` - Additional sets of `color`, `depth` and `multisample` values, one for each multisample setting (`list`)

**Examples:**

```lua
local index = GetCurrentMultisampleFormat()
local formatsIndex = (index - 1) * 3 + 1
local color, depth, samples = select(formatsIndex, GetMultisampleFormats())
print(format("%d-bit color %d-bit depth %dx multisample", color, depth, samples))
```

---

## GetRefreshRates

Returns a list of available screen refresh rates. The current refresh rate can be found in the `gxRefresh` CVar.

**Signature:**

```lua
... = GetRefreshRates()
```

**Returns:**

- `...` - A list of numbers, each an available screen refresh rates (in hertz, or zycles per second) (`number`)

---

## GetScreenHeight

Returns the height of the screen for UI layout purposes. Measurements for layout are affected by the UI Scale setting (i.e. the `uiscale` CVar) and may not match actual screen pixels.

**Signature:**

```lua
height = GetScreenHeight()
```

**Returns:**

- `height` - Height of the screen in layout pixels (`number`)

---

## GetScreenResolutions

Returns a list of available screen resolutions

**Signature:**

```lua
... = GetScreenResolutions()
```

**Returns:**

- `...` - A list of strings, each a description of the dimensions of an available screen resolution (e.g. `"800x600"`, `"1024x768"`) (`string`)

**Examples:**

```lua
-- Print all available screen resolutions:
print("Available resolutions:", string.join(", ", GetScreenResolutions()))
```

---

## GetScreenWidth

Returns the width of the screen for UI layout purposes. Measurements for layout are affected by the UI Scale setting (i.e. the `uiscale` CVar) and may not match actual screen pixels.

**Signature:**

```lua
screenWidth = GetScreenWidth()
```

**Returns:**

- `screenWidth` - Width of the screen in layout pixels (`number`)

---

## GetTerrainMip

Returns the level of terrain detail displayed. Corresponds to the "Terrain Blending" slider in the default UI's Video Options pane.

**Signature:**

```lua
terrainDetail = GetTerrainMip()
```

**Returns:**

- `terrainDetail` - Level of terrain detail displayed (`number`)
  - `0` - Low detail
  - `1` - High detail

---

## GetVideoCaps

Returns information about graphics capabilities of the current system

**Signature:**

```lua
hasAnisotropic, hasPixelShaders, hasVertexShaders, hasTrilinear, hasTripleBufering, maxAnisotropy, hasHardwareCursor = GetVideoCaps()
```

**Returns:**

- `hasAnisotropic` - 1 if anisotropic filtering is available; otherwise 0 (`number`)
- `hasPixelShaders` - 1 if pixel shaders are available; otherwise 0 (`number`)
- `hasVertexShaders` - 1 if vertex shaders are available; otherwise 0 (`number`)
- `hasTrilinear` - 1 if trilinear filtering is available; otherwise 0 (`number`)
- `hasTripleBufering` - 1 if triple buffering is available; otherwise 0 (`number`)
- `maxAnisotropy` - Number of available settings for anisotropic filtering (corresponds to the "Texture Filtering" slider in the default UI) (`number`)
- `hasHardwareCursor` - 1 if hardware cursor support is available; otherwise 0 (`number`)

---

## GetWaterDetail `deprecated`

Returns the current value of the water detail option

---

## IsDesaturateSupported

Returns whether the current hardware supports desaturated textures

**Signature:**

```lua
isSupported = IsDesaturateSupported()
```

**Returns:**

- `isSupported` - 1 if texture desaturation is supported; otherwise nil (`1nil`)

---

## IsPlayerResolutionAvailable

Returns whether the current hardware supports high resolution player textures

**Signature:**

```lua
isAvailable = IsPlayerResolutionAvailable()
```

**Returns:**

- `isAvailable` - 1 if high-resolution player textures can be enabled; otherwise nil (`1nil`)

---

## IsStereoVideoAvailable

Returns whether the current system supports stereoscopic 3D display

**Signature:**

```lua
isAvailable = IsStereoVideoAvailable()
```

**Returns:**

- `isAvailable` - 1 if video options for stereoscopic 3D display should be shown; otherwise nil (`1nil`)

---

## RestartGx

Restart the client's graphic subsystem. Does not reload the UI.

**Signature:**

```lua
RestartGx()
```

---

## RestoreVideoEffectsDefaults

Resets video effects options to default values

---

## RestoreVideoResolutionDefaults

Resets video resolution options to default values

---

## RestoreVideoStereoDefaults

Resets stereoscopic 3D video options to default values. These options are shown in the Video -> Stereo panel in the default UI and include settings for convergence and eye separation.

**Signature:**

```lua
RestoreVideoStereoDefaults()
```

---

## SetBaseMip `deprecated`

Sets the level of texture resolution rendered by the client

---

## SetFarclip `deprecated`

Changes the maximum distance at which terrain is drawn

---

## SetGamma

Changes the display gamma setting. Gamma value determines the contrast between lighter and darker portions of the game display; for a detailed explanation see [the Wikipedia article on Gamma corection](http://en.wikipedia.org/wiki/Gamma_correction).

**Signature:**

```lua
SetGamma(value)
```

**Arguments:**

- `value` - New gamma value (`number`)

---

## SetMultisampleFormat

Changes the multisample setting. The `index` argument corresponds to the individual settings described by [`GetMultisampleFormats()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMultisampleFormats) (each a set of three values).

**Signature:**

```lua
SetMultisampleFormat(index)
```

**Arguments:**

- `index` - Index of a multisample setting (`number`)

---

## SetScreenResolution

Changes the screen resolution

**Signature:**

```lua
SetScreenResolution(index)
```

**Arguments:**

- `index` - Index of a resolution setting (between 1 and `select("#",`[`GetScreenResolutions()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetScreenResolutions)`)`) (`number`)

---

## SetTerrainMip

Changes the level of terrain detail displayed

---

## SetTexLodBias `internal`

**Signature:**

```lua
SetTexLodBias()
```

---

## SetWaterDetail `deprecated`

Sets the value for the water details display

**Signature:**

```lua
SetWaterDetail(value)
```

**Arguments:**

- `value` - The new value for the water detail (`number`)

---

← [WoW API Docs](../index.md)
