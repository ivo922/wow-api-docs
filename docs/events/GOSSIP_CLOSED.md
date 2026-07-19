# GOSSIP_CLOSED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GOSSIP_CLOSED)

---

Fires when an NPC gossip interaction ends. Many NPCs provide a single gossip option leading into another type of interaction (e.g. a flight master offering a greeting) -- in this case, the gossip interaction still happens but is automatically skipped by the default UI, so this event still fires.

**Signature:**

```lua
()
```
