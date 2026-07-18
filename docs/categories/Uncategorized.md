# Uncategorized functions

← [WoW API Docs](../index.md)

**192** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#uncategorized)

---

## AcceptProposal

Accepts a LFG dungeon invite.

**Signature:**

```lua
AcceptProposal()
```

---

## BNAcceptFriendInvite

This function is not yet documented

---

## BNConnected

Returns whether or not the player is connected to Battle.net

**Signature:**

```lua
isOnline = BNConnected()
```

**Returns:**

- `isOnline` - true if the player is connected to Battle.net; otherwise false (`boolean`)

---

## BNCreateConversation

Create a conversation between you and two friends

**Signature:**

```lua
result = BNCreateConversation(presenceID_1, presenceID_2)
```

**Arguments:**

- `presenceID_1` - The presenceID of your first friend (`number`)
- `presenceID_2` - The presenceID of your second friend (`number`)

**Returns:**

- `result` - ASSUMPTION: If creation conversation was successful or not (`boolean`)

---

## BNDeclineFriendInvite

This function is not yet documented

---

## BNFeaturesEnabled

Returns whether or not RealID services are disabled

**Signature:**

```lua
isEnabled = BNFeaturesEnabled()
```

**Returns:**

- `isEnabled` - true if RealID is enabled; otherwise false (`boolean`)

---

## BNFeaturesEnabledAndConnected

This function is not yet documented

---

## BNGetBlockedInfo

This function is not yet documented

---

## BNGetBlockedToonInfo

This function is not yet documented

---

## BNGetConversationInfo

Returns information about an existing battle.net conversation

**Signature:**

```lua
type = BNGetConversationInfo(channel)
```

**Arguments:**

- `channel` - ID of channel you want to check (`number`)

**Returns:**

- `type` - Seems to be 'conversation' if the conversation exists, nil if not (`string`)

---

## BNGetConversationMemberInfo

Returns information about a member of a battle.net conversation

**Signature:**

```lua
presenceID, unknown, displayName = BNGetConversationMemberInfo(channel, memberIndex)
```

**Arguments:**

- `channel` - The index of the channel you want member info for (`number`)
- `memberIndex` - The index of the member you want info for (`number`)

**Returns:**

- `presenceID` - This number seems to be the same as the presence ID of the RealID friend (`number`)
- `unknown` - Unknown (ID?) (`number`)
- `displayName` - The name that gets displayed with chat messages. Real name for friends, charname for FoF (`string`)

---

## BNGetCustomMessageTable

This function is not yet documented

---

## BNGetFOFInfo

Returns information about the specified friend of a RealID friend

**Signature:**

```lua
presenceID, givenName, surname, isFriend = BNGetFOFInfo(presenceID, mutual, non-mutual, index)
```

**Arguments:**

- `presenceID` - presenceID for the RealID friend for whom you are requesting friend info (`number`)
- `mutual` - Should the list include mutual friends (i.e. people who you and the person referenced by presenceID are both friends with). (`boolean`)
- `non-mutual` - Should the list include non-mutual friends. (`boolean`)
- `index` - The index of the entry in the list to retrieve (1 to BNGetNumFOF(...)) (`number`)

**Returns:**

- `presenceID` - a unique numeric identifier for this friend for this session (`number`)
- `givenName` - a |K Escape Sequence representing the friend's first/given name (`string`)
- `surname` - a |K Escape Sequence representing the friend's Surname/Family name (`string`)
- `isFriend` - true if this person is a direct friend of yours, false otherwise (`boolean`)

---

## BNGetFriendInviteInfo

This function is not yet documented

---

## BNGetMaxPlayersInConversation

Returns the maximum number of realID friends you can have in one conversation

**Signature:**

```lua
count = BNGetMaxPlayersInConversation()
```

**Returns:**

- `count` - The max number of players that can be in one conversation (`number`)

---

## BNGetNumBlocked

This function is not yet documented

---

## BNGetNumBlockedToons

This function is not yet documented

---

## BNGetNumConversationMembers

Returns the number of members in a battle.net conversation

**Signature:**

```lua
memberCount = BNGetNumConversationMembers(channel)
```

**Arguments:**

- `channel` - The index of the conversation to get member count for (`number`)

**Returns:**

- `memberCount` - Number of members in the conversation you asked for. 0 for non-existing conversations (`number`)

