# ActionBar functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#actionbar)

---

## ChangeActionBarPage `nocombat`

Changes the current action bar page

**Signature:**

```lua
ChangeActionBarPage(page)
```

**Arguments:**

- `page` - The action bar page to change to (`number`)

---

## GetActionBarPage

Returns the current action bar page

**Signature:**

```lua
page = GetActionBarPage()
```

**Returns:**

- `page` - The current action bar page (`number`)

---

## GetActionBarToggles

Returns the current visibility settings for the four secondary action bars

**Signature:**

```lua
showBar1, showBar2, showBar3, showBar4 = GetActionBarToggles()
```

**Returns:**

- `showBar1` - 1 if the interface option is set to show the Bottom Left ActionBar, otherwise nil (`1nil`)
- `showBar2` - 1 if the interface option is set to show the Bottom Right ActionBar, otherwise nil (`1nil`)
- `showBar3` - 1 if the interface option is set to show the Right ActionBar, otherwise nil (`1nil`)
- `showBar4` - 1 if the interface option is set to show the Right ActionBar 2, otherwise nil (`1nil`)

---

## GetBonusBarOffset

Returns the current "stance" offset for use with the bonus action bar. This value corresponds to what "stance" the player is currently in, and more specifically which set of actions correspond to that stance. Action IDs for special stances start on action bar #7 (or `NUM_ACTIONBAR_PAGES + 1`), so the `offset` returned by this function corresponds to the number to be added to `NUM_ACTIONBAR_PAGES` in calculating action IDs for these action bars.

Note that the UI definition of "stance" includes not just warrior stances but also druid shapeshift forms, rogue/druid stealth, priest shadowform, and various other cases, but does not necessarily include all states normally presented in the default UI's stance/shapeshift bar (notable exclusions are paladin auras and death knight presences).

**Signature:**

```lua
offset = GetBonusBarOffset()
```

**Returns:**

- `offset` - Offset of the stance's action bar in relation to `NUM_ACTIONBAR_PAGES` (`number`)

---

## GetPossessInfo

Returns information about special actions available while the player possesses another unit. Used in the default UI to show additional special actions (e.g. canceling possession) while the player possesses another unit through an ability such as Eyes of the Beast or Mind Control.

Does not apply to actions (spells) belonging to the possessed unit; those are regular actions (see [`GetActionInfo()`](Action.md#getactioninfo)) whose [`actionID`](../types/actionID.md)s begin at `((NUM_ACTIONBAR_PAGES - 1 +` [`GetBonusBarOffset()`](ActionBar.md#getbonusbaroffset)`) * NUM_ACTIONBAR_BUTTONS + 1)`.

**Signature:**

```lua
texture, name = GetPossessInfo(index)
```

**Arguments:**

- `index` - Index of a possession bar action (between 1 and `NUM_POSSESS_SLOTS`) (`number`)

**Returns:**

- `texture` - Path to an icon texture for the action (`string`)
- `name` - The name of the spell in the queried possess bar slot. (`string`)

---

## IsPossessBarVisible

Returns whether a special action bar should be shown while the player possesses another unit. Used in the default UI to switch between using the ShapeshiftBarFrame or PossessBarFrame to show actions belonging to the possessed unit.

**Signature:**

```lua
isVisible = IsPossessBarVisible()
```

**Returns:**

- `isVisible` - 1 if the possessed unit's actions should be shown on a special action bar (`1nil`)

---

## SetActionBarToggles

Configures display of additional ActionBars in the default UI

**Signature:**

```lua
SetActionBarToggles(bar1, bar2, bar3, bar4, alwaysShow)
```

**Arguments:**

- `bar1` - 1 to show the bottom left ActionBar; otherwise nil (`1nil`)
- `bar2` - 1 to show the bottom right ActionBar; otherwise nil (`1nil`)
- `bar3` - 1 to show the right-side ActionBar; otherwise nil (`1nil`)
- `bar4` - 1 to show the second right-side ActionBar; otherwise nil (`1nil`)
- `alwaysShow` - 1 to always show ActionBar backgrounds even for empty slots; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
