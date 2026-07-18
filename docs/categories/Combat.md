# Combat functions

← [WoW API Docs](../index.md)

**4** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#combat)

---

## AttackTarget `protected`

Begins auto-attack against the player's current target. (If the "Auto Attack/Auto Shot" option is turned on, also begins Auto Shot for hunters.)

**Signature:**

```lua
AttackTarget()
```

---

## StartAttack `protected`

Begins auto-attack against a specified target

**Signature:**

```lua
StartAttack("unit") or StartAttack("name")
```

**Arguments:**

- `unit` - A unit to attack (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to attack (`string`)

---

## StopAttack `protected`

Stops auto-attack if active

**Signature:**

```lua
StopAttack()
```

---

## UnitAffectingCombat

Returns whether a unit is currently in combat

**Signature:**

```lua
inCombat = UnitAffectingCombat("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `inCombat` - 1 if the unit is currently involved in combat; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
