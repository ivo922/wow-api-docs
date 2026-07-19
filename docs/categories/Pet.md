# Pet functions

← [WoW API Docs](../index.md)

**36** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#pet)

---

## CastPetAction `protected`

Casts a pet action on a specific target

**Signature:**

```lua
CastPetAction(index [, "unit"])
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)
- `unit` - A unit to be used as target for the action (`string`, [unitID](../types/unitID.md))

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

## DisableSpellAutocast

Disables automatic casting of a pet spell

**Signature:**

```lua
DisableSpellAutocast("spell")
```

**Arguments:**

- `spell` - The name of a pet spell (`string`)

---

## EnableSpellAutocast

Enables automatic casting of a pet spell

**Signature:**

```lua
EnableSpellAutocast("spell")
```

**Arguments:**

- `spell` - Name of a pet spell (`string`)

---

## GetPetActionCooldown

Returns cooldown information about a given pet action slot

**Signature:**

```lua
start, duration, enable = GetPetActionCooldown(index)
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the action is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the action is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the action is ready.) (`number`)

---

## GetPetActionInfo

Returns information about a pet action

**Signature:**

```lua
name, subtext, texture, isToken, isActive, autoCastAllowed, autoCastEnabled = GetPetActionInfo(index)
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

**Returns:**

- `name` - Localized name of the action, or a token which can be used to get the localized name of a standard action (`string`)
- `subtext` - Secondary text for the action (generally a spell rank; e.g. "Rank 8") (`string`)
- `texture` - Path to an icon texture for the action, or a token which can be used to get the texture path of a standard action (`string`)
- `isToken` - 1 if the returned `name` and `texture` are tokens for standard actions, which should be used to look up actual values (e.g. `PET_ACTION_ATTACK`, `PET_ATTACK_TEXTURE`); nil if `name` and `texture` can be displayed as-is (`1nil`)
- `isActive` - 1 if the action is currently active; otherwise nil. (Indicates which state is chosen for the follow/stay and aggressive/defensive/passive switches.) (`1nil`)
- `autoCastAllowed` - 1 if automatic casting is allowed for the action; otherwise nil (`1nil`)
- `autoCastEnabled` - 1 if automatic casting is currently turned on for the action; otherwise nil (`1nil`)

---

## GetPetActionSlotUsable

Returns whether a pet action can be used. Used in the default UI to show pet actions as grayed out when the pet cannot be commanded to perform them (e.g. when the player or pet is stunned).

**Signature:**

```lua
usable = GetPetActionSlotUsable(index)
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

**Returns:**

- `usable` - 1 if the pet action is currently available; otherwise nil (`1nil`)

---

## GetPetActionsUsable

Returns whether the pet's actions are usable. Note: [`GetPetActionSlotUsable`](Action.md#getpetactionslotusable) can return nil for individual actions even if `GetPetActionsUsable` returns 1 (though not the other way around).

**Signature:**

```lua
petActionsUsable = GetPetActionsUsable()
```

**Returns:**

- `petActionsUsable` - 1 if the pet's actions are usable; otherwise nil (`1nil`)

---

## GetPetExperience

Returns information about experience points for the player's pet

**Signature:**

```lua
currXP, nextXP = GetPetExperience()
```

**Returns:**

- `currXP` - The pet's current amount of experience points (`number`)
- `nextXP` - Total amount of experience points required for the pet to gain a level (`number`)

---

## GetPetFoodTypes

Returns a list of the food types the player's pet will eat

**Signature:**

```lua
... = GetPetFoodTypes()
```

**Returns:**

- `...` - A list of strings, each the localized name of a food type the pet will eat (`list`)
  - `Bread` - Baked goods
  - `Cheese` - Cheese products
  - `Fish` - Raw and cooked fish
  - `Fruit` - Fruits
  - `Fungus` - Mushrooms, lichens, and similar
  - `Meat` - Raw and cooked meat

