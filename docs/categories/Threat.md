# Threat functions

← [WoW API Docs](../index.md)

**4** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#threat)

---

## GetThreatStatusColor

Returns color values for a given threat status. Color component values are floating point numbers between 0 and 1, with 1 representing full intensity.

**Signature:**

```lua
red, green, blue = GetThreatStatusColor(status)
```

**Arguments:**

- `status` - A threat status category, as returned by [`UnitThreatSituation`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitThreatSituation) or [`UnitDetailedThreatSituation`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitDetailedThreatSituation) (`number`)

**Returns:**

- `red` - Red component of the color (`number`)
- `green` - Green component of the color (`number`)
- `blue` - Blue component of the color (`number`)

---

## IsThreatWarningEnabled

Returns whether the default Aggro Warning UI should currently be shown.

This function (and the `threatWarning` CVar that affects its behavior) has no effect on other threat APIs; it merely indicates whether Blizzard's threat warning UI should be displayed.

**Signature:**

```lua
enabled = IsThreatWarningEnabled()
```

**Returns:**

- `enabled` - 1 if the Aggro Warning UI should be displayed; nil otherwise (`1nil`)

---

## UnitDetailedThreatSituation

Returns detailed information about the threat status of one unit against another.

The different values returned by this function reflect the complexity of NPC threat management:

Raw threat roughly equates to the amount of damage a unit has caused to the NPC plus the amount of healing the unit has performed in the NPC's presence. (Each quantity that goes into this sum may be modified, however; such as by a paladin's Righteous Fury self-buff, a priest's Silent Resolve talent, or a player whose cloak is enchanted with Subtlety.)

Generally, whichever unit has the highest raw threat against an NPC becomes its primary target, and raw threat percentage simplifies this comparison.

However, most NPCs are designed to maintain some degree of target focus -- so that they don't rapidly switch targets if, for example, a unit other than the primary target suddenly reaches 101% raw threat. The amount by which a unit must surpass the primary target's threat to become the new primary target varies by distance from the NPC.

Thus, a scaled percentage value is given to provide clarity. The `rawPercent` value returned from this function can be greater than 100 (indicating that `unit` has greater threat against `mobUnit` than `mobUnit`'s primary target, and is thus in danger of becoming the primary target), but the `scaledPercent` value will always be 100 or lower.

Threat information for a pair of units is only returned if the player has threat against the NPC unit in question. (For example, no threat data is provided if the player's pet is attacking an NPC but the player himself has taken no action, even though the pet has threat against the NPC.)

**Signature:**

```lua
isTanking, status, scaledPercent, rawPercent, threatValue = UnitDetailedThreatSituation(unit, mobUnit) or UnitDetailedThreatSituation("name", mobUnit)
```

**Arguments:**

- `unit` - The unit whose threat situation is being requested (`unitid`)
- `name` - The name of a unit to query. Only valid for the player, pet, and party/raid members. (`string`)
- `mobUnit` - An NPC unit the first unit may have threat against (`unitid`)

**Returns:**

- `isTanking` - 1 if unit is mobUnit's primary target, nil otherwise (`1nil`)
- `status` - A threat status category (`number`)
  - `0` - Unit has less than 100% raw threat (default UI shows no indicator)
  - `1` - Unit has 100% or higher raw threat but isn't mobUnit's primary target (default UI shows yellow indicator)
  - `2` - Unit is `mobUnit`'s primary target, and another unit has 100% or higher raw threat (default UI shows orange indicator)
  - `3` - Unit is `mobUnit`'s primary target, and no other unit has 100% or higher raw threat (default UI shows red indicator)
- `scaledPercent` - A percentage value representing unit's threat against `mobUnit`, scaled such that a value of 100% represents unit becoming `mobUnit`'s primary target (`number`)
- `rawPercent` - A percentage value representing unit's threat against `mobUnit` relative to the the threat of mobUnit's primary target (`number`)
- `threatValue` - The raw value of unit's threat against mobUnit (`number`)

---

## UnitThreatSituation

Returns the general threat status of a unit. See [`UnitDetailedThreatSituation`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitDetailedThreatSituation) for details about threat values.

Threat information for a pair of units is only returned if the player has threat against the NPC unit in question. (For example, no threat data is provided if the player's pet is attacking an NPC but the player himself has taken no action, even though the pet has threat against the NPC.)

**Signature:**

```lua
status = UnitThreatSituation(unit [, mobUnit]) or UnitThreatSituation("name" [, mobUnit])
```

**Arguments:**

- `unit` - The unit whose threat situation is being requested (`unitid`)
- `name` - The name of a unit to query. Only valid for the player, pet, and party/raid members. (`string`)
- `mobUnit` - An NPC unit the first unit may have threat against; if nil, returned values reflect whichever NPC unit the first unit has the highest threat against. (`unitid`)

**Returns:**

- `status` - A threat status category (`number`)
  - `0` - Unit has less than 100% raw threat (default UI shows no indicator)
  - `1` - Unit has 100% or higher raw threat but isn't `mobUnit`'s primary target (default UI shows yellow indicator)
  - `2` - Unit is `mobUnit`'s primary target, and another unit has 100% or higher raw threat (default UI shows orange indicator)
  - `3` - Unit is `mobUnit`'s primary target, and no other unit has 100% or higher raw threat (default UI shows red indicator)

---

← [WoW API Docs](../index.md)
