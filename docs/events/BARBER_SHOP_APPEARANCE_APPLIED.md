# BARBER_SHOP_APPEARANCE_APPLIED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/BARBER_SHOP_APPEARANCE_APPLIED)

---

Fires after changes to the player's appearance have been purchased at a barber shop. Both [`BARBER_SHOP_SUCCESS`](BARBER_SHOP_SUCCESS.md) and this event fire when purchasing an appearance change; the former fires first (causing the default UI to play a sound effect), and this event fires afterward to update the state of the barber shop controls and cost indicator.

**Signature:**

```lua
()
```