---

## BNGetNumFOF

This function is not yet documented

---

## BNGetNumFriendInvites

This function is not yet documented

---

## BNGetSelectedBlock

This function is not yet documented

---

## BNGetSelectedToonBlock

This function is not yet documented

---

## BNInviteToConversation

Invite a friend into an existing conversation

**Signature:**

```lua
BNInviteToConversation(channel, presenceID)
```

**Arguments:**

- `channel` - The ID of the conversation to invite to (`number`)
- `presenceID` - The presenceID of the friend to invite (`number`)

---

## BNIsBlocked

This function is not yet documented

---

## BNIsFriend

This function is not yet documented

---

## BNIsSelf

Returns whether or not the presence ID is the one of the player

**Signature:**

```lua
isSelf = BNIsSelf(presenceID)
```

**Arguments:**

- `presenceID` - (`number`)

**Returns:**

- `isSelf` - true if the presence ID is the one of the player; false otherwise (`boolean`)

---

## BNIsToonBlocked

This function is not yet documented

---

## BNLeaveConversation

This function is not yet documented

---

## BNListConversation

This function is not yet documented

---

## BNRemoveFriend

This function is not yet documented

---

## BNReportFriendInvite

This function is not yet documented

---

## BNReportPlayer

This function is not yet documented

---

## BNRequestFOFInfo

This function is not yet documented

---

## BNSendConversationMessage

This function is not yet documented

---

## BNSendFriendInvite

This function is not yet documented

---

## BNSendFriendInviteByID

This function is not yet documented

---

## BNSendWhisper

This function is not yet documented

---

## BNSetAFK

This function is not yet documented

---

## BNSetBlocked

This function is not yet documented

---

## BNSetDND

This function is not yet documented

---

## BNSetFocus

This function is not yet documented

---

## BNSetSelectedBlock

This function is not yet documented

---

## BNSetSelectedFriend

This function is not yet documented

---

## BNSetSelectedToonBlock

This function is not yet documented

---

## BNSetToonBlocked

This function is not yet documented

---

## BattlefieldMgrEntryInviteResponse

This function is not yet documented

---

## BattlefieldMgrExitRequest

This function is not yet documented

---

## BattlefieldMgrQueueInviteResponse

This function is not yet documented

---

## BattlefieldMgrQueueRequest

This function is not yet documented

---

## CalendarContextInviteTentative

This function is not yet documented

---

## CalendarEventTentative

This function is not yet documented

---

## CalendarGetDayEventSequenceInfo

This function is not yet documented

---

## CanChangePlayerDifficulty

This function is not yet documented

---

## CanMapChangeDifficulty

This function is not yet documented

---

## CanPartyLFGBackfill

This function is not yet documented

---

## CanResetTutorials

This function is not yet documented

---

## CancelSell

This function is not yet documented

---

## CannotBeResurrected

This function is not yet documented

---

## ChangePlayerDifficulty

This function is not yet documented

---

## ClearAllLFGDungeons

This function is not yet documented

---

## ClearLFGDungeon

This function is not yet documented

---

## CompleteLFGRoleCheck

This function is not yet documented

---

## DungeonUsesTerrainMap

This function is not yet documented

---

## FindSpellBookSlotByID

Return the spell book slot number of a supplied spellID.

---

## ForceGossip

This function is not yet documented

---

## GMReportLag

This function is not yet documented

---

## GetAllowLowLevelRaid

This function is not yet documented

---

## GetAutoCompletePresenceID

This function is not yet documented

---

## GetAvailableQuestInfo

Returns the flags of an available quest during an NPC dialog

**Signature:**

```lua
isTrivial, isDaily, isRepeatable = GetAvailableQuestInfo(availableIndex)
```

**Arguments:**

