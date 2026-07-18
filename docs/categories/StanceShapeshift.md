# Stance/Shapeshift functions

← [WoW API Docs](../index.md)

**6** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#stance)

---

## CancelShapeshiftForm

Cancels the current shapeshift form. Unlike other Shapeshift APIs, this function refers specifically to shapeshifting -- therefore including some abilities not found on the default UI's ShapeshiftBar and excluding some which are. For example, cancels shaman Ghost Wolf form and druid shapeshifts but not warrior stances, paladin auras, or rogue stealth.

**Signature:**

```lua
CancelShapeshiftForm()
```

---

## CastShapeshiftForm `protected`

Casts an ability on the stance/shapeshift bar

**Signature:**

```lua
CastShapeshiftForm(index)
```

**Arguments:**

- `index` - Index of an ability on the stance/shapeshift bar (between 1 and [`GetNumShapeshiftForms()`](https://web.archive.org/web/20100105231313/http://wowprogramming.com/docs/api/GetNumShapeshiftForms)) (`number`)

---

## GetNumShapeshiftForms

Returns the number of abilities to be presented on the stance/shapeshift bar

**Signature:**

```lua
numForms = GetNumShapeshiftForms()
```

**Returns:**

- `numForms` - Number of abilities to be presented on the stance/shapeshift bar (`number`)

---

## GetShapeshiftForm

Returns the index of the active ability on the stance/shapeshift bar

**Signature:**

```lua
index = GetShapeshiftForm()
```

**Returns:**

- `index` - Index of the active ability on the stance/shapeshift bar (between 1 and [`GetNumShapeshiftForms()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumShapeshiftForms)) (`number`)

---

## GetShapeshiftFormCooldown

Returns cooldown information about an ability on the stance/shapeshift bar

**Signature:**

```lua
start, duration, enable = GetShapeshiftFormCooldown(index)
```

**Arguments:**

- `index` - Index of an ability on the stance/shapeshift bar (between 1 and [`GetNumShapeshiftForms()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumShapeshiftForms)) (`number`)

**Returns:**

- `start` - The value of [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime) at the moment the cooldown began, or 0 if the ability is ready (`number`)
- `duration` - The length of the cooldown, or 0 if the ability is ready (`number`)
- `enable` - 1 if a Cooldown UI element should be used to display the cooldown, otherwise 0. (Does not always correlate with whether the ability is ready.) (`number`)

---

## GetShapeshiftFormInfo

Returns information about a shapeshift form

**Signature:**

```lua
texture, name, isActive, isCastable = GetShapeshiftFormInfo(index)
```

**Arguments:**

- `index` - The index of a shapeshift form (`number`)

**Returns:**

- `texture` - The path to the shapeshift form's icon texture (`string`)
- `name` - The name of the shapeshift form (`string`)
- `isActive` - 1 if the shapeshift form is currently active, otherwise nil (`1nil`)
- `isCastable` - 1 if the shapeshift form is currently castable, otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
