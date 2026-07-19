# ADDON_ACTION_FORBIDDEN

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ADDON_ACTION_FORBIDDEN)

---

Fires when a non-Blizzard addon attempts to use a protected API. In the default UI, this event triggers a dialog box providing the name of the addon and offering to disable it and reload the UI.

**Signature:**

```lua
("culprit")
```

**Arguments:**

- `culprit` - The name of the addon that called the forbidden function (`string`)
