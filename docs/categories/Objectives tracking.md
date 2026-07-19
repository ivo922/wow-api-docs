# Objectives tracking functions

← [WoW API Docs](../index.md)

**14** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#objective)

---

## AddQuestWatch

Adds a quest to the objectives tracker

**Signature:**

```lua
AddQuestWatch(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

---

## AddTrackedAchievement

Adds an achievement to the objectives tracker UI

**Signature:**

```lua
AddTrackedAchievement(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

---

## GetNumQuestWatches

Returns the number of quests included in the objectives tracker

**Signature:**

```lua
numWatches = GetNumQuestWatches()
```

**Returns:**

- `numWatches` - Number of quests from the quest log currently marked for watching (`number`)

---

## GetNumTrackedAchievements

Returns the number of achievements flagged for display in the objectives tracker UI

**Signature:**

```lua
count = GetNumTrackedAchievements()
```

**Returns:**

- `count` - Number of achievements flagged for tracking (`number`)

---

## GetQuestIndexForWatch

Returns the quest log index of a quest in the objectives tracker

**Signature:**

```lua
questIndex = GetQuestIndexForWatch(index)
```

**Arguments:**

- `index` - Index of a quest in the list of quests on the objectives tracker (between 1 and [`GetNumQuestWatches()`](Objectives tracking.md#getnumquestwatches)) (`number`)

**Returns:**

- `questIndex` - Index of the quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

---

## GetQuestLogSpecialItemCooldown

Returns cooldown information about an item associated with a current quest. Available for a number of quests which involve using an item (i.e. "Use the MacGuffin to summon and defeat the boss", "Use this saw to fell 12 trees", etc.)

**Signature:**

```lua
start, duration, enable = GetQuestLogSpecialItemCooldown(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest log entry with an associated usable item (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

**Returns:**

- `start` - The value of [`GetTime()`](Utility.md#gettime) at the moment the cooldown began, or 0 if the item is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the item is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the item is ready.) (`number`)

---

## GetQuestLogSpecialItemInfo

Returns information about a usable item associated with a current quest. Available for a number of quests which involve using an item (i.e. "Use the MacGuffin to summon and defeat the boss", "Use this saw to fell 12 trees", etc.)

**Signature:**

```lua
link, icon, charges = GetQuestLogSpecialItemInfo(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest log entry with an associated usable item (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](../types/hyperlink.md))
- `icon` - Path to an icon texture for the item (`string`)
- `charges` - Number of times the item can be used, or 0 if no limit (`number`)

---

## GetTrackedAchievements

Returns numeric IDs of the achievements flagged for display in the objectives tracker UI

**Signature:**

```lua
... = GetTrackedAchievements()
```

**Returns:**

- `...` - List of numeric IDs for the achievements being tracked (`list`)

---

## IsQuestLogSpecialItemInRange

Returns whether the player's target is in range for using an item associated with a current quest. Available for a number of quests which involve using an item (i.e. "Use the MacGuffin to summon and defeat the boss", "Use this saw to fell 12 trees", etc.)

**Signature:**

```lua
inRange = IsQuestLogSpecialItemInRange(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest log entry with an associated usable item (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

**Returns:**

- `inRange` - 1 if the player is close enough to the target to use the item; 0 if the target is out of range; nil if the quest item does not require a target (`number`)

---

## IsQuestWatched

Returns whether a quest from the quest log is listed in the objectives tracker

**Signature:**

```lua
isWatched = IsQuestWatched(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

**Returns:**

- `isWatched` - 1 if the quest is being watched; otherwise nil (`1nil`)

---

## IsTrackedAchievement

Returns whether an achievement is flagged for display in the objectives tracker UI

**Signature:**

```lua
isTracked = IsTrackedAchievement(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

**Returns:**

- `isTracked` - True if the achievement is flagged for tracking; otherwise false (`boolean`)

---

## RemoveQuestWatch

Removes a quest from the objectives tracker

**Signature:**

```lua
RemoveQuestWatch(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

---

## RemoveTrackedAchievement

Removes an achievement from the objectives tracker UI

**Signature:**

```lua
RemoveTrackedAchievement(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

---

## UseQuestLogSpecialItem `protected`

Uses the item associated with a current quest. Available for a number of quests which involve using an item (i.e. "Use the MacGuffin to summon and defeat the boss", "Use this saw to fell 12 trees", etc.)

**Signature:**

```lua
UseQuestLogSpecialItem(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest log entry with an associated usable item (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

---

← [WoW API Docs](../index.md)
