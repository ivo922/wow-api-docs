# Achievement functions

← [WoW API Docs](../index.md)

**34** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#achievement)

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

## CanShowAchievementUI

Returns whether the Achievements UI should be enabled.

Used by the default UI to determine whether to show or hide the menu button for Achievements (as it also does for Talents); currently always returns true.

**Signature:**

```lua
canShow = CanShowAchievementUI()
```

**Returns:**

- `canShow` - true if the Achievements UI should be enabled, otherwise false (`boolean`)

---

## ClearAchievementComparisonUnit

Disables comparing achievements/statistics with another player

**Signature:**

```lua
ClearAchievementComparisonUnit()
```

---

## GetAchievementCategory

Returns the numeric ID of the category to which an achievement belongs

**Signature:**

```lua
categoryID = GetAchievementCategory(achievementID)
```

**Arguments:**

- `achievementID` - The numeric ID of an achievement (`number`)

**Returns:**

- `categoryID` - The numeric ID of the achievement's category (`number`)

---

## GetAchievementComparisonInfo

Returns information about the comparison unit's achievements. Only accurate once the `INSPECT_ACHIEVEMENT_READY` event has fired following a call to `SetAchievementComparisonUnit()`. No longer accurate once `ClearAchievementComparisonUnit()` is called.

**Signature:**

