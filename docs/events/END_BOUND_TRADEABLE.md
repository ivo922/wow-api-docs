# END_BOUND_TRADEABLE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/END_BOUND_TRADEABLE)

---

Fires when the player attempts an action which will make a looted Bind on Pickup item no longer tradeable. A Bind on Pickup item looted by the player can still be traded to other players (though only those who were eligible to loot it originally) for several minutes after looting, but certain actions can cancel this period early.

**Signature:**

```lua
()
```
