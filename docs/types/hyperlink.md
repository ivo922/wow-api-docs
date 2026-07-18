# Type: hyperlink

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

A string containing markup allowing the client to present it as a link, which the player can click to view more information about or take action regarding the data it represents.

Hyperlinks take the form `|H(linktype):(linkdata)|h(text)|h`, where `(linktype)` determines the type of link, `(linkdata)` is a code referencing the linked information, and `(text)` is the text visible to the player. Some API functions which operate on links do not require a full `hyperlink`, only its `linktype:linkdata` portion.

Links are often encapsulated in a [`colorString`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api_types/colorString) -- in such cases, the full `colorString`-wrapped link is the only form of the link allowed to be used in chat; attempting to transmit an invalid link may cause the player to be disconnected from the server.

The WoW client recognizes several kinds of hyperlinks, identified by their `linktype`. For `linkdata` elements noted as optional below, the client can still resolve the link if they are omitted:

`player` (example: `|Hplayer:Aerdrig|h[Aerdrig]|h`) - Represents a player character. Left-clicking a player link in the default UI opens the ChatFrameEditBox to send a whispered message to the character. Right-clicking opens a menu with options for inviting the character to the player's party/raid, adding the character to the ignore list, or reporting the chat message in which the link appears as spam.
 The `linkdata` for a player link consists solely of the player's name (or in cross-realm battlegrounds, the player's name and home realm separated by a hyphen, e.g. "Gundark-Broxigar").

`playerGM` (example: `|HplayerGM:Eyonix|h[Eyonix]|h`) - A variation on the `player` type used exclusively for Game Master chat.

`glyph` (example: `|cff66bbff|Hglyph:23:460|h[Glyph of Fortitude]|h|r`) - Represents a glyph inscribed in a character's spellbook. Clicking a glyph link in the default UI shows a tooltip with its description.
 The `linkdata` for a glyph link follows the format `socket:glyphID`:

- `socket` (optional) - The socket in which the glyph is placed; values 21 through 26 correspond to `glyphIndex` values 1 through 6.
- `glyphID` - A unique identifier for the glyph effect; not used elsewhere in the API.

`spell` (example: `|cff71d5ff|Hspell:46584|h[Raise Dead]|h|r`) - Represents a spell. Clicking a spell link in the default UI shows a tooltip with its description.
 The `linkdata` for a spell link consists solely of the [`spellID`](spellID.md) number uniquely identifying the spell, usable with APIs such as [`GetSpellInfo()`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/GetSpellInfo).

`enchant` (example: `|cffffd000|Henchant:59387|h[Certificate of Ownership]|h|r`) - Represents a trade skill recipe (originally used only for Enchanting, but now applies to all trade skills). Clicking a spell link in the default UI shows a tooltip with its description (and that of the item it creates, if applicable).
 The `linkdata` for a spell link consists solely of the [`spellID`](spellID.md) number uniquely identifying the trade skill recipe, usable with APIs such as [`GetSpellInfo()`](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/api/GetSpellInfo).

`quest` (example: `|cffffff00|Hquest:982:17|h[Deep Ocean, Vast Sea]|h|r`) - Represents a quest from a character's quest log. Clicking a quest link in the default UI shows a tooltip with a brief description of the quest and its objectives. When the client displays a quest link sent by another character, it automatically alters the enclosing `colorString` to reflect the difficulty of the quest relative to the player's level.
 The `linkdata` for a quest link follows the format `questID:level`:

- `questID` - A unique identifier for the quest; found on database sites (e.g. `quest ID 982`) but not used elsewhere in the API.
- `level` (optional) - Recommended character level for attempting the quest. (A level of `-1` means the quest is appropriate for any level; used for holiday quests.)

`talent` (example: `|cff4e96f7|Htalent:1396:4|h[Unleashed Fury]|h|r`) - Represents a talent. Clicking a talent link in the default UI shows a tooltip with its description.
 The `linkdata` for a talent link follows the format `talentID:points`:

- `talentID` - A unique identifier for the talent; not used elsewhere in the API.
- `rank` (optional) - Number of points spent in the talent, minus one: if this value is omitted or `-1`, the tooltip shows the talent as it appears in the Talents UI when zero points have been spent ; if this value is `0` , the tooltip shows the talent as it appears when one point has been spent on it. Values greater than the number of available ranks for a talent are interpreted as `-1`.

`achievement` (example: `|cffffff00|Hachievement:2336:060000000279E425:1:10:14:8:4294967295:4294967295:4294967295:4294967295|h[Insane in the Membrane]|h|r`) - Represents an achievement earned or in progress by a player. Clicking an achievement link in the default UI shows a tooltip with a summary of the achievement and (if applicable) its criteria. 
 The `linkdata` for an achievement link follows the format `achievementID:playerGUID:completed:month:day:year:bits1:bits2:bits3:bits4`. If only the first element `acheivementID` is specified, the client resolving the link will show the player's progress or completion of the achievement; otherwise, all elements are required:

