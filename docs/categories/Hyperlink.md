# Hyperlink functions

← [WoW API Docs](../index.md)

**30** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#hyperlink)

---

## GetAchievementLink

Returns a hyperlink representing the player's progress on an achievement.

The tooltip associated with the hyperlink shows not only the details of the achievement itself, but also the completion of or progress towards the achievement by the player who produced the link.

**Signature:**

```lua
link = GetAchievementLink(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

**Returns:**

- `link` - A hyperlink for the player's achievement (`string`)

---

## GetAuctionItemLink

Returns a hyperlink for an item in an auction listing

**Signature:**

```lua
link = GetAuctionItemLink("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`)
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetBuybackItemLink

Returns a hyperlink for an item recently sold to a vendor and available to be repurchased

**Signature:**

```lua
link = GetBuybackItemLink(index)
```

**Arguments:**

- `index` - Index of an item in the buyback listing (between 1 and [`GetNumBuybackItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumBuybackItems)) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetContainerItemLink

Returns a hyperlink for an item in the player's bags

**Signature:**

```lua
link = GetContainerItemLink(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerID))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#containerSlotID))

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetCursorInfo

Returns information about the contents of the cursor

**Signature:**

```lua
type, data, subType = GetCursorInfo()
```

**Returns:**

- `type` - Type of data attached to the cursor (`string`)
  - `companion`
  - `equipmentset`
  - `guildbankmoney`
  - `item`
  - `macro`
  - `merchant`
  - `money`
  - `spell`
- `data` - Identifier for the data on the cursor; varies by type: (`value`)
  - `companion` - Index of the companion in the non-combat pet or mount list (`number`)
  - `equipmentset` - Name of the equipment set (`string`)
  - `guildbankmoney` - Amount of the money from the guild bank (in copper) (`number`)
  - `item` - Numeric identifier for the item (`number`, [`itemID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemID))
  - `macro` - Index of the macro in the macro listing (`number`, [`macroID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
  - `merchant` - Index of the item in the vendor's listings (`number`)
  - `money` - Amount of the player's money (in copper) (`number`)
  - `spell` - Index of the spell in the player's spellbook (`number`, [`spellbookID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#spellbookID))
- `subType` - Secondary identifier for the data on the cursor; used only for certain types: (`string`)
  - `companion` - `"CRITTER"` or `"MOUNT"`, indicating whether the returned `data` is an index in the non-combat pet or mount list
  - `item` - A complete [`hyperlink`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink) for the item
  - `spell` - `"spell"` or `"pet"`, indicating whether the returned `data` is an index in the player's or pet's spellbook

---

## GetExistingSocketLink

Returns a hyperlink for a permanently socketed gem. If the given socket contains a permanently socketed gem, returns an item link for that gem (even if a new gem has been dropped in the socket to overwrite the existing gem, but has not yet been confirmed). If the socket is empty, returns `nil`.

Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/SOCKET_INFO_UPDATE) and [`SOCKET_INFO_CLOSE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/SOCKET_INFO_CLOSE) events).

**Signature:**

```lua
link = GetExistingSocketLink(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumSockets)) (`number`)

**Returns:**

- `link` - A hyperlink for the socketed gem (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetGlyphLink

Gets a hyperlink for the contents of a glyph socket.

Glyph links are distinct from item and spell links: e.g. "|cff66bbff|Hglyph:21:361|h[Glyph of Hunter's Mark]|h|r".

**Signature:**

```lua
link = GetGlyphLink(socket, talentGroup)
```

**Arguments:**

- `socket` - Which glyph socket to query (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#glyphIndex))
- `talentGroup` - Which set of glyphs to query, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `link` - A hyperlink for the glyph socket's contents, or "" if the socket is empty (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetGuildBankItemLink

Returns a hyperlink for an item in the guild bank

**Signature:**

```lua
item = GetGuildBankItemLink(tab, slot)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `slot` - Index of an item slot in the guild bank tab (between 1 and `MAX_GUILDBANK_SLOTS_PER_TAB`) (`number`)

**Returns:**

- `item` - A hyperlink for the contents of the slot (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetGuildBankTransaction

Returns information about a transaction in the log for a guild bank tab. Only returns valid information following the [`GUILDBANKLOG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/GUILDBANKLOG_UPDATE) event which fires after calling [`QueryGuildBankLog()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/QueryGuildBankLog).

**Signature:**

```lua
type, name, itemLink, count, tab1, tab2, year, month, day, hour = GetGuildBankTransaction(tab, index)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `index` - Index of a log entry (between 1 and [`GetNumGuildBankTransactions(tab)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTransactions)) (`number`)

**Returns:**

- `type` - Type of transaction (`string`)
  - `deposit`
  - `move`
  - `repair`
  - `withdraw`
- `name` - Name of the guild member responsible for the transaction (`string`)
- `itemLink` - A hyperlink for the item involved in the transaction (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))
- `count` - Number of stacked items involved in the transaction (`number`)
- `tab1` - Index of the source tab, if the item was moved between tabs (`number`)
- `tab2` - Index of the destination tab, if the item was moved between tabs (`number`)
- `year` - Number of years since the event occurred (`number`)
- `month` - Number of months since the event occurred (`number`)
- `day` - Number of days since the event occurred (`number`)
- `hour` - Number of hours since the event occurred (`number`)

---

## GetInboxItemLink

Returns a hyperlink for an item attached to a mail in the player's inbox

**Signature:**

```lua
itemlink = GetInboxItemLink(mailID, attachmentIndex)
```

**Arguments:**

- `mailID` - Index of a mail in the player's inbox (between 1 and [`GetInboxNumItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInboxNumItems)) (`number`)
- `attachmentIndex` - Index of an attachment to the mail (between 1 and `ATTACHMENTS_MAX_RECEIVE`) (`number`)

**Returns:**

- `itemlink` - A hyperlink for the attachment item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetInventoryItemLink

Returns an item link for an equipped item

**Signature:**

```lua
link = GetInventoryItemLink("unit", slot)
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInventorySlotInfo) (`number`, [inventoryID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#inventoryID))

**Returns:**

- `link` - An item link for the given item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetItemGem

Returns information about gems socketed in an item

**Signature:**

```lua
name, link = GetItemGem(itemID, index) or GetItemGem("itemName", index) or GetItemGem("itemLink", index)
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemString) portion of an item link (`string`)
- `index` - Index of a socket on the item (`number`)

**Returns:**

- `name` - Name of the gem in the socket (`string`)
- `link` - A hyperlink for the gem in the socket (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetLootRollItemLink

Returns a hyperlink for an item currently up for loot rolling

**Signature:**

```lua
link = GetLootRollItemLink(id)
```

**Arguments:**

- `id` - Index of an item currently up for loot rolling (as provided in the [`START_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/START_LOOT_ROLL) event) (`number`)

**Returns:**

- `link` - A hyperlink for the loot roll item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetLootSlotLink

Returns a hyperlink for an item available as loot. Returns nil if the loot slot is empty or contains money.

**Signature:**

```lua
link = GetLootSlotLink(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`)

---

## GetMacroItem

Returns information about the item used by a macro. If a macro contains conditional, random, or sequence commands, this function returns the item which would currently be used if the macro were run.

**Signature:**

```lua
name, link = GetMacroItem(index) or GetMacroItem("name")
```

**Arguments:**

- `index` - Index of a macro (`number`, [macroID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#macroID))
- `name` - Name of a macro (`string`)

**Returns:**

- `name` - Name of the item (`string`)
- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetMerchantItemLink

Returns a hyperlink for an item available for purchase from a vendor

**Signature:**

```lua
link = GetMerchantItemLink(index)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMerchantNumItems)) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetNewSocketLink

Returns a hyperlink for a gem added to a socket. If the given socket contains a new gem (one that has been placed in the UI, but not yet confirmed for permanently socketing into the item), returns an item link for that gem. If the socket is empty or has a permanently socketed gem but no new gem, returns `nil`.

Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/SOCKET_INFO_UPDATE) and [`SOCKET_INFO_CLOSE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/SOCKET_INFO_CLOSE) events).

**Signature:**

```lua
link = GetNewSocketLink(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumSockets)) (`number`)

**Returns:**

- `link` - A hyperlink for the gem added to the socket (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

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

- `questIndex` - Index of a quest in the quest log (between 1 and [`GetNumQuestLogEntries()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumQuestLogEntries)) (`number`)

**Returns:**

- `link` - A hyperlink for the quest (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

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

## GetSendMailItemLink

Returns a hyperlink for an item attached to the outgoing message

**Signature:**

```lua
itemlink = GetSendMailItemLink(slot)
```

**Arguments:**

- `slot` - Index of an outgoing attachment slot (between 1 and `ATTACHMENTS_MAX_SEND`) (`number`)

**Returns:**

- `itemlink` - A hyperlink for the attachment item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

**Examples:**

```lua
-- Scan all the send mail item slots, printing a link for each item
for slot=1,ATTACHMENTS_MAX_SEND do
  local link = GetSendMailItemLink(slot)
  if link then
    print("Item " .. link .. " is in slot " .. slot)
  end
end
```

---

## GetSpellLink

Returns a hyperlink for a spell

**Signature:**

```lua
link, tradeLink = GetSpellLink(index, "bookType") or GetSpellLink("name") or GetSpellLink(id)
```

**Arguments:**

- `index` - Index of a spell in the spellbook (`number`, [spellbookID](https://web.archive.org/web/20100823090329/http://wowprogramming.com/docs/api_types#spellbookID))
- `bookType` - Type of spellbook (`string`)
  - `pet` - The pet's spellbook
  - `spell` - The player's spellbook
- `name` - Name of a spell, optionally including secondary text (e.g. "Mana Burn" to find the player's highest rank, or "Mana Burn(Rank 2)" -- no space before the parenthesis -- for a specific rank) (`string`)
- `id` - Numeric ID of a spell (`number`, [spellID](https://web.archive.org/web/20100823090329/http://wowprogramming.com/docs/api_types#spellID))

**Returns:**

- `link` - A hyperlink for the spell (`string`, [hyperlink](https://web.archive.org/web/20100823090329/http://wowprogramming.com/docs/api_types#hyperlink))
- `tradeLink` - A hyperlink representing the player's list of trade skill recipes, if the spell is a trade skill (i.e. if "casting" the spell opens a trade skill window) (`string`)

---

## GetTalentLink

Returns a hyperlink for a talent

**Signature:**

```lua
link = GetTalentLink(tabIndex, talentIndex, inspect, pet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100105230815/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100105230815/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `link` - A hyperlink representing the talent and the number of points spent in it (`string`, [hyperlink](https://web.archive.org/web/20100105230815/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetTradePlayerItemLink

Returns a hyperlink for an item offered for trade by the player

**Signature:**

```lua
link = GetTradePlayerItemLink(index)
```

**Arguments:**

- `index` - Index of an item offered for trade by the player (between 1 and `MAX_TRADE_ITEMS`) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetTradeSkillItemLink

Returns a hyperlink for the item created by a tradeskill recipe. The tooltip produced when resolving the link describes only the item created by the recipe. For a link which describes the recipe itself (its reagents and description), see [`GetTradeSkillRecipeLink()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTradeSkillRecipeLink).

If the recipe does not create an item, this function returns the same hyperlink as does [`GetTradeSkillRecipeLink()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTradeSkillRecipeLink) (though the text of the link may differ).

**Signature:**

```lua
link = GetTradeSkillItemLink(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTradeSkills)) (`number`)

**Returns:**

- `link` - A hyperlink for the item created by the recipe (`string`)

---

## GetTradeSkillListLink

Returns a hyperlink to the player's list of recipes for the current trade skill

**Signature:**

```lua
link = GetTradeSkillListLink()
```

**Returns:**

- `link` - A hyperlink other players can resolve to see the player's full list of tradeskill recipes (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetTradeSkillReagentItemLink

Returns a hyperlink for a reagent in a tradeskill recipe

**Signature:**

```lua
link = GetTradeSkillReagentItemLink(skillIndex, reagentIndex)
```

**Arguments:**

- `skillIndex` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTradeSkills)) (`number`)
- `reagentIndex` - Index of a reagent in the recipe (between 1 and [`GetTradeSkillNumReagents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTradeSkillNumReagents)) (`number`)

**Returns:**

- `link` - A hyperlink for the reagent item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetTradeSkillRecipeLink

Returns hyperlink for a tradeskill recipe. The tooltip produced when resolving the link describes the recipe itself -- its reagents and (if present) description -- in addition to (if applicable) the item created. For a link which only describes the created item, see [`GetTradeSkillItemLink()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTradeSkillItemLink).

**Signature:**

```lua
link = GetTradeSkillRecipeLink(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTradeSkills)) (`number`)

**Returns:**

- `link` - A hyperlink for the trade skill recipe (`string`)

---

## GetTradeTargetItemLink

Returns a hyperlink for an item offered for trade by the target

**Signature:**

```lua
link = GetTradeTargetItemLink(index)
```

**Arguments:**

- `index` - Index of an item offered for trade by the target (between 1 and `MAX_TRADE_ITEMS`) (`number`)

**Returns:**

- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

## GetTrainerServiceItemLink

Returns a hyperlink for the item associated with a trainer service. Currently only returns item links for trainer services which teach trade skill recipes which produce items; does not return spell or recipe links.

**Signature:**

```lua
link = GetTrainerServiceItemLink(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTrainerServices)) (`number`)

**Returns:**

- `link` - A hyperlink for the item associated with a trainer service (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

← [WoW API Docs](../index.md)
