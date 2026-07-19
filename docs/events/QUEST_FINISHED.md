# QUEST_FINISHED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_FINISHED)

---

Fires when the player ends interaction with a questgiver or ends a stage of the questgiver dialog. A typical dialogue with a questgiver is presented in four stages (though some stages may be skipped for some quests):

- A greeting, in which the questgiver presents the player a choice of one or more available or active quests (presented via the [`QUEST_GREETING`](QUEST_GREETING.md) or [`GOSSIP_SHOW`](GOSSIP_SHOW.md) events).
- After choosing an available quest, the questgiver describes its details and rewards, offering the player a chance to accept or decline the quest (presented via the [`QUEST_DETAIL`](QUEST_DETAIL.md) event).
- Upon returning (and selecting the active quest from the greeting) after accepting the quest, the questgiver verifies the player's progress on the quest and allows the player to turn it in if complete (presented via the [`QUEST_PROGRESS`](QUEST_PROGRESS.md) event).
- With the completed quest turned in, the questgiver presents additional text and offers rewards for the player to choose -- or merely accept, in the case of a single reward or no reward save for XP or money (presented via the [`QUEST_COMPLETE`](QUEST_COMPLETE.md) event).

This event fires when the player completes any of the above stages of dialog, before the event presenting the next stage fires, or when the player declines or aborts interaction with the questgiver.

**Signature:**

```lua
()
```
