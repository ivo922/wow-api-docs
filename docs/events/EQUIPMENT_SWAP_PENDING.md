# EQUIPMENT_SWAP_PENDING

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/EQUIPMENT_SWAP_PENDING)

---

Fires when the player begins to switch equipment sets. Many other events fire as the equipment swap takes place (each piece of equipment being equipped or placed into the character's bags, the character's combat attributes changing due to the new equipment, etc). An addon may not need to monitor each event that happens as part of this process, so it can unregister those events when `EQUIPMENT_SWAP_PENDING` fires and re-register for them when [`EQUIPMENT_SWAP_FINISHED`](EQUIPMENT_SWAP_FINISHED.md) fires.

**Signature:**

```lua
()
```
