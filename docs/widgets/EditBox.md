# EditBox

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/EditBox)

EditBoxes are used to allow the player to type text into a UI component. They inherit from FontInstance as well as Frame in order to provide the needed support for text display, and add methods for entering text, such as positioning a cursor within text, establishing character limits, controlling whether text should be displayed in password-fashion (with bullets substituted for the characters), manipulating an entry history, or controlling and responding to changes in keyboard focus.

The most common use for an EditBox is to accept chat input from the player, but they are also used for commands, configuration, and confirmation, such as requiring you to type "DELETE" before destroying a valuable item, or entering the name of a new macro.

Most EditBoxes are derived from ChatFrameEditBoxTemplate, or use the same textures to create a visible frame around the editable area.

---

## Methods

---

### EditBox:AddHistoryLine

Adds a line of text to the edit box's stored history. Once added, the user can quickly set the edit box's contents to one of these lines by pressing the up or down arrow keys. (History lines are only accessible via the arrow keys if the edit box is not in [multi-line](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/EditBox/SetMultiLine) mode.)

**Signature:**

```lua
EditBox:AddHistoryLine("text")
```

**Arguments:**

- `text` - Text to be added to the edit box's list of history lines (`string`)

---

### Frame:AllowAttributeChanges

Temporarily allows insecure code to modify the frame's attributes during combat

**Signature:**

```lua
EditBox:AllowAttributeChanges()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:CanChangeAttribute

Returns whether secure frame attributes can currently be changed. Applies only to protected frames inheriting from one of the [secure frame templates](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/secure_template); frame attributes may only be changed by non-Blizzard scripts while the player is not in combat (or for a short time after a secure script calls [`:AllowAttributeChanges()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/AllowAttributeChanges)).

**Signature:**

```lua
enabled = Frame:CanChangeAttribute()
```

**Returns:**

- `enabled` - `1` if secure frame attributes can currently be changed; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

---

### Region:CanChangeProtectedState

Returns whether protected properties of the region can be changed by non-secure scripts. Addon scripts are allowed to change protected properties for non-secure frames, or for secure frames while the player is not in combat.

**Signature:**

```lua
canChange = Region:CanChangeProtectedState()
```

**Returns:**

