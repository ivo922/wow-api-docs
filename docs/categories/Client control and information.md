# Client control and information functions

← [WoW API Docs](../index.md)

**22** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#client)

---

## CancelLogout `protected`

Cancels a pending logout or quit. Only has effect if logout or quit is pending (following the [`PLAYER_CAMPING`](../events/PLAYER_CAMPING.md) or [`PLAYER_QUITING`](../events/PLAYER_QUITING.md) event).

**Signature:**

```lua
CancelLogout()
```

---

## DownloadSettings

Restores game settings from a backup stored on the server. This function only works if server-synchronized settings are enabled. This is controlled by the `synchronizeSettings` CVar.

**Signature:**

```lua
DownloadSettings()
```

---

## ForceLogout `internal`

Forces the client to logout. Not usable in the current WoW client; causes an error message to be displayed.

**Signature:**

```lua
ForceLogout()
```

---

## ForceQuit

Immediately exits World of Warcraft. Unlike [`Quit()`](Client control and information.md#quit), this function exits the game application regardless of current conditions.

Used in the default UI when the player chooses "Exit now" in the dialog that appears if the player attempts to quit while not in an inn, major city, or other "rest" area.

**Signature:**

```lua
ForceQuit()
```

---

## GetAccountExpansionLevel

Returns the most recent of WoW's retail expansion packs for which the player's account is authorized.

Used in the default UI to determine the player's maximum possible level (and showing or hiding the XP bar accordingly). Also indicates whether the player is allowed to access expansion areas (e.g. Outland, Draenei / Blood Elf starting areas, Northrend).

**Signature:**

```lua
expansionLevel = GetAccountExpansionLevel()
```

**Returns:**

- `expansionLevel` - Expansion level of the player's account (`number`)
  - `0` - World of Warcraft ("Classic")
  - `1` - World of Warcraft: The Burning Crusade
  - `2` - World of Warcraft: Wrath of the Lich King
  - `3` - World of Warcraft: Cataclysm

---

## GetBuildInfo

Returns the version information about the client

**Signature:**

```lua
version, internalVersion, date, uiVersion = GetBuildInfo()
```

**Returns:**

- `version` - Display version number of the client (e.g. `"3.1.1"`) (`string`)
- `internalVersion` - Internal version number of the client (e.g. `"9835"`) (`string`)
- `date` - Date on which the client executable was built (e.g. `"Apr 24 2009"`); not necessarily the date it was released to the public (`string`)
- `uiVersion` - Version compatibility number for UI purposes (e.g. `30100`); generally, installed addons should have this number in the `Interface` header of their TOC files to avoid being marked as Out of Date and possibly not loaded (`number`)

---

## GetExistingLocales

Returns a list of installed localization packs for the WoW client

**Signature:**

```lua
... = GetExistingLocales()
```

**Returns:**

- `...` - A list of strings, each the four-letter locale code (see [`GetLocale()`](Client control and information.md#getlocale)) for an installed localization (`list`)

---

## GetExpansionLevel

Returns the expansion level of the game

---

## GetGameTime

Returns the current realm (server) time

**Signature:**

```lua
hour, minute = GetGameTime()
```

**Returns:**

- `hour` - Hour portion of the time (on a 24-hour clock) (`number`)
- `minute` - Minute portion of the time (`number`)

---

## GetLocale

Returns a code indicating the localization currently in use by the client

**Signature:**

```lua
locale = GetLocale()
```

**Returns:**

- `locale` - A four character locale code indicating the localization currently in use by the client (`string`)
  - `deDE` - German
  - `enGB` - British English
  - `enUS` - American English
  - `esES` - Spanish (European)
  - `esMX` - Spanish (Latin American)
  - `frFR` - French
  - `koKR` - Korean
  - `ruRU` - Russian
  - `zhCN` - Chinese (simplified; mainland China)
  - `zhTW` - Chinese (traditional; Taiwan)

---

## GetNetStats

Returns information about current network connection performance

**Signature:**

```lua
bandwidthIn, bandwidthOut, latencyHome, latencyWorld = GetNetStats()
```

**Returns:**

- `bandwidthIn` - Current incomming bandwidth (download) usage, measured in KB/s (`number`)
- `bandwidthOut` - Current outgoing bandwidth (upload) usage, measured in KB/s (`number`)
- `latencyHome` - Average roundtrip latency to the home realm server (only updated every 30 seconds) (`number`)
- `latencyWorld` - Average roundtrip latency to the current world server (only updated every 30 seconds) (`number`)

---

## IsLinuxClient

Returns whether the player is using the Linux game client. Does not indicate whether the player is running a Windows clint on Linux with virtualization software. Blizzard has not released an official WoW client for Linux, but this function is included just in case that situation changes.

**Signature:**

```lua
isLinux = IsLinuxClient()
```

**Returns:**

- `isLinux` - 1 if running the Linux client; otherwise nil (`1nil`)

---

## IsMacClient

Returns whether the player is using the Mac OS X game client

**Signature:**

```lua
isMac = IsMacClient()
```

**Returns:**

- `isMac` - 1 if running the Mac OS X client; otherwise nil (`1nil`)

---

## IsWindowsClient

Returns whether the player is using the Windows game client

**Signature:**

```lua
isWindows = IsWindowsClient()
```

**Returns:**

- `isWindows` - 1 if running the Windows client; otherwise nil (`1nil`)

---

## Logout

Attempts to log out and return to the character selection screen. Results vary based on current conditions:

- If the player is in combat or under other temporary restrictions (e.g. falling), fires the [`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md) event with a message indicating the player cannot log out at the moment.
- If the player is not in an inn, major city, or other "rest" area (i.e. [`IsResting()`](Player information.md#isresting) returns `nil`), fires the [`PLAYER_CAMPING`](../events/PLAYER_CAMPING.md) event, causing the default UI to show a countdown, logging the player out after a period of time if not canceled.
- If the player is in a "rest" area, logs out immediately.

**Signature:**

```lua
Logout()
```

---

## NotWhileDeadError

Causes the default UI to display an error message indicating that actions are disallowed while the player is dead. Fires a [`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md) event containing a localized message identified by the global variable `ERR_PLAYER_DEAD`.

**Signature:**

```lua
NotWhileDeadError()
```

---

## Quit

Attempts to exit the World of Warcraft client. Results vary based on current conditions:

- If the player is in combat or under other temporary restrictions (e.g. falling), fires the [`UI_ERROR_MESSAGE`](../events/UI_ERROR_MESSAGE.md) event with a message indicating the player cannot log out at the moment.
- If the player is not in an inn, major city, or other "rest" area (i.e. [`IsResting()`](Player information.md#isresting) returns `nil`), fires the [`PLAYER_QUITING`](../events/PLAYER_QUITING.md) event, causing the default UI to show a countdown, quitting WoW after a period of time if not canceled.
- If the player is in a "rest" area, quits the game immediately.

**Signature:**

```lua
Quit()
```

---

## ReloadUI `hardware`

Reloads the user interface. Saved variables are written to disk, the default UI is reloaded, and all enabled non-LoadOnDemand addons are loaded, including any addons previously disabled which were enabled during the session (see [`EnableAddOn()`](Addon-related.md#enableaddon) et al).

**Signature:**

```lua
ReloadUI()
```

---

## Screenshot

Saves an image of the current game display. Screenshot images are saved to the folder `Screenshots` within the folder where the World of Warcraft client is installed.

Taking a screenshot fires the [`SCREENSHOT_SUCCEEDED`](../events/SCREENSHOT_SUCCEEDED.md) event (or the [`SCREENSHOT_FAILED`](../events/SCREENSHOT_FAILED.md) event in case of an error), which causes the default UI to display a message in the middle of the screen. Additional screenshots taken while this message is displayed will include it -- the default UI's `TakeScreenshot()` function hides this message so it is not included in screenshots.

**Signature:**

```lua
Screenshot()
```

---

## SetEuropeanNumbers

Sets the decimal separator for displayed numbers. Affects the style not only of numbers displayed in the UI, but any string coercion of numbers with `tostring()` as well.

**Signature:**

```lua
SetEuropeanNumbers(enable)
```

**Arguments:**

- `enable` - True to use comma (",") as the decimal separator; false to use period (".") as the decimal separator (`boolean`)

---

## SetUIVisibility

Enables or disables display of UI elements in the 3-D world. Applies only to 2-D UI elements displayed in the 3-D world: nameplates and raid target icons (skull, circle, square, etc). Does not directly control nameplates and target icons -- only affects whether they are displayed (see the `nameplateShowEnemies`/`nameplateShowFriends` CVars and [`SetRaidTarget`](Raid.md#setraidtarget) functions for direct control).

Does not apply to 3-D UI elements such as the selection circle, area-effect targeting indicator, vehicle weapon aim indicator, etc.

**Signature:**

```lua
SetUIVisibility(visible)
```

**Arguments:**

- `visible` - True to enable display of UI elements in the 3-D world; false to disable (`boolean`)

---

## UploadSettings

Stores a backup of game settings on the server.

Does nothing unless server-side settings have been disabled by setting the synchronizeSettings CVar to 0.

**Signature:**

```lua
UploadSettings()
```

---

← [WoW API Docs](../index.md)
