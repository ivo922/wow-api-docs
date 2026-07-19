# Tradeskill functions

← [WoW API Docs](../index.md)

**36** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#tradeskill)

---

## CloseTradeSkill

Ends interaction with the Trade Skill UI. Fires the [`TRADE_SKILL_CLOSE`](../events/TRADE_SKILL_CLOSE.md) event, indicating that TradeSkill APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseTradeSkill()
```

---

## CollapseTradeSkillSubClass

Collapses a group header in the trade skill listing. Causes an error if `index` does not refer to a header.

**Signature:**

```lua
CollapseTradeSkillSubClass(index)
```

**Arguments:**

- `index` - Index of a header in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

---

## DoTradeSkill

Performs a trade skill recipe

**Signature:**

```lua
DoTradeSkill(index [, repeat])
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)
- `repeat` - Number of times to repeat the recipe (`number`)

---

## ExpandTradeSkillSubClass

Expands a group header in the trade skill listing. Causes an error if `index` does not refer to a header.

**Signature:**

```lua
ExpandTradeSkillSubClass(index)
```

**Arguments:**

- `index` - Index of a header in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

---

## GetFirstTradeSkill

Returns the index of the first non-header in the trade skill listing

**Signature:**

```lua
index = GetFirstTradeSkill()
```

**Returns:**

- `index` - Index of the first trade skill recipe (as opposed to group headers) (`number`)

---

## GetNumTradeSkills

Returns the number of entries in the trade skill listing. Entries include both group headers and individual trade skill recipes. Reflects the list as it should currently be displayed, not necessarily the complete list -- if headers are collapsed or a filter is enabled, a smaller number will be returned.

Returns 0 if a trade skill is not "open".

**Signature:**

```lua
numSkills = GetNumTradeSkills()
```

**Returns:**

- `numSkills` - Number of headers and recipes to display in the trade skill list (`number`)

---

## GetTradeSkillCooldown

Returns the time remaining on a trade skill recipe's cooldown

**Signature:**

