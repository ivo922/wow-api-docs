# NPC "Gossip" Dialog functions

← [WoW API Docs](../index.md)

**11** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#gossip)

---

## CloseGossip

Ends an NPC "gossip" interaction. Causes the [`GOSSIP_CLOSED`](../events/GOSSIP_CLOSED.md) event to fire, indicating that Gossip APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseGossip()
```

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

## GetGossipOptions

Returns a list of interaction options for the Gossip NPC

**Signature:**

```lua
text, gossipType, ... = GetGossipOptions()
```

**Returns:**

- `text` - Text to be displayed for the gossip option (`string`)
- `gossipType` - Non-localized string indicating the type of gossip option (`string`)
  - `Banker` - Begin a Bank interaction
  - `BattleMaster` - Queue for a battleground instance
  - `Binder` - Set the player's Hearthstone location
  - `Gossip` - Talk to the NPC
  - `Tabard` - Begin a Tabard design interaction
  - `Taxi` - Begin a Taxi (flight master) interaction
  - `Trainer` - Begin a Trainer interaction
  - `Vendor` - Begin a Merchant interaction
- `...` - Additional `text, gossipType` values for each gossip option available (`list`)

---

## GetGossipText

Returns greeting or other text to be displayed in an NPC dialog

**Signature:**

```lua
text = GetGossipText()
```

**Returns:**

- `text` - Text to be displayed for the NPC conversation (`string`)

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

## GetNumGossipOptions

Returns the number of non-quest dialog options for the current Gossip NPC. Used by the default UI to skip greeting gossip for NPCs which provide only a greeting and one gossip option leading to the NPC's main interaction type (e.g. flight masters, merchants).

**Signature:**

```lua
numOptions = GetNumGossipOptions()
```

**Returns:**

- `numOptions` - Number of options available from the current Gossip NPC (`number`)

---

## SelectGossipActiveQuest

Chooses a quest which can be turned in to the current Gossip NPC. Causes the [`QUEST_PROGRESS`](../events/QUEST_PROGRESS.md) event to fire, in which it is determined whether the player can complete the quest.

**Signature:**

```lua
SelectGossipActiveQuest(index)
```

**Arguments:**

- `index` - Index of a quest which can be turned in to the current Gossip NPC (between 1 and [`GetNumGossipActiveQuests()`](NPC Gossip Dialog.md#getnumgossipactivequests)) (`number`)

---

## SelectGossipAvailableQuest

Chooses a quest available from the current Gossip NPC. Usable after a [`QUEST_GREETING`](../events/QUEST_GREETING.md) event. Causes the [`QUEST_DETAIL`](../events/QUEST_DETAIL.md) event to fire, in which the questgiver presents the player with the details of a quest and the option to accept or decline.

**Signature:**

```lua
SelectGossipAvailableQuest(index)
```

**Arguments:**

- `index` - Index of a quest available from the current Gossip NPC (between 1 and [`GetNumGossipAvailableQuests()`](NPC Gossip Dialog.md#getnumgossipavailablequests)) (`number`)

---

## SelectGossipOption

Chooses and activates an NPC dialog option. Results may vary according to the gossip option chosen; may end the gossip (firing a [`GOSSIP_CLOSED`](../events/GOSSIP_CLOSED.md) event) and start another interaction (firing a [`MERCHANT_SHOW`](../events/MERCHANT_SHOW.md), [`TRAINER_SHOW`](../events/TRAINER_SHOW.md), [`TAXIMAP_OPENED`](../events/TAXIMAP_OPENED.md), or similar event) or may continue the gossip with new text and new options (firing another [`GOSSIP_SHOW`](../events/GOSSIP_SHOW.md) event).

Calling this function with only the first argument may cause the [`GOSSIP_CONFIRM`](../events/GOSSIP_CONFIRM.md) event to fire, indicating that the player needs to provide confirmation (or additional information) before the option will be activated. Confirmation is needed for certain options requiring the character to spend (e.g. when activating Dual Talent Specialization); additional information is needed for options such as those used when redeeming a Loot Card code from the WoW trading card game to receive an in-game item. In either case, the confirmation and additional information can be provided (as by the popup dialog in the default UI) by calling this function again with all three arguments.

**Signature:**

```lua
SelectGossipOption(index [, "text" [, confirm]])
```

**Arguments:**

- `index` - The option in the NPC gossip window to select, from 1 to GetNumGossipOptions() (`number`)
- `text` - Text to include when confirming the selection (`string`)
- `confirm` - true to confirm the selection; false or omitted otherwise (`boolean`)

---

← [WoW API Docs](../index.md)
