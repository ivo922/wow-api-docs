# EQUIPMENT_SWAP_FINISHED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/EQUIPMENT_SWAP_FINISHED)

---

Fires when the process of switching equipment sets is complete. Many other events fire as the equipment swap takes place (each piece of equipment being equipped or placed into the character's bags, the character's combat attributes changing due to the new equipment, etc). An addon may not need to monitor each event that happens as part of this process, so it can unregister those events when [`EQUIPMENT_SWAP_PENDING`](EQUIPMENT_SWAP_PENDING.md) fires and re-register for them when `EQUIPMENT_SWAP_FINISHED` fires.

**Signature:**

```lua
()
```
