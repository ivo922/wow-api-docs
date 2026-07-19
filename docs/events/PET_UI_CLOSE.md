# PET_UI_CLOSE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/PET_UI_CLOSE)

---

Fires when information about the player's pet is no longer available. Used in the default UI to determine whether the Pet section of the Character window should be shown; most often, this is determined in response to other events (e.g. [`UNIT_PET`](UNIT_PET.md)), but this event may fire in some cases where the player switches pets.

**Signature:**

```lua
()
```
