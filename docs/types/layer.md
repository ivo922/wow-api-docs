# Type: layer

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

String identifying the layer in which a region's graphics are drawn relative to those of other regions in the same frame; graphics in higher layers (as numbered below) are drawn "on top of" those in lower layers.

- `BACKGROUND` - First (lowest) layer
- `BORDER` - Second layer
- `ARTWORK` - Third layer; default for regions for which layer is not specified
- `OVERLAY` - Fourth layer
- `HIGHLIGHT` - Fifth (highest) layer; regions in this layer are automatically shown when the mouse is over the containing Frame (if the Frame's enableMouse property is true).

---

← [API Types](../API Types.md)
