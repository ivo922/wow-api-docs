# Talent functions

← [WoW API Docs](../index.md)

**21** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#talent)

---

## AddPreviewTalentPoints

Spends (or unspends) talent points in the Talent UI's preview mode

**Signature:**

```lua
AddPreviewTalentPoints(tabIndex, talentIndex, points, isPet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `points` - Number of points to spend on the talent, or a negative number to unspend points. Values larger than allowed for the talent will be clipped to the maximum value (e.g. attempting to spend ten points on a talent that has five ranks will only spend up to five points). (`number`)
- `isPet` - True to edit talents for the player's pet, false to edit talents for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

---

## CheckTalentMasterDist

Returns whether the player is in range of an NPC that can reset talents. Usable following the [`CONFIRM_TALENT_WIPE`](https://web.archive.org/web/20111212183617/http://wowprogramming.com/docs/events/CONFIRM_TALENT_WIPE) event which fires when the player speaks to an trainer NPC and chooses to reset his or her talents. Used in the default UI to hide the confirmation window for such if the player moves too far away from the NPC.

**Signature:**

```lua
inRange = CheckTalentMasterDist()
```

**Returns:**

- `inRange` - 1 if the player is in range of a talent trainer; otherwise nil (`1nil`)

---

## ConfirmTalentWipe `confirmation`

Resets the player's talents. Usable following the [`CONFIRM_TALENT_WIPE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_TALENT_WIPE) event which fires when the player speaks to an trainer NPC and chooses to reset his or her talents.

**Signature:**

```lua
ConfirmTalentWipe()
```

---

## GetActiveTalentGroup

Returns the index of the active talent specialization

**Signature:**

```lua
activeTalentGroup = GetActiveTalentGroup(isInspect, isPet)
```

**Arguments:**

- `isInspect` - true to query talent info for the currently inspected unit, false to query talent info for the player (`boolean`)
- `isPet` - true to query talent info for the player's pet, false to query talent info for the player (`boolean`)

**Returns:**

- `activeTalentGroup` - Which talent group is currently active (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents

---

## GetGroupPreviewTalentPointsSpent

Returns the total number of points spent in the Talent UI's preview mode.

This function only counts points spent in the preview mode, not those actually learned.

**Signature:**

```lua
pointsSpent = GetGroupPreviewTalentPointsSpent(isPet, talentGroup)
```

**Arguments:**

- `isPet` - true to query talent info for the player's pet, false to query talent info for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `pointsSpent` - Number of points spent in preview mode (`number`)

---

## GetNumTalentGroups

Returns the number of talent specs a character can switch among

**Signature:**

```lua
numTalentGroups = GetNumTalentGroups(isInspect, isPet)
```

**Arguments:**

- `isInspect` - true to query talent info for the currently inspected unit, false to query talent info for the player (`boolean`)
- `isPet` - true to query talent info for the player's pet, false to query talent info for the player (`boolean`)

**Returns:**

- `numTalentGroups` - Number of talent groups the character has enabled (`number`)
  - `1` - Default
  - `2` - The character has purchased Dual Talent Specialization

---

## GetNumTalentTabs

Returns the number of talent tabs for the player, pet, or inspect target

**Signature:**

```lua
numTabs = GetNumTalentTabs(inspect, pet)
```

**Arguments:**

- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)

**Returns:**

- `numTabs` - Number of talent tabs (`number`)

---

## GetNumTalents

Returns the number of options in a talent tab

**Signature:**

