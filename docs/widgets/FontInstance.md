# FontInstance

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/FontInstance)

FontInstance is an abstract UI type that groups together the functionality of text-based frames, such as Buttons, MessageFrames, EditBoxes, SimpleHTML frames, and abstract Font objects. Methods are provided for setting text color and changing other aspects of font display like typeface, size, justification, shadow and spacing.

---

## Methods

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

---

### FontInstance:GetFontObject

Returns the `Font` object from which the font instance's properties are inherited

**Signature:**

```lua
font = FontInstance:GetFontObject()
```

---

### FontInstance:GetJustifyH

Returns the font instance's horizontal text alignment style

**Signature:**

```lua
justify = FontInstance:GetJustifyH()
```

**Returns:**

- `justify` - Horizontal text alignment style (`string`, [justifyH](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#justifyH))
  - `CENTER`
  - `LEFT`
  - `RIGHT`

---

### FontInstance:GetJustifyV

Returns the font instance's vertical text alignment style

**Signature:**

```lua
justify = FontInstance:GetJustifyV()
```

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

---

### FontInstance:GetShadowOffset

Returns the offset of the font instance's text shadow from its text

**Signature:**

```lua
xOffset, yOffset = FontInstance:GetShadowOffset()
```

---

### FontInstance:GetSpacing

Returns the font instance's amount of spacing between lines

**Signature:**

```lua
spacing = FontInstance:GetSpacing()
```

---

### FontInstance:GetTextColor

Returns the font instance's default text color

**Signature:**

```lua
textR, textG, textB, textAlpha = FontInstance:GetTextColor()
```

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

### FontInstance:SetFont

Sets the font instance's basic font properties

**Signature:**

```lua
isValid = FontInstance:SetFont("filename", fontHeight, "flags")
```

---

### FontInstance:SetFontObject

Sets the `Font` object from which the font instance's properties are inherited

**Signature:**

```lua
FontInstance:SetFontObject(object) or FontInstance:SetFontObject("name")
```

---

### FontInstance:SetJustifyH

Sets the font instance's horizontal text alignment style

**Signature:**

```lua
FontInstance:SetJustifyH("justify")
```

**Arguments:**

- `justify` - Horizontal text alignment style (`string`, [justifyH](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#justifyH))
  - `CENTER`
  - `LEFT`
  - `RIGHT`

---

### FontInstance:SetJustifyV

sets the vertical justification.

**Signature:**

```lua
FontInstance:SetJustifyV()
```

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

---

### FontInstance:SetSpacing

Sets the font instance's amount of spacing between lines

**Signature:**

```lua
FontInstance:SetSpacing(spacing)
```

**Arguments:**

- `spacing` - Amount of space between lines of text (in pixels) (`number`)

---

### FontInstance:SetTextColor

Sets the font instance's default text color. This color is used for otherwise unformatted text displayed using the font instance; however, portions of the text may be colored differently using the [`colorString`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#colorString) format (commonly seen in [`hyperlink`s](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink)).

**Signature:**

```lua
FontInstance:SetTextColor(textR, textG, textB, textAlpha)
```

**Arguments:**

- `textR` - Red component of the text color (0.0 - 1.0) (`number`)
- `textG` - Green component of the text color (0.0 - 1.0) (`number`)
- `textB` - Blue component of the text color (0.0 - 1.0) (`number`)
- `textAlpha` - Alpha (opacity) of the text (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

---

← [Widgets](../Widgets.md)
