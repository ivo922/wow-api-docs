# MINIMAP_PING

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/MINIMAP_PING)

---

Fires when the player or a group member "pings" a point on the minimap to share its location with the group

**Signature:**

```lua
("unit", x, y)
```

**Arguments:**

- `unit` - The unit of the player that was the source of said event (`string`)
- `x` - The x coordinate. 0 is the center point going out to .5 to the right and -.5 to the left. (`number`)
- `y` - The y coordinate. 0 is the center point going out to .5 to the top and -.5 to the bottom. (`number`)