---

## GetPetHappiness

Returns information about the player's pet's happiness

---

## GetPetIcon

Returns an icon representing the current pet. Used in the default Pet Stables and Talent UIs for hunter pets; returns nil for other pets.

**Signature:**

```lua
texture = GetPetIcon()
```

**Returns:**

- `texture` - Path to an icon texture for the pet (`string`)

---

## GetPetTalentTree

Returns the name of the talent tree used by the player's current pet. Hunter pets use one of three different talent trees according to pet type. Returns `nil` if the player does not have a pet or the player's current pet does not use talents (i.e. warlock pets, quest pets, etc.)

**Signature:**

```lua
talent = GetPetTalentTree()
```

**Returns:**

- `talent` - Localized name of the pet's talent tree (`string`)

---

## GetPetTimeRemaining

Returns the time remaining before a temporary pet is automatically dismissed. Temporary pets include priests' Shadowfriend, mages' Water Elemental, and various quest-related pets.

**Signature:**

```lua
petTimeRemaining = GetPetTimeRemaining()
```

**Returns:**

- `petTimeRemaining` - Amount of time remaining until the temporary pet is automatically dismissed (in seconds), or nil if the player does not have a temporary pet (`number`)

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

## HasPetSpells

Returns whether the player's current pet has a spellbook

**Signature:**

```lua
hasPetSpells, petType = HasPetSpells()
```

**Returns:**

- `hasPetSpells` - 1 if the player currently has an active pet with spells/abilities; otherwise nil (`1nil`)
- `petType` - Non-localized token identifying the type of pet (`string`)
  - `DEMON` - A warlock's demonic minion
  - `PET` - A hunter's beast

---

## HasPetUI

Returns whether the pet UI should be displayed for the player's pet. Special quest-related pets, vehicles, and possessed units all count as pets but do not use the pet UI or associated functions.

**Signature:**

```lua
hasPetUI, isHunterPet = HasPetUI()
```

**Returns:**

- `hasPetUI` - 1 if the pet UI should be displayed for the player's pet (`1nil`)
- `isHunterPet` - 1 if the player's pet is a hunter pet (`1nil`)

---

## IsPetAttackActive

Returns whether the pet's attack action is currently active

**Signature:**

```lua
isActive = IsPetAttackActive()
```

**Returns:**

- `isActive` - 1 if the pet's attack action is currently active; otherwise nil (`1nil`)

---

## PetAbandon `confirmation`

