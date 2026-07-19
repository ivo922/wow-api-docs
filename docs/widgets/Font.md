# Font

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/Font)

The Font object is the only type of object that is not attached to a parent widget; indeed, its purpose is to be shared between other objects that share font characteristics. In this way, changes to the Font object will update the text appearance of all text objects that have it set as their Font using `:SetFontObject()`. This allows a coder to maintain a consistent appearance between UI elements, as well as simplifying the resourcs and work required to update multiple text-based UI elements.

---

## Methods

---

### Font:CopyFontObject

Sets the font's properties to match those of another Font object. Unlike [`FontInstance:SetFontObject()`](FontInstance.md#fontinstancesetfontobject), this method allows one-time reuse of another font object's properties without continuing to inherit future changes made to the other object's properties.

**Signature:**

```lua
Font:CopyFontObject(object) or Font:CopyFontObject("name")
```

**Arguments:**

- `object` - Reference to a `Font` object (`font`)
- `name` - Global name of a `Font` object (`string`)

---

### Font:GetAlpha

Returns the opacity for text displayed by the font

**Signature:**

```lua
alpha = Font:GetAlpha()
```

**Returns:**

- `alpha` - Alpha (opacity) of the text (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

---

### FontInstance:GetFont

Returns the font instance's basic font properties

**Signature:**

```lua
filename, fontHeight, flags = FontInstance:GetFont()
```

**Returns:**

- `filename` - Path to a font file (`string`)
- `fontHeight` - Height (point size) of the font to be displayed (in pixels) (`number`)
- `flags` - Additional properties for the font specified by one or more (separated by commas) of the following tokens: (`string`)
  - `MONOCHROME` - Font is rendered without antialiasing
  - `OUTLINE` - Font is displayed with a black outline
  - `THICKOUTLINE` - Font is displayed with a thick black outline

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:GetFontObject

Returns the `Font` object from which the font instance's properties are inherited. See [`FontInstance:SetFontObject()`](FontInstance.md#fontinstancesetfontobject) for details.

**Signature:**

```lua
font = FontInstance:GetFontObject()
```

**Returns:**

- `font` - Reference to the `Font` object from which the font instance's properties are inherited, or `nil` if the font instance has no inherited properties (`font`)

*Inherited from [FontInstance](FontInstance.md)*

---

### Font:GetIndentedWordWrap

This function is not yet documented

**Signature:**

```lua
Font:GetIndentedWordWrap()
```

---

### FontInstance:GetJustifyH

Returns the font instance's horizontal text alignment style

**Signature:**

```lua
justify = FontInstance:GetJustifyH()
```

**Returns:**

- `justify` - Horizontal text alignment style (`string`, [justifyH](../types/justifyH.md))
  - `CENTER`
  - `LEFT`
  - `RIGHT`

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:GetJustifyV

Returns the font instance's vertical text alignment style

**Signature:**

```lua
justify = FontInstance:GetJustifyV()
```

**Returns:**

- `justify` - Vertical text alignment style (`string`, [justifyV](../types/justifyV.md))
  - `BOTTOM`
  - `MIDDLE`
  - `TOP`

*Inherited from [FontInstance](FontInstance.md)*

---

### UIObject:GetName

Returns the widget object's name

**Signature:**

```lua
name = UIObject:GetName()
```

**Returns:**

- `name` - Name of the object (`string`)

*Inherited from [UIObject](UIObject.md)*

---

### UIObject:GetObjectType

Returns the object's widget type

**Signature:**

```lua
type = UIObject:GetObjectType()
```

**Returns:**

- `type` - Name of the object's type (e.g. `Frame`, `Button`, `FontString`, etc.) (`string`)

*Inherited from [UIObject](UIObject.md)*

---

### FontInstance:GetShadowColor

Returns the color of the font's text shadow

**Signature:**

```lua
shadowR, shadowG, shadowB, shadowAlpha = FontInstance:GetShadowColor()
```

**Returns:**

- `shadowR` - Red component of the shadow color (0.0 - 1.0) (`number`)
- `shadowG` - Green component of the shadow color (0.0 - 1.0) (`number`)
- `shadowB` - Blue component of the shadow color (0.0 - 1.0) (`number`)
- `shadowAlpha` - Alpha (opacity) of the text's shadow (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:GetShadowOffset

Returns the offset of the font instance's text shadow from its text

**Signature:**

```lua
xOffset, yOffset = FontInstance:GetShadowOffset()
```

**Returns:**

- `xOffset` - Horizontal distance between the text and its shadow (in pixels) (`number`)
- `yOffset` - Vertical distance between the text and its shadow (in pixels) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:GetSpacing

Returns the font instance's amount of spacing between lines

**Signature:**

```lua
spacing = FontInstance:GetSpacing()
```

**Returns:**

- `spacing` - Amount of space between lines of text (in pixels) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:GetTextColor

Returns the font instance's default text color

**Signature:**

```lua
textR, textG, textB, textAlpha = FontInstance:GetTextColor()
```

**Returns:**

- `textR` - Red component of the text color (0.0 - 1.0) (`number`)
- `textG` - Green component of the text color (0.0 - 1.0) (`number`)
- `textB` - Blue component of the text color (0.0 - 1.0) (`number`)
- `textAlpha` - Alpha (opacity) of the text (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### UIObject:IsObjectType

Returns whether the object belongs to a given widget type

**Signature:**

```lua
isType = UIObject:IsObjectType("type")
```

**Arguments:**

- `type` - Name of an object type (e.g. `Frame`, `Button`, `FontString`, etc.) (`string`)

**Returns:**

- `isType` - `1` if the object belongs to the given type (or a subtype thereof); otherwise `nil` (`1nil`)

*Inherited from [UIObject](UIObject.md)*

---

### Font:SetAlpha

Sets the opacity for text displayed by the font

**Signature:**

```lua
Font:SetAlpha(alpha)
```

**Arguments:**

- `alpha` - Alpha (opacity) of the text (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

---

### FontInstance:SetFont

Sets the font instance's basic font properties. Font files included with the default WoW client:

- `Fonts\\FRIZQT__.TTF` - Friz Quadrata, used by default for player names and most UI text
- `Fonts\\ARIALN.TTF` - Arial Narrow, used by default for chat windows, action button numbers, etc.
- `Fonts\\skurri.ttf` - Skurri, used by default for incoming damage/parry/miss/etc indicators on the Player and Pet frames
- `Fonts\\MORPHEUS.ttf` - Morpheus, used by default for quest title headers, mail, and readable in-game objects.

Font files can also be included in addons.

**Signature:**

```lua
isValid = FontInstance:SetFont("filename", fontHeight, "flags")
```

**Arguments:**

- `filename` - Path to a font file (`string`)
- `fontHeight` - Height (point size) of the font to be displayed (in pixels) (`number`)
- `flags` - Additional properties for the font specified by one or more (separated by commas) of the following tokens: (`string`)
  - `MONOCHROME` - Font is rendered without antialiasing
  - `OUTLINE` - Font is displayed with a black outline
  - `THICKOUTLINE` - Font is displayed with a thick black outline

**Returns:**

- `isValid` - `1` if `filename` refers to a valid font file; otherwise `nil` (`1nil`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetFontObject

Sets the `Font` object from which the font instance's properties are inherited. This method allows for easy standardization and reuse of font styles. For example, a button's normal font can be set to appear in the same style as many default UI elements by setting its font to `"GameFontNormal"` -- if Blizzard changes the main UI font in a future patch, or if the user installs another addon which changes the main UI font, the button's font will automatically change to match.

**Signature:**

```lua
FontInstance:SetFontObject(object) or FontInstance:SetFontObject("name")
```

**Arguments:**

- `object` - Reference to a `Font` object (`font`)
- `name` - Global name of a `Font` object (`string`)

*Inherited from [FontInstance](FontInstance.md)*

---

### Font:SetIndentedWordWrap

This function is not yet documented

**Signature:**

```lua
Font:SetIndentedWordWrap()
```

---

### FontInstance:SetJustifyH

Sets the font instance's horizontal text alignment style

**Signature:**

```lua
FontInstance:SetJustifyH("justify")
```

**Arguments:**

- `justify` - Horizontal text alignment style (`string`, [justifyH](../types/justifyH.md))
  - `CENTER`
  - `LEFT`
  - `RIGHT`

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetJustifyV

sets the vertical justification.

**Signature:**

```lua
FontInstance:SetJustifyV()
```

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetShadowColor

Sets the color of the font's text shadow

**Signature:**

```lua
FontInstance:SetShadowColor(shadowR, shadowG, shadowB, shadowAlpha)
```

**Arguments:**

- `shadowR` - Red component of the shadow color (0.0 - 1.0) (`number`)
- `shadowG` - Green component of the shadow color (0.0 - 1.0) (`number`)
- `shadowB` - Blue component of the shadow color (0.0 - 1.0) (`number`)
- `shadowAlpha` - Alpha (opacity) of the text's shadow (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetShadowOffset

Sets the offset of the font instance's text shadow from its text

**Signature:**

```lua
FontInstance:SetShadowOffset(xOffset, yOffset)
```

**Arguments:**

- `xOffset` - Horizontal distance between the text and its shadow (in pixels) (`number`)
- `yOffset` - Vertical distance between the text and its shadow (in pixels) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetSpacing

Sets the font instance's amount of spacing between lines

**Signature:**

```lua
FontInstance:SetSpacing(spacing)
```

**Arguments:**

- `spacing` - Amount of space between lines of text (in pixels) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetTextColor

Sets the font instance's default text color. This color is used for otherwise unformatted text displayed using the font instance; however, portions of the text may be colored differently using the [`colorString`](../types/colorString.md) format (commonly seen in [`hyperlink`s](../types/hyperlink.md)).

**Signature:**

```lua
FontInstance:SetTextColor(textR, textG, textB, textAlpha)
```

**Arguments:**

- `textR` - Red component of the text color (0.0 - 1.0) (`number`)
- `textG` - Green component of the text color (0.0 - 1.0) (`number`)
- `textB` - Blue component of the text color (0.0 - 1.0) (`number`)
- `textAlpha` - Alpha (opacity) of the text (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [FontInstance](FontInstance.md)*

---

← [Widgets](../Widgets.md)
