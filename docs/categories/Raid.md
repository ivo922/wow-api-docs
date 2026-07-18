# Raid functions

← [WoW API Docs](../index.md)

**33** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#raid)

---

## AcceptGroup

Accepts an invitation to join a party or raid. Usable in response to the [`PARTY_INVITE_REQUEST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PARTY_INVITE_REQUEST) event which fires when the player is invited to join a group. This function does not automatically hide the default UI's group invite dialog; doing such requires calling `StaticPopup_Hide("PARTY_INVITE")`, but only after the [`PARTY_MEMBERS_CHANGED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PARTY_MEMBERS_CHANGED) event fires indicating the player has successfully joined the group.

**Signature:**

```lua
AcceptGroup()
```

---

## ClearPartyAssignment `protected`

Removes a group role assignment from a member of the player's party or raid. If no unit (or name) is given, removes the role assignment from all members of the party or raid.

**Signature:**

```lua
ClearPartyAssignment("assignment" [, "unit"]) or ClearPartyAssignment("assignment" [, "name" [, exactMatch]])
```

**Arguments:**

- `assignment` - A group role to assign to the unit (`string`)
  - `MAINASSIST` - Remove the main assist role
  - `MAINTANK` - Remove the main tank role
- `unit` - A unit in the player's party or raid (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit in the player's party or raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

## ConfirmReadyCheck

Responds to a ready check

**Signature:**

```lua
ConfirmReadyCheck(ready)
```

**Arguments:**

- `ready` - True to report as "ready"; false to report as "not ready" (`true`)

---

## ConvertToRaid

Converts a party to a raid. Only has effect if the player is in a party and the party leader.

**Signature:**

```lua
ConvertToRaid()
```

---

## DeclineGroup

Declines an invitation to join a party or raid. Usable in response to the [`PARTY_INVITE_REQUEST`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PARTY_INVITE_REQUEST) event which fires when the player is invited to join a group.

**Signature:**

```lua
DeclineGroup()
```

---

## DemoteAssistant

Demotes the given player from raid assistant status

**Signature:**

```lua
DemoteAssistant("unit") or DemoteAssistant("name" [, exactMatch])
```

**Arguments:**