```lua
cooldown = GetTradeSkillCooldown(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `cooldown` - Time remaining before the recipe can be performed again (in seconds), or nil if the recipe is currently available or has no cooldown (`number`)

---

## GetTradeSkillDescription

Returns descriptive text for a tradeskill recipe. Most recipes that create items don't provide descriptive text; it's more often used for enchants and special recipes such as inscription or alchemy research.

**Signature:**

```lua
description = GetTradeSkillDescription(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `description` - Descriptive text for the tradeskill recipe, or nil if no text is associated with the recipe (`string`)

---

## GetTradeSkillIcon

Returns the icon for a trade skill recipe. For recipes which create an item, this is generally the icon of the item created; for other recipes (such as enchants and alchemy/inscription research) a generic icon is used.

**Signature:**

```lua
texturePath = GetTradeSkillIcon(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `texturePath` - Path to an icon texture for the recipe (`string`)

---

## GetTradeSkillInfo

Returns information about a trade skill header or recipe

**Signature:**

```lua
skillName, skillType, numAvailable, isExpanded, serviceType = GetTradeSkillInfo(index)
```

**Arguments:**

- `index` - Index of an entry in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `skillName` - Name of the entry (`string`)
- `skillType` - Indicates whether the entry is a header or recipe and difficulty of recipes (`string`)
  - `easy` - Low chance for the player to gain skill by performing the recipe (displayed as green in the default UI
  - `header` - This entry is a header and not an actual trade skill recipe
  - `medium` - Moderate chance for the player to gain skill by performing the recipe (displayed as yellow in the default UI
  - `optimal` - High chance for the player to gain skill by performing the recipe (displayed as orange in the default UI
  - `trivial` - No chance for the player to gain skill by performing the recipe (displayed as gray in the default UI
- `numAvailable` - Number of times the player can repeat the recipe given available reagents (`number`)
- `isExpanded` - 1 if the entry is a header and is expanded; otherwise nil (`1nil`)
- `serviceType` - Indicates what type of service the recipe provides (items, enhancements,...) (`string`)
  - `Emboss` - Applies an emboss (letherworkers)
  - `Embrodier` - Applies an embroider (tailors)
  - `Enchant` - Applies an enchant (enchanters)
  - `Engrave` - Engraves a rune (runeforging)
  - `Inscribe` - Puts an inscription (scribers)
  - `Modify` - Puts a socket (blacksmiths)
  - `Tinker` - Puts a device like webbing or flexweave (engineers)
  - `nil` - Produces an item

---

## GetTradeSkillInvSlotFilter

Returns whether the trade skill listing is filtered by a given item equipment slot

**Signature:**

```lua
enabled = GetTradeSkillInvSlotFilter(index)
```

**Arguments:**

- `index` - Index of an item equipment slot (in the list returned by [`GetTradeSkillInvSlots()`](Tradeskill.md#gettradeskillinvslots)), or `0` for the "All" filter (`number`)

**Returns:**

- `enabled` - 1 if the filter is enabled; otherwise nil (`1nil`)

---

## GetTradeSkillInvSlots

Returns a list of recipe equipment slots for the current trade skill. These inventory types correspond to those of the items produced (see [`GetItemInfo()`](Item.md#getiteminfo) and [`GetAuctionItemInvTypes()`](Auction.md#getauctioninvtypes)) and can be used to filter the recipe list.

**Signature:**

```lua
... = GetTradeSkillInvSlots()
```

**Returns:**

- `...` - A list of strings, each the localized name of an inventory type applicable to the current trade skill listing (`list`)

---

## GetTradeSkillItemLevelFilter

Returns the current settings for filtering the trade skill listing by required level of items produced

**Signature:**

```lua
minLevel, maxLevel = GetTradeSkillItemLevelFilter()
```

**Returns:**

- `minLevel` - Lowest required level of items to show in the filtered list (`number`)
- `maxLevel` - Highest required level of items to show in the filtered list (`number`)

---

## GetTradeSkillItemLink

Returns a hyperlink for the item created by a tradeskill recipe. The tooltip produced when resolving the link describes only the item created by the recipe. For a link which describes the recipe itself (its reagents and description), see [`GetTradeSkillRecipeLink()`](Hyperlink.md#gettradeskillrecipelink).

If the recipe does not create an item, this function returns the same hyperlink as does [`GetTradeSkillRecipeLink()`](Hyperlink.md#gettradeskillrecipelink) (though the text of the link may differ).

**Signature:**

```lua
link = GetTradeSkillItemLink(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `link` - A hyperlink for the item created by the recipe (`string`)

---

## GetTradeSkillItemNameFilter

Returns the current search text for filtering the trade skill listing by name

**Signature:**

```lua
text = GetTradeSkillItemNameFilter()
```

**Returns:**

- `text` - Text to search for in recipe names, produced item names or descriptions, or reagents; nil if no search filter is in use (`string`)

---

## GetTradeSkillLine

Returns information about the current trade skill

**Signature:**

```lua
tradeskillName, rank, maxLevel = GetTradeSkillLine()
```

**Returns:**

- `tradeskillName` - Name of the trade skill, or "UNKNOWN" if no trade skill window is open (`string`)
- `rank` - The character's current rank in the trade skill (`number`)
- `maxLevel` - The character's current maximum rank in the trade skill (e.g. 300 for a character of Artisan status) (`number`)

---

## GetTradeSkillListLink

Returns a hyperlink to the player's list of recipes for the current trade skill

**Signature:**

```lua
link = GetTradeSkillListLink()
```

**Returns:**

- `link` - A hyperlink other players can resolve to see the player's full list of tradeskill recipes (`string`, [hyperlink](../types/hyperlink.md))

---

## GetTradeSkillNumMade

Returns the number of items created when performing a tradeskill recipe

**Signature:**

```lua
minMade, maxMade = GetTradeSkillNumMade(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `minMade` - Minimum number of items created when performing the recipe (`number`)
- `maxMade` - Maximum number of items created when performing the recipe (`number`)

---

## GetTradeSkillNumReagents

Returns the number of different reagents required for a trade skill recipe

**Signature:**

```lua
numReagents = GetTradeSkillNumReagents(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `numReagents` - Number of different reagents required for the recipe (`number`)

---

## GetTradeSkillReagentInfo

Returns information about a reagent in a trade skill recipe

**Signature:**

```lua
reagentName, reagentTexture, reagentCount, playerReagentCount = GetTradeSkillReagentInfo(skillIndex, reagentIndex)
```

**Arguments:**

- `skillIndex` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)
- `reagentIndex` - Index of a reagent in the recipe (between 1 and [`GetTradeSkillNumReagents()`](Tradeskill.md#gettradeskillnumreagents)) (`number`)

**Returns:**

- `reagentName` - Name of the reagent (`string`)
- `reagentTexture` - Path to an icon texture for the reagent (`string`)
- `reagentCount` - Quantity of the reagent required to perform the recipe (`number`)
- `playerReagentCount` - Quantity of the reagent in the player's possession (`number`)

---

## GetTradeSkillReagentItemLink

Returns a hyperlink for a reagent in a tradeskill recipe

**Signature:**

```lua
link = GetTradeSkillReagentItemLink(skillIndex, reagentIndex)
```

**Arguments:**

- `skillIndex` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)
- `reagentIndex` - Index of a reagent in the recipe (between 1 and [`GetTradeSkillNumReagents()`](Tradeskill.md#gettradeskillnumreagents)) (`number`)

**Returns:**

- `link` - A hyperlink for the reagent item (`string`, [hyperlink](../types/hyperlink.md))

---

## GetTradeSkillRecipeLink

Returns hyperlink for a tradeskill recipe. The tooltip produced when resolving the link describes the recipe itself -- its reagents and (if present) description -- in addition to (if applicable) the item created. For a link which only describes the created item, see [`GetTradeSkillItemLink()`](Hyperlink.md#gettradeskillitemlink).

**Signature:**

```lua
link = GetTradeSkillRecipeLink(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `link` - A hyperlink for the trade skill recipe (`string`)

---

## GetTradeSkillSelectionIndex

Returns the index of the currently selected trade skill recipe. Selection in the recipe list is used only for display in the default UI and has no effect on other Trade Skill APIs.

**Signature:**

```lua
index = GetTradeSkillSelectionIndex()
```

**Returns:**

- `index` - Index of the selected recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

---

## GetTradeSkillSubClassFilter

Returns whether the trade skill listing is filtered by a given item subclass

**Signature:**

```lua
enabled = GetTradeSkillSubClassFilter(index)
```

**Arguments:**

- `index` - Index of an item subclass (in the list returned by [`GetTradeSkillSubClasses()`](Tradeskill.md#gettradeskillsubclasses)), or `0` for the "All" filter (`number`)

**Returns:**

- `enabled` - 1 if the filter is enabled; otherwise nil (`1nil`)

---

## GetTradeSkillSubClasses

Returns a list of recipe subclasses for the current trade skill. These subclasses correspond to those of the items produced (see [`GetItemInfo()`](Item.md#getiteminfo) and [`GetAuctionItemSubClasses()`](Auction.md#getauctionitemsubclasses)) and can be used to filter the recipe list.

**Signature:**

```lua
... = GetTradeSkillSubClasses()
```

**Returns:**

- `...` - A list of strings, each the localized name of an item or recipe subclass applicable to the current trade skill listing (`list`)

---

## GetTradeSkillTools

Returns a list of required tools for a trade skill recipe. A tool may be an item (e.g. [Blacksmith Hammer](http://www.wowhead.com/?item=5956), [Virtuoso Inking Set](http://www.wowhead.com/?item=39505)) the player must possess, or a description of a generic (e.g. near an Anvil, in a Moonwell) or specific (e.g. Netherstorm, Emerald Dragonshrine) location to which the player must travel in order to perform the recipe. The `hasTool` return is only valid for the former.

**Signature:**

```lua
toolName, hasTool, ... = GetTradeSkillTools(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

**Returns:**

- `toolName` - Name of the required tool (`string`)
- `hasTool` - 1 if the tool is an item in the player's possession; otherwise nil (`1nil`)
- `...` - An additional `toolName, hasTool` pair for each tool required (`list`)

---

## GetTradeskillRepeatCount

Returns the number of times the trade skill recipe currently being performed will repeat. Returns 1 if a recipe is not being performed; after [`DoTradeSkill()`](Tradeskill.md#dotradeskill) is called, returns the number of repetitions queued (which decrements as each repetition is finished).

**Signature:**

```lua
repeatCount = GetTradeskillRepeatCount()
```

**Returns:**

- `repeatCount` - Number of times the current recipe will repeat (`number`)

---

## IsTradeSkillLinked

Returns whether the TradeSkill UI is showing another player's skill

**Signature:**

```lua
isLinked, name = IsTradeSkillLinked()
```

**Returns:**

- `isLinked` - 1 if the TradeSkill APIs currently reflect another character's tradeskill; nil if showing the player's tradeskill or if no skill is shown (`1nil`)
- `name` - If showing another character's skill, the name of that character (`string`)

---

## SelectTradeSkill

Selects a recipe in the trade skill listing. Selection in the recipe list is used only for display in the default UI and has no effect on other Trade Skill APIs.

**Signature:**

```lua
SelectTradeSkill(index)
```

**Arguments:**

- `index` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](Tradeskill.md#getnumtradeskills)) (`number`)

---

## SetTradeSkillInvSlotFilter

Filters the trade skill listing by equipment slot of items produced

**Signature:**

```lua
SetTradeSkillInvSlotFilter(index [, enable [, exclusive]])
```

**Arguments:**

- `index` - Index of an item equipment slot (in the list returned by [`GetTradeSkillInvSlots()`](Tradeskill.md#gettradeskillinvslots)), or `0` for no filter (`number`)
- `enable` - 1 to show recipes matching inventory type `index` in the filtered list; 0 to hide them (`number`)
- `exclusive` - 1 to disable other subclass filters when enabling this one; otherwise nil (`1nil`)

---

## SetTradeSkillItemLevelFilter

Filters the trade skill listing by required level of items produced

**Signature:**

```lua
SetTradeSkillItemLevelFilter(minLevel, maxLevel)
```

**Arguments:**

- `minLevel` - Lowest required level of items to show in the filtered list (`number`)
- `maxLevel` - Highest required level of items to show in the filtered list (`number`)

---

## SetTradeSkillItemNameFilter

Filters the trade skill listing by name of recipe, item produced, or reagents. Uses a substring (not exact-match) search: e.g. for a Scribe, the search string "doc" might filter the list to show only [Certificate of Ownership](http://www.wowhead.com/?item=43850) because it matches the word "documentation" in that item's tooltip; a search for "stam" will match all items providing a Stamina bonus.

**Signature:**

```lua
SetTradeSkillItemNameFilter("text")
```

**Arguments:**

- `text` - Text to search for in recipe names, produced item names or descriptions, or reagents (`string`)

---

## SetTradeSkillSubClassFilter

Filters the trade skill listing by subclass of items produced

**Signature:**

```lua
SetTradeSkillSubClassFilter(index [, enable [, exclusive]])
```

**Arguments:**

- `index` - Index of an item subclass (in the list returned by [`GetTradeSkillSubClasses()`](Tradeskill.md#gettradeskillsubclasses)), or `0` for no filter (`number`)
- `enable` - 1 to show recipes matching subclass `index` in the filtered list; 0 to hide them (`number`)
- `exclusive` - 1 to disable other subclass filters when enabling this one; otherwise nil (`1nil`)

---

## StopTradeSkillRepeat

Cancels repetition of a trade skill recipe. If a recipe is currently being performed, it will continue, but further scheduled repetitions will be canceled.

**Signature:**

```lua
StopTradeSkillRepeat()
```

---

## TradeSkillOnlyShowMakeable

Filters the trade skill listing by whether the player currently has enough reagents for each recipe

**Signature:**

```lua
TradeSkillOnlyShowMakeable(filter)
```

**Arguments:**

- `filter` - True to filter the recipe listing to show only recipes for which the player currently has enough reagents; false to show all recipes (`boolean`)

---

## TradeSkillOnlyShowSkillUps

Filters the trade skill listing by whether the player can gain skill ranks from each recipe. The default UI does not provide controls for this filter, but it can nonetheless be used to alter the contents of the trade skill recipe listing.

**Signature:**

```lua
TradeSkillOnlyShowSkillUps(filter)
```

**Arguments:**

- `filter` - True to filter the recipe listing to show only recipes which the player can gain skill ranks by performing; false to show all recipes (`boolean`)

---

← [WoW API Docs](../index.md)
