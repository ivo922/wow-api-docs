# Player information functions

← [WoW API Docs](../index.md)

**61** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#player)

---

## AcceptResurrect

Accepts an offered resurrection spell. Not used for self-resurrection; see [`UseSoulstone()`](Player information.md#usesoulstone) for such cases.

**Signature:**

```lua
AcceptResurrect()
```

---

## AcceptXPLoss `confirmation`

Resurrects the player at a spirit healer, accepting possible consequences. Resurrecting at a spirit healer generally results in a loss of durability (both equipped items and those in the player's bags) and may also result in the Resurrection Sickness debuff.

Early in the development of World of Warcraft, resurrecting at a spirit healer caused a loss of experience points. The change to a loss of item durability was made before the initial public release of World of Warcraft, but the name of this function was never changed.

**Signature:**

```lua
AcceptXPLoss()
```

---

## CanHearthAndResurrectFromArea

Returns whether the player is in a world PvP zone offering an exit option.

Used by the default UI to show the MiniMapBattlefieldFrame and provide a menu option for leaving if the player is in a world PvP combat zone (i.e. Wintergrasp).

**Signature:**

```lua
status = CanHearthAndResurrectFromArea()
```

**Returns:**

- `status` - 1 if in a world PvP zone with an exit option; otherwise nil (`1nil`)

---

## CheckBinderDist

Returns whether the player is in range of an NPC that can set the Hearthstone location. Usable following the [`CONFIRM_BINDER`](https://web.archive.org/web/20100105235302/http://wowprogramming.com/docs/events/CONFIRM_BINDER) event which fires when the player speaks to an Innkeeper (or similar) NPC and chooses to set his or her Hearthstone location. Used in the default UI to hide the confirmation window for such if the player moves too far away from the NPC.

**Signature:**

```lua
inRange = CheckBinderDist()
```

**Returns:**

- `inRange` - 1 if the player is in range of an NPC that can set the Hearthstone location; otherwise nil (`1nil`)

---

## CheckSpiritHealerDist

Returns whether the player is in range of a spirit healer. Usable following the [`CONFIRM_XP_LOSS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_XP_LOSS) event which fires upon speaking to a spirit healer while dead and choosing the option to immediately resurrect. Used in the default UI to hide the confirmation window for such if the player moves too far away from the spirit healer.

**Signature:**

```lua
inRange = CheckSpiritHealerDist()
```

**Returns:**

- `inRange` - 1 if the player is in range of a spirit healer; otherwise nil (`1nil`)

---

## ConfirmBinder

Sets the player's Hearthstone to the current location. Usable in response to the [`CONFIRM_BINDER`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_BINDER) event which fires upon speaking to an Innkeeper (or similar NPC) and choosing the Hearthstone option.

**Signature:**

```lua
ConfirmBinder()
```

---

## DeclineResurrect

Declines an offered resurrection spell. Usable following the [`RESURRECT_REQUEST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/RESURRECT_REQUEST) event which fires when the player is offered resurrection by another unit.

**Signature:**

```lua
DeclineResurrect()
```

---

## Dismount

Dismounts from the player's summoned mount

**Signature:**

```lua
Dismount()
```

---

## GetBindLocation

Returns the name of the player's Hearthstone location

**Signature:**

```lua
location = GetBindLocation()
```

**Returns:**

- `location` - Name of the player's Hearthstone location (`string`)

---

## GetComboPoints

Returns the player's number of combo points on the target.

**Signature:**

```lua
comboPoints = GetComboPoints("unit" [, "target"])
```

**Arguments:**

- `unit` - Either 'player' or 'vehicle' (`string`, [unitID](../types/unitID.md))
- `target` - Unit to check for combo points. (`string`, [unitID](../types/unitID.md))

**Returns:**

- `comboPoints` - Number of combo points (between 0 and `MAX_COMBO_POINTS`) (`number`)

---

## GetCorpseRecoveryDelay

Returns the amount of time left until the player can recover their corpse. Applies to resurrection spells offered by other units, resurrecting by returning to the player's corpse as a ghost, and to resurrecting at a graveyard's spirit healer, if the player has recently died several times in short succession.

**Signature:**

```lua
timeLeft = GetCorpseRecoveryDelay()
```

**Returns:**

- `timeLeft` - Amount of time remaining before the player can resurrect (in seconds); 0 if the player can resurrect immediately (`number`)

---

## GetCurrentTitle

Returns the currently selected player title

**Signature:**

```lua
currentTitle = GetCurrentTitle()
```

**Returns:**

- `currentTitle` - Index of the player's current title (between 1 and [`GetNumTitles()`](Player information.md#getnumtitles)) (`integer`)

---

## GetNumTitles

Returns the number of available player titles. Includes all titles, not just those earned by the player

**Signature:**

```lua
numTitles = GetNumTitles()
```

**Returns:**

- `numTitles` - Number of available player titles (`number`)

---

## GetPlayerFacing

Returns the player's orientation (heading). Indicates the direction the player model is (normally) facing and in which the player will move if he begins walking forward, not the camera orientation.

**Signature:**

```lua
facing = GetPlayerFacing()
```

**Returns:**

- `facing` - Direction the player is facing (in radians, 0 = north, values increasing counterclockwise) (`number`)

---

## GetQuestLogRewardTitle

Returns the title reward for the selected quest in the quest log. Returns `nil` if no title is awarded or if no quest is selected.

**Signature:**

```lua
title = GetQuestLogRewardTitle()
```

**Returns:**

- `title` - Title to be awarded to the player upon completing the quest (`string`)

---

## GetRealmName

Returns the name of the player's realm (server name)

**Signature:**

```lua
realm = GetRealmName()
```

**Returns:**

- `realm` - The name of the player's realm (server) (`string`)

---

## GetReleaseTimeRemaining

Returns the amount of time remaining until the player's spirit is automatically released when dead. Returns `-1` if the player died in a dungeon or raid instance; in such cases, the player's spirit will not be released automatically (see [`RepopMe()`](Player information.md#repopme) to release manually).

**Signature:**

```lua
timeleft = GetReleaseTimeRemaining()
```

**Returns:**

- `timeleft` - Amount of time remaining until the player's spirit is automatically released to the nearest graveyard (in seconds) (`number`)

---

## GetResSicknessDuration

Returns the duration of resurrection sickness at the player's current level. Returns nil for players under level 10, who are allowed to resurrect at a spirit healer without suffering resurrection sickness.

**Signature:**

```lua
resSicknessTime = GetResSicknessDuration()
```

**Returns:**

- `resSicknessTime` - Text describing the duration of resurrection sickness were the player to resurrect at a spirit healer (`string`)

---

## GetRestState

Returns the player's current rest state

**Signature:**

```lua
state, name, multiplier = GetRestState()
```

**Returns:**

- `state` - Number identiying the current rest state (`number`)
  - `1` - Rested
  - `2` - Normal
  - `3` - Tired - used in locales with account play time limits
  - `4` - Unhealthy - used in locales with account play time limits
- `name` - Localized text describing the player's current rest state (`string`)
- `multiplier` - Multiplier for experience points earned from kills (`number`)

---

## GetRuneCooldown

Returns cooldown information about one of the player's rune resources. Note the placement of runes 3-4 (normally Unholy) and 5-6 (normally Frost) are reversed in the default UI. Also note the behavior of returned values differs slightly from most other GetXYZCooldown-style functions.

**Signature:**

```lua
start, duration, runeReady = GetRuneCooldown(slot)
```

**Arguments:**

- `slot` - Index of a rune slot, as positioned in the default UI: (`number`)
  - `1` - Leftmost
  - `2` - Second from left
  - `3` - Fifth from left (second from right)
  - `4` - Sixth from left (rightmost)
  - `5` - Third from left
  - `6` - Fourth from left

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the rune is ready (`number`)
- `duration` - The length of the cooldown (regardless of whether the rune is currently cooling down) (`number`)
- `runeReady` - True if the rune can be used; false if the rune is cooling down (`boolean`)

---

## GetRuneCount

Returns the number of available rune resources in one of the player's rune slots. Returns 1 if a rune is ready and 0 if a rune is on cooldown.

**Signature:**

```lua
count = GetRuneCount(slot)
```

**Arguments:**

- `slot` - Index of a rune slot, as positioned in the default UI: (`number`)
  - `1` - Leftmost
  - `2` - Second from left
  - `3` - Fifth from left (second from right)
  - `4` - Sixth from left (rightmost)
  - `5` - Third from left
  - `6` - Fourth from left

**Returns:**

- `count` - Number of available runes in the slot (`number`)

---

## GetRuneType

Returns the type of one of the player's rune resources. Note the placement of runes 3-4 (normally Unholy) and 5-6 (normally Frost) are reversed in the default UI.

**Signature:**

```lua
runeType = GetRuneType(slot)
```

**Arguments:**

- `slot` - Index of a rune slot, as positioned in the default UI: (`number`)
  - `1` - Leftmost
  - `2` - Second from left
  - `3` - Fifth from left (second from right)
  - `4` - Sixth from left (rightmost)
  - `5` - Third from left
  - `6` - Fourth from left

**Returns:**

- `runeType` - Type of the rune (`number`)
  - `1` - Blood rune
  - `2` - Unholy rune
  - `3` - Frost rune
  - `4` - Death rune

---

## GetTimeToWellRested `deprecated`

This function is deprecated and should no longer be used

---

## GetTitleName

Returns the text of an available player title

**Signature:**

```lua
titleName = GetTitleName(titleIndex)
```

**Arguments:**

- `titleIndex` - Index of a title available to the player (between 1 and [`GetNumTitles()`](Player information.md#getnumtitles)) (`integer`)

**Returns:**

- `titleName` - The text of the title (`string`)

---

## GetUnitPitch

Returns the player's current pitch (slope or angle of movement). Only valid for the unitID "player". The slope returned here reflects only the direction of movement for swimming or flying, not the current orientation of the player model or camera. (When on solid ground, GetUnitPitch indicates what the angle of flight would be were the player to start flying.)

The returned value is in radians, with positive values indicating upward slope, negative values indicating downward slope, and 0 indicating perfectly level flight (or swimming).

**Signature:**

```lua
pitch = GetUnitPitch("unit")
```

**Arguments:**

- `unit` - Unit to query; only valid for `player` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `pitch` - Unit's slope of movement in radians (`number`)

---

## GetUnitSpeed

Returns a unit's current speed. Valid for all observable units. Values returned indicate the current movement speed in yards per second. (It's not relative to facing or ground position; i.e. you won't see a smaller value when flying up at an angle or a negative value when backing up.) Does not indicate falling speed or the speed of boats, zeppelins, and some forms of quest-related transportation, but does indicate current speed on taxi flights and when moving due to combat effects such as Disengage, Death Grip, or various knockback abilities.

Examples: Normal running: 7; Walking: 2.5; Running backwards: 4.5; Epic flying mount: 26.6

**Signature:**

```lua
speed = GetUnitSpeed(unit)
```

**Arguments:**

- `unit` - Unit to query (`unitid`)

**Returns:**

- `speed` - Unit's current speed in yards per second (`number`)

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

## HasFullControl

Returns whether the player character can be controlled

**Signature:**

```lua
hasControl = HasFullControl()
```

**Returns:**

- `hasControl` - 1 if the player character can be controlled (i.e. isn't feared, charmed, etc); otherwise nil (`1nil`)

---

## HasKey

Returns whether the player has any keys stored in the Keyring container. Used in the default UI to show or hide the UI for the Keyring container

**Signature:**

```lua
hasKey = HasKey()
```

**Returns:**

- `hasKey` - Returns 1 if the player has any keys stored in the Keyring container; otherwise nil (`1nil`)

---

## HasSoulstone

Returns whether the player can instantly resurrect in place. Only returns valid information while the player is dead and has not yet released his or her spirit to the graveyard.

**Signature:**

```lua
text = HasSoulstone()
```

**Returns:**

- `text` - If the player can resurrect in place, the text to be displayed on the dialog button for such (e.g. "Use Soulstone", "Reincarnate"); otherwise nil (`string`)

---

## HasWandEquipped

Returns whether the player has a wand equipped

**Signature:**

```lua
isEquipped = HasWandEquipped()
```

**Returns:**

- `isEquipped` - 1 if a wand is equipped; otherwise nil (`1nil`)

---

## IsFalling

Returns whether the player is currently falling

**Signature:**

```lua
falling = IsFalling()
```

**Returns:**

- `falling` - 1 if the player is falling; otherwise nil (`1nil`)

---

## IsFlyableArea

**Signature:**

```lua
isFlyable = IsFlyableArea()
```

**Returns:**

- `isFlyable` - 1 if the current area is a flyable area, otherwise nil (`1nil`)

---

## IsFlying

Returns whether the player is currently flying

**Signature:**

```lua
isFlying = IsFlying()
```

**Returns:**

- `isFlying` - 1 if the player is currently flying; otherwise nil (`1nil`)

---

## IsInInstance

Returns whether the player is in an instance (and its type if applicable)

**Signature:**

```lua
isInstance, instanceType = IsInInstance()
```

**Returns:**

- `isInstance` - 1 if the player is in an instance, otherwise nil (`1nil`)
- `instanceType` - The type of instance the player is in (`string`)
  - `arena` - Player versus player arena
  - `none` - Not inside an instance
  - `party` - 5-man instance
  - `pvp` - Player versus player battleground
  - `raid` - Raid instance

---

## IsIndoors

Returns whether the player is currently indoors

**Signature:**

```lua
inside = IsIndoors()
```

**Returns:**

- `inside` - 1 if the player is currently indoors; otherwise nil (`1nil`)

---

## IsMounted

**Signature:**

```lua
mounted = IsMounted()
```

**Returns:**

- `mounted` - 1 if the player is mounted, otherwise nil (`1nil`)

---

## IsOutOfBounds

Returns whether the player is currently outside the bounds of the world. Used in the default UI (in conjunction with [`IsFalling()`](Player information.md#isfalling)) to allow the player to release to a graveyard if the character has encountered a bug and fallen underneath the world geometry.

**Signature:**

```lua
outOfBounds = IsOutOfBounds()
```

**Returns:**

- `outOfBounds` - 1 if the player is currently outside the bounds of the world; otherwise nil (`1nil`)

---

## IsOutdoors

Returns whether the player is currently outdoors. "Outdoors" as defined by this function corresponds to the ability to use a mount in that specific location, not necessarily whether there is a roof above the player character's head. For example, returns 1 in Ironforge, Undercity, and the Caverns of Time, but nil in the nominally outdoor areas of instances such as Stratholme, Drak'tharon Keep, and Hellfire Ramparts. (Note that even in "outdoor" areas, standing on top of certain objects may interfere with the player's ability to mount up.)

**Signature:**

```lua
isOutdoors = IsOutdoors()
```

**Returns:**

- `isOutdoors` - 1 if the player is currently outdoors; otherwise nil (`1nil`)

---

## IsResting

Returns whether the player is currently resting. Rest state is provided in Inns and major cities and allows the player to log out immediately (instead of after a brief delay) and accrue bonus XP to be awarded for kills.

**Signature:**

```lua
resting = IsResting()
```

**Returns:**

- `resting` - 1 if the player is resting; otherwise nil (`boolean`)

---

## IsStealthed

Returns whether the player is currently stealthed

**Signature:**

```lua
stealthed = IsStealthed()
```

**Returns:**

- `stealthed` - 1 if rogue Stealth, druid cat form Prowl, or a similar ability is active on the player; otherwise nil (`1nil`)

---

## IsSwimming

Returns whether the player is currently swimming. "Swimming" as defined by this function corresponds to the ability to use swimming abilities (such as druid Aquatic Form) or inability to use land-restricted abilities (such as eating or summoning a flying mount), not necessarily to whether the player is in water.

**Signature:**

```lua
isSwimming = IsSwimming()
```

**Returns:**

- `isSwimming` - 1 if the player is currently swimming; otherwise nil (`1nil`)

---

## IsTitleKnown

Returns whether the player has earned the ability to display a title

**Signature:**

```lua
isKnown = IsTitleKnown(titleIndex)
```

**Arguments:**

- `titleIndex` - Index of a title available to the player (between 1 and [`GetNumTitles()`](Player information.md#getnumtitles)) (`integer`)

**Returns:**

- `isKnown` - 1 if the player has earned the ability to display the title; otherwise nil (`1nil`)

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

## OffhandHasWeapon

Returns whether the player has an equipped weapon in the off hand slot

**Signature:**

```lua
hasWeapon = OffhandHasWeapon()
```

**Returns:**

- `hasWeapon` - 1 if the player has a weapon equipped in the off hand slot; otherwise nil (`1nil`)

---

## OpeningCinematic

Displays the introductory cinematic for the player's race. Only has effect if the player has never gained any experience.

**Signature:**

```lua
OpeningCinematic()
```

---

## RepopMe

Releases the player's spirit to the nearest graveyard. Only has effect if the player is dead.

**Signature:**

```lua
RepopMe()
```

---

## ResurrectGetOfferer

Returns the name of a unit offering to resurrect the player.

Returns nil if no resurrection has been offered or if an offer has expired.

**Signature:**

```lua
name = ResurrectGetOfferer()
```

**Returns:**

- `name` - Name of the unit offering resurrection (`string`)

---

## ResurrectHasSickness

Returns whether accepting an offered resurrection spell will cause the player to suffer Resurrection Sickness. Usable following the [`RESURRECT_REQUEST`](https://web.archive.org/web/20100105214257/http://wowprogramming.com/docs/api/RESURRECT_REQUEST) event which fires when the player is offered resurrection by another unit.

Generally always returns `nil`, as resurrection by other players does not cause sickness.

**Signature:**

```lua
hasSickness = ResurrectHasSickness()
```

**Returns:**

- `hasSickness` - 1 if accepting resurrection will cause Resurrection Sickness; otherwise nil (`1nil`)

---

## ResurrectHasTimer

Returns whether the player must wait before resurrecting. Applies to resurrection spells offered by other units, resurrecting by returning to the player's corpse as a ghost, and to resurrecting at a graveyard's spirit healer, if the player has recently died several times in short succession. See [`GetCorpseRecoveryDelay()`](Player information.md#getcorpserecoverydelay) for the time remaining until the player can resurrect.

**Signature:**

```lua
hasTimer = ResurrectHasTimer()
```

**Returns:**

- `hasTimer` - 1 if the player must wait before resurrecting; otherwise nil (`1nil`)

---

## RetrieveCorpse

Confirms resurrection by returning to the player's corpse

**Signature:**

```lua
RetrieveCorpse()
```

---

## SetCurrentTitle `hardware`

Changes a player's displayed title

**Signature:**

```lua
SetCurrentTitle(titleIndex)
```

**Arguments:**

- `titleIndex` - Index of a title available to the player (between 1 and [`GetNumTitles()`](Player information.md#getnumtitles)), or -1 to show no title (`integer`)

---

## ShowCloak

Enables or disables display of the player's cloak. Only affects the player's appearance; does not change the other effects of having the cloak equipped. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
ShowCloak(show)
```

**Arguments:**

- `show` - 1 to display the player's cloak; nil to hide it (`1nil`)

---

## ShowHelm

Enables or disables display of the player's headgear. Only affects the player's appearance; does not change the other effects of having the headgear equipped. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
ShowHelm(show)
```

**Arguments:**

- `show` - 1 to display the player's headgear; nil to hide it (`1nil`)

---

## ShowingCloak

Returns whether the player's cloak is displayed. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
isShown = ShowingCloak()
```

**Returns:**

- `isShown` - 1 if the player's cloak is shown; otherwise nil (`1nil`)

---

## ShowingHelm

Returns whether the player's headgear is displayed. Determines not only the appearance of the player character on the local client, but the way other players see the character as well.

**Signature:**

```lua
isShown = ShowingHelm()
```

**Returns:**

- `isShown` - 1 if the player's headgear is shown; otherwise nil (`1nil`)

---

## ToggleSheath

Sheaths or unsheaths the player character's hand-held items. Calling repeatedly will cause the player character to draw his or her melee weapons, followed by his or her range weapon, followed by hiding all weapons.

**Signature:**

```lua
ToggleSheath()
```

---

## UnitCharacterPoints

Returns the player's number of unused talent points and profession slots

---

## UnitXP

Returns the player's current amount of experience points

**Signature:**

```lua
currXP = UnitXP("unit")
```

**Arguments:**

- `unit` - A unit to query; only valid for `player` (`string`, [unitID](../types/unitID.md))

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

- `unit` - A unit to query; only valid for `player` (`string`, [unitID](../types/unitID.md))

**Returns:**

- `playerMaxXP` - Total amount of experience points required for the player to gain a level (`number`)

---

## UseSoulstone

Instantly resurrects the player in place, if possible. Usable if the player is dead (and has not yet released his or her spirit to the graveyard) and has the ability to instantly resurrect (provided by a Warlock's Soulstone or a Shaman's Reincarnation passive ability).

**Signature:**

```lua
UseSoulstone()
```

---

← [WoW API Docs](../index.md)
