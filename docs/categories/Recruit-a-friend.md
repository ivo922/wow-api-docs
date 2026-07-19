# Recruit-a-friend functions

← [WoW API Docs](../index.md)

**8** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#raf)

---

## AcceptLevelGrant

Accepts a level offered by the player's Recruit-a-Friend partner

**Signature:**

```lua
AcceptLevelGrant()
```

---

## CanGrantLevel

Returns whether the player can give levels to a Recruit-a-Friend partner

**Signature:**

```lua
canGrant = CanGrantLevel("unit")
```

**Arguments:**

- `unit` - Unit to gift a level (`string`, [unitID](../types/unitID.md))

**Returns:**

- `canGrant` - 1 if the player can grant a level to the unit; otherwise nil (`1nil`)

---

## CanSummonFriend

Returns whether a unit can be summoned via Recruit-a-Friend. Indicates whether the target unit is currently summonable, not just whether that unit's account is linked to the player's via the Recruit-A-Friend program.

**Signature:**

```lua
canSummon = CanSummonFriend("name") or CanSummonFriend("unit")
```

**Arguments:**

- `name` - Exact name of a player to summon (`string`)
- `unit` - A unit to summon (`string`, [unitID](../types/unitID.md))

**Returns:**

- `canSummon` - 1 if the unit can be summoned, otherwise nil (`1nil`)

---

## DeclineLevelGrant

Refuses a level offered by the player's Recruit-a-Friend partner

**Signature:**

```lua
DeclineLevelGrant()
```

---

## GetSummonFriendCooldown

Returns cooldown information about the player's Summon Friend ability

**Signature:**

```lua
start, duration = GetSummonFriendCooldown()
```

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the ability is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the ability is ready (`number`)

---

## GrantLevel

Grants a level to the player's Recruit-a-Friend partner. Does not immediately cause the partner character to level up: that player is given a chance to accept or decline the offered level.

**Signature:**

```lua
GrantLevel("unit")
```

**Arguments:**

- `unit` - Unit to gift a level (`string`, [unitID](../types/unitID.md))

---

## IsReferAFriendLinked

Returns whether a unit's account is linked to the player's via the Recruit-a-Friend program

**Signature:**

```lua
isLinked = IsReferAFriendLinked("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `isLinked` - 1 if the unit's account is linked to the player's (`1nil`)

---

## SummonFriend

Summons a unit whose account is linked to the player's via the Recruit-a-Friend program. Does not instantly teleport the unit -- calling this function begins casting the Summon Friend "spell", and once it completes the unit is prompted to accept or decline the summon.

**Signature:**

```lua
SummonFriend("name") or SummonFriend("unit")
```

**Arguments:**

- `name` - Exact name of a player to summon (only applies to units in the player's party or raid) (`string`)
- `unit` - A unit to summon (`string`, [unitID](../types/unitID.md))

---

← [WoW API Docs](../index.md)
