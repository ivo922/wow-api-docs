# QUEST_ACCEPTED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_ACCEPTED)

---

Fires when a new quest is added to the player's quest log (which is what happens after a player accepts a quest).

**Signature:**

```lua
(questIndex)
```

**Arguments:**

- `questIndex` - Index where the accepted quest was placed in the quest log (between 1 and [`GetNumQuestLogEntries()`](../categories/Quest.md#getnumquestlogentries)) (`number`)
