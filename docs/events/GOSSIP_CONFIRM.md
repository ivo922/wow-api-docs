# GOSSIP_CONFIRM

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GOSSIP_CONFIRM)

---

Fires when the player is requested to confirm a gossip choice. Used when a gossip interaction involves a warning, such as for spending a large amount of money (e.g. purchasing Dual Talent Specialization).

**Signature:**

```lua
(index, "message", cost)
```

**Arguments:**

- `index` - The numeric index of the gossip option you're confirming (`number`)
- `message` - The message to display for the confirmation (`string`)
- `cost` - The cost of the action you're confirming. Will be 0 if there is no cost. (`number`)
