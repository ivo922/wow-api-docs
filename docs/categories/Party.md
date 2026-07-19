# Party functions

← [WoW API Docs](../index.md)

**23** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#party)

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
- `unit` - A unit in the player's party or raid (`string`, [unitID](../types/unitID.md))
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

## DoReadyCheck

Initiates a ready check. Only has effect if the player is the party/raid leader or a raid assistant.

**Signature:**

```lua
DoReadyCheck()
```

---

## GetNumPartyMembers

Returns the number of additional members in the player's party

**Signature:**

```lua
numPartyMembers = GetNumPartyMembers()
```

**Returns:**

- `numPartyMembers` - Number of additional members in the player's party (between 1 and `MAX_PARTY_MEMBERS`, or 0 if the player is not in a party) (`number`)

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
- `unit` - A unit in the player's party or raid (`string`, [unitID](../types/unitID.md))
- `name` - Name of a unit in the player's party or raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

**Returns:**

- `isAssigned` - 1 if the unit is assigned the specified role; otherwise nil (`1nil`)

---

## GetPartyLeaderIndex

Returns the index of the current party leader. Returns 0 if the player is the party leader or if the player is not in a party.

**Signature:**

```lua
index = GetPartyLeaderIndex()
```

**Returns:**

- `index` - Numeric portion of the `party` [`unitID`](../types/unitID.md) for the party leader (e.g. 3 = `party3`) (`number`)

---

## GetPartyMember

Returns whether a party member exists at a given index

**Signature:**

```lua
hasMember = GetPartyMember(index)
```

**Arguments:**

- `index` - Index of a party member (between 1 and `MAX_PARTY_MEMBERS`), or the numeric portion of a `party` [`unitID`](../types/unitID.md) (e.g. 3 = `party3`) (`number`)

**Returns:**

- `hasMember` - 1 if the given `index` corresponds to a member in the player's party; otherwise nil (`1nil`)

---

## GetReadyCheckStatus

Returns a unit's status during a ready check. Returns nil for all units unless the player is the party/raid leader or a raid assistant.

**Signature:**

```lua
status = GetReadyCheckStatus("unit")
```

**Arguments:**

- `unit` - A unit in the player's party or raid (`string`, [unitID](../types/unitID.md))

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

## GetRealNumPartyMembers

Returns the number of members in the player's non-battleground party. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
numMembers = GetRealNumPartyMembers()
```

**Returns:**

- `numMembers` - Number of members in the player's non-battleground party (`number`)

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

## IsPartyLeader

Returns whether or not a unit is the current party leader

**Signature:**

```lua
isLeader = IsPartyLeader(unit)
```

**Arguments:**

- `unit` - The unit to query (`unitid`)

**Returns:**

- `isLeader` - 1 if the unit is the party leader, otherwise nil (`1nil`)

---

## IsRealPartyLeader

Returns whether the player is the leader of a non-battleground party. When the player is in a party/raid and joins a battleground or arena, the normal party/raid functions refer to the battleground's party/raid, but the game still keeps track of the player's place in a non-battleground party/raid.

**Signature:**

```lua
isLeader = IsRealPartyLeader()
```

**Returns:**

- `isLeader` - 1 if the player is the leader of a non-battleground party; otherwise nil (`1nil`)

---

## LeaveParty

Exits the current party or raid. If there are only two characters in the party or raid, causes the party or raid to be disbanded.

**Signature:**

```lua
LeaveParty()
```

---

## PromoteToLeader

Promotes a player to party/raid leader

**Signature:**

```lua
PromoteToLeader("unit") or PromoteToLeader("name" [, exactMatch])
```

**Arguments:**

- `unit` - A unit in the party or raid (`string`, [unitID](../types/unitID.md))
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
- `unit` - A unit in the player's party or raid (`string`, [unitID](../types/unitID.md))
- `name` - Name of a unit in the player's party or raid (`string`)
- `exactMatch` - True to check only units whose name exactly matches the `name` given; false to allow partial matches (`boolean`)

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

## UnitInParty

Returns whether a unit is a player unit in the player's party. Always returns 1 for the `player` unit. Returns nil for the player's or party members' pets.

**Signature:**

```lua
inParty = UnitInParty("unit") or UnitInParty("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `inParty` - 1 if the unit is a player unit in the player's party; otherwise nil. (`1nil`)

---

## UnitIsPartyLeader

Returns whether a unit is the leader of the player's party

**Signature:**

```lua
leader = UnitIsPartyLeader("unit") or UnitIsPartyLeader("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `leader` - 1 if the unit is the party leader; otherwise nil (`1nil`)

---

## UnitPlayerOrPetInParty

Returns whether a unit is in the player's party or belongs to a party member. Returns nil for the player and the player's pet.

**Signature:**

```lua
inParty = UnitPlayerOrPetInParty("unit") or UnitPlayerOrPetInParty("name")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](../types/unitID.md))
- `name` - The name of a unit to query (`string`)

**Returns:**

- `inParty` - 1 if the unit is in the player's party or is a pet belonging to a party member; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
