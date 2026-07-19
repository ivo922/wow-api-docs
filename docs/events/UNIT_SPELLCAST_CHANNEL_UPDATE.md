# UNIT_SPELLCAST_CHANNEL_UPDATE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_CHANNEL_UPDATE)

---

Fires when a unit's channeled spell is interrupted or delayed

**Signature:**

```lua
("unitID", "spell", "rank", lineID, spellID)
```

**Arguments:**

- `unitID` - The unit that's casting. (`string`)
- `spell` - The name of the spell that's being casted. (`string`)
- `rank` - The rank of the spell that's being casted. (`string`)
- `lineID` - Spell lineID counter. This number is always 0 for channels. (`number`)
- `spellID` - The id of the spell that's being casted. (`number`, [spellID](../types/spellID.md))
