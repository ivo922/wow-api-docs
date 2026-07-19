# Stat information functions

← [WoW API Docs](../index.md)

**38** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#stats)

---

## GetArmorPenetration

Returns the percentage of enemy armor ignored due to the player's Armor Penetration Rating

**Signature:**

```lua
amount = GetArmorPenetration()
```

**Returns:**

- `amount` - Percentage of enemy armor ignored due to the player's Armor Penetration Rating (`number`)

---

## GetAttackPowerForStat

Returns the attack power bonus provided by one of the player's basic statistics

**Signature:**

```lua
attackPower = GetAttackPowerForStat(statIndex, effectiveStat)
```

**Arguments:**

- `statIndex` - Index of a basic statistic (`number`)
  - `1` - Strength
  - `2` - Agility
  - `3` - Stamina
  - `4` - Intellect
  - `5` - Spirit
- `effectiveStat` - Value of the statistic to use in attack power calculation (`number`)

**Returns:**

- `attackPower` - Attack power bonus provided to the player by the basic statistic value (`number`)

---

## GetBlockChance

Returns the player's percentage chance to block with a shield

**Signature:**

```lua
chance = GetBlockChance()
```

**Returns:**

- `chance` - Percentage chance to block (`number`)

---

## GetCombatRating

Returns the value of a combat rating for the player

**Signature:**

```lua
rating = GetCombatRating(ratingIndex)
```

**Arguments:**

- `ratingIndex` - Index of a rating; the following global constants are provided for convenience (`number`)
  - `CR_BLOCK` - Block skill
  - `CR_CRIT_MELEE` - Melee critical strike chance
  - `CR_CRIT_RANGED` - Ranged critical strike chance
  - `CR_CRIT_SPELL` - Spell critical strike chance
  - `CR_CRIT_TAKEN_MELEE` - Melee Resilience
  - `CR_CRIT_TAKEN_RANGED` - Ranged Resilience
  - `CR_CRIT_TAKEN_SPELL` - Spell Resilience
  - `CR_DEFENSE_SKILL` - Defense skill
  - `CR_DODGE` - Dodge skill
  - `CR_HASTE_MELEE` - Melee haste
  - `CR_HASTE_RANGED` - Ranged haste
  - `CR_HASTE_SPELL` - Spell haste
  - `CR_HIT_MELEE` - Melee chance to hit
  - `CR_HIT_RANGED` - Ranged chance to hit
  - `CR_HIT_SPELL` - Spell chance to hit
  - `CR_HIT_TAKEN_MELEE` - Unused
  - `CR_HIT_TAKEN_RANGED` - Unused
  - `CR_HIT_TAKEN_SPELL` - Unused
  - `CR_PARRY` - Parry skill
  - `CR_WEAPON_SKILL` - Weapon skill
  - `CR_WEAPON_SKILL_MAINHAND` - Main-hand weapon skill
  - `CR_WEAPON_SKILL_OFFHAND` - Offhand weapon skill
  - `CR_WEAPON_SKILL_RANGED` - Ranged weapon skill

**Returns:**

- `rating` - Value of the rating for the player (`number`)

---

## GetCombatRatingBonus

Returns the percentage effect for the player's current value of a given combat rating. Used in the default UI to show tooltips with actual percentage effects (such as increased parry chance or reduced critical strike damage taken) when mousing over rating information in the Character window.

**Signature:**

```lua
ratingBonus = GetCombatRatingBonus(ratingIndex)
```

**Arguments:**

