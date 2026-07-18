# Tracking functions

← [WoW API Docs](../index.md)

**4** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#tracking)

---

## GetNumTrackingTypes

Returns the number of available minimap object/unit tracking abilities

**Signature:**

```lua
count = GetNumTrackingTypes()
```

**Returns:**

- `count` - Number of available tracking types (`number`)

---

## GetTrackingInfo

Returns information about a given tracking option

**Signature:**

```lua
name, texture, active, category = GetTrackingInfo(index)
```

**Arguments:**

- `index` - Index of a tracking ability to query (between 1 and [`GetNumTrackingTypes()`](https://web.archive.org/web/20100105222919/http://wowprogramming.com/docs/api/GetNumTrackingTypes)) (`number`)

**Returns:**

- `name` - Localized name of the tracking ability (`string`)
- `texture` - Path to an icon texture for the tracking ability (`string`)
- `active` - 1 if the tracking abilty is active; otherwise nil (`1nil`)
- `category` - Category of the tracking ability; used in the default UI to determine whether to strip the border from the ability's icon texture, and also indicates when the ability can be used: (`string`)
  - `other` - Ability is available to all players and can be used at any time
  - `spell` - Ability is a spell from the player's spellbook; using it may be subject to spell casting restrictions

---

## GetTrackingTexture

Returns the texture of the active tracking ability

---

## SetTracking

Enables a given minimap object/unit tracking ability

**Signature:**

```lua
SetTracking(index, enabled)
```

**Arguments:**

- `index` - Index of a tracking ability (between 1 and [`GetNumTrackingTypes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTrackingTypes)) (`number`)
- `enabled` - pass true to enable, false to disable (`boolean`)

---

← [WoW API Docs](../index.md)
