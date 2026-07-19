# Spell functions

← [WoW API Docs](../index.md)

**46** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#spell)

---

## CastSpell `protected`

Casts a from the spellbook. Only protected (i.e. usable only by the Blizzard UI) if the given `id` corresponds to a spell which can be cast (not a passive spell) and is not a trade skill; can be used by addons to cast the "spells" that open trade skill windows.

**Signature:**

```lua
CastSpell(id, "bookType")
```

**Arguments:**

- `id` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook

---

## CastSpellByID `protected`

Casts a spell specified by id (optionally on a specified unit). Only protected (i.e. usable only by the Blizzard UI) if the given spell is castable (not passive) and is not a trade skill; can be used by addons to cast the "spells" that open trade skill windows.

**Signature:**

```lua
CastSpellByID(spellID [, "target"])
```

**Arguments:**

- `spellID` - ID of the spell to cast (`number`, [spellID](../types/spellID.md))
- `target` - A unit to target with the spell (`string`, [unitID](../types/unitID.md))

---

## CastSpellByName `protected`

Casts a spell specified by name (optionally on a specified unit). Only protected (i.e. usable only by the Blizzard UI) if the given spell is castable (not passive) and is not a trade skill; can be used by addons to cast the "spells" that open trade skill windows.

**Signature:**

```lua
CastSpellByName("name" [, "target"])
```

**Arguments:**

- `name` - Name of a spell to cast (`string`)
- `target` - A unit to target with the spell (`string`, [unitID](../types/unitID.md))

---

## CursorHasSpell

Returns whether a spell is on the cursor. See [`GetCursorInfo()`](Cursor.md#getcursorinfo) for more detailed information.

**Signature:**

```lua
hasSpell = CursorHasSpell()
```

**Returns:**

- `hasSpell` - 1 if the cursor is currently holding a spell; otherwise nil (`1nil`)

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

## GetItemSpell

Returns information about the spell cast by an item's "Use:" effect

**Signature:**

```lua
name, rank = GetItemSpell(itemID) or GetItemSpell("itemName") or GetItemSpell("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `name` - Name of the spell (`string`)
- `rank` - Secondary text associated with the spell (often a rank, e.g. "Rank 7"); or the empty string (`""`) if not applicable (`string`)

---

## GetKnownSlotFromHighestRankSlot

Returns the spellbook slot for the player's highest known rank of a spell

**Signature:**

```lua
maxRankSlot = GetKnownSlotFromHighestRankSlot(slot)
```

**Arguments:**

- `slot` - Spellbook slot index of a known spell (`number`)

**Returns:**

- `maxRankSlot` - Spellbook slot index of the highest rank of that spell known to the player (`number`)

---

## GetNumSpellTabs

Returns the number of tabs in the player's spellbook

**Signature:**

```lua
numTabs = GetNumSpellTabs()
```

**Returns:**

- `numTabs` - Number of spellbook tabs (`number`)

**Examples:**

```lua
-- Prints the names of all spell tabs to chat
for i = 1, GetNumSpellTabs() do
  local name = GetSpellTabInfo(i);
  print(name);
end
```

---

## GetQuestLogRewardSpell

Returns information about the spell reward for the selected quest in the quest log. If both `isTradeskillSpell` and `isSpellLearned` are `nil`, the reward is a spell cast upon the player.

**Signature:**

```lua
texture, name, isTradeskillSpell, isSpellLearned = GetQuestLogRewardSpell()
```

**Returns:**

- `texture` - Path to the spell's icon texture (`string`)
- `name` - Name of the spell (`string`)
- `isTradeskillSpell` - 1 if the spell is a tradeskill recipe; otherwise nil (`1nil`)
- `isSpellLearned` - 1 if the reward teaches the player a new spell; otherwise nil (`1nil`)

---

## GetRewardSpell

Returns information about a spell awarded when completing a quest. Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED` events); otherwise may return zero or values from the most recently displayed quest.

If both `isTradeskillSpell` and `isSpellLearned` are `nil`, the reward is a spell cast upon the player.

