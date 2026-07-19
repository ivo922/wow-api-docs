# Keybind functions

← [WoW API Docs](../index.md)

**21** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#binding)

---

## ClearOverrideBindings

Clears any registered override bindings for a given owner. An override binding is a temporary key or click binding that can be used to override the default bindings. The bound key will revert to its normal setting once the override has been removed.

**Signature:**

```lua
ClearOverrideBindings(owner)
```

**Arguments:**

- `owner` - A Frame (or other [widget](../Widgets.md)) object for which override bindings are registered (`table`)

---

## GetBinding

Returns information about a key binding

**Signature:**

```lua
commandName, binding1, binding2 = GetBinding(index)
```

**Arguments:**

- `index` - Index in the key bindings list (between 1 and [`GetNumBindings()`](Keybind.md#getnumbindings)) (`number`)

**Returns:**

- `commandName` - Name of the binding command (`string`)
- `binding1` - First key binding for the command, or nil if no key is bound (`string`, [binding](../types/binding.md))
- `binding2` - Second key binding for the command, or nil if no key is bound (`string`, [binding](../types/binding.md))

---

## GetBindingAction

Returns the action bound to a key or key combination

**Signature:**

```lua
action = GetBindingAction("key" [, checkOverride])
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `checkOverride` - True to check possible override bindings for the `key`, false or omitted to check only normal bindings (`boolean`)

**Returns:**

- `action` - Name of the action associated with the key, or the empty string (`""`) if the key is not bound to an action (`string`)

---

## GetBindingByKey

Returns the action bound to a key or key combination

**Signature:**

```lua
action = GetBindingByKey("key")
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))

**Returns:**

- `action` - Name of the action associated with the key, or the empty string (`""`) if the key is not bound to an action (`string`)

---

## GetBindingKey

Returns the key combinations for a given binding command. Although the default UI only allows two combinations to be bound to a command, more than two can be set via the API.

**Signature:**

```lua
key1, ... = GetBindingKey("COMMAND")
```

**Arguments:**

- `COMMAND` - Name of a binding command (`string`)

**Returns:**

- `key1` - First key binding for the command, or nil if no key is bound (`string`, [binding](../types/binding.md))
- `...` - A list of additional [bindings](../types/binding.md) for the command (`list`)

---

## GetCurrentBindingSet

Returns which set of key bindings is currently in use

**Signature:**

```lua
bindingSet = GetCurrentBindingSet()
```

**Returns:**

- `bindingSet` - Set of bindings currently in use (`number`)
  - `1` - Key bindings shared by all characters
  - `2` - Character specific key bindings

---

## GetNumBindings

Returns the number of entries in the key bindings list

**Signature:**

```lua
numBindings = GetNumBindings()
```

**Returns:**

- `numBindings` - Number of binding actions (and headers) in the key bindings list (`number`)

---

## LoadBindings

Loads a set of key bindings. The [`UPDATE_BINDINGS`](../events/UPDATE_BINDINGS.md) event fires when the new bindings have taken effect.

**Signature:**

```lua
LoadBindings(set)
```

**Arguments:**

- `set` - A set of key bindings to load (`number`)
  - `0` - Default key bindings
  - `1` - Account-wide key bindings
  - `2` - Character-specific key bindings

---

## RunBinding

Runs the script associated with a key binding action. Note: this function is not protected, but the scripts for many default key binding actions are (and can only be called by the Blizzard UI).

**Signature:**

```lua
RunBinding("COMMAND")
```

**Arguments:**

- `COMMAND` - Name of a key binding command (`string`)

---

## SaveBindings

Saves the current set of key bindings

**Signature:**

```lua
SaveBindings(set)
```

**Arguments:**

- `set` - A set to which to save the current bindings (`number`)
  - `1` - Account-wide key bindings
  - `2` - Character-specific key bindings

---

## SetBinding

Binds a key combination to a binding command

**Signature:**

```lua
success = SetBinding("key" [, "command"])
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `command` - Name of a key binding command, or nil to unbind the key (`string`)

**Returns:**

- `success` - 1 if the key binding (or unbinding) was successful; otherwise nil (`1nil`)

---

## SetBindingClick

Binds a key combination to "click" a Button object. When the binding is used, all of the relevant mouse handlers on the button (save for `OnEnter` and `OnLeave`) fire just as if the button were activated by the mouse (including `OnMouseDown` and `OnMouseUp` as the key is pressed and released).

**Signature:**

```lua
success = SetBindingClick("key", "buttonName" [, "mouseButton"])
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `buttonName` - Name of a [Button](../widgets/Button.md) object on which the binding simulates a click (`string`)
- `mouseButton` - Name of the mouse button with which the binding simulates a click (`string`)

**Returns:**

- `success` - 1 if the key binding was successful; otherwise nil (`1nil`)

---

## SetBindingItem

Binds a key combination to use an item in the player's possession

**Signature:**

```lua
success = SetBindingItem("key", itemID) or SetBindingItem("key", "itemName") or SetBindingItem("key", "itemLink")
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

**Returns:**

- `success` - 1 if the binding was successful; otherwise nil (`1nil`)

---

## SetBindingMacro

Binds a key combination to run a macro

**Signature:**

```lua
success = SetBindingMacro("key", index) or SetBindingMacro("key", "name")
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `index` - Index of a macro (`number`, [macroID](../types/macroID.md))
- `name` - Name of a macro (`string`)

**Returns:**

