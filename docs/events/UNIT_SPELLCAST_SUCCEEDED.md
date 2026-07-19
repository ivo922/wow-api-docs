# UNIT_SPELLCAST_SUCCEEDED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_SUCCEEDED)

---

Fires when a unit's spell cast succeeds

**Signature:**

```lua
("unitID", "spell", "rank", ?, spellID)
```

**Arguments:**

- `unitID` - The unit that's casting. (`string`)
- `spell` - The name of the spell that's being casted. (`string`)
- `rank` - The rank of the spell that's being casted. (`string`)
- `?` - unknown. (`number`)
- `spellID` - The id of the spell that's being casted. (`number`)
