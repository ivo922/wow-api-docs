# QUEST_ACCEPT_CONFIRM

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_ACCEPT_CONFIRM)

---

Fires when certain kinds of quests (e.g. NPC escort quests) are started by another member of the player's group

**Signature:**

```lua
("name", "quest")
```

**Arguments:**

- `name` - The name of the user who started the quest. (`string`)
- `quest` - The name of the quest that was started. (`string`)
