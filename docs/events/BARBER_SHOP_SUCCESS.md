# BARBER_SHOP_SUCCESS

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/BARBER_SHOP_SUCCESS)

---

Fires immediately when changes to the player's appearance have been purchased at a barber shop. Both this event and [`BARBER_SHOP_APPEARANCE_APPLIED`](BARBER_SHOP_APPEARANCE_APPLIED.md) fire when purchasing an appearance change; this event fires first (causing the default UI to play a sound effect), and the other fires afterward to update the state of the barber shop controls and cost indicator.

**Signature:**

```lua
()
```
