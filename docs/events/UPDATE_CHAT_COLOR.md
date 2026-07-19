# UPDATE_CHAT_COLOR

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UPDATE_CHAT_COLOR)

---

Fires when the color settings for chat message types are updated

**Signature:**

```lua
("type", red, green, blue)
```

**Arguments:**

- `type` - Chat message type for which the color setting has changed (`string`)
- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
