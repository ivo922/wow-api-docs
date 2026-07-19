# UNIT_COMBAT

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_COMBAT)

---

Fires when a unit takes or recovers from damage due to a combat effect

**Signature:**

```lua
("unitID", "action", "descriptor", damage, damageType)
```

**Arguments:**

- `unitID` - The unit that was affected. (`string`)
- `action` - The action type that happened, i.e. WOUND, DODGE, HEAL (`string`)
- `descriptor` - A descriptor that describes the action, i.e. CRITICAL, CRUSHING (`string`)
- `damage` - The ammount of damage or healing received (`number`)
- `damageType` - The type of damage dealt. Is 0(physical) for healing. (`number`)
