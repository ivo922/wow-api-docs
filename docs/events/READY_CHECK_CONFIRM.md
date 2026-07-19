# READY_CHECK_CONFIRM

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/READY_CHECK_CONFIRM)

---

Fires when a unit responds to a ready check

**Signature:**

```lua
(id, response)
```

**Arguments:**

- `id` - The unitid without raid or party prefix (`number`)
- `response` - `true` if the unit is ready, otherwise `false`. (`boolean`)
