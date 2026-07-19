# Summoning functions

← [WoW API Docs](../index.md)

**6** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#summon)

---

## CancelSummon

Declines an offered summons. Usable between when the [`CONFIRM_SUMMON`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_SUMMON) event fires (due to a summoning spell cast by another player) and when the value returned by [`GetSummonConfirmTimeLeft()`](Summoning.md#getsummonconfirmtimeleft) reaches zero.

**Signature:**

```lua
CancelSummon()
```

---

## ConfirmSummon

Accepts an offered summons, teleporting the player to the summoner's location. Usable between when the [`CONFIRM_SUMMON`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_SUMMON) event fires (due to a summoning spell cast by another player) and when the value returned by [`GetSummonConfirmTimeLeft()`](Summoning.md#getsummonconfirmtimeleft) reaches zero.

**Signature:**

```lua
ConfirmSummon()
```

---

## GetSummonConfirmAreaName

Returns the destination area of an offered summons. The name returned is generally that of the subzone in which the summoner performed the spell.

Usable between when the [`CONFIRM_SUMMON`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_SUMMON) event fires (due to a summoning spell cast by another player) and when the value returned by [`GetSummonConfirmTimeLeft()`](Summoning.md#getsummonconfirmtimeleft) reaches zero.

**Signature:**

```lua
area = GetSummonConfirmAreaName()
```

**Returns:**

- `area` - Name of the location to which the player will be teleported upon accepting the summons (`string`)

---

## GetSummonConfirmSummoner

Returns the name of the unit offering a summons to the player. Usable between when the [`CONFIRM_SUMMON`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/CONFIRM_SUMMON) event fires (due to a summoning spell cast by another player) and when the value returned by [`GetSummonConfirmTimeLeft()`](Summoning.md#getsummonconfirmtimeleft) reaches zero.

**Signature:**

```lua
text = GetSummonConfirmSummoner()
```

**Returns:**

- `text` - Name of the summoning unit (`string`)

---

## GetSummonConfirmTimeLeft

Returns the amount of time remaining before an offered summons expires. Returns 0 if no summons is currently available.

**Signature:**

```lua
timeleft = GetSummonConfirmTimeLeft()
```

**Returns:**

- `timeleft` - Time remaining until the offered summons can no longer be accepted (in seconds) (`number`)

---

## PlayerCanTeleport

Returns whether the player can accept a summons

**Signature:**

```lua
amount = PlayerCanTeleport()
```

**Returns:**

- `amount` - True if the player is currently allowed to accept a summons (`boolean`)

---

← [WoW API Docs](../index.md)
