# CVar functions

← [WoW API Docs](../index.md)

**10** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#cvar)

---

## GetCVar

Returns the value of a configuration variable. Causes an error if the named CVar does not exist.

Note that all values are returned as strings: use of `tonumber()` may be required if using a value in a numeric context. (See also [`GetCVarBool()`](CVar.md#getcvarbool) for binary values.)

**Signature:**

```lua
string = GetCVar("cvar")
```

**Arguments:**

- `cvar` - Name of a CVar (`string`)

**Returns:**

- `string` - Value of the CVar (`any`)

---

## GetCVarAbsoluteMax

Returns the absolute maximum value allowed for a configuration variable

---

## GetCVarAbsoluteMin

Returns the absolute minimum value allowed for a configuration variable

**Signature:**

```lua
min = GetCVarAbsoluteMin("cvar")
```

**Arguments:**

- `cvar` - Name of a CVar (`string`)

**Returns:**

- `min` - Absolute minimum value allowed for the CVar (`number`)

---

## GetCVarBool

Returns the value of a configuration variable in a format compatible with Lua conditional expressions. All configuration variables are stored as strings; many CVars represent the state of a binary flag and are stored as either `"1"` or `"0"`. This function provides a convenient way to test the state of such variables without the extra syntax required to explicitly check for `"1"` or `"0"` values.

**Signature:**

```lua
value = GetCVarBool("cvar")
```

**Arguments:**

- `cvar` - Name of a CVar (`string`)

**Returns:**

- `value` - 1 if the CVar's value should be treated as `true`; nil if it should be treated as `false` (`1nil`)

---

## GetCVarDefault

Returns the default value of a configuration variable. Causes an error if the named CVar does not exist.

**Signature:**

```lua
value = GetCVarDefault("CVar")
```

**Arguments:**

- `CVar` - Name of a CVar (`string`)

**Returns:**

- `value` - Default value of the CVar (`string`)

---

## GetCVarInfo

Returns information about a configuration variable

**Signature:**

```lua
value, defaultValue, serverStoredAccountWide, serverStoredPerCharacter = GetCVarInfo("cvar")
```

**Arguments:**

- `cvar` - Name of a CVar (`string`)

**Returns:**

- `value` - Current value of the CVar (`string`)
- `defaultValue` - Default value of the CVar (`string`)
- `serverStoredAccountWide` - 1 if the CVar's value is saved on the server and shared by all characters on the player's account; otherwise nil (`1nil`)
- `serverStoredPerCharacter` - 1 if the CVar's value is saved on the server and specific to the current cahracter; otherwise nil (`1nil`)

---

## GetCVarMax

Returns the maximum recommended value for a configuration variable

---

## GetCVarMin

Returns the minimum recommended value for a configuration variable. Used in the default UI to set the lower bounds for options controlled by slider widgets.

**Signature:**

```lua
min = GetCVarMin("cvar")
```

**Arguments:**

- `cvar` - Name of a CVar (`string`)

**Returns:**

- `min` - Minimum value allowed for the CVar (`number`)

---

## RegisterCVar

Registers a configuration variable to be saved

**Signature:**

```lua
RegisterCVar("cvar", "default")
```

**Arguments:**

- `cvar` - Name of a CVar (`string`)
- `default` - Default value of the CVar (`string`)

---

## SetCVar

Sets the value of a configuration variable

**Signature:**

```lua
SetCVar("cvar", value [, "raiseEvent"])
```

**Arguments:**

- `cvar` - Name of the CVar to set (`string`)
- `value` - New value for the CVar (`any`)
- `raiseEvent` - If true, causes the [`CVAR_UPDATE`](../events/CVAR_UPDATE.md) event to fire (`string`)

---

← [WoW API Docs](../index.md)
