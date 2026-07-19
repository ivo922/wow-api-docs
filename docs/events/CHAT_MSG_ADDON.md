# CHAT_MSG_ADDON

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_ADDON)

---

Fires when an addon communication message is received (see [`SendAddonMessage()`](../categories/Addon-related.md#sendaddonmessage)). The local client receives any messages it sends; thus, this event fires for messages sent by the local client as well as those receives from others.

**Signature:**

```lua
("prefix", "message", "channel", "sender")
```

**Arguments:**

- `prefix` - The prefix declared from SendAddonMessage. (`string`)
- `message` - The message from SendAddonMessage. (`string`)
- `channel` - The message channel used for this message. Possible values include PARTY, RAID, GUILD, BATTLEGROUND, or WHISPER. (`string`)
- `sender` - The username of the sender. (`string`)
