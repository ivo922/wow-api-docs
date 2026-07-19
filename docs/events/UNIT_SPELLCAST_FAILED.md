# UNIT_SPELLCAST_FAILED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_FAILED)

---

Fires when a unit's spell cast fails

**Signature:**

```lua
("unitID", "spell", "rank", unknownid, spellid)
```

**Arguments:**

- `unitID` - The unit that's casting. (`string`)
- `spell` - The name of the spell that's being casted. (`string`)
- `rank` - The rank of the spell that's being casted. (`string`)
- `unknownid` - A numeric identifier, likely some client-generated sequence id, probably related to `UNIT_SPELLCAST_SENT`. (`number`)
- `spellid` - The numeric spell id of the spell that was attempted (`number`, [blizzid](../types/blizzid.md))
