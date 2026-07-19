# Type: binding

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

String identifying one or more keyboard keys or mouse buttons, used with [key binding](../index.md) and [modified click](../index.md) API functions and the [`OnKeyDown`](../widgets/Frame.md#onkeydown)/[`OnKeyUp`](../widgets/Frame.md#onkeyup) script handlers. Most letter, number, and symbol keys are identified by their (uppercase) letter, number, or symbol.

Other keys are identified by a series of global variables with names prefaced by `"KEY_"`: e.g. the localized name for the binding `NUMPAD0` can be found in `_G["KEY_NUMPAD0"]`. Some keys have platform-specific names: e.g. the localized name for the binding `PRINTSCREEN` can be found in `_G["KEY_PRINTSCREEN_MAC"]` (revealing that it refers to the F13 key found on Mac extended keyboards).

Modifier keys are identified as follows:

- `LSHIFT`, `RSHIFT`, `SHIFT` - Left, right, or generic Shift key
- `LCTRL`, `RCTRL`, `CTRL` - Left, right, or generic Control key
- `LALT`, `RALT`, `ALT` - Left, right, or generic Alt (or Option) key
- `STRG` - German equivalent to CTRL key

Mouse buttons are identified by the token `"BUTTON"` followed by the button number; e.g. `BUTTON1` for the primary (left) button, `BUTTON2` for the right button, `BUTTON3` for middle, etc.

For use in key bindings, several key/button identifiers can be strung together with hyphens to indicate a key combination; e.g. `CTRL-SHIFT-SPACE`, `RALT-F12`, `SHIFT-BUTTON1`.

---

← [API Types](../API Types.md)
