# QUEST_COMPLETE

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE)

---

Fires when the player is looking at the "Complete" page for a quest, at a questgiver.. This is the portion of a questgiver dialog in which the player is offered to choose a reward (or accept the only reward) and sees the "Complete" button available. This event does NOT fire when they *actually* complete the quest, it fires when they SEE the "Complete" button and are offered the *ability* to complete the quest, and has nothing to do with whether they actually turned in the quest or not.

To avoid confusion: This event should not be used if you want to know *when* the player actually turns in a quest, that's not what this event does (see above).

This event happens after the portion in which the questgiver verifies the player's progress on the quest.

**Signature:**

```lua
()
```
