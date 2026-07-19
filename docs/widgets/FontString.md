# FontString

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/FontString)

FontStrings are one of the two types of Region that is visible on the screen. It draws a block of text on the screen using the characteristics in an associated FontObject. You can change the text contents of it, set it to use a new FontObject, and set how it handles text that doesn't fit in its normal dimensions, such as how to wrap the text and whether to indent subsequent lines.

FontStrings are used widely through the UI, to display labels on controls, the names of units, keybindings on action buttons, health and mana values, and most other text data.

---

## Methods

---

### Region:CanChangeProtectedState

Returns whether protected properties of the region can be changed by non-secure scripts. Addon scripts are allowed to change protected properties for non-secure frames, or for secure frames while the player is not in combat.

**Signature:**

```lua
canChange = Region:CanChangeProtectedState()
```

**Returns:**

- `canChange` - `1` if addon scripts are currently allowed to change protected properties of the region (e.g. showing or hiding it, changing its position, or altering frame attributes); otherwise `nil` (`value`, [1nil](../types/1nil.md))

*Inherited from [Region](Region.md)*

---

### FontString:CanNonSpaceWrap

Returns whether long lines of text will wrap within or between words

**Signature:**

```lua
enabled = FontString:CanNonSpaceWrap()
```

**Returns:**

- `enabled` - `1` if long lines of text will wrap at any character boundary (i.e possibly in the middle of a word); `nil` to only wrap at whitespace characters (i.e. only between words) (`1nil`)

---

### FontString:CanWordWrap

Returns whether long lines of text in the font string can wrap onto subsequent lines

**Signature:**

```lua
enabled = FontString:CanWordWrap()
```

**Returns:**

- `enabled` - `1` if long lines of text can wrap onto subsequent lines; otherwise `nil` (`1nil`)

---

### Region:ClearAllPoints

Clear all anchor point for the given region

**Signature:**

```lua
Region:ClearAllPoints()
```

*Inherited from [Region](Region.md)*

---

### Region:CreateAnimationGroup

Create and return a new AnimationGroup as a child of this Region

**Signature:**

```lua
Region:CreateAnimationGroup(["name" [, "inheritsFrom"]])
```

**Arguments:**

- `name` - A global name to use for the new animation group (`string`)
- `inheritsFrom` - A template from which the new animation group should inherit (`string`)

*Inherited from [Region](Region.md)*

---

### VisibleRegion:GetAlpha

Returns the opacity of the region relative to its parent

**Signature:**

```lua
alpha = VisibleRegion:GetAlpha()
```

**Returns:**

