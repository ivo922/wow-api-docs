# Keyboard functions

← [WoW API Docs](../index.md)

**11** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#keyboard)

---

## GetCurrentKeyBoardFocus

Returns the frame currently handling keyboard input. Typically an EditBox

**Signature:**

```lua
frame = GetCurrentKeyBoardFocus()
```

**Returns:**

- `frame` - Frame currently handling keyboard input, or nil if no frame is currently focused (`table`)

---

## IsAltKeyDown

Returns whether an Alt key on the keyboard is held down.

**Signature:**

```lua
isDown = IsAltKeyDown()
```

**Returns:**

- `isDown` - 1 if an Alt key on the keyboard is currently held down; otherwise nil (`1nil`)

---

## IsControlKeyDown

Returns whether a Control key on the keyboard is held down

**Signature:**

```lua
isDown = IsControlKeyDown()
```

**Returns:**

- `isDown` - 1 if a Control key on the keyboard is currently held down; otherwise nil (`1nil`)

---

## IsLeftAltKeyDown

Returns whether the left Alt key is currently held down. (Note: The Mac WoW client does not distingish between left and right modifier keys, so both Alt keys are reported as Left Alt.)

**Signature:**

```lua
isDown = IsLeftAltKeyDown()
```

**Returns:**

- `isDown` - 1 if the left Alt key on the keyboard is currently held down; otherwise nil (`1nil`)

---

## IsLeftControlKeyDown

Returns whether the left Control key is held down. (Note: The Mac WoW client does not distingish between left and right modifier keys, so both Control keys are reported as Left Control.)

**Signature:**

```lua
isDown = IsLeftControlKeyDown()
```

**Returns:**

- `isDown` - 1 if the left Control key is held down; otherwise nil (`1nil`)

---

## IsLeftShiftKeyDown

Returns whether the left Shift key on the keyboard is held down. (Note: The Mac WoW client does not distingish between left and right modifier keys, so both Shift keys are reported as Left Shift.)

**Signature:**

```lua
isDown = IsLeftShiftKeyDown()
```

**Returns:**

- `isDown` - 1 if the left Shift key on the keyboard is currently held down; otherwise nil (`1nil`)

---

## IsModifierKeyDown

Returns whether a modifier key is held down. Modifier keys include shift, control or alt on either side of the keyboard. WoW does not recognize platform-specific modifier keys (such as fn, meta, Windows, or Command).

**Signature:**

```lua
isDown = IsModifierKeyDown()
```

**Returns:**

- `isDown` - 1 if any modifier key is held down; otherwise nil (`1nil`)

---

## IsRightAltKeyDown

Returns whether the right Alt key is currently held down. (Note: The Mac WoW client does not distingish between left and right modifier keys, so both Alt keys are reported as Left Alt.)

**Signature:**

```lua
isDown = IsRightAltKeyDown()
```

**Returns:**

- `isDown` - 1 if the right Alt key on the keyboard is currently held down; otherwise nil (`1nil`)

---

## IsRightControlKeyDown

Returns whether the right Control key on the keyboard is held down. (Note: The Mac WoW client does not distingish between left and right modifier keys, so both Control keys are reported as Left Control.)

**Signature:**

```lua
isDown = IsRightControlKeyDown()
```

**Returns:**

- `isDown` - 1 if the right Control key on the keyboard is held down; otherwise nil (`1nil`)

---

## IsRightShiftKeyDown

Returns whether the right shift key on the keyboard is held down. (Note: The Mac WoW client does not distingish between left and right modifier keys, so both Shift keys are reported as Left Shift.)

**Signature:**

```lua
isDown = IsRightShiftKeyDown()
```

**Returns:**

- `isDown` - 1 if the right shift key on the keyboard is currently held down; otherwise nil (`1nil`)

---

## IsShiftKeyDown

Returns whether a Shift key on the keyboard is held down

**Signature:**

```lua
isDown = IsShiftKeyDown()
```

**Returns:**

- `isDown` - 1 if a Shift key on the keyboard is currently held down; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
