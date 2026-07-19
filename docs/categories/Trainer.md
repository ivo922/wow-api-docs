# Trainer functions

← [WoW API Docs](../index.md)

**30** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#trainer)

---

## BuyTrainerService

Purchases an ability or recipe available from a trainer

**Signature:**

```lua
BuyTrainerService(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

---

## CheckTalentMasterDist

Returns whether the player is in range of an NPC that can reset talents. Usable following the [`CONFIRM_TALENT_WIPE`](../events/CONFIRM_TALENT_WIPE.md) event which fires when the player speaks to an trainer NPC and chooses to reset his or her talents. Used in the default UI to hide the confirmation window for such if the player moves too far away from the NPC.

**Signature:**

```lua
inRange = CheckTalentMasterDist()
```

**Returns:**

- `inRange` - 1 if the player is in range of a talent trainer; otherwise nil (`1nil`)

---

## CloseTrainer

Ends interaction with a trainer. Fires the [`TRAINER_CLOSED`](../events/TRAINER_CLOSED.md) event, indicating that Trainer APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseTrainer()
```

---

## CollapseTrainerSkillLine

Collapses a group header in the trainer service listing

---

## ExpandTrainerSkillLine

Expands a group header in the trainer service listing

---

## GetNumTrainerServices

Returns the number of entries in the trainer service listing. Entries include both group headers and individual trainer services (i.e spells or recipes to be purchased). Reflects the list as it should currently be displayed, not necessarily the complete list -- if headers are collapsed or a filter is enabled, a smaller number will be returned.

Returns 0 if not interacting with a trainer.

**Signature:**

```lua
numServices = GetNumTrainerServices()
```

**Returns:**

- `numServices` - Number of headers and services to display in the trainer service listing (`number`)

---

## GetTrainerGreetingText

Returns the current trainer's greeting text. In the default UI, this text is displayed at the top of the trainer window.

May return the empty string or the last used trainer's greeting text if called while not interacting with a trainer.

**Signature:**

```lua
text = GetTrainerGreetingText()
```

**Returns:**

- `text` - Greeting text for the trainer with whom the player is currently interacting (`string`)

---

## GetTrainerSelectionIndex

Returns the index of the currently selected trainer service. Selection in the recipe list is used only for display in the default UI and has no effect on other Trade Skill APIs.

**Signature:**

```lua
selectionIndex = GetTrainerSelectionIndex()
```

**Returns:**

- `selectionIndex` - Index of the selected entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

---

## GetTrainerServiceAbilityReq

Returns information about an ability required for purchasing a trainer service

**Signature:**

