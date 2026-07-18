# Addon-related functions

← [WoW API Docs](../index.md)

**15** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#addon)

---

## DisableAddOn

Marks an addon as disabled. The addon will remain active until the player logs out and back in or reloads the UI (see [`ReloadUI()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ReloadUI)). Changes to the enabled/disabled state of addons while in-game are saved on a per-character basis.

**Signature:**

```lua
DisableAddOn("name") or DisableAddOn(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumAddOns)) (`number`)

---

## DisableAllAddOns

Marks all addons as disabled. Addons will remain active until the player logs out and back in or reloads the UI (see [`ReloadUI()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ReloadUI)).

Changes to the enabled/disabled state of addons while in-game are saved on a per-character basis.

**Signature:**

```lua
DisableAllAddOns()
```

---

## EnableAddOn

Marks an addon as enabled. The addon will remain inactive until the player logs out and back in or reloads the UI (see [`ReloadUI()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ReloadUI)).

Changes to the enabled/disabled state of addons while in-game are saved on a per-character basis.

**Signature:**

```lua
EnableAddOn(index) or EnableAddOn("name")
```

**Arguments:**

- `index` - The index of the addon to be enabled (`number`)
- `name` - The name of the addon to be enabled (`string`)

---

## EnableAllAddOns

Marks all addons as enabled. Addons will remain inactive until the player logs out and back in or reloads the UI (see [`ReloadUI()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ReloadUI)).

Changes to the enabled/disabled state of addons while in-game are saved on a per-character basis.

**Signature:**

```lua
EnableAllAddOns()
```

---

## GetAddOnDependencies

Returns a list of addons a given addon is dependent upon

**Signature:**

```lua
... = GetAddOnDependencies("name") or GetAddOnDependencies(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumAddOns)) (`number`)

**Returns:**

- `...` - A list of strings, each the (folder) name of another addon this addon is dependent upon (`list`)

---

## GetAddOnInfo

Returns information about an addon in the client's addon list

**Signature:**

```lua
name, title, notes, enabled, loadable, reason, security = GetAddOnInfo(index) or GetAddOnInfo("name")
```

**Arguments:**

- `index` - The index of the AddOn, must be in the range of 1 to GetNumAddOns(). (`number`)
- `name` - The name of the AddOn, as it appears in its folder name. (`string`)

**Returns:**

- `name` - The name of the addon (`string`)
- `title` - The title of the addon (`string`)
- `notes` - The value of the "Notes" field from the table of contents (`string`)
- `enabled` - 1 if the addon is enabled for the current character, otherwise nil (`1nil`)
- `loadable` - If the addon is capable of being loaded (`1nil`)
- `reason` - If the addon isn't loadable, what is the reason (`string`)
- `security` - "SECURE" if the addon is secure, otherwise "INSECURE". A "secure" addon is one that is released by Blizzard and is digitally signed (`string`)

---

## GetAddOnMetadata

Returns the value of certain fields in an addon's TOC file

**Signature:**

```lua
data = GetAddOnMetadata(index, "variable") or GetAddOnMetadata("name", "variable")
```

**Arguments:**

- `index` - The index of the AddOn, must be in the range of 1 to GetNumAddOns(). (`number`)
- `name` - The name of the AddOn as it appears in its folder name. (`string`)
- `variable` - The variable name that you want to query, only a limited number of values are accepted. (`string`)
  - `Author` - The author of the AddOn as outlined in the TOC file
  - `Notes` - Any notes the author of the AddOn placed into the TOC file
  - `Title` - The title of the AddOn, this defaults to the name of the AddOn as it appears in its folder name
  - `Version` - The version string that the author placed in the TOC file
  - `X-` - These are the only custom tags that can be queried, can be anything you want.

**Returns:**

- `data` - The data available in the TOC for the variable queried, or nil if the variable is not queryable or not defined. (`string`)

---

## GetNumAddOns

Returns the number of addons in the addon listing

**Signature:**

```lua
numAddons = GetNumAddOns()
```

**Returns:**

- `numAddons` - The number of addons in the addon listing (`number`)

---

## InterfaceOptionsFrame_OpenToCategory `blizzardui`

Opens the Interface Options window and displays a given panel within it

**Signature:**

```lua
InterfaceOptionsFrame_OpenToCategory("panelName") or InterfaceOptionsFrame_OpenToCategory(panel)
```

**Arguments:**

- `panelName` - The registered name of an options panel (`string`)
- `panel` - A Frame object already registered as an options panel (`table`)

---

## InterfaceOptions_AddCategory `blizzardui`

Registers a panel to be displayed in the Interface Options window. The following members and methods are used by the Interface Options frame to display and organize panels:

`panel.name` - `string` (required) - The name of the AddOn or group of configuration options. This is the text that will display in the AddOn options list.

`panel.parent` - `string` (optional) - Name of the parent of the AddOn or group of configuration options. This identifies "panel" as the child of another category. If the parent category doesn't exist, "panel" will be displayed as a regular category.

`panel.okay` - `function` (optional) - This method will run when the player clicks "okay" in the Interface Options.

`panel.cancel` - `function` (optional) - This method will run when the player clicks "cancel" in the Interface Options. Use this to revert their changes.

`panel.default` - `function` (optional) - This method will run when the player clicks "defaults". Use this to revert their changes to your defaults.

`panel.refresh` - `function` (optional) - This method will run when the Interface Options frame calls its OnShow function and after defaults have been applied via the panel.default method described above. Use this to refresh your panel's UI in case settings were changed without player interaction.

**Signature:**

```lua
InterfaceOptions_AddCategory(panel)
```

**Arguments:**

- `panel` - A Frame object (`table`)

---

## IsAddOnLoadOnDemand

Returns whether an addon can be loaded without restarting the UI

**Signature:**

```lua
isLod = IsAddOnLoadOnDemand("name") or IsAddOnLoadOnDemand(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumAddOns)) (`number`)

**Returns:**

- `isLod` - 1 if the addon is LoadOnDemand-capable; otherwise nil (`1nil`)

---

## IsAddOnLoaded

Returns whether an addon is currently loaded

**Signature:**

```lua
loaded = IsAddOnLoaded("name") or IsAddOnLoaded(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](https://web.archive.org/web/20100105223616/http://wowprogramming.com/docs/api/GetNumAddOns)) (`number`)

**Returns:**

- `loaded` - 1 if the addon is loaded; otherwise nil (`1nil`)

---

## LoadAddOn

Loads a LoadOnDemand-capable addon. If the given addon has dependencies which are also LoadOnDemand-capable, those addons will be loaded as well. This function will not load disabled addons.

**Signature:**

```lua
loaded, reason = LoadAddOn("name") or LoadAddOn(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumAddOns)) (`number`)

**Returns:**

- `loaded` - 1 if loading the addon was successful; otherwise nil (`number`)
- `reason` - If the addon could not be loaded, an unlocalized string token indicating the reason for failure. Localized strings for display can be found by prepending `"ADDON_"`; e.g. `ADDON_DEP_MISSING == "Dependency missing"`. (`string`)
  - `BANNED` - Banned
  - `CORRUPT` - Corrupt
  - `DEP_BANNED` - Dependency banned
  - `DEP_CORRUPT` - Dependency corrupt
  - `DEP_DISABLED` - Dependency disabled
  - `DEP_INCOMPATIBLE` - Dependency incompatible
  - `DEP_INSECURE` - Dependency insecure
  - `DEP_INTERFACE_VERSION` - Dependcy out of date
  - `DEP_MISSING` - Dependency missing
  - `DEP_NOT_DEMAND_LOADED` - Dependency not loadable on demand
  - `DISABLED` - Disabled
  - `INCOMPATIBLE` - Incompatible
  - `INSECURE` - Insecure
  - `INTERFACE_VERSION` - Out of Date
  - `MISSING` - Missing
  - `NOT_DEMAND_LOADED` - Not loadable on demand

---

## ResetDisabledAddOns

Reverts changes to the enabled/disabled state of addons. Any addons enabled or disabled in the current session will return to their enabled/disabled state as of the last login or UI reload.

**Signature:**

```lua
ResetDisabledAddOns()
```

---

## SendAddonMessage

Sends a chat-like message receivable by other addons. Allows for client-to-client addon communication.

Unlike with [`SendChatMessage`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SendChatMessage), messages sent via `SendAddonMessage`:

- do not appear in receiving players' chat windows (unless an addon explicitly prints them)
- are not subject to strict server-side spam filtering/throttling (sending too many messages at once can still disconnect the user)
- are not modified if the sending character is drunk

Messages are received via the [`CHAT_MSG_ADDON`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_ADDON) event.

**Signature:**

```lua
SendAddonMessage("prefix", "message" [, "type" [, "target"]])
```

**Arguments:**

- `prefix` - An arbitrary label for the message. Allows receiving addons to filter incoming messages: for example, if an addon uses the same prefix for all messages it sends, an addon interested in only those messages can check for that prefix before handling the message content. Cannot contain the tab character (`\t`). (`string`)
- `message` - A message to send; combined length of `prefix` and `message` is limited to 254 characters (`string`)
- `type` - Scope in which to broadcast the message: (`string`)
  - `BATTLEGROUND` - To all allied players in the current battleground instance
  - `GUILD` - To all members of the player's guild
  - `PARTY` - To all members of the player's party (used by default if no type is given)
  - `RAID` - To all members of the player's raid group (automatically reverts to sending to party if the player is not in a raid group)
  - `WHISPER` - To a specific player
- `target` - If type is `"WHISPER"`, the name of the target player (in cross-realm battlegrounds, the format "Name-Realm" can be used to target a player from another realm; e.g. "Thott-Cenarius") (`string`)

**Examples:**

```lua
-- Hypothetical communication using addon messages
local MSG_PREFIX = "MY_MOD"
SendAddonMessage(MSG_PREFIX, "Resync", "GUILD")
SendAddonMessage(MSG_PREFIX, "VersionCheck", "WHISPER", player)
```

---

← [WoW API Docs](../index.md)
