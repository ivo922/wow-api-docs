# Mac client functions

← [WoW API Docs](../index.md)

**24** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#mac)

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

## MovieRecording_Cancel `maconly`

Cancels video recording and compression. If a recording is in progress, recording is stopped and the results discarded. If compression is in progress, compression is stopped and the uncompressed portion of the movie is deleted.

**Signature:**

```lua
MovieRecording_Cancel()
```

---

## MovieRecording_DataRate `maconly`

Returns the data rate required for a given set of video recording parameters. The value returned is a prediction of the rate at which data will be written to the hard drive while recording -- if the hardware cannot support this data rate, game performance may suffer and recording may stop.

**Signature:**

```lua
dataRate = MovieRecording_DataRate(width, framerate, sound)
```

**Arguments:**

- `width` - Width of the output video (in pixels) (`number`)
- `framerate` - Number of video frames to be recorded per second (`number`)
- `sound` - 1 if game audio is to be captured with video; otherwise 0 (`number`)

**Returns:**

- `dataRate` - Summary of the data rate (e.g. "438.297 KB/s", "11.132 MB/s") (`string`)

---

## MovieRecording_DeleteMovie `maconly`

Deletes an uncompressed movie

**Signature:**

```lua
MovieRecording_DeleteMovie("filename")
```

**Arguments:**

- `filename` - Path to an uncompressed movie (as provided in the [`MOVIE_UNCOMPRESSED_MOVIE`](../events/MOVIE_UNCOMPRESSED_MOVIE.md) event) (`string`)

---

## MovieRecording_GetAspectRatio `maconly`

Returns the aspect ratio of the game display. Used in the default UI to calculate dimensions for scaling captured video to predetermined widths.

For example, if the aspect ratio is 0.75 (as on a 1600x1200 screen), a movie scaled to 640 pixels wide will be 480 pixels tall; but if the aspect ratio is 0.625 (as on a 1440x900 screen), a movie scaled to 640 pixels wide will be 400 pixels tall.

**Signature:**

```lua
ratio = MovieRecording_GetAspectRatio()
```

**Returns:**

- `ratio` - Ratio of the game display's width to its height (`number`)

---

## MovieRecording_GetMovieFullPath `maconly`

Returns a path to the movie currently being recorded or compressed. If no movie is being recorded or compressed, returns either the empty string (`""`) or the path of the last movie recorded/compressed.

**Signature:**

```lua
path = MovieRecording_GetMovieFullPath()
```

**Returns:**

- `path` - Path to the movie currently being recorded or compressed, relative to the folder containing the World of Warcraft app (`string`)

---

## MovieRecording_GetProgress `maconly`

Returns information about movie compression progress

**Signature:**

```lua
recovering, progress = MovieRecording_GetProgress()
```

**Returns:**

- `recovering` - True if a previous compression was interrupted (e.g. due to WoW being crashing or being forced to quit), indicating that recovery is being attempted on the file; otherwise false (`boolean`)
- `progress` - Progress of the movie compression process (0 = just started, 1 = finished) (`number`)

---

## MovieRecording_GetTime `maconly`

Returns the amount of time since video recording was last started. Used in the default UI to show the length of the recording in progress when mousing over the recording indicator on the minimap.

May return a nonsensical value if no video has been recorded since logging in.

**Signature:**

```lua
time = MovieRecording_GetTime()
```

**Returns:**

- `time` - Amount of time since video recording was last started (HH:MM:SS) (`string`)

---

## MovieRecording_GetViewportWidth `maconly`

Returns the current width of the game display. Used in the default UI to allow the current screen resolution (or an integral factor thereof) to be selected as the video recording resolution.

**Signature:**

```lua
width = MovieRecording_GetViewportWidth()
```

**Returns:**

- `width` - Width of the game display (`number`)

---

## MovieRecording_IsCodecSupported `maconly`

Returns whether a video codec is supported on the current system

**Signature:**

```lua
isSupported = MovieRecording_IsCodecSupported(codecID)
```

**Arguments:**

- `codecID` - Four-byte identifier of a QuickTime codec (`number`)
  - `1635148593` - H.264 - supported natively by Apple devices like the iPod, iPhone and AppleTV; best ratio quality/size but slowest to compress
  - `1768124260` - Apple Intermediate Codec - fastest to compress, but exclusive to Mac OS X
  - `1835692129` - Motion JPEG - faster to compress than H.264 but it will generate a bigger file
  - `1836070006` - MPEG-4 - supported by many digital cameras and iMovie

**Returns:**

- `isSupported` - true if the codec is supported on the current system, otherwise false (`boolean`)

---

## MovieRecording_IsCompressing `maconly`

Returns whether a movie file is currently being compressed

**Signature:**

```lua
isCompressing = MovieRecording_IsCompressing()
```

**Returns:**

- `isCompressing` - true if the client is currently compressing a recording; otherwise false (`boolean`)

---

## MovieRecording_IsCursorRecordingSupported `maconly`

