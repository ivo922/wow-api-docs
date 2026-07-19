# BAG_UPDATE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/BAG_UPDATE)

---

Fires when the contents of one of the player's containers change. Container contents may change due to obtaining an item, consuming an item, moving an item between or within bags, etc. Note that containers also include the keyring, bank and bank bags.

Fires many times (once for each slot in each container) during the login / UI load process. An addon which does extensive processing for this event should register it only after [`PLAYER_ENTERING_WORLD`](PLAYER_ENTERING_WORLD.md) has fired if they are not interested in processing each event individually during the load process.

**Signature:**

```lua
(bagID)
```

**Arguments:**

- `bagID` - The id of the bag that is receiving an update. (`number`, [containerID](../types/containerID.md))