- `achievementID` - A unique identifier for the achievements; usable with various Achievement API functions.
- `playerGUID` (optional) - GUID of a player character whose progress or completion of the achievement is linked (return value of `UnitGUID' without the "0x" prefix).
- `completed` (optional) - `1` if the character has completed the achievement; otherwise `0`.
- `month` (optional) - Index of the month (1 = January) in which the character completed the achievement, or `0` if the achievement is incomplete.
- `day` (optional) - Day of the month on which the character completed the achievement, or `0` if the achievement is incomplete.
- `year` (optional) - Year (two-digit year) in which the character completed the achievement, or `-1` if the achievement is incomplete.
- `bits1`, `bits2`, `bits3`, `bits4` (optional) - Encoded data fields interpreted by the client to show completion of achievement criteria.

`trade` (example: `|cffffd000|Htrade:45361:339:375:60000000279E425:Q/nPf6nprU3/n/fA8/Bw/PA+/B+/Aw/HA+/Bw/HA+5nfg////////P////HAAAQAA+DAAAAAAA|h[Inscription]|h|r`) - Represents the entire list of recipes for a character's trade skill or profession. 
 The `linkdata` for an achievement link follows the format `spellID:skill:maxSkill:playerGUID:data`. If only the first element `acheivementID` is specified, the client resolving the link will show the player's progress or completion of the achievement; otherwise, all elements are required:

- `spellID` - The `spellID` number uniquely identifying the trade skill and its rank (e.g. Apprentice Tailoring vs. Journeyman Tailoring), usable with APIs such as `GetSpellInfo()`.
- `skill` - The character's current skill in the profession.
- `maxSkill` - The maximum skill for the character's current rank in the profession (e.g. 375 for Master rank).
- `playerGUID` - GUID of the character whose profession is linked (return value of `UnitGUID' without the "0x" prefix).
- `data` (optional) - Encoded data field interpreted by the client to show the character's list of known trade skill recipes.

`item` (examples: `|cffa335ee|Hitem:45457:3828:3395:3395:0:0:0:0:80|h[Staff of Endless Winter]|h|r`, `|cff1eff00|Hitem:36360:0:0:0:0:0:-37:1633878093:80|h[Frostpaw Legguards]|h|r`) - Represents an item. Clicking an item link in the default UI shows a tooltip with information about the item. Control-clicking an equippable item opens the DressUpFrame to preview how the item would look on the player character if equipped.
 The `linkdata` for an item link follows the format `itemID:enchant:gem1:gem2:gem3:gem4:suffixID:uniqueID:level`:

- `itemID` - The item's `itemID`.
- `enchant` (optional) - Unique identifier of the enchantment applied to the item; not used elsewhere in the API.
- `gem1`, `gem2`, `gem3`, `gem4` (optional) - Unique identifiers of the enchantments provided by gems socketed in the item (not the `itemID`s of the gems themselves); not used elsewhere in the API.
- `suffixID` (optional) - Identifies the specific variation represented for random-property items (e.g. "... of the Monkey", 
 "... of Frost Protection", etc.). A positive number indicates a variation with specific stat values (e.g. `1200` = "of the Bear", 8 stamina 8 strength; `1220` = "of the Bear", 14 stamina 15 strength); a negative number indicates a type of variation, with actual stat values to be determined by decoding the `uniqueID`.
- `uniqueID` (optional) - A number used internally by the WoW client/server architecture to track a specific occurrence of an item: used for crafted items which display "<Made by *Name*>" in their tooltips and for random-property items. For items with a negative `suffixID`, using `bit.band(uniqueID, 0xFFFF)` reveals the factor used to calculate the item's stats.
- `level` - Level of the character linking the item; used for "Heirloom" items whose stats change based on the level of the character equipping them.

`levelup` (examples: `|cffFF4E00|Hlevelup:61:LEVEL_UP_TYPE_CHARACTER|h[Level 61]|h|r`) - represents the level up information for a player unit.
 The `linkdata`for a levelup link follows the format
 `level:type`

- `level` - The numeric level the unit has reached
- `type` - This is one of `LEVEL_UP_TYPE_CHARACTER`, `LEVEL_UP_TYPE_PET` and `LEVEL_UP_TYPE_GUILD` and specifies who gained the level
- Note: A level up of type `LEVEL_UP_TYPE_PET` on a non-pet class will display the level up information of the last level up link clicked (or a blank information if none has been clicked since UI load) on non-pet classes.

`instancelock` (example: `|cffff8000|Hinstancelock:01000000003E8E2E7:531:0:15|h[Ahn'Qiraj Temple]|h|r`) - represence a player's instance lockout
 The `linkdata` for an instancelock link follows the format `guid:instanceID:difficulty:bossesDefeated`

- `guid` - The GUID of the player the lockout belongs to
- `instanceID` - The ID of the instance

- `0` - Normal
- `1` - Heroic 5-man
- `2` - Heroic raid

---

← [API Types](../API Types.md)
