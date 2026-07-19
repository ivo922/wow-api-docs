# CHAT_MSG_BN_WHISPER

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_BN_WHISPER)

---

Fires when you receive a whisper though Battle.Net

**Signature:**

```lua
("message", "sender", "unknown", "unknown", "unknown", "unknown", unknown, unknown, "unknown", unknown, counter, "unknown", presenceID, unknown)
```

**Arguments:**

- `message` - The message thats received (`string`)
- `sender` - The sender's RealID name. (i.e 'John Doe') or sometimes your own wow characters name. (looks like it will use the wow-character name when you are chatting, but will contain realid when other clients send messages) (`string`)
- `unknown` - unknown (`string`)
- `unknown` - unknown (`string`)
- `unknown` - unknown (`string`)
- `unknown` - unknown (`string`)
- `unknown` - unknown (`number`)
- `unknown` - unknown (`number`)
- `unknown` - unknown (`string`)
- `unknown` - This variable has an unkown purpose although it always seems to be 0. (`number`)
- `counter` - This variable appears to be sequential number that the client recieves. (`number`)
- `unknown` - unknown (`string`)
- `presenceID` - presenceID of the sender (`number`, [presenceID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#presenceID))
- `unknown` - this seems to always be false (`boolean`)
