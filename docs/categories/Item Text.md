# Item Text functions

← [WoW API Docs](../index.md)

**9** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#itemtext)

---

## CloseItemText

Ends interaction with a text object or item. Causes the `ITEM_TEXT_CLOSED` event to fire, indicating that ItemText APIs are no longer valid.

Called by the default UI when closing the ItemTextFrame, which is used for both readable world objects (books, plaques, gravestones, etc) and readable items (looted books, various quest-related scrolls and parchments, saved mail messages, etc).

**Signature:**

```lua
CloseItemText()
```

---

## ItemTextGetCreator

Returns the original author of the currently viewed text item. Used for mail messages sent by other players; when the player makes a permanent copy of a letter and reads it from inventory, the default UI uses this function to display a signature (e.g. "From, Leeroy") at the end of the message text.

**Signature:**

```lua
creator = ItemTextGetCreator()
```

**Returns:**

- `creator` - Creator of the text item, or nil if not available (`string`)

---

## ItemTextGetItem

Returns the name of the currently viewed text item. Used for readable world objects (plaques, books on tables, etc) and readable inventory items (looted books/parchments/scrolls/etc, saved copies of mail messages). For saved mail messages the name returned is always "Plain Letter" (or localized equivalent); the message subject is lost when saving a copy.

**Signature:**

```lua
text = ItemTextGetItem()
```

**Returns:**

- `text` - Name of the text item (`string`)

---

## ItemTextGetMaterial

Returns display style information for the currently viewed text item. The value returned can be used to look up background textures and text colors for display:

- Background textures displayed in the default UI can be found by prepending `"Interface\\ItemTextFrame\\ItemText-"` and appending `"-TopLeft"`, `"-TopRight"`, `"-BotLeft"`, `"-BotRight"` to the material string (e.g. `"Interface\\ItemTextFrame\\ItemText-Stone-TopLeft"`).
- Colors for body and title text can be found by calling `GetMaterialTextColors(material)` (a Lua function implemented in the Blizzard UI).

In cases where this function returns nil, the default UI uses the colors and textures for "Parchment".

**Signature:**

```lua
material = ItemTextGetMaterial()
```

**Returns:**

- `material` - String identifying a display style for the current text item, or nil for the default style (`string`)
  - `Bronze` - Colored metallic background
  - `Marble` - Light stone background
  - `Parchment` - Yellowed parchment background (default)
  - `Silver` - Gray metallic background
  - `Stone` - Dark stone background

---

## ItemTextGetPage

Returns the current page number in the currently viewed text item

**Signature:**

```lua
page = ItemTextGetPage()
```

**Returns:**

- `page` - Number of the currently displayed page (`number`)

---

## ItemTextGetText

Returns the text of the currently viewed text item. Used for readable world objects (plaques, books on tables, etc) and readable inventory items (looted books/parchments/scrolls/etc, saved copies of mail messages). Returns valid data only between the `ITEM_TEXT_BEGIN` and `ITEM_TEXT_CLOSED` events, with the `ITEM_TEXT_READY` event indicating when new text is available (as when changing pages).

**Signature:**

```lua
text = ItemTextGetText()
```

**Returns:**

- `text` - Text to be displayed for the current page of the currently viewed text item (`string`)

---

## ItemTextHasNextPage

Returns whether the currently viewed text item has additional pages

**Signature:**

```lua
next = ItemTextHasNextPage()
```

**Returns:**

- `next` - 1 if the currently viewed text item has one or more pages beyond the current page; otherwise nil (`1nil`)

---

## ItemTextNextPage

Moves to the next page in the currently viewed text item. The `ITEM_TEXT_READY` event fires when text for the next page becomes available. Does nothing if already viewing the last page of text.

**Signature:**

```lua
ItemTextNextPage()
```

---

## ItemTextPrevPage

Moves to the previous page in the currently viewed text item. The `ITEM_TEXT_READY` event fires when text for the previous page becomes available. Does nothing if already viewing the first page of text.

**Signature:**

```lua
ItemTextPrevPage()
```

---

← [WoW API Docs](../index.md)
