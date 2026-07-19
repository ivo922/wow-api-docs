# Sound functions

← [WoW API Docs](../index.md)

**19** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#sound)

---

## PlayMusic

Plays an audio file as background music. Any other background music that is currently playing will be faded out as the new music begins; if the `Sound_ZoneMusicNoDelay` is set, music will loop continuously until [`StopMusic()`](Sound.md#stopmusic) is called.

WoW supports WAV, MP3 and Ogg audio formats.

**Signature:**

```lua
PlayMusic("musicfile")
```

**Arguments:**

- `musicfile` - Path to a music file (`string`)

---

## PlaySound

Plays one of WoW's built-in sound effects. Only supports sounds found in the `Sound\Interface` directory within WoW's MPQ files; to play other built-in sounds or sounds in an addon directory, use [`PlaySoundFile()`](Sound.md#playsoundfile).

**Signature:**

```lua
PlaySound("sound")
```

**Arguments:**

- `sound` - Name of a built-in sound effect (`string`)

**Examples:**

```lua
PlaySound("AuctionWindowOpen");
```

---

## PlaySoundFile

Plays an audio file at a given path. For a shorter way to specify one of WoW's built-in UI sound effects, see [`PlaySound()`](Sound.md#playsound).

WoW supports custom sound files using Ogg or MP3 audio format. MP3 support was dropped in patch 6.0.2, but added again in patch 6.0.3

**Signature:**

```lua
PlaySoundFile("soundFile", "soundChannel")
```

**Arguments:**

- `soundFile` - A path to the sound file to be played (`string`)
- `soundChannel` - The sound volume slider setting the sound should use. One of `SFX`, `Music`, `Ambience` or `Master`. (`string`)

---

## Sound_ChatSystem_GetInputDriverNameByIndex

Returns the name of the given chat system sound input driver

**Signature:**

```lua
Sound_ChatSystem_GetInputDriverNameByIndex(index)
```

**Arguments:**

- `index` - The desired index (`number`)

---

## Sound_ChatSystem_GetNumInputDrivers

Returns the number of chat system sound input drivers

**Signature:**

```lua
Sound_ChatSystem_GetNumInputDrivers()
```

---

## Sound_ChatSystem_GetNumOutputDrivers

Returns the number of chat system sound output drivers

**Signature:**

```lua
Sound_ChatSystem_GetNumOutputDrivers()
```

---

## Sound_ChatSystem_GetOutputDriverNameByIndex

Returns the name of the given chat system sound output driver

**Signature:**

```lua
Sound_ChatSystem_GetOutputDriverNameByIndex(index)
```

**Arguments:**

- `index` - The desired index (`number`)

---

## Sound_GameSystem_GetInputDriverNameByIndex

Returns the name of the given game sound input driver

**Signature:**

```lua
Sound_GameSystem_GetInputDriverNameByIndex(index)
```

**Arguments:**

- `index` - The desired index (`number`)

---

## Sound_GameSystem_GetNumInputDrivers

Returns the number of game sound input drivers

**Signature:**

```lua
Sound_GameSystem_GetNumInputDrivers()
```

---

## Sound_GameSystem_GetNumOutputDrivers

Returns the number of game sound output drivers

**Signature:**

```lua
Sound_GameSystem_GetNumOutputDrivers()
```

---

## Sound_GameSystem_GetOutputDriverNameByIndex

Returns the name of the given game sound output driver

**Signature:**

```lua
Sound_GameSystem_GetOutputDriverNameByIndex(index)
```

**Arguments:**

- `index` - The desired index (`number`)

---

## Sound_GameSystem_RestartSoundSystem

Restarts the game's sound systems

**Signature:**

```lua
Sound_GameSystem_RestartSoundSystem()
```

---

## StopMusic

Stops currently playing in-game music

**Signature:**

```lua
StopMusic()
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
