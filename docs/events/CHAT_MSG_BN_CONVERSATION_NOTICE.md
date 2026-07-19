# CHAT_MSG_BN_CONVERSATION_NOTICE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_BN_CONVERSATION_NOTICE)

---

Fires when you join a conversation channel (private channel for you and your friends) on Battle.Net

**Signature:**

```lua
("message/status", "sender", "unknown", "channelString", "unknown", "unknown", unknown, channelNumber, "unknown", unknown, counter, "unknown", presenceID, unknown)
```

**Arguments:**

- `message/status` - The message thats received or a statuscode like YOU_ JOINED_ CONVERSATION, YOU_ LEFT_ CONVERSATION, MEMBER_ LEFT. (`string`)
- `sender` - The sender's RealID name. (i.e 'John Doe') or sometimes your own wow characters name. (looks like it will use the wow-character name when you are chatting, but will contain realid when other clients send messages) (`string`)
- `unknown` - unknown (`string`)
- `channelString` - The full name of the channel, including number. (`string`)
- `unknown` - unknown (`string`)
- `unknown` - unknown (`string`)
- `unknown` - unknown (`number`)
- `channelNumber` - The numeric ID of the channel. (The UI adds +10 to the number) (`number`)
- `unknown` - unknown (`string`)
- `unknown` - This variable has an unkown purpose although it always seems to be 0. (`number`)
- `counter` - This variable appears to be sequential number that the client recieves. (`number`)
- `unknown` - unknown (`string`)
- `presenceID` - presenceID of the channel owner (`number`, [presenceID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#presenceID))
- `unknown` - this seems to always be false (`boolean`)