- `canChange` - `1` if addon scripts are currently allowed to change protected properties of the region (e.g. showing or hiding it, changing its position, or altering frame attributes); otherwise `nil` (`value`, [1nil](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#1nil))

*Inherited from [Region](Region.md)*

---

### Region:ClearAllPoints

Removes all anchor points from the region

**Signature:**

```lua
EditBox:ClearAllPoints()
```

*Inherited from [Region](Region.md)*

---

### EditBox:ClearFocus

Clears the input focus from an edit box.. Clears the input focus from an edit box. After this function is called the edit box in question will no longer receive keypresses.

**Signature:**

```lua
EditBox:ClearFocus()
```

---

### EditBox:ClearHistory

This function is not yet documented

**Signature:**

```lua
EditBox:ClearHistory()
```

---

### Region:CreateAnimationGroup

Creates a new AnimationGroup as a child of the region

**Signature:**

```lua
animationGroup = EditBox:CreateAnimationGroup(["name" [, "inheritsFrom"]])
```

*Inherited from [Region](Region.md)*

---

### Frame:CreateFontString

Creates a new [[docs/widgets/FontString|`FontString`]] as a child of the frame

**Signature:**

```lua
fontstring = EditBox:CreateFontString(["name" [, "layer" [, "inherits"]]])
```

*Inherited from [Frame](Frame.md)*

---

### Frame:CreateTexture

Creates a new [[docs/widgets/Texture|`Texture`]] as a child of the frame

**Signature:**

```lua
texture = EditBox:CreateTexture(["name" [, "layer" [, "inherits"]]])
```

*Inherited from [Frame](Frame.md)*

---

### Frame:CreateTitleRegion

Creates a title region for dragging the frame

**Signature:**

```lua
region = EditBox:CreateTitleRegion()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:DisableDrawLayer

Prevents display of all child objects of the frame on a specified graphics layer

**Signature:**

```lua
EditBox:DisableDrawLayer("layer")
```

*Inherited from [Frame](Frame.md)*

---

### Frame:EnableDrawLayer

Allows display of all child objects of the frame on a specified graphics layer

**Signature:**

```lua
Frame:EnableDrawLayer("layer")
```

**Arguments:**

- `layer` - Name of a graphics layer (`string`, [layer](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#layer))

*Inherited from [Frame](Frame.md)*

---

### Frame:EnableJoystick

Enables or disables joystick interactivity

**Signature:**

```lua
EditBox:EnableJoystick(enable)
```

*Inherited from [Frame](Frame.md)*

---

### Frame:EnableKeyboard

Enables or disables keyboard interactivity for the frame. Keyboard interactivity must be enabled in order for a frame's [`OnKeyDown`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnKeyDown), [`OnKeyUp`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnKeyUp), or [`OnChar`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnChar) scripts to be run.

**Signature:**

```lua
Frame:EnableKeyboard(enable)
```

**Arguments:**

- `enable` - True to enable keyboard interactivity; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### Frame:EnableMouse

Enables or disables mouse interactivity for the frame. Mouse interactivity must be enabled in order for a frame's mouse-related [script](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) handlers to be run.

**Signature:**

```lua
Frame:EnableMouse(enable)
```

**Arguments:**

- `enable` - True to enable mouse interactivity; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### Frame:EnableMouseWheel

Enables or disables mouse wheel interactivity for the frame. Mouse wheel interactivity must be enabled in order for a frame's [`OnMouseWheel`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnMouseWheel) script handler to be run.

**Signature:**

```lua
Frame:EnableMouseWheel(enable)
```

**Arguments:**

- `enable` - True to enable mouse wheel interactivity; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

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

### EditBox:GetAltArrowKeyMode

Returns whether arrow keys are ignored by the edit box unless the Alt key is held

**Signature:**

```lua
enabled = EditBox:GetAltArrowKeyMode()
```

**Returns:**

- `enabled` - `1` if arrow keys are ignored by the edit box unless the Alt key is held; otherwise `nil` (`1nil`)

---

### Region:GetAnimationGroups

Returns a list of animation groups belonging to the region

**Signature:**

```lua
... = EditBox:GetAnimationGroups()
```

*Inherited from [Region](Region.md)*

---

### Frame:GetAttribute

Returns the value of a secure frame attribute. See the [secure template documentation](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/secure_template) for more information about frame attributes.

**Signature:**

```lua
value = Frame:GetAttribute("name")
```

**Arguments:**

- `name` - Name of an attribute to query (`string`)

**Returns:**

- `value` - Value of the named attribute (`value`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetBackdrop

Returns information about the frame's backdrop graphic. See [SetBackdrop](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/SetBackdrop).

**Signature:**

```lua
backdrop = Frame:GetBackdrop()
```

**Returns:**

- `backdrop` - A table containing the backdrop settings, or `nil` if the frame has no backdrop (`table`, [backdrop](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#backdrop))

*Inherited from [Frame](Frame.md)*

---

### Frame:GetBackdropBorderColor

Returns the shading color for the frame's border graphic

**Signature:**

```lua
red, green, blue, alpha = Frame:GetBackdropBorderColor()
```

**Returns:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetBackdropColor

Returns the shading color for the frame's background graphic

**Signature:**

```lua
red, green, blue, alpha = Frame:GetBackdropColor()
```

**Returns:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:GetBlinkSpeed

Returns the rate at which the text insertion blinks when the edit box is focused

**Signature:**

```lua
duration = EditBox:GetBlinkSpeed()
```

**Returns:**

- `duration` - Amount of time for which the cursor is visible during each "blink" (in seconds) (`number`)

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

### Frame:GetBoundsRect

Returns the position and dimension of the smallest area enclosing the frame and its children. This information may not match that returned by [`:GetRect()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Region/GetRect) if the frame contains textures, font strings, or child frames whose boundaries lie outside its own.

**Signature:**

```lua
left, bottom, width, height = Frame:GetBoundsRect()
```

**Returns:**

- `left` - Distance from the left edge of the screen to the left edge of the area (in pixels) (`number`)
- `bottom` - Distance from the bottom edge of the screen to the bottom of the area (in pixels) (`number`)
- `width` - Width of the area (in pixels) (`number`)
- `height` - Height of the area (in pixels) (`number`)

*Inherited from [Frame](Frame.md)*

---

### Region:GetCenter

Returns the screen coordinates of the region's center

**Signature:**

```lua
x, y = EditBox:GetCenter()
```

*Inherited from [Region](Region.md)*

---

### Frame:GetChildren

Returns a list of child frames of the frame

**Signature:**

```lua
... = Frame:GetChildren()
```

**Returns:**

- `...` - A list of the frames which are children of this frame (`list`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetClampRectInsets

Returns offsets from the frame's edges used when limiting user movement or resizing of the frame. Note: despite the name of this method, the values are all offsets along the normal axes, so to inset the frame's clamping area from its edges, the left and bottom measurements should be positive and the right and top measurements should be negative.

**Signature:**

```lua
left, right, top, bottom = Frame:GetClampRectInsets()
```

**Returns:**

- `left` - Offset from the left edge of the frame to the left edge of its clamping area (in pixels) (`number`)
- `right` - Offset from the right edge of the frame's clamping area to the right edge of the frame (in pixels) (`number`)
- `top` - Offset from the top edge of the frame's clamping area to the top edge of the frame (in pixels) (`number`)
- `bottom` - Offset from the bottom edge of the frame to the bottom edge of its clamping area (in pixels) (`number`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:GetCursorPosition

Returns the current cursor position inside a given edit box.. Returns the current cursor position inside a given edit box. The index starts at 0 at the front of the line.

**Signature:**

```lua
position = EditBox:GetCursorPosition()
```

**Returns:**

- `position` - The position of the cursor (`number`)

---

### Frame:GetDepth

Returns the 3D depth of the frame (for stereoscopic 3D setups)

**Signature:**

```lua
depth = Frame:GetDepth()
```

**Returns:**

- `depth` - Apparent 3D depth of this frame relative to that of its parent frame (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetDontSavePosition

This function is not yet documented

**Signature:**

```lua
EditBox:GetDontSavePosition()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:GetEffectiveAlpha

Returns the overall opacity of the frame. Unlike [`:GetAlpha()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/GetAlpha) which returns the opacity of the frame relative to its parent, this function returns the absolute opacity of the frame, taking into account the relative opacity of parent frames.

**Signature:**

```lua
alpha = Frame:GetEffectiveAlpha()
```

**Returns:**

- `alpha` - Effective alpha (opacity) of the region (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetEffectiveDepth

Returns the overall 3D depth of the frame (for stereoscopic 3D configurations)

**Signature:**

```lua
depth = EditBox:GetEffectiveDepth()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:GetEffectiveScale

Returns the overall scale factor of the frame

**Signature:**

```lua
scale = EditBox:GetEffectiveScale()
```

*Inherited from [Frame](Frame.md)*

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

Returns the `Font` object from which the font instance's properties are inherited

**Signature:**

```lua
font = EditBox:GetFontObject()
```

*Inherited from [FontInstance](FontInstance.md)*

---

### Frame:GetFrameLevel

Sets the level at which the frame is layered relative to others in its strata. Frames with higher frame level are layered "in front of" frames with a lower frame level. When not set manually, a frame's level is determined by its place in the frame hierarchy -- e.g. UIParent's level is 1, children of UIParent are at level 2, children of those frames are at level 3, etc.

**Signature:**

```lua
level = Frame:GetFrameLevel()
```

**Returns:**

- `level` - Layering level of the frame relative to others in its [`frameStrata`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#frameStrata) (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetFrameStrata

Returns the general layering strata of the frame

**Signature:**

```lua
strata = Frame:GetFrameStrata()
```

**Returns:**

- `strata` - Token identifying the strata in which the frame should be layered (`string`, [frameStrata](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#frameStrata))
  - `BACKGROUND`
  - `DIALOG`
  - `FULLSCREEN`
  - `FULLSCREEN_DIALOG`
  - `HIGH`
  - `LOW`
  - `MEDIUM`
  - `PARENT`
  - `TOOLTIP`

*Inherited from [Frame](Frame.md)*

---

### Region:GetHeight

Returns the height of the region

**Signature:**

```lua
height = EditBox:GetHeight()
```

*Inherited from [Region](Region.md)*

---

### EditBox:GetHistoryLines

Returns the maximum number of history lines stored by the edit box

**Signature:**

```lua
count = EditBox:GetHistoryLines()
```

**Returns:**

- `count` - Maximum number of history lines stored by the edit box (`number`)

---

### Frame:GetHitRectInsets

Returns the insets from the frame's edges which determine its mouse-interactable area

**Signature:**

```lua
left, right, top, bottom = EditBox:GetHitRectInsets()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:GetID

Returns the frame's numeric identifier. Frame IDs have no effect on frame behavior, but can be a useful way to keep track of multiple similar frames, especially in cases where a list of frames is created from a template (such as for action buttons, loot slots, or lines in a FauxScrollFrame).

**Signature:**

```lua
id = Frame:GetID()
```

**Returns:**

- `id` - A numeric identifier for the frame (`number`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:GetIndentedWordWrap

Returns whether long lines of text are indented when wrapping

**Signature:**

```lua
indent = EditBox:GetIndentedWordWrap()
```

---

### EditBox:GetInputLanguage

Returns the currently selected keyboard input language (character set / input method)

**Signature:**

```lua
language = EditBox:GetInputLanguage()
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

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:GetJustifyV

Returns the font instance's vertical text alignment style

**Signature:**

```lua
justify = EditBox:GetJustifyV()
```

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

### EditBox:GetMaxBytes

Returns the maximum number of bytes of text allowed in the edit box

**Signature:**

```lua
maxBytes = EditBox:GetMaxBytes()
```

---

### EditBox:GetMaxLetters

Returns the maximum number of text characters allowed in the edit box

**Signature:**

```lua
maxLetters = EditBox:GetMaxLetters()
```

---

### Frame:GetMaxResize

Returns the maximum size of the frame for user resizing

**Signature:**

```lua
maxWidth, maxHeight = EditBox:GetMaxResize()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:GetMinResize

Returns the minimum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing).

**Signature:**

```lua
minWidth, minHeight = Frame:GetMinResize()
```

**Returns:**

- `minWidth` - Minimum width of the frame (in pixels), or `0` for no limit (`number`)
- `minHeight` - Minimum height of the frame (in pixels), or `0` for no limit (`number`)

*Inherited from [Frame](Frame.md)*

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

### Frame:GetNumChildren

Returns the number of child frames belonging to the frame

**Signature:**

```lua
numChildren = EditBox:GetNumChildren()
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:GetNumLetters

Returns the number of text characters in the edit box

**Signature:**

```lua
numLetters = EditBox:GetNumLetters()
```

**Returns:**

- `numLetters` - Number of text characters in the edit box (`number`)

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

### Frame:GetNumRegions

Returns the number of non-Frame child regions belonging to the frame

**Signature:**

```lua
numRegions = EditBox:GetNumRegions()
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:GetNumber

Returns the contents of the edit box as a number. Similar to [`tonumber`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/tonumber)`(editbox:`[`GetText()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/EditBox/GetText)`)`; returns `0` if the contents of the edit box cannot be converted to a number.

**Signature:**

```lua
num = EditBox:GetNumber()
```

**Returns:**

- `num` - Contents of the edit box as a number (`number`)

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

- `index` - Index of an anchor point defined for the region (between `1` and `region:`[`GetNumPoints()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Region/GetNumPoints)) (`number`)

**Returns:**

- `point` - Point on this region at which it is anchored to another (`string`, [anchorPoint](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#anchorPoint))
- `relativeTo` - Reference to the other region to which this region is anchored (`region`)
- `relativePoint` - Point on the other region to which this region is anchored (`string`, [anchorPoint](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#anchorPoint))
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

### Frame:GetRegions

Returns a list of non-Frame child regions belonging to the frame

**Signature:**

```lua
... = EditBox:GetRegions()
```

*Inherited from [Frame](Frame.md)*

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

### Frame:GetScale

Returns the frame's scale factor

**Signature:**

```lua
scale = EditBox:GetScale()
```

*Inherited from [Frame](Frame.md)*

---

### ScriptObject:GetScript

Returns the widget's handler function for a script

**Signature:**

```lua
handler = ScriptObject:GetScript("scriptType")
```

**Arguments:**

- `scriptType` - A script type; see [scripts reference](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) for details (`string`)

**Returns:**

- `handler` - The object's handler function for the script type (`function`)

*Inherited from [ScriptObject](ScriptObject.md)*

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
xOffset, yOffset = EditBox:GetShadowOffset()
```

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
spacing = EditBox:GetSpacing()
```

*Inherited from [FontInstance](FontInstance.md)*

---

### EditBox:GetText

Returns the edit box's text contents

**Signature:**

```lua
text = EditBox:GetText()
```

**Returns:**

- `text` - Text contained in the edit box (`string`)

---

### FontInstance:GetTextColor

Returns the font instance's default text color

**Signature:**

```lua
textR, textG, textB, textAlpha = EditBox:GetTextColor()
```

*Inherited from [FontInstance](FontInstance.md)*

---

### EditBox:GetTextInsets

Returns the insets from the edit box's edges which determine its interactive text area

**Signature:**

```lua
left, right, top, bottom = EditBox:GetTextInsets()
```

---

### Frame:GetTitleRegion

Returns the frame's TitleRegion object. See [`:CreateTitleRegion()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/CreateTitleRegion) for more information.

**Signature:**

```lua
region = Frame:GetTitleRegion()
```

**Returns:**

- `region` - Reference to the frame's TitleRegion object (`region`)

*Inherited from [Frame](Frame.md)*

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

### EditBox:GetUTF8CursorPosition

Returns the cursor's numeric position in the edit box, taking UTF-8 multi-byte character into account

**Signature:**

```lua
position = EditBox:GetUTF8CursorPosition()
```

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

### EditBox:HasFocus

Returns whether the edit box is currently focused for keyboard input

**Signature:**

```lua
enabled = EditBox:HasFocus()
```

**Returns:**

- `enabled` - `1` if the edit box is currently focused for keyboard input; otherwise `nil` (`1nil`)

---

### ScriptObject:HasScript

Returns whether the widget supports a script handler

**Signature:**

```lua
hasScript = EditBox:HasScript("scriptType")
```

*Inherited from [ScriptObject](ScriptObject.md)*

---

### VisibleRegion:Hide

Hides the region

**Signature:**

```lua
VisibleRegion:Hide()
```

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### EditBox:HighlightText

Selects all or a portion of the text in the edit box

**Signature:**

```lua
EditBox:HighlightText([start [, end]])
```

---

### ScriptObject:HookScript

Securely hooks a script handler. Equivalent to [`hooksecurefunc()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/hooksecurefunc) for script handlers; allows one to "post-hook" a secure handler without tainting the original.

The original handler will still be called, but the handler supplied will also be called after the original, with the same arguments. Return values from the supplied handler are discarded. Note that there is no API to remove a hook from a handler: any hooks applied will remain in place until the UI is reloaded.

If there was no prior script handler set, then this simply sets the new function as the handler for the script type.

**Signature:**

```lua
ScriptObject:HookScript("scriptType", handler)
```

**Arguments:**

- `scriptType` - Name of the [script](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) whose handler should be hooked (`string`)
- `handler` - A function to be called whenever the script handler is run (`function`)

*Inherited from [ScriptObject](ScriptObject.md)*

---

### Frame:IgnoreDepth

Sets whether the frame's depth property is ignored (for stereoscopic 3D setups). If a frame's depth property is ignored, the frame itself is not rendered with stereoscopic 3D separation, but 3D graphics within the frame may be; this property is used on the default UI's WorldFrame.

**Signature:**

```lua
Frame:IgnoreDepth(enable)
```

**Arguments:**

- `enable` - True to ignore the frame's depth property; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:Insert

Inserts text into the edit box at the current cursor position

**Signature:**

```lua
EditBox:Insert("text")
```

**Arguments:**

- `text` - Text to be inserted (`string`)

---

### EditBox:IsAutoFocus

Returns whether the edit box automatically acquires keyboard input focus

**Signature:**

```lua
enabled = EditBox:IsAutoFocus()
```

---

### Frame:IsClampedToScreen

Returns whether the frame's boundaries are limited to those of the screen

**Signature:**

```lua
enabled = EditBox:IsClampedToScreen()
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:IsCountInvisibleLetters

This function is not yet documented

**Signature:**

```lua
EditBox:IsCountInvisibleLetters()
```

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

### Frame:IsEventRegistered

Returns whether the frame is registered for a given [[docs/events|event]]

**Signature:**

```lua
registered = EditBox:IsEventRegistered("event")
```

*Inherited from [Frame](Frame.md)*

---

### Frame:IsIgnoringDepth

Returns whether the frame's depth property is ignored (for stereoscopic 3D setups)

**Signature:**

```lua
enabled = Frame:IsIgnoringDepth()
```

**Returns:**

- `enabled` - `1` if the frame's depth property is ignored; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:IsInIMECompositionMode

Returns whether the edit box is in Input Method Editor composition mode. Character composition mode is used for input methods in which multiple keypresses generate one printed character. In such input methods, the edit box's [`OnChar`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnChar) script is run for each keypress -- if the `OnChar` script should act only when a complete character is entered in the edit box, `:IsInIMECompositionMode()` can be used to test for such cases.

This mode is common in clients for languages using non-Roman characters (such as Chinese or Korean), but can still occur in client languages using Roman scripts (e.g. English) -- such as when typing accented characters on the Mac client (e.g. typing "option-u" then "e" to insert the character "ë").

**Signature:**

```lua
enabled = EditBox:IsInIMECompositionMode()
```

**Returns:**

- `enabled` - `1` if the edit box is in IME character composition mode; otherwise `nil` (`1nil`)

---

### Frame:IsJoystickEnabled

Returns whether joystick interactivity is enabled for the frame

**Signature:**

```lua
enabled = EditBox:IsJoystickEnabled()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:IsKeyboardEnabled

Returns whether keyboard interactivity is enabled for the frame

**Signature:**

```lua
enabled = EditBox:IsKeyboardEnabled()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:IsMouseEnabled

Returns whether mouse interactivity is enabled for the frame

**Signature:**

```lua
enabled = Frame:IsMouseEnabled()
```

**Returns:**

- `enabled` - `1` if mouse interactivity is enabled for the frame; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

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

### Frame:IsMouseWheelEnabled

Returns whether mouse wheel interactivity is enabled for the frame

**Signature:**

```lua
enabled = Frame:IsMouseWheelEnabled()
```

**Returns:**

- `enabled` - `1` if mouse wheel interactivity is enabled for the frame; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

---

### Frame:IsMovable

Returns whether the frame can be moved by the user

**Signature:**

```lua
movable = Frame:IsMovable()
```

**Returns:**

- `movable` - `1` if the frame can be moved by the user; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:IsMultiLine

Returns whether the edit box shows more than one line of text

**Signature:**

```lua
multiLine = EditBox:IsMultiLine()
```

**Returns:**

- `multiLine` - `1` if the edit box shows more than one line of text; otherwise `nil` (`1nil`)

---

### EditBox:IsNumeric

Returns whether the edit box only accepts numeric input

**Signature:**

```lua
enabled = EditBox:IsNumeric()
```

**Returns:**

- `enabled` - `1` if only numeric input is allowed; otherwise `nil` (`1nil`)

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

### EditBox:IsPassword

Returns whether the text entered in the edit box is masked

**Signature:**

```lua
enabled = EditBox:IsPassword()
```

**Returns:**

- `enabled` - `1` if text entered in the edit box is masked with asterisk characters (`*`); otherwise `nil` (`1nil`)

---

### Region:IsProtected

Returns whether the region is protected. Non-secure scripts may change certain properties of a protected region (e.g. showing or hiding it, changing its position, or altering frame attributes) only while the player is not in combat. Regions may be explicitly protected by Blizzard scripts or XML; other regions can become protected by becoming children of protected regions or by being positioned relative to protected regions.

**Signature:**

```lua
isProtected, explicit = Region:IsProtected()
```

**Returns:**

- `isProtected` - `1` if the region is protected; otherwise `nil` (`value`, [1nil](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#1nil))
- `explicit` - `1` if the region is explicitly protected; `nil` if the frame is only protected due to relationship with a protected region (`value`, [1nil](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#1nil))

*Inherited from [Region](Region.md)*

---

### Frame:IsResizable

Returns whether the frame can be resized by the user

**Signature:**

```lua
enabled = Frame:IsResizable()
```

**Returns:**

- `enabled` - `1` if the frame can be resized by the user; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

---

### VisibleRegion:IsShown

Returns whether the region is shown. Indicates only whether the region has been explicitly shown or hidden -- a region may be explicitly shown but not appear on screen because its parent region is hidden. See [`VisibleRegion:IsVisible()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/VisibleRegion/IsVisible) to test for actual visibility.

**Signature:**

```lua
shown = VisibleRegion:IsShown()
```

**Returns:**

- `shown` - `1` if the region is shown; otherwise `nil` (`1nil`)

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Frame:IsToplevel

Returns whether the frame is automatically raised to the front when clicked

**Signature:**

```lua
enabled = Frame:IsToplevel()
```

**Returns:**

- `enabled` - `1` if the frame is automatically raised to the front when clicked; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

---

### Frame:IsUserPlaced

Returns whether the frame is flagged for automatic saving and restoration of position and dimensions

**Signature:**

```lua
enabled = Frame:IsUserPlaced()
```

**Returns:**

- `enabled` - `1` if the frame is flagged for automatic saving and restoration of position and dimensions; otherwise `nil` (`1nil`)

*Inherited from [Frame](Frame.md)*

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

### Frame:Lower

Reduces the frame's frame level below all other frames in its strata

**Signature:**

```lua
Frame:Lower()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:Raise

Increases the frame's frame level above all other frames in its strata

**Signature:**

```lua
Frame:Raise()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:RegisterAllEvents

Registers the frame for all events. This method is recommended for debugging purposes only, as using it will cause the frame's [`OnEvent`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnEvent) script handler to be run very frequently for likely irrelevant events. (For code that needs to be run very frequently, use an [`OnUpdate`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnUpdate) script handler.)

**Signature:**

```lua
Frame:RegisterAllEvents()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:RegisterEvent

Registers the frame for an [event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events). The frame's [`OnEvent`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnEvent) script handler will be run whenever the event fires. See the event documentation for details on event arguments.

**Signature:**

```lua
Frame:RegisterEvent("event")
```

**Arguments:**

- `event` - Name of an [event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events) (`string`)

*Inherited from [Frame](Frame.md)*

---

### Frame:RegisterForDrag

Registers the frame for dragging

**Signature:**

```lua
EditBox:RegisterForDrag(...)
```

*Inherited from [Frame](Frame.md)*

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

### EditBox:SetAltArrowKeyMode

Sets whether arrow keys are ignored by the edit box unless the Alt key is held

**Signature:**

```lua
EditBox:SetAltArrowKeyMode(enable)
```

**Arguments:**

- `enable` - True to cause the edit box to ignore arrow key presses unless the Alt key is held; false to allow unmodified arrow key presses for cursor movement (`boolean`)

---

### Frame:SetAttribute

Sets a secure frame attribute

**Signature:**

```lua
EditBox:SetAttribute("name", value)
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:SetAutoFocus

Sets whether the edit box automatically acquires keyboard input focus. If auto-focus behavior is enabled, the edit box automatically acquires keyboard focus when it is shown and when no other edit box is focused.

**Signature:**

```lua
EditBox:SetAutoFocus(enable)
```

**Arguments:**

- `enable` - True to enable the edit box to automatically acquire keyboard input focus; false to disable (`boolean`)

---

### Frame:SetBackdrop

Sets a backdrop graphic for the frame

**Signature:**

```lua
EditBox:SetBackdrop(backdrop)
```

*Inherited from [Frame](Frame.md)*

---

### Frame:SetBackdropBorderColor

Sets a shading color for the frame's border graphic

**Signature:**

```lua
EditBox:SetBackdropBorderColor(red, green, blue [, alpha])
```

*Inherited from [Frame](Frame.md)*

---

### Frame:SetBackdropColor

Sets a shading color for the frame's background graphic. As with [`Texture:SetVertexColor()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Texture/SetVertexColor), this color is a shading applied to the colors of the texture image; a color of `(1, 1, 1)` allows the image's original colors to show.

**Signature:**

```lua
Frame:SetBackdropColor(red, green, blue [, alpha])
```

**Arguments:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:SetBlinkSpeed

Sets the rate at which the text insertion blinks when the edit box is focused. The speed indicates how long the cursor stays in each state (shown and hidden); e.g. if the blink speed is 0.5 (the default, the cursor is shown for one half second and then hidden for one half second (thus, a one-second cycle); if the speed is 1.0, the cursor is shown for one second and then hidden for one second (a two-second cycle).

**Signature:**

```lua
EditBox:SetBlinkSpeed(duration)
```

**Arguments:**

- `duration` - Amount of time for which the cursor is visible during each "blink" (in seconds) (`number`)

---

### Frame:SetClampRectInsets

Sets offsets from the frame's edges used when limiting user movement or resizing of the frame. Note: despite the name of this method, the parameters are offsets along the normal axes -- to inset the frame's clamping area from its edges, the left and bottom measurements should be positive and the right and top measurements should be negative.

**Signature:**

```lua
Frame:SetClampRectInsets(left, right, top, bottom)
```

**Arguments:**

- `left` - Offset from the left edge of the frame to the left edge of its clamping area (in pixels) (`number`)
- `right` - Offset from the right edge of the frame's clamping area to the right edge of the frame (in pixels) (`number`)
- `top` - Offset from the top edge of the frame's clamping area to the top edge of the frame (in pixels) (`number`)
- `bottom` - Offset from the bottom edge of the frame to the bottom edge of its clamping area (in pixels) (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetClampedToScreen

Sets whether the frame's boundaries should be limited to those of the screen. Applies to user moving/resizing of the frame (via [`:StartMoving()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartMoving), [`:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing), or [title region](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/SetTitleRegion)); attempting to move or resize the frame beyond the edges of the screen will move/resize it no further than the edge of the screen closest to the mouse position. Does not apply to programmatically setting the frame's position or size.

**Signature:**

```lua
Frame:SetClampedToScreen(enable)
```

**Arguments:**

- `enable` - True to limit the frame's boundaries to those of the screen; false to allow the frame to be moved/resized without such limits (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:SetCountInvisibleLetters

This function is not yet documented

**Signature:**

```lua
EditBox:SetCountInvisibleLetters()
```

---

### EditBox:SetCursorPosition

Sets the cursor position in the edit box

**Signature:**

```lua
EditBox:SetCursorPosition(position)
```

**Arguments:**

- `position` - New position for the keyboard input cursor (between 0, for the position before the first character, and `editbox:`[`GetNumLetters()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/EditBox/GetNumLetters), for the position after the last character) (`number`)

---

### Frame:SetDepth

Sets the 3D depth of the frame (for stereoscopic 3D configurations)

**Signature:**

```lua
Frame:SetDepth(depth)
```

**Arguments:**

- `depth` - Apparent 3D depth of this frame relative to that of its parent frame (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetDontSavePosition

This function is not yet documented

**Signature:**

```lua
EditBox:SetDontSavePosition()
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:SetFocus

Focuses the edit box for keyboard input. Only one edit box may be focused at a time; setting focus to one edit box will remove it from the currently focused edit box.

**Signature:**

```lua
EditBox:SetFocus()
```

---

### FontInstance:SetFont

Sets the font instance's basic font properties

**Signature:**

```lua
isValid = EditBox:SetFont("filename", fontHeight, "flags")
```

*Inherited from [FontInstance](FontInstance.md)*

---

### FontInstance:SetFontObject

Sets the `Font` object from which the font instance's properties are inherited

**Signature:**

```lua
EditBox:SetFontObject(object) or EditBox:SetFontObject("name")
```

*Inherited from [FontInstance](FontInstance.md)*

---

### Frame:SetFrameLevel

Sets the level at which the frame is layered relative to others in its strata. Frames with higher frame level are layered "in front of" frames with a lower frame level.

**Signature:**

```lua
Frame:SetFrameLevel(level)
```

**Arguments:**

- `level` - Layering level of the frame relative to others in its [`frameStrata`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#frameStrata) (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetFrameStrata

Sets the general layering strata of the frame. Where [frame level](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/SetFrameLevel) provides fine control over the layering of frames, frame strata provides a coarser level of layering control: frames in a higher strata always appear "in front of" frames in lower strata regardless of frame level.

**Signature:**

```lua
Frame:SetFrameStrata("strata")
```

**Arguments:**

- `strata` - Token identifying the strata in which the frame should be layered (`string`, [frameStrata](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#frameStrata))

*Inherited from [Frame](Frame.md)*

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

### EditBox:SetHistoryLines

Sets the maximum number of history lines stored by the edit box

**Signature:**

```lua
EditBox:SetHistoryLines(count)
```

---

### Frame:SetHitRectInsets

Sets the insets from the frame's edges which determine its mouse-interactable area

**Signature:**

```lua
EditBox:SetHitRectInsets(left, right, top, bottom)
```

*Inherited from [Frame](Frame.md)*

---

### Frame:SetID

Sets a numeric identifier for the frame

**Signature:**

```lua
EditBox:SetID(id)
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:SetIndentedWordWrap

Sets whether long lines of text are indented when wrapping

**Signature:**

```lua
EditBox:SetIndentedWordWrap(indent)
```

**Arguments:**

- `indent` - True to indent wrapped lines of text; false otherwise (`boolean`)

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

### EditBox:SetMaxBytes

Sets the maximum number of bytes of text allowed in the edit box. Attempts to type more than this number into the edit box will produce no results; programmatically inserting text or setting the edit box's text will truncate input to the maximum length.

Note: Unicode characters may consist of more than one byte each, so the behavior of a byte limit may differ from that of a [character limit](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/EditBox/SetMaxLetters) in practical use.

**Signature:**

```lua
EditBox:SetMaxBytes(maxBytes)
```

**Arguments:**

- `maxBytes` - Maximum number of text bytes allowed in the edit box, or `0` for no limit (`number`)

---

### EditBox:SetMaxLetters

Sets the maximum number of text characters allowed in the edit box. Attempts to type more than this number into the edit box will produce no results; programmatically inserting text or setting the edit box's text will truncate input to the maximum length.

**Signature:**

```lua
EditBox:SetMaxLetters(maxLetters)
```

**Arguments:**

- `maxLetters` - Maximum number of text characters allowed in the edit box, or `0` for no limit (`number`)

---

### Frame:SetMaxResize

Sets the maximum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing).

**Signature:**

```lua
Frame:SetMaxResize(maxWidth, maxHeight)
```

**Arguments:**

- `maxWidth` - Maximum width of the frame (in pixels), or `0` for no limit (`number`)
- `maxHeight` - Maximum height of the frame (in pixels), or `0` for no limit (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetMinResize

Sets the minimum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing).

**Signature:**

```lua
Frame:SetMinResize(minWidth, minHeight)
```

**Arguments:**

- `minWidth` - Minimum width of the frame (in pixels), or `0` for no limit (`number`)
- `minHeight` - Minimum height of the frame (in pixels), or `0` for no limit (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetMovable

Sets whether the frame can be moved by the user. Enabling this property does not automatically implement behaviors allowing the frame to be dragged by the user -- such behavior must be implemented in the frame's mouse script handlers. If this property is not enabled, [`Frame:StartMoving()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartMoving) causes a Lua error.

For simple automatic frame dragging behavior, see [`Frame:CreateTitleRegion()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/CreateTitleRegion).

**Signature:**

```lua
Frame:SetMovable(enable)
```

**Arguments:**

- `enable` - True to allow the frame to be moved by the user; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### EditBox:SetMultiLine

Sets whether the edit box shows more than one line of text. When in multi-line mode, the edit box's height is determined by the number of lines shown and cannot be set directly -- enclosing the edit box in a `ScrollFrame` may prove useful in such cases.

**Signature:**

```lua
EditBox:SetMultiLine(multiLine)
```

**Arguments:**

- `multiLine` - True to allow the edit box to display more than one line of text; false for single-line display (`boolean`)

---

### EditBox:SetNumber

Sets the contents of the edit box to a number

**Signature:**

```lua
EditBox:SetNumber(num)
```

---

### EditBox:SetNumeric

Sets whether the edit box only accepts numeric input

**Signature:**

```lua
EditBox:SetNumeric(enable)
```

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

### EditBox:SetPassword

Sets whether the text entered in the edit box is masked

**Signature:**

```lua
EditBox:SetPassword(enable)
```

---

### Region:SetPoint

Sets an anchor point for the region

**Signature:**

```lua
Region:SetPoint("point" [, relativeTo [, "relativePoint" [, xOffset [, yOffset]]]])
```

**Arguments:**

- `point` - Point on this region at which it is to be anchored to another (`string`, [anchorPoint](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#anchorPoint))
- `relativeTo` - Reference to the other region to which this region is to be anchored; if `nil` or omitted, anchors the region relative to its parent (or to the screen dimensions if the region has no parent) (`region`)
- `relativePoint` - Point on the other region to which this region is to be anchored; if `nil` or omitted, defaults to the same value as `point` (`string`, [anchorPoint](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#anchorPoint))
- `xOffset` - Horizontal distance between `point` and `relativePoint` (in pixels; positive values put `point` to the right of `relativePoint`); if `nil` or omitted, defaults to `0` (`number`)
- `yOffset` - Vertical distance between `point` and `relativePoint` (in pixels; positive values put `point` below `relativePoint`); if `nil` or omitted, defaults to `0` (`number`)

*Inherited from [Region](Region.md)*

---

### Frame:SetResizable

Sets whether the frame can be resized by the user. Enabling this property does not automatically implement behaviors allowing the frame to be drag-resized by the user -- such behavior must be implemented in the frame's mouse script handlers. If this property is not enabled, [`Frame:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing) causes a Lua error.

**Signature:**

```lua
Frame:SetResizable(enable)
```

**Arguments:**

- `enable` - True to allow the frame to be resized by the user; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetScale

Sets the frame's scale factor. A frame's scale factor affects the size at which it appears on the screen relative to that of its parent. The entire interface may be scaled by changing `UIParent`'s scale factor (as can be done via the Use UI Scale setting in the default interface's Video Options panel).

**Signature:**

```lua
Frame:SetScale(scale)
```

**Arguments:**

- `scale` - Scale factor for the frame relative to its parent (`number`)

*Inherited from [Frame](Frame.md)*

---

### ScriptObject:SetScript

Sets the widget's handler function for a script

**Signature:**

```lua
ScriptObject:SetScript("scriptType", handler)
```

**Arguments:**

- `scriptType` - A script type; see [scripts](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) for details (`string`)
- `handler` - A function to become the widget's handler for the script type (`function`)

*Inherited from [ScriptObject](ScriptObject.md)*

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

### EditBox:SetText

Sets the edit box's text contents

**Signature:**

```lua
EditBox:SetText("text")
```

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

*Inherited from [FontInstance](FontInstance.md)*

---

### EditBox:SetTextInsets

Sets the insets from the edit box's edges which determine its interactive text area

**Signature:**

```lua
EditBox:SetTextInsets(left, right, top, bottom)
```

**Arguments:**

- `left` - Distance from the left edge of the edit box to the left edge of its interactive text area (in pixels) (`number`)
- `right` - Distance from the right edge of the edit box to the right edge of its interactive text area (in pixels) (`number`)
- `top` - Distance from the top edge of the edit box to the top edge of its interactive text area (in pixels) (`number`)
- `bottom` - Distance from the bottom edge of the edit box to the bottom edge of its interactive text area (in pixels) (`number`)

---

### Frame:SetToplevel

Sets whether the frame should automatically come to the front when clicked. When a frame with `Toplevel` behavior enabled is clicked, it automatically changes its [frame level](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/SetFrameLevel) such that it is greater than (and therefore drawn "in front of") all other frames in its [strata](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/SetFrameStrata).

**Signature:**

```lua
Frame:SetToplevel(enable)
```

**Arguments:**

- `enable` - True to cause the frame to automatically come to the front when clicked; false otherwise (`boolean`)

*Inherited from [Frame](Frame.md)*

---

### Frame:SetUserPlaced

Flags the frame for automatic saving and restoration of position and dimensions. The position and size of frames so flagged is automatically saved when the UI is shut down (as when quitting, logging out, or reloading) and restored when the UI next starts up (as when logging in or reloading). If the frame does not have a name (set at creation time) specified, its position will not be saved. As implied by its name, enabling this property is useful for frames which can be moved or resized by the user.

This function is automatically called with the value true when frame:StartMoving() is called.

**Signature:**

```lua
Frame:SetUserPlaced(enable)
```

**Arguments:**

- `enable` - True to enable automatic saving and restoration of the frame's position and dimensions; false to disable (`boolean`)

*Inherited from [Frame](Frame.md)*

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

### VisibleRegion:Show

Shows the region

**Signature:**

```lua
VisibleRegion:Show()
```

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Frame:StartMoving

Begins repositioning the frame via mouse movement

**Signature:**

```lua
EditBox:StartMoving()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:StartSizing

Begins resizing the frame via mouse movement

**Signature:**

```lua
Frame:StartSizing()
```

*Inherited from [Frame](Frame.md)*

---

### Region:StopAnimating

Stops any active animations involving the region or its children

**Signature:**

```lua
EditBox:StopAnimating()
```

*Inherited from [Region](Region.md)*

---

### Frame:StopMovingOrSizing

Ends movement or resizing of the frame initiated with [[docs/widgets/Frame/StartMoving|`:StartMoving()`]] or [[docs/widgets/Frame/StartSizing|`:StartSizing()`]]

**Signature:**

```lua
EditBox:StopMovingOrSizing()
```

*Inherited from [Frame](Frame.md)*

---

### EditBox:ToggleInputLanguage

Switches the edit box's language input mode

**Signature:**

```lua
EditBox:ToggleInputLanguage()
```

---

### Frame:UnregisterAllEvents

Unregisters the frame from any [[docs/events|events]] for which it is registered

**Signature:**

```lua
EditBox:UnregisterAllEvents()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:UnregisterEvent

Unregisters the frame for an event

**Signature:**

```lua
EditBox:UnregisterEvent("event")
```

*Inherited from [Frame](Frame.md)*

---

## Script Handlers

---

### OnAttributeChanged

Run when a frame attribute is changed

**Signature:**

```lua
OnAttributeChanged(self, "name", value)
```

---

### OnChar

Run for each text character typed in the frame

**Signature:**

```lua
OnChar(self, "text")
```

---

### OnCharComposition

Run when the edit box's input composition mode changes

**Signature:**

```lua
OnCharComposition(self, "text")
```

---

### OnCursorChanged

Run when the position of the text insertion cursor in the edit box changes

**Signature:**

```lua
OnCursorChanged(self, x, y, width, height)
```

---

### OnDisable

Run when the frame is disabled

**Signature:**

```lua
OnDisable(self)
```

---

### OnDragStart

Run when the mouse is dragged starting in the frame

**Signature:**

```lua
OnDragStart(self, "button")
```

---

### OnDragStop

Run when the mouse button is released after a drag started in the frame

**Signature:**

```lua
OnDragStop(self)
```

---

### OnEditFocusGained

Run when the edit box becomes focused for keyboard input

**Signature:**

```lua
OnEditFocusGained(self)
```

---

### OnEditFocusLost

Run when the edit box loses keyboard input focus

**Signature:**

```lua
OnEditFocusLost(self)
```

---

### OnEnable

Run when the frame is enabled

**Signature:**

```lua
OnEnable(self)
```

---

### OnEnter

Run when the mouse cursor enters the frame's interactive area

**Signature:**

```lua
OnEnter(self, motion)
```

---

### OnEnterPressed

Run when the Enter (or Return) key is pressed while the edit box has keyboard focus

**Signature:**

```lua
OnEnterPressed(self)
```

---

### OnEscapePressed

Run when the Escape key is pressed while the edit box has keyboard focus

**Signature:**

```lua
OnEscapePressed(self)
```

---

### OnEvent

Run whenever an [[docs/events|event]] fires for which the frame is registered

**Signature:**

```lua
OnEvent(self, "event", ...)
```

---

### OnHide

Run when the frame's visbility changes to hidden

**Signature:**

```lua
OnHide(self)
```

---

### OnHyperlinkClick

Run when the mouse clicks a hyperlink in the scrolling message frame or SimpleHTML frame

**Signature:**

```lua
OnHyperlinkClick(self, "linkData", "link", "button")
```

---

### OnHyperlinkEnter

Run when the mouse moves over a hyperlink in the scrolling message frame or SimpleHTML frame

**Signature:**

```lua
OnHyperlinkEnter(self, "linkData", "link")
```

---

### OnHyperlinkLeave

Run when the mouse moves away from a hyperlink in the scrolling message frame or SimpleHTML frame

**Signature:**

```lua
OnHyperlinkLeave(self, "linkData", "link")
```

---

### OnInputLanguageChanged

Run when the edit box's language input mode changes

**Signature:**

```lua
OnInputLanguageChanged(self, "language")
```

---

### OnKeyDown

Run when a keyboard key is pressed if the frame is keyboard enabled

**Signature:**

```lua
OnKeyDown(self, "key")
```

---

### OnKeyUp

Run when a keyboard key is released if the frame is keyboard enabled

**Signature:**

```lua
OnKeyUp(self, "key")
```

---

### OnLeave

Run when the mouse cursor leaves the frame's interactive area

**Signature:**

```lua
OnLeave(self, motion)
```

---

### OnLoad

Run when the frame is created

**Signature:**

```lua
OnLoad(self)
```

---

### OnMouseDown

Run when a mouse button is pressed while the cursor is over the frame

**Signature:**

```lua
OnMouseDown(self, "button")
```

---

### OnMouseUp

Run when the mouse button is released following a mouse down action in the frame

**Signature:**

```lua
OnMouseUp(self, "button")
```

---

### OnMouseWheel

Run when the frame receives a mouse wheel scrolling action

**Signature:**

```lua
OnMouseWheel(self, delta)
```

---

### OnReceiveDrag

Run when the mouse button is released after dragging into the frame

**Signature:**

```lua
OnReceiveDrag(self)
```

---

### OnShow

Run when the frame becomes visible

**Signature:**

```lua
OnShow(self)
```

---

### OnSizeChanged

Run when a frame's size changes

**Signature:**

```lua
OnSizeChanged(self, width, height)
```

---

### OnSpacePressed

Run when the space bar is pressed while the edit box has keyboard focus

**Signature:**

```lua
OnSpacePressed(self)
```

---

### OnTabPressed

Run when the Tab key is pressed while the edit box has keyboard focus

**Signature:**

```lua
OnTabPressed(self)
```

---

### OnTextChanged

Run when the edit box's text is changed

**Signature:**

```lua
OnTextChanged(self, userInput)
```

---

### OnTextSet

Run when the edit box's text is set programmatically

**Signature:**

```lua
OnTextSet(self)
```

---

### OnUpdate

Run each time the screen is drawn by the game engine

**Signature:**

```lua
OnUpdate(self, elapsed)
```

---

← [Widgets](../Widgets.md)
