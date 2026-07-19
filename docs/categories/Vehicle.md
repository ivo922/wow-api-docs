# Vehicle functions

← [WoW API Docs](../index.md)

**37** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#vehicle)

---

## CanEjectPassengerFromSeat

Returns whether the player can eject the occupant of a seat in the player's vehicle

**Signature:**

```lua
canEject = CanEjectPassengerFromSeat(seat)
```

**Arguments:**

- `seat` - Index of a seat in the player's vehicle (`number`)

**Returns:**

- `canEject` - True if the player can eject the seat's occupant; false if the player cannot eject the occupant or if the seat is empty (`boolean`)

---

## CanExitVehicle

Returns whether the player is in a vehicle. Used in the default UI to determine whether to show the "Leave Vehicle" button while controlling siege vehicles, turrets, and certain special mounts and quest entities.

**Signature:**

```lua
canExit = CanExitVehicle()
```

**Returns:**

- `canExit` - 1 if the player is in a vehicle and can exit; otherwise nil (`1nil`)

---

## CanSwitchVehicleSeat

Returns whether the player can change vehicle seats. Tells you if the player can switch seats in general, whereas [UnitVehicleSeatInfo](Vehicle.md#unitvehicleseatinfo)() tells you if the player can switch into a specific seat.

**Signature:**

```lua
canSwitch = CanSwitchVehicleSeat()
```

**Returns:**

- `canSwitch` - Can the player change vehicle seats (`boolean`)

---

## CanSwitchVehicleSeats

Returns whether the player is in a vehicle with multiple seats

**Signature:**

```lua
canSwitch = CanSwitchVehicleSeats()
```

**Returns:**

- `canSwitch` - 1 if the player can switch seats; otherwise nil (`1nil`)

---

## CombatTextSetActiveUnit

Sets the main unit for display of floating combat text.

Certain types of floating combat text are only displayed for the "active" unit (normally the player): incoming damage, incoming heals, mana/energy/power gains, low health/mana warnings, etc. This function is used by the default UI to allow the player's vehicle to "stand in" for the player for purposes of combat text; using this function with units other than "player" or "vehicle" has no effect.

**Signature:**

```lua
CombatTextSetActiveUnit(unit)
```

**Arguments:**

- `unit` - Unit to show main combat text for (`unitid`)

---

## EjectPassengerFromSeat

Ejects the occupant of a seat in the player's vehicle

**Signature:**

```lua
EjectPassengerFromSeat(seat)
```

**Arguments:**

- `seat` - Index of a seat in the player's vehicle (`number`)

---

## IsUsingVehicleControls `internal`

This is a Blizzard internal function

---

## IsVehicleAimAngleAdjustable

Returns whether the player is controlling a vehicle weapon with adjustable aim angle

**Signature:**

```lua
hasAngleControl = IsVehicleAimAngleAdjustable()
```

**Returns:**

- `hasAngleControl` - 1 if the player is controlling a vehicle weapon with adjustable aim angle; otherwise nil (`1nil`)

---

## IsVehicleAimPowerAdjustable `internal`

This is a Blizzard internal function

---

## UnitControllingVehicle

Returns whether a unit is controlling a vehicle

**Signature:**

```lua
isControlling = UnitControllingVehicle("unit") or UnitControllingVehicle("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `isControlling` - True if the unit is controlling a vehicle; otherwise false (`boolean`)

---

## UnitHasVehicleUI

Returns whether a unit is controlling a vehicle or vehicle weapon. Used in the default UI to show the vehicle's health and power status bars in place of the controlling unit's. Returns false for passengers riding in but not controlling part of a vehicle; to find out whether a unit is riding in a vehicle, use [`UnitInVehicle`](Vehicle.md#unitinvehicle). Also note that in some vehicles the player can command a vehicle weapon (e.g. gun turret) without controlling the vehicle itself; to find out whether a unit is controlling a vehicle, use [`UnitControllingVehicle`](Vehicle.md#unitcontrollingvehicle).

**Signature:**

```lua
hasVehicle = UnitHasVehicleUI("unit") or UnitHasVehicleUI("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `hasVehicle` - True if the unit is controlling a vehicle or vehicle weapon; otherwise false (`boolean`)

---

## UnitInVehicle

Returns whether a unit is in a vehicle. A unit can be riding in a vehicle without controlling it: to test whether a unit is controlling a vehicle, use [`UnitControllingVehicle`](Vehicle.md#unitcontrollingvehicle) or [`UnitHasVehicleUI`](Vehicle.md#unithasvehicleui).

Note: multi-passenger mounts appear as vehicles for passengers but not for the owner.

**Signature:**

```lua
inVehicle = UnitInVehicle("unit") or UnitInVehicle("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `inVehicle` - 1 if the unit is in a vehicle; otherwise nil (`1nil`)

---

## UnitInVehicleControlSeat

Returns whether a unit controls a vehicle

**Signature:**

```lua
isInControl = UnitInVehicleControlSeat()
```

**Returns:**

- `isInControl` - True if the unit controls a vehicle (`boolean`)

---

## UnitIsControlling

Returns whether a unit is controlling another unit. Applies to Mind Control and similar cases as well as to players piloting vehicles.

**Signature:**

```lua
isControlling = UnitIsControlling("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `isControlling` - 1 if the unit is controlling another unit; otherwise nil (`1nil`)

---

## UnitSwitchToVehicleSeat

Moves the player to another seat within his current vehicle

**Signature:**

```lua
UnitSwitchToVehicleSeat("unit", seat)
```

**Arguments:**

- `unit` - Unit to move (only valid for `player`) (`string`, [unitID](../types/unitID.md))
- `seat` - Index of a seat to switch to (`number`)

---

## UnitTargetsVehicleInRaidUI

Returns whether attempts to target a unit should target its vehicle. The unit can still be targeted: this flag is used to provide a convenience in the default UI for certain cases (such as the Malygos encounter) such that clicking a unit in the raid UI targets its vehicle (e.g. so players can use their drakes to heal other players' drakes).

**Signature:**

```lua
targetVehicle = UnitTargetsVehicleInRaidUI("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `targetVehicle` - True if clicking the unit's raid UI representation should target the unit's vehicle instead of the unit itself; otherwise false (`boolean`)

---

## UnitUsingVehicle

Returns whether a unit is using a vehicle. Unlike similar functions, `UnitUsingVehicle()` also returns `true` while the unit is transitioning between seats in a vehicle.

**Signature:**

```lua
usingVehicle = UnitUsingVehicle("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `usingVehicle` - `1` if the unit is using a vehicle; otherwise `nil` (`1nil`)

---

## UnitVehicleSeatCount

Returns the number of seats in a unit's vehicle. Note: returns 0 for multi-passenger mounts even thought multiple seats are available.

**Signature:**

```lua
numSeats = UnitVehicleSeatCount("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))

**Returns:**

- `numSeats` - Number of seats in the unit's vehicle (`number`)

---

## UnitVehicleSeatInfo

Returns information about seats in a vehicle. Note: multi-passenger mounts appear as vehicles for passengers but not for the owner; seat information applies only to the passenger seats.

**Signature:**

```lua
controlType, occupantName, occupantRealm, canEject, canSwitchSeats = UnitVehicleSeatInfo("unit", seat)
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `seat` - Index of a seat in the unit's vehicle (`number`)

**Returns:**

- `controlType` - Type of control for the seat (`string`)
  - `Child` - Unit in this seat controls part of the vehicle but not its movement (e.g. a gun turret)
  - `None` - Unit in this seat has no control over the vehicle
  - `Root` - Unit in this seat controls the movement of the vehicle
- `occupantName` - Name of the unit in the seat, or nil if the seat is empty (`string`)
- `occupantRealm` - Home realm of the unit in the seat; nil if the seat is empty or its occupant is from the same realm as the player (`string`)
- `canEject` - True if the vehicle's driver can eject the occupant of the seat (`boolean`)
- `canSwitchSeats` - True if the player can switch to this seat. (`boolean`)

---

## UnitVehicleSkin

Returns the style of vehicle UI to display for a unit

**Signature:**

```lua
skin = UnitVehicleSkin("unit") or UnitVehicleSkin("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - Name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `skin` - Token identifying the style of vehicle UI to display for the unit (`string`)
  - `Mechanical` - Used for mechanical vehicles
  - `Natural` - Used for creature mounts

---

## VehicleAimDecrement

Adjusts vehicle aim downward by a specified amount

**Signature:**

```lua
VehicleAimDecrement(amount)
```

**Arguments:**

- `amount` - Angle by which to adjust aim (in radians) (`number`)

---

## VehicleAimDownStart `protected`

Starts adjusting vehicle aim downward

**Signature:**

```lua
VehicleAimDownStart()
```

---

## VehicleAimDownStop `protected`

Stops adjusting vehicle aim downward

**Signature:**

```lua
VehicleAimDownStop()
```

---

## VehicleAimGetAngle

Returns the aim angle of a vehicle weapon. The returned value is in radians, with positive values indicating upward angle, negative values indicating downward angle, and 0 indicating straight ahead.

**Signature:**

```lua
angle = VehicleAimGetAngle()
```

**Returns:**

- `angle` - Vertical angle of vehicle weapon aim (in radians) (`number`)

---

## VehicleAimGetNormAngle

Returns the aim angle of a vehicle weapon relative to its minimum angle. The returned value is in radians, with 0 indicating the lowest angle allowed for the vehicle weapon and increasing values for upward aim.

**Signature:**

```lua
angle = VehicleAimGetNormAngle()
```

**Returns:**

- `angle` - Vertical angle of vehicle weapon aim (in radians) (`number`)

---

## VehicleAimGetNormPower `internal`

This is a Blizzard internal function

---

## VehicleAimIncrement

Adjusts vehicle aim upward by a specified amount

**Signature:**

```lua
VehicleAimIncrement(amount)
```

**Arguments:**

- `amount` - Angle by which to adjust aim (in radians) (`number`)

---

## VehicleAimRequestAngle

Attempts to set a vehicle weapon's aim angle to a specific value. Causes aim angle to transition smoothly from the current value to the requested value (or to the closest allowed value to the requested value if it is beyond the vehicle's limits).

Aim angle values are in radians, with positive values indicating upward angle, negative values indicating downward angle, and 0 indicating straight ahead.

**Signature:**

```lua
VehicleAimRequestAngle(amount)
```

**Arguments:**

- `amount` - New aim angle (in radians) (`number`)

---

## VehicleAimRequestNormAngle

Attempts to set a vehicle weapon's aim angle to a specific value relative to its minimum value. Causes aim angle to transition smoothly from the current value to the requested value (or to the closest allowed value to the requested value if it is beyond the vehicle's limits).

The returned value is in radians, with 0 indicating the lowest angle allowed for the vehicle weapon and increasing values for upward aim.

**Signature:**

```lua
VehicleAimRequestNormAngle(amount)
```

**Arguments:**

- `amount` - New aim angle (in radians) (`number`)

---

## VehicleAimSetNormPower `internal`

This is a Blizzard internal function

---

## VehicleAimUpStart `protected`

Starts adjusting vehicle aim upward

**Signature:**

```lua
VehicleAimUpStart()
```

---

## VehicleAimUpStop `protected`

Stops adjusting vehicle aim upward

**Signature:**

```lua
VehicleAimUpStop()
```

---

## VehicleCameraZoomIn

Zooms the player's view in while in a vehicle

**Signature:**

```lua
VehicleCameraZoomIn()
```

---

## VehicleCameraZoomOut

Zooms the player's view out while in a vehicle

**Signature:**

```lua
VehicleCameraZoomOut()
```

---

## VehicleExit

Removes the player from the current vehicle. Does nothing if the player is not in a vehicle.

**Signature:**

```lua
VehicleExit()
```

---

## VehicleNextSeat

Moves the player from his current seat in a vehicle to the next sequentially numbered seat. If the player is in the highest-numbered seat, cycles around to the lowest-numbered seat.

**Signature:**

```lua
VehicleNextSeat()
```

---

## VehiclePrevSeat

Moves the player from his current seat in a vehicle to the previous sequentially numbered seat. If the player is in the lowest-numbered seat, cycles around to the highest-numbered seat.

**Signature:**

```lua
VehiclePrevSeat()
```

---

← [WoW API Docs](../index.md)
