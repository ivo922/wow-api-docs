# CHAT_MSG_MONEY

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_MONEY)

---

Fires when the player receives money as loot

**Signature:**

```lua
("message", "sender", "language", "channelString", "target", "flags", unknown, channelNumber, "channelName", unknown, counter)
```

**Arguments:**

- `message` - The message thats received (`string`)
- `sender` - The sender's username. (`string`)
- `language` - The language the message is in. (`string`)
- `channelString` - The full name of the channel, including number. (`string`)
- `target` - The username of the target of the action. Not used by all events. (`string`)
- `flags` - The various chat flags. Like, DND or AFK. (`string`)
- `unknown` - This variable has an unkown purpose, although it may be some sort of internal channel id. That however is not confirmed. (`number`)
- `channelNumber` - The numeric ID of the channel. (`number`)
- `channelName` - The full name of the channel, does not include the number. (`string`)
- `unknown` - This variable has an unkown purpose although it always seems to be 0. (`number`)
- `counter` - This variable appears to be a counter of chat events that the client recieves. (`number`)
