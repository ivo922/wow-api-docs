# Buff functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#buff)

---

## CancelItemTempEnchantment

**Signature:**

```lua
CancelItemTempEnchantment(slot)
```

**Arguments:**

- `slot` - 1 to cancel the mainhand item enchant, 2 to cancel the offhand item enchant (`number`)

---

## CancelShapeshiftForm

Cancels the current shapeshift form. Unlike other Shapeshift APIs, this function refers specifically to shapeshifting -- therefore including some abilities not found on the default UI's ShapeshiftBar and excluding some which are. For example, cancels shaman Ghost Wolf form and druid shapeshifts but not warrior stances, paladin auras, or rogue stealth.

**Signature:**

```lua
CancelShapeshiftForm()
```

---

## CancelUnitBuff

Cancels a buff on the player

**Signature:**

```lua
CancelUnitBuff("unit", index [, "filter"]) or CancelUnitBuff("unit", "name" [, "rank" [, "filter"]])
```

**Arguments:**

- `unit` - A unit to query (only valid for 'player') (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player (`string`)
  - `CANCELABLE` - Query auras that can be cancelled
  - `HARMFUL` - Query debuffs only
  - `HELPFUL` - Query buffs only
  - `NOT_CANCELABLE` - Query auras that cannot be cancelled
  - `PLAYER` - Query auras the player has cast
  - `RAID` - Query auras the player can cast on party/raid members (as opposed to self buffs)

---

## GetWeaponEnchantInfo

Returns information about temporary enchantments on the player's weapons. Does not return information about permanent enchantments added via Enchanting, Runeforging, etc; refers instead to temporary buffs such as wizard oils, sharpening stones, rogue poisons, and shaman weapon enhancements.

**Signature:**

```lua
hasMainHandEnchant, mainHandExpiration, mainHandCharges, hasOffHandEnchant, offHandExpiration, offHandCharges = GetWeaponEnchantInfo()
```

**Returns:**

- `hasMainHandEnchant` - 1 if the main hand weapon has a temporary enchant (`1nil`)
- `mainHandExpiration` - The time until the enchant expires, in milliseconds (`number`)
- `mainHandCharges` - The number of charges left on the enchantment (`number`)
- `hasOffHandEnchant` - 1 if the offhand weapon has a temporary enchant (`1nil`)
- `offHandExpiration` - The time until the enchant expires, in milliseconds (`number`)
- `offHandCharges` - The number of charges left on the enchantment (`number`)

---

## UnitAura

Returns information about buffs/debuffs on a unit

**Signature:**

```lua
name, rank, icon, count, dispelType, duration, expires, caster, isStealable, nameplateShowPersonal, spellID, canApplyAura, isBossDebuff, _, nameplateShowAll, timeMod, value1, value2, value3 = UnitAura("unit", index [, "filter"]) or UnitAura("unit", "name", "rank" [, "filter"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player. Defaults to 'HELPFUL' (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `HARMFUL` - Show debuffs only
  - `HELPFUL` - Show buffs only (default)
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - When used with a HELPFUL filter it will show auras the player can cast on party/raid members (as opposed to self buffs). If used with a HARMFUL filter it will return debuffs the player can cure

**Returns:**

- `name` - Name of the aura (`string`)
- `rank` - Secondary text for the aura (often a rank; e.g. "Rank 7") (`string`)
- `icon` - Path to an icon texture for the aura (`string`)
- `count` - The number of times the aura has been applied (`number`)
- `dispelType` - Type of aura (relevant for dispelling and certain other mechanics); nil if not one of the following values: (`string`)
  - `Curse`
  - `Disease`
  - `Magic`
  - `Poison`
- `duration` - Total duration of the aura (in seconds). Zero if the unit is phased or out of range. (`number`)
- `expires` - Time at which the aura will expire; can be compared to [GetTime()](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) to determine time remaining. Zero if the unit is phased or out of range. (`number`)
- `caster` - Unit which applied the aura. If the aura was applied by a unit that does not have a token but is controlled by one that does (e.g. a totem or another player's vehicle), returns the controlling unit. Returns nil if the casting unit (or its controller) has no unitID. (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `isStealable` - true if the aura can be transferred to a player using the Spellsteal spell (`boolean`)
- `nameplateShowPersonal` - true if the aura should be visible above nameplates of affected targets, but only for the player that casted it (`boolean`)
- `spellID` - spellID of the aura (`number`)
- `canApplyAura` - true if the player can apply the aura (not necessarily if the player did apply the aura, just if the player can apply the aura). (`boolean`)
- `isBossDebuff` - true if the aura was cast by a boss. (`boolean`)
- `_` - unknown parameter (`boolean`)
- `nameplateShowAll` - true if the aura should be visible above nameplates of affected targets for all players (`boolean`)
- `timeMod` - the real time remaining on the aura is `(expirationTime - GetTime()) / timeMod`, likely used e.g. on Chronomatic Anomaly (`number`)
- `value1` - Value of variable effect 1 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value2` - Value of variable effect 2 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value3` - Value of variable effect 3 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)

---

## UnitBuff

Returns information about a buff on a unit. This function is an alias for [`UnitAura()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitAura) with a built-in `HELPFUL` filter (which cannot be removed or negated with the `HARMFUL` filter).

