# CHAT_MSG_SYSTEM

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_SYSTEM)

---

Fires when a system message is received. System messages are a catch-all category for messages received in via the chat system. Examples:

- The server message which appears upon login (e.g. "Welcome to Patch 3.4! If you encounter interface problems, please disable your addons and delete your WTF folder.")
- The feedback message which appears when the player enters AFK or DND status
- Results from a `/who` query, if the query has three or fewer results
- Notification that a friend or guild member has logged in or gone offline

Many standard system message patterns can be found as localized format strings in `FrameXML\GlobalStrings.lua` (after using the AddOn Kit to extract the default interface files). When this event is received, the message has already been localized and formatted, but using the format string may be useful for parsing variables from the message.

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
