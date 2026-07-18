# Limited play time functions

← [WoW API Docs](../index.md)

**3** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#playtime)

---

## GetBillingTimeRested

Returns the amount of time for which the player must be offline in order to lift play time restrictions. After playing for a number of hours, restrictions may be placed on the player's ability to gain loot or XP, complete quests, or use trade skills; if in such a state, the player must log off for the period of time specified by this function in order to return to normal play.

Only used in locales where the length of play sessions is restricted (e.g. mainland China).

**Signature:**

```lua
time = GetBillingTimeRested()
```

**Returns:**

- `time` - Offline time required to lift play time restrictions (in minutes) (`number`)

---

## NoPlayTime

Returns whether the player has exceeded the allowed play time limit. When in this state, the player is unable to gain loot or XP or complete quests and cannot use trade skills; returning to normal requires logging out of the game for a period of time (see [`GetBillingTimeRested`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetBillingTimeRested)).

Only used in locales where the length of play sessions is restricted (e.g. mainland China).

**Signature:**

```lua
hasNoTime = NoPlayTime()
```

**Returns:**

- `hasNoTime` - 1 if the player is out of play time, otherwise nil (`1nil`)

---

## PartialPlayTime

Returns whether the player is near the allowed play time limit. When in this state, the player receives half the normal amount of money and XP from kills and quests and cannot use trade skills; returning to normal requires logging out of the game for a period of time (see [`GetBillingTimeRested`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetBillingTimeRested)).

Only used in locales where the length of play sessions is restricted (e.g. mainland China).

**Signature:**

```lua
partialPlayTime = PartialPlayTime()
```

**Returns:**

- `partialPlayTime` - 1 if the character gains only partial xp, nil if not. (`1nil`)

---

← [WoW API Docs](../index.md)
