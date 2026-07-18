# Type: GUID (Globally Unique IDentifier)

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

All entities in World of Warcraft are identified by a unique 64-bit number; generally presented as a string containing a hexadecimal representation of the number (e.g. `"0xF530007EAC083004"`). (Note that Lua in WoW does not support 64-bit integers, so this value cannot be converted with `tonumber`.)

The type of unit represented by a GUID can be determined by using `bit.band()` to mask the first three digits with `0x00F`:
- `0x000` - A player
- `0x003` - An NPC
- `0x004` - A player's pet (i.e. hunter/warlock pets and similar; non-combat pets count as NPCs) 
- `0x005` - A vehicle

Further content of the GUID varies by unit type:

**Players** - The remaining thirteen digits are unique to a player character at least within that character's battlegroup (that is, they remain unique and constant even in cross-server battlegrounds). This number is also semi-permanent -- it persists from character creation until deletion, renaming, or server transfer.

**NPCs** - Remaining digits can be broken down as follows:

- *Digits 4-6* - Unused.
- *Digits 7-10* - NPC creature ID: identifies the specific named NPC (e.g. Hogger, Loque'nahak) or type of NPC (e.g. Sunfury Nethermancer, Shattertusk Mammoth). Converting to decimal results in the ID found on database sites such as wowhead.com; can also be used with `PlayerModel:SetCreature` to view the NPC's model.
- *Digits 11-16* - Spawn counter: identifies the individual NPC (i.e. differentiates between the Gamon you recently killed and the Gamon that respawned a few minutes later, or between one Ymirheim Defender and another).

**Pets** - Hunter pets immediately after taming retain the GUID they had as a wild creature; after resummoning or logout/login, their GUID changes to the pet format. Remaining digits can be broken down as follows:

- *Digits 4-10* - A constant value unique to the individual pet: like a player's unique ID it is constant across multiple sessions.
- *Digits 11-16* - Spawn counter: changes when the pet is dismissed and re-summoned.

**Vehicles** - Same format and content as NPCs.

For example, the GUID `0xF530007EAC083004` can be deconstructed as follows:

- digits 1-3 are "F53"; `bit.band(0xF53, 0x00F) == 0x003`, so this is an NPC
- digits 7-10 are "7EAC"; `0x7EAC == 32428`, which we can look up to find the NPC is a [Underbelly Rat](https://web.archive.org/web/20110319023203/http://www.wowhead.com/?npc=32428).
- digits 11-16 have no intrinsic meaning, but distinguish this Underbelly Rat from all others spawned since the last server reset.

### Example Code: a function to decode GUIDs

```lua
function ParseGUID(guid)
   local first3 = tonumber("0x"..strsub(guid, 3,5))
   local unitType = bit.band(first3,0x00f)

   if (unitType == 0x000) then
      print("Player, ID #", strsub(guid,6))
   elseif (unitType == 0x003) then
      local creatureID = tonumber("0x"..strsub(guid,9,12))
      local spawnCounter = tonumber("0x"..strsub(guid,13)) 
      print("NPC, ID #",creatureID,"spawn #",spawnCounter)
   elseif (unitType == 0x004) then
      local petID = tonumber("0x"..strsub(guid,6,12))
      local spawnCounter = tonumber("0x"..strsub(guid,13)) 
      print("Pet, ID #",petID,"spawn #",spawnCounter)
   elseif (unitType == 0x005) then
      local creatureID = tonumber("0x"..strsub(guid,9,12))
      local spawnCounter = tonumber("0x"..strsub(guid,13)) 
      print("Vehicle, ID #",creatureID,"spawn #",spawnCounter)
   end
end
```

---

← [API Types](../API Types.md)
