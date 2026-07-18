# Modified click functions

← [WoW API Docs](../index.md)

**5** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#modclick)

---

## GetModifiedClick

Returns the keys/buttons bound for a modified click action

**Signature:**

```lua
binding = GetModifiedClick("name")
```

**Arguments:**

- `name` - Token identifying a modified click action (`string`)

**Returns:**

- `binding` - The set of modifiers (and mouse button, if applicable) registered for the action (`string`, [binding](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#binding))

---

## GetModifiedClickAction

Returns the token identifying a modified click action

**Signature:**

```lua
action = GetModifiedClickAction(index)
```

**Arguments:**

- `index` - Index of a modified click action (between 1 and [`GetNumModifiedClickActions()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumModifiedClickActions)) (`number`)

**Returns:**

- `action` - Token identifying the modified click action, or `nil` if no action is defined at the given `index` (`string`)

---

## GetNumModifiedClickActions

Returns the number of modified click actions registered. May return an invalid result if called when no modified click actions have been registered (i.e. early in the UI loading process).

**Signature:**

```lua
num = GetNumModifiedClickActions()
```

**Returns:**

- `num` - Number of modifed click actions registered (`number`)

---

## IsModifiedClick

Determines if the modifiers specified in the click-type had been held down while the button click occurred.. If called from a click handler (`OnMouseDown`, `OnMouseUp`, `OnClick`, `OnDoubleClick`, `PreClick`, or `PostClick`), checks mouse buttons included in the binding; otherwise checks modifiers only (see example).

**Signature:**

```lua
modifiedClick = IsModifiedClick("type")
```

**Arguments:**

- `type` - Token identifying a modified click action (`string`)

**Returns:**

- `modifiedClick` - 1 if the modifier key set bound to the action is active (i.e. the keys are held down); otherwise nil (`1nil`)

---

## SetModifiedClick

Sets a modified click for a given action

**Signature:**

```lua
SetModifiedClick("action", "binding")
```

**Arguments:**

- `action` - Token identifying the modified click action (`string`)
- `binding` - The set of modifiers (and mouse button, if applicable) to register for the action (`string`, [binding](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#binding))

---

← [WoW API Docs](../index.md)
