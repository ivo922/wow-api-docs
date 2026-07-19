# QUEST_LOG_UPDATE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_LOG_UPDATE)

---

Fires when the game client receives updates relating to the player's quest log (this event is not just related to the quests inside it). There are a LOT of various things that cause the server to send quest log information to the player's client, such as: Logging into the game world, zoning between servers (anytime you see a loading screen), accepting quests, deleting/abandoning quests, completing quests, quest progress updates (achieving whole or partial objective updates for a quest), when dailies reset (the "You can only complete 25 more daily quests today" event), and whenever something regarding the DISPLAY of the quest log VISUALLY changes (such as when you collapse or expand headers in the quest log; with headers being the lines such as "Terokkar Forest", that separate the quests into groups).

This event (`QUEST_LOG_UPDATE`) should therefore only be used if you care about the QUEST LOG itself more than the quests; ie if you implement a custom quest log, then you'd use this event to update the display when things like dailies reset or headers change.

However, if you are ONLY interested in tracking QUEST-related information (accepting quests, abandoning quests, achieving quest progress, and completing quests), there's a better event: [`UNIT_QUEST_LOG_CHANGED`](UNIT_QUEST_LOG_CHANGED.md). See its page for details.

**Signature:**

```lua
()
```
