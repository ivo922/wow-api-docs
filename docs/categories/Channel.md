# Channel functions

← [WoW API Docs](../index.md)

**50** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#channel)

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

## ChannelBan

Bans a character from a chat channel. Has no effect unless the player is a moderator of the given channel

**Signature:**

```lua
ChannelBan("channel", "fullname")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `fullname` - Name of the character to be banned (`string`)

---

## ChannelInvite

Invites a character to join a chat channel

**Signature:**

```lua
ChannelInvite("channel", "name")
```

**Arguments:**

- `channel` - Name of a channel (`string`)
- `name` - Name of a character to invite (`string`)

---

## ChannelKick

Removes a player from the channel. Has no effect unless the player is a moderator of the given channel

**Signature:**

```lua
ChannelKick("channel", "fullname")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `fullname` - Name of the character to kick (`string`)

---

## ChannelModerator

Grants a character moderator status in a chat channel. Has no effect unless the player is the owner of the given channel

**Signature:**

```lua
ChannelModerator("channel", "fullname")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `fullname` - Name of the character to promote to moderator (`string`)

---

## ChannelMute

Grants a character ability to speak in a moderated chat channel

**Signature:**

```lua
ChannelMute("channelName", "name") or ChannelMute(channelId, "name")
```

**Arguments:**

- `channelName` - Name of a channel (`string`)
- `channelId` - Index of a channel (`number`)
- `name` - Name of a character to mute (`string`)

---

## ChannelSilenceAll

Silences a character for chat and voice on a channel

**Signature:**

```lua
ChannelSilenceAll("channelName", ["unit"] or ["name"]) or ChannelSilenceAll(channelId, ["unit"] or ["name"]) or ChannelSilenceAll(["channelName"] or [channelId], "unit") or ChannelSilenceAll(["channelName"] or [channelId], "name")
```

**Arguments:**

- `channelName` - Name of a channel (`string`)
- `channelId` - Index of a channel (`number`)
- `unit` - Unit to silence (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a character to silence (`string`)

---

## ChannelSilenceVoice

Silences the given character for voice chat on the channel. Only a raid/party/battleground leader or assistant can silence a player.

**Signature:**

```lua
ChannelSilenceVoice("channelName", ["unit"] or ["name"]) or ChannelSilenceVoice(channelId, ["unit"] or ["name"]) or ChannelSilenceVoice(["channelName"] or [channelId], "unit") or ChannelSilenceVoice(["channelName"] or [channelId], "name")
```

**Arguments:**

- `channelName` - Name of a channel (`string`)
- `channelId` - Index of a channel (`number`)
- `unit` - Unit to silence (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a character to silence (`string`)

---

## ChannelToggleAnnouncements

Enables or disables printing of join/leave announcements for a channel

**Signature:**

```lua
ChannelToggleAnnouncements("channel")
```

**Arguments:**

- `channel` - Name of the channel for which to enable or disable announcements (`string`)

---

## ChannelUnSilenceAll

Unsilences a character for chat and voice on a channel

**Signature:**

```lua
ChannelUnSilenceAll("channelName", ["unit"] or ["name"]) or ChannelUnSilenceAll(channelId, ["unit"] or ["name"]) or ChannelUnSilenceAll(["channelName"] or [channelId], "unit") or ChannelUnSilenceAll(["channelName"] or [channelId], "name")
```

**Arguments:**

- `channelName` - Name of a channel (`string`)
- `channelId` - Index of a channel (`number`)
- `unit` - Unit to unsilence (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a character to unsilence (`string`)

---

## ChannelUnSilenceVoice

Unsilences a character on a chat channel

**Signature:**

```lua
ChannelUnSilenceVoice("channelName", ["unit"] or ["name"]) or ChannelUnSilenceVoice(channelId, ["unit"] or ["name"]) or ChannelUnSilenceVoice(["channelName"] or [channelId], "unit") or ChannelUnSilenceVoice(["channelName"] or [channelId], "name")
```

**Arguments:**

- `channelName` - Name of a channel (`string`)
- `channelId` - Index of a channel (`number`)
- `unit` - Unit to unsilence (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a character to unsilence (`string`)

---

## ChannelUnban

Lifts the ban preventing a character from joining a chat channel. Has no effect unless the player is a moderator of the given channel

**Signature:**

```lua
ChannelUnban("channel", "fullname")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `fullname` - Name of the character to for which to lift the ban (`string`)

