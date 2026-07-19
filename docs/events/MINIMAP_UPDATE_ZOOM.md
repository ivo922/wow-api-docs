# MINIMAP_UPDATE_ZOOM

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MINIMAP_UPDATE_ZOOM)

---

Fires when the minimap zoom type changes. The client stores separate zoom level settings for both indoor and outdoor areas; this event fires so that the minimap's zoom level can be changed when the player moves between such areas. It does not fire when directly setting the minimap's zoom level.

**Signature:**

```lua
()
```