- `ratingIndex` - Index of a rating; the following global constants are provided for convenience (`number`)
  - `CR_BLOCK` - Block skill
  - `CR_CRIT_MELEE` - Melee critical strike chance
  - `CR_CRIT_RANGED` - Ranged critical strike chance
  - `CR_CRIT_SPELL` - Spell critical strike chance
  - `CR_CRIT_TAKEN_MELEE` - Melee Resilience
  - `CR_CRIT_TAKEN_RANGED` - Ranged Resilience
  - `CR_CRIT_TAKEN_SPELL` - Spell Resilience
  - `CR_DEFENSE_SKILL` - Defense skill
  - `CR_DODGE` - Dodge skill
  - `CR_HASTE_MELEE` - Melee haste
  - `CR_HASTE_RANGED` - Ranged haste
  - `CR_HASTE_SPELL` - Spell haste
  - `CR_HIT_MELEE` - Melee chance to hit
  - `CR_HIT_RANGED` - Ranged chance to hit
  - `CR_HIT_SPELL` - Spell chance to hit
  - `CR_HIT_TAKEN_MELEE` - Unused
  - `CR_HIT_TAKEN_RANGED` - Unused
  - `CR_HIT_TAKEN_SPELL` - Unused
  - `CR_PARRY` - Parry skill
  - `CR_WEAPON_SKILL` - Weapon skill
  - `CR_WEAPON_SKILL_MAINHAND` - Main-hand weapon skill
  - `CR_WEAPON_SKILL_OFFHAND` - Offhand weapon skill
  - `CR_WEAPON_SKILL_RANGED` - Ranged weapon skill

**Returns:**

- `ratingBonus` - Percentage change in the underlying statistic or mechanic conferred by the player's rating value (`number`)

---

## GetCritChance

Returns the player's melee critical strike chance

**Signature:**

```lua
critChance = GetCritChance()
```

**Returns:**

- `critChance` - The player's percentage critical strike chance for melee attacks (`number`)

---

## GetCritChanceFromAgility

Returns additional critical strike chance provided by Agility

**Signature:**

```lua
critChance = GetCritChanceFromAgility(["unit"])
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` and `pet`, defaults to `player` if omitted (`string`, [unitID](../types/unitID.md))

**Returns:**

- `critChance` - Additional percentage chance of critical strikes conferred by the unit's Agility statistic (`number`)

---

## GetDamageBonusStat

Returns the index of the basic statistic that provides increased physical damage. Unused in the default UI.

**Signature:**

```lua
bonusStat = GetDamageBonusStat()
```

**Returns:**

- `bonusStat` - Index of the basic statistic which provides attack (`number`)
  - `1` - Strength (Druids, Mages, Paladins, Priests, Shamans, Warlocks and Warriors)
  - `2` - Agility (Hunters and Rogues)

---

## GetDodgeChance

Returns the player's chance to dodge melee attacks

**Signature:**

```lua
chance = GetDodgeChance()
```

**Returns:**

- `chance` - Percentage chance to dodge melee attacks (`number`)

---

## GetExpertise

Returns the player's current expertise value

**Signature:**

```lua
expertise = GetExpertise()
```

**Returns:**

- `expertise` - The player's expertise value (`number`)

---

## GetExpertisePercent

Returns the reduction in chance to be dodged or parried conferred by the player's expertise value

**Signature:**

```lua
expertisePerc, offhandExpertisePercent = GetExpertisePercent()
```

**Returns:**

- `expertisePerc` - Reduction in percentage chance for main hand attacks to be dodged or parried (`number`)
- `offhandExpertisePercent` - Reduction in percentage chance for off hand attacks to be dodged or parried (`number`)

---

## GetManaRegen

Returns information about the player's mana regeneration rate

**Signature:**

```lua
base, casting = GetManaRegen()
```

**Returns:**

- `base` - Amount of mana regenerated per second while not casting (`number`)
- `casting` - Amount of mana regenerated per second while casting (`number`)

---

## GetMaxCombatRatingBonus

Returns the maximum possible percentage bonus for a given combat rating.

While this function can be applied to all combat ratings, it is currently only used in the default UI to account for the cap on (incoming) critical strike damage and mana drains provided by Resilience rating -- specifically, in generating the tooltip where Resilience rating is shown in the Character window (PaperDollFrame).

**Signature:**

```lua
max = GetMaxCombatRatingBonus(ratingIndex)
```

**Arguments:**

