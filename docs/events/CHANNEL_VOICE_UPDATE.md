# CHANNEL_VOICE_UPDATE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CHANNEL_VOICE_UPDATE)

---

Fires when a member in a voice chat channel starts or stops speaking

**Signature:**

```lua
(id, enabled, active)
```

**Arguments:**

- `id` - The id of the speaker who has changed. (`number`)
- `enabled` - If voice chat is enabled. (`boolean`)
- `active` - If the player is speaking at this moment. (`boolean`)
