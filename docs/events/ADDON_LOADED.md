# ADDON_LOADED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ADDON_LOADED)

---

Fires when an addon and its saved variables are loaded. Fires once for each addon (i.e. an addon loaded early in sequence will see `ADDON_LOADED` events for all addons loaded later).

**Signature:**

```lua
("name")
```

**Arguments:**

- `name` - The name of the addon that has been loaded (`string`)