- `ratingIndex` - Which rating to query; the following global constants can be used for standard values: (`number`)
  - `CR_BLOCK` - Block skill
  - `CR_CRIT_MELEE` - Melee critical strike chance
  - `CR_CRIT_RANGED` - Ranged critical strike chance
  - `CR_CRIT_SPELL` - Spell critical strike chance
  - `CR_CRIT_TAKEN_MELEE` - Resilience (as applied to melee attacks)
  - `CR_CRIT_TAKEN_RANGED` - Resilience (as applied to ranged attacks)
  - `CR_CRIT_TAKEN_SPELL` - Resilience (as applied to spell effects
  - `CR_DEFENSE_SKILL` - Defense skill
  - `CR_DODGE` - Dodge skill
  - `CR_HASTE_MELEE` - Melee haste
  - `CR_HASTE_RANGED` - Ranged haste
  - `CR_HASTE_SPELL` - Spell haste
  - `CR_HIT_MELEE` - Melee chance to hit
  - `CR_HIT_RANGED` - Ranged chance to hit
  - `CR_HIT_SPELL` - Spell chance to hit
  - `CR_HIT_TAKEN_MELEE` - Unused
  - `CR_HIT_TAKEN_RANGED` - Unused
  - `CR_HIT_TAKEN_SPELL` - Unused
  - `CR_PARRY` - Parry skill
  - `CR_WEAPON_SKILL` - Weapon skill
  - `CR_WEAPON_SKILL_MAINHAND` - Main-hand weapon skill
  - `CR_WEAPON_SKILL_OFFHAND` - Offhand weapon skill
  - `CR_WEAPON_SKILL_RANGED` - Ranged weapon skill

**Returns:**

- `max` - The maximum possible percentage bonus for the given rating (`number`)

---

## GetParryChance

Returns the player's parry chance

**Signature:**

```lua
chance = GetParryChance()
```

**Returns:**

- `chance` - The player's percentage chance to parry melee attacks (`number`)

---

## GetPowerRegen

Returns information about the player's mana/energy/etc regeneration rate. Contexts for `inactiveRegen` and `activeRegen` vary by power type.

If the player (currently) uses mana, `activeRegen` refers to mana regeneration while casting (within five seconds of casting a spell) and `inactiveRegen` refers to mana regeneration while not casting (more than five seconds after casting a spell). For other power types, `activeRegen` refers to regeneration while in combat and `inactiveRegen` to regeneration outside of combat.

Note that values returned can be negative: e.g. for rage and runic power users, `inactiveRegen` describes the rate of power decay while not in combat.

**Signature:**

```lua
inactiveRegen, activeRegen = GetPowerRegen()
```

**Returns:**

- `inactiveRegen` - Power change per second while inactive (`number`)
- `activeRegen` - Power change per second while active (`number`)

---

## GetRangedCritChance

Returns the player's ranged critical strike chance

**Signature:**

```lua
critChance = GetRangedCritChance()
```

**Returns:**

- `critChance` - The player's percentage critical strike chance for ranged attacks (`number`)

---

## GetShieldBlock

Returns the amount of damage prevented when the player blocks with a shield

**Signature:**

```lua
damage = GetShieldBlock()
```

**Returns:**

- `damage` - The amount of damage prevented when the player blocks with a shield (`number`)

---

## GetSpellBonusDamage

Returns the player's spell damage bonus for a spell school

**Signature:**

```lua
minModifier = GetSpellBonusDamage(school)
```

**Arguments:**

- `school` - Index of a spell school (`number`)
  - `1` - Physical
  - `2` - Holy
  - `3` - Fire
  - `4` - Nature
  - `5` - Frost
  - `6` - Shadow
  - `7` - Arcane

**Returns:**

- `minModifier` - The player's spell damage bonus for the given school (`number`)

---

## GetSpellBonusHealing

Returns the player's amount of bonus healing

**Signature:**

```lua
bonusHealing = GetSpellBonusHealing()
```

**Returns:**

- `bonusHealing` - Amount of bonus healing (`integer`)

---

## GetSpellCritChance

Returns the player's spell critical strike chance for a spell school

**Signature:**

```lua
minCrit = GetSpellCritChance(school)
```

**Arguments:**

- `school` - Index of a spell school (`number`)
  - `1` - Physical
  - `2` - Holy
  - `3` - Fire
  - `4` - Nature
  - `5` - Frost
  - `6` - Shadow
  - `7` - Arcane

**Returns:**

- `minCrit` - The player's percentage critical strike chance for spells from the given school (`number`)

---

## GetSpellCritChanceFromIntellect

Returns additional spell critical strike chance provided by Intellect

**Signature:**

```lua
critChance = GetSpellCritChanceFromIntellect(["unit"])
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` and `pet`, defaults to `player` if omitted (`string`, [unitID](../types/unitID.md))

**Returns:**

- `critChance` - Additional percentage chance of spell critical strikes conferred by the unit's Intellect statistic (`number`)

---

## GetSpellPenetration

Returns the amount of enemy magic resistance ignored due to the player's Spell Penetration Rating

**Signature:**

```lua
penetration = GetSpellPenetration()
```

**Returns:**

- `penetration` - Amount of enemy magic resistance ignored due to the player's Spell Penetration Rating (`number`)

---

## GetUnitHealthModifier

Returns the health modifier for the player's pet

**Signature:**

```lua
modifier = GetUnitHealthModifier("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `modifier` - Factor modifying the unit's health value (`number`)

---

## GetUnitHealthRegenRateFromSpirit

Returns the increase in health regeneration rate provided by Spirit

**Signature:**

```lua
regen = GetUnitHealthRegenRateFromSpirit("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `regen` - Increase in non-combat health regeneration per second provided by Spirit (`number`)

---

## GetUnitManaRegenRateFromSpirit

Returns the increase in mana regeneration rate provided by Spirit

**Signature:**

```lua
regen = GetUnitManaRegenRateFromSpirit("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `regen` - Increase in inactive (non-casting) mana regeneration per second provided by Spirit (`number`)

---

## GetUnitMaxHealthModifier

Returns the maximum health modifier for the player's pet

**Signature:**

```lua
modifier = GetUnitMaxHealthModifier("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `modifier` - Factor modifying the unit's maximum health value (`number`)

---

## GetUnitPowerModifier

Returns the mana modifier for the player's pet

**Signature:**

```lua
modifier = GetUnitPowerModifier("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `modifier` - Factor modifying the unit's mana value (`number`)

---

## UnitArmor

Returns the player's or pet's armor value

**Signature:**

```lua
base, effectiveArmor, armor, posBuff, negBuff = UnitArmor("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `base` - The unit's base armor value (`number`)
- `effectiveArmor` - The unit's effective armor value (`number`)
- `armor` - The unit's current armor value (`number`)
- `posBuff` - Positive modifiers to armor value (`number`)
- `negBuff` - Negative modifiers to armor value (`number`)

---

## UnitAttackBothHands

Returns information about the player's or pet's weapon skill

**Signature:**

```lua
mainHandAttackBase, mainHandAttackMod, offHandHandAttackBase, offHandAttackMod = UnitAttackBothHands("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `mainHandAttackBase` - The unit's base weapon skill for the main hand weapon (`number`)
- `mainHandAttackMod` - Temporary modifiers to main hand weapon skill (`number`)
- `offHandHandAttackBase` - The unit's base weapon skill for the off hand weapon (`number`)
- `offHandAttackMod` - Temporary modifiers to off hand weapon skill (`number`)

---

## UnitAttackPower

Returns the player's or pet's melee attack power

**Signature:**

```lua
base, posBuff, negBuff = UnitAttackPower("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `base` - The unit's base attack power (`number`)
- `posBuff` - Total effect of positive buffs to attack power (`number`)
- `negBuff` - Total effect of negative buffs to attack power (`number`)

---

## UnitAttackSpeed

Returns information about the unit's melee attack speed

**Signature:**

```lua
speed, offhandSpeed = UnitAttackSpeed("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `speed` - Current speed of the unit's main hand attack (number of seconds per attack) (`number`)
- `offhandSpeed` - Current speed of the unit's off hand attack (number of seconds per attack) (`number`)

---

## UnitDamage

Returns information about the player's or pet's melee attack damage

**Signature:**

```lua
minDamage, maxDamage, minOffHandDamage, maxOffHandDamage, physicalBonusPos, physicalBonusNeg, percent = UnitDamage("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `minDamage` - The unit's minimum melee damage (`number`)
- `maxDamage` - The unit's maximum melee damage (`number`)
- `minOffHandDamage` - The unit's minimum offhand melee damage (`number`)
- `maxOffHandDamage` - The unit's maximum offhand melee damage (`number`)
- `physicalBonusPos` - Positive physical bonus (should be >= 0) (`number`)
- `physicalBonusNeg` - Negative physical bonus (should be <= 0) (`number`)
- `percent` - Factor by which damage output is multiplied due to buffs/debuffs (`number`)

---

## UnitDefense

Returns the player's or pet's Defense skill

**Signature:**

```lua
base, modifier = UnitDefense("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `base` - The unit's base defense skill (`number`)
- `modifier` - Temporary modifiers to defense skill (`number`)

---

## UnitRangedAttack

Returns information about the player's or pet's ranged weapon skill

**Signature:**

```lua
rangedAttackBase, rangedAttackMod = UnitRangedAttack("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `rangedAttackBase` - The unit's base ranged weapon skill (`number`)
- `rangedAttackMod` - Temporary modifiers to ranged weapon skill (`number`)

---

## UnitRangedAttackPower

Returns the player's or pet's ranged attack power

**Signature:**

```lua
base, posBuff, negBuff = UnitRangedAttackPower("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `base` - Base ranged attack power (`number`)
- `posBuff` - Positive buffs to ranged attack power (`number`)
- `negBuff` - Negative buffs to ranged attack power (`number`)

---

## UnitRangedDamage

Returns information about the player's or pet's ranged attack damage and speed

**Signature:**

```lua
rangedAttackSpeed, minDamage, maxDamage, physicalBonusPos, physicalBonusNeg, percent = UnitRangedDamage("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `rangedAttackSpeed` - Current speed of the unit's ranged attack (attacks per second), or 0 if no ranged weapon is equipped (`number`)
- `minDamage` - The minimum base damage per attack (`number`)
- `maxDamage` - The maximum base damage per attack (`number`)
- `physicalBonusPos` - Positive modifiers to ranged weapon damage (`number`)
- `physicalBonusNeg` - Negative modifiers to ranged weapon damage (`number`)
- `percent` - Factor by which damage output is multiplied due to buffs/debuffs (`number`)

---

## UnitResistance

Returns information about the player's or pet's magic resistance

**Signature:**

```lua
base, resistance, positive, negative = UnitResistance("unit", resistanceIndex)
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))
- `resistanceIndex` - Index of a magic resistance type (`number`)
  - `1` - Fire
  - `2` - Nature
  - `3` - Frost
  - `4` - Shadow
  - `5` - Arcane

**Returns:**

- `base` - Base resistance value (generally 0) (`number`)
- `resistance` - Current resistance value (including modifiers (`number`)
- `positive` - Positive resistance modifiers (`number`)
- `negative` - Negative resistance modifiers (`number`)

---

## UnitStat

Returns information about a basic character statistic for the player or pet

**Signature:**

```lua
stat, effectiveStat, posBuff, negBuff = UnitStat("unit", statIndex)
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` or `pet` (`string`, [unitID](../types/unitID.md))
- `statIndex` - Index of a basic statistic (`number`)
  - `1` - Strength
  - `2` - Agility
  - `3` - Stamina
  - `4` - Intellect
  - `5` - Spirit

**Returns:**

- `stat` - Current value of the statistic (`number`)
- `effectiveStat` - Effective value of the statistic (`number`)
- `posBuff` - Positive modifiers to the statistic (`number`)
- `negBuff` - Negative modifiers to the statistic (`number`)

---

← [WoW API Docs](../index.md)
