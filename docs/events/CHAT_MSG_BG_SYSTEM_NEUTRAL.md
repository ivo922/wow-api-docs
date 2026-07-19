# CHAT_MSG_BG_SYSTEM_NEUTRAL

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_BG_SYSTEM_NEUTRAL)

---

Fires when a general battleground, zone or world message is received. General battleground messages include those indicating that the match has ended or will begin soon. Also includes scripted events in certain zones (e.g. a warning to players entering Zul'Gurub) and occasional messages broadcast to all players in the realm, such as during major server events (e.g. "The wrath of Neptulon has subsided...").

**Signature:**

```lua
("message")
```

**Arguments:**

- `message` - The message received. (`string`)
