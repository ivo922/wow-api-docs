# Experience (XP) functions

← [WoW API Docs](../index.md)

**5** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#xp)

---

## GetRewardXP

Returns the experience awarded when completing a quest

---

## GetXPExhaustion

Returns the amount of rested bonus experience available. This value increments as the player spends time resting and depletes as the player earns experience from kills while rested.

**Signature:**

```lua
exhaustionXP = GetXPExhaustion()
```

**Returns:**

- `exhaustionXP` - The amount of rested bonus experience available (`number`)

---

## IsXPUserDisabled

Returns whether experience gain has been disabled for the player

**Signature:**

```lua
isDisabled = IsXPUserDisabled()
```

**Returns:**

- `isDisabled` - True if experience gain has been disabled for the player; false otherwise (`boolean`)

---

## UnitXP

Returns the player's current amount of experience points

**Signature:**

```lua
currXP = UnitXP("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `currXP` - Current amount of experience points (`number`)

---

## UnitXPMax

Return the total amount of experience points required for the player to gain a level

**Signature:**

```lua
playerMaxXP = UnitXPMax("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `playerMaxXP` - Total amount of experience points required for the player to gain a level (`number`)

---

← [WoW API Docs](../index.md)