**Signature:**

```lua
name, rank, icon, count, dispelType, duration, expires, caster, isStealable, nameplateShowPersonal, spellID, canApplyAura, isBossDebuff, _, nameplateShowAll, timeMod, value1, value2, value3 = UnitBuff("unit", index [, "filter"]) or UnitBuff("unit", "name" [, "rank" [, "filter"]])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

**Returns:**

- `name` - Name of the aura (`string`)
- `rank` - Secondary text for the aura (often a rank; e.g. "Rank 7") (`string`)
- `icon` - Path to an icon texture for the aura (`string`)
- `count` - The number of times the aura has been applied (`number`)
- `dispelType` - Type of aura (relevant for dispelling and certain other mechanics); nil if not one of the following values: (`string`)
  - `Curse`
  - `Disease`
  - `Magic`
  - `Poison`
- `duration` - Total duration of the aura (in seconds). Zero if the unit is phased or out of range. (`number`)
- `expires` - Time at which the aura will expire; can be compared to [GetTime()](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) to determine time remaining. Zero if the unit is phased or out of range. (`number`)
- `caster` - Unit which applied the aura. If the aura was applied by a unit that does not have a token but is controlled by one that does (e.g. a totem or another player's vehicle), returns the controlling unit. Returns nil if the casting unit (or its controller) has no unitID. (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `isStealable` - true if the aura can be transferred to a player using the Spellsteal spell (`boolean`)
- `nameplateShowPersonal` - true if the aura should be visible above nameplates of affected targets, but only for the player that casted it (`boolean`)
- `spellID` - spellID of the aura (`number`)
- `canApplyAura` - true if the player can apply the aura (not necessarily if the player did apply the aura, just if the player can apply the aura). (`boolean`)
- `isBossDebuff` - true if the aura was cast by a boss. (`boolean`)
- `_` - unknown parameter (`boolean`)
- `nameplateShowAll` - true if the aura should be visible above nameplates of affected targets for all players (`boolean`)
- `timeMod` - the real time remaining on the aura is `(expirationTime - GetTime()) / timeMod`, likely used e.g. on Chronomatic Anomaly (`number`)
- `value1` - Value of variable effect 1 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value2` - Value of variable effect 2 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value3` - Value of variable effect 3 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)

---

## UnitDebuff

Returns information about a debuff on a unit. This function is an alias for [`UnitAura()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/UnitAura) with a built-in `HARMFUL` filter (which cannot be removed or negated with the `HELPFUL` filter).

**Signature:**

```lua
name, rank, icon, count, dispelType, duration, expires, caster, isStealable, nameplateShowPersonal, spellID, canApplyAura, isBossDebuff, _, nameplateShowAll, timeMod, value1, value2, value3 = UnitDebuff("unit", index [, "filter"]) or UnitDebuff("unit", "name" [, "rank" [, "filter"]])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of an aura to query (`number`)
- `name` - Name of an aura to query (`string`)
- `rank` - Secondary text of an aura to query (often a rank; e.g. "Rank 7") (`string`)
- `filter` - A list of filters to use separated by the pipe '|' character; e.g. `"CANCELABLE|PLAYER"` will query cancelable debuffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

**Returns:**

- `name` - Name of the aura (`string`)
- `rank` - Secondary text for the aura (often a rank; e.g. "Rank 7") (`string`)
- `icon` - Path to an icon texture for the aura (`string`)
- `count` - The number of times the aura has been applied (`number`)
- `dispelType` - Type of aura (relevant for dispelling and certain other mechanics); nil if not one of the following values: (`string`)
  - `Curse`
  - `Disease`
  - `Magic`
  - `Poison`
- `duration` - Total duration of the aura (in seconds). Zero if the unit is phased or out of range. (`number`)
- `expires` - Time at which the aura will expire; can be compared to [GetTime()](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) to determine time remaining. Zero if the unit is phased or out of range. (`number`)
- `caster` - Unit which applied the aura. If the aura was applied by a unit that does not have a token but is controlled by one that does (e.g. a totem or another player's vehicle), returns the controlling unit. Returns nil if the casting unit (or its controller) has no unitID. (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `isStealable` - true if the aura can be transferred to a player using the Spellsteal spell (`boolean`)
- `nameplateShowPersonal` - true if the aura should be visible above nameplates of affected targets, but only for the player that casted it (`boolean`)
- `spellID` - spellID of the aura (`number`)
- `canApplyAura` - true if the player can apply the aura (not necessarily if the player did apply the aura, just if the player can apply the aura). (`boolean`)
- `isBossDebuff` - true if the aura was cast by a boss. (`boolean`)
- `_` - unknown parameter (`boolean`)
- `nameplateShowAll` - true if the aura should be visible above nameplates of affected targets for all players (`boolean`)
- `timeMod` - the real time remaining on the aura is `(expirationTime - GetTime()) / timeMod`, likely used e.g. on Chronomatic Anomaly (`number`)
- `value1` - Value of variable effect 1 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value2` - Value of variable effect 2 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)
- `value3` - Value of variable effect 3 of the aura. (HoTs, resource-capturing trinkets, etc.) (`number`)

---

← [WoW API Docs](../index.md)