- `unit` - A unit in the raid (`string`, [unitID](https://web.archive.org/web/20111212184456/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit in the raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

## DoReadyCheck

Initiates a ready check. Only has effect if the player is the party/raid leader or a raid assistant.

**Signature:**

```lua
DoReadyCheck()
```

---

## GetNumRaidMembers

Returns the number of members in the player's raid

**Signature:**

```lua
numRaidMembers = GetNumRaidMembers()
```

**Returns:**

- `numRaidMembers` - Number of members in the raid (including the player) (`number`)

---

## GetPartyAssignment

Returns whether a party/raid member is assigned a specific group role

**Signature:**

```lua
isAssigned = GetPartyAssignment("assignment", "unit") or GetPartyAssignment("assignment", "name" [, exactMatch])
```

**Arguments:**

- `assignment` - A group role assignment (`string`)
  - `MAINASSIST` - Return whether the unit is assigned the main assist role
  - `MAINTANK` - Return whether the unit is assigned the main tank role
- `unit` - A unit in the player's party or raid (`string`, [unitID](https://web.archive.org/web/20100712064245/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit in the player's party or raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

**Returns:**

- `isAssigned` - 1 if the unit is assigned the specified role; otherwise nil (`1nil`)

---

## GetRaidRosterInfo

**Signature:**

```lua
name, rank, subgroup, level, class, fileName, zone, online, isDead, role, isML = GetRaidRosterInfo(index)
```

**Arguments:**

- `index` - The index of the raid member (`number`)

**Returns:**

- `name` - The name of the player (`string`)
- `rank` - The player's rank in the raid (`number`)
  - `Raid Assistant`
  - `Raid Leader`
  - `0` - Raid Member
- `subgroup` - The raid subgroup that the player belongs to (`number`)
- `level` - The player's level (`number`)
- `class` - The localized name of the player's class (`string`)
- `fileName` - The uppercase english name of the player's class (`string`)
  - `DRUID`
  - `HUNTER`
  - `MAGE`
  - `PALADIN`
  - `PRIEST`
  - `ROGUE`
  - `SHAMAN`
  - `WARLOCK`
  - `WARRIOR`
- `zone` - The name of the zone the player is currently in (`string`)
- `online` - 1 if the player is currently online, otherwise nil (`1nil`)
- `isDead` - 1 if the player is currently dead, otherwise nil (`1nil`)
- `role` - The player's role, or nil (`string`)
  - `MAINASSIST`
  - `MAINTANK`
- `isML` - 1 if the player is the master-looter, otherwise nil (`1nil`)

---

## GetRaidRosterSelection

Returns the index of the selected unit in the raid roster. Selection in the raid roster is used only for display in the default UI and has no effect on other Raid APIs.

**Signature:**

```lua
raidIndex = GetRaidRosterSelection()
```

**Returns:**

- `raidIndex` - Index of the raid member (between 1 and [`GetNumRaidMembers()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumRaidMembers)); matches the numeric part of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID), e.g. 21 for `raid21` (`number`)

---

## GetRaidTargetIndex

Returns the index of the raid target marker on a unit

**Signature:**

```lua
index = GetRaidTargetIndex("unit") or GetRaidTargetIndex("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query; only valid for `player`, `pet`, and party/raid members (`string`)

**Returns:**

- `index` - Index of a target marker (`number`)
  - `1` - Star
  - `2` - Circle
  - `3` - Diamond
  - `4` - Triangle
  - `5` - Moon
  - `6` - Square
  - `7` - Cross
  - `8` - Skull
  - `nil` - No marker

---

## GetReadyCheckStatus

Returns a unit's status during a ready check. Returns nil for all units unless the player is the party/raid leader or a raid assistant.

**Signature:**

```lua
status = GetReadyCheckStatus("unit")
```

**Arguments:**

- `unit` - A unit in the player's party or raid (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `status` - Ready check status for the unit (`string`)
  - `"notready"` - Unit has responded as not ready
  - `"ready"` - Unit has responded as ready
  - `"waiting"` - Unit has not yet responded
  - `nil` - No ready check is in progress

---

## GetReadyCheckTimeLeft

Returns the amount of time left on the current ready check. Returns `0` if no ready check is in progress.

**Signature:**

```lua
timeLeft = GetReadyCheckTimeLeft()
```

**Returns:**

- `timeLeft` - Amount of time remaining on the ready check (in seconds) (`number`)

---

## GetRealNumRaidMembers

Returns the number of members in the player's non-battleground raid. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
numMembers = GetRealNumRaidMembers()
```

**Returns:**

- `numMembers` - Number of members in the player's non-battleground raid (`number`)

---

## InviteUnit

Invites a character to the player's party or raid

**Signature:**

```lua
InviteUnit("name")
```

**Arguments:**

- `name` - Name of a character to invite (`string`)

---

## IsRaidLeader

Returns whether the player is the raid leader

**Signature:**

```lua
isLeader = IsRaidLeader()
```

**Returns:**

- `isLeader` - 1 if the player is the raid leader; otherwise nil (`1nil`)

---

## IsRaidOfficer

Returns whether the player is a raid assistant

**Signature:**

```lua
isRaidOfficer = IsRaidOfficer()
```

**Returns:**

- `isRaidOfficer` - 1 if the player is a raid assistant; otherwise nil (`boolean`)

---

## IsRealRaidLeader

Returns whether the player is the leader of a non-battleground raid. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
isLeader = IsRealRaidLeader()
```

**Returns:**

- `isLeader` - 1 if the player is the leader of a non-battleground raid; otherwise nil (`1nil`)

---

## LeaveParty

Exits the current party or raid. If there are only two characters in the party or raid, causes the party or raid to be disbanded.

**Signature:**

```lua
LeaveParty()
```

---

## PromoteToAssistant

Promotes a raid member to raid assistant

**Signature:**

```lua
PromoteToAssistant("unit") or PromoteToAssistant("name" [, exactMatch])
```

**Arguments:**

- `unit` - A unit in the raid (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit in the raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

## PromoteToLeader

Promotes a player to party/raid leader

**Signature:**

```lua
PromoteToLeader("unit") or PromoteToLeader("name" [, exactMatch])
```

**Arguments:**

- `unit` - A unit in the party or raid (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a party member (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

## SetPartyAssignment `protected`

Assigns a group role to a member of the player's party or raid

**Signature:**

```lua
SetPartyAssignment("assignment", "unit") or SetPartyAssignment("assignment", "name" [, exactMatch])
```

**Arguments:**

- `assignment` - A group role to assign to the unit (`string`)
  - `MAINASSIST` - Assign the main assist role
  - `MAINTANK` - Assign the main tank role
- `unit` - A unit in the player's party or raid (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit in the player's party or raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

---

## SetRaidRosterSelection

Selects a unit in the raid roster. Selection in the raid roster is used only for display in the default UI and has no effect on other Raid APIs.

**Signature:**

```lua
SetRaidRosterSelection(index)
```

**Arguments:**

- `index` - Index of the raid member (between 1 and [`GetNumRaidMembers()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumRaidMembers)); matches the numeric part of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID), e.g. 21 for `raid21` (`number`)

---

## SetRaidSubgroup

Moves a raid member to a non-full raid subgroup. Only has effect if the player is the raid leader or a raid assistant. To put a member into a full subgroup (switching places with a member of that group), see [`SwapRaidSubgroup()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SwapRaidSubgroup).

**Signature:**

```lua
SetRaidSubgroup(index, subgroup)
```

**Arguments:**

- `index` - Index of the raid member (between 1 and [`GetNumRaidMembers()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumRaidMembers)); matches the numeric part of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID), e.g. 21 for `raid21` (`number`)
- `subgroup` - Index of a raid subgroup (between 1 and `MAX_RAID_GROUPS`) (`number`)

---

## SetRaidTarget

Puts a raid target marker on a unit

**Signature:**

```lua
SetRaidTarget("unit", index) or SetRaidTarget("name", index)
```

**Arguments:**

- `unit` - A unit to mark (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - Name of a unit to mark (`string`)
- `index` - Index of a target marker (`number`)
  - `0` - Clear any raid target markers
  - `1` - Star
  - `2` - Circle
  - `3` - Diamond
  - `4` - Triangle
  - `5` - Moon
  - `6` - Square
  - `7` - Cross
  - `8` - Skull

---

## SwapRaidSubgroup

Swaps two raid members between subgroups in the raid. Only has effect if the player is the raid leader or a raid assistant. To move a member into a non-full subgroup without switching places with another member, see [`SetRaidSubgroup()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetRaidSubgroup).

**Signature:**

```lua
SwapRaidSubgroup(index1, index2)
```

**Arguments:**

- `index1` - Index of the first raid member (between 1 and [`GetNumRaidMembers()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumRaidMembers)); matches the numeric part of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID), e.g. 21 for `raid21` (`number`)
- `index2` - Index of the other raid member (`number`)

---

## UninviteUnit

Removes a character from the player's party or raid. Only works if the player is the party leader, raid leader, or raid assistant.

Also used by the Looking For Group tool to vote kick players. This is what the "reason" argument is used for.

**Signature:**

```lua
UninviteUnit("name", "reason")
```

**Arguments:**

- `name` - Name of a character to uninvite (`string`)
- `reason` - Reason for the action, optional and may be left as a nil value (`string`)

---

## UnitInRaid

Returns whether a unit is in the player's raid

**Signature:**

```lua
inRaid = UnitInRaid("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `inRaid` - Index of the unit in the raid (matches the numeric part of the unit's `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) minus 1; e.g. returns 0 for `raid1`, 12 for `raid13`, etc) (`number`)

---

## UnitIsPartyLeader

Returns whether a unit is the leader of the player's party

**Signature:**

```lua
leader = UnitIsPartyLeader("unit") or UnitIsPartyLeader("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `leader` - 1 if the unit is the party leader; otherwise nil (`1nil`)

---

## UnitIsRaidOfficer

Returns whether a unit is a raid assistant in the player's raid

**Signature:**

```lua
leader = UnitIsRaidOfficer("unit") or UnitIsRaidOfficer("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `leader` - 1 if the unit is a raid assistant; otherwise nil (`1nil`)

---

## UnitPlayerOrPetInRaid

Returns whether a unit is in the player's raid or belongs to a raid member

**Signature:**

```lua
inParty = UnitPlayerOrPetInRaid("unit") or UnitPlayerOrPetInRaid("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `inParty` - 1 if the unit is in the player's raid or is a pet belonging to a raid member; otherwise nil (`1nil`)

---

## UnitTargetsVehicleInRaidUI

Returns whether attempts to target a unit should target its vehicle. The unit can still be targeted: this flag is used to provide a convenience in the default UI for certain cases (such as the Malygos encounter) such that clicking a unit in the raid UI targets its vehicle (e.g. so players can use their drakes to heal other players' drakes).

**Signature:**

```lua
targetVehicle = UnitTargetsVehicleInRaidUI("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `targetVehicle` - True if clicking the unit's raid UI representation should target the unit's vehicle instead of the unit itself; otherwise false (`boolean`)

---

← [WoW API Docs](../index.md)
