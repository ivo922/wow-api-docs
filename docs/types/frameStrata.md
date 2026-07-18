# Type: frameStrata

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

String identifying the general layering order of frames; where [frame level](https://web.archive.org/web/20110319023203/http://wowprogramming.com/docs/widgets/Frame/SetFrameLevel) provides fine control over the layering of frames, frame strata provides a coarser level of layering control. Frames in a higher strata always appear "in front of" frames in lower strata regardless of frame level. Available frame strata are listed below in order from lowest to highest:

- `BACKGROUND` - Used by default for static UI elements such as the PlayerFrame and Minimap
- `LOW` - Used by default for lower-priority UI elements such as the party member and target frames
- `MEDIUM` - Default frame strata for general usage
- `HIGH` - Used by default for higher-priority UI elements such as the Calendar and Loot frames
- `DIALOG` - Used by default for alerts and other dialog boxes which should appear over nearly all other UI elements
- `FULLSCREEN` - Used by default for full-screen windows such as the World Map
- `FULLSCREEN_DIALOG` - Used by default for alerts or dialog boxes which should appear even when a full-screen window is visible
- `TOOLTIP` - Used for mouse cursor tooltips, ensuring they appear over all other UI elements

---

← [API Types](../API Types.md)
