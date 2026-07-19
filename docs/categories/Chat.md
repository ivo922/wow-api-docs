# Chat functions

← [WoW API Docs](../index.md)

**32** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#chat)

---

## AddChatWindowChannel

Adds a chat channel to the saved list of those displayed in a chat window. Used by the default UI's function `ChatFrame_AddChannel()` which manages the set of channel messages shown in a displayed ChatFrame.

**Signature:**

```lua
zoneChannel = AddChatWindowChannel(index, channel)
```

**Arguments:**

- `index` - Index of a chat frame (between `1` and `NUM_CHAT_WINDOWS`) (`number`)
- `channel` - Name of a chat channel (`number`)

**Returns:**

- `zoneChannel` - `0` for non-zone channels, otherwise a numeric index specific to that channel (`number`)

---

## AddChatWindowMessages

Adds a message type to the saved list of those displayed in a chat window. Used by the default UI's function `ChatFrame_AddMessageGroup()`, which manages the set of message types shown in a displayed ChatFrame.

**Signature:**

```lua
AddChatWindowMessages(index, "messageGroup")
```

**Arguments:**

- `index` - Index of a chat frame (between `1` and `NUM_CHAT_WINDOWS`) (`number`)
- `messageGroup` - Token identifying a message type (`string`, [chatMsgType](../types/chatMsgType.md))

---

## CanComplainChat

Returns whether a chat message can be reported as spam

**Signature:**

```lua
canComplain = CanComplainChat(lineID)
```

**Arguments:**

- `lineID` - Unique identifier of a chat message (11th argument received with the corresponding `CHAT_MSG` event) (`number`)

**Returns:**

- `canComplain` - 1 if the player can report the given chat message as spam; otherwise nil (`1nil`)

---

## ChangeChatColor

**Signature:**

```lua
ChangeChatColor("messageType", red, green, blue)
```

**Arguments:**

- `messageType` - The message type, as listed in chat-cache.txt. Example values are "SAY" and "CHANNEL1". (`string`)
- `red` - The value of the red component color (0.0 - 1.0) (`number`)
- `green` - The value of the green component color (0.0 - 1.0) (`number`)
- `blue` - The value of the blue component color (0.0 - 1.0) (`number`)

---

## ChatFrame_AddMessageEventFilter `blizzardui`

Adds a function to filter or alter messages to the chat display system. The filter function will be called each time a message is sent to one of the default chat frames (ChatFrame1, ChatFrame2, ..., ChatFrame7). The function will be passed the chat frame object that the message is being added to, along with the event that caused the messages to be added, and the arguments to that event.

A filter function may return `true` if the message should be filtered , or `false` if the message should be displayed. Following this boolean flag, the message can return a list of (possibly) altered arguments to be passed to the next filter function.

See examples for details.

**Signature:**

```lua
ChatFrame_AddMessageEventFilter("event", filter)
```

**Arguments:**

- `event` - A `CHAT_MSG_` [Event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events) for which the filter should be used (`string`)
- `filter` - A function to filter incoming messages (`function`)

**Examples:**

```lua
-- a filter to hide all yelled messaged containing certain text
function noGoldSpam(self,event,msg)
  local badWords = {"gold","%$","www","%.com","%.net","%.org"}
  local matchCount = 0;
  for _, word in ipairs(badWords) do
    if (string.match(msg, word)) then
      matchCount = matchCount + 1;
    end
  end
  if (matchCount > 1) then
    return true;
  else
    return false;
  end
end
ChatFrame_AddMessageEventFilter("CHAT_MSG_YELL",noGoldSpam)
```

```lua
-- a filter to display icons next to item links in loot messages
function addLootIcons(self, event, msg, ...)
  local _, fontSize = GetChatWindowInfo(self:GetID())
  local function iconForLink(link)
    local texture = GetItemIcon(link)
    return "\124T"..texture..":"..fontSize.."\124t"..link
  end
  msg = string.gsub(msg,"(\124c%x+\124Hitem:.-\124h\124r)",iconForLink)
  return false, msg, ...
end
ChatFrame_AddMessageEventFilter("CHAT_MSG_LOOT", addLootIcons)
```

---

## ChatFrame_GetMessageEventFilters `blizzardui`

