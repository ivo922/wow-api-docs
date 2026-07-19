# SPELL_UPDATE_COOLDOWN

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/SPELL_UPDATE_COOLDOWN)

---

Fires when the cooldown on one of the player's spells begins or ends. Only fires while something is being cast (i.e. beginning of cast, end of cast.)

While the event does react to every cooldown of a spell finishing, it doesn't fire until the next spellcast. If you're waiting for this event to see if a cooldown has finished, try [`SPELL_UPDATE_USABLE`](SPELL_UPDATE_USABLE.md)

**Signature:**

```lua
()
```
