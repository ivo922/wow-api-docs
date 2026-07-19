# ITEM_TEXT_TRANSLATION

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/ITEM_TEXT_TRANSLATION)

---

Fires when a "translation" progress bar should be displayed while the player interacts with a readable item or world object. Such a UI element indicates the player character's progress in translating the text to a readable in-game language; this feature is generally not used in the current version of WoW.

Readable items include [books](http://www.wowhead.com/?item=2756), [scrolls](http://www.wowhead.com/?item=23798), and [saved copies of mail messages](../categories/Mail.md#takeinboxtextitem); readable world objects include [plaques](http://www.wowhead.com/?object=25331), [gravestones](http://www.wowhead.com/?object=179909) and [books on tables](http://www.wowhead.com/?object=192706).

**Signature:**

```lua
(maxvalue)
```

**Arguments:**

- `maxvalue` - The max value (`number`)
