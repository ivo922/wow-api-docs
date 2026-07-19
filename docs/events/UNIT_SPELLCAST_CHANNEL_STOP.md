# UNIT_SPELLCAST_CHANNEL_STOP

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_CHANNEL_STOP)

---

Fires when a unit stops or cancels a channeled spell

**Signature:**

```lua
("unitID", "spell", "rank")
```

**Arguments:**

- `unitID` - The unit that was casting. (`string`)
- `spell` - The name of the spell that wass being casted. (`string`)
- `rank` - The rank of the spell that wass being casted. (`string`)
