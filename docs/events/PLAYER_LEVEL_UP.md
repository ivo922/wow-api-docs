# PLAYER_LEVEL_UP

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PLAYER_LEVEL_UP)

---

Fires when the player gains a character level. Ding!

**Signature:**

```lua
("level", hp, mp, talentPoints, strength, agility, stamina, intellect, spirit)
```

**Arguments:**

- `level` - The new player level. More accurate than UnitLevel at that time. (`string`)
- `hp` - Hit points gained. (`number`)
- `mp` - Mana points gained. (`number`)
- `talentPoints` - Talent points gained. (`number`)
- `strength` - Strength points gained. (`number`)
- `agility` - Agility points gained. (`number`)
- `stamina` - Stamina points gained. (`number`)
- `intellect` - Intellect points gained. (`number`)
- `spirit` - Spirit points gained. (`number`)
