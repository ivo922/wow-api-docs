# Type: backdrop

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

A backdrop definition is a Lua table with specific attributes, that match directly with the elements in the `` definition in an XML definition. It has the following structure:

```lua
{
  bgFile = "Interface\\DialogFrame\\UI-DialogBox-Gold-Background",  -- path to the background texture
  edgeFile = "Interface\\DialogFrame\\UI-DialogBox-Gold-Border",    -- path to the border texture
  tile = true,      -- true to repeat the background texture to fill the frame, false to scale it
  tileSize = 32,    -- size (width or height) of the square repeating background tiles (in pixels)
  edgeSize = 32,    -- thickness of edge segments and square size of edge corners (in pixels)
  insets = {        -- distance from the edges of the frame to those of the background texture (in pixels)
    left = 11,
    right = 12,
    top = 12,
    bottom = 11
  }
}
```

---

← [API Types](../API Types.md)
