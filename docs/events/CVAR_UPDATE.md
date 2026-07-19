# CVAR_UPDATE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CVAR_UPDATE)

---

Fires when the value of a configuration variable is updated. Fires regardless of whether the variable's value has changed.

Except that it doesn't fire for all CVars that can be set in preferences, and it doesn't fire when someone changes a CVar outside of preferences unless they specifically give it an argument to fire with. You likely want to hook SetCVar instead.

**Signature:**

```lua
("glStr", "value")
```

**Arguments:**

- `glStr` - Global string related to the given CVAR (like "ENABLE*BGSOUND" for "Sound*EnableSoundWhenGameIsInBG" CVAR). (`string`)
- `value` - The updated value assigned to the CVAR. Note: For boolean values this is a string of 0 or 1. (`string`)
