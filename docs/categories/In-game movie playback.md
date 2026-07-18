# In-game movie playback functions

← [WoW API Docs](../index.md)

**5** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#movie)

---

## GameMovieFinished

Ends in-game movie playback

**Signature:**

```lua
GameMovieFinished()
```

---

## GetMovieResolution

Returns the horizontal resolution available for displaying movie content

**Signature:**

```lua
resolution = GetMovieResolution()
```

**Returns:**

- `resolution` - Horizontal resolution (in pixels) available for displaying movie content (`number`)

---

## InCinematic

Returns whether an in-game cinematic is playing. Applies to in-game-engine cinematics (such as when logging into a new character for the first time), not prerecorded movies.

**Signature:**

```lua
inCinematic = InCinematic()
```

**Returns:**

- `inCinematic` - 1 if an in-game cinematic is playing; otherwise nil (`1nil`)

---

## OpeningCinematic

Displays the introductory cinematic for the player's race. Only has effect if the player has never gained any experience.

**Signature:**

```lua
OpeningCinematic()
```

---

## StopCinematic

Exits a currently playing in-game cinematic. Applies to in-game-engine cinematics (such as when logging into a new character for the first time), not prerecorded movies.

**Signature:**

```lua
StopCinematic()
```

---

← [WoW API Docs](../index.md)
