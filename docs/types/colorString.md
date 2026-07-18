# Type: colorString

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

Formatting used to colorize sections of text when displayed in a FontString. Color strings take the form `|c(colorvalue)(text)|r`:

- `(colorvalue)` - A string of four hexadecimal-formatted bytes describing component values of the color. Each byte can be a value from `00` (representing zero intensity of the component) to `ff` (representing full intensity of the component):
 
 Nominally alpha value, but currently unused: always `ff`.
 Red component of the color
 Green component of the color
 Blue component of the color
- `(text)` - The text to be colorized.

Examples: `|cffffff00(bright yellow)|r`, `|cff0070dd(rare item blue)|r`, `|cff40c040(easy quest green)|r`

Color strings can be used for display anywhere in the UI, can only be delivered in chat messages if used as part of a [`hyperlink`](hyperlink.md).

---

← [API Types](../API Types.md)
