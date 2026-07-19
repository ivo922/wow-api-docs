# Utility functions

← [WoW API Docs](../index.md)

**35** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#utility)

---

## CreateFont

Creates a new Font object

**Signature:**

```lua
fontObject = CreateFont("name")
```

**Arguments:**

- `name` - Name to assign to the newly created object; used both as the name of the object (retrievable with [`Font:GetName()`](../widgets/UIObject.md#uiobjectgetname)) and as a global variable referencing the object (unless another global by that name already exists) (`string`)

**Returns:**

- `fontObject` - The newly created Font object (`table`)

---

## CreateFrame

Creates a new Frame object

**Signature:**

```lua
frame = CreateFrame("frameType" [, "name" [, parent [, "template"]]])
```

**Arguments:**

- `frameType` - Type of frame to create; see [the widget documentation](../Widgets.md) for details (`string`)
- `name` - Name to assign to the newly created object; used both as the name of the object (retrievable via the [GetName](../widgets/UIObject.md#uiobjectgetname) method) and as a global variable referencing the object, unless another global by that name already exists (`string`)
- `parent` - Reference to another frame to be the new frame's parent (`table`)
- `template` - Name of a template to be used in creating the frame; if creating a frame from multiple templates, a comma-separated list of names (`string`)

**Returns:**

- `frame` - A reference to the newly created Frame (`table`)

**Examples:**

```lua
-- creates a generic button in the middle of the screen
mybutton = CreateFrame("Button","mybutton",UIParent,"UIPanelButtonTemplate")
mybutton:SetPoint("CENTER",0,0)
mybutton:SetWidth(80)
mybutton:SetHeight(22)
```

---

## EnumerateFrames

Returns the next frame following the frame passed, or nil if no more frames exist

**Signature:**

```lua
nextFrame = EnumerateFrames([currentFrame])
```

**Arguments:**

- `currentFrame` - The current frame to get the next frame, or nil to get the first frame (`table`)

**Returns:**

- `nextFrame` - The frame following currentFrame or nil if no more frames exist, or the first frame if nil was passed (`table`)

---

## GetAutoCompleteResults

Returns a list of character names which complete a given partial name prefix

**Signature:**

```lua
... = GetAutoCompleteResults("inputString", includeBitfield, excludeBitfield, maxResults [, cursorPosition])
```

**Arguments:**

- `inputString` - Partial name for which to return completions (`string`)
- `includeBitfield` - One or more of the following flags (combined via `bit.bor()`), indicating which characters should be included in the result list: (`number`, [bitfield](../types/bitfield.md))
  - `0x00000000` - `AUTOCOMPLETE_FLAG_NONE`: No characters
  - `0x00000001` - `AUTOCOMPLETE_FLAG_IN_GROUP`: Characters in the player's party or raid
  - `0x00000002` - `AUTOCOMPLETE_FLAG_IN_GUILD`: Characters in the player's guild
  - `0x00000004` - `AUTOCOMPLETE_FLAG_FRIEND`: Characters from the player's friends list
  - `0x00000010` - `AUTOCOMPLETE_FLAG_INTERACTED_WITH`: Characters with whom the player has recently interacted
  - `0x00000020` - `AUTOCOMPLETE_FLAG_ONLINE`: Currently online friends and guildmates
  - `0xffffffff` - `AUTOCOMPLETE_FLAG_ALL`: All characters
- `excludeBitfield` - One or more of the following flags (combined via `bit.bor()`), indicating which characters should be excluded from the result list: (`number`, [bitfield](../types/bitfield.md))
  - `0x00000000` - `AUTOCOMPLETE_FLAG_NONE`: No characters
  - `0x00000001` - `AUTOCOMPLETE_FLAG_IN_GROUP`: Characters in the player's party or raid
  - `0x00000002` - `AUTOCOMPLETE_FLAG_IN_GUILD`: Characters in the player's guild
  - `0x00000004` - `AUTOCOMPLETE_FLAG_FRIEND`: Characters from the player's friends list
  - `0x00000010` - `AUTOCOMPLETE_FLAG_INTERACTED_WITH`: Characters with whom the player has recently interacted
  - `0x00000020` - `AUTOCOMPLETE_FLAG_ONLINE`: Currently online friends and guildmates
  - `0xffffffff` - `AUTOCOMPLETE_FLAG_ALL`: All characters
- `maxResults` - Maximum number of results to be returned (`number`)
- `cursorPosition` - Cursor position in the `inputString`; currently unused (`number`)

**Returns:**

- `...` - A list of strings, each the name of a character matching the search parameters (`list`)

---

## GetClickFrame

Returns the Frame object associated with the given name.

Returns nil if there is no UI object with the name given, or if the named UI object is not a Frame.

**Signature:**

```lua
frame = GetClickFrame("name")
```

**Arguments:**

- `name` - Name of a Frame or other UI object (`string`)

**Returns:**

- `frame` - A reference to the named frame (`table`)

---

## GetCurrentKeyBoardFocus

Returns the frame currently handling keyboard input. Typically an EditBox

**Signature:**

```lua
frame = GetCurrentKeyBoardFocus()
```

**Returns:**

- `frame` - Frame currently handling keyboard input, or nil if no frame is currently focused (`table`)

---

## GetFramesRegisteredForEvent

Returns all frames registered for a given event

**Signature:**

```lua
... = GetFramesRegisteredForEvent("event")
```

**Arguments:**

- `event` - An event name (`string`)

**Returns:**

- `...` - A list of tables, each a reference to a frame registered for the event (`list`)

**Examples:**

```lua
-- Print the names of any named frames registered for an event
local function printFrameNames(...)
  for i=1,select("#", ...) do
    local frame = select(i, ...)
    local name = frame:GetName()
    if name then
      ChatFrame1:AddMessage(name)
    end
  end
end

printFrameNames(GetFramesRegisteredForEvent("UNIT_HEALTH"))
```

---

## GetMirrorTimerInfo

Returns information about special countdown timers

**Signature:**

```lua
timer, value, maxvalue, scale, paused, label = GetMirrorTimerInfo(index)
```

**Arguments:**

- `index` - Index of an available timer (between 1 and `MIRRORTIMER_NUMTIMERS`) (`number`)

**Returns:**

- `timer` - Non-localized token identifying the type of timer (`string`)
  - `BREATH` - Used for the Breath timer when swimming underwater
  - `DEATH` - Currently unused
  - `EXHAUSTION` - Used for the Fatigue timer when swimming far from shore
  - `FEIGNDEATH` - Used for the Hunter Feign Death ability
- `value` - Number of seconds remaining before the timer expires (`number`)
- `maxvalue` - Maximum value of the timer (`number`)
- `scale` - Rate at which the timer bar should move (e.g. -1 for a slowly "emptying" bar, 10 for a quickly "filling" bar); unused in the default UI (`number`)
- `paused` - 1 if the timer is currently paused; otherwise 0 (`number`)
- `label` - Localized text to be displayed for the timer (`string`)

---

## GetMirrorTimerProgress

Returns a high-resolution value for a special countdown timer

**Signature:**

```lua
progress = GetMirrorTimerProgress("timer")
```

**Arguments:**

- `timer` - Non-localized token identifying the type of timer (`string`)
  - `BREATH` - Used for the Breath timer when swimming underwater
  - `DEATH` - Currently unused
  - `EXHAUSTION` - Used for the Fatigue timer when swimming far from shore
  - `FEIGNDEATH` - Used for the Hunter Feign Death ability

**Returns:**

- `progress` - Number of milliseconds remaining before the timer expires (`number`)

---

## GetMouseButtonClicked

Returns which mouse button triggered the current script. If called in a line of execution that started with a click handler (OnMouseDown, OnMouseUp, OnClick, OnDoubleClick, PreClick, or PostClick), returns a string identifying which mouse button triggered the handler. Otherwise, returns nil.

**Signature:**

```lua
button = GetMouseButtonClicked()
```

**Returns:**

- `button` - Name of the mouse button that triggered the current script (`string`)

---

## GetMouseButtonName

Returns the name for a mouse button specified by number

**Signature:**

```lua
buttonName = GetMouseButtonName(buttonNumber)
```

**Arguments:**

- `buttonNumber` - A mouse button number (1-5) (`number`)

**Returns:**

- `buttonName` - The name of the given mouse button (`string`)
  - `Button4`
  - `Button5`
  - `LeftButton`
  - `MiddleButton`
  - `RightButton`

---

## GetMouseFocus

Returns the frame that is currently under the mouse, and has mouse input enabled.

**Signature:**

```lua
frame = GetMouseFocus()
```

**Returns:**

- `frame` - The frame that currently has the mouse focus (`table`)

**Examples:**

```lua
-- Returns the name of the frame under the mouse, if it's named
local frame = GetMouseFocus()
if not frame then
  ChatFrame1:AddMessage("There is no mouse enabled frame under the cursor")
else
  local name = frame:GetName() or tostring(frame)
  ChatFrame1:AddMessage(name .. " has the mouse focus")
end
```

---

## GetMuteName

Returns the name of a character on the mute list

**Signature:**

```lua
name = GetMuteName(index)
```

**Arguments:**

- `index` - Index of an entry in the mute listing (between 1 and [`GetNumMutes()`](Voice.md#getnummutes)) (`number`)

**Returns:**

- `name` - Name of the muted character (`string`)

---

## GetNumFrames

Returns the number of existing Frame objects (and derivatives). Only counts Frame objects and derivatives thereof (e.g. Button, Minimap, and StatusBar; but not FontString, AnimationGroup, and Texture).

**Signature:**

```lua
numFrames = GetNumFrames()
```

**Returns:**

- `numFrames` - Number of existing Frame objects (and derivatives) (`number`)

---

## GetText

Returns a localized string according to given parameters. Applies to any global variable whose name fits a standard format: for example, `GetText("foo")` returns the value of the global variable `foo` (if it exists), and `GetText("foo", 3)` returns the value of `foo_FEMALE` (or if it does not exist, the value of `foo`). Causes a Lua error if the given variable does not exists (or is nil).

**Signature:**

```lua
text = GetText("token" [, gender [, ordinal]])
```

**Arguments:**

- `token` - Base name of a localized string token (`string`)
- `gender` - Gender of the string's subject (as returned by [`UnitSex()`](Unit.md#unitsex)) (`number`)
- `ordinal` - Currently unused (`number`)

**Returns:**

- `text` - The localized string according to the given parameters (`string`)

---

## GetTime

Returns a number representing the current time (with millisecond precision). Unlike with [`time()`](Lua library.md#time-luaapi), the number returned by this function has no meaning of its own and may not be comparable across clients; however, since it also provides higher resolution it can be compared against itself for high-precision time measurements.

**Signature:**

```lua
time = GetTime()
```

**Returns:**

- `time` - A number that represents the current time in seconds (with millisecond precision) (`number`)

---

## IsLoggedIn

Returns whether the login process has completed. The [`PLAYER_LOGIN`](../events/PLAYER_LOGIN.md) event provides similar information; this function presents an alternative that can be used across UI reloads.

**Signature:**

```lua
loggedIn = IsLoggedIn()
```

**Returns:**

- `loggedIn` - 1 if the login process has completed; otherwise nil (`1nil`)

---

## IsMouseButtonDown

Returns whether a given mouse button is held down. If no button is specified, returns 1 if any mouse button is held down.

**Signature:**

```lua
isDown = IsMouseButtonDown([button])
```

**Arguments:**

- `button` - Number or name of a mouse button (`number,string`)
  - `1 or LeftButton` - Primary mouse button
  - `2 or RightButton` - Secondary mouse button
  - `3 or MiddleButton` - Third mouse button (or clickable scroll control)
  - `4 or Button4` - Fourth mouse button
  - `5 or Button5` - Fifth mouse button

**Returns:**

- `isDown` - 1 if the mouse button is down; otherwise nil (`1nil`)

---

## RegisterForSave `internal` `protected`

Enables a global variable for automatic saving upon logout & UI reload. Used for some data saved on the local client by the default UI.

Addons should use the `## SavedVariables` TOC directive instead.

**Signature:**

```lua
RegisterForSave()
```

---

## RegisterForSavePerCharacter `internal` `protected`

Enables a global variable for automatic saving (on a per-character basis) upon logout & UI reload. Used for some data saved on the local client by the default UI.

Addons should use the `## SavedVariablesPerCharacter` TOC directive instead.

**Signature:**

```lua
RegisterForSavePerCharacter()
```

---

## RequestTimePlayed `server`

Requests information from the server about the player character's total time spent online. Information is not returned immediately; the [`TIME_PLAYED_MSG`](../events/TIME_PLAYED_MSG.md) event fires when the requested data is available.

**Signature:**

```lua
RequestTimePlayed()
```

---

## RunScript

Runs a string as a Lua script

**Signature:**

```lua
RunScript("script")
```

**Arguments:**

- `script` - A Lua script to be run (`string`)

---

## SecondsToTime `blizzardui`

Returns a description of an amount of time in appropriate units. Output includes markup normally hidden when displayed in a FontString (see last example); this markup allows the client to automatically print the singular or plural form of a word depending on the value of the preceding number.

**Signature:**

```lua
time = SecondsToTime(seconds [, noSeconds [, notAbbreviated [, maxCount]]])
```

**Arguments:**

- `seconds` - An amount of time (in seconds) (`number`)
- `noSeconds` - True to omit a seconds term in the description; false or omitted otherwise (`boolean`)
- `notAbbreviated` - True to use full unit names in the description (e.g. Hours, Minutes); false or omitted to use abbreviations (e.g. Hr, Min) (`boolean`)
- `maxCount` - Maximum number of terms to include in the description; defaults to 2 if omitted (`number`)

**Returns:**

- `time` - A description of the amount of time in appropriate units (see examples) (`string`)

---

## SetPortraitToTexture

Sets a Texture object to display an arbitrary texture, altering it to fit a circular frame. Used in the default UI to display square textures (such as item icons) within the circular "portrait" frames used in many default UI elements.

Caveat: The texture must be of the BLP format.

**Signature:**

```lua
SetPortraitToTexture("frameName", "texturePath")
```

**Arguments:**

- `frameName` - Name of a Texture object (`string`)
- `texturePath` - Path to a texture to display (`string`)

---

## debuglocals

Returns information about the local variables at a given stack depth

**Signature:**

```lua
localsInfo = debuglocals(stackLevel)
```

**Arguments:**

- `stackLevel` - The stack level to query (`number`)

**Returns:**

- `localsInfo` - A string detailing the local variables at the given stack depth. (`string`)

---

## getglobal

Returns the value of a global variable. Often used in the default UI in cases where several similar names are systematically constructed. Examples:

In a script attached to a frame template, `getglobal(self:GetName().."Icon")` can refer to the Texture whose name is defined in XML as `$parentIcon`.

Several sets of localized string tokens follow standard formats: e.g. `getglobal("ITEM_QUALITY"..quality.."_DESC)` returns the name for the numeric `quality`.

Equivalent to `_G.name` or `_G["name"]`.

**Signature:**

```lua
value = getglobal("name")
```

**Arguments:**

- `name` - Name of a global variable (`string`)

**Returns:**

- `value` - Value of the given variable (`value`)

---

## scrub

Replaces non-simple values in a list with nil.

All simple values (strings, numbers, and booleans) are passed from the input list to the output list unchanged. Non-simple values (tables, functions, threads, and userdata) are replaced by nil in the output list.

**Signature:**

```lua
... = scrub(...)
```

**Arguments:**

- `...` - A list of values (`list`)

**Returns:**

- `...` - The list of input values, with all non-simple values replaced by nil (`list`)

---

## setglobal

Sets a global variable to a specified value. Allows setting the value of a global variable in contexts where its name might be overridden by that of a local variable; i.e. `setglobal(name, value)` is equivalent to `_G.name = value` or `_G["name"] = value`.

**Signature:**

```lua
setglobal("name", value)
```

**Arguments:**

- `name` - Name of a global variable (`string`)
- `value` - New value for the variable (`value`)

---

## strconcat

Joins a list of strings (with no separator). Equivalent to `strjoin("", ...)`. If no strings are provided, returns the empty string (`""`).

**Signature:**

```lua
result = strconcat("...")
```

**Arguments:**

- `...` - A list of strings to concatenate (`string`)

**Returns:**

- `result` - The concatenated string (`string`)

---

## strjoin

Joins a list of strings together with a given separator. If given a list of strings not already in a table, this function can be used instead of `table.concat` for better performance.

Also available as `string.join` (though not provided by the Lua standard library).

**Signature:**

```lua
text = strjoin("sep", ...)
```

**Arguments:**

- `sep` - A separator to insert between joined strings (`string`)
- `...` - A list of strings to be joined together (`list`)

**Returns:**

- `text` - The list of strings joined together with the given separator string (`string`)

---

## strlenutf8

Returns the length of a string, taking UTF-8 multi-byte characters into account

**Signature:**

```lua
length = strlenutf8("string")
```

**Arguments:**

- `string` - The string to query. (`string`)

**Returns:**

- `length` - The length of the given string, taking UTF-8 multi-byte characters into account. (`number`)

---

## strreplace

Fast simple substring substitution. Matches the semantics of `string.gsub`, but only finds and replaces specific substrings rather than using more powerful and more computationally expensive regular expression matching. Thus, this function can be used in place of `string.gsub` in performance-critical situations where only simple matching is needed.

Also available as `string.replace` (though not provided by the Lua standard library).

**Signature:**

```lua
newText, count = strreplace("text", "pattern", "replacement", "count")
```

**Arguments:**

- `text` - Text to be altered (`string`)
- `pattern` - A substring to be located within the source text (`string`)
- `replacement` - Text to be inserted in place of the found pattern (`string`)
- `count` - Maximum number of replacements to be made (`string`)

**Returns:**

- `newText` - The input string with matching substrings replaced (`string`)
- `count` - Number of occurrences of the substring replaced (`number`)

---

## strsplit

Splits a string based on another seperator string. Also available as `string.split` (though not provided by the Lua standard library).

**Signature:**

```lua
... = strsplit("sep", "text", limit)
```

**Arguments:**

- `sep` - The seperator string to use (`string`)
- `text` - The text to split (`string`)
- `limit` - The maximum number of pieces to split the string into (`number`)

**Returns:**

- `...` - A list of strings, split from the input text based on the seperator string (`string`)

---

## strtrim

Trims leading and trailing characters (whitespace by default) from a string. Also available as `string.trim` (though not provided by the Lua standard library).

**Signature:**

```lua
text = strtrim("str" [, "trimChars"])
```

**Arguments:**

- `str` - A string to trim (`string`)
- `trimChars` - A string listing the characters to be trimmed (e.g. `"[]{}()"` to trim leading and trailing brackets, braces, and parentheses); if `nil` or omitted, whitespace characters (space, tab, newline, etc) are trimmed (`string`)

**Returns:**

- `text` - The trimmed string (`string`)

**Examples:**

```lua
strtrim("   This is a test   ")
-- Returns "This is a test"
```

```lua
strtrim("121abc456", "615")
-- Returns "21abc4"
```

---

## wipe

Removes all entries from a table

**Signature:**

```lua
emptyTable = wipe(aTable)
```

**Arguments:**

- `aTable` - A table whose contents are to be erased (`table`)

**Returns:**

- `emptyTable` - The input table, with all entries removed (`table`)

---

← [WoW API Docs](../index.md)
