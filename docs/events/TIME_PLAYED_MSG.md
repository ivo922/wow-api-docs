# TIME_PLAYED_MSG

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TIME_PLAYED_MSG)

---

Fires when information about the player's total time played becomes available. Such information is normally requested via the `/played` command.

**Signature:**

```lua
(total, level)
```

**Arguments:**

- `total` - The ammount of time played total, in seconds. (`number`)
- `level` - The ammount of time played this level, in seconds. (`number`)
