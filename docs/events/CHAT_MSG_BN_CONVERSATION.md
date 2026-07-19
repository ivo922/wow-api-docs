# CHAT_MSG_BN_CONVERSATION

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_BN_CONVERSATION)

---

Fires when you type a message in chat or when you recive a message from another player using Battle.Net

**Signature:**

```lua
("message", "sender", "unknown", "channelString", "unknown", "unknown", unknown, channelNumber, "unknown", unknown, counter, "unknown", presenceID, unknown)
```

**Arguments:**

- `message` - The message thats received (`string`)
- `sender` - The sender's RealID name. (i.e 'John Doe') (`string`)
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
- `presenceID` - this is the presenceID of the sender. (`number`, [presenceID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#presenceID))
- `unknown` - this seems to always be false (`boolean`)
