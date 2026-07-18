# Action functions

← [WoW API Docs](../index.md)

**26** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#action)

---

## ActionHasRange

Returns whether an action has a range restriction

**Signature:**

```lua
hasRange = ActionHasRange(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `hasRange` - 1 if the action has a range restriction; otherwise nil (`1nil`)

---

## CastPetAction `protected`

Casts a pet action on a specific target

**Signature:**

```lua
CastPetAction(index [, "unit"])
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)
- `unit` - A unit to be used as target for the action (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

---

## GetActionAutocast `deprecated`

Returns information about autocast actions. No player actions have allowed automatic casting since the initial public release of World of Warcraft.

**Signature:**

```lua
autocastAllowed, autocastEnabled = GetActionAutocast(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `autocastAllowed` - 1 if automatic casting is allowed for the action; otherwise nil (`1nil`)
- `autocastEnabled` - 1 if automatic casting is currently turned on for the action; otherwise nil (`1nil`)

---

## GetActionCooldown

Returns cooldown information about an action

**Signature:**

```lua
start, duration, enable = GetActionCooldown(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `start` - The value of [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) at the moment the cooldown began, or 0 if the action is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the action is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the action is ready.) (`number`)

**Examples:**

```lua
-- Show all actions currently on cooldown
for i=1,120 do
   local start,duration,enable = GetActionCooldown(i)
   if start > 0 and enable == 1 then
      local actiontype,id,subtype = GetActionInfo(i)
      local name
      
      if actiontype == "spell" then
         name = GetSpellName(id, "spell")
      elseif actiontype == "item" then
         name = GetItemInfo(id)
      elseif actiontype == "companion" then
         name = select(2, GetCompanionInfo(subtype, id))
      end
      
      local timeLeft = math.floor((start + duration) - GetTime())
      local output = string.format("Cooldown on %s %s (%s seconds left)", actiontype, name, timeLeft)
      ChatFrame1:AddMessage(output)
      
   end
end
```

---

## GetActionCount

Returns the number of uses remaining for the given action slot. Applies to spells that require reagents, items that stack, or items with charges; used in the default UI to display the count on action buttons.

Returns 0 for any action that does not use a count. To distinguish between actions which do not use a count and actions which do but whose current count is 0, see [`IsConsumableAction`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsConsumableAction).

**Signature:**

```lua
count = GetActionCount(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `count` - Number of times the action can be used (`number`)

---

## GetActionInfo

Returns information about an action slot

**Signature:**

```lua
type, id, subType, spellID = GetActionInfo(slot)
```

**Arguments:**

- `slot` - An action slot (`number`)

**Returns:**

- `type` - Type of action in the slot (`string`)
  - `companion` - Summons a mount or non-combat pet
  - `equipmentset` - Equips a set of items
  - `item` - Uses an item
  - `macro` - Runs a macro
  - `spell` - Casts a spell
- `id` - An identifier for the action; varies by type: (`number or string`)
  - `companion` - The companion's index in the mount or minipet list
  - `equipmentset` - Name of the equipment set
  - `item` - The item's [itemID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemID)
  - `macro` - The macro's index in the macro list ([macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
  - `spell` - The spell's index in the player's spellboook ([spellbookID)](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#spellbookID)
- `subType` - Subtype of the action (or `nil` if not applicable) (`string`)
  - `CRITTER` - For `companion` actions: indicates `id` is as an index in the non-combat pets list
  - `MOUNT` - For `companion` actions: indicates `id` is an index in the mounts list
  - `spell` - For `spell` actions: indicates `id` is an index in the player's spellbook (as opposed to the pet's)
- `spellID` - For `spell` and `companion` actions, the global ID of the spell (or the summoning "spell" for a companion) (`string`, [spellID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#spellID))

**Examples:**

```lua
-- Prints all types and subtypes found in the player's actions
local types = {}
for i=1,120 do
   local type,id,subtype = GetActionInfo(i)
   if type then
      types[type] = types[type] or {}
      if subtype then
         types[type][subtype] = 1
      end
   end
end

for type, subtypes in pairs(types) do
   print("Type:", type, "subtypes:")
   local numSubtypes = 0
   for subtype in pairs(subtypes) do
      print("   ", subtype)
      numSubtypes = numSubtypes + 1
   end

   if numSubtypes == 0 then
      print("   no subtypes")
   end
end
```

---

## GetActionText

Returns the text label associated with an action. Currently used only for macros, which in the default UI show their name as a label on an action button.

**Signature:**

```lua
text = GetActionText(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `text` - Label for the action (`string`)

---

## GetActionTexture

Returns the icon texture for an action. Can be the icon of a spell or item, the icon manually set for a macro, or an icon reflecting the current state of a macro.

**Signature:**

```lua
texture = GetActionTexture(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `texture` - Path to an icon texture for the action in the slot, or nil if the slot is empty (`string`)

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

- `start` - The value of [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) at the moment the cooldown began, or 0 if the action is ready (`number`)
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

Returns whether the pet's actions are usable. Note: [`GetPetActionSlotUsable`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetPetActionSlotUsable) can return nil for individual actions even if `GetPetActionsUsable` returns 1 (though not the other way around).

**Signature:**

```lua
petActionsUsable = GetPetActionsUsable()
```

**Returns:**

- `petActionsUsable` - 1 if the pet's actions are usable; otherwise nil (`1nil`)

---

## HasAction

Returns whether an action slot contains an action

**Signature:**

```lua
hasAction = HasAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `hasAction` - 1 if the slot contains an action; otherwise nil (`1nil`)

---

## IsActionInRange

Returns whether the player's target is in range of an action

**Signature:**

```lua
inRange = IsActionInRange(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `inRange` - 1 if the player's target is in range for the action or 0 if out of range; nil if the action cannot be used on the player's target regardless of range (`number`)

---

## IsAttackAction

Returns whether an action is the standard melee Attack action. Used in the default UI to flash the action button while auto-attack is active. Does not apply to other repeating actions such as Auto Shot (for hunters) and Shoot (for wand users); for those, see [`IsAutoRepeatAction`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsAutoRepeatAction).

**Signature:**

```lua
isAttack = IsAttackAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isAttack` - 1 if the action enables/disables melee auto-attack; otherwise nil (`1nil`)

---

## IsAutoRepeatAction

Returns whether an action is an automatically repeating action. Used in the default UI to flash the action button while the action is repeating. Applies to actions such as Auto Shot (for hunters) and Shoot (for wand and other ranged weapon users) but not to the standard melee Attack action; for it, see [`IsAttackAction`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsAttackAction).

**Signature:**

```lua
isRepeating = IsAutoRepeatAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isRepeating` - 1 if the action is an auto-repeat action; otherwise nil (`1nil`)

---

## IsConsumableAction

Returns whether using an action consumes an item. Applies both to consumable items (such as food and potions) and to spells which use a reagent (e.g. Prayer of Fortitude, Divine Intervention, Water Walking, Portal: Dalaran).

**Signature:**

```lua
isConsumable = IsConsumableAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isConsumable` - 1 if using the action consumes an item; otherwise nil (`1nil`)

---

## IsCurrentAction

Returns whether an action is currently being used

**Signature:**

```lua
isCurrent = IsCurrentAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isCurrent` - 1 if the action is currently being cast, is waiting for the user to choose a target, is a repeating action which is currently repeating, or is the open trade skill; otherwise nil (`1nil`)

---

## IsEquippedAction

Returns whether an action contains an equipped item. Applies to actions involving equippable items (not to consumables or other items with "Use:" effects) and indicates the effect of performing the action: if an action's item is not equipped, using the action will equip it; if the item is equipped and has a "Use:" effect, using the action will activate said effect.

**Signature:**

```lua
isEquipped = IsEquippedAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isEquipped` - 1 if the action contains an equipped item; otherwise nil (`1nil`)

---

## IsStackableAction

Returns whether an action uses stackable items. Applies to consumable items such as potions, wizard oils, food and drink; not used for spells which consume reagents (for those, see [`IsConsumableAction`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsConsumableAction)).

**Signature:**

```lua
isStackable = IsStackableAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isStackable` - 1 if the action uses stackable items; otherwise nil (`1nil`)

---

## IsUsableAction

Returns whether an action is usable

**Signature:**

```lua
isUsable, notEnoughMana = IsUsableAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

**Returns:**

- `isUsable` - 1 if the action is usable; otherwise nil (`1nil`)
- `notEnoughMana` - 1 if the player lacks the resources (e.g. mana, energy, runes) to use the action; otherwise nil (`1nil`)

---

## PickupAction `nocombat`

Puts the contents of an action bar slot onto the cursor or the cursor contents into an action bar slot. After an action is picked up via this function, it can only be placed into other action bar slots (with [`PlaceAction()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PlaceAction) or by calling `PickupAction()` again), even if the action is an item which could otherwise be placed elsewhere. Unlike many other "pickup" cursor functions, this function removes the picked-up action from the source slot -- an action slot can be emptied by calling this function followed by [`ClearCursor()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ClearCursor).

If the action slot is empty and the cursor already holds an action, a spell, a companion (mount or non-combat pet), a macro, an equipment set, or an item (with a "Use:" effect), it is put into the action slot. If both the cursor and the slot hold an action (or any of the above data types), the contents of the cursor and the slot are exchanged.

**Signature:**

```lua
PickupAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

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

## PlaceAction `nocombat`

Puts the contents of the cursor into an action bar slot. If the action slot is empty and the cursor already holds an action, a spell, a companion (mount or non-combat pet), a macro, an equipment set, or an item (with a "Use:" effect), it is put into the action slot. If both the cursor and the slot hold an action (or any of the above data types), the contents of the cursor and the slot are exchanged.

Does nothing if the cursor is empty.

**Signature:**

```lua
PlaceAction(slot)
```

**Arguments:**

- `slot` - Destination action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

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

## UseAction `protected`

Uses an action

**Signature:**

```lua
UseAction(slot [, "target" [, "button"]])
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))
- `target` - A unit to be used as target for the action (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `button` - Mouse button used to activate the action (`string`)
  - `Button4` - Fourth mouse button
  - `Button5` - Fifth mouse button
  - `LeftButton` - Left mouse button (also used when the action is activated via keyboard)
  - `MiddleButton` - Third mouse button (typically middle button / scroll wheel)
  - `RightButton` - Right mouse button

---

← [WoW API Docs](../index.md)
