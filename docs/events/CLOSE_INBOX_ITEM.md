# CLOSE_INBOX_ITEM

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CLOSE_INBOX_ITEM)

---

Fires when the mail message being viewed is no longer available. Occurs when the player takes all items attached to the currently viewed message, causing it to be deleted.

**Signature:**

```lua
(id)
```

**Arguments:**

- `id` - The id of the mail slot you took the item from (`number`)
