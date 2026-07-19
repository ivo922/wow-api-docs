# Targeting functions

← [WoW API Docs](../index.md)

**17** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#target)

---

## AssistUnit `protected`

Targets the unit targeted by another unit

**Signature:**

```lua
AssistUnit("unit") or AssistUnit("name")
```

**Arguments:**

- `unit` - A unit to assist (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to assist (`string`)

---

## ClearFocus `protected`

Clears the player's focus unit

**Signature:**

```lua
ClearFocus()
```

---

## ClearTarget `protected`

Clears the player's current target

**Signature:**

```lua
ClearTarget()
```

---

## FocusUnit `protected`

Changes the `focus` unitID to refer to a new unit

**Signature:**

```lua
FocusUnit("unit") or FocusUnit("name")
```

**Arguments:**

- `unit` - A unit to focus (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to focus; only valid for `player`, `pet`, and party/raid members (`string`)

---

## SpellCanTargetUnit

Returns whether the spell currently awaiting a target can target a given unit. Only applies when the player has attempted to cast a spell but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
canTarget = SpellCanTargetUnit("unit") or SpellCanTargetUnit("name")
```

**Arguments:**

- `unit` - A unit to target (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to target; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `canTarget` - 1 if the spell currently awaiting targeting can target the given unit (`1nil`)

---

## SpellTargetUnit `protected`

Casts the spell currently awaiting a target on a unit

**Signature:**

```lua
SpellTargetUnit("unit") or SpellTargetUnit("name")
```

**Arguments:**

- `unit` - A unit to target (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to target; only valid for `player`, `pet`, and party/raid members (`string`)

---

## TargetLastEnemy `protected`

Targets the most recently targeted enemy unit

**Signature:**

```lua
TargetLastEnemy()
```

---

## TargetLastFriend `protected`

Targets the most recently targeted friendly unit

**Signature:**

```lua
TargetLastFriend()
```

---

## TargetLastTarget `protected`

Targets the most recently targeted unit

**Signature:**

```lua
TargetLastTarget()
```

---

## TargetNearest `protected`

Cycles targets through nearest units regardless of reaction/affiliation

**Signature:**

```lua
TargetNearest([backward])
```

**Arguments:**

- `backward` - Reverses direction of target cycling if true (as with the default TAB vs. SHIFT-TAB bindings) (`boolean`)

---

## TargetNearestEnemy `protected`

Cycles your target through the nearest enemy units.

This function can only be called once per hardware event.

**Signature:**

```lua
TargetNearestEnemy(backward)
```

**Arguments:**

- `backward` - Reverses the direction of the cycling if true (e.g. TAB vs. SHIFT-TAB) (`boolean`)

---

## TargetNearestEnemyPlayer `protected`

Cycles targets through nearby enemy player units

**Signature:**

```lua
TargetNearestEnemyPlayer(backward)
```

**Arguments:**

- `backward` - Reverses direction of target cycling if true (as with the default TAB vs. SHIFT-TAB bindings) (`boolean`)

---

## TargetNearestFriend `protected`

Cycles targets through nearby friendly units

**Signature:**

```lua
TargetNearestFriend(backward)
```

**Arguments:**

- `backward` - Reverses direction of target cycling if true (as with the default TAB vs. SHIFT-TAB bindings) (`boolean`)

---

## TargetNearestFriendPlayer `protected`

Cycles targets through nearby friendly player units

**Signature:**

```lua
TargetNearestFriendPlayer(backward)
```

**Arguments:**

- `backward` - Reverses direction of target cycling if true (as with the default TAB vs. SHIFT-TAB bindings) (`boolean`)

---

## TargetNearestPartyMember `protected`

Cycles targets through nearby party members

**Signature:**

```lua
TargetNearestPartyMember(backward)
```

**Arguments:**

- `backward` - Reverses direction of target cycling if true (as with the default TAB vs. SHIFT-TAB bindings) (`boolean`)

---

## TargetNearestRaidMember `protected`

Cycles targets through nearby raid members

**Signature:**

```lua
TargetNearestRaidMember(backward)
```

**Arguments:**

- `backward` - Reverses direction of target cycling if true (as with the default TAB vs. SHIFT-TAB bindings) (`boolean`)

---

## TargetUnit `protected`

Targets a unit. Passing `nil` is equivalent to calling [`ClearTarget()`](Targeting.md#cleartarget-protected)).

**Signature:**

```lua
TargetUnit("unit") or TargetUnit("name" [, exactMatch])
```

**Arguments:**

- `unit` - A unit to target (`string`, [unitID](../types/unitID.md))
- `name` - Name of a unit to target (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

← [WoW API Docs](../index.md)
