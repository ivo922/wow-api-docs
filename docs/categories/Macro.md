# Macro functions

← [WoW API Docs](../index.md)

**23** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#macro)

---

## CreateMacro

Creates a new macro

**Signature:**

```lua
index = CreateMacro("name", icon, "body", perCharacter)
```

**Arguments:**

- `name` - Name for the new macro (up to 16 characters); need not be unique, though duplicate names can cause issues for other Macro API functions (`string`)
- `icon` - Index of a macro icon (between 1 and [`GetNumMacroIcons()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumMacroIcons)) (`number`)
- `body` - Body of the macro (up to 255 characters) (`string`)
- `perCharacter` - 1 if the macro should be stored as a character-specific macro; otherwise nil (`1nil`)

**Returns:**

- `index` - Index of the newly created macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))

**Examples:**

```lua
-- Create a character specific macro
local index = CreateMacro("DanceMonkey", 13, "/emote dances like a monkey!!!", 1)

-- Create a general macro
local index = CreateMacro("Heal", 73, "/cast Flash Heal\n/say Let the light of Elune cleanse you!")
```

---

## CursorHasMacro

Returns whether a macro is on the cursor. See [`GetCursorInfo()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetCursorInfo) for more detailed information.

**Signature:**

```lua
hasMacro = CursorHasMacro()
```

**Returns:**

- `hasMacro` - 1 if the cursor is currently holding a macro; otherwise nil (`1nil`)

---

## DeleteMacro

Deletes a macro

**Signature:**

```lua
DeleteMacro(index) or DeleteMacro("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

---

## EditMacro `nocombat`

Changes the name, icon, and/or body of a macro. After patch 4.3 then the numeric 'icon' argument has been replaced by 'iconTexture'.

Furthermore, the function always prepend 'Interface\Icons' to the 'iconTexture' string.

**Signature:**

```lua
newIndex = EditMacro(index, "name", "iconTexture", "body")
```

**Arguments:**

- `index` - Existing index of the macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - New name for the macro (up to 16 characters); nil to keep an existing name (`string`)
- `iconTexture` - name of icon texture; nil to keep an existing texture (`string`)
- `body` - Body of the macro (up to 255 characters); nil to keep the existing body (`string`)

**Returns:**

- `newIndex` - Index at which the macro is now saved (may differ from input `index` if the macro's name was changed, as macros are saved in alphabetical order) (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))

---

## GetMacroBody

Returns the body text of a macro

**Signature:**

```lua
body = GetMacroBody(index) or GetMacroBody("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

**Returns:**

- `body` - Body text / commands of the macro (`string`)

---

## GetMacroIconInfo

Returns the texture for a macro icon option

**Signature:**

```lua
texture = GetMacroIconInfo(index)
```

**Arguments:**

- `index` - Index of a macro icon option (between 1 and [`GetNumMacroIcons()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumMacroIcons)) (`number`)

**Returns:**

- `texture` - Path to the icon texture (`string`)

---

## GetMacroIndexByName

Returns the index of a macro specified by name

**Signature:**

```lua
index = GetMacroIndexByName("name")
```

**Arguments:**

- `name` - Name of a macro (`string`)

**Returns:**

- `index` - Index of the named macro, or 0 if no macro by that name exists (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))

---

## GetMacroInfo

Returns information about a macro

**Signature:**

```lua
name, texture, body = GetMacroInfo(index) or GetMacroInfo("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

**Returns:**

- `name` - Name of the macro (`string`)
- `texture` - Path to an icon texture for the macro (`string`)
- `body` - Body text / commands of the macro (`string`)

---

## GetMacroItem

Returns information about the item used by a macro. If a macro contains conditional, random, or sequence commands, this function returns the item which would currently be used if the macro were run.

**Signature:**

```lua
name, link = GetMacroItem(index) or GetMacroItem("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

**Returns:**

- `name` - Name of the item (`string`)
- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetMacroItemIconInfo

Returns the texture for an item icon. Despite the "macro" in the title, this function is only used by the default UI for providing tab icon options in the guild bank.

**Signature:**

```lua
texture = GetMacroItemIconInfo(index)
```

**Arguments:**

- `index` - Index of an item icon option (between 1 and [`GetNumMacroItemIcons()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumMacroItemIcons)) (`number`)

**Returns:**

- `texture` - Path to the icon texture (`string`)

---

## GetMacroSpell

Returns information about the spell cast by a macro. If a macro contains conditional, random, or sequence commands, this function returns the spell which would currently be cast if the macro were run.

**Signature:**

```lua
name, rank = GetMacroSpell(index) or GetMacroSpell("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

**Returns:**

- `name` - Name of the spell (`string`)
- `rank` - Secondary text associated with the spell (e.g. "Rank 4", "Racial") (`string`)

---

## GetNumMacroIcons

Returns the number of available macro icons

**Signature:**

```lua
numMacroIcons = GetNumMacroIcons()
```

**Returns:**

- `numMacroIcons` - The number of available macro icons (`number`)

---

## GetNumMacroItemIcons

Returns the number of available item icons. Despite the "macro" in the title, this function is only used by the default UI for providing tab icon options in the guild bank.

**Signature:**

```lua
numIcons = GetNumMacroItemIcons()
```

**Returns:**

- `numIcons` - Number of available item icons (`number`)

---

## GetNumMacros

Returns the number of macros the player has stored

**Signature:**

```lua
numAccountMacros, numCharacterMacros = GetNumMacros()
```

**Returns:**

- `numAccountMacros` - Number of account-wide macros (`number`)
- `numCharacterMacros` - Number of character-specific macros (`number`)

---

## GetRunningMacro

Returns the index of the currently running macro.

**Signature:**

```lua
index = GetRunningMacro()
```

**Returns:**

- `index` - Index of the currently running macro, or nil if no macro is running (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))

---

## GetRunningMacroButton

Returns the mouse button that was used to activate the running macro

**Signature:**

```lua
button = GetRunningMacroButton()
```

**Returns:**

- `button` - Name of the mouse button used to activate the macro; always "LeftButton" if the macro was triggered by a key binding (`string`)
  - `Button4`
  - `Button5`
  - `LeftButton`
  - `MiddleButton`
  - `RightButton`

---

## PickupMacro

Puts a macro onto the cursor

**Signature:**

```lua
PickupMacro(index) or PickupMacro("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

---

## RunMacro `protected`

Runs a macro

**Signature:**

```lua
RunMacro(index [, ""button""]) or RunMacro("name" [, ""button""])
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)
- `"button"` - The mouse button used to click the macro; may be used by `[button:`*x*`]` options in the macro (`string`)

---

## RunMacroText `protected`

Runs arbitrary text as a macro

**Signature:**

```lua
RunMacroText(""text"" [, ""button""])
```

**Arguments:**

- `"text"` - The text of the macro to run (`string`)
- `"button"` - The mouse button used to click the macro; may be used by `[button:`*x*`]` options in the macro (`string`)

---

## SecureCmdOptionParse

Returns the action (and target, if applicable) for a secure macro command. Used in the default UI to parse macro conditionals.

**Signature:**

```lua
action, target = SecureCmdOptionParse("cmd")
```

**Arguments:**

- `cmd` - A command to be parsed (typically the body of a macro, macrotext attribute or slash command (`string`)

**Returns:**

- `action` - Argument to the base macro command (e.g. the name of a spell for `/cast`), or the empty string (`""`) if the base command takes no arguments (e.g. `/stopattack`); nil if the command should not be executed (`string`)
- `target` - Unit or name to use as the target of the action (`string`)

---

## SetMacroItem

Changes the item used for dynamic feedback for a macro. Normally a macro uses the item or spell specified by its commands to provide dynamic feedback when placed on an action button (through the Action APIs, e.g. [`IsActionUsable()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsActionUsable)): e.g. if the macro uses a consumable item, the button will show the number of items remaining; if the macro uses an item with a cooldown, the button will show the state of the cooldown. This function allows overriding the item or spell used by the macro with another item -- the given item's state will be used for such feedback instead of the item or spell used by the macro.

**Signature:**

```lua
SetMacroItem(index, "item" [, target]) or SetMacroItem("name", "item" [, target])
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)
- `item` - Name of an item to use for the macro (`string`)
- `target` - A unit to use as target of the item (affects the macro's range indicator) (`unitid`)

---

## SetMacroSpell

Changes the spell used for dynamic feedback for a macro. Normally a macro uses the item or spell specified by its commands to provide dynamic feedback when placed on an action button (through the Action APIs, e.g. [`IsActionUsable()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsActionUsable)): e.g. if the macro uses a consumable item, the button will show the number of items remaining; if the macro uses an item with a cooldown, the button will show the state of the cooldown. This function allows overriding the item or spell used by the macro with another item -- the given item's state will be used for such feedback instead of the item or spell used by the macro.

**Signature:**

```lua
SetMacroSpell(index, "spell" [, target]) or SetMacroSpell("name", "spell" [, target])
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)
- `spell` - Name of a spell to use for the macro (`string`)
- `target` - A unit to use as target of the spell (affects the macro's range indicator) (`unitid`)

---

## StopMacro `protected`

Stops execution of a running macro

**Signature:**

```lua
StopMacro()
```

---

← [WoW API Docs](../index.md)
