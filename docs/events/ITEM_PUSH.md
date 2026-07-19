# ITEM_PUSH

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ITEM_PUSH)

---

Fires when the player receives an item. This event fires in addition to others which may indicate the item's origin (e.g. [`QUEST_ACCEPTED`](QUEST_ACCEPTED.md) or [`CHAT_MSG_LOOT`](CHAT_MSG_LOOT.md)); in the default UI, this event triggers an "item falling into bag" animation displayed above the bag icons.

**Signature:**

```lua
(bagID, "icon")
```

**Arguments:**

- `bagID` - The id of the bag that the item is going into. (`number`)
- `icon` - The icon file for the item being received. (`string`)