---

## ChannelUnmoderator

Revokes moderator status from a character on a chat channel. Has no effect unless the player is the owner of the given channel

**Signature:**

```lua
ChannelUnmoderator("channel", "fullname")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `fullname` - Name of the character to demote from moderator (`string`)

---

## ChannelUnmute

Removes a character's ability to speak in a moderated chat channel

**Signature:**

```lua
ChannelUnmute("channelName", "name") or ChannelUnmute(channelId, "name")
```

**Arguments:**

- `channelName` - Name of a channel (`string`)
- `channelId` - Index of a channel (`number`)
- `name` - Name of a character to unmute (`string`)

---

## ChannelVoiceOff

Disables voice chat in a channel

**Signature:**

```lua
ChannelVoiceOff("channel") or ChannelVoiceOff(channelIndex)
```

**Arguments:**

- `channel` - Name of a channel (`string`)
- `channelIndex` - Index of a channel (`number`)

---

## ChannelVoiceOn

Enables voice chat in a channel

**Signature:**

```lua
ChannelVoiceOn("channel") or ChannelVoiceOn(channelIndex)
```

**Arguments:**

- `channel` - Name of a channel (`string`)
- `channelIndex` - Index of a channel (`number`)

---

## ClearChannelWatch `deprecated`

**Signature:**

```lua
ClearChannelWatch()
```

---

## CollapseChannelHeader

Collapses a group header in the chat channel listing

**Signature:**

```lua
CollapseChannelHeader(index)
```

**Arguments:**

- `index` - Index of a header in the display channel list (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## DeclineInvite

Declines an invitation to a chat channel. Usable in response to the [`CHANNEL_INVITE_REQUEST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHANNEL_INVITE_REQUEST) event which fires when the player is invited to join a chat channel.

**Signature:**

```lua
DeclineInvite("channel")
```

**Arguments:**

- `channel` - Name of a chat channel (`string`)

---

## DisplayChannelOwner `server`

Requests information from the server about a channel's owner. Fires the [`CHANNEL_OWNER`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHANNEL_OWNER) event indicating the name of the channel owner.

**Signature:**

```lua
DisplayChannelOwner("channel") or DisplayChannelOwner(channelIndex)
```

**Arguments:**

- `channel` - Name of a channel (`string`)
- `channelIndex` - Index of a channel (`number`)

---

## DisplayChannelVoiceOff

Disables voice in a channel specified by its position in the channel list display

**Signature:**

```lua
DisplayChannelVoiceOff(index)
```

**Arguments:**