- `availableIndex` - Number of an available quest in the dialog frame; 1..[`GetNumAvailableQuests()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumAvailableQuests) (`number`)

**Returns:**

- `isTrivial` - True if the quest is trivial (gray), false otherwise. (`boolean`)
- `isDaily` - True if the quest is daily, false otherwise. (`boolean`)
- `isRepeatable` - True if the quest is repeatable, false otherwise. (`boolean`)

---

## GetAvailableRoles

Returns what roles the player is able to queue into the LFD system as

---

## GetChatWindowSavedDimensions

This function is not yet documented

---

## GetChatWindowSavedPosition

This function is not yet documented

---

## GetContainerItemQuestInfo

Returns quest information about an item in the player's bags

**Signature:**

```lua
isQuest, questId, isActive = GetContainerItemQuestInfo(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `isQuest` - true if the item is a quest item, nil otherwise. (`boolean`)
- `questId` - ID of the quest started by the item, nil if the item does not start a quest. (`number`)
- `isActive` - 1 if the quest started by the item is in the player's quest log, nil otherwise. (`1nil`)

---

## GetFactionInfoByID

Returns information about a faction or header listing. Returns information about a faction regardless of whether the faction is known to the player (indeed, even for factions only available to the opposing alliance); see [`GetFactionInfo`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetFactionInfo) for information about factions listed in the player's Reputation UI.

Faction IDs used by this function match those found on database sites (e.g. [Guardians of Hyjal](http://www.wowhead.com/faction=1158)) and are also returned by [`GetQuestLogRewardFactionInfo`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetQuestLogRewardFactionInfo).

**Signature:**

```lua
name, description, standingID, barMin, barMax, barValue, atWarWith, canToggleAtWar, isHeader, isCollapsed, hasRep, isWatched, isChild = GetFactionInfoByID(factionID)
```

**Arguments:**

- `factionID` - Unique numeric identifier for a faction (`number`)

**Returns:**

- `name` - Name of the faction (`string`)
- `description` - Brief description of the faction, as displayed in the default UI's detail window for a selected faction (`string`)
- `standingID` - Current standing with the given faction (`number`, [standingID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#standingID))
  - `1` - Hated
  - `2` - Hostile
  - `3` - Unfriendly
  - `4` - Neutral
  - `5` - Friendly
  - `6` - Honored
  - `7` - Revered
  - `8` - Exalted
- `barMin` - The minimum value of the reputation bar at the given standing (`number`)
- `barMax` - The maximum value of the reputation bar at the given standing (`number`)
- `barValue` - The player's current reputation with the faction (`number`)
- `atWarWith` - 1 if the player is at war with the given faction, otherwise nil (`1nil`)
- `canToggleAtWar` - 1 if the player can declare war with the given faction, otherwise nil (`1nil`)
- `isHeader` - 1 if the index refers to a faction group header (`1nil`)
- `isCollapsed` - 1 if the index refers to a faction group header and currently collapsed (`1nil`)
- `hasRep` - 1 if the index refers to a faction group header whose reputation value should be displayed (`1nil`)
- `isWatched` - 1 if the faction is currently being watched (i.e. displayed above the experience bar) (`1nil`)
- `isChild` - 1 if the index refers to a faction sub-group header within another group, or to an individual faction within a sub-group (`1nil`)

---

## GetInstanceLockTimeRemainingEncounter

This function is not yet documented

---

## GetLFDChoiceCollapseState

This function is not yet documented

---

## GetLFDChoiceEnabledState

This function is not yet documented

---

## GetLFDChoiceInfo

This function is not yet documented

---

## GetLFDChoiceLockedState

This function is not yet documented

---

## GetLFDChoiceOrder

This function is not yet documented

---

## GetLFDLockInfo

This function is not yet documented

---

## GetLFDLockPlayerCount

This function is not yet documented

---

## GetLFGBootProposal

This function is not yet documented

---

## GetLFGCompletionReward

Returns the various rewards for a completed LFG dungeon

**Signature:**

```lua
name, typeID, textureFilename, moneyBase, moneyVar, experienceBase, experienceVar, numStrangers, numRewards = GetLFGCompletionReward()
```

**Returns:**

- `name` - Name of the instance (`string`)
- `typeID` - Type of the dungeon (TYPEID*DUNGEON, TYPEID*HEROIC*DIFFICULTY, TYPEID*RANDOM_DUNGEON) (`number`)
- `textureFilename` - Filename of the instance icon (to be used with 'Interface/LFGFrame/LFGIcon-' (`string`)
- `moneyBase` - Base amount of money (moneyAmount = moneyBase + moneyVar * numStrangers) (`number`)
- `moneyVar` - Money reward coefficient (`number`)
- `experienceBase` - Base amount of experience (experienceGained = experienceBase + experienceVar * numStrangers) (`number`)
- `experienceVar` - Experience reward coefficient (`number`)
- `numStrangers` - Amount of pickups in the group (`number`)
- `numRewards` - Amount of actual dungeon rewards (currency or item) (`number`)

---

## GetLFGCompletionRewardItem

This function is not yet documented

---

## GetLFGDeserterExpiration

This function is not yet documented

---

## GetLFGDungeonInfo

This function is not yet documented

---

## GetLFGDungeonRewardInfo

This function is not yet documented

---

## GetLFGDungeonRewardLink

This function is not yet documented

---

## GetLFGDungeonRewards

This function is not yet documented

---

## GetLFGInfoLocal

This function is not yet documented

---

## GetLFGInfoServer

This function is not yet documented

---

## GetLFGProposal

Returns info about the currently pending LFD operation

**Signature:**

```lua
GetLFGProposal()
```

---

## GetLFGProposalEncounter

This function is not yet documented

---

## GetLFGProposalMember

This function is not yet documented

---

## GetLFGQueueStats

This function is not yet documented

---

## GetLFGQueuedList

This function is not yet documented

---

## GetLFGRandomCooldownExpiration

This function is not yet documented

---

## GetLFGRandomDungeonInfo

This function is not yet documented

---

## GetLFGRoleUpdate

This function is not yet documented

---

## GetLFGRoleUpdateMember

This function is not yet documented

---

## GetLFGRoleUpdateSlot

This function is not yet documented

---

## GetLFRChoiceOrder

This function is not yet documented

---

## GetLastQueueStatusIndex

This function is not yet documented

---

## GetMultiCastBarOffset

This function is not yet documented

---

## GetMultiCastTotemSpells

This function is not yet documented

---

## GetNextCompleatedTutorial

This function is not yet documented

---

## GetNumQuestItemDrops

This function is not yet documented

---

## GetNumQuestLogRewardFactions

This function is not yet documented

---

## GetNumRandomDungeons

This function is not yet documented

---

## GetPartyLFGBackfillInfo

This function is not yet documented

---

## GetPetSpellBonusDamage

This function is not yet documented

---

## GetPrevCompleatedTutorial

This function is not yet documented

---

## GetQuestLogItemDrop

This function is not yet documented

---

## GetQuestLogRewardArenaPoints

This function is not yet documented

---

## GetQuestLogRewardFactionInfo

This function is not yet documented

---

## GetQuestLogRewardXP

Returns the experience reward at the player's level for the selected quest in the quest log

**Signature:**

```lua
experience = GetQuestLogRewardXP()
```

**Returns:**

- `experience` - Amount of experience rewarded for completing the quest (`number`)

---

## GetQuestPOILeaderBoard

This function is not yet documented

---

## GetQuestSortIndex

This function is not yet documented

---

## GetQuestWatchIndex

Returns the quest watch (objective tracker) index of a quest in the quest log

**Signature:**

```lua
questWatchIndex = GetQuestWatchIndex(questLogIndex)
```

**Arguments:**

- `questLogIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumQuestLogEntries)) (`number`)

**Returns:**

- `questWatchIndex` - Index of a quest in the list of quests on the objectives tracker (between 1 and [`GetNumQuestWatches()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumQuestWatches)) (`number`)

---

## GetQuestWorldMapAreaID

This function is not yet documented

---

## GetRaidDifficulty

This function is not yet documented

---

## GetRandomBGHonorCurrencyBonuses

This function is not yet documented

---

## GetRandomDungeonBestChoice

Returns the dungeonID of the random dungeon group that provides the best loot for the player.. The dungeonID that is returned refers to an integer found in LFGDungeons.dbc.

This function is normally used only for initialization of the LFGQueueFrame in FrameXML LFDFrame.lua. You can programatically join the suggested queue for a random dungeon for which your character is eligible.

**Signature:**

```lua
GetRandomDungeonBestChoice()
```

---

## GetRewardArenaPoints

Returns the amount of arena points awarded when completing a quest.

Only valid when the questgiver UI is showing the accept/decline or completion stages of a quest dialog (between the `QUEST_DETAIL` and `QUEST_FINISHED` events, or between the `QUEST_COMPLETE` and `QUEST_FINISHED `events); otherwise may return zero or a value from the most recently displayed quest.

Unused as of 3.3.3, as no quest rewards arena points since the Call to Arms quests have been removed.

**Signature:**

```lua
arenaPoints = GetRewardArenaPoints()
```

**Returns:**

- `arenaPoints` - The arena points to be awarded (`number`)

---

## GetVehicleUIIndicator

This function is not yet documented

---

## GetVehicleUIIndicatorSeat

This function is not yet documented

---

## HasCompletedAnyAchievement

Checks if the player has completed at least 1 achievement. Used to determine whether or not the achievements frame should be loaded, and if the Achievements button on the micro menu should be enabled or not.

**Signature:**

```lua
state = HasCompletedAnyAchievement()
```

**Returns:**

- `state` - 1 if the player has completed at least one achievement, nil otherwise. (`boolean`)

---

## HasLFGRestrictions

This function is not yet documented

---

## IsBNLogin

This function is not yet documented

---

## IsInLFGDungeon

This function is not yet documented

---

## IsLFGDungeonJoinable

This function is not yet documented

---

## IsListedInLFR

Returns whether the player is currently listed in the Raid Browser

**Signature:**

```lua
listedInLFR = IsListedInLFR()
```

**Returns:**

- `listedInLFR` - `true` if the player is listed in the raid browser; otherwise `false` (`boolean`)

---

## IsPartyLFG

This function is not yet documented

---

## IsPetAttackAction

This function is not yet documented

---

## IsTutorialFlagged

This function is not yet documented

---

## IsZoomOutAvailable

This function is not yet documented

---

## JoinLFG

This function is not yet documented

---

## LeaveLFG

Leave the LFG queue.

**Signature:**

```lua
LeaveLFG()
```

---

## PartyLFGStartBackfill

This function is not yet documented

---

## ProcessQuestLogRewardFactions

This function is not yet documented

---

## QuestIsDaily

This function is not yet documented

---

## QuestIsWeekly

This function is not yet documented

---

## QuestMapUpdateAllQuests

This function is not yet documented

---

## QuestPOIGetIconInfo

Returns information about a QuestPOI icon. Only works if the quest is displayed on the world map.
Only returns the nearest of these points if there are more than one.

**Signature:**

```lua
_, posX, posY, objective = QuestPOIGetIconInfo(questID)
```

**Arguments:**

- `questID` - The quest index to query (`number`)

**Returns:**

- `_` - Undocumented in Blizzard code (`unknown`)
- `posX` - The x coordinate offset for the given POI (`number`)
- `posY` - The y coordinate offset for the given POI (`number`)
- `objective` - The objective number for the given POI (`number`)

---

## QuestPOIGetQuestIDByIndex

This function is not yet documented

---

## QuestPOIGetQuestIDByVisibleIndex

This function is not yet documented

---

## QuestPOIUpdateIcons

This function is not yet documented

---

## QuestPOIUpdateTexture

This function is not yet documented

---

## RefreshLFGList

This function is not yet documented

---

## RegisterStaticConstants

This function is not yet documented

---

## RejectProposal

Rejects a LFG dungeon invite.

**Signature:**

```lua
RejectProposal()
```

---

## RequestLFDPartyLockInfo

This function is not yet documented

---

## RequestLFDPlayerLockInfo

Requests instance lockout and Call to Arms dungeon reward information.. When called the server will update the client on instance lockout and Call to Arms. The API will then return updated values instead of old once.

Once [`LFG_UPDATE_RANDOM_INFO`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LFG_UPDATE_RANDOM_INFO) event is received it means that updated Call to Arms data is finally available for the client.

**Signature:**

```lua
RequestLFDPlayerLockInfo()
```

---

## RespondMailLockSendItem

This function is not yet documented

---

## SearchLFGGetEncounterResults

This function is not yet documented

---

## SearchLFGGetJoinedID

This function is not yet documented

---

## SearchLFGGetNumResults

This function is not yet documented

---

## SearchLFGGetPartyResults

This function is not yet documented

---

## SearchLFGGetResults

This function is not yet documented

---

## SearchLFGJoin

This function is not yet documented

---

## SearchLFGLeave

This function is not yet documented

---

## SearchLFGSort

This function is not yet documented

---

## SendSystemMessage

This function is not yet documented

---

## SetAllowLowLevelRaid

Enabling this if your character is below level 10 will allow you to join a raid group.

**Signature:**

```lua
SetAllowLowLevelRaid(enable)
```

**Arguments:**

- `enable` - 1 to enable low level raids for this character, nil otherwise. (`boolean`)

---

## SetAuctionsTabShowing

This function is not yet documented

---

## SetChatColorNameByClass

Sets whether the player names should be colored by class for a given chat type

**Signature:**

```lua
SetChatColorNameByClass("chatType", colorByName)
```

**Arguments:**

- `chatType` - The chatType that is being set. This value of this is the same as the index of the global `ChatTypeInfo` table. (`string`)
- `colorByName` - Whether or not names should be colored by class for the given chat type. (`boolean`)

---

## SetChatWindowSavedDimensions

This function is not yet documented

---

## SetChatWindowSavedPosition

This function is not yet documented

---

## SetLFGBootVote

This function is not yet documented

---

## SetLFGDungeon

Sets a flag indicating that the player would like to join a given dungeon/queue. This function simply indicates that the player would like to join a given dungeon or queue. Joining the queue is accomplished using the [`JoinLFG()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/JoinLFG) function. Clearing the dungeons that have been flagged is accomplished using the [`ClearAllLFGDungeons`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ClearAllLFGDungeons) function.

**Signature:**

```lua
SetLFGDungeon(queueIndex)
```

**Arguments:**

- `queueIndex` - A numeric identifier for the dungeon/queue being joined. For random queues this can be obtained using `/dump LFDQueueFrame.type` (`number`)

---

## SetLFGDungeonEnabled

This function is not yet documented

---

## SetLFGHeaderCollapsed

This function is not yet documented

---

## SetMapByID

Sets the map based on a specified ID. For example, if you are an Undead character in the starting area, which is map ID 21, you can open your map and run SetMapByID(22) to change it to Western Plaguelands. In fact, you can run that anywhere If you are a fresh undead in tirisfal glades(MapAreaID:21), you get your map out, then you use SetMapByID(22) it will change to WPL

**Signature:**

```lua
SetMapByID(id)
```

**Arguments:**

- `id` - The unique numeric map ID, can be obtained from `GetCurrentMapAreaID()` (`number`)

---

## SetPOIIconOverlapDistance

This function is not yet documented

---

## SetPOIIconOverlapPushDistance

This function is not yet documented

---

## SetSavedInstanceExtend

This function is not yet documented

---

## ShiftQuestWatches

This function is not yet documented

---

## SortBGList

This function is not yet documented

---

## SortQuestWatches

Sorts the quests listed in the watch frame based on the set criteria

**Signature:**

```lua
changed = SortQuestWatches()
```

**Returns:**

- `changed` - `true` if the quest watches were re-ordered during the sort, otherwise `false` (`boolean`)

---

## Stopwatch_Clear

This function is not yet documented

---

## Stopwatch_FinishCountdown

This function is not yet documented

---

## Stopwatch_IsPlaying

Returns True/False if Stop Watch is running.

**Signature:**

```lua
isPlaying = Stopwatch_IsPlaying()
```

**Returns:**

- `isPlaying` - Returns true/false depending on if the Stop Watch is currently counting Down/Up (`boolean`)

---

## Stopwatch_Pause

This function is not yet documented

---

## Stopwatch_Play

This function is not yet documented

---

## Stopwatch_StartCountdown

Sets the Stop Watches timer value

**Signature:**

```lua
Stopwatch_StartCountdown(hours, minutes, seconds)
```

**Arguments:**

- `hours` - Sets the amount of hours the Stop Watch will run (`integer`)
- `minutes` - Sets the amount of minutes the Stop Watch will run (`integer`)
- `seconds` - Sets the amount of seconds the Stop Watch will run (`integer`)

---

## Stopwatch_Toggle

Toggles visibility of the StopwatchFrame

**Signature:**

```lua
Stopwatch_Toggle()
```

---

## TriggerTutorial

This function is not yet documented

---

## UnitGroupRolesAssigned

Returns information about a unit's role in a group

**Signature:**

```lua
role = UnitGroupRolesAssigned("unit")
```

**Arguments:**

- `unit` - Unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `role` - Returns the unit's role (`string`)
  - `DAMAGER`
  - `HEALER`
  - `NONE`
  - `TANK`

---

## UnitHasLFGDeserter

This function is not yet documented

---

## UnitHasLFGRandomCooldown

This function is not yet documented

---

## debughook

This function is not yet documented

---

← [WoW API Docs](../index.md)