- `alpha` - Alpha (opacity) of the region (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Region:GetAnimationGroups

Returns a list of animation groups belonging to this region

**Signature:**

```lua
... = Region:GetAnimationGroups()
```

**Returns:**

- `...` - The list of animation groups belonging to this region (`list of AnimationGroup`)

*Inherited from [Region](Region.md)*

---

### Region:GetBottom

Returns the distance from the bottom of the screen to the bottom of the region

**Signature:**

```lua
bottom = Region:GetBottom()
```

**Returns:**

- `bottom` - Distance from the bottom edge of the screen to the bottom edge of the region (in pixels) (`number`)

*Inherited from [Region](Region.md)*

---

### Region:GetCenter

Returns the screen coordinates of the Region's center.

**Signature:**

```lua
Region:GetCenter()
```

*Inherited from [Region](Region.md)*

---

### LayeredRegion:GetDrawLayer

Returns the layer at which the region's graphics are drawn relative to others in its frame

**Signature:**

```lua
layer = LayeredRegion:GetDrawLayer()
```

**Returns:**

- `layer` - String identifying a graphics layer; one of the following values: (`string`, [layer](../types/layer.md))
  - `ARTWORK`
  - `BACKGROUND`
  - `BORDER`
  - `HIGHLIGHT`
  - `OVERLAY`

*Inherited from [LayeredRegion](LayeredRegion.md)*

---

### FontString:GetFieldSize

This function is not yet documented

**Signature:**

```lua
FontString:GetFieldSize()
```

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

### Region:GetHeight

Returns the height of the region.

**Signature:**

```lua
Region:GetHeight()
```

*Inherited from [Region](Region.md)*

---

### FontString:GetIndentedWordWrap

This function is not yet documented

**Signature:**

```lua
FontString:GetIndentedWordWrap()
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

### Region:GetLeft

Returns the distance from the left edge of the screen to the left edge of the region

**Signature:**

```lua
left = Region:GetLeft()
```

**Returns:**

- `left` - Distance from the left edge of the screen to the left edge of the region (in pixels) (`number`)

*Inherited from [Region](Region.md)*

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

### Region:GetNumPoints

Returns the number of anchor points defined for the region

**Signature:**

```lua
numPoints = Region:GetNumPoints()
```

**Returns:**

- `numPoints` - Number of defined anchor points for the region (`number`)

*Inherited from [Region](Region.md)*

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

### ParentedObject:GetParent

Returns the object's parent object

**Signature:**

```lua
parent = ParentedObject:GetParent()
```

**Returns:**

- `parent` - Reference to the object's parent object, or `nil` if the object has no parent (`uiobject`)

*Inherited from [ParentedObject](ParentedObject.md)*

---

### Region:GetPoint

Returns information about one of the region's anchor points

**Signature:**

```lua
point, relativeTo, relativePoint, xOffset, yOffset = Region:GetPoint(index)
```

**Arguments:**

- `index` - Index of an anchor point defined for the region (between `1` and `region:`[`GetNumPoints()`](Region.md#regiongetnumpoints)) (`number`)

**Returns:**

- `point` - Point on this region at which it is anchored to another (`string`, [anchorPoint](../types/anchorPoint.md))
- `relativeTo` - Reference to the other region to which this region is anchored (`region`)
- `relativePoint` - Point on the other region to which this region is anchored (`string`, [anchorPoint](../types/anchorPoint.md))
- `xOffset` - Horizontal distance between `point` and `relativePoint` (in pixels; positive values put `point` to the right of `relativePoint`) (`number`)
- `yOffset` - Vertical distance between `point` and `relativePoint` (in pixels; positive values put `point` below `relativePoint`) (`number`)

*Inherited from [Region](Region.md)*

---

### Region:GetRect

Returns the position and dimensions of the region

**Signature:**

```lua
left, bottom, width, height = Region:GetRect()
```

**Returns:**

- `left` - Distance from the left edge of the screen to the left edge of the region (in pixels) (`number`)
- `bottom` - Distance from the bottom edge of the screen to the bottom of the region (in pixels) (`number`)
- `width` - Width of the region (in pixels) (`number`)
- `height` - Height of the region (in pixels) (`number`)

*Inherited from [Region](Region.md)*

---

### Region:GetRight

Returns the distance from the left edge of the screen to the right edge of the region

**Signature:**

```lua
right = Region:GetRight()
```

**Returns:**

- `right` - Distance from the left edge of the screen to the right edge of the region (in pixels) (`number`)

*Inherited from [Region](Region.md)*

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

### Region:GetSize

Returns the width and height of the region

**Signature:**

```lua
width, height = Region:GetSize()
```

**Returns:**

- `width` - The width of the region (`number`)
- `height` - The height of the region (`number`)

*Inherited from [Region](Region.md)*

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

### FontString:GetStringHeight

Returns the height of the text displayed in the font string. This value is based on the text currently displayed; e.g. a long block of text wrapped to several lines results in a greater height than that for a short block of text that fits on fewer lines.

**Signature:**

```lua
height = FontString:GetStringHeight()
```

**Returns:**

- `height` - Height of the text currently displayed in the font string (in pixels) (`number`)

---

### FontString:GetStringWidth

Returns the width of the text displayed in the font string. This value is based on the text currently displayed; e.g. a short text label results in a smaller width than a longer block of text. Very long blocks of text that don't fit the font string's dimensions all result in similar widths, because this method measures the width of the text displayed, which is truncated with an ellipsis ("…").

**Signature:**

```lua
width = FontString:GetStringWidth()
```

**Returns:**

- `width` - Width of the text currently displayed in the font string (in pixels) (`number`)

---

### FontString:GetText

Returns the text currently set for display in the font string. This is not necessarily the text actually displayed: text that does not fit within the `FontString`'s dimensions will be truncated with an ellipsis ("…") for display.

**Signature:**

```lua
text = FontString:GetText()
```

**Returns:**

- `text` - Text to be displayed in the font string (`string`)

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

### Region:GetTop

Returns the distance from the bottom of the screen to the top of the region

**Signature:**

```lua
top = Region:GetTop()
```

**Returns:**

- `top` - Distance from the bottom edge of the screen to the top edge of the region (in pixels) (`number`)

*Inherited from [Region](Region.md)*

---

### Region:GetWidth

Returns the width of the region

**Signature:**

```lua
width = Region:GetWidth()
```

**Returns:**

- `width` - Width of the region (in pixels) (`number`)

*Inherited from [Region](Region.md)*

---

### VisibleRegion:Hide

Hides the region

**Signature:**

```lua
VisibleRegion:Hide()
```

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Region:IsDragging

Returns whether the region is currently being dragged

**Signature:**

```lua
isDragging = Region:IsDragging()
```

**Returns:**

- `isDragging` - `1` if the region (or its parent or ancestor) is currently being dragged; otherwise `nil` (`1nil`)

*Inherited from [Region](Region.md)*

---

### Region:IsMouseOver

Returns whether the mouse cursor is over the given region. This function replaces the previous `MouseIsOver` FrameXML function.

**Signature:**

```lua
isOver = Region:IsMouseOver()
```

**Returns:**

- `isOver` - `1` if the mouse is over the region; otherwise `nil` (`1nil`)

*Inherited from [Region](Region.md)*

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

### Region:IsProtected

Returns whether the region is protected. Non-secure scripts may change certain properties of a protected region (e.g. showing or hiding it, changing its position, or altering frame attributes) only while the player is not in combat. Regions may be explicitly protected by Blizzard scripts or XML; other regions can become protected by becoming children of protected regions or by being positioned relative to protected regions.

**Signature:**

```lua
isProtected, explicit = Region:IsProtected()
```

**Returns:**

- `isProtected` - `1` if the region is protected; otherwise `nil` (`value`, [1nil](../types/1nil.md))
- `explicit` - `1` if the region is explicitly protected; `nil` if the frame is only protected due to relationship with a protected region (`value`, [1nil](../types/1nil.md))

*Inherited from [Region](Region.md)*

---

### VisibleRegion:IsShown

Returns whether the region is shown. Indicates only whether the region has been explicitly shown or hidden -- a region may be explicitly shown but not appear on screen because its parent region is hidden. See [`VisibleRegion:IsVisible()`](VisibleRegion.md#visibleregionisvisible) to test for actual visibility.

**Signature:**

```lua
shown = VisibleRegion:IsShown()
```

**Returns:**

- `shown` - `1` if the region is shown; otherwise `nil` (`1nil`)

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### VisibleRegion:IsVisible

Returns whether the region is visible. A region is "visible" if it has been explicitly shown (or not explicitly hidden) and its parent region (and parent's parent, etc) is also shown.

A region may be "visible" and not appear on screen -- it may not have any anchor points set, its position and size may be outside the bounds of the screen, or it may not draw anything (e.g. a FontString with no text, a Texture with no image, or a Frame with no visible children).

**Signature:**

```lua
visible = VisibleRegion:IsVisible()
```

**Returns:**

- `visible` - `1` if the region is visible; otherwise `nil` (`1nil`)

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Region:SetAllPoints

Sets all anchor points of the region to match those of another region. If no region is specified, the region's anchor points are set to those of its parent.

**Signature:**

```lua
Region:SetAllPoints([region]) or Region:SetAllPoints(["name"])
```

**Arguments:**

- `region` - Reference to a region (`region`)
- `name` - Global name of a region (`string`)

*Inherited from [Region](Region.md)*

---

### VisibleRegion:SetAlpha

Sets the opacity of the region relative to its parent

**Signature:**

```lua
VisibleRegion:SetAlpha(alpha)
```

**Arguments:**

- `alpha` - Alpha (opacity) of the region (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### FontString:SetAlphaGradient

Creates an opacity gradient over the text in the font string. Seen in the default UI when quest text is presented by a questgiver (if the "Instant Quest Text" feature is not turned on): This method is used with a length of 30 to fade in the letters of the description, starting at the first character; then the start value is incremented in an [`OnUpdate`](Frame.md#onupdate) script, creating the animated fade-in effect.

**Signature:**

```lua
FontString:SetAlphaGradient(start, length)
```

**Arguments:**

- `start` - Character position in the font string's text at which the gradient should begin (between `0` and `string.len(fontString:`[`GetText()`](FontString.md#fontstringgettext)`) - 6`) (`number`)
- `length` - Width of the gradient in pixels, or `0` to restore the text to full opacity (`number`)

---

### LayeredRegion:SetDrawLayer

Sets the layer at which the region's graphics are drawn relative to others in its frame

**Signature:**

```lua
LayeredRegion:SetDrawLayer("layer")
```

**Arguments:**

- `layer` - String identifying a graphics layer; one of the following values: (`string`, [layer](../types/layer.md))
  - `ARTWORK`
  - `BACKGROUND`
  - `BORDER`
  - `HIGHLIGHT`
  - `OVERLAY`

*Inherited from [LayeredRegion](LayeredRegion.md)*

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

### FontString:SetFormattedText

Sets the text displayed in the font string using format specifiers. Equivalent to `:SetText(`[`format(format, ...)`](../categories/Lua library.md#format-luaapi)`)`, but does not create a throwaway Lua string object, resulting in greater memory-usage efficiency.

**Signature:**

```lua
FontString:SetFormattedText("formatString", ...)
```

**Arguments:**

- `formatString` - A string containing format specifiers (as with [`string.format()`](../categories/Lua library.md#format-luaapi)) (`string`)
- `...` - A list of values to be included in the formatted string (`list`)

---

### Region:SetHeight

Sets the region's height

**Signature:**

```lua
Region:SetHeight(height)
```

**Arguments:**

- `height` - New height for the region (in pixels); if `0`, causes the region's height to be determined automatically according to its anchor points (`number`)

*Inherited from [Region](Region.md)*

---

### FontString:SetIndentedWordWrap

This function is not yet documented

**Signature:**

```lua
FontString:SetIndentedWordWrap()
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

### FontString:SetNonSpaceWrap

Sets whether long lines of text will wrap within or between words

**Signature:**

```lua
FontString:SetNonSpaceWrap(enable)
```

**Arguments:**

- `enable` - True to wrap long lines of text at any character boundary (i.e possibly in the middle of a word); false to only wrap at whitespace characters (i.e. only between words) (`boolean`)

---

### Region:SetParent

Makes another frame the parent of this region

**Signature:**

```lua
Region:SetParent(frame) or Region:SetParent("name")
```

**Arguments:**

- `frame` - The new parent frame (`frame`)
- `name` - Global name of a frame (`string`)

*Inherited from [Region](Region.md)*

---

### Region:SetPoint

Sets an anchor point for the region

**Signature:**

```lua
Region:SetPoint("point" [, relativeTo [, "relativePoint" [, xOffset [, yOffset]]]])
```

**Arguments:**

- `point` - Point on this region at which it is to be anchored to another (`string`, [anchorPoint](../types/anchorPoint.md))
- `relativeTo` - Reference to the other region to which this region is to be anchored; if `nil` or omitted, anchors the region relative to its parent (or to the screen dimensions if the region has no parent) (`region`)
- `relativePoint` - Point on the other region to which this region is to be anchored; if `nil` or omitted, defaults to the same value as `point` (`string`, [anchorPoint](../types/anchorPoint.md))
- `xOffset` - Horizontal distance between `point` and `relativePoint` (in pixels; positive values put `point` to the right of `relativePoint`); if `nil` or omitted, defaults to `0` (`number`)
- `yOffset` - Vertical distance between `point` and `relativePoint` (in pixels; positive values put `point` below `relativePoint`); if `nil` or omitted, defaults to `0` (`number`)

*Inherited from [Region](Region.md)*

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

### Region:SetSize

Sets the size of the region to the specified values

**Signature:**

```lua
Region:SetSize(width, height)
```

**Arguments:**

- `width` - The width to set for the region (`number`)
- `height` - The height to set for the region (`number`)

*Inherited from [Region](Region.md)*

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

### FontString:SetText

Sets the text to be displayed in the font string

**Signature:**

```lua
FontString:SetText()
```

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

### FontString:SetTextHeight

Scales the font string's rendered text to a different height. This method scales the image of the text as already rendered at its existing height by the game's graphics engine -- producing an effect which is efficient enough for use in fast animations, but with reduced visual quality in the text. To re-render the text at a new point size, see [`:SetFont()`](FontInstance.md#fontinstancesetfont).

**Signature:**

```lua
FontString:SetTextHeight(height)
```

**Arguments:**

- `height` - Height (point size) to which the text should be scaled (in pixels) (`number`)

---

### LayeredRegion:SetVertexColor

Sets a color shading for the region's graphics. The effect of changing this property differs by the type of region:

For `FontString`s, this color overrides the normal text color (as set by [`FontInstance:SetTextColor()`](FontInstance.md#fontinstancesettextcolor)).

For `Texture`s, this color acts as a filter applied to the texture image: each color component value is a factor by which the corresponding component values in the image are multiplied. (See examples.)

**Signature:**

```lua
LayeredRegion:SetVertexColor(red, green, blue [, alpha])
```

**Arguments:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [LayeredRegion](LayeredRegion.md)*

---

### Region:SetWidth

Sets the region's width

**Signature:**

```lua
Region:SetWidth(width)
```

**Arguments:**

- `width` - New width for the region (in pixels); if `0`, causes the region's width to be determined automatically according to its anchor points (`number`)

*Inherited from [Region](Region.md)*

---

### FontString:SetWordWrap

Sets whether long lines of text in the font string can wrap onto subsequent lines

**Signature:**

```lua
FontString:SetWordWrap(enable)
```

**Arguments:**

- `enable` - True to allow long lines of text in the font string to wrap onto subsequent lines; false to disallow (`boolean`)

---

### VisibleRegion:Show

Shows the region

**Signature:**

```lua
VisibleRegion:Show()
```

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Region:StopAnimating

Stops any active animations involving the region or its children

**Signature:**

```lua
Region:StopAnimating()
```

*Inherited from [Region](Region.md)*

---

← [Widgets](../Widgets.md)
