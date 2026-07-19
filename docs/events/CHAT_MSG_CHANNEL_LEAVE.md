# CHAT_MSG_CHANNEL_LEAVE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHAT_MSG_CHANNEL_LEAVE)

---

Fires when another character leaves a world or custom chat channel monitored by the player. Used for numbered chat channels (e.g. Trade, General, and player-created channels). Only used for other characters leaving the channel -- when the player leaves the channel, [`CHAT_MSG_CHANNEL_NOTICE`](CHAT_MSG_CHANNEL_NOTICE.md) fires.

**Signature:**

```lua
("unkown", "sender", "unknown", "channelString", "unknown", "unknown", unknown, channelNumber, "channelName", unknown, unknown)
```

**Arguments:**

- `unkown` - empty string (`string`)
- `sender` - The sender's username. (`string`)
- `unknown` - empty string (`string`)
- `channelString` - The full name of the channel, including number. (`string`)
- `unknown` - empty string (`string`)
- `unknown` - empty string (`string`)
- `unknown` - 0 (`number`)
- `channelNumber` - The numeric ID of the channel. (`number`)
- `channelName` - The full name of the channel, does not include the number. (`string`)
- `unknown` - 0 (`number`)
- `unknown` - 852 (`number`)
