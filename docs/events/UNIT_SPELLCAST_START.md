# UNIT_SPELLCAST_START

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_START)

---

Fires when a unit begins casting a spell

**Signature:**

```lua
("unitID", "spell", "rank", lineID, spellID)
```

**Arguments:**

- `unitID` - The unit that's casting. (`string`)
- `spell` - The name of the spell that's being casted. (`string`)
- `rank` - The rank of the spell that's being casted. (`string`)
- `lineID` - Spell lineID counter. The Nth spell that UNIT_SPELLCAST events have fired for. Unique to each spell cast - UNIT_SPELLCAST_START and UNIT_SPELLCAST_SUCCESS events referring to the same cast will have the same lineID. Resets to 0 when the count reaches 255, but this number may just always be 0 for some spells. (`number`)
- `spellID` - The id of the spell that's being casted. (`number`, [spellID](../types/spellID.md))
