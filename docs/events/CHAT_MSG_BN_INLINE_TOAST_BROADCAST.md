# CHAT_MSG_BN_INLINE_TOAST_BROADCAST

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_BN_INLINE_TOAST_BROADCAST)

---

Fires whenever a user changes their broadcast message on Battle.Net

**Signature:**

```lua
("message", "sender", "unknown", "unknown", "unknown", "unknown", unknown, unknown, "unknown", unknown, counter, "unknown", presenceID, unknown)
```

**Arguments:**

- `message` - The broadcast message. (`string`)
- `sender` - The sender's RealID name. (i.e 'John Doe') (`string`)
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
- `presenceID` - presenceID of the player sending the boadcast message (`number`, [presenceID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#presenceID))
- `unknown` - this seems to always be false (`boolean`)
