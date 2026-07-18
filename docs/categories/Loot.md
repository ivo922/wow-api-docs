# Loot functions

← [WoW API Docs](../index.md)

**23** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#loot)

---

## CloseLoot

Ends interaction with a lootable corpse or object. Causes the [`LOOT_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LOOT_CLOSED) event to fire, indicating that Loot APIs may no longer have effects or return valid data.

If the corpse was designated as the player's loot (via the Round Robin, Group Loot, or Need Before Greed loot methods), the corpse's loot becomes available to the rest of the group. If (and only if) the loot was generated from Disenchanting, Prospecting, Milling or similar, all loot items are automatically picked up.

**Signature:**

```lua
CloseLoot()
```

---

## ConfirmLootRoll `confirmation`

Confirms the player's intent regarding an item up for loot rolling. Usable after the [`CONFIRM_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_LOOT_ROLL) event fires, warning that an item binds on pickup.

**Signature:**

```lua
ConfirmLootRoll(id, rollType)
```

**Arguments:**

- `id` - Index of an item currently up for loot rolling (as provided in the [`START_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/START_LOOT_ROLL) event) (`number`)
- `rollType` - Type of roll action to perform (`number`)
  - `0` - Pass (declines the loot)
  - `1` - Roll "need" (wins if highest roll)
  - `2` - Roll "greed" (wins if highest roll and no other member rolls "need")

---

## ConfirmLootSlot `confirmation`

Confirms picking up an item available as loot. Usable after the [`LOOT_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LOOT_BIND_CONFIRM) event fires, warning that an item binds on pickup.

**Signature:**

```lua
ConfirmLootSlot(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

---

## GetLootMethod

Returns information about the current loot method in a party or raid. Only returns useful information if the player is in a party or raid.

**Signature:**

```lua
method, partyMaster, raidMaster = GetLootMethod()
```

**Returns:**

- `method` - Current loot method (`string`)
  - `freeforall` - Free for All - any group member can take any loot at any time
  - `group` - Group Loot - like Round Robin, but items above a quality threshold are rolled on
  - `master` - Master Looter - like Round Robin, but items above a quality threshold are left for a designated loot master to
  - `needbeforegreed` - Need before Greed - like Group Loot, but members automatically pass on items
  - `roundrobin` - Round Robin - group members take turns being able to loot
- `partyMaster` - Numeric portion of the `party` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) of the loot master (e.g. if `2`, the loot master's unitID is `party2`); nil if not using the Master Looter method or if the player is in a raid whose loot master is not in the player's subgroup. If the player is the master looter, this value will return 0. (`number`)
- `raidMaster` - Numeric portion of the `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) of the loot master (e.g. if `17`, the loot master's unitID is `raid17`); nil if not using the Master Looter method or not in a raid group (`number`)

---

## GetLootRollItemInfo

Returns information about an item currently up for loot rolling

**Signature:**

```lua
texture, name, count, quality, bindOnPickUp = GetLootRollItemInfo(id)
```

**Arguments:**

- `id` - Index of an item currently up for loot rolling (as provided in the [`START_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/START_LOOT_ROLL) event) (`number`)

**Returns:**

- `texture` - Path to an icon texture for the item (`string`)
- `name` - Name of the item (`string`)
- `count` - Number of stacked items (`number`)
- `quality` - Quality (rarity) of the item. (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))
- `bindOnPickUp` - 1 if the item is bind on pickup; otherwise nil (`1nil`)

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

## GetLootRollTimeLeft

Returns the amount of time remaining before loot rolling for an item expires. When the time expires, all group members who have not yet chosen to roll Need or Greed automatically pass, random roll results are produced for those who chose to roll, and the server declares a winner and awards the item.

**Signature:**

```lua
timeLeft = GetLootRollTimeLeft(id)
```

**Arguments:**

- `id` - Index of an item currently up for loot rolling (as provided in the [`START_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/START_LOOT_ROLL) event) (`number`)

**Returns:**

- `timeLeft` - Amount of time remaining before loot rolling for the item expires (in milliseconds) (`number`)

---

## GetLootSlotInfo

Returns a hyperlink for an item available as loot

**Signature:**

```lua
texture, item, quantity, quality, locked = GetLootSlotInfo(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

**Returns:**

- `texture` - Path to an icon texture for the item or amount of money (`string`)
- `item` - Name of the item, or description of the amount of money (`string`)
- `quantity` - Number of stacked items, or 0 for money (`number`)
- `quality` - Quality (rarity) of the item (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))
- `locked` - 1 if the item is locked (preventing the player from looting it); otherwise nil (`1nil`)

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

## GetLootThreshold

Returns the threshold used for Master Looter, Group Loot, and Need Before Greed loot methods. Items above the `threshold` quality will trigger the special behavior of the current loot method: for Group Loot and Need Before Greed, rolling will automatically begin once a group member loots the corpse or object holding the item; for Master Loot, the item will be invisible to all but the loot master tasked with assigning the loot.

**Signature:**

```lua
threshold = GetLootThreshold()
```

**Returns:**

- `threshold` - Minimum item quality to trigger the loot method (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))

---

## GetMasterLootCandidate

Returns information about a given loot candidate. Used in the default UI to build the popup menu used in master loot assignment. Only valid if the player is the master looter.

Not all party/raid members may be eligible for a given corpse's (or object's) loot: e.g. a member is ineligible for loot from a creature killed while that member was not in the immediate area. By repeatedly calling this function (with `index` incrementing from 1 to the total number of party/raid members, including the player), one can build a list of the names of members eligible for the current loot.

The index is cast in stone at the time the mob was killed. If you move raid members around prior to distributing loot, their original positions will be returned by this function. The expression `ceil(index/5)` will yield the group number (in a raid) and the expression `index % 5` will yield the group position number for an eligible raider.

**Signature:**

```lua
candidate = GetMasterLootCandidate(index)
```

**Arguments:**

- `index` - Index of a member of the party or raid (*not* equivalent to the numeric part of a `party` or `raid` [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID)) (`number`)

**Returns:**

- `candidate` - Name of the candidate (`string`)

---

## GetNumLootItems

Returns the number of items available to be looted

**Signature:**

```lua
numItems = GetNumLootItems()
```

**Returns:**

- `numItems` - Number of the items available to be looted (`number`)

---

## GetOptOutOfLoot

Returns whether the player has opted out of loot rolls. When opting out, no prompt will be shown for loot which ordinarily would prompt the player to roll (need/greed) or pass; the loot rolling process will continue for other group members as if the player had chosen to pass on every roll.

**Signature:**

```lua
isOptOut = GetOptOutOfLoot()
```

**Returns:**

- `isOptOut` - 1 if the has opted out of loot rolls; otherwise nil (`1nil`)

---

## GiveMasterLoot

Awards a loot item to a group member. Has no effect if the player is not the loot master or if no loot or candidate matching the given parameters exists.

**Signature:**

```lua
GiveMasterLoot(slot, index)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)
- `index` - Index of a loot candidate (see [`GetMasterLootCandidate()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMasterLootCandidate)) (`number`)

---

## IsFishingLoot

Returns whether the currently displayed loot came from fishing. Used in the default UI to play a fishing sound effect and change the appearance of the loot window.

**Signature:**

```lua
isFishing = IsFishingLoot()
```

**Returns:**

- `isFishing` - 1 if the currently displayed loot is fishing loot; otherwise nil (`1nil`)

---

## LootSlot

Attempts to pick up an item available as loot. If the item in the loot slot binds on pickup, the [`LOOT_BIND_CONFIRM`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LOOT_BIND_CONFIRM) event fires, indicating that [`ConfirmLootSlot(slot)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ConfirmLootSlot) must be called in order to actually loot the item. Please note: if you call this while processing a [`LOOT_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LOOT_OPENED) event and it is the last item to be looted from the corpse, can cause [`LOOT_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LOOT_CLOSED) to fire and be processed before your `LOOT_OPENED` event handler completes.

**Signature:**

```lua
LootSlot(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

---

## LootSlotIsCoin

Returns whether a loot slot contains money

**Signature:**

```lua
isCoin = LootSlotIsCoin(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

**Returns:**

- `isCoin` - 1 if the loot slot contains money; otherwise nil (`1nil`)

---

## LootSlotIsItem

Returns whether a loot slot contains an item

**Signature:**

```lua
isItem = LootSlotIsItem(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

**Returns:**

- `isItem` - 1 if the loot slot contains an item; otherwise nil (`1nil`)

---

## RollOnLoot

Register the player's intent regarding an item up for loot rolling. Rolls are not actually performed until all eligible group members have registered their intent or the time period for rolling expires.

If the item binds on pickup, the [`CONFIRM_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_LOOT_ROLL) event fires, indicating that [`ConfirmLootRoll(id)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/ConfirmLootRoll) must be called in order to actually roll on the item.

**Signature:**

```lua
RollOnLoot(id, rollType)
```

**Arguments:**

- `id` - Index of an item currently up for loot rolling (as provided in the [`START_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/START_LOOT_ROLL) event) (`number`)
- `rollType` - Type of roll action to perform (`number`)
  - `0` - Pass (declines the loot)
  - `1` - Roll "need" (wins if highest roll)
  - `2` - Roll "greed" (wins if highest roll and no other member rolls "need")
  - `3` - Disenchant

