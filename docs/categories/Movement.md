# Movement functions

← [WoW API Docs](../index.md)

**28** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#movement)

---

## AscendStop `protected`

Stops movement initiated by [`JumpOrAscendStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/JumpOrAscendStart). Used by the `JUMP` binding, which also controls ascent when swimming or flying. Has no meaningful effect if called while jumping (in which case movement is generally stopped by hitting the ground).

**Signature:**

```lua
AscendStop()
```

---

## DescendStop `protected`

Stops movement initiated by [`SitStandOrDescendStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SitStandOrDescendStart). Used by the `SITORSTAND` binding, which also controls descent when swimming or flying. Has no meaningful effect if called while sitting/standing.

**Signature:**

```lua
DescendStop()
```

---

## FollowUnit

Causes the player character to automatically follow another unit. Only friendly player units can be followed.

**Signature:**

```lua
FollowUnit("unit") or FollowUnit("name" [, strict])
```

**Arguments:**

- `unit` - A unit to follow (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit to follow (`string`)
- `strict` - True if only an exact match for the given name should be allowed; false to allow partial matches (`boolean`)

---

## InteractUnit `protected`

Interacts with (as with right-clicking on) a unit

**Signature:**

```lua
InteractUnit(unit)
```

**Arguments:**

- `unit` - The unit to interact with (`unitid`)

---

## JumpOrAscendStart `protected`

Causes the player character to jump (or begins ascent if swimming or flying). Used by the `JUMP` binding, which also controls ascent when swimming or flying.

**Signature:**

```lua
JumpOrAscendStart()
```

---

## MoveAndSteerStart `protected`

Begins moving the player character forward while steering via mouse movement. After calling this function, the player character begins moving forward while cursor movement rotates (or steers) the character, altering yaw (facing) and/or pitch (vertical movement angle) as well as camera position.

Equivalent to calling both [`CameraOrSelectOrMoveStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/CameraOrSelectOrMoveStart) and [`TurnOrActionStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TurnOrActionStart) without calling the respective `Stop` functions; i.e. holding both left and right mouse buttons down. Used by the `MOVEANDSTEER` binding, which can be customized to allow alternate access to this action if the player's system does not allow pressing multiple mouse buttons at once.

**Signature:**

```lua
MoveAndSteerStart()
```

---

## MoveAndSteerStop `protected`

Ends movement initiated by [`MoveAndSteerStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveAndSteerStart). After calling this function, forward movement and character steering stops and normal cursor movement resumes.

Used by the `MOVEANDSTEER` binding.

**Signature:**

```lua
MoveAndSteerStop()
```

---

## MoveBackwardStart `protected`

Begins moving the player character backward. Used by the `MOVEBACKWARD` binding.

**Signature:**

```lua
MoveBackwardStart()
```

---

## MoveBackwardStop `protected`

Ends movement initiated by [`MoveBackwardStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveBackwardStart)

**Signature:**

```lua
MoveBackwardStop()
```

---

## MoveForwardStart `protected`

Begins moving the player character forward. Used by the `MOVEFORWARD` binding.

**Signature:**

```lua
MoveForwardStart()
```

---

## MoveForwardStop `protected`

Ends movement initiated by [`MoveForwardStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveForwardStart)

**Signature:**

```lua
MoveForwardStop()
```

---

## PitchDownStart `protected`

Begins adjusting the player character's angle of vertical movement downward. Affects only the angle or slope of movement for swimming or flying; has no immediately visible effect if the player is not moving, but alters the trajectory followed as soon as the player begins moving. Continuously adjusts pitch until the minimum angle is reached or [`PitchDownStop()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PitchDownStop) is called.

Used by the `PITCHDOWN` binding.

**Signature:**

```lua
PitchDownStart()
```

---

## PitchDownStop `protected`

Ends movement initiated by [`PitchDownStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PitchDownStart)

**Signature:**

```lua
PitchDownStop()
```

---

## PitchUpStart `protected`

Begins adjusting the player character's angle of vertical movement upward. Affects only the angle or slope of movement for swimming or flying; has no immediately visible effect if the player is not moving, but alters the trajectory followed as soon as the player begins moving. Continuously adjusts pitch until the maximum angle is reached or [`PitchUpStop()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PitchUpStop) is called.

Used by the `PITCHUP` binding.

**Signature:**

```lua
PitchUpStart()
```

---

## PitchUpStop `protected`

Ends movement initiated by [`PitchUpStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PitchUpStart)

**Signature:**

```lua
PitchUpStop()
```

---

## SitStandOrDescendStart `protected`

Causes the player character to sit down if standing and vice versa (or begins descent if swimming or flying). Used by the `SITORSTAND` binding, which also controls descent when swimming or flying.

**Signature:**

```lua
SitStandOrDescendStart()
```

---

## StrafeLeftStart `protected`

Begins moving the player character sideways to his or her left

**Signature:**

```lua
StrafeLeftStart()
```

---

## StrafeLeftStop `protected`

Ends movement initiated by [`StrafeLeftStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/StrafeLeftStart)

**Signature:**

```lua
StrafeLeftStop()
```

---

## StrafeRightStart `protected`

Begins moving the player character sideways to his or her right

**Signature:**

```lua
StrafeRightStart()
```

---

## StrafeRightStop `protected`

Ends movement initiated by [`StrafeRightStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/StrafeRightStart)

**Signature:**

```lua
StrafeRightStop()
```

---

## ToggleAutoRun `protected`

Starts or stops the player character automatically moving forward

**Signature:**

```lua
ToggleAutoRun()
```

---

## ToggleRun `protected`

Switches the character's ground movement mode between running and walking. If running, switches to walking, and vice versa. Has no effect on swimming or flying speed.

**Signature:**

```lua
ToggleRun()
```

---

## TurnLeftStart `protected`

Begins turning the player character to the left. "Left" here is relative to the player's facing; i.e. if looking down at the character from above, he or she turns counter-clockwise.

Used by the `TURNLEFT` binding.

**Signature:**

```lua
TurnLeftStart()
```

---

## TurnLeftStop `protected`

Ends movement initiated by [`TurnLeftStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TurnLeftStart)

**Signature:**

```lua
TurnLeftStop()
```

---

## TurnOrActionStart `protected`

Begins character steering or interaction (equivalent to right-clicking in the 3-D world). After calling this function (i.e. while the right mouse button is held), cursor movement rotates (or steers) the player character, altering yaw (facing) and/or pitch (vertical movement angle) as well as camera position. Final results vary by context and are determined when calling [`TurnOrActionStop()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TurnOrActionStop) (i.e. releasing the right mouse button).

Used by the `TURNORACTION` binding (not customizable in the default UI), which is bound to the right mouse button by default.

**Signature:**

```lua
TurnOrActionStart()
```

---

## TurnOrActionStop `protected`

Ends action initiated by [`TurnOrActionStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TurnOrActionStart). After calling this function (i.e. releasing the right mouse button), character steering stops and normal cursor movement resumes. If the cursor has not moved significantly since calling [`TurnOrActionStart()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TurnOrActionStart_) (i.e. pressing the right mouse button), results vary by context:

if the cursor is over a nearby unit, interacts with (or attacks) that unit, making it the player's target.

if the cursor is over a nearby interactable world object (e.g. mailbox, treasure chest, or quest object), interacts with (or uses) that object.

if the cursor is over a faraway unit or world object and the "Click-to-Move" option is enabled (i.e. the "autointeract" CVar is "1"), attempts to move the player character to the unit/object and interact with it once nearby.

if the cursor is over a faraway world object and the "Click-to-Move" option is disabled, fires a [`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE) event indicating the player is too far away to interact with the object.

otherwise, does nothing.

Used by the `TURNORACTION` binding (not customizable in the default UI), which is bound to the right mouse button by default.

**Signature:**

```lua
TurnOrActionStop()
```

---

## TurnRightStart `protected`

Begins turning the player character to the right. "Right" here is relative to the player's facing; i.e. if looking down at the character from above, he or she turns clockwise.

Used by the `TURNRIGHT` binding.

**Signature:**

```lua
TurnRightStart()
```

---

## TurnRightStop `protected`

Ends movement initiated by [`TurnRightStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TurnRightStart)

**Signature:**

```lua
TurnRightStop()
```

---

← [WoW API Docs](../index.md)
