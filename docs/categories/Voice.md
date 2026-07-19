# Voice functions

← [WoW API Docs](../index.md)

**54** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#voice)

---

## AddMute

Adds a character to the muted list for voice chat. The Muted list acts for voice chat as the Ignore list does for text chat: muted characters will never be heard regardless of which voice channels they join the player in.

**Signature:**

```lua
AddMute("name")
```

**Arguments:**

- `name` - Name of a character to add to the mute list (`string`)

---

## AddOrDelMute

Adds or removes a character from the voice mute list. Adds the character to the list if he/she is not already on it; removes the character if already on the list.

The Muted list acts for voice chat as the Ignore list does for text chat: muted characters will never be heard regardless of which voice channels they join the player in.

**Signature:**

```lua
AddOrDelMute("unit") or AddOrDelMute("name")
```

**Arguments:**

- `unit` - A unit to mute (`string`, [unitID](../types/unitID.md))
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
- `unit` - Unit to silence (`string`, [unitID](../types/unitID.md))
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
- `unit` - Unit to silence (`string`, [unitID](../types/unitID.md))
- `name` - Name of a character to silence (`string`)

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
- `unit` - Unit to unsilence (`string`, [unitID](../types/unitID.md))
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
- `unit` - Unit to unsilence (`string`, [unitID](../types/unitID.md))
- `name` - Name of a character to unsilence (`string`)

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

## DelMute

Removes a character from the muted list for voice chat. The Muted list acts for voice chat as the Ignore list does for text chat: muted characters will never be heard regardless of which voice channels they join the player in.

**Signature:**

```lua
DelMute("name")
```

**Arguments:**

- `name` - Name of a character to remove from the mute list (`string`)

---

## DisplayChannelVoiceOff

Disables voice in a channel specified by its position in the channel list display

**Signature:**

```lua
DisplayChannelVoiceOff(index)
```

**Arguments:**

