# CHAT_MSG_AFK

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_AFK)

---

Fires when an automatic AFK response is received. When the player attempts to whisper or invite a character whose status is AFK, an automatic response is returned containing either a custom message set by that character or the default message, "Away From Keyboard"

**Signature:**

```lua
("message", "sender", "language", "channelString", "target", "flags", unknown, channelNumber, "channelName", unknown, counter, "senderGUID")
```

**Arguments:**

- `message` - The response message (`string`)
- `sender` - The sender's username. (`string`)
- `language` - The language the message is in. (`string`)
- `channelString` - The full name of the channel, including number. (`string`)
- `target` - The username of the target of the action. Not used by all events. (`string`)
- `flags` - The various chat flags. Like, DND or AFK. (`string`)
- `unknown` - This variable has an unkown purpose, although it may be some sort of internal channel id. That however is not confirmed. (`number`)
- `channelNumber` - The numeric ID of the channel. (`number`)
- `channelName` - The full name of the channel, does not include the number. (`string`)
- `unknown` - This variable has an unkown purpose although it always seems to be 0. (`number`)
- `counter` - counter of chat events that the client recieves. (`number`)
- `senderGUID` - The sender's GUID (`string`)