Returns the list of filters registered for a chat event. See [`ChatFrame_AddMessageEventFilter()`](Chat.md#chatframe_addmessageeventfilter-blizzardui) for details about chat message filters.

**Signature:**

```lua
filterTable = ChatFrame_GetMessageEventFilters("event")
```

**Arguments:**

- `event` - A `CHAT_MSG_` [Event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events) (`string`)

**Returns:**

- `filterTable` - A table containing any filters set for the given event, with numeric keys corresponding to the order in which filters were registered (`table`)

---

## ChatFrame_RemoveMessageEventFilter `blizzardui`

Removes a previously set chat message filter. See [`ChatFrame_AddMessageEventFilter()`](Chat.md#chatframe_addmessageeventfilter-blizzardui) for details about chat message filters.

**Signature:**

```lua
ChatFrame_RemoveMessageEventFilter("event", filter)
```

**Arguments:**

- `event` - `CHAT_MSG_` [Event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events) from which to remove a filter (`string`)
- `filter` - A filter function registered for the event (`function`)

---

## ComplainChat

Reports a chat message as spam. Used in the default UI when right-clicking the name of a player in a chat message and choosing "Report Spam" from the menu.

**Signature:**

```lua
ComplainChat(lineID) or ComplainChat("name" [, "text"])
```

**Arguments:**

- `lineID` - Unique identifier of a chat message (11th argument received with the corresponding `CHAT_MSG` event) (`number`)
- `name` - Name of a player to complain about (`string`)
- `text` - Specific text to complain about (`string`)

---

## DoEmote

Performs a preset emote (with optional target). The list of built-in emote tokens can be found in global variables whose names follow the format `"EMOTE"..num.."_TOKEN"`, where `num` is a number between `1` and `MAXEMOTEINDEX` (a variable local to ChatFrame.lua.)

For custom emotes (as performed using the `/emote` or `/me` commands in the default UI), see [`SendChatMessage()`](Chat.md#sendchatmessage-server).

**Signature:**

```lua
DoEmote("emote" [, "target" [, hold]])
```

**Arguments:**

- `emote` - Non-localized token identifying an emote to perform (`string`)
- `target` - Name of a unit at whom to direct the emote (`string`)
- `hold` - Hold the emote animation until cancelled (`boolean`)

---

## GetChatTypeIndex

Returns the numeric index corresponding to a chat message type. These indices are used in the default UI to identify lines printed in a chat window, allowing (for example) their color to be changed to match changes in the player's color preferences.

**Signature:**

```lua
index = GetChatTypeIndex("messageGroup")
```

**Arguments:**

- `messageGroup` - Token identifying a message type (`string`, [chatMsgType](../types/chatMsgType.md))

**Returns:**

- `index` - Numeric index of the chat type (`number`)

---

## GetChatWindowChannels

Returns the saved list of channels to which a chat window is subscribed

**Signature:**

```lua
channelName, channelId, ... = GetChatWindowChannels(index)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)

**Returns:**

- `channelName` - Name of the channel (`string`)
- `channelId` - Numeric id for the channel (`number`)
- `...` - Additional `channelName, channelId` pairs for each channel belonging to the chat window (`list`)

---

## GetChatWindowInfo

Returns the saved settings for a chat window. These values reflect the settings saved between sessions, which are used by the default UI to set up the chat frames it displays.

**Signature:**

```lua
name, fontSize, r, g, b, alpha, shown, locked, docked, uninteractable = GetChatWindowInfo(index)
```

**Arguments:**

- `index` - Index of the window you wish you get information on (starts at 1) (`number`)

**Returns:**

- `name` - Name of the chat window (`string`)
- `fontSize` - Font size for text displayed in the chat window (`number`)
- `r` - Red component of the window's background color (0.0 - 1.0) (`number`)
- `g` - Green component of the window's background color (0.0 - 1.0) (`number`)
- `b` - Blue component of the window's background color (0.0 - 1.0) (`number`)
- `alpha` - Alpha value (opacity) of the window's background (0 = fully transparent, 1 = fully opaque) (`number`)
- `shown` - 1 if the window should be shown; 0 if it should be hidden (`number`)
- `locked` - 1 if the window should be locked; 0 if it should be movable/resizable (`number`)
- `docked` - 1 if the window should be docked to the main chat window; otherwise 0 (`number`)
- `uninteractable` - 1 if the window should ignore all mouse events; otherwise 0 (`number`)

---

## GetChatWindowMessages

Returns the saved list of messages to which a chat window is subscribed

**Signature:**

```lua
... = GetChatWindowMessages(index)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)

**Returns:**

- `...` - A list of [`chatMsgType`](../types/chatMsgType.md)s for which the chat window is subscribed (`list`)

---

## GetDefaultLanguage

Returns the name of the player character's default language. This is the language used in the chat system (Common or Orcish, as opposed to Taurahe, Darnassian, etc), not the real-world language of the client or server.

**Signature:**

```lua
language = GetDefaultLanguage()
```

**Returns:**

- `language` - Localized name of the player character's default language (`string`)

---

## GetLanguageByIndex

Returns the localized name of a player character language

**Signature:**

```lua
language = GetLanguageByIndex(index)
```

**Arguments:**

- `index` - Index of a player character language (between 1 and [`GetNumLanguages()`](Chat.md#getnumlanguages) (`number`)

**Returns:**

- `language` - Localized name of the language (e.g. "Common" or "Gnomish") (`string`)

---

## GetNumLanguages

Returns the number of languages the player character can speak

**Signature:**

```lua
languages = GetNumLanguages()
```

**Returns:**

- `languages` - Number of in-game languages known to the player character (generally 2 for most races, 1 for Orcs or Humans) (`number`)

---

## LoggingChat

Enables or disables saving chat text to a file. Text received via the chat system (but not necessarily all text displayed in chat windows) will be saved to the file `Logs/WoWChatLog.txt` (path is relative to the folder containing the World of Warcraft client); the file is not actually updated until the player logs out.

Chat text in the log file follows a similar format to its display in-game, but with added timestamps.

**Signature:**

```lua
isLogging = LoggingChat(toggle)
```

**Arguments:**

- `toggle` - True to enable chat logging; false or omitted to disable (`boolean`)

**Returns:**

- `isLogging` - 1 if chat logging is enabled; otherwise nil (`1nil`)

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

## RandomRoll `server`

Initiates a public, server-side "dice roll". Used in the default UI to implement the `/roll` chat command; when called, the server generates a random integer and sends it to the player and all others nearby (or in the same party/raid) via a [`CHAT_MSG_SYSTEM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_SYSTEM) event. (The server message is formatted according to the global `RANDOM_ROLL_RESULT`; e.g. "Leeroy rolls 3 (1-100)".)

For random number generation that does not involve the server or send visible messages to other clients, see `math.random`.

**Signature:**

```lua
RandomRoll(min, max)
```

**Arguments:**

- `min` - Lowest number to be randomly chosen (`number,string`)
- `max` - Highest number to be randomly chosen (`number,string`)

---

## RemoveChatWindowChannel

Removes a channel from a chat window's list of saved channel subscriptions. Used by the default UI's function `ChatFrame_RemoveChannel()` which manages the set of channel messages shown in a displayed ChatFrame.

**Signature:**

```lua
RemoveChatWindowChannel(index, "channel")
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `channel` - Name of the channel to remove (`string`)

---

## RemoveChatWindowMessages

Removes a message type from a chat window's list of saved message subscriptions. Used by the default UI's functions `ChatFrame_RemoveMessageGroup()` and `ChatFrame_RemoveAllMessageGroups()` which manage the set of message types shown in a displayed ChatFrame.

**Signature:**

```lua
RemoveChatWindowMessages(index, "messageGroup")
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `messageGroup` - Token identifying a message type (`string`, [chatMsgType](../types/chatMsgType.md))

---

## ResetChatColors

Removes all saved color settings for chat message types, resetting them to default values

**Signature:**

```lua
ResetChatColors()
```

---

## ResetChatWindows

Removes all saved chat window settings, resetting them to default values. Used by the default UI's function `FCF_ ResetChatWindows()` which resets the appearance and behavior of displayed FloatingChatFrames.

**Signature:**

```lua
ResetChatWindows()
```

---

## SendChatMessage `server`

Sends a chat message

**Signature:**

```lua
SendChatMessage("text" [, "chatType" [, languageIndex [, "channel"]]])
```

**Arguments:**

- `text` - Message to be sent (up to 255 characters) (`string`)
- `chatType` - Channel on which to send the message (defaults to `SAY` if omitted) (`string`)
  - `CHANNEL` - Message to a server or custom chat channel (sent with `/1`, `/2`, etc in the default UI); requires channel number for `channel` argument
  - `DND` - Enables Away-From-Keyboard status for the player, with `text` as the custom message seen by others attempting to whisper the player
  - `EMOTE` - Custom text emotes visible to nearby players (sent with `/e` in the default UI)
  - `GUILD` - Messages to guild members (sent with `/g` in the default UI)
  - `INSTANCE_CHAT` - Messages to a LFG/LFR instance group (sent with `/i` in the default UI)
  - `OFFICER` - Messages to guild officers (sent with `/o` in the default UI)
  - `PARTY` - Messages to party members (sent with `/p` in the default UI)
  - `RAID` - Messages to raid members (sent with `/ra` in the default UI)
  - `RAID_WARNING` - Warning to raid members (sent with `/rw` in the default UI)
  - `SAY` - Speech to nearby players (sent with `/s` in the default UI)
  - `WHISPER` - Message to a specific character (sent with `/w` in the default UI); requires name of the character for `channel` argument
  - `YELL` - Yell to not-so-nearby players (sent with `/y` in the default UI)
- `languageIndex` - Language in which to send the message; defaults to Common (for Alliance players) or Orcish (for Horde players) if omitted. Language indices can be retrieved from [`GetLanguageByIndex()`](Chat.md#getlanguagebyindex). (`number`)
- `channel` - If `chatType` is `WHISPER`, name of the target character; if `chatType` is `CHANNEL`, number identifying the target channel; ignored otherwise (`string`)

---

## SetChatWindowAlpha

Saves a chat window's background opacity setting. Used by the default UI's function `FCF_SetWindowAlpha()` which changes the opacity of a displayed FloatingChatFrame.

**Signature:**

```lua
SetChatWindowAlpha(index, alpha)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `alpha` - Alpha value (opacity) of the chat window background (0 = fully transparent, 1 = fully opaque) (`number`)

---

## SetChatWindowColor

Saves a chat window's background color setting. Used by the default UI's function `FCF_SetWindowColor()` which changes the colors of a displayed FloatingChatFrame.

**Signature:**

```lua
SetChatWindowColor(index, r, g, b)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `r` - Red component of the background color (0.0 - 1.0) (`number`)
- `g` - Green component of the background color (0.0 - 1.0) (`number`)
- `b` - Blue component of the background color (0.0 - 1.0) (`number`)

---

## SetChatWindowDocked

Saves whether a chat window should be docked with the main chat window. Used by the default UI's functions `FCF_DockFrame()` and `FCF_UnDockFrame()` which manage the positioning of FloatingChatFrames.

**Signature:**

```lua
SetChatWindowDocked(index, docked)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `docked` - True if the window should be docked with the main chat window; otherwise false (`boolean`)

---

## SetChatWindowLocked

Saves whether a chat window is locked. Used by the default UI's functions `FCF_OpenNewWindow()` and `FCF_SetLocked()` which manage the behavior of a FloatingChatFrame.

**Signature:**

```lua
SetChatWindowLocked(index, locked)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `locked` - True if the frame should be locked; otherwise false (`boolean`)

---

## SetChatWindowName

Saves a chat window's display name setting. Used by the default UI's function `FCF_SetWindowName()` which also handles setting the name displayed for a FloatingChatFrame.

**Signature:**

```lua
SetChatWindowName(index, "name")
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `name` - Name to be displayed for the chat window (`string`)

---

## SetChatWindowShown

Saves whether a chat window should be shown. Used by the default UI's function `FCF_OpenNewWindow()` which initializes a displayed FloatingChatFrame.

**Signature:**

```lua
SetChatWindowShown(index, shown)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `shown` - True if the window should be shown, false otherwise (`boolean`)

---

## SetChatWindowSize

Saves a chat window's font size setting. Used by the default UI's function `FCF_SetChatWindowFontSize()` which also handles changing the font displayed in a FloatingChatFrame.

**Signature:**

```lua
SetChatWindowSize(index, size)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `size` - Font size for the chat window (in points) (`number`)

---

## SetChatWindowUninteractable

Saves whether a chat window is marked as non-interactive. Used by the default UI's function `FCF_SetUninteractable()` which also handles enabling/disabling mouse events in the FloatingChatFrame.

**Signature:**

```lua
SetChatWindowUninteractable(index, setUninteractable)
```

**Arguments:**

- `index` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) (`number`)
- `setUninteractable` - True flag the window as non-interactive; false otherwise (`boolean`)

---

← [WoW API Docs](../index.md)