```lua
completed, month, day, year = GetAchievementComparisonInfo(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

**Returns:**

- `completed` - True if the comparison unit has completed the achievement; otherwise nil (`boolean`)
- `month` - Month in which the comparison unit completed the achievement (`number`)
- `day` - Day of the month on which the comparison unit completed the achievement (`number`)
- `year` - Year in which the comparison unit completed the achievement. (Two digit year, assumed to be 21st century.) (`number`)

---

## GetAchievementCriteriaInfo

Gets information about criteria for an achievement or data for a statistic

**Signature:**

```lua
description, type, completed, quantity, requiredQuantity, characterName, flags, assetID, quantityString, criteriaID = GetAchievementCriteriaInfo(achievementID, index) or GetAchievementCriteriaInfo(statisticID)
```

**Arguments:**

- `achievementID` - The numeric ID of an achievement (`number`)
- `index` - Index of one of the achievement's criteria (between 1 and GetAchievementNumCriteria()) (`number`)
- `statisticID` - The numeric ID of a statistic (`number`)

**Returns:**

- `description` - Description of the criterion (as displayed in the UI for achievements with multiple criteria) or statistic (`string`)
- `type` - Type of criterion: a value of 8 indicates the criterion is another achievement; other values are not used in the default UI (`number`)
- `completed` - True if the player has completed the criterion; otherwise false (`boolean`)
- `quantity` - If applicable, number of steps taken towards completing the criterion (e.g. for the only criterion of "Did Somebody Order a Knuckle Sandwich?", the player's current Unarmed skill; for the first criterion of "Pest Control", 1 if the player has killed an Adder, 0 otherwise (`number`)
- `requiredQuantity` - If applicable, number of steps required to complete the criterion (e.g. 400 for the only criterion of "Did Somebody Order a Knuckle Sandwich?"; 1 for any criterion of "Pest Control" (`number`)
- `characterName` - Character name with which the criterion was completed. Currently always the player character's name for completed criteria (`string`)
- `flags` - Test against the following masks with bit.band() to reveal additional information: (`bitfield`)
  - `0x00000001` - Criterion should be displayed as a progress bar
  - `0x00000002` - Criterion should be hidden in normal achievement displays
- `assetID` - Internal ID number of the quest to complete, NPC to kill, item to acquire, world object to interact with, achievement to earn, or other game entity related to completing the criterion. (Note: some but not all of these ID types are usable elsewhere in the WoW API) (`number`)
- `quantityString` - Text to be shown when displaying `quantity` and `requiredQuantity` in a UI element. (Not always the same as `format("%d / %d", quantity, requiredQuantity)`; e.g. "Got My Mind On My Money" shows monetary amounts with embedded textures for gold, silver, and copper) (`string`)
- `criteriaID` - Unique ID number identifying the criterion; usable with `GetAchievementInfoFromCriteria()` (`number`)

---

## GetAchievementInfo

Gets information about an achievement or statistic

**Signature:**

```lua
id, name, points, completed, month, day, year, description, flags, icon, rewardText = GetAchievementInfo(category, index) or GetAchievementInfo(id)
```

**Arguments:**

- `category` - Numeric ID of an achievement category (`number`)
- `index` - Index of an achievement within a category (between 1 and GetCategoryNumAchievements()) (`number`)
- `id` - The numeric ID of an achievement or statistic (`number`)

**Returns:**

- `id` - The numeric ID of the achievement or statistic (`number`)
- `name` - Name of the achievement or statistic (`string`)
- `points` - Amount of achievement points awarded for completing the achievement (`number`)
- `completed` - True if the player has completed the achievement; otherwise false (`boolean`)
- `month` - Month in which the player completed the achievement (`number`)
- `day` - Day of the month on which the player completed the achievement (`number`)
- `year` - Year in which the player completed the achievement. (Two digit year, assumed to be 21st century.) (`number`)
- `description` - Description of the achievement (`string`)
- `flags` - Test against the following masks with bit.band() to reveal additional information: (`bitfield`)
  - `0x00000001` - Info is for a statistic, not an achievement
  - `0x00000002` - Achievement should be hidden in normal displays
  - `0x00000080` - Achievement should display its criteria as a progress bar regardless of per-criterion flags
- `icon` - Path to an icon texture for the achievement (`string`)
- `rewardText` - Text describing a reward for the achievement, or the empty string if no reward is offered (`string`)

---

## GetAchievementInfoFromCriteria

Gets information about an achievement or statistic given a criterion ID

**Signature:**

```lua
id, name, points, description, flags, icon, rewardText = GetAchievementInfoFromCriteria(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement or statistic criterion (as can be retrieved from GetAchievementCriteriaInfo()) (`number`)

**Returns:**

- `id` - The numeric ID of the achievement or statistic (`number`)
- `name` - Name of the achievement or statistic (`string`)
- `points` - Amount of achievement points awarded for completing the achievement (`number`)
- `description` - Description of the achievement (`string`)
- `flags` - Test against the following masks with bit.band() to reveal additional information: (`bitfield`)
  - `0x00000001` - Info is for a statistic, not an achievement
  - `0x00000002` - Achievement should be hidden in normal displays
  - `0x00000080` - Achievement should display its criteria as a progress bar regardless of per-criterion flags
- `icon` - Path to an icon texture for the achievement (`string`)
- `rewardText` - Text describing a reward for the achievement, or the empty string if no reward is offered (`string`)

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

## GetAchievementNumCriteria

Returns the number of measured criteria for an achievement.

Measured criteria for an achievement are shown in the default UI as details when clicking on an achievement in the achievements window or when showing an achievement in the objectives tracker; e.g. "Master of Arms" (15 criteria: Axes, Bows, Crossbows, Daggers, etc.) and "Safe Deposit" (1 criterion: number of bank slots purchased).

Not all achievements have criteria: achievements with zero criteria are those that can be completed in a single event (though a complicated event it may be), explained in achievement's description: e.g. "Reach level 80", "Fall 65 yards without dying", and "With all three Twilight Drakes still alive, engage and defeat Sartharion the Onyx Guardian on Normal Difficulty".

**Signature:**

```lua
count = GetAchievementNumCriteria(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

**Returns:**

- `count` - Number of criteria for the achievement (`number`)

---

## GetAchievementNumRewards

Returns the number of point rewards for an achievement (currently always 1).

Currently all achievements and statistics offer one reward (according to this function), though the rewards offered by statistics are all zero points.

**Signature:**

```lua
count = GetAchievementNumRewards(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement or statistic (`number`)

**Returns:**

- `count` - Number of point rewards offered for the achievement (`number`)

---

## GetAchievementReward

Returns the number of achievement points awarded for earning an achievement.

Currently all achievements and statistics offer one reward (according to this function), though the rewards offered by statistics are all zero points.

**Signature:**

```lua
points = GetAchievementReward(id, index)
```

**Arguments:**

- `id` - The numeric ID of an achievement or statistic (`number`)
- `index` - Index of one of the achievement's rewards (between 1 and GetAchievementNumRewards(); currently always 1) (`number`)

**Returns:**

- `points` - Number of achievement points awarded for completing the achievement (`number`)

---

## GetCategoryInfo

Returns information about an achievement/statistic category

**Signature:**

```lua
name, parentID, flags = GetCategoryInfo(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement/statistic category (`number`)

**Returns:**

- `name` - Name of the category (`string`)
- `parentID` - ID of the parent category of which this is a sub-category, or -1 if this is a top-level category (`number`)
- `flags` - Various additional information about the category; currently unused (0 for all existing categories) (`bitfield`)

---

## GetCategoryList

Returns a list of all achievement categories

**Signature:**

```lua
categories = GetCategoryList()
```

**Returns:**

- `categories` - A list of achievement category IDs (`table`)

---

## GetCategoryNumAchievements

Returns the number of achievements/statistics to display in a category.

Note this function does not return the total number of achievements in a category; it only returns the number to be displayed in the default UI. Achievements may belong to a category but not be counted for display: e.g. among those which are part of a series (100 Quests Completed, 500 Quests Completed), only the achievement most recently completed and the achievement following it in the series are shown.

**Signature:**

```lua
numItems, numCompleted = GetCategoryNumAchievements(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement/statistic category (`number`)

**Returns:**

- `numItems` - Number of achievements or statistics to display in the category (`number`)
- `numCompleted` - Number of completed achievements in the category (or 0 for statistics) (`number`)

---

## GetComparisonAchievementPoints

Returns the comparison unit's total achievement points earned.

Only accurate once the `INSPECT_ACHIEVEMENT_READY `event has fired following a call to `SetAchievementComparisonUnit()`. No longer accurate once `ClearAchievementComparisonUnit()` is called.

**Signature:**

```lua
points = GetComparisonAchievementPoints()
```

**Returns:**

- `points` - Total number of achievement points earned by the comparison unit (`number`)

---

## GetComparisonCategoryNumAchievements

Returns the number of achievements completed by the comparison unit within a category.

Only accurate once the `INSPECT_ACHIEVEMENT_READY `event has fired following a call to `SetAchievementComparisonUnit()`. No longer accurate once `ClearAchievementComparisonUnit()` is called.

**Signature:**

```lua
numCompleted = GetComparisonCategoryNumAchievements(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement category (`number`)

**Returns:**

- `numCompleted` - Number of achievements completed by the comparison unit in the category (`number`)

---

## GetComparisonStatistic

Returns the comparison unit's data for a statistic.

Only accurate once the `INSPECT_ACHIEVEMENT_READY `event has fired following a call to `SetAchievementComparisonUnit()`. No longer accurate once `ClearAchievementComparisonUnit()` is called.

**Signature:**

```lua
info = GetComparisonStatistic(id)
```

**Arguments:**

- `id` - The numeric ID of a statistic (`number`)

**Returns:**

- `info` - The comparison unit's data for the statistic, or "--" if none has yet been recorded for it (`string`)

---

## GetLatestCompletedAchievements

Returns a list of the player's most recently earned achievements

**Signature:**

```lua
... = GetLatestCompletedAchievements()
```

**Returns:**

- `...` - A list of up to five numeric IDs of recently earned achievements, ordered from newest to oldest (`list`)

---

## GetLatestCompletedComparisonAchievements

Returns a list of the comparison unit's most recently earned achievements

**Signature:**

```lua
... = GetLatestCompletedComparisonAchievements()
```

**Returns:**

- `...` - A list of up to five numeric IDs of recently earned achievements, ordered from newest to oldest (`list`)

---

## GetLatestUpdatedComparisonStats `deprecated`

Returns a list of the comparison unit's latest updated statistics.

Currently always returns a list of invalid statistic IDs -- the "latest updated statistics" feature is no longer a part of the Achievements UI.

**Signature:**

```lua
... = GetLatestUpdatedComparisonStats()
```

**Returns:**

- `...` - A list of up to five numeric IDs of recently updated statistics for the comparison unit, ordered from newest to oldest (`list`)

---

## GetLatestUpdatedStats `deprecated`

Returns a list of the player's latest updated statistics.

Currently always returns a list of invalid statistic IDs -- the "latest updated statistics" feature is no longer a part of the Achievements UI.

**Signature:**

```lua
... = GetLatestUpdatedStats()
```

**Returns:**

- `...` - A list of up to five numeric IDs of recently updated statistics for the player, ordered from newest to oldest (`list`)

---

## GetNextAchievement

Returns the next achievement for an achievement which is part of a series

**Signature:**

```lua
nextID, completed = GetNextAchievement(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

**Returns:**

- `nextID` - If the given achievement is part of a series and not the last in its series, the ID of the next achievement in the series; otherwise nil (`number`)
- `completed` - True if the next achievement has been completed; otherwise nil (`boolean`)

---

## GetNumComparisonCompletedAchievements

Returns the number of achievements earned by the comparison unit.

Does not include Feats of Strength.

**Signature:**

```lua
total, completed = GetNumComparisonCompletedAchievements()
```

**Returns:**

- `total` - Total number of achievements currently in the game (`number`)
- `completed` - Number of achievements earned by the comparison unit (`number`)

---

## GetNumCompletedAchievements

Returns the number of achievements earned by the player.

Does not include Feats of Strength.

**Signature:**

```lua
total, completed = GetNumCompletedAchievements()
```

**Returns:**

- `total` - Total number of achievements currently in the game (`number`)
- `completed` - Number of achievements earned by the player (`number`)

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

## GetPreviousAchievement

Returns the previous achievement for an achievement which is part of a series

**Signature:**

```lua
previousID = GetPreviousAchievement(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

**Returns:**

- `previousID` - If the given achievement is part of a series and not the first in its series, the ID of the previous achievement in the series; otherwise nil (`number`)

---

## GetStatistic

Returns data for a statistic that can be shown on the statistics tab of the achievements window

**Signature:**

```lua
info = GetStatistic(id)
```

**Arguments:**

- `id` - The numeric ID of a statistic (`number`, [blizzid](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#blizzid))

**Returns:**

- `info` - The data for the statistic, or "--" if none has yet been recorded for it (`string`)

---

## GetStatisticsCategoryList

Returns a list of all statistic categories

**Signature:**

```lua
categories = GetStatisticsCategoryList()
```

**Returns:**

- `categories` - A list of statistic category IDs (`table`)

---

## GetTotalAchievementPoints

Returns the player's total achievement points earned

**Signature:**

```lua
points = GetTotalAchievementPoints()
```

**Returns:**

- `points` - Total number of achievement points earned by the player (`number`)

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

## RemoveTrackedAchievement

Removes an achievement from the objectives tracker UI

**Signature:**

```lua
RemoveTrackedAchievement(id)
```

**Arguments:**

- `id` - The numeric ID of an achievement (`number`)

---

## SetAchievementComparisonUnit

Enables comparing achievements/statistics with another player.

After a call to this function, the `INSPECTACHIEVEMENTREADY `event fires to indicate that achievement/statistic comparison functions will return valid data on the given unit.

**Signature:**

```lua
success = SetAchievementComparisonUnit(unit)
```

**Arguments:**

- `unit` - ID of a unit to compare against (`unitID`)

**Returns:**

- `success` - 1 if the given unit is a valid unit. (Does not indicate whether the unit exists or can be compared against.) (`1nil`)

---

← [WoW API Docs](../index.md)
