# Barbershop functions

← [WoW API Docs](../index.md)

**9** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#barber)

---

## ApplyBarberShopStyle

Purchases the selected barber shop style changes. Does not exit the barber shop session, so further changes are still allowed.

The `BARBER_SHOP_SUCCESS` and `BARBER_SHOP_APPEARANCE_APPLIED` events fire once the style change takes effect.

**Signature:**

```lua
ApplyBarberShopStyle()
```

---

## BarberShopReset

Resets barber shop options to the currently worn styles. Changes the underlying data (and thus the character's appearance) only; the default barbershop UI does not update.

**Signature:**

```lua
BarberShopReset()
```

---

## CanAlterSkin

Lets you check if the player can change their skin color. Returns true if the player can change their skin color while using the barbershop.

**Signature:**

```lua
canAlter = CanAlterSkin()
```

**Returns:**

- `canAlter` - Can the player change skin color (`boolean`)

---

## CancelBarberShop

Exits a barber shop session. Causes the player character to stand up, returning to the normal world, and fires the `BARBER_SHOP_CLOSE` event. Any style changes already paid for (with [`ApplyBarberShopStyle()`](https://web.archive.org/web/20111212170217/http://wowprogramming.com/docs/api/ApplyBarberShopStyle)) are kept; any changes since are discarded.

**Signature:**

```lua
CancelBarberShop()
```

---

## GetBarberShopStyleInfo

Returns information about the selected barber shop style option

**Signature:**

```lua
name, unused, cost, isCurrent = GetBarberShopStyleInfo(styleIndex)
```

**Arguments:**

- `styleIndex` - Index of a style option (`number`)
  - `1` - Hair (or Horn) Style
  - `2` - Hair (or Horn) Color
  - `3` - Varies by race and gender: Facial Hair, Earrings, Features, Hair, Horns, Markings, Normal, Piercings, or Tusks

**Returns:**

- `name` - Name of the style option, or nil if the style is not named (`string`)
- `unused` - Currently unused (`string`)
- `cost` - Price of applying the style option, not including changes to other style options (in copper) (`number`)
- `isCurrent` - 1 if the style option matches the character's existing style; otherwise nil (`1nil`)

---

## GetBarberShopTotalCost

Returns the total price of selected barber shop style changes

**Signature:**

```lua
cost = GetBarberShopTotalCost()
```

**Returns:**

- `cost` - Price of the barber shop style change (in copper) (`number`)

---

## GetFacialHairCustomization

Returns a token used for displaying facial feature customization options. The token referred to by this function can be used to look up a global variable containing localized names for the customization options available to the player's race at character creation time and in the Barbershop UI; see example.

**Signature:**

```lua
token = GetFacialHairCustomization()
```

**Returns:**

- `token` - Part of a localized string token for displaying facial feature options for the player's race (`string`)

---

## GetHairCustomization

Returns a token used for displaying "hair" customization options. The token referred to by this function can be used to look up a global variable containing localized names for the customization options available to the player's race at character creation time and in the Barbershop UI; see example.

**Signature:**

```lua
token = GetHairCustomization()
```

**Returns:**

- `token` - Part of a localized string token for displaying "hair" options for the player's race (`string`)

**Examples:**

```lua
-- prints localized names for customization options
-- e.g. "Hair Style"/"Hair Color" or "Horn Style"/"Horn Color"
local token = GetHairCustomization();
print(_G["HAIR_"..token.."_STYLE"]);
print(_G["HAIR_"..token.."_COLOR"]);
```

---

## SetNextBarberShopStyle

Selects the next style for a barber shop style option. Changes the underlying data (and thus the character's appearance) only; the default barbershop UI does not update.

**Signature:**

```lua
SetNextBarberShopStyle(styleIndex [, reverse])
```

**Arguments:**

- `styleIndex` - Index of a style option (`number`)
  - `1` - Hair (or Horn) Style
  - `2` - Hair (or Horn) Color
  - `3` - Varies by race and gender: Facial Hair, Earrings, Features, Hair, Horns, Markings, Normal, Piercings, or Tusks
- `reverse` - True to select the previous style; false or omitted to select the next (`boolean`)

---

← [WoW API Docs](../index.md)