- `success` - 1 if the key binding was successful; otherwise nil (`1nil`)

---

## SetBindingSpell

Binds a key combination to cast a spell

**Signature:**

```lua
success = SetBindingSpell("key", "spellname")
```

**Arguments:**

- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `spellname` - Name of a spell to bind (`string`)

**Returns:**

- `success` - 1 if the key binding was successful; otherwise nil (`1nil`)

---

## SetMouselookOverrideBinding

Overrides the default mouselook bindings to perform another binding with the mouse buttons

**Signature:**

```lua
SetMouselookOverrideBinding("key", "binding")
```

**Arguments:**

- `key` - The mouselook key to override (`string`)
  - `BUTTON1` - Override the left mouse button
  - `BUTTON2` - Override the right mouse button
- `binding` - The binding to perform instead of mouselooking, or nil to clear the override (`string`)

---

## SetOverrideBinding

Sets an override binding for a binding command. Override bindings are temporary. The bound key will revert to its normal setting once the override is removed. Priority overrides work the same way but will revert to the previous override binding (if present) rather than the base binding for the key.

Call with a fourth argument of `nil` to remove the override binding for a specific key, or see [`ClearOverrideBindings()`](Keybind.md#clearoverridebindings) to remove all bindings associated with a given `owner`.

**Signature:**

```lua
SetOverrideBinding(owner, isPriority, "key", "command")
```

**Arguments:**

- `owner` - The Frame (or other [widget](../Widgets.md)) object responsible for this override (`table`)
- `isPriority` - True if this binding takes higher priority than other override bindings; false otherwise (`boolean`)
- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `command` - Name of a key binding command, or nil to remove the override binding (`string`)

---

## SetOverrideBindingClick

Sets an override binding to "click" a Button object. Override bindings are temporary. The bound key will revert to its normal setting once the override is removed. Priority overrides work the same way but will revert to the previous override binding (if present) rather than the base binding for the key.

Call with a fourth argument of `nil` to remove the override binding for a specific key, or see [`ClearOverrideBindings()`](Keybind.md#clearoverridebindings) to remove all bindings associated with a given `owner`.

**Signature:**

```lua
SetOverrideBindingClick(owner, isPriority, "key", "buttonName" [, "mouseButton"])
```

**Arguments:**

- `owner` - The Frame (or other [widget](../Widgets.md)) object responsible for this override (`table`)
- `isPriority` - True if this binding takes higher priority than other override bindings; false otherwise (`boolean`)
- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `buttonName` - Name of a [Button](../widgets/Button.md) object on which the binding simulates a click (`string`)
- `mouseButton` - Name of the mouse button with which the binding simulates a click (`string`)

---

## SetOverrideBindingItem

Sets an override binding to use an item in the player's possession. Override bindings are temporary. The bound key will revert to its normal setting once the override is removed. Priority overrides work the same way but will revert to the previous override binding (if present) rather than the base binding for the key.

Call with a fourth argument of `nil` to remove the override binding for a specific key, or see [`ClearOverrideBindings()`](Keybind.md#clearoverridebindings) to remove all bindings associated with a given `owner`.

**Signature:**

```lua
SetOverrideBindingItem(owner, isPriority, "key", itemID) or SetOverrideBindingItem(owner, isPriority, "key", "itemName") or SetOverrideBindingItem(owner, isPriority, "key", "itemLink")
```

**Arguments:**

- `owner` - The Frame (or other [widget](../Widgets.md)) object responsible for this override (`table`)
- `isPriority` - True if this binding takes higher priority than other override bindings; false otherwise (`boolean`)
- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)

---

## SetOverrideBindingMacro

Sets an override binding to run a macro. Override bindings are temporary. The bound key will revert to its normal setting once the override is removed. Priority overrides work the same way but will revert to the previous override binding (if present) rather than the base binding for the key.

Call with a fourth argument of `nil` to remove the override binding for a specific key, or see [`ClearOverrideBindings()`](Keybind.md#clearoverridebindings) to remove all bindings associated with a given `owner`.

**Signature:**

```lua
SetOverrideBindingMacro(owner, isPriority, "key", index) or SetOverrideBindingMacro(owner, isPriority, "key", "name")
```

**Arguments:**

- `owner` - The Frame (or other [widget](../Widgets.md)) object responsible for this override (`table`)
- `isPriority` - True if this binding takes higher priority than other override bindings; false otherwise (`boolean`)
- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `index` - Index of a macro (`number`, [macroID](../types/macroID.md))
- `name` - Name of a macro (`string`)

---

## SetOverrideBindingSpell

Set an override binding to a specific spell. Override bindings are temporary. The bound key will revert to its normal setting once the override is removed. Priority overrides work the same way but will revert to the previous override binding (if present) rather than the base binding for the key. See [`ClearOverrideBindings()`](Keybind.md#clearoverridebindings) to remove bindings associated with a given `owner`.

**Signature:**

```lua
SetOverrideBindingSpell(owner, isPriority, "key", "spellname")
```

**Arguments:**

- `owner` - The Frame (or other [widget](../Widgets.md)) object responsible for this override (`table`)
- `isPriority` - True if this binding takes higher priority than other override bindings; false otherwise (`boolean`)
- `key` - A key or key combination (e.g. "CTRL-2") (`string`, [binding](../types/binding.md))
- `spellname` - Name of a spell, or nil to remove the override binding (`string`)

---

← [WoW API Docs](../index.md)
