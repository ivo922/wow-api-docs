# UI/Visual functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#ui)

---

## ConsoleAddMessage

Prints text to the debug console.

The debugging console can be activated by launching WoW from the command line with the "-console" option, then pressing the "`" (backtick/tilde) key ingame. Its usefulness outside of Blizzard internal environments is limited.

**Signature:**

```lua
ConsoleAddMessage()
```

---

## ConsoleExec

Runs a console command. Used by the default UI to handle `/console` commands.

**Signature:**

```lua
ConsoleExec("console_command")
```

**Arguments:**

- `console_command` - The console command to run (`string`)

---

## SetupFullscreenScale

Sizes a frame to take up the entire screen regardless of screen resolution

**Signature:**

```lua
SetupFullscreenScale(frame)
```

**Arguments:**

- `frame` - Frame to resize to full screen (`table`)

---

## ShowCloak

Enables or disables display of the player's cloak. Only affects the player's appearance; does not change the other effects of having the cloak equipped. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
ShowCloak(show)
```

**Arguments:**

- `show` - 1 to display the player's cloak; nil to hide it (`1nil`)

---

## ShowHelm

Enables or disables display of the player's headgear. Only affects the player's appearance; does not change the other effects of having the headgear equipped. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
ShowHelm(show)
```

**Arguments:**

- `show` - 1 to display the player's headgear; nil to hide it (`1nil`)

---

## ShowingCloak

Returns whether the player's cloak is displayed. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
isShown = ShowingCloak()
```

**Returns:**

- `isShown` - 1 if the player's cloak is shown; otherwise nil (`1nil`)

---

## ShowingHelm

Returns whether the player's headgear is displayed. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
isShown = ShowingHelm()
```

**Returns:**

- `isShown` - 1 if the player's headgear is shown; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
