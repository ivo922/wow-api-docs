# Quest functions

← [WoW API Docs](../index.md)

**100** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#quest)

---

## AbandonQuest `confirmation`

Confirms abandoning a quest. Use [`SetAbandonQuest()`](Quest.md#setabandonquest) first to select the quest to abandon.

**Signature:**

```lua
AbandonQuest()
```

---

## AcceptQuest

**Signature:**

```lua
AcceptQuest() This function needs to be reviewed
```

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

## CloseQuest

Ends interaction with a questgiver. Fires the [`QUEST_FINISHED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/QUEST_FINISHED) event, indicating that questgiver-related APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseQuest()
```

---

## CollapseQuestHeader

Collapses a header in the quest log

**Signature:**

```lua
CollapseQuestHeader(questIndex)
```

**Arguments:**

- `questIndex` - Index of a header in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)), or 0 to collapse all headers (`number`)

---

## CompleteQuest

Begins turning in a quest to a questgiver. Usable following the [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS) event in which it is determined whether the player can complete the quest.

Does not complete the quest turn-in process; after calling this function, the [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) event fires as the questgiver presents rewards (or sometimes only closure to the quest narrative); following that event, the [`GetQuestReward()`](Quest.md#getquestreward) function finishes the turn-in.

**Signature:**

```lua
CompleteQuest()
```

---

## ConfirmAcceptQuest

Accepts a quest started by another group member. Usable following the [`QUEST_ACCEPT_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_ACCEPT_CONFIRM) event which fires when another member of the player's party or raid starts certain quests (e.g. escort quests).

**Signature:**

```lua
ConfirmAcceptQuest()
```

---

## DeclineQuest

Declines a quest.. Usable following the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL) event in which the questgiver presents the player with the details of a quest and the option to accept or decline.

**Signature:**

```lua
DeclineQuest()
```

---

## ExpandQuestHeader

Expands a quest header in the quest log

**Signature:**

```lua
ExpandQuestHeader(questIndex)
```

**Arguments:**

- `questIndex` - Index of a header in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)), or 0 to expand all headers (`number`)

---

## GetAbandonQuestItems

Returns information about items that would be destroyed by abandoning a quest. Usable after calling [`SetAbandonQuest()`](Quest.md#setabandonquest) but before calling [`AbandonQuest()`](Quest.md#abandonquest-confirmation).

**Signature:**

```lua
items = GetAbandonQuestItems()
```

**Returns:**

- `items` - A string listing any items that would be destroyed (`string`)

---

## GetAbandonQuestName

Returns the name of the quest being abandoned. Usable after calling [`SetAbandonQuest()`](Quest.md#setabandonquest) but before calling [`AbandonQuest()`](Quest.md#abandonquest-confirmation).

**Signature:**

```lua
name = GetAbandonQuestName()
```

**Returns:**

- `name` - Name of the quest being abandoned (`string`)

---

## GetActiveLevel

Returns the level of a quest which can be turned in to the current Quest NPC. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event.

Note: Most quest NPCs present active quests using the [`GetGossipActiveQuests()`](NPC Gossip Dialog.md#getgossipactivequests) instead of this function.

**Signature:**

```lua
level = GetActiveLevel(index)
```

**Arguments:**

- `index` - Index of a quest which can be turned in to the current Quest NPC (between 1 and [`GetNumActiveQuests()`](Quest.md#getnumactivequests)) (`number`)

**Returns:**

- `level` - Recommended character level for attempting the quest (`number`)

---

## GetActiveTitle

Returns the name of a quest which can be turned in to the current Quest NPC. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event.

Note: Most quest NPCs present active quests using the [`GetGossipActiveQuests()`](NPC Gossip Dialog.md#getgossipactivequests) instead of this function.

**Signature:**

```lua
title = GetActiveTitle(index)
```

**Arguments:**

- `index` - Index of a quest which can be turned in to the current Quest NPC (between 1 and [`GetNumActiveQuests()`](Quest.md#getnumactivequests)) (`number`)

**Returns:**

- `title` - Title of the quest (`string`)

---

## GetAvailableLevel

Returns the level of a quest available from the current Quest NPC. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event.

Note: Most quest NPCs present available quests using the [`GetGossipAvailableQuests()`](NPC Gossip Dialog.md#getgossipavailablequests) instead of this function.

**Signature:**

```lua
level = GetAvailableLevel(index)
```

**Arguments:**

- `index` - Index of a quest available from the current Quest NPC (between 1 and [`GetNumAvailableQuests()`](Quest.md#getnumavailablequests)) (`number`)

**Returns:**

- `level` - Recommended character level for attempting the quest (`number`)

---

## GetAvailableTitle

Returns the name of a quest available from the current Quest NPC. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event.

Note: Most quest NPCs present available quests using the [`GetGossipAvailableQuests()`](NPC Gossip Dialog.md#getgossipavailablequests) instead of this function.

**Signature:**

```lua
title = GetAvailableTitle(index)
```

**Arguments:**

- `index` - Index of a quest available from the current Quest NPC (between 1 and [`GetNumAvailableQuests()`](Quest.md#getnumavailablequests)) (`number`)

**Returns:**

- `title` - Title of the quest (`string`)

---

## GetDailyQuestsCompleted

Returns the number of daily quests the player has completed today. The daily quest period resets at or around 3:00 AM server time on most realms.

**Signature:**

```lua
dailyQuestsComplete = GetDailyQuestsCompleted()
```

**Returns:**

- `dailyQuestsComplete` - Number of daily quests completed in the current period (`number`)

---

## GetGossipActiveQuests

Returns a list of quests which can be turned in to the current Gossip NPC. These quests are displayed with a question mark icon in the default UI's GossipFrame.

**Signature:**

```lua
name, level, isTrivial, ... = GetGossipActiveQuests()
```

**Returns:**

- `name` - Name of the quest (`string`)
- `level` - Suggested character level for attempting the quest (`number`)
- `isTrivial` - 1 if the quest is considered "trivial" at the player's level (rewards no XP); otherwise nil (`1nil`)
- `...` - Additional `name, level, isTrivial` values if more than one quest is active (`list`)

---

## GetGossipAvailableQuests

Returns a list of quests available from the current Gossip NPC. For quests which can be turned in to the NPC, see [`GetGossipActiveQuests()`](NPC Gossip Dialog.md#getgossipactivequests).

**Signature:**

```lua
name, level, isTrivial, isDaily, isRepeatable, ... = GetGossipAvailableQuests()
```

**Returns:**

- `name` - Name of the quest (`string`)
- `level` - Suggested character level for attempting the quest (`number`)
- `isTrivial` - 1 if the quest is considered "trivial" at the player's level (rewards no XP); otherwise nil (`1nil`)
- `isDaily` - 1 if the quest may be repeated only once per day; otherwise nil (`1nil`)
- `isRepeatable` - 1 if the quest may be repeated at any time; otherwise nil (`1nil`)
- `...` - Additional `name, level, isTrivial, isDaily, isRepeatable` values for each available quest (`list`)

---

## GetGreetingText

Returns the greeting text displayed for quest NPCs with multiple quests. Not used often; most quest NPCs offering multiple quests (and/or other options) use the Gossip functions to provide a greeting (see [`GetGossipText()`](NPC Gossip Dialog.md#getgossiptext)).

**Signature:**

```lua
greetingText = GetGreetingText()
```

**Returns:**

- `greetingText` - Text to be displayed before choosing from among the NPC's multiple quests (`string`)

---

## GetMaxDailyQuests

Returns the maximum number of daily quests that can be completed each day.

**Signature:**

```lua
max = GetMaxDailyQuests()
```

**Returns:**

- `max` - The maximum number of daily quests that can be completed each day (`number`)

---

## GetNumActiveQuests

Returns the number of quests which can be turned in to the current Quest NPC. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event.

Note: Most quest NPCs present active quests using the [`GetGossipActiveQuests()`](NPC Gossip Dialog.md#getgossipactivequests) instead of this function.

**Signature:**

```lua
numActiveQuests = GetNumActiveQuests()
```

**Returns:**

- `numActiveQuests` - Number of quests which can be turned in to the current Quest NPC (`number`)

---

## GetNumAvailableQuests

Returns the number quests available from the current Quest NPC. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event.

Note: Most quest NPCs present available quests using the [`GetGossipAvailableQuests()`](NPC Gossip Dialog.md#getgossipavailablequests) instead of this function.

**Signature:**

```lua
numAvailableQuests = GetNumAvailableQuests()
```

**Returns:**

- `numAvailableQuests` - Number of quests available from the current Quest NPC (`number`)

---

## GetNumGossipActiveQuests

Returns the number of quests which can be turned in to the current Gossip NPC. These quests are displayed with a question mark icon in the default UI's GossipFrame.

**Signature:**

```lua
num = GetNumGossipActiveQuests()
```

**Returns:**

- `num` - Number of quests which can be turned in to the current Gossip NPC (`number`)

---

## GetNumGossipAvailableQuests

Returns the number of quests available from the current Gossip NPC. These quests are displayed with an exclamation mark icon in the default UI's GossipFrame.

**Signature:**

```lua
num = GetNumGossipAvailableQuests()
```

**Returns:**

- `num` - Number of quests available from the current Gossip NPC (`number`)

---

## GetNumQuestChoices

Returns the number of available quest rewards from which the player must choose one upon completing the quest presented by a questgiver. Only valid during the accept/decline or completion stages of a quest dialog (following the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL) or [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) events); otherwise may return 0 or a value from the most recently displayed quest.

**Signature:**

```lua
numQuestChoices = GetNumQuestChoices()
```

**Returns:**

- `numQuestChoices` - Number of available quest rewards from which the player must choose one upon completing the quest (`number`)

---

## GetNumQuestItems

Returns the number of different items required to complete the quest presented by a questgiver. Usable following the [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS) event in which it is determined whether the player can complete the quest.

**Signature:**

```lua
numRequiredItems = GetNumQuestItems()
```

**Returns:**

- `numRequiredItems` - Number of different items required to complete the quest (`number`)

---

## GetNumQuestLeaderBoards

Returns the number of quest objectives for a quest in the player's quest log

**Signature:**

```lua
numObjectives = GetNumQuestLeaderBoards([questIndex])
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)); if omitted, defaults to the selected quest (`number`)

