# Companion functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#companion)

---

## CallCompanion

Summons a non-combat pet or mount.

If called referencing the current non-combat pet, dismisses it. Does nothing if given an index greater than [`GetNumCompanions(type)`](Companion.md#getnumcompanions).

**Signature:**

```lua
CallCompanion("type", index)
```

**Arguments:**

- `type` - Type of companion (`string`)
  - `CRITTER` - A non-combat pet
  - `MOUNT` - A mount
- `index` - Index of a companion (between 1 and [`GetNumCompanions(type)`](Companion.md#getnumcompanions)) (`number`)

---

## DismissCompanion

Unsummons the current non-combat pet or mount

**Signature:**

```lua
DismissCompanion("type")
```

**Arguments:**

- `type` - The type of companion (`string`)
  - `CRITTER` - Non-combat pet
  - `MOUNT` - Mount

---

## GetCompanionCooldown

Returns cooldown information for a non-combat pet or mount

**Signature:**

```lua
start, duration, enable = GetCompanionCooldown("type", index)
```

**Arguments:**

- `type` - Type of companion (`string`)
  - `CRITTER` - A non-combat pet
  - `MOUNT` - A mount
- `index` - Index of a companion (between 1 and [`GetNumCompanions(type)`](Companion.md#getnumcompanions)) (`number`)

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the companion is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the companion is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the companion is ready.) (`number`)

---

## GetCompanionInfo

Returns information about a non-combat pet or mount

**Signature:**

```lua
creatureID, creatureName, spellID, icon, active = GetCompanionInfo("type", index)
```

**Arguments:**

- `type` - Type of companion (`string`)
  - `CRITTER` - A non-combat pet
  - `MOUNT` - A mount
- `index` - Index of a companion (between 1 and [`GetNumCompanions(type)`](Companion.md#getnumcompanions)) (`number`)

**Returns:**

- `creatureID` - Unique ID of the companion (usable with [`PlayerModel:SetCreature`](../widgets/PlayerModel.md#playermodelsetcreature)) (`number`)
- `creatureName` - Localized name of the companion (`string`)
- `spellID` - The "spell" for summoning the companion (usable with [`GetSpellLink`](Hyperlink.md#getspelllink) et al) (`number`)
- `icon` - Path to an icon texture for the companion (`string`)
- `active` - 1 if the companion queried is currently summoned; otherwise nil (`1nil`)

---

## GetNumCompanions

Returns the number of mounts or non-combat pets the player can summon

**Signature:**

```lua
count = GetNumCompanions("type")
```

**Arguments:**

- `type` - The type of companion (`string`)
  - `CRITTER` - Non-combat pets
  - `MOUNT` - Mounts

**Returns:**

- `count` - The number of available companions (`number`)

---

## PickupCompanion

Puts a non-combat pet or mount onto the cursor

**Signature:**

```lua
PickupCompanion("type", index)
```

**Arguments:**

- `type` - Type of companion (`string`)
  - `CRITTER` - A non-combat pet
  - `MOUNT` - A mount
- `index` - Index of a companion (between 1 and [`GetNumCompanions(type)`](Companion.md#getnumcompanions)) (`number`)

---

## SummonRandomCritter

Summons a random critter companion

**Signature:**

```lua
SummonRandomCritter()
```

---

← [WoW API Docs](../index.md)
