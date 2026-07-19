# QUEST_WATCH_UPDATE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_WATCH_UPDATE)

---

Fires when the player's status regarding a quest's objectives changes, for instance picking up a required object or killing a mob for that quest. All forms of (quest objective) progress changes will trigger this event.

**Signature:**

```lua
(questIndex)
```

**Arguments:**

- `questIndex` - Index of the affected quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](../categories/Quest.md#getnumquestlogentries)) (`number`)