**Returns:**

- `numObjectives` - Number of trackable objectives for the quest (`number`)

---

## GetNumQuestLogChoices

Returns the number of available item reward choices for the selected quest in the quest log. This function refers to quest rewards for which the player is allowed to choose one item from among several; for items always awarded upon quest completion, see [GetNumQuestLogRewards](Quest.md#getnumquestlogrewards).

**Signature:**

```lua
numChoices = GetNumQuestLogChoices()
```

**Returns:**

- `numChoices` - Number of items among which a reward can be chosen for completing the quest (`number`)

---

## GetNumQuestLogEntries

Returns the number of quests and headers in the quest log

**Signature:**

```lua
numEntries, numQuests = GetNumQuestLogEntries()
```

**Returns:**

- `numEntries` - Total number of entries (quests and headers) (`number`)
- `numQuests` - Number of quests only (`number`)

---

## GetNumQuestLogRewards

Returns the number of item rewards for the selected quest in the quest log. This function refers to items always awarded upon quest completion; for quest rewards for which the player is allowed to choose one item from among several, see [GetNumQuestLogChoices](Quest.md#getnumquestlogchoices).

**Signature:**

```lua
numRewards = GetNumQuestLogRewards()
```

**Returns:**

- `numRewards` - Number of rewards for completing the quest (`number`)

---

## GetNumQuestRewards

Returns the number of different items always awarded upon completing the quest presented by a questgiver. Only valid during the accept/decline or completion stages of a quest dialog (following the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL) or [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) events); otherwise may return 0 or a value from the most recently displayed quest.

**Signature:**

```lua
numQuestRewards = GetNumQuestRewards()
```

**Returns:**

- `numQuestRewards` - Number of different items always awarded upon completing the quest (`number`)

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

## GetNumWorldStateUI

Returns the number of world state UI elements. World State UI elements include PvP, instance, and quest objective information (displayed at the top center of the screen in the default UI) as well as more specific information for "control point" style PvP objectives. Examples: the Horde/Alliance score in Arathi Basin, the tower status and capture progress bars in Hellfire Peninsula, the progress text in the Black Morass and Violet Hold instances, and the event status text for quests [The Light of Dawn](http://www.wowhead.com/?quest=12801) and [The Battle For The Undercity](http://www.wowhead.com/?quest=13267).

**Signature:**

```lua
numUI = GetNumWorldStateUI()
```

**Returns:**

- `numUI` - Returns the number of world state elements (`number`)

---

## GetObjectiveText

Returns a summary of objectives for the quest offered by a questgiver. Only valid when the questgiver UI is showing the accept/decline stage of a quest dialog (between the [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) and [`QUEST_FINISHED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_FINISHED) events); otherwise may return the empty string or a value from the most recently displayed quest.

**Signature:**

```lua
questObjective = GetObjectiveText()
```

**Returns:**

- `questObjective` - The objective text for the currently displayed quest (`string`)

---

## GetProgressText

Returns the quest progress text presented by a questgiver. Only valid when the questgiver UI is showing the progress stage of a quest dialog (between the [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS) and [`QUEST_FINISHED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_FINISHED) events); otherwise may return the empty string or a value from the most recently displayed quest.

**Signature:**

```lua
text = GetProgressText()
```

**Returns:**

- `text` - Progress text for the quest (`string`)

---

## GetQuestBackgroundMaterial

Returns background display style information for a questgiver dialog. The value returned can be used to look up background textures and text colors for display:

- Background textures displayed in the default UI can be found by prepending `"Interface\\ItemTextFrame\\ItemText-"` and appending `"-TopLeft"`, `"-TopRight"`, `"-BotLeft"`, `"-BotRight"` to the material string (e.g. `"Interface\\ItemTextFrame\\ItemText-Stone-TopLeft"`).
- Colors for body and title text can be found by calling `GetMaterialTextColors(material)` (a Lua function implemented in the Blizzard UI).

In cases where this function returns nil, the default UI uses the colors and textures for "Parchment".

**Signature:**

```lua
material = GetQuestBackgroundMaterial()
```

**Returns:**

- `material` - String identifying a display style for the questgiver dialog, or nil for the default style (`string`)
  - `Bronze` - Colored metallic background
  - `Marble` - Light stone background
  - `Parchment` - Yellowed parchment background (default)
  - `Silver` - Gray metallic background
  - `Stone` - Dark stone background

---

## GetQuestDifficultyColor `blizzardui`

Returns a table of color values indicating the difficulty of a quest's level as compared to the player's

**Signature:**

```lua
color = GetQuestDifficultyColor(level)
```

**Arguments:**

- `level` - Level for which to compare difficulty (`number`)

**Returns:**

- `color` - A table containing color values (keyed `r`, `g`, and `b`) representing the difficulty of a quest at the input level as compared to the player's (`table`)

---

## GetQuestGreenRange

Returns the level range in which a quest below the player's level still rewards XP. If a quest's level is up to `range` levels below the player's level, the quest is considered easy but still rewards experience points upon completion; these quests are colored green in the default UI's quest log. (Quests more than `range` levels below the player's are colored gray in the default UI and reward no XP.)

**Signature:**

```lua
range = GetQuestGreenRange()
```

**Returns:**

- `range` - Maximum difference between player level and a lower quest level for a quest to reward experience (`number`)

**Examples:**

```lua
-- function used to color quest log entries in the default UI
function GetDifficultyColor(level)
  local levelDiff = level - UnitLevel("player");
  local color
  if ( levelDiff >= 5 ) then
    color = QuestDifficultyColor["impossible"];
  elseif ( levelDiff >= 3 ) then
    color = QuestDifficultyColor["verydifficult"];
  elseif ( levelDiff >= -2 ) then
    color = QuestDifficultyColor["difficult"];
  elseif ( -levelDiff <= GetQuestGreenRange() ) then
    color = QuestDifficultyColor["standard"];
  else
    color = QuestDifficultyColor["trivial"];
  end
  return color;
end
```

---

## GetQuestIndexForTimer

Returns the quest log index of a timed quest's timer

**Signature:**

```lua
questIndex = GetQuestIndexForTimer(index)
```

**Arguments:**

- `index` - Index of a timer (in the list returned by [`GetQuestTimers()`](Quest.md#getquesttimers)) (`number`)

**Returns:**

- `questIndex` - Index of the quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

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

## GetQuestItemInfo

Returns information about items in a questgiver dialog. Only valid when the questgiver UI is showing the accept/decline, progress, or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED`, `QUEST_PROGRESS` and `QUEST_FINISHED`, or `QUEST_COMPLETE` and `QUEST_FINISHED` events); otherwise may return empty values or those from the most recently displayed quest.

**Signature:**

```lua
name, texture, numItems, quality, isUsable = GetQuestItemInfo("type", index)
```

**Arguments:**

- `type` - Which of the possible sets of items to query (`string`)
  - `choice` - Items from which the player may choose a reward
  - `required` - Items required to complete the quest
  - `reward` - Items given as reward for the quest
- `index` - Which item to query (from 1 to GetNumQuestChoices(), GetNumQuestItems(), or GetNumQuestRewards(), depending on the value of the itemType argument) (`number`)

**Returns:**

- `name` - The name of the item (`string`)
- `texture` - Path to a texture for the item's icon (`string`)
- `numItems` - Number of the item required or rewarded (`number`)
- `quality` - The quality of the item (`number`)
  - `0` - Poor
  - `1` - Common
  - `2` - Uncommon
  - `3` - Rare
  - `4` - Epic
  - `5` - Legendary
  - `6` - Artifact
- `isUsable` - 1 if the player can currently use/equip the item; otherwise nil (`1nil`)

---

## GetQuestItemLink

Returns a hyperlink for an item in a questgiver dialog. Only valid when the questgiver UI is showing the accept/decline, progress, or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED`, `QUEST_PROGRESS` and `QUEST_FINISHED`, or `QUEST_COMPLETE` and `QUEST_FINISHED` events); otherwise may return `nil` or a value from the most recently displayed quest.

**Signature:**

```lua
link = GetQuestItemLink("itemType", index)
```

**Arguments:**

- `itemType` - Token identifying one of the possible sets of items (`string`)
  - `choice` - Items from which the player may choose a reward
  - `required` - Items required to complete the quest
  - `reward` - Items given as reward for the quest
- `index` - Index of an item in the set (between 1 and `GetNumQuestChoices()`, `GetNumQuestItems()`, or `GetNumQuestRewards()`, according to `itemType`) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`)

---

## GetQuestLink

Returns a hyperlink for an entry in the player's quest log

**Signature:**

```lua
link = GetQuestLink(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

**Returns:**

- `link` - A hyperlink for the quest (`string`, [hyperlink](../types/hyperlink.md))

---

## GetQuestLogChoiceInfo

Returns information about available item rewards for the selected quest in the quest log. This function refers to quest rewards for which the player is allowed to choose one item from among several; for items always awarded upon quest completion, see [GetQuestLogRewardInfo](Quest.md#getquestlogrewardinfo).

**Signature:**

```lua
name, texture, numItems, quality, isUsable = GetQuestLogChoiceInfo(index)
```

**Arguments:**

- `index` - Index of a quest reward choice (between 1 and GetNumQuestLogChoices()) (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `numItems` - Number of items in the stack (`number`)
- `quality` - Quality of the item (`number`, [itemQuality](../types/itemQuality.md))
- `isUsable` - 1 if the player can use or equip the item; otherwise nil (`1nil`)

---

## GetQuestLogCompletionText

Returns the completion text for the selected quest in the quest log. Completion text usually includes instructions on to whom and where to hand in the quest once it has been completed. Example: "Return to William Pestle at Goldshire in Elwynn Forest."

**Signature:**

```lua
completionText = GetQuestLogCompletionText()
```

**Returns:**

- `completionText` - Completion instructions for the quest (`string`)

---

## GetQuestLogGroupNum

Returns the suggested group size for the selected quest in the quest log

**Signature:**

```lua
suggestedGroup = GetQuestLogGroupNum()
```

**Returns:**

- `suggestedGroup` - Recommended number of players in a group attempting the quest (`number`)

---

## GetQuestLogItemLink

Returns a hyperlink for an item related to the selected quest in the quest log

**Signature:**

```lua
GetQuestLogItemLink("itemType", index)
```

**Arguments:**

- `itemType` - Token identifying one of the possible sets of items (`string`)
  - `choice` - Items from which the player may choose a reward
  - `reward` - Items always given as reward for the quest
- `index` - Index of an item in the set (between 1 and `GetNumQuestLogChoices()` or `GetNumQuestLogRewards()`, according to `itemType`) (`number`)

---

## GetQuestLogLeaderBoard

Returns information about objectives for a quest in the quest log

**Signature:**

```lua
text, type, finished = GetQuestLogLeaderBoard(objective [, questIndex])
```

**Arguments:**

- `objective` - Index of a quest objective (between 1 and [`GetNumQuestLeaderBoards()`](Quest.md#getnumquestleaderboards)) (`number`)
- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)); if omitted, defaults to the selected quest (`number`)

**Returns:**

- `text` - Text of the objective (e.g. "Gingerbread Cookie: 0/5") (`string`)
- `type` - Type of objective (`string`)
  - `event` - Requires completion of a scripted event
  - `item` - Requires collecting a number of items
  - `monster` - Requires slaying a number of NPCs
  - `object` - Requires interacting with a world object
  - `reputation` - Requires attaining a certain level of reputation with a faction
- `finished` - 1 if the objective is complete; otherwise nil (`1nil`)

---

## GetQuestLogPushable

Return whether the selected quest in the quest log can be shared to party members

**Signature:**

```lua
shareable = GetQuestLogPushable()
```

**Returns:**

- `shareable` - 1 if the quest is shareable; otherwise nil (`1nil`)

---

## GetQuestLogQuestText

Returns the description and objective text for the selected quest in the quest log

**Signature:**

```lua
questDescription, questObjectives = GetQuestLogQuestText()
```

**Returns:**

- `questDescription` - Full description of the quest (as seen in the NPC dialog when accepting the quest) (`string`)
- `questObjectives` - A (generally) brief summary of quest objectives (`string`)

---

## GetQuestLogRequiredMoney

Returns the amount of money required for the selected quest in the quest log

**Signature:**

```lua
money = GetQuestLogRequiredMoney()
```

**Returns:**

- `money` - The amount of money required to complete the quest (in copper) (`number`)

---

## GetQuestLogRewardHonor

Returns the honor reward for the selected quest in the quest log

---

## GetQuestLogRewardInfo

Returns information about item rewards for the selected quest in the quest log. This function refers to items always awarded upon quest completion; for quest rewards for which the player is allowed to choose one item from among several, see [GetQuestLogChoiceInfo](Quest.md#getquestlogchoiceinfo).

**Signature:**

```lua
name, texture, numItems, quality, isUsable = GetQuestLogRewardInfo(index)
```

**Arguments:**

- `index` - Index of a quest reward (between 1 and GetNumQuestLogRewards()) (`number`)

**Returns:**

- `name` - Name of the item (`string`)
- `texture` - Path to an icon texture for the item (`string`)
- `numItems` - Number of items in the stack (`number`)
- `quality` - Quality of the item (`number`, [itemQuality](../types/itemQuality.md))
- `isUsable` - 1 if the player can use or equip the item; otherwise nil (`1nil`)

---

## GetQuestLogRewardMoney

Returns the money reward for the selected quest in the quest log

**Signature:**

```lua
money = GetQuestLogRewardMoney()
```

**Returns:**

- `money` - Amount of money rewarded for completing the quest (in copper) (`number`)

---

## GetQuestLogRewardSpell

Returns information about the spell reward for the selected quest in the quest log. If both `isTradeskillSpell` and `isSpellLearned` are `nil`, the reward is a spell cast upon the player.

**Signature:**

```lua
texture, name, isTradeskillSpell, isSpellLearned = GetQuestLogRewardSpell()
```

**Returns:**

- `texture` - Path to the spell's icon texture (`string`)
- `name` - Name of the spell (`string`)
- `isTradeskillSpell` - 1 if the spell is a tradeskill recipe; otherwise nil (`1nil`)
- `isSpellLearned` - 1 if the reward teaches the player a new spell; otherwise nil (`1nil`)

---

## GetQuestLogRewardTalents

Returns the talent point reward for the selected quest in the quest log. Returns `0` for quests which do not award talent points.

(Very few quests award talent points; currently this functionality is only used within the Death Knight starting experience.)

**Signature:**

```lua
talents = GetQuestLogRewardTalents()
```

**Returns:**

- `talents` - Number of talent points to be awarded upon completing the quest (`number`)

---

## GetQuestLogRewardTitle

Returns the title reward for the selected quest in the quest log. Returns `nil` if no title is awarded or if no quest is selected.

**Signature:**

```lua
title = GetQuestLogRewardTitle()
```

**Returns:**

- `title` - Title to be awarded to the player upon completing the quest (`string`)

---

## GetQuestLogSelection

Returns the index of the selected quest in the quest log

**Signature:**

```lua
questIndex = GetQuestLogSelection()
```

**Returns:**

- `questIndex` - Index of the selected quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

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

## GetQuestLogSpellLink

Returns a hyperlink for a spell in the selected quest in the quest log

**Signature:**

```lua
link = GetQuestLogSpellLink()
```

**Returns:**

- `link` - A hyperlink for the spell or tradeskill recipe (`string`, [hyperlink](../types/hyperlink.md))

---

## GetQuestLogTimeLeft

Returns time remaining for the selected quest in the quest log. If the selected quest is not timed, returns nil.

**Signature:**

```lua
questTimer = GetQuestLogTimeLeft()
```

**Returns:**

- `questTimer` - The amount of time left to complete the quest (`number`)

---

## GetQuestLogTitle

Returns information about an entry in the player's quest log

**Signature:**

```lua
questLogTitleText, level, questTag, suggestedGroup, isHeader, isCollapsed, isComplete, isDaily, questID = GetQuestLogTitle(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

**Returns:**

- `questLogTitleText` - Title of the quest (`string`)
- `level` - Recommended character level for attempting the quest (`number`)
- `questTag` - Localized tag describing the type of quest (`string`)
  - `Dungeon` - Dungeon or instance quest
  - `Elite` - Elite quest
  - `Group` - Group quest
  - `Heroic` - Heroic quest
  - `PVP` - PVP specific quest
  - `Raid` - Raid quest
  - `nil` - Standard quest
- `suggestedGroup` - For some group quests, the recommended number of group members for attempting the quest (`number`)
- `isHeader` - 1 if the entry is a group header; nil if the entry is a quest (`1nil`)
- `isCollapsed` - 1 if the entry is a collapsed header; otherwise nil (`1nil`)
- `isComplete` - Whether the quest is complete (`number`)
  - `-1` - The quest was failed
  - `1` - The quest was completed
  - `nil` - The quest has yet to reach a conclusion
- `isDaily` - 1 if the quest is a daily quest; otherwise nil (`1nil`)
- `questID` - The quest's questID. (`number`)

---

## GetQuestMoneyToGet

Returns the amount of money required to complete the quest presented by a questgiver. Usable following the [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS) event in which it is determined whether the player can complete the quest.

**Signature:**

```lua
money = GetQuestMoneyToGet()
```

**Returns:**

- `money` - Amount of money required to complete the quest (in copper) (`number`)

---

## GetQuestResetTime

Returns the amount of time remaining until the daily quest period resets

**Signature:**

```lua
time = GetQuestResetTime()
```

**Returns:**

- `time` - Amount of time remaining until the daily quest period resets (in seconds) (`number`)

**Examples:**

```lua
-- Print the amount of time until dailies reset
print("Daily quests reset in " .. SecondsToTime(GetQuestResetTime()))
```

---

## GetQuestReward

Finishes turning in a quest to a questgiver, selecting an item reward if applicable. Usable following the [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) event in which the questgiver presents the player with rewards.

**Signature:**

```lua
GetQuestReward(choice)
```

**Arguments:**

- `choice` - Index of a quest reward choice (between 1 and [`GetNumQuestChoices()`](Quest.md#getnumquestchoices)), or nil if the quest does not offer a choice of item rewards (`number`)

---

## GetQuestSpellLink

Returns a hyperlink for a spell in a questgiver dialog. Only valid when the questgiver UI is showing the accept/decline, progress, or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED`, `QUEST_PROGRESS` and `QUEST_FINISHED`, or `QUEST_COMPLETE` and `QUEST_FINISHED` events); otherwise may return empty values or those from the most recently displayed quest.

**Signature:**

```lua
link = GetQuestSpellLink()
```

**Returns:**

- `link` - A hyperlink for the spell or tradeskill recipe (`string`, [hyperlink](../types/hyperlink.md))

---

## GetQuestText

Returns the text for the quest offered by a questgiver. Only valid when the questgiver UI is showing the accept/decline stage of a quest dialog (between the [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) and [`QUEST_FINISHED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_FINISHED) events); otherwise may return the empty string or a value from the most recently displayed quest.

**Signature:**

```lua
text = GetQuestText()
```

**Returns:**

- `text` - The text for the currently displayed quest (`string`)

---

## GetQuestTimers

Returns a list of the times remaining for any active timed quests

**Signature:**

```lua
... = GetQuestTimers()
```

**Returns:**

- `...` - A list of numbers, each the amount of time (in seconds) remaining for a timed quest (`number`)

---

## GetQuestsCompleted

Gets a table containing the quests the player has completed. This function will only return data after [QueryQuestsCompleted()](Quest.md#queryquestscompleted-server) has been called and the [`QUEST_QUERY_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_QUERY_COMPLETE) event has fired. The keys in the returned table are the numeric questIds, with a value of true for each set key.

**Signature:**

```lua
completedQuests = GetQuestsCompleted(questTbl)
```

**Arguments:**

- `questTbl` - A table that will be wiped and filled with the quest data (`table`)

**Returns:**

- `completedQuests` - A hash table containing a list of the questIds the player has completed. (`table`)

---

## GetRewardHonor

Returns the amount of honor points awarded when completing a quest.

Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED `events); otherwise may return zero or a value from the most recently displayed quest.

**Signature:**

```lua
honor = GetRewardHonor()
```

**Returns:**

- `honor` - The honor points to be awarded (`number`)

---

## GetRewardMoney

Returns the amount of money awarded when completing a quest.

Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED `events); otherwise may return zero or a value from the most recently displayed quest.

**Signature:**

```lua
money = GetRewardMoney()
```

**Returns:**

- `money` - The amount of money to be awarded (in copper) (`number`)

---

## GetRewardSpell

Returns information about a spell awarded when completing a quest. Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED` events); otherwise may return zero or values from the most recently displayed quest.

If both `isTradeskillSpell` and `isSpellLearned` are `nil`, the reward is a spell cast upon the player.

**Signature:**

```lua
texture, name, isTradeskillSpell, isSpellLearned = GetRewardSpell()
```

**Returns:**

- `texture` - Path to the spell's icon texture (`string`)
- `name` - Name of the spell (`string`)
- `isTradeskillSpell` - 1 if the spell is a tradeskill recipe; otherwise nil (`1nil`)
- `isSpellLearned` - 1 if the reward teaches the player a new spell; otherwise nil (`1nil`)

---

## GetRewardTalents

Returns the talent points awarded when completing a quest. Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED` events); otherwise may return zero or a value from the most recently displayed quest.

(Very few quests award talent points; currently this functionality is only used within the Death Knight starting experience.)

**Signature:**

```lua
talents = GetRewardTalents()
```

**Returns:**

- `talents` - The talent points to be awarded (`number`)

---

## GetRewardText

Returns questgiver dialog to be displayed when completing a quest. Only valid when the questgiver UI is showing the completion stage of a quest dialog (between the [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) and [`QUEST_FINISHED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_FINISHED) events); otherwise may return the empty string or a value from the most recently displayed quest.

**Signature:**

```lua
text = GetRewardText()
```

**Returns:**

- `text` - Text to be displayed for the quest completion dialog (`string`)

---

## GetRewardTitle

Returns the title awarded when completing a quest.

Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED `events); otherwise may return nil or a value from the most recently displayed quest.

**Signature:**

```lua
title = GetRewardTitle()
```

**Returns:**

- `title` - The title to be awarded, or nil if the quest does not reward a title (`string`)

---

## GetRewardXP

Returns the experience awarded when completing a quest

---

## GetSuggestedGroupNum

Returns the suggested group size for attempting the quest currently offered by a questgiver. Usable following the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL) event in which the questgiver presents the player with the details of a quest and the option to accept or decline.

**Signature:**

```lua
suggestedGroup = GetSuggestedGroupNum()
```

**Returns:**

- `suggestedGroup` - Suggested group size for attempting the quest currently offered by a questgiver (`number`)

---

## GetTitleText

Returns the title text for the quest presented by a questgiver. Only valid following the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL), [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS), or [`QUEST_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_COMPLETE) events; otherwise may return nil or a value from the most recently displayed quest.

**Signature:**

```lua
text = GetTitleText()
```

**Returns:**

- `text` - Title text for the quest (`string`)

---

## GetWorldStateUIInfo

Returns information about a world state UI element. World State UI elements include PvP, instance, and quest objective information (displayed at the top center of the screen in the default UI) as well as more specific information for "control point" style PvP objectives. Examples: the Horde/Alliance score in Arathi Basin, the tower status and capture progress bars in Hellfire Peninsula, the progress text in the Black Morass and Violet Hold instances, and the event status text for quests [The Light of Dawn](https://web.archive.org/web/20100106001949/http://www.wowhead.com/?quest=12801) and [The Battle For The Undercity](https://web.archive.org/web/20100106001949/http://www.wowhead.com/?quest=13267).

**Signature:**

```lua
uiType, state, text, icon, dynamicIcon, tooltip, dynamicTooltip, extendedUI, extendedUIState1, extendedUIState2, extendedUIState3 = GetWorldStateUIInfo(index)
```

**Arguments:**

- `index` - Index of a world state UI element (between 1 and [`GetNumWorldStateUI()`](Instance.md#getnumworldstateui)) (`number`)

**Returns:**

- `uiType` - 1 if the element should be conditionally displayed (based on the state of the "Show World PvP Objectives" setting and the player's location); any other value if the element is always displayed (`number`)
- `state` - State of the element: 0 always indicates the element should be hidden; other possible states vary by context (e.g. in Warsong Gulch, state 2 indicates the team holds the enemy flag) (`number`)
- `text` - Text to be displayed for the element (`string`)
- `icon` - Path to a texture for the element's main icon (usually describing the element itself: e.g. a Horde or Alliance icon for elements displaying a battleground score) (`string`)
- `dynamicIcon` - Path to a texture for a secondary icon (usually describing transient status: e.g. a flag icon in Warsong Gulch) (`string`)
- `tooltip` - Text to be displayed when mousing over the UI element (`string`)
- `dynamicTooltip` - Text to be displayed when mousing over the element's `dynamicIcon` (`string`)
- `extendedUI` - Identifies the type of additional UI elements to display if applicable (`string`)
  - `""` - No additional UI should be displayed
  - `"CAPTUREPOINT"` - A capture progress bar should be displayed for the element
- `extendedUIState1` - Index of the capture progress bar corresponding to the element (`number`)
- `extendedUIState2` - Position of the capture bar (0 = left/Horde edge, 100 = right/Alliance edge) (`number`)
- `extendedUIState3` - Width of the neutral section of the capture bar: e.g. if 50, the `extendedUIState2` values 0-25 correspond to Horde ownership of the objective, values 76-100 to Alliance ownership, and values 26-75 to no ownership (`number`)

---

## IsActiveQuestTrivial

Returns whether a quest which can be turned in to the current Quest NPC is trivial at the player's level. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event. Used in the default UI to display "(low level)" when listing the quest.

Note: Most quest NPCs present active quests using the [`GetGossipActiveQuests()`](NPC Gossip Dialog.md#getgossipactivequests) instead of this function.

**Signature:**

```lua
trivial = IsActiveQuestTrivial(index)
```

**Arguments:**

- `index` - Index of a quest which can be turned in to the current Quest NPC (between 1 and [`GetNumActiveQuests()`](Quest.md#getnumactivequests)) (`number`)

**Returns:**

- `trivial` - 1 if the quest is trivial at the player's level; otherwise nil (`1nil`)

---

## IsAvailableQuestTrivial

Returns whether a quest available from the current Quest NPC is trivial at the player's level. Only returns valid information after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event. Used in the default UI to display "(low level)" when listing the quest.

Note: Most quest NPCs present available quests using the [`GetGossipAvailableQuests()`](NPC Gossip Dialog.md#getgossipavailablequests) instead of this function.

**Signature:**

```lua
trivial = IsAvailableQuestTrivial(index)
```

**Arguments:**

- `index` - Index of a quest available from the current Quest NPC (between 1 and [`GetNumAvailableQuests()`](Quest.md#getnumavailablequests)) (`number`)

**Returns:**

- `trivial` - 1 if the quest is trivial at the player's level; otherwise nil (`1nil`)

---

## IsCurrentQuestFailed

Returns whether the player has failed the selected quest in the quest log

**Signature:**

```lua
isFailed = IsCurrentQuestFailed()
```

**Returns:**

- `isFailed` - 1 if the player has failed the quest; otherwise nil (`1nil`)

---

## IsQuestCompletable

Returns whether the player can complete the quest presented by a questgiver

**Signature:**

```lua
isCompletable = IsQuestCompletable()
```

**Returns:**

- `isCompletable` - 1 if the player currently meets the requirements (e.g. number of items collected) complete the quest; otherwise nil (`1nil`)

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

## IsUnitOnQuest

Checks if a specified unit is on a quest from the players quest log.

**Signature:**

```lua
state = IsUnitOnQuest(index, "unit")
```

**Arguments:**

- `index` - The quest index to query. (`number`)
- `unit` - The name of the unit to query. (`string`)

**Returns:**

- `state` - 1 if the unit is on that quest, nil otherwise (`1nil`)

---

## QueryQuestsCompleted `server`

Queries the server for the player's completed quest information. This function is throttled by the server and can currently only be called every 15 minutes. This function will return immediately, and the [`QUEST_QUERY_COMPLETE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_QUERY_COMPLETE) will fire when the information is available from the server. At that point, it can be obtained using the [GetQuestsCompleted](Quest.md#getquestscompleted) function.

**Signature:**

```lua
QueryQuestsCompleted()
```

---

## QuestChooseRewardError

Causes the default UI to display an error message indicating that the player must choose a reward to complete the quest presented by a questgiver. Fires a [`UI_ERROR_MESSAGE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UI_ERROR_MESSAGE) event containing a localized message identified by the global variable `ERR_QUEST_MUST_CHOOSE`. Choose wisely.

**Signature:**

```lua
QuestChooseRewardError()
```

---

## QuestFlagsPVP

Returns whether accepting the offered quest will flag the player for PvP. Only valid when the questgiver UI is showing the accept/decline stage of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events); otherwise may return nil or a value from the most recently displayed quest.

**Signature:**

```lua
questFlag = QuestFlagsPVP()
```

**Returns:**

- `questFlag` - 1 if accepting the quest will flag the player for PvP for as long as it remains in the quest log; otherwise nil (`1nil`)

---

## QuestGetAutoAccept

This function is not yet documented

---

## QuestLogPushQuest

Shares a quest with other group members

**Signature:**

```lua
QuestLogPushQuest([questIndex])
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)); if omitted, defaults to the selected quest (`number`)

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

## SelectActiveQuest

Selects a quest which can be turned in to the current Quest NPC. Usable after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event. Causes the [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS) event to fire, in which it is determined whether the player can complete the quest.

Note: Most quest NPCs present active quests using the [`GetGossipActiveQuests()`](NPC Gossip Dialog.md#getgossipactivequests) instead of this function.

**Signature:**

```lua
SelectActiveQuest(index)
```

**Arguments:**

- `index` - Index of a quest which can be turned in to the current Quest NPC (between 1 and [`GetNumActiveQuests()`](Quest.md#getnumactivequests)) (`number`)

---

## SelectAvailableQuest

Chooses a quest available from the current Quest NPC. Causes the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL) event to fire, in which the questgiver presents the player with the details of a quest and the option to accept or decline.

Note: Most quest NPCs present available quests using the [`GetGossipAvailableQuests()`](NPC Gossip Dialog.md#getgossipavailablequests) instead of this function.

**Signature:**

```lua
SelectAvailableQuest(index)
```

**Arguments:**

- `index` - Index of a quest available from the current Quest NPC (between 1 and [`GetNumAvailableQuests()`](Quest.md#getnumavailablequests)) (`number`)

---

## SelectGossipActiveQuest

Chooses a quest which can be turned in to the current Gossip NPC. Causes the [`QUEST_PROGRESS`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_PROGRESS) event to fire, in which it is determined whether the player can complete the quest.

**Signature:**

```lua
SelectGossipActiveQuest(index)
```

**Arguments:**

- `index` - Index of a quest which can be turned in to the current Gossip NPC (between 1 and [`GetNumGossipActiveQuests()`](NPC Gossip Dialog.md#getnumgossipactivequests)) (`number`)

---

## SelectGossipAvailableQuest

Chooses a quest available from the current Gossip NPC. Usable after a [`QUEST_GREETING`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_GREETING) event. Causes the [`QUEST_DETAIL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/QUEST_DETAIL) event to fire, in which the questgiver presents the player with the details of a quest and the option to accept or decline.

**Signature:**

```lua
SelectGossipAvailableQuest(index)
```

**Arguments:**

- `index` - Index of a quest available from the current Gossip NPC (between 1 and [`GetNumGossipAvailableQuests()`](NPC Gossip Dialog.md#getnumgossipavailablequests)) (`number`)

---

## SelectQuestLogEntry

Selects a quest from the quest log. The selected quest is used by other functions which do not take a quest index as argument (e.g. [`GetQuestLogQuestText()`](Quest.md#getquestlogquesttext)).

**Signature:**

```lua
SelectQuestLogEntry(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

---

## SetAbandonQuest

Begins the process of abandoning a quest in the player's quest log. To finish abandoning the quest, call [`AbandonQuest()`](Quest.md#abandonquest-confirmation).

This function must be called to select a quest in order for [`GetAbandonQuestItems()`](Quest.md#getabandonquestitems) or [`GetAbandonQuestName()`](Quest.md#getabandonquestname) to return valid data.

**Signature:**

```lua
SetAbandonQuest(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](Quest.md#getnumquestlogentries)) (`number`)

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