```lua
numTalents = GetNumTalents(tabIndex, inspect, pet)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)

**Returns:**

- `numTalents` - Number of different talent options (`number`)

---

## GetPetTalentTree

Returns the name of the talent tree used by the player's current pet. Hunter pets use one of three different talent trees according to pet type. Returns `nil` if the player does not have a pet or the player's current pet does not use talents (i.e. warlock pets, quest pets, etc.)

**Signature:**

```lua
talent = GetPetTalentTree()
```

**Returns:**

- `talent` - Localized name of the pet's talent tree (`string`)

---

## GetPreviewTalentPointsSpent `deprecated`

This function is deprecated and should no longer be used

---

## GetTalentInfo

Returns information about a talent option

**Signature:**

```lua
name, iconTexture, tier, column, rank, maxRank, isExceptional, meetsPrereq, previewRank, meetsPreviewPrereq = GetTalentInfo(tabIndex, talentIndex, inspect, pet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `name` - Name of the talent (`string`)
- `iconTexture` - The icon texture of the talent. (`string`)
- `tier` - Row in which the talent should be displayed (1 = top) (`number`)
- `column` - Column in which the talent should be displayed (1 = left) (`number`)
- `rank` - Number of points spent in the talent (`number`)
- `maxRank` - Maximum number of points that can be spent in the talent (`number`)
- `isExceptional` - 1 if the talent confers a new ability (spell); otherwise nil (`1nil`)
- `meetsPrereq` - 1 if the prerequisites to learning the talent have been met; otherwise nil (`1nil`)
- `previewRank` - Number of points spent in the talent in preview mode (`number`)
- `meetsPreviewPrereq` - 1 if the prerequisites to learning the talent have been met in preview mode; otherwise nil (`1nil`)

---

## GetTalentLink

Returns a hyperlink for a talent

**Signature:**

```lua
link = GetTalentLink(tabIndex, talentIndex, inspect, pet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100105230815/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100105230815/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `link` - A hyperlink representing the talent and the number of points spent in it (`string`, [hyperlink](https://web.archive.org/web/20100105230815/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetTalentPrereqs

Returns information about prerequisites to learning a talent

**Signature:**

```lua
tier, column, isLearnable, isPreviewLearnable, ... = GetTalentPrereqs(tabIndex, talentIndex, inspect, pet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `tier` - Row in which the talent's prerequisite is displayed (1 = top) (`number`)
- `column` - Column in which the talent's prerequisite is displayed (1 = left) (`number`)
- `isLearnable` - 1 if the talent is learnable; otherwise nil (`1nil`)
- `isPreviewLearnable` - 1 if the talent is learnable in preview mode; otherwise nil (`1nil`)
- `...` - Additional sets of `tier, column, isLearnable, isPreviewLearnable` values for each prerequisite to learning the talent (`list`)

---

## GetTalentTabInfo

Returns information about a talent tab

**Signature:**

```lua
id, name, description, icon, points, background, previewPoints, isUnlocked = GetTalentTabInfo(tabIndex, inspect, pet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `id` - ID of the talent tab (`number`, [blizzid](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#blizzid))
- `name` - Name of the talent tab (`string`)
- `description` - Localized summary of the talent tab (`string`)
- `icon` - Path to an icon texture for the talent tab (`string`)
- `points` - Number of points spent in the talent tab (`number`)
- `background` - Path to a background texture for the talent tab (`string`)
- `previewPoints` - Number of points spent in the talent tab in preview mode (`number`)
- `isUnlocked` - Whether the player can put points into the talent tab or not (`boolean`)

---

## GetUnspentTalentPoints

Returns the number of unused talent points

**Signature:**

```lua
points = GetUnspentTalentPoints(inspect, pet, talentGroup)
```

**Arguments:**

- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `points` - Number of points available for spending (`number`)

---

## LearnPreviewTalents `confirmation`

Commits changes made in the Talent UI's preview mode

**Signature:**

```lua
LearnPreviewTalents(isPet)
```

**Arguments:**

- `isPet` - true to edit talents for the player's pet, false to edit talents for the player (`boolean`)

---

## LearnTalent

Learns a talent, spending one talent point

**Signature:**

```lua
LearnTalent(tabIndex, talentIndex, isPet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `isPet` - True to edit talents for the player's pet, false to edit talents for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

---

## ResetGroupPreviewTalentPoints

Reverts all changes made in the Talent UI's preview mode

**Signature:**

```lua
ResetGroupPreviewTalentPoints(isPet, talentGroup)
```

**Arguments:**

- `isPet` - true to edit talents for the player's pet, false to edit talents for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

---

## ResetPreviewTalentPoints

Reverts changes made within a specific tab in the Talent UI's preview mode

**Signature:**

```lua
ResetPreviewTalentPoints(tabIndex, isPet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent school/tab (between 1 and GetNumTalentTabs()) (`number`)
- `isPet` - true to edit talents for the player's pet, false to edit talents for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

---

## SetActiveTalentGroup

Switches the player's active talent specialization.

Calling this function with the index of an inactive talent group does not immediately perform the switch: it begins casting a spell ("Activate Primary/Secondary Spec"), and only once the spellcast is complete are the player's talents changed.

Calling this function with the index of the active talent group, or with any argument if the player has not purchased Dual Talent Specialization does nothing.

**Signature:**

```lua
SetActiveTalentGroup(talentGroup)
```

**Arguments:**

- `talentGroup` - Index of the talent specialization to enable (`number`)

---

## UnitCharacterPoints

Returns the player's number of unused talent points and profession slots

---

← [WoW API Docs](../index.md)
