# Looking for group functions

← [WoW API Docs](../index.md)

**5** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#lfg)

---

## GetLFGMode

Provides information about the LFG status of the player.

**Signature:**

```lua
mode, submode = GetLFGMode()
```

**Returns:**

- `mode` - Current LFG status (`string`)
  - `abandonedInDungeon` - The party disbanded and player is still in the dungeon.
  - `lfgparty` - LFG dungeon is in-progress.
  - `nil` - Player is not in LFG
  - `proposal` - LFG party formed, notifying matched players dungeon is ready.
  - `queued` - Player is in LFG queue.
  - `rolecheck` - Querying groupmates to select their LFG roles before queuing.
- `submode` - Your LFG sub-status. Used to indicate priority for filling party slots. (`string`)
  - `empowered` - Indicates that your party has lost a player and is set to higher priority for finding a replacement
  - `nil` - Not looking for more party members
  - `unempowered` - Default priority in the LFG system.

---

## GetLFGRoles

Returns the group roles for which the player has signed up in the LFG system

**Signature:**

```lua
leader, tank, healer, damage = GetLFGRoles()
```

**Returns:**

- `leader` - True if the player is willing to lead a group; otherwise false (`boolean`)
- `tank` - True if the player is willing to take on the role of protecting allies by drawing enemy attacks; otherwise false (`boolean`)
- `healer` - True if the player is willing to take on the role of healing allies who take damage; otherwise false (`boolean`)
- `damage` - True if the player is willing to take on the role of damaging enemies; otherwise false (`boolean`)

---

## GetLFGTypes

Returns a list of LFG query types

**Signature:**

```lua
... = GetLFGTypes()
```

**Returns:**

- `...` - A list of strings, each the localized name of an LFG type (Dungeon, Raid, Zone, etc.) (`list`)

---

## SetLFGComment

Associates a brief text comment with the player's listing in the LFG system. In the default UI, other players see this comment when mousing over the player's name in the Looking for More listing.

**Signature:**

```lua
SetLFGComment("comment")
```

**Arguments:**

- `comment` - A comment to be associated with the player's listing in the LFG system (max 63 characters); or the empty string (`""`) to clear an existing comment (`string`)

---

## SetLFGRoles

Sets group roles for which to advertise the player in the LFG system. Passing `true` for a role the player's class does not support (e.g. healing on a warrior or tanking on a priest) has no effect: see example.

**Signature:**

```lua
SetLFGRoles(leader, tank, healer, damage)
```

**Arguments:**

- `leader` - True if the player is willing to lead a group; otherwise false (`boolean`)
- `tank` - True if the player is willing to take on the role of protecting allies by drawing enemy attacks; otherwise false (`boolean`)
- `healer` - True if the player is willing to take on the role of healing allies who take damage; otherwise false (`boolean`)
- `damage` - True if the player is willing to take on the role of damaging enemies; otherwise false (`boolean`)

---

← [WoW API Docs](../index.md)