```lua
ability, hasReq = GetTrainerServiceAbilityReq(index, abilityIndex)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)
- `abilityIndex` - Index of one of the service's ability requirements (between 1 and [`GetTrainerServiceNumAbilityReq(index)`](Trainer.md#gettrainerservicenumabilityreq)) (`number`)

**Returns:**

- `ability` - Name of the required ability (`string`)
- `hasReq` - 1 if the player has the required ability; otherwise nil (`1nil`)

---

## GetTrainerServiceCost

Returns the cost to purchase a trainer service

**Signature:**

```lua
moneyCost, talentCost, skillCost = GetTrainerServiceCost(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `moneyCost` - Amount of money required to purchase the service (in copper) (`number`)
- `talentCost` - Number of talent points required to purchase the service (generally unused) (`number`)
- `skillCost` - 1 if purchasing the service counts against the player's limit of learnable professions; otherwise 0 (`number`)

---

## GetTrainerServiceDescription

Returns the description of a trainer service. Generally returns the same description found in the spell's tooltip for spells purchased from a class trainer; returns nil for trade skills and recipes.

**Signature:**

```lua
text = GetTrainerServiceDescription(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `text` - Description of the service (`string`)

---

## GetTrainerServiceIcon

Returns the icon for a trainer service

**Signature:**

```lua
icon = GetTrainerServiceIcon(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `icon` - Path to an icon texture for the service (`string`)

---

## GetTrainerServiceInfo

Returns information about an entry in the trainer service listing

**Signature:**

```lua
serviceName, serviceSubText, serviceType, isExpanded = GetTrainerServiceInfo(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `serviceName` - Name of the service (`string`)
- `serviceSubText` - Secondary text associated with the service (often a spell rank; e.g. "(Rank 4)") (`string`)
- `serviceType` - Type of service entry (`string`)
  - `available` - The player can currently use this service
  - `header` - This entry is a group header, not a trainer service
  - `unavailable` - The player cannot currently use this service
  - `used` - The player has already used this service
- `isExpanded` - 1 if the entry is a header which is currently expanded, or if the header containing the entry is expanded; otherwise nil (`1nil`)

---

## GetTrainerServiceItemLink

Returns a hyperlink for the item associated with a trainer service. Currently only returns item links for trainer services which teach trade skill recipes which produce items; does not return spell or recipe links.

**Signature:**

```lua
link = GetTrainerServiceItemLink(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `link` - A hyperlink for the item associated with a trainer service (`string`, [hyperlink](../types/hyperlink.md))

---

## GetTrainerServiceLevelReq

Returns the character level required to purchase a trainer service

**Signature:**

```lua
reqLevel = GetTrainerServiceLevelReq(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `reqLevel` - Level required to purchase the service, or nil if the service has no level requirement (`number`)

---

## GetTrainerServiceNumAbilityReq

Returns the number of ability requirements for purchasing a trainer service. Ability requirements are often used for ranked class spells purchased from the trainer: e.g. learning Blood Strike (Rank 3) requires having learned Blood Strike (Rank 2). See [`GetTrainerServiceAbilityReq()`](Trainer.md#gettrainerserviceabilityreq) for information about specific ability requirements.

**Signature:**

```lua
numRequirements = GetTrainerServiceNumAbilityReq(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `numRequirements` - Number of different ability requirements for the trainer service (`number`)

---

## GetTrainerServiceSkillLine

Returns the name of the skill line associated with a trainer service. For trade skill trainers, skill line is the name of the trade skill (e.g. Tailoring, First Aid). For other trainers, skill line is the name of the group header under which the skill appears (e.g. Riding, Frost, Protection, Holy, Defense, Dual Wield).

**Signature:**

```lua
skillLine = GetTrainerServiceSkillLine(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `skillLine` - Name of the skill line associated with the service (`string`)

---

## GetTrainerServiceSkillReq

Returns information about the skill requirement for a trainer service. Often used for trade skill recipes: e.g. Netherweave Bag requires Tailoring (315).

**Signature:**

```lua
skill, rank, hasReq = GetTrainerServiceSkillReq(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

**Returns:**

- `skill` - Name of the required skill (`string`)
- `rank` - Rank required in the skill (`number`)
- `hasReq` - 1 if the player has the required skill and rank; otherwise nil (`1nil`)

---

## GetTrainerServiceStepIncrease `deprecated`

This function is deprecated and should no longer be used

---

## GetTrainerServiceStepReq `deprecated`

**Signature:**

```lua
GetTrainerServiceStepReq()
```

---

## GetTrainerServiceTypeFilter

Returns whether the trainer service listing is filtered by a service status

**Signature:**

```lua
isEnabled = GetTrainerServiceTypeFilter("type")
```

**Arguments:**

- `type` - A trainer service status (`string`)
  - `available` - Services the player can use
  - `unavailable` - Services the player cannot currently use
  - `used` - Services the player has already used

**Returns:**

- `isEnabled` - 1 if services matching the filter type are shown in the listing; otherwise nil (`1nil`)

---

## GetTrainerSkillLineFilter

Returns whether the trainer service listing is filtered by a skill line

---

## GetTrainerSkillLines

Returns the list of service group names available at a trainer

---

## IsTradeskillTrainer

Returns whether the player is interacting with a trade skill trainer (as opposed to a class trainer)

**Signature:**

```lua
isTradeskill = IsTradeskillTrainer()
```

**Returns:**

- `isTradeskill` - 1 if interacting with a trade skill trainer; otherwise nil (`1nil`)

---

## IsTrainerServiceSkillStep

Returns whether a trainer service is a trade skill level

---

## OpenTrainer `deprecated`

This function is deprecated and should no longer be used

---

## SelectTrainerService

Selects an entry in the trainer service listing. Selection in the service list is used only for display in the default UI and has no effect on other Trainer APIs.

**Signature:**

```lua
SelectTrainerService(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](Trainer.md#getnumtrainerservices)) (`number`)

---

## SetTrainerServiceTypeFilter

Filters the trainer service listing by service status

**Signature:**

```lua
SetTrainerServiceTypeFilter("type" [, enable [, exclusive]])
```

**Arguments:**

- `type` - A service status (`string`)
  - `available` - Services the player can use
  - `unavailable` - Services the player cannot currently use
  - `used` - Services the player has already used
- `enable` - 1 to show services matching `type` in the filtered list; 0 to hide them (`number`)
- `exclusive` - 1 to disable other type filters when enabling this one; otherwise nil (`1nil`)

---

## SetTrainerSkillLineFilter

Filters the trainer service listing by skill line. The default UI does not provide control for skill line filters, but they can nonetheless be used to alter the contents of the trainer service listing.

**Signature:**

```lua
SetTrainerSkillLineFilter("type" [, enable [, exclusive]])
```

**Arguments:**

- `type` - Index of a skill line filter (in the list returned by [`GetTrainerSkillLines()`](Trainer.md#gettrainerskilllines)) (`string`)
- `enable` - 1 to show services matching the given skill line in the filtered list; 0 to hide them (`number`)
- `exclusive` - 1 to disable other skill line filters when enabling this one; otherwise nil (`1nil`)

---

## UnitCharacterPoints

Returns the player's number of unused talent points and profession slots

---

← [WoW API Docs](../index.md)
