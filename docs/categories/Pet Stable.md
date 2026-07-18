# Pet Stable functions

← [WoW API Docs](../index.md)

**14** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#stable)

---

## BuyStableSlot `confirmation`

Purchases the next available stable slot, without confirmation. Only available while interacting with a Stable Master NPC (between the `PET_STABLE_SHOW` and `PET_STABLE_CLOSED` events and only if [`IsAtStableMaster()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/IsAtStableMaster) returns true).

**Signature:**

```lua
BuyStableSlot()
```

---

## ClickStablePet

Inspects or moves a pet in the Pet Stable UI. Action taken depends on cursor contents as well as the `index` passed:

If the cursor does not contain a pet, selects the given pet slot.

If the cursor contains the active pet and `index` is a stable slot, places the pet into the stable (but not necessarily into the given slot).

If the cursor contains a stabled pet, and `index` is 0, makes the stabled pet the active pet (and puts the active pet into the stable).

**Signature:**

```lua
selected = ClickStablePet(index)
```

**Arguments:**

- `index` - Index of a stable slot (`number`)
  - `0` - Active pet
  - `1 to NUM_PET_STABLE_SLOTS` - A stable slot

**Returns:**

- `selected` - 1 if the function selected a stabled pet, rather than placed a pet in the stable slot (`1nil`)

---

## ClosePetStables

Ends use of the Pet Stables UI/API. Causes the `PET_STABLE_CLOSED` event to fire, indicating that stables-related APIs are no longer valid.

**Signature:**

```lua
ClosePetStables()
```

---

## GetNextStableSlotCost

Returns the cost of the next available stable slot

---

## GetNumStablePets

Returns the number of stabled pets. Returned value does not include the current pet.

**Signature:**

```lua
numPets = GetNumStablePets()
```

**Returns:**

- `numPets` - Number of pets in the stables (`number`)

---

## GetNumStableSlots

Returns the number of stable slots the player has purchased.

---

## GetSelectedStablePet

Returns the index of the selected stable pet

**Signature:**

```lua
selectedPet = GetSelectedStablePet()
```

**Returns:**

- `selectedPet` - Index of the currently selected stable pet (`number`)
  - `-1` - The player has no pets (in the stables or otherwise)
  - `0` - The active pet is selected
  - `1 to NUM_PET_STABLE_SLOTS` - A stable slot is selected

---

## GetStablePetFoodTypes

Returns the types of food that a stabled pet will eat

**Signature:**

```lua
... = GetStablePetFoodTypes(index)
```

**Arguments:**

- `index` - Index of a stable slot (`number`)
  - `0` - Active pet
  - `1 to NUM_PET_STABLE_SLOTS` - A stabled pet

**Returns:**

- `...` - A list of strings, each the localized name of a food type the pet will eat (`list`)

---

## GetStablePetInfo

Returns information about a stabled pet

**Signature:**

```lua
icon, name, level, family, talent = GetStablePetInfo(index)
```

**Arguments:**

- `index` - Index of a stable slot (`number`)
  - `0` - Active pet
  - `1 to NUM_PET_STABLE_SLOTS` - A stable slot

**Returns:**

- `icon` - Path to an icon texture for the pet (`string`)
- `name` - Name of the pet (`string`)
- `level` - Level of the pet (`number`)
- `family` - Localized name of the pet's creature family (e.g. Cat, Bear, Chimaera) (`string`)
- `talent` - Localized name of the pet's talent tree (e.g. Ferocity, Tenacity, Cunning) (`string`)

---

## IsAtStableMaster

Returns whether the player is interacting with a Stable Master NPC. The Pet Stable UI/API can be active without an NPC if the player is using the [Call Stabled Pet](http://www.wowhead.com/?spell= 62757) ability. New stable slots can only be purchased while talking to an NPC -- the default UI uses this function to determine whether to show UI elements related to purchasing slots.

**Signature:**

```lua
isAtNPC = IsAtStableMaster()
```

**Returns:**

- `isAtNPC` - True if the player is interacting with a Stable Master NPC; otherwise false (`boolean`)

---

## PickupStablePet

Puts a pet from the stables onto the cursor. Use with [`ClickStablePet`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ClickStablePet) to move pets between stabled and active status.

**Signature:**

```lua
PickupStablePet(index)
```

**Arguments:**

- `index` - Index of a stable slot (`number`)
  - `0` - Active pet
  - `1 to NUM_PET_STABLE_SLOTS` - A stable slot

---

## SetPetStablePaperdoll

Sets the given Model to show the selected stabled pet

**Signature:**

```lua
SetPetStablePaperdoll(model)
```

**Arguments:**

- `model` - A Model frame (`table`)

**Examples:**

```lua
-- Open the character window and the pet stable before running this code
-- Changes the character model to the pet model
SetPetStablePaperdoll(CharacterModelFrame)
```

---

## StablePet

Puts the player's current pet into the stables

**Signature:**

```lua
StablePet()
```

---

## UnstablePet

Makes a pet from the stables the active pet

---

← [WoW API Docs](../index.md)
