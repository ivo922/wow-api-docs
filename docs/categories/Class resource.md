# Class resource functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#resource)

---

## DestroyTotem

Destroys a specific totem (or ghoul). Totem functions are also used for ghouls summoned by a Death Knight's Raise Dead ability (if the ghoul is not made a controllable pet by the Master of Ghouls talent).

**Signature:**

```lua
DestroyTotem(slot)
```

**Arguments:**

- `slot` - Which totem to destroy (`number`)
  - `1` - Fire (or Death Knight's ghoul)
  - `2` - Earth
  - `3` - Water
  - `4` - Air

---

## GetRuneCooldown

Returns cooldown information about one of the player's rune resources. Note the placement of runes 3-4 (normally Unholy) and 5-6 (normally Frost) are reversed in the default UI. Also note the behavior of returned values differs slightly from most other GetXYZCooldown-style functions.

**Signature:**

```lua
start, duration, runeReady = GetRuneCooldown(slot)
```

**Arguments:**

- `slot` - Index of a rune slot, as positioned in the default UI: (`number`)
  - `1` - Leftmost
  - `2` - Second from left
  - `3` - Fifth from left (second from right)
  - `4` - Sixth from left (rightmost)
  - `5` - Third from left
  - `6` - Fourth from left

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the rune is ready (`number`)
- `duration` - The length of the cooldown (regardless of whether the rune is currently cooling down) (`number`)
- `runeReady` - True if the rune can be used; false if the rune is cooling down (`boolean`)

---

## GetRuneCount

Returns the number of available rune resources in one of the player's rune slots. Returns 1 if a rune is ready and 0 if a rune is on cooldown.

**Signature:**

```lua
count = GetRuneCount(slot)
```

**Arguments:**

- `slot` - Index of a rune slot, as positioned in the default UI: (`number`)
  - `1` - Leftmost
  - `2` - Second from left
  - `3` - Fifth from left (second from right)
  - `4` - Sixth from left (rightmost)
  - `5` - Third from left
  - `6` - Fourth from left

**Returns:**

- `count` - Number of available runes in the slot (`number`)

---

## GetRuneType

Returns the type of one of the player's rune resources. Note the placement of runes 3-4 (normally Unholy) and 5-6 (normally Frost) are reversed in the default UI.

**Signature:**

```lua
runeType = GetRuneType(slot)
```

**Arguments:**

- `slot` - Index of a rune slot, as positioned in the default UI: (`number`)
  - `1` - Leftmost
  - `2` - Second from left
  - `3` - Fifth from left (second from right)
  - `4` - Sixth from left (rightmost)
  - `5` - Third from left
  - `6` - Fourth from left

**Returns:**

- `runeType` - Type of the rune (`number`)
  - `1` - Blood rune
  - `2` - Unholy rune
  - `3` - Frost rune
  - `4` - Death rune

---

## GetTotemInfo

Returns information on a currently active totem (or ghoul). Totem functions are also used for ghouls summoned by a Death Knight's Raise Dead ability (if the ghoul is not made a controllable pet by the Master of Ghouls talent).

**Signature:**

```lua
haveTotem, name, startTime, duration, icon = GetTotemInfo(slot)
```

**Arguments:**

- `slot` - Which totem to query (`number`)
  - `1` - Fire (or Death Knight's ghoul)
  - `2` - Earth
  - `3` - Water
  - `4` - Air

**Returns:**

- `haveTotem` - True if a totem of the given type is active (`boolean`)
- `name` - The name of the totem (`string`)
- `startTime` - The value of GetTime() when the totem was created (`number`)
- `duration` - The total duration the totem will last (in seconds) (`number`)
- `icon` - Path to a texture to use as the totem's icon (`string`)

---

## GetTotemTimeLeft

Returns the time remaining before a totem (or ghoul) automatically disappears.

Using `GetTime()` and the third and fourth returns (`startTime `and `duration`) of `GetTotemInfo()` instead of this function is recommended if frequent updates are needed.

Totem functions are also used for ghouls summoned by a Death Knight's Raise Dead ability (if the ghoul is not made a controllable pet by the Master of Ghouls talent).

**Signature:**

```lua
seconds = GetTotemTimeLeft(slot)
```

**Arguments:**

- `slot` - Which totem to query (`number`)
  - `1` - Fire (or Death Knight's ghoul)
  - `2` - Earth
  - `3` - Water
  - `4` - Air

**Returns:**

- `seconds` - Time remaining before the totem/ghoul is automatically destroyed (`number`)

---

## TargetTotem `protected`

Targets one of the player's totems (or a Death Knight's ghoul). Totem functions are also used for ghouls summoned by a Death Knight's Raise Dead ability (if the ghoul is not made a controllable pet by the Master of Ghouls talent).

**Signature:**

```lua
TargetTotem(slot)
```

**Arguments:**

- `slot` - Which totem to target (`number`)
  - `1` - Fire (or Death Knight's ghoul)
  - `2` - Earth
  - `3` - Water
  - `4` - Air

---

← [WoW API Docs](../index.md)