---

## SetLootMethod

Sets the loot method for a party or raid group. Has no effect if the player is not the party or raid leader.

See [`SetLootThreshold`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetLootThreshold) for the quality threshold used by Master Looter, Group Loot, and Need Before Greed methods.

**Signature:**

```lua
SetLootMethod("method" [, "master"])
```

**Arguments:**

- `method` - Method to use for loot distribution (`string`)
  - `freeforall` - Free for All - any group member can take any loot at any time
  - `group` - Group Loot - like Round Robin, but items above a quality threshold are rolled on
  - `master` - Master Looter - like Round Robin, but items above a quality threshold are left for a designated loot master to
  - `needbeforegreed` - Need before Greed - like Group Loot, but members automatically pass on items
  - `roundrobin` - Round Robin - group members take turns being able to loot
- `master` - Name or [`unitID`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID) of the master looter (`string`)

---

## SetLootPortrait

Sets a Texture object to show the appropriate portrait image when looting. Normally, the loot portrait image is the same as that of the creature being looted. Not used in the default UI -- a generic image for all loot is used instead.

**Signature:**

```lua
SetLootPortrait(texture)
```

**Arguments:**

- `texture` - A Texture object (`table`)

---

## SetLootThreshold

Sets the threshold used for Master Looter, Group Loot, and Need Before Greed loot methods. Has no effect if the player is not the party or raid leader.

Items above the `threshold` quality will trigger the special behavior of the current loot method: for Group Loot and Need Before Greed, rolling will automatically begin once a group member loots the corpse or object holding the item; for Master Loot, the item will be invisible to all but the loot master tasked with assigning the loot.

The loot threshold defaults to `2` (Uncommon) when forming a new party/raid. Setting the threshold to `0` (Poor) or `1` (Common) has no effect -- qualities below Uncommon are always treated as below the threshold. The default UI only allows setting the threshold as high as `4` (Epic), but higher thresholds are allowed.

**Signature:**

```lua
SetLootThreshold(threshold)
```

**Arguments:**

- `threshold` - Minimum item quality to trigger the loot method (`number`, [itemQuality](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#itemQuality))

---

## SetOptOutOfLoot

Changes the player's preference to opt out of loot rolls. When opting out, no prompt will be shown for loot which ordinarily would prompt the player to roll (need/greed) or pass; the loot rolling process will continue for other group members as if the player had chosen to pass on every roll.

**Signature:**

```lua
SetOptOutOfLoot(enable)
```

**Arguments:**

- `enable` - True to opt out of loot, false to participate in loot rolls (`boolean`)

---

← [WoW API Docs](../index.md)
