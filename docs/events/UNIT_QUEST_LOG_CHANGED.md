# UNIT_QUEST_LOG_CHANGED

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_QUEST_LOG_CHANGED)

---

Fires when a unit's quests change (accepted/objective progress/abandoned/completed). This event will trigger both for *your* status changes, and that of *others* (when in a party/raid), and signifies that something has changed regarding the unit's current quests. This event triggering means that one of the following has occured: Accepted a new quest, abandoned an existing quest, achieved progress on the objectives of a quest, or completed (turned in) a quest.

unitID will be "player" when the event relates to you. This event is VERY reliable for players, and is the preferred event when you ONLY care about changes relating to the player's quests and don't care about all the other triggerings that come with using the player-only [`QUEST_LOG_UPDATE`](QUEST_LOG_UPDATE.md) (that event should really only be used if you are writing a Quest Log replacement addon, as it triggers on many, many non-quest related things).

unitID will be partyX/raidX when the event relates to a party or raid member. However, this event is EXTREMELY unreliable for party and raid members, as it will ONLY trigger if you are at a very close range to them; and it will only trigger when they GAIN a quest (accepting) or LOSE a quest (abandon/turn in), meaning that you can't expect to use this event to monitor the quest status of other units, as you may be out of range when they accept or finish a quest (and then your client won't trigger this event and you won't know that they have a new quest/no longer has a certain quest). Also, even if they ARE in range it won't trigger for PROGRESS updates (such as finishing or achieving progress on certain objectives). It's best to just completely ignore that this event claims to be for other units, as its range limitation makes it useless for keeping an accurate look at other unit's quest state.

Note: If you are in a party or raid and YOUR status changes, this event will be triggered twice; once with a unitID of "player", and once with your *current* "partyX/raidX" unitID (be aware that your ID changes whenever the party/raid layout changes; one call you may be raid37, and another call you may be raid21, so never store the value and assume it to stay the same).

Warning Regarding Use: If your addon's operation relies on building an internal table of the user's quests, and you want that table available immediately at logon/UI reload, you MUST complement this event with [`QUEST_LOG_UPDATE`](QUEST_LOG_UPDATE.md) (which fires 2 times on logon and 1 time on UI reload), and build/update your quest table on BOTH `QUEST_LOG_UPDATE` and `UNIT_QUEST_LOG_CHANGED`. That's because the latter event only fires on *actual CHANGES* to your quests, and NOT on logon/UI reload. However, *as soon as* `QUEST_LOG_UPDATE` has fired you don't need it anymore, and you should use [UnregisterEvent](../widgets/Frame.md#frameunregisterevent) to remove it. This ensures that your addon starts out watching for QLU, uses it *once* to grab the "initial state", unregisters from it since we don't need it anymore, and then uses UQLC from then on to monitor CHANGES to the quests. (Also note that, no, you can't use [`PLAYER_LOGIN`](PLAYER_LOGIN.md) since the quest log data is received later than that.)

**Signature:**

```lua
("unitID")
```

**Arguments:**

- `unitID` - The unit that was affected. (`string`)