- `index` - Index of a channel in the channel list display (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100105224853/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## DisplayChannelVoiceOn

Enables voice in a channel specified by its position in the channel list display

**Signature:**

```lua
DisplayChannelVoiceOn(index)
```

**Arguments:**

- `index` - Index of a channel in the channel list display (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## EnumerateServerChannels

Returns the available server channel names

**Signature:**

```lua
... = EnumerateServerChannels()
```

**Returns:**

- `...` - A list of strings, each the name of an available server channel (e.g. "General", "Trade", "WorldDefense", "GuildRecruitment", "LookingForGroup") (`string`)

---

## ExpandChannelHeader

Expands a group header in the chat channel listing

**Signature:**

```lua
ExpandChannelHeader(index)
```

**Arguments:**

- `index` - Index of a header in the display channel list (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## GetActiveVoiceChannel

Returns the currently active voice channel

**Signature:**

```lua
index = GetActiveVoiceChannel()
```

**Returns:**

- `index` - Index of the active voice channel in the chat display window (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)), or nil if no channel is active (`number`)

---

## GetChannelDisplayInfo

Returns information about an entry in the channel list display

**Signature:**

```lua
name, header, collapsed, channelNumber, count, active, category, voiceEnabled, voiceActive = GetChannelDisplayInfo(index)
```

**Arguments:**

- `index` - Index of an entry in the channel list display (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

**Returns:**

- `name` - Name of the channel or header (`string`)
- `header` - 1 if the entry is a group header; otherwise nil (`1nil`)
- `collapsed` - 1 if the entry is a collapsed group header; otherwise nil (`1nil`)
- `channelNumber` - Number identifying the channel (as returned by [`GetChannelList()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetChannelList) and used by [`SendChatMessage()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SendChatMessage) and other channel functions) (`number`)
- `count` - Number of characters in the channel (`number`)
- `active` - 1 if the channel is currently active; otherwise nil. (Used for special server channels, e.g. "Trade" and "LookingForGroup", which can only be used under certain conditions) (`1nil`)
- `category` - Category to which the chat channel belongs (`string`)
  - `CHANNEL_CATEGORY_CUSTOM` - Custom channels created by players
  - `CHANNEL_CATEGORY_GROUP` - Group channels (party, raid, battleground)
  - `CHANNEL_CATEGORY_WORLD` - World channels (General, Trade, etc.)
- `voiceEnabled` - 1 if voice chat is enabled for the channel; otherwise nil (`1nil`)
- `voiceActive` - 1 if voice chat is active for the channel; otherwise nil (`1nil`)

---

## GetChannelList

Returns the list of the channels the player has joined

**Signature:**

```lua
index, channel, ... = GetChannelList()
```

**Returns:**

- `index` - Index of the channel (`number`)
- `channel` - Name of the channel (`string`)
- `...` - Additional `index, channel` pairs for each channel the player has joined (`list`)

---

## GetChannelName

Returns information about a chat channel

**Signature:**

```lua
channel, channelName, instanceID = GetChannelName(channelIndex) or GetChannelName("channelName")
```

**Arguments:**

- `channelIndex` - A channel ID (`number`)
- `channelName` - A channel name (`string`)

**Returns:**

- `channel` - ID of the channel (`number`)
- `channelName` - Name of the channel (`string`)
- `instanceID` - The channel's instance ID, or 0 if there are not separate instances of the channel. (`number`)

---

## GetChannelRosterInfo

Returns information about a character in a chat channel in the channel list display

**Signature:**

```lua
name, owner, moderator, muted, active, enabled = GetChannelRosterInfo(index, rosterIndex)
```

**Arguments:**

- `index` - Index of a channel in the channel list display (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)
- `rosterIndex` - Index of a participant in the channel (between 1 and `count`, where `count = select(5,`[`GetChannelDisplayInfo`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetChannelDisplayInfo)`(index)`) (`number`)

**Returns:**

- `name` - Name of the character (`string`)
- `owner` - 1 if the character is the channel owner; otherwise nil (`1nil`)
- `moderator` - 1 if the character is a channel moderator; otherwise nil (`1nil`)
- `muted` - 1 if the character is muted; otherwise nil (`1nil`)
- `active` - 1 if the character is currently speaking in the channel; otherwise nil (`1nil`)
- `enabled` - 1 if the character has voice chat active for the channel; otherwise nil (`1nil`)

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

## GetNumChannelMembers

Returns the number of members in a chat channel

**Signature:**

```lua
numMembers = GetNumChannelMembers(id)
```

**Arguments:**

- `id` - Numeric identifier of a chat channel (`number`)

**Returns:**

- `numMembers` - Number of characters in the channel (`number`)

---

## GetNumDisplayChannels

Returns the number of entries in the channel list display

**Signature:**

```lua
channelCount = GetNumDisplayChannels()
```

**Returns:**

- `channelCount` - Number of channels and group headers to be displayed in the channel list (`number`)

---

## GetSelectedDisplayChannel

Returns the selected channel in the channel list display

**Signature:**

```lua
index = GetSelectedDisplayChannel()
```

**Returns:**

- `index` - Index of the selected channel in the display channel list (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## IsDisplayChannelModerator

Returns whether the player is a moderator of the selected channel in the channel list display

**Signature:**

```lua
isModerator = IsDisplayChannelModerator()
```

**Returns:**

- `isModerator` - 1 if the player is a moderator of the selected channel; otherwise nil (`1nil`)

---

## IsDisplayChannelOwner

Returns whether the player is the owner of the selected channel in the channel list display

**Signature:**

```lua
isOwner = IsDisplayChannelOwner()
```

**Returns:**

- `isOwner` - 1 if the player is the owner of the selected channel; otherwise nil (`1nil`)

---

## IsSilenced

Returns whether a character is silenced on a chat channel

**Signature:**

```lua
isSilenced = IsSilenced("name", "channel")
```

**Arguments:**

- `name` - Name of a character (`string`)
- `channel` - Name of a chat channel (`string`)

**Returns:**

- `isSilenced` - 1 if the character is silenced on the given channel; otherwise nil (`1nil`)

---

## JoinChannelByName `deprecated`

This function is deprecated and should no longer be used

---

## JoinPermanentChannel

Joins a channel, saving associated chat window settings

**Signature:**

```lua
zoneChannel, channelName = JoinPermanentChannel("name" [, "password" [, chatFrameIndex [, enableVoice]]])
```

**Arguments:**

- `name` - Name of the channel to join (`string`)
- `password` - Password to use when joining (`string`)
- `chatFrameIndex` - Index of a chat frame (between 1 and `NUM_CHAT_WINDOWS`) in which to subscribe to the channel (`number`)
- `enableVoice` - True to enable voice in the channel; otherwise false (`boolean`)

**Returns:**

- `zoneChannel` - 0 for non-zone channels, otherwise a numeric index specific to that channel (`number`)
- `channelName` - Display name of the channel, if the channel was a zone channel (`string`)

---

## JoinTemporaryChannel

Joins a channel, but does not save associated chat window settings

**Signature:**

```lua
JoinTemporaryChannel("channel")
```

**Arguments:**

- `channel` - Name of a channel to join (`string`)

---

## LeaveChannelByName

Leaves a chat channel

**Signature:**

```lua
LeaveChannelByName("name")
```

**Arguments:**

- `name` - Name of a chat channel to leave (`string`)

---

## ListChannelByName `server`

Requests the list of participants in a chat channel. Fires the [`CHAT_MSG_CHANNEL_LIST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_CHANNEL_LIST) event listing the names of all characters in the channel.

**Signature:**

```lua
ListChannelByName("channel") or ListChannelByName(channelIndex)
```

**Arguments:**

- `channel` - Name of a channel (`string`)
- `channelIndex` - Index of a channel (`number`)

---

## ListChannels `server`

Requests a list of channels joined by the player. Fires the [`CHAT_MSG_CHANNEL_LIST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_CHANNEL_LIST) event listing the names and indices of all channels joined by the player.

**Signature:**

```lua
ListChannels()
```

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

## SetActiveVoiceChannel

Sets the currently active voice channel

**Signature:**

```lua
SetActiveVoiceChannel(index)
```

**Arguments:**

- `index` - Index of a channel in the chat display window (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## SetActiveVoiceChannelBySessionID

Sets the currently active voice chat channel

**Signature:**

```lua
SetActiveVoiceChannelBySessionID(session)
```

**Arguments:**

- `session` - Index of a voice session (between 1 and [`GetNumVoiceSessions()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumVoiceSessions)) (`number`)

---

## SetChannelOwner

Gives channel ownership to another character. Has no effect unless the player is the owner of the given channel.

**Signature:**

```lua
SetChannelOwner("channel", "fullname")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `fullname` - Name of the character to make the new owner (`string`)

---

## SetChannelPassword

Sets a password on a custom chat channel

**Signature:**

```lua
SetChannelPassword("channel", "password")
```

**Arguments:**

- `channel` - Name of the channel (`string`)
- `password` - Password to set for the channel (`string`)

---

## SetSelectedDisplayChannel

Selects a channel in the channel list display

**Signature:**

```lua
SetSelectedDisplayChannel(index)
```

**Arguments:**

- `index` - Index of a channel in the channel list display (between 1 and [`GetNumDisplayChannels()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDisplayChannels)) (`number`)

---

## SilenceMember `deprecated`

This function is deprecated and should no longer be used

---

## UnSilenceMember `deprecated`

This function is deprecated and should no longer be used

---

← [WoW API Docs](../index.md)