Returns whether the current system supports recording the mouse cursor in movies

**Signature:**

```lua
isSupported = MovieRecording_IsCursorRecordingSupported()
```

**Returns:**

- `isSupported` - True if the cursor recording option should be enabled; otherwise false (`boolean`)

---

## MovieRecording_IsRecording `maconly`

Returns whether movie recording is currently in progress

**Signature:**

```lua
isRecording = MovieRecording_IsRecording()
```

**Returns:**

- `isRecording` - 1 if the client is currently recording, otherwise nil (`1nil`)

---

## MovieRecording_IsSupported

Returns whether movie recording is supported on the current system

**Signature:**

```lua
isSupported = MovieRecording_IsSupported()
```

**Returns:**

- `isSupported` - true if the client supports video recording; otherwise nil (`boolean`)

---

## MovieRecording_MaxLength `maconly`

Returns the maximum length of recorded video for a given set of video recording parameters. The value returned reflects both the data rate associated with the given parameters and the amount of space remaining on the hard drive.

**Signature:**

```lua
time = MovieRecording_MaxLength(width, framerate, sound)
```

**Arguments:**

- `width` - Width of the output video (in pixels) (`number`)
- `framerate` - Number of video frames to be recorded per second (`number`)
- `sound` - 1 if game audio is to be captured with video; otherwise 0 (`number`)

**Returns:**

- `time` - Maximum length of recorded video (HH:MM:SS) (`string`)

---

## MovieRecording_QueueMovieToCompress `maconly`

Queues an uncompressed movie for compression. If there are no items currently in the queue the movie will begin compressing immediately.

**Signature:**

```lua
MovieRecording_QueueMovieToCompress("filename")
```

**Arguments:**

- `filename` - Path to an uncompressed movie (as provided in the [`MOVIE_UNCOMPRESSED_MOVIE`](../events/MOVIE_UNCOMPRESSED_MOVIE.md) event) (`string`)

---

## MovieRecording_SearchUncompressedMovie `maconly`

Enables or disables a search for uncompressed movies. After calling this function with `true`, a [`MOVIE_UNCOMPRESSED_MOVIE`](../events/MOVIE_UNCOMPRESSED_MOVIE.md) fires for the first uncompressed movie found (causing the default UI to prompt the user to choose whether to compress, ignore, or delete the movie). Calling this function with `false` ignores the movie, causing the search to continue (firing a `MOVIE_UNCOMPRESSED_MOVIE` event for the next uncompressed movie found, and so forth).

**Signature:**

```lua
MovieRecording_SearchUncompressedMovie(enable)
```

**Arguments:**

- `enable` - True to begin searching for uncompressed movies, false to ignore a movie for compression (`boolean`)

---

## MovieRecording_Toggle `maconly`

Begins or ends video recording. Used by the `MOVIE_RECORDING_STARTSTOP` key binding.

**Signature:**

```lua
MovieRecording_Toggle()
```

---

## MovieRecording_ToggleGUI `maconly`

Enables or disables inclusion of UI elements in a video recording. Equivalent to the `MovieRecordingGUI` CVar, but provided as a convenience for the `MOVIE_RECORDING_GUI` so UI recording can be turned on or off while a movie is recording.

**Signature:**

```lua
MovieRecording_ToggleGUI()
```

---

## MusicPlayer_BackTrack `protected` `maconly`

Causes iTunes to return to the previous track played. Used by the iTunes Remote key bindings only available on the Mac OS X WoW client. Only has effect while the iTunes application is open.

**Signature:**

```lua
MusicPlayer_BackTrack()
```

---

## MusicPlayer_NextTrack `protected` `maconly`

Causes iTunes to play the next track in sequence. Used by the iTunes Remote key bindings only available on the Mac OS X WoW client. Only has effect while the iTunes application is open.

**Signature:**

```lua
MusicPlayer_NextTrack()
```

---

## MusicPlayer_PlayPause `protected` `maconly`

Causes iTunes to start or pause playback. Used by the iTunes Remote key bindings only available on the Mac OS X WoW client. Only has effect while the iTunes application is open.

**Signature:**

```lua
MusicPlayer_PlayPause()
```

---

## MusicPlayer_VolumeDown `protected` `maconly`

Causes iTunes to lower its playback volume. Affects the iTunes volume setting only, not the overall system volume or any of WoW's volume settings.

Used by the iTunes Remote key bindings only available on the Mac OS X WoW client. Only has effect while the iTunes application is open.

**Signature:**

```lua
MusicPlayer_VolumeDown()
```

---

## MusicPlayer_VolumeUp `protected` `maconly`

Causes iTunes to raise its playback volume. Affects the iTunes volume setting only, not the overall system volume or any of WoW's volume settings.

Used by the iTunes Remote key bindings only available on the Mac OS X WoW client. Only has effect while the iTunes application is open.

**Signature:**

```lua
MusicPlayer_VolumeUp()
```

---

← [WoW API Docs](../index.md)
