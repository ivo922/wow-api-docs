# CHAT_MSG_BATTLEGROUND_LEADER

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_BATTLEGROUND_LEADER)

---

Fires when a message is received in the battleground chat channel from the battleground group leader

**Signature:**

```lua
("message", "author", "language")
```

**Arguments:**

- `message` - The message received. (`string`)
- `author` - The sender's username. (`string`)
- `language` - What language the message is in. (`string`)