- `index` - Index of a channel in the channel list display (between 1 and [`GetNumDisplayChannels()`](Channel.md#getnumdisplaychannels)) (`number`)

---

## DisplayChannelVoiceOn

Enables voice in a channel specified by its position in the channel list display

**Signature:**

```lua
DisplayChannelVoiceOn(index)
```

**Arguments:**

- `index` - Index of a channel in the channel list display (between 1 and [`GetNumDisplayChannels()`](Channel.md#getnumdisplaychannels)) (`number`)

---

## GetActiveVoiceChannel

Returns the currently active voice channel

**Signature:**

```lua
index = GetActiveVoiceChannel()
```

**Returns:**

- `index` - Index of the active voice channel in the chat display window (between 1 and [`GetNumDisplayChannels()`](Channel.md#getnumdisplaychannels)), or nil if no channel is active (`number`)

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

## GetMuteStatus

Returns whether a character is muted or silenced. If the `channel` argument is specified, this function checks the given character's voice/silence status on the channel as well as for whether the character is on the player's Muted list.

**Signature:**

```lua
muteStatus = GetMuteStatus("unit" [, "channel"]) or GetMuteStatus("name" [, "channel"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - Name of a character to query (`string`)
- `channel` - Name of a voice channel (`string`)

**Returns:**

- `muteStatus` - 1 if the character is muted; otherwise nil (`1nil`)

---

## GetNumMutes

Returns the number of characters on the player's mute list

**Signature:**

```lua
numMuted = GetNumMutes()
```

**Returns:**

- `numMuted` - The number of characters on the player's mute list (`number`)

---

## GetNumVoiceSessionMembersBySessionID

Returns the number of members in a voice channel

**Signature:**

```lua
numMembers = GetNumVoiceSessionMembersBySessionID(sessionId)
```

**Arguments:**

- `sessionId` - Index of a voice session (between 1 and [`GetNumVoiceSessions()`](Voice.md#getnumvoicesessions)) (`number`)

**Returns:**

- `numMembers` - Number of members in the voice channel (`number`)

---

## GetNumVoiceSessions

Returns the number of available voice channels. Returns 0 if voice chat is disabled.

**Signature:**

```lua
count = GetNumVoiceSessions()
```

**Returns:**

- `count` - Number of available voice sessions (`number`)

---

## GetSelectedMute

Returns the index of the selected entry in the Muted list. Mute list selection is only used for display purposes in the default UI and has no effect on other API functions.

**Signature:**

```lua
selectedMute = GetSelectedMute()
```

**Returns:**

- `selectedMute` - Index of the selected entry in the mute listing (between 1 and [`GetNumMutes()`](Voice.md#getnummutes)), or 0 if no entry is selected (`number`)

---

## GetVoiceCurrentSessionID

Returns an identifier for the active voice session

**Signature:**

```lua
id = GetVoiceCurrentSessionID()
```

**Returns:**

- `id` - Index of the active voice session (between 1 and [`GetNumVoiceSessions()`](Voice.md#getnumvoicesessions)), or nil if no session is active (`number`)

---

## GetVoiceSessionInfo

Returns information about a voice session

**Signature:**

```lua
name, active = GetVoiceSessionInfo(session)
```

**Arguments:**

- `session` - Index of a voice session (between 1 and [`GetNumVoiceSessions()`](Voice.md#getnumvoicesessions)) (`number`)

**Returns:**

- `name` - Name of the voice session (channel) (`string`)
- `active` - 1 if the session is the active voice channel; otherwise nil (`1nil`)

---

## GetVoiceSessionMemberInfoBySessionID

Returns information about a member of a voice channel

**Signature:**

```lua
name, voiceActive, sessionActive, muted, squelched = GetVoiceSessionMemberInfoBySessionID(session, index)
```

**Arguments:**

- `session` - Index of a voice session (between 1 and [`GetNumVoiceSessions()`](Voice.md#getnumvoicesessions)) (`number`)
- `index` - Index of a member in the voice session (between 1 and [`GetNumVoiceSessionMembersBySessionID(session)`](Voice.md#getnumvoicesessionmembersbysessionid)) (`number`)

**Returns:**

- `name` - Name of the member (`string`)
- `voiceActive` - 1 if the member has enabled voice chat; otherwise nil (`1nil`)
- `sessionActive` - 1 if the channel is the member's active voice channel; otherwise nil (`1nil`)
- `muted` - 1 if the member is on the player's muted list; otherwise nil (`1nil`)
- `squelched` - 1 if the member was silenced by the channel moderator; otherwise nil (`1nil`)

---

## GetVoiceStatus

Returns whether a character has voice chat enabled

**Signature:**

```lua
status = GetVoiceStatus(unit, "channel") or GetVoiceStatus("name", "channel")
```

**Arguments:**

- `unit` - The unitid to query (`unitid`)
- `name` - The name of the player to query (`string`)
- `channel` - Channel to query for voice status. (`string`)

**Returns:**

- `status` - 1 if voice is enabled; otherwise nil (`1nil`)

---

## IsIgnoredOrMuted

Returns whether a unit can be heard due to ignored/muted status

**Signature:**

```lua
isIgnoredOrMuted = IsIgnoredOrMuted("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `isIgnoredOrMuted` - 1 if the unit is ignored or muted, nil otherwise (`1nil`)

---

## IsMuted

Returns whether a character has been muted by the player

**Signature:**

```lua
muted = IsMuted("unit") or IsMuted("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `muted` - 1 if the unit is muted; otherwise nil (`1nil`)

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

## IsVoiceChatAllowed `review`

Returns whether the player is allowed to enable the voice chat feature

**Signature:**

```lua
isAllowed = IsVoiceChatAllowed()
```

**Returns:**

- `isAllowed` - 1 if voice chat is allowed; otherwise nil (`1nil`)

---

## IsVoiceChatAllowedByServer

Returns whether voice chat is supported by the realm server

**Signature:**

```lua
IsVoiceChatAllowedByServer()
```

---

## IsVoiceChatEnabled

Returns whether the voice chat system is enabled

**Signature:**

```lua
isEnabled = IsVoiceChatEnabled()
```

**Returns:**

- `isEnabled` - 1 if the voice chat system is enabled; otherwise nil (`1nil`)

---

## SetActiveVoiceChannel

Sets the currently active voice channel

**Signature:**

```lua
SetActiveVoiceChannel(index)
```

**Arguments:**

- `index` - Index of a channel in the chat display window (between 1 and [`GetNumDisplayChannels()`](Channel.md#getnumdisplaychannels)) (`number`)

---

## SetActiveVoiceChannelBySessionID

Sets the currently active voice chat channel

**Signature:**

```lua
SetActiveVoiceChannelBySessionID(session)
```

**Arguments:**

- `session` - Index of a voice session (between 1 and [`GetNumVoiceSessions()`](Voice.md#getnumvoicesessions)) (`number`)

---

## SetSelectedMute

Selects an entry in the Muted list. Mute list selection is only used for display purposes in the default UI and has no effect on other API functions.

**Signature:**

```lua
SetSelectedMute(index)
```

**Arguments:**

- `index` - Index of an entry in the mute listing (between 1 and [`GetNumMutes()`](Voice.md#getnummutes)) (`number`)

---

## SilenceMember `deprecated`

This function is deprecated and should no longer be used

---

## UnSilenceMember `deprecated`

This function is deprecated and should no longer be used

---

## UnitIsSilenced

Returns whether a character is silenced on a voice channel

**Signature:**

```lua
silenced = UnitIsSilenced("name", "channel")
```

**Arguments:**

- `name` - Name of a character (`string`)
- `channel` - Name of a chat channel (`string`)

**Returns:**

- `silenced` - 1 if the unit is silenced on the given channel; otherwise nil (`1nil`)

---

## UnitIsTalking

Returns whether a unit is currently speaking in voice chat. Despite the "unit" name, this function only accepts player names, not `unitID`s.

**Signature:**

```lua
state = UnitIsTalking("unit")
```

**Arguments:**

- `unit` - Name of a character in the player's current voice channel (`string`)

**Returns:**

- `state` - 1 if the unit is currently speaking in voice chat; otherwise nil (`1nil`)

---

## VoiceChat_ActivatePrimaryCaptureCallback `deprecated`

This function is deprecated and should no longer be used

---

## VoiceChat_GetCurrentMicrophoneSignalLevel

Returns the current volume level of the microphone signal

**Signature:**

```lua
volume = VoiceChat_GetCurrentMicrophoneSignalLevel()
```

**Returns:**

- `volume` - The current volume level of the microphone signal (`number`)

---

## VoiceChat_IsPlayingLoopbackSound

Returns whether the Microphone Test recording is playing

**Signature:**

```lua
VoiceChat_IsPlayingLoopbackSound(isPlaying)
```

**Arguments:**

- `isPlaying` - 1 if the loopback sound is currently being played; otherwise nil (`number`)

---

## VoiceChat_IsRecordingLoopbackSound

Returns whether a Microphone Test is recording

**Signature:**

```lua
isRecording = VoiceChat_IsRecordingLoopbackSound()
```

**Returns:**

- `isRecording` - 1 if the player is recording a voice sample, otherwise 0 (`number`)

---

## VoiceChat_PlayLoopbackSound

Plays back the Microphone Test recording

**Signature:**

```lua
VoiceChat_PlayLoopbackSound()
```

---

## VoiceChat_RecordLoopbackSound

Begins recording a Microphone Test

**Signature:**

```lua
VoiceChat_RecordLoopbackSound(seconds)
```

**Arguments:**

- `seconds` - The amount of time to record (in seconds) (`number`)

---

## VoiceChat_StartCapture `deprecated`

This function is deprecated and should no longer be used

---

## VoiceChat_StopCapture `deprecated`

This function is deprecated and should no longer be used

---

## VoiceChat_StopPlayingLoopbackSound

Stops playing the Microphone Test recording

**Signature:**

```lua
VoiceChat_StopPlayingLoopbackSound()
```

---

## VoiceChat_StopRecordingLoopbackSound

Stops recording a Microphone Test

**Signature:**

```lua
VoiceChat_StopRecordingLoopbackSound()
```

---

## VoiceEnumerateCaptureDevices

Returns the name of an audio input device for voice chat

**Signature:**

```lua
deviceName = VoiceEnumerateCaptureDevices(deviceIndex)
```

**Arguments:**

- `deviceIndex` - Index of the device (between 1 and [`Sound_ChatSystem_GetNumInputDrivers()`](Sound.md#sound_chatsystem_getnuminputdrivers)) (`number`)

**Returns:**

- `deviceName` - Name of the device (`string`)

---

## VoiceEnumerateOutputDevices

Returns the name of an audio output device for voice chat

**Signature:**

```lua
device = VoiceEnumerateOutputDevices(deviceIndex)
```

**Arguments:**

- `deviceIndex` - Index of the device (between 1 and [`Sound_ChatSystem_GetNumOutputDrivers()`](Sound.md#sound_chatsystem_getnumoutputdrivers)) (`number`)

**Returns:**

- `device` - Name of the device (`string`)

---

## VoiceGetCurrentCaptureDevice

Returns the index of the current voice capture device

**Signature:**

```lua
index = VoiceGetCurrentCaptureDevice()
```

**Returns:**

- `index` - Index of the current voice capture device (between 1 and [`Sound_ChatSystem_GetNumInputDrivers()`](Sound.md#sound_chatsystem_getnuminputdrivers)) (`number`)

---

## VoiceGetCurrentOutputDevice

Returns the index of the current voice output device

**Signature:**

```lua
index = VoiceGetCurrentOutputDevice()
```

**Returns:**

- `index` - Index of the current voice output device (between 1 and [`Sound_ChatSystem_GetNumOutputDrivers()`](Sound.md#sound_chatsystem_getnumoutputdrivers)) (`number`)

---

## VoiceIsDisabledByClient

Returns whether the voice chat system cannot be enabled. Voice chat may be disabled if the underlying hardware does not support it or if multiple instances of World of Warcraft are running on the same hardware.

**Signature:**

```lua
isDisabled = VoiceIsDisabledByClient()
```

**Returns:**

- `isDisabled` - 1 if the voice system is disabled; otherwise nil (`1nil`)

---

## VoicePushToTalkStart `deprecated`

Used internally to start talking, when push-to-talk is active in voice chat.

**Signature:**

```lua
VoicePushToTalkStart()
```

---

## VoicePushToTalkStop `deprecated`

Used internally to stop talking, when push-to-talk is active in voice chat

**Signature:**

```lua
VoicePushToTalkStop()
```

---

## VoiceSelectCaptureDevice

Selects an audio input device for voice chat

**Signature:**

```lua
VoiceSelectCaptureDevice("deviceName")
```

**Arguments:**

- `deviceName` - Name of an audio input device, as returned from [`VoiceEnumerateCaptureDevices()`](Sound.md#voiceenumeratecapturedevices) (`string`)

---

## VoiceSelectOutputDevice

Selects an audio output device for voice chat

**Signature:**

```lua
VoiceSelectOutputDevice("deviceName")
```

**Arguments:**

- `deviceName` - Name of an audio output device, as returned from [`VoiceEnumerateOutputDevices()`](Sound.md#voiceenumerateoutputdevices) (`string`)

---

← [WoW API Docs](../index.md)
