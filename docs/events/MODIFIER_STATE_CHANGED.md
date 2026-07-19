# MODIFIER_STATE_CHANGED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MODIFIER_STATE_CHANGED)

---

Fires when a modifier key is pressed or released.

**Signature:**

```lua
("key", state)
```

**Arguments:**

- `key` - The name of the key that you pressed. Possible values are LSHIFT, RSHIFT, LCTRL, RCTRL, LALT, and RALT. (`string`)
- `state` - The state the key has entered. 1 means that the the key has been pressed. 0 means that the key has been released. (`number`)
