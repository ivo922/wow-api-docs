# Type: unitID

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

Used throughout the API to identify units of interest. Possible values:

- `player` - The player him/herself
- `pet` - The player's pet
- `vehicle` - The vehicle currently controlled by the player
- `target` - The player's current target
- `focus` - The player's focused unit (as can be set by typing `/focus name`)
- `mouseover` - The unit currently under the mouse cursor (applies to both unit frames and units in the 3D world)
- `npc` - The unit the player is currently interacting with (via the Merchant, Trainer, Bank, or similar UI); not necessarily an NPC (e.g. also used in the Trade UI)
- `party1` to `party4` - Another member of the player's party. Indices match the order party member frames are displayed in the default UI (`party1` is at the top, `party4` at the bottom), but not consistent among party members (i.e. if Thrall and Cairne are in the same party, the player Thrall sees as `party2` may not be the same player Cairne sees as `party2`).
- `partypet1` to `partypet4` - A pet belonging to another member of the player's party
- `raid1` to `raid40` - A member of the player's raid group. Unlike with the `party` tokens, one of the `raid` unit IDs will belong to the player. Indices have no relation to the arrangement of units in the default UI.
- `raidpet1` to `raidpet40` - A pet belonging to a member of the player's raid group
- `arena1` to `arena5` - A member of the opposing team in an Arena match

A `unitID` can also be formed by appending `"target"` to an existing `unitID`, referring to that unit's target. This can be done repeatedly. For example, consider a raid situation where the token `raid13` refers to a priest: `raid13target` might be a rogue the priest is healing, `raid13targettarget` might be the boss monster the rogue is attacking, and `raid13targettargettarget` might be the warrior tanking the boss.

You can also append `"pet"` to a `unitID` to refer to that unit's pet, although it should only be appended once because pets cannot have pets. The unit `pet` is a shorter (and more efficient) way to write `playerpet`, but both refer to the same unit. `raidpet1` is also the same as `raid1pet`. A very long `unitID` such as `targettargetpettarget` is valid, and will refer to the player's target if the player's target and the player's pet are targeting the player.

Many (but not all) API functions that accept a `unitID` also accept the name of a unit (assuming that unit is in the player's party or raid). For example, [`UnitHealth("Cladhaire")`](../categories/Unit.md#unithealth) will return the same value as `UnitHealth("party1")` if the unit `party1` is the player named Cladhaire. In such situations, a unit's target can still be accessed by appending `"-target"`; e.g. `UnitHealth("Cladhaire-target")`.

---

← [API Types](../API Types.md)