**Signature:**

```lua
texture, name, isTradeskillSpell, isSpellLearned = GetRewardSpell()
```

**Returns:**

- `texture` - Path to the spell's icon texture (`string`)
- `name` - Name of the spell (`string`)
- `isTradeskillSpell` - 1 if the spell is a tradeskill recipe; otherwise nil (`1nil`)
- `isSpellLearned` - 1 if the reward teaches the player a new spell; otherwise nil (`1nil`)

---

## GetSpellAutocast

Returns information about automatic casting for a spell in the spellbook. Generally, only certain pet spells can be autocast.

**Signature:**

```lua
autocastAllowed, autocastEnabled = GetSpellAutocast(id, "bookType")
```

**Arguments:**

- `id` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook

**Returns:**

- `autocastAllowed` - 1 if automatic casting is allowed for the action; otherwise nil (`1nil`)
- `autocastEnabled` - 1 if automatic casting is currently turned on for the action; otherwise nil (`1nil`)

---

## GetSpellCooldown

Returns cooldown information about a spell in the spellbook

**Signature:**

```lua
start, duration, enable = GetSpellCooldown(index, "bookType") or GetSpellCooldown("name") or GetSpellCooldown(id)
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)
- `id` - Numeric ID of a spell (`number`, [spellID](../types/spellID.md))

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the spell is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the spell is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the spell is ready.) (`number`)

---

## GetSpellCount

Returns the number of times a spell can be cast. Generally used for spells whose casting is limited by the number of item reagents in the player's possession.

**Signature:**

```lua
numCasts = GetSpellCount(index, "bookType") or GetSpellCount("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `numCasts` - Number of times the spell can be cast, or 0 if unlimited (`number`)

**Examples:**

```lua
-- print a list of reagent-limited spells in the player's spellbook
local numTabs = GetNumSpellTabs()
for tabid=1,numTabs do
  local name,texture,offset,numSpells = GetSpellTabInfo(tabid)
  for spellid=1,numSpells do
    local name,rank = GetSpellName(spellid + offset, "book")
    local count = GetSpellCount(spellid + offset, "book")
    if count > 0 then
      print(name .. " ( ".. count .. " casts)")
    end
  end
end
```

---

## GetSpellInfo

Returns information about a spell

**Signature:**

```lua
name, rank, icon, powerCost, isFunnel, powerType, castingTime, minRange, maxRange = GetSpellInfo(index, "bookType") or GetSpellInfo("name") or GetSpellInfo(id)
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell, optionally including secondary text (e.g. "Mana Burn" to find the player's highest rank, or "Mana Burn(Rank 2)" -- no space before the parenthesis -- for a specific rank) (`string`)
- `id` - Numeric ID of a spell (`number`, [spellID](../types/spellID.md))

**Returns:**

- `name` - Name of the spell (`string`)
- `rank` - Secondary text associated with the spell (e.g."Rank 5", "Racial", etc.) (`string`)
- `icon` - Path to an icon texture for the spell (`string`)
- `powerCost` - Amount of mana, rage, energy, runic power, or focus required to cast the spell (`number`)
- `isFunnel` - True for spells with health funneling effects (like Health Funnel) (`boolean`)
- `powerType` - Power type to cast the spell (`number`)
  - `-2` - Health
  - `0` - Mana
  - `1` - Rage
  - `2` - Focus
  - `3` - Energy
  - `5` - Runes
  - `6` - Runic Power
- `castingTime` - Casting time of the spell in milliseconds (`number`)
- `minRange` - Minimum range from the target required to cast the spell (`number`)
- `maxRange` - Maximum range from the target at which you can cast the spell (`number`)

---

## GetSpellLink

Returns a hyperlink for a spell

**Signature:**

```lua
link, tradeLink = GetSpellLink(index, "bookType") or GetSpellLink("name") or GetSpellLink(id)
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell, optionally including secondary text (e.g. "Mana Burn" to find the player's highest rank, or "Mana Burn(Rank 2)" -- no space before the parenthesis -- for a specific rank) (`string`)
- `id` - Numeric ID of a spell (`number`, [spellID](../types/spellID.md))

**Returns:**

- `link` - A hyperlink for the spell (`string`, [hyperlink](../types/hyperlink.md))
- `tradeLink` - A hyperlink representing the player's list of trade skill recipes, if the spell is a trade skill (i.e. if "casting" the spell opens a trade skill window) (`string`)

---

## GetSpellName

Returns the name and secondary text for a spell in the spellbook. This function can been replaced with GetSpellBookItemName(index, bookType);

**Signature:**

```lua
spellName, subSpellName = GetSpellName(id, "bookType")
```

**Arguments:**

- `id` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook

**Returns:**

- `spellName` - Localized name of the spell (`string`)
- `subSpellName` - Secondary text associated with the spell (e.g. "Rank 5", "Racial Passive", "Artisan") (`string`)

---

## GetSpellTabInfo

Returns information about a tab in the spellbook

**Signature:**

```lua
name, texture, offset, numSpells = GetSpellTabInfo(index)
```

**Arguments:**

- `index` - Index of a spellbook tab (between 1 and [`GetNumSpellTabs()`](Spell.md#getnumspelltabs)) (`number`)

**Returns:**

- `name` - Name of the spellbook tab (`string`)
- `texture` - Path to an icon texture for the spellbook tab (`string`)
- `offset` - [`spellbookID`](../types/spellbookID.md) of the first spell to be listed under the tab (`number`)
- `numSpells` - Number of spells listed under the tab (`number`)

---

## GetSpellTexture

Returns the icon texture path for a spell

**Signature:**

```lua
texture = GetSpellTexture(index, "bookType") or GetSpellTexture("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `texture` - Path to an icon texture for the spell (`string`)

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

## IsAttackSpell

Returns whether a spell is the standard melee Attack spell

**Signature:**

```lua
isAttack = IsAttackSpell(index, "bookType") or IsAttackSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isAttack` - 1 if the spell enables/disables melee auto-attack; otherwise nil (`1nil`)

---

## IsAutoRepeatSpell

Returns whether a spell is an automatically repeating spell

**Signature:**

```lua
isAutoRepeat = IsAutoRepeatSpell("spellName")
```

**Arguments:**

- `spellName` - The name of the spell to query (`string`)

**Returns:**

- `isAutoRepeat` - If the spell is an auto-repeating spell (`1nil`)

---

## IsConsumableSpell

Returns whether casting a spell consumes a reagent item

**Signature:**

```lua
isConsumable = IsConsumableSpell(index, "bookType") or IsConsumableSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isConsumable` - 1 if casting the spell consumes a reagent item; otherwise nil (`1nil`)

---

## IsCurrentSpell

Returns whether a spell is currently being used

**Signature:**

```lua
isCurrent = IsCurrentSpell(index, "bookType") or IsCurrentSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isCurrent` - 1 if the spell is currently being cast, is waiting for the user to choose a target, is a repeating spell which is currently repeating, or is the open trade skill; otherwise nil (`1nil`)

---

## IsHarmfulSpell

Returns whether a spell can be used against hostile units

**Signature:**

```lua
isHarmful = IsHarmfulSpell(index, "bookType") or IsHarmfulSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isHarmful` - 1 if the spell can be used against hostile units; otherwise nil (`1nil`)

**Examples:**

```lua
-- print a list of harmful spells
local numTabs = GetNumSpellTabs()
for i=1,numTabs do
  local name,texture,offset,numSpells = GetSpellTabInfo(i)
  for spellId=1,numSpells do
    local harmful = IsHarmfulSpell(i, "spell")
    if harmful then
      local name,rank = GetSpellName(i, "spell")
      print(name .. " is a harmful spell")
    end
  end
end
```

---

## IsHelpfulSpell

Returns whether an item can be used on the player or friendly units

**Signature:**

```lua
isHarmful = IsHelpfulSpell(index, "bookType") or IsHelpfulSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isHarmful` - 1 if the spell can be used on the player or friendly units; otherwise nil (`1nil`)

---

## IsPassiveSpell

Returns whether a spell is passive (cannot be cast)

**Signature:**

```lua
isPassive = IsPassiveSpell(index, "bookType") or IsPassiveSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isPassive` - 1 if the spell is passive; otherwise nil (`1nil`)

---

## IsSelectedSpell

Returns whether a spell is currently selected in the spellbook

---

## IsSpellInRange

Returns whether the player is in range to cast a spell on a unit

**Signature:**

```lua
inRange = IsSpellInRange(index, "bookType", "unit") or IsSpellInRange("name", "unit")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)
- `unit` - A unit to target with the spell (`string`, [unitID](../types/unitID.md))

**Returns:**

- `inRange` - 1 if the player is near enough to cast the spell on the unit; 0 if not in range; nil if the unit is not a valid target for the spell (`1nil`)

---

## IsSpellKnown

Returns whether the player (or pet) knows a spell

**Signature:**

```lua
isKnown = IsSpellKnown(spellID [, isPet])
```

**Arguments:**

- `spellID` - Numeric ID of a spell (`number`, [spellID](../types/spellID.md))
- `isPet` - True to check only spells known to the player's pet; false or omitted to check only spells known to the player (`boolean`)

**Returns:**

- `isKnown` - True if the player (or pet) knows the given spell; false otherwise (`boolean`)

---

## IsUsableSpell

Returns whether or not a given spell is usable or cannot be used due to lack of mana. Does not account for spell cooldowns (see [`GetSpellCooldown()`](Spell.md#getspellcooldown) -- returns 1 if other conditions allow for casting the spell (e.g. if the spell can only be cast while outdoors).

**Signature:**

```lua
isUsable, notEnoughMana = IsUsableSpell(index, "bookType") or IsUsableSpell("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `isUsable` - 1 if the spell is castable; otherwise nil (`1nil`)
- `notEnoughMana` - 1 if the player lacks the resources (e.g. mana, energy, runes) to cast the spell; otherwise nil (`1nil`)

---

## PickupSpell

Puts a spell onto the cursor

**Signature:**

```lua
PickupSpell(spellID)
```

**Arguments:**

- `spellID` - The spellID of the spell (`number`, [spellID](../types/spellID.md))

---

## SetMultiCastSpell

Sets a multi-cast action slot to a given spell. This function is used to set up the multi-cast action slots, such as the totem bar that was introduced with WoW 3.2. The player is able to customize three different sets of totems that can then be cast with a single click.

**Signature:**

```lua
SetMultiCastSpell(action, spell)
```

**Arguments:**

- `action` - The multi-cast action slot to set (`number`)
- `spell` - The numeric spellId to set to the given action slot (`number`)

---

## SpellCanTargetGlyph

Returns whether the spell currently awaiting a target requires a glyph slot to be chosen.

Only applies when the player has attempted to cast a spell -- in this case, the "spell" cast when one uses a glyph item -- but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
canTarget = SpellCanTargetGlyph()
```

**Returns:**

- `canTarget` - 1 if the spell can target glyph slots (`1nil`)

---

## SpellCanTargetItem

Returns whether the spell currently awaiting a target requires an item to be chosen. Only applies when the player has attempted to cast a spell but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
canTarget = SpellCanTargetItem()
```

**Returns:**

- `canTarget` - 1 if the spell can target an item; otherwise nil (`1nil`)

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

## SpellHasRange

Returns whether an item has a range limitation for its use. For example: Shadowbolt can only be used on a unit within a given range of the player; Ritual of Summoning requires a target but has no range restriction; Fel Armor has no target and thus no range restriction.

**Signature:**

```lua
hasRange = SpellHasRange(index, "bookType") or SpellHasRange("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

**Returns:**

- `hasRange` - 1 if the spell has an effective range; otherwise nil. (`1nil`)

---

## SpellIsTargeting

Returns whether a spell is currently awaiting a target

**Signature:**

```lua
isTargeting = SpellIsTargeting()
```

**Returns:**

- `isTargeting` - 1 if a spell is currently awaiting a target; otherwise nil (`1nil`)

---

## SpellStopCasting `protected`

Stops casting or targeting the spell in progress

**Signature:**

```lua
SpellStopCasting()
```

---

## SpellStopTargeting `protected`

Cancels the spell currently awaiting a target. When auto-self cast is not enabled and the player casts a spell that requires a target, the cursor changes to a glowing hand so the user can select a target. This function cancels targeting mode so the player can cast another spell.

**Signature:**

```lua
SpellStopTargeting()
```

---

## SpellTargetItem `protected`

Casts the spell currently awaiting a target on an item. Usable when the player has attempted to cast a spell (e.g. an Enchanting recipe or the "Use:" effect of a sharpening stone or fishing lure) but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
SpellTargetItem(itemID) or SpellTargetItem("itemName") or SpellTargetItem("itemLink")
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

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

## ToggleSpellAutocast

Enables or disables automatic casting of a spell. Generally only pet spells can be autocast.

**Signature:**

```lua
ToggleSpellAutocast(index, "bookType") or ToggleSpellAutocast("name")
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](../types/spellbookID.md))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell (`string`)

---

## UnitCastingInfo

Returns information about the spell a unit is currently casting

**Signature:**

```lua
name, subText, text, texture, startTime, endTime, isTradeSkill, castID, notInterruptible = UnitCastingInfo("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `name` - Name of the spell being cast (`string`)
- `subText` - Secondary text associated with the spell (e.g."Rank 5", "Racial", etc.) (`string`)
- `text` - Text to be displayed on a casting bar (`string`)
- `texture` - Path to an icon texture for the spell (`string`)
- `startTime` - Time at which the cast was started (in milliseconds; can be compared to [`GetTime()`](Utility.md#gettime) `* 1000`) (`number`)
- `endTime` - Time at which the cast will finish (in milliseconds; can be compared to [`GetTime()`](Utility.md#gettime) `* 1000`) (`number`)
- `isTradeSkill` - 1 if the spell being cast is a trade skill recipe; otherwise nil (`1nil`)
- `castID` - Reference number for this spell; matches the 4th argument of `UNIT_SPELLCAST_*` events for the same spellcast (`number`)
- `notInterruptible` - 1 if the spell can be interrupted; otherwise nil. See the [`UNIT_SPELLCAST_NOT_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_NOT_INTERRUPTIBLE) and [`UNIT_SPELLCAST_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_INTERRUPTIBLE) events for changes to this status. (`1nil`)

---

## UnitChannelInfo

Returns information about the spell a unit is currently channeling

**Signature:**

```lua
name, subText, text, texture, startTime, endTime, isTradeSkill, notInterruptible = UnitChannelInfo("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `name` - Name of the spell being cast (`string`)
- `subText` - Secondary text associated with the spell (e.g."Rank 5", "Racial", etc.) (`string`)
- `text` - Text to be displayed on a casting bar (`string`)
- `texture` - Path to an icon texture for the spell (`string`)
- `startTime` - Time at which the cast was started (in milliseconds; can be compared to [`GetTime()`](Utility.md#gettime) `* 1000`) (`number`)
- `endTime` - Time at which the cast will finish (in milliseconds; can be compared to [`GetTime()`](Utility.md#gettime) `* 1000`) (`number`)
- `isTradeSkill` - 1 if the spell being cast is a trade skill recipe; otherwise nil (`1nil`)
- `notInterruptible` - Indicates that the spell cannot be interrupted, [`UNIT_SPELLCAST_NOT_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_NOT_INTERRUPTIBLE) and [`UNIT_SPELLCAST_INTERRUPTIBLE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_INTERRUPTIBLE) are fired to indicate changes in the interruptible status. (`boolean`)

---

## UpdateSpells `server`

Requests spellbook information from the server

---

← [WoW API Docs](../index.md)