Releases the player's pet. For Hunter pets, this function sends the pet away, never to return (in the default UI, it's called when accepting the "Are you sure you want to permanently abandon your pet?" dialog). For other pets, this function is equivalent to [`PetDismiss()`](Pet.md#petdismiss).

**Signature:**

```lua
PetAbandon()
```

---

## PetAggressiveMode `protected`

Enables aggressive mode for the player's pet. In this mode, the pet automatically attacks any nearby hostile targets.

**Signature:**

```lua
PetAggressiveMode()
```

---

## PetAttack `protected`

Instructs the pet to attack. The pet will attack the player's current target if no unit is specified.

**Signature:**

```lua
PetAttack(["unit"]) or PetAttack(["name"])
```

**Arguments:**

- `unit` - A unit to attack (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to attack (`string`)

---

## PetCanBeAbandoned

Returns whether the player's pet can be abandoned. Only Hunter pets can be permanently abandoned.

**Signature:**

```lua
canAbandon = PetCanBeAbandoned()
```

**Returns:**

- `canAbandon` - 1 if the player's pet can be abandoned, otherwise nil (`1nil`)

---

## PetCanBeDismissed

Returns whether a Dismiss Pet command should be available for the player's pet. Returns 1 for hunter pets even though they use the Dismiss Pet (cast) spell instead of a Dismiss Pet (instant) command; the value of [`PetCanBeAbandoned()`](Pet.md#petcanbeabandoned) overrides this in causing the default UI to hide the command. Currently unused, but may be used in the future for other pets.

**Signature:**

```lua
canDismiss = PetCanBeDismissed()
```

**Returns:**

- `canDismiss` - 1 if a Dismiss Pet command should be available for the player's pet; otherwise nil (`1nil`)

---

## PetCanBeRenamed

Returns whether the player's pet can be renamed. Only hunter pets can be renamed, and only once (barring use of a [Certificate of Ownership](http://www.wowhead.com/?item=43850)).

**Signature:**

```lua
canRename = PetCanBeRenamed()
```

**Returns:**

- `canRename` - 1 if the player can rename the currently controlled pet, otherwise nil (`1nil`)

---

## PetDefensiveMode `protected`

Enables defensive mode for the player's pet. In this mode, the pet automatically attacks only units which attack it or the player or units the player is attacking.

**Signature:**

```lua
PetDefensiveMode()
```

---

## PetDismiss

Dismisses the currently controlled pet. Used for dismissing Warlock pets, Mind Control targets, etc. Has no effect for Hunter pets, which can only be dismissed using the Dismiss Pet spell.

**Signature:**

```lua
PetDismiss()
```

---

## PetFollow `protected`

Instructs the pet to follow the player. If the pet is currently attacking a target, the pet will stop attacking.

**Signature:**

```lua
PetFollow()
```

---

## PetHasActionBar

Returns whether the player's current pet has an action bar

**Signature:**

```lua
hasActionBar = PetHasActionBar()
```

**Returns:**

- `hasActionBar` - Returns 1 if the player's pet has an action bar; otherwise nil (`1nil`)

---

## PetPassiveMode `protected`

Enables passive mode for the player's pet. In this mode, the pet will not automatically attack any target.

**Signature:**

```lua
PetPassiveMode()
```

---

## PetRename

Renames the currently controlled pet. Only Hunter pets can be renamed, and a given pet can only be renamed once (barring use of a [Certificate of Ownership](http://www.wowhead.com/?item=43850)).

**Signature:**

```lua
PetRename("name" [, "genitive" [, "dative" [, "accusative" [, "instrumental" [, "prepositional"]]]]])
```

**Arguments:**

- `name` - New name for the pet (nominative form on Russian clients) (`string`)
- `genitive` - Genitive form of the pet's new name; applies only on Russian clients (`string`)
- `dative` - Dative form of the pet's new name; applies only on Russian clients (`string`)
- `accusative` - Accusative form of the pet's new name; applies only on Russian clients (`string`)
- `instrumental` - Instrumental form of the pet's new name; applies only on Russian clients (`string`)
- `prepositional` - Prepositional form of the pet's new name; applies only on Russian clients (`string`)

---

## PetStopAttack `protected`

Instructs the pet to stop attacking

**Signature:**

```lua
PetStopAttack()
```

---

## PetWait `protected`

Instructs the pet to stay at its current location. If the pet is currently attacking a target, the pet will stop attacking.

**Signature:**

```lua
PetWait()
```

---

## PickupPetAction

Puts the contents of a pet action slot onto the cursor or the cursor contents into a pet action slot. Only pet actions and spells from the "pet" portion of the spellbook can be placed into pet action slots.

If the cursor is empty and the referenced pet action slot contains an action, that action is put onto the cursor (but remains in the slot). If the cursor contains a pet action or pet spell and the slot is empty, the action/spell is placed into the slot. If both the cursor and the slot contain pet actions, the contents of the cursor and the pet action slot are exchanged.

**Signature:**

```lua
PickupPetAction(index)
```

**Arguments:**

- `index` - Index of a pet action (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

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

## TogglePetAutocast `protected`

Turns autocast on or off for a pet action. Turns autocast on if not autocasting and vice versa.

**Signature:**

```lua
TogglePetAutocast(index)
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

---

← [WoW API Docs](../index.md)
