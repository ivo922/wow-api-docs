# UNIT_SPELLCAST_FAILED_QUIET

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_SPELLCAST_FAILED_QUIET)

---

Fires when a unit's spell cast fails and no error message should be displayed. The default UI displays an error message when [`UNIT_SPELLCAST_FAILED`](UNIT_SPELLCAST_FAILED.md) fires; in some situations (e.g. if the player attempts to cast while mind controlled), this event is used instead, preventing an error message from being displayed while still notifying interested scripts of the failure.

**Signature:**

```lua
("unitID", "spell", "rank")
```

**Arguments:**

- `unitID` - The unit that's casting. (`string`)
- `spell` - The name of the spell that's being casted. (`string`)
- `rank` - The rank of the spell that's being casted. (`string`)
