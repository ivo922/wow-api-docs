# UNIT_SPELLCAST_SENT

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_SENT)

---

Fires when a request to cast a spell (on behalf of the player or a unit controlled by the player) is sent to the server

**Signature:**

```lua
("unitID", "spell", "rank", "target", lineID)
```

**Arguments:**

- `unitID` - The unit that's casting. (`string`)
- `spell` - The name of the spell that's being casted. (`string`)
- `rank` - The rank of the spell that's being casted. (`string`)
- `target` - The name of the target of your spell. (`string`)
- `lineID` - Spell lineID counter. The Nth spell that UNIT_SPELLCAST events have fired for. Unique to each spell cast - UNIT_SPELLCAST_START and UNIT_SPELLCAST_SUCCESS events referring to the same cast will have the same lineID. Resets to 0 when the count reaches 255, but this number may just always be 0 for some spells. (`number`)
