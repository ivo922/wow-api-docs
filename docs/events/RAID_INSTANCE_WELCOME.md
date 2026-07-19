# RAID_INSTANCE_WELCOME

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/RAID_INSTANCE_WELCOME)

---

Fires when the player enters an instance that has a reset timer

**Signature:**

```lua
("name", ttl)
```

**Arguments:**

- `name` - The name of the instance you're entering (`string`)
- `ttl` - The time till the instance resets, in seconds. (`number`)
