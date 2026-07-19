# GameTooltip

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/GameTooltip)

GameTooltips are used to display explanatory information relevant to a particular element of the game world. They offer almost innumerable methods for setting the specific object, creature or ability the tooltip should describe, and a smaller number of methods for querying what it is that the tooltip is currently describing.

GameTooltips are sufficiently complicated that an entire chapter is dedicated to describing them. In addition to methods for setting their contents, they also support options controlling their positioning and visibility on screen, as well as methods to facilitate adding more text to them (for instance, an addon that displays, in the tooltip for a soul shard created by a warlock, the name of the player or monster from which the shard was collected).

While most of the heavy lifting is done by the frame called simply GameTooltip, there is also one called ItemRefTooltip that does the work of displaying information about items linked in chat when they are clicked.

---

## Methods

---

### GameTooltip:AddDoubleLine

Adds a line to the tooltip with both left-side and right-side portions. The tooltip is not automatically resized to fit the added line; to do so, call the tooltip's [`:Show()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/VisibleRegion/Show) method after adding lines.

**Signature:**

```lua
GameTooltip:AddDoubleLine("textLeft", "textRight" [, rL [, gL [, bL [, rR [, gR [, bR]]]]]])
```

**Arguments:**

- `textLeft` - Text to be displayed on the left side of the new line (`string`)
- `textRight` - Text to be displayed on the right side of the new line (`string`)
- `rL` - Red component of the color for the left-side text (0.0 - 1.0) (`number`)
- `gL` - Green component of the color for the left-side text (0.0 - 1.0) (`number`)
- `bL` - Blue component of the color for the left-side text (0.0 - 1.0) (`number`)
- `rR` - Red component of the color for the right-side text (0.0 - 1.0) (`number`)
- `gR` - Green component of the color for the right-side text (0.0 - 1.0) (`number`)
- `bR` - Blue component of the color for the right-side text (0.0 - 1.0) (`number`)

---

### GameTooltip:AddFontStrings

Adds fontstrings to the tooltip, dynamically expanding the number of lines

**Signature:**

```lua
GameTooltip:AddFontStrings()
```

---

### GameTooltip:AddLine

Adds a line of text to the tooltip. The tooltip is not automatically resized to fit the added line (and wrap it, if applicable); to do so, call the tooltip's [`:Show()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/VisibleRegion/Show) method after adding lines.

**Signature:**

```lua
GameTooltip:AddLine("text" [, r [, g [, b [, wrap]]]])
```

**Arguments:**

- `text` - Text to be added as a new line in the tooltip (`string`)
- `r` - Red component of the text color (0.0 - 1.0) (`number`)
- `g` - Green component of the text color (0.0 - 1.0) (`number`)
- `b` - Blue component of the text color (0.0 - 1.0) (`number`)
- `wrap` - True to cause the line to wrap if it is longer than other, non-wrapping lines in the tooltip or longer than the tooltip's forced width (`boolean`)

---

### GameTooltip:AddTexture

Adds a texture to the last tooltip line. The texture is sized to match the height of the line's text and positioned to the left of the text (indenting the text to provide room).

**Signature:**

```lua
GameTooltip:AddTexture("texture")
```

**Arguments:**

- `texture` - Path to a texture image file (`string`)

---

### Frame:AllowAttributeChanges

Temporarily allows insecure code to modify the frame's attributes during combat. This permission is automatically rescinded when the frame's [`OnUpdate`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnUpdate) script next runs.

**Signature:**

```lua
Frame:AllowAttributeChanges()
```

*Inherited from [Frame](Frame.md)*

---

### GameTooltip:AppendText

Adds text to the first line of the tooltip

**Signature:**

```lua
GameTooltip:AppendText("text")
```

**Arguments:**

- `text` - Text to be appended to the tooltip's first line (`string`)

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

Clear all anchor point for the given region

**Signature:**

```lua
Region:ClearAllPoints()
```

*Inherited from [Region](Region.md)*

---

### GameTooltip:ClearLines

Clears the tooltip's contents. Scripts scanning the tooltip contents should be aware that this method clears the text of all the tooltip's left-side font strings but hides the right-side font strings without clearing their text.

**Signature:**

```lua
GameTooltip:ClearLines()
```

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

### Frame:CreateFontString

Creates a new FontString for the Frame on a given layer, possibly inheriting from a template

**Signature:**

```lua
Frame:CreateFontString(["name" [, "layer" [, "inherits"]]])
```

**Arguments:**

- `name` - A global name to use for the new font string (`string`)
- `layer` - The graphic layer on which to create the font string. Default value is `ARTWORK`. (`string`, [layer](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#layer))
- `inherits` - A template from which the new front string should inherit (`string`)

*Inherited from [Frame](Frame.md)*

---

### Frame:CreateTexture

Creates a new [`Texture`](Texture.md) as a child of the frame. The `sublevel` argument can be used to provide layering of textures within a draw layer. As it can be difficult to compute the proper layering, addon authors should avoid using this option, and it's XML equivalent `textureSubLevel` without reason. It should also be noted that `FontStrings` will always appear on top of all textures in a given draw layer.

**Signature:**

```lua
texture = Frame:CreateTexture(["name" [, "layer" [, "inherits" [, sublevel]]]])
```

**Arguments:**

- `name` - Global name for the new texture (`string`)
- `layer` - Graphic layer on which to create the texture; defaults to `ARTWORK` if not specified (`string`, [layer](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#layer))
- `inherits` - Name of a template from which the new texture should inherit (`string`)
- `sublevel` - The sub-level on the given graphics layer ranging from `-8`- to `7`. The default value of this argument is `0` (`number`)

**Returns:**

- `texture` - Reference to the new `Texture` object (`texture`)

*Inherited from [Frame](Frame.md)*

---

### Frame:CreateTitleRegion

Creates a title region for dragging the frame. Creating a title region allows a frame to be repositioned by the user (by clicking and dragging in the region) without requiring additional scripts. (This behavior only applies if the frame is [mouse enabled](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/EnableMouse).)

**Signature:**

```lua
region = Frame:CreateTitleRegion()
```

**Returns:**

- `region` - Reference to the new `Region` object (`region`)

*Inherited from [Frame](Frame.md)*

---

### Frame:DisableDrawLayer

Prevents display of all child objects of the frame on a specified graphics layer

**Signature:**

```lua
Frame:DisableDrawLayer("layer")
```

**Arguments:**

- `layer` - Name of a graphics layer (`string`, [layer](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#layer))

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

Enables or disables joystick interactivity. Joystick interactivity must be enabled in order for a frame's joystick-related [script](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) handlers to be run.

(As of this writing, joystick support is partially implemented but not enabled in the current version of World of Warcraft.)

**Signature:**

```lua
Frame:EnableJoystick(enable)
```

**Arguments:**

- `enable` - True to enable joystick interactivity; false to disable (`boolean`)

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

### GameTooltip:FadeOut

Causes the tooltip to begin fading out

**Signature:**

```lua
GameTooltip:FadeOut()
```

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

### GameTooltip:GetAnchorType

Returns the method for anchoring the tooltip relative to its owner

**Signature:**

```lua
anchor = GameTooltip:GetAnchorType()
```

**Returns:**

- `anchor` - Token identifying the method for anchoring the tooltip relative to its owner frame (`string`)
  - `ANCHOR_BOTTOMLEFT` - Align the top right of the tooltip with the bottom left of the owner
  - `ANCHOR_CURSOR` - Toolip follows the mouse cursor
  - `ANCHOR_LEFT` - Align the bottom right of the tooltip with the top left of the owner
  - `ANCHOR_NONE` - Tooltip appears in the default position
  - `ANCHOR_PRESERVE` - Tooltip's position is saved between sessions (useful if the tooltip is made user-movable)
  - `ANCHOR_RIGHT` - Align the bottom left of the tooltip with the top right of the owner
  - `ANCHOR_TOPLEFT` - Align the bottom left of the tooltip with the top left of the owner
  - `ANCHOR_TOPRIGHT` - Align the bottom right of the tooltip with the top right of the owner

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

Returns the screen coordinates of the Region's center.

**Signature:**

```lua
Region:GetCenter()
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
GameTooltip:GetDontSavePosition()
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

Returns the overall 3D depth of the frame (for stereoscopic 3D configurations). Unlike [`:GetDepth()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/GetDepth) which returns the apparent depth of the frame relative to its parent, this function returns the absolute depth of the frame, taking into account the relative depths of parent frames.

**Signature:**

```lua
depth = Frame:GetEffectiveDepth()
```

**Returns:**

- `depth` - Apparent 3D depth of this frame relative to the screen (`number`)

*Inherited from [Frame](Frame.md)*

---

### Frame:GetEffectiveScale

Returns the frame's effective scale

**Signature:**

```lua
Frame:GetEffectiveScale()
```

*Inherited from [Frame](Frame.md)*

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

Returns the height of the region.

**Signature:**

```lua
Region:GetHeight()
```

*Inherited from [Region](Region.md)*

---

### Frame:GetHitRectInsets

Returns the inserts for the frame's HitRect

**Signature:**

```lua
Frame:GetHitRectInsets()
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

### GameTooltip:GetItem

Returns the name and hyperlink for the item displayed in the tooltip

**Signature:**

```lua
name, link = GameTooltip:GetItem()
```

**Returns:**

- `name` - Name of the item whose information is displayed in the tooltip, or nil. (`string`)
- `link` - A hyperlink for the item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

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

### Frame:GetMaxResize

Returns the maximum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing).

**Signature:**

```lua
maxWidth, maxHeight = Frame:GetMaxResize()
```

**Returns:**

- `maxWidth` - Maximum width of the frame (in pixels), or `0` for no limit (`number`)
- `maxHeight` - Maximum height of the frame (in pixels), or `0` for no limit (`number`)

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

### GameTooltip:GetMinimumWidth

Returns the minimum width of the tooltip

**Signature:**

```lua
width = GameTooltip:GetMinimumWidth()
```

**Returns:**

- `width` - Minimum width of the tooltip frame (in pixels) (`number`)

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
numChildren = Frame:GetNumChildren()
```

**Returns:**

- `numChildren` - Number of child frames belonging to the frame (`number`)

*Inherited from [Frame](Frame.md)*

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
numRegions = Frame:GetNumRegions()
```

**Returns:**

- `numRegions` - Number of non-Frame child regions (`FontString`s and `Texture`s) belonging to the frame (`number`)

*Inherited from [Frame](Frame.md)*

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

### GameTooltip:GetOwner

Returns the frame to which the tooltip refers and is anchored

**Signature:**

```lua
owner = GameTooltip:GetOwner()
```

**Returns:**

- `owner` - Reference to the `Frame` object to which the tooltip is anchored (`frame`)

---

### GameTooltip:GetPadding

Returns the amount of space between tooltip's text and its right-side edge

**Signature:**

```lua
padding = GameTooltip:GetPadding()
```

**Returns:**

- `padding` - Amount of space between the right-side edge of the tooltip's text and the right-side edge of the tooltip frame (in pixels) (`number`)

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
... = Frame:GetRegions()
```

**Returns:**

- `...` - A list of each non-Frame child region (`FontString` or `Texture`) belonging to the frame (`list`)

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

Returns the scale of the frame

**Signature:**

```lua
Frame:GetScale()
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

### GameTooltip:GetSpell

Returns information about the spell displayed in the tooltip

**Signature:**

```lua
spellName, spellRank, spellID = GameTooltip:GetSpell()
```

**Returns:**

- `spellName` - Name of the spell, or nil if the information in the tooltip is not for a spell. (`string`)
- `spellRank` - Secondary text associated with the spell name (often a rank, e.g. `"Rank 8"`) (`string`)
- `spellID` - Numeric identifier for the spell and rank (`number`, [spellID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#spellID))

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

### GameTooltip:GetUnit

Returns information about the unit displayed in the tooltip

**Signature:**

```lua
name, unit = GameTooltip:GetUnit()
```

**Returns:**

- `name` - Name of the unit displayed in the tooltip, or nil (`string`)
- `unit` - Unit identifier of the unit, or `nil` if the unit cannot be referenced by a `unitID` (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

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

### ScriptObject:HasScript

Returns whether the widget supports a script handler

**Signature:**

```lua
hasScript = ScriptObject:HasScript("scriptType")
```

**Arguments:**

- `scriptType` - A script type; see [scripts reference](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) for details (`string`)

**Returns:**

- `hasScript` - `1` if the widget can handle the script, otherwise `nil` (`1nil`)

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

### Frame:IsClampedToScreen

Returns whether or not the frame is clamped to the screen

**Signature:**

```lua
Frame:IsClampedToScreen()
```

*Inherited from [Frame](Frame.md)*

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

### GameTooltip:IsEquippedItem

Returns whether the tooltip is displaying an item currently equipped by the player

**Signature:**

```lua
enabled = GameTooltip:IsEquippedItem()
```

**Returns:**

- `enabled` - `1` if the tooltip is displaying information about an item currently equipped by the player; otherwise `nil` (`1nil`)

---

### Frame:IsEventRegistered

Returns whether or not the frame is registered for the given event

**Signature:**

```lua
Frame:IsEventRegistered()
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

### Frame:IsJoystickEnabled

Returns whether joystick interactivity is enabled for the frame

**Signature:**

```lua
enabled = GameTooltip:IsJoystickEnabled()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:IsKeyboardEnabled

Returns whether or not the frame is keyboard enabled

**Signature:**

```lua
Frame:IsKeyboardEnabled()
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

### GameTooltip:IsOwned

Returns whether the tooltip has an owner frame

**Signature:**

```lua
hasOwner = GameTooltip:IsOwned()
```

**Returns:**

- `hasOwner` - `1` if the tooltip has an owner frame; otherwise `nil` (`1nil`)

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

### GameTooltip:IsUnit

Returns whether the tooltip is displaying information for a given unit

**Signature:**

```lua
isUnit = GameTooltip:IsUnit("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `isUnit` - `1` if the tooltip is displaying information for the unit; otherwise `nil` (`1nil`)

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

### GameTooltip:NumLines

Returns the number of lines of text currently shown in the tooltip

**Signature:**

```lua
numLines = GameTooltip:NumLines()
```

**Returns:**

- `numLines` - Number of lines currently shown in the tooltip (`number`)

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

Registers the frame for dragging. Once the frame is registered for dragging (and [mouse enabled](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/EnableMouse)), the frame's [`OnDragStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnDragStart) and [`OnDragStop`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnDragStop) scripts will be called when the specified mouse button(s) are clicked and dragged starting from within the frame (or its mouse-interactive area).

**Signature:**

```lua
Frame:RegisterForDrag(...)
```

**Arguments:**

- `...` - A list of strings, each the name of a mouse button for which the frame should respond to drag actions (`list`)
  - `Button4`
  - `Button5`
  - `LeftButton`
  - `MiddleButton`
  - `RightButton`

*Inherited from [Frame](Frame.md)*

---

### GameTooltip:SetAction

Fills the tooltip with information about the contents of an action slot

**Signature:**

```lua
GameTooltip:SetAction(slot)
```

**Arguments:**

- `slot` - An action bar slot (`number`, [actionID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#actionID))

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

### GameTooltip:SetAnchorType

Sets the method for anchoring the tooltip relative to its owner

**Signature:**

```lua
GameTooltip:SetAnchorType("anchor" [, xOffset [, yOffset]])
```

**Arguments:**

- `anchor` - Token identifying the positioning method for the tooltip relative to its owner frame (`string`)
  - `ANCHOR_BOTTOMLEFT` - Align the top right of the tooltip with the bottom left of the owner
  - `ANCHOR_CURSOR` - Toolip follows the mouse cursor
  - `ANCHOR_LEFT` - Align the bottom right of the tooltip with the top left of the owner
  - `ANCHOR_NONE` - Tooltip appears in the default position
  - `ANCHOR_PRESERVE` - Tooltip's position is saved between sessions (useful if the tooltip is made user-movable)
  - `ANCHOR_RIGHT` - Align the bottom left of the tooltip with the top right of the owner
  - `ANCHOR_TOPLEFT` - Align the bottom left of the tooltip with the top left of the owner
  - `ANCHOR_TOPRIGHT` - Align the bottom right of the tooltip with the top right of the owner
- `xOffset` - Horizontal distance from the anchor to the tooltip (`number`)
- `yOffset` - Vertical distance from the anchor to the tooltip (`number`)

---

### Frame:SetAttribute

Sets a secure frame attribute. See the [secure template documentation](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/secure_template) for more information about frame attributes.

**Signature:**

```lua
Frame:SetAttribute("name", value)
```

**Arguments:**

- `name` - Name of an attribute, case insensitive (`string`)
- `value` - New value to set for the attribute (`value`)

*Inherited from [Frame](Frame.md)*

---

### GameTooltip:SetAuctionItem

Fills the tooltip with information about an item in the auction house

**Signature:**

```lua
GameTooltip:SetAuctionItem("list", index)
```

**Arguments:**

- `list` - Type of auction listing (`string`, [ah-list-type](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#ah-list-type))
  - `bidder` - Auctions the player has bid on
  - `list` - Auctions the player can browse and bid on or buy out
  - `owner` - Auctions the player placed
- `index` - Index of an auction in the listing (`number`)

---

### GameTooltip:SetAuctionSellItem

Fills the tooltip with information about the item currently being set up for auction

**Signature:**

```lua
GameTooltip:SetAuctionSellItem()
```

---

### Frame:SetBackdrop

Sets a frame's backdrop as defined by a table.

This function accepts the return from the Frame:GetBackdrop() function.  The format of the backdropTbl argument is as follows:

{
 bgFile = "bgFile", 
 edgeFile = "edgeFile", 
 tile = false, 
 tileSize = 0, 
 edgeSize = 32,
 insets = { 
 left = 0, 
 right = 0, 
 top = 0, 
 bottom = 0 
 }
}

**Signature:**

```lua
Frame:SetBackdrop()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:SetBackdropBorderColor

Sets a shading color for the frame's border graphic. As with [`Texture:SetVertexColor()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Texture/SetVertexColor), this color is a shading applied to the colors of the texture image; a color of `(1, 1, 1)` allows the image's original colors to show.

**Signature:**

```lua
Frame:SetBackdropBorderColor(red, green, blue [, alpha])
```

**Arguments:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

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

### GameTooltip:SetBackpackToken

Fills the tooltip with information about a currency marked for watching on the Backpack UI

**Signature:**

```lua
GameTooltip:SetBackpackToken(index)
```

**Arguments:**

- `index` - Index of a 'slot' for displaying currencies on the backpack (between 1 and `MAX_WATCHED_TOKENS`) (`number`)

---

### GameTooltip:SetBagItem

**Signature:**

```lua
hasCooldown, repairCost = GameTooltip:SetBagItem(bag,item)
```

---

### GameTooltip:SetBuybackItem

Fills the tooltip with information about item recently sold to a vendor and available to be repurchased

**Signature:**

```lua
GameTooltip:SetBuybackItem(index)
```

**Arguments:**

- `index` - Index of an item in the buyback listing (between 1 and [`GetNumBuybackItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumBuybackItems)) (`number`)

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

### GameTooltip:SetCurrencyToken

Fills the tooltip with information about a special currency type. Note that passing the index of a header will crash the client.

**Signature:**

```lua
GameTooltip:SetCurrencyToken(index)
```

**Arguments:**

- `index` - Index of a currency type in the currency list (between 1 and [`GetCurrencyListSize()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetCurrencyListSize)) (`number`)

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
GameTooltip:SetDontSavePosition()
```

*Inherited from [Frame](Frame.md)*

---

### GameTooltip:SetEquipmentSet

Fills the tooltip with information about an equipment set

**Signature:**

```lua
GameTooltip:SetEquipmentSet("name")
```

**Arguments:**

- `name` - Name of the equipment set (`string`)

---

### GameTooltip:SetExistingSocketGem

Fills the tooltip with information about a permanently socketed gem

**Signature:**

```lua
GameTooltip:SetExistingSocketGem(index, toDestroy)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumSockets)) (`number`)
- `toDestroy` - True to alter the tooltip display to indicate that this gem will be destroyed by socketing a new gem; false to show the normal tooltip for the gem (`boolean`)

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

### GameTooltip:SetFrameStack

Fills the tooltip with a list of frames under the mouse cursor. Not relevant outside of addon development and debugging.

**Signature:**

```lua
GameTooltip:SetFrameStack(includeHidden)
```

**Arguments:**

- `includeHidden` - True to include hidden frames in the list; false to list only visible frames (`boolean`)

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

### GameTooltip:SetGlyph

Fills the tooltip with information about one of the player's glyphs

**Signature:**

```lua
GameTooltip:SetGlyph(socket, talentGroup)
```

**Arguments:**

- `socket` - Which socket's glyph to display (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#glyphIndex))
- `talentGroup` - Which set of glyphs to display, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

---

### GameTooltip:SetGuildBankItem

Fills the tooltip with information about an item in the guild bank. Information is only available if the guild bank tab has been opened in the current play session.

**Signature:**

```lua
GameTooltip:SetGuildBankItem(tab, slot)
```

**Arguments:**

- `tab` - Index of a guild bank tab (between 1 and [`GetNumGuildBankTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumGuildBankTabs)) (`number`)
- `slot` - Index of an item slot in the guild bank tab (between 1 and `MAX_GUILDBANK_SLOTS_PER_TAB`) (`number`)

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

### Frame:SetHitRectInsets

Sets the insets from the frame's edges which determine its mouse-interactable area

**Signature:**

```lua
Frame:SetHitRectInsets(left, right, top, bottom)
```

**Arguments:**

- `left` - Distance from the left edge of the frame to the left edge of its mouse-interactive area (in pixels) (`number`)
- `right` - Distance from the right edge of the frame to the right edge of its mouse-interactive area (in pixels) (`number`)
- `top` - Distance from the top edge of the frame to the top edge of its mouse-interactive area (in pixels) (`number`)
- `bottom` - Distance from the bottom edge of the frame to the bottom edge of its mouse-interactive area (in pixels) (`number`)

*Inherited from [Frame](Frame.md)*

---

### GameTooltip:SetHyperlink

Fills the tooltip with information about an item, quest, spell, or other entity represented by a hyperlink

**Signature:**

```lua
GameTooltip:SetHyperlink("hyperlink")
```

**Arguments:**

- `hyperlink` - A full hyperlink, or the `linktype:linkdata` portion thereof (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))

---

### GameTooltip:SetHyperlinkCompareItem

Fills the tooltip with information about the item currently equipped in the slot used the supplied item

**Signature:**

```lua
success = GameTooltip:SetHyperlinkCompareItem("hyperlink" [, index])
```

**Arguments:**

- `hyperlink` - A full hyperlink, or the `linktype:linkdata` portion thereof, for an item to compare against the player's equipped similar item (`string`, [hyperlink](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#hyperlink))
- `index` - Index of the slot to compare against (1, 2, or 3), if more than one item of the equipment type can be equipped at once (e.g. rings and trinkets) (`number`)

**Returns:**

- `success` - `1` if an item's information was loaded into the tooltip; otherwise `nil` (`number`, [1nil](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#1nil))

---

### Frame:SetID

Sets a numeric identifier for the frame. Frame IDs have no effect on frame behavior, but can be a useful way to keep track of multiple similar frames, especially in cases where a list of frames is created from a template (such as for action buttons, loot slots, or lines in a FauxScrollFrame).

**Signature:**

```lua
Frame:SetID(id)
```

**Arguments:**

- `id` - A numeric identifier for the frame (`number`)

*Inherited from [Frame](Frame.md)*

---

### GameTooltip:SetInboxItem

Fills the tooltip with information about an item attached to a message in the player's inbox

**Signature:**

```lua
GameTooltip:SetInboxItem(mailID, attachmentIndex)
```

**Arguments:**

- `mailID` - Index of a message in the player's inbox (between 1 and [`GetInboxNumItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInboxNumItems)) (`number`)
- `attachmentIndex` - Index of an attachment to the message (between 1 and `select(8,`[`GetInboxHeaderInfo(mailID)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInboxHeaderInfo)`)`) (`number`)

---

### GameTooltip:SetInventoryItem

Fills the tooltip with information about an equipped item

**Signature:**

```lua
hasItem, hasCooldown, repairCost = GameTooltip:SetInventoryItem("unit", slot [, nameOnly])
```

**Arguments:**

- `unit` - A unit to query; only valid for 'player' or the unit currently being inspected (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetInventorySlotInfo) (`number`, [inventoryID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#inventoryID))
- `nameOnly` - True to omit much of the item's information (stat bonuses, sockets, and binding) from the tooltip; false to show all of the item's information (`boolean`)

**Returns:**

- `hasItem` - `1` if the unit has an item in the given slot; otherwise `nil` (`number`, [1nil](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#1nil))
- `hasCooldown` - `1` if the item is currently on cooldown; otherwise `nil` (`number`, [1nil](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#1nil))
- `repairCost` - Cost to repair the item (in copper, ignoring faction discounts) (`number`)

---

### GameTooltip:SetLFGCompletionReward

This function is not yet documented

**Signature:**

```lua
GameTooltip:SetLFGCompletionReward()
```

---

### GameTooltip:SetLFGDungeonReward

This function is not yet documented

**Signature:**

```lua
GameTooltip:SetLFGDungeonReward()
```

---

### GameTooltip:SetLootItem

Fills the tooltip with information about an item available as loot

**Signature:**

```lua
GameTooltip:SetLootItem(slot)
```

**Arguments:**

- `slot` - Index of a loot slot (between 1 and [`GetNumLootItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumLootItems)) (`number`)

---

### GameTooltip:SetLootRollItem

Fills the tooltip with information about an item currently up for loot rolling

**Signature:**

```lua
GameTooltip:SetLootRollItem(id)
```

**Arguments:**

- `id` - Index of an item currently up for loot rolling (as provided in the [`START_LOOT_ROLL`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/START_LOOT_ROLL) event) (`number`)

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

### GameTooltip:SetMerchantCostItem

Fills the tooltip with information about an alternate currency required to purchase an item from a vendor. Only applies to item-based currencies, not honor or arena points.

**Signature:**

```lua
GameTooltip:SetMerchantCostItem(index, currency)
```

**Arguments:**

- `index` - Index of an item in the vendor's listing (between 1 and [`GetMerchantNumItems()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMerchantNumItems)) (`number`)
- `currency` - Index of one of the item currencies required to purchase the item (between 1 and `select(3,`[`GetMerchantItemCostInfo(index)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetMerchantItemCostInfo)`)`) (`number`)

---

### GameTooltip:SetMerchantItem

Fills the tooltip with information about an item available for purchase from a vendor

**Signature:**

```lua
GameTooltip:SetMerchantItem(merchantIndex)
```

**Arguments:**

- `merchantIndex` - The index of an item in the merchant window, between `1` and `GetMerchantNumItems()`. (`number`)

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

### GameTooltip:SetMinimumWidth

Sets the minimum width of the tooltip. Normally, a tooltip is automatically sized to match the width of its shortest line of text; setting a minimum width can be useful if the tooltip also contains non-text frames (such as an amount of money or a status bar).

The tooltip is not automatically resized to the new width; to do so, call the tooltip's [`:Show()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/VisibleRegion/Show) method.

**Signature:**

```lua
GameTooltip:SetMinimumWidth(width)
```

**Arguments:**

- `width` - Minimum width of the tooltip frame (in pixels) (`number`)

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

### GameTooltip:SetOwner

Sets the frame to which the tooltip refers and is anchored

**Signature:**

```lua
GameTooltip:SetOwner(frame [, "anchorType" [, xOffset [, yOffset]]])
```

**Arguments:**

- `frame` - Reference to the `Frame` to which the tooltip refers (`frame`)
- `anchorType` - Token identifying the positioning method for the tooltip relative to its owner frame (`string`)
  - `ANCHOR_BOTTOMLEFT` - Align the top right of the tooltip with the bottom left of the owner
  - `ANCHOR_CURSOR` - Toolip follows the mouse cursor
  - `ANCHOR_LEFT` - Align the bottom right of the tooltip with the top left of the owner
  - `ANCHOR_NONE` - Tooltip appears in the default position
  - `ANCHOR_PRESERVE` - Tooltip's position is saved between sessions (useful if the tooltip is made user-movable)
  - `ANCHOR_RIGHT` - Align the bottom left of the tooltip with the top right of the owner
  - `ANCHOR_TOPLEFT` - Align the bottom left of the tooltip with the top left of the owner
  - `ANCHOR_TOPRIGHT` - Align the bottom right of the tooltip with the top right of the owner
- `xOffset` - The horizontal offset for the tooltip anchor (`number`)
- `yOffset` - The vertical offset for the tooltip anchor (`number`)

---

### GameTooltip:SetPadding

Sets the amount of space between tooltip's text and its right-side edge. Used in the default UI's ItemRefTooltip to provide space for a close button.

**Signature:**

```lua
GameTooltip:SetPadding(padding)
```

**Arguments:**

- `padding` - Amount of space between the right-side edge of the tooltip's text and the right-side edge of the tooltip frame (in pixels) (`number`)

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

### GameTooltip:SetPetAction

Fills the tooltip with information about a pet action. Only provides information for pet action slots containing pet spells -- in the default UI, the standard pet actions (attack, follow, passive, aggressive, etc) are special-cased to show specific tooltip text.

**Signature:**

```lua
GameTooltip:SetPetAction(index)
```

**Arguments:**

- `index` - Index of a pet action button (between 1 and `NUM_PET_ACTION_SLOTS`) (`number`)

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

### GameTooltip:SetPossession

Fills the tooltip with information about one of the special actions available while the player possesses another unit

**Signature:**

```lua
GameTooltip:SetPossession(index)
```

**Arguments:**

- `index` - Index of a possession bar action (between 1 and `NUM_POSSESS_SLOTS`) (`number`)

---

### GameTooltip:SetQuestItem

Fills the tooltip with information about an item in a questgiver dialog

**Signature:**

```lua
GameTooltip:SetQuestItem("itemType", index)
```

**Arguments:**

- `itemType` - Token identifying one of the possible sets of items (`string`)
  - `choice` - Items from which the player may choose a reward
  - `required` - Items required to complete the quest
  - `reward` - Items given as reward for the quest
- `index` - Index of an item in the set (between 1 and `GetNumQuestChoices()`, `GetNumQuestItems()`, or `GetNumQuestRewards()`, according to `itemType`) (`number`)

---

### GameTooltip:SetQuestLogItem

Fills the tooltip with information about an item related to the selected quest in the quest log

**Signature:**

```lua
GameTooltip:SetQuestLogItem("itemType", index)
```

**Arguments:**

- `itemType` - Token identifying one of the possible sets of items (`string`)
  - `choice` - Items from which the player may choose a reward
  - `reward` - Items always given as reward for the quest
- `index` - Index of an item in the set (between 1 and `GetNumQuestLogChoices()` or `GetNumQuestLogRewards()`, according to `itemType`) (`number`)

---

### GameTooltip:SetQuestLogRewardSpell

Fills the tooltip with information about the reward spell for the selected quest in the quest log

**Signature:**

```lua
GameTooltip:SetQuestLogRewardSpell()
```

---

### GameTooltip:SetQuestLogSpecialItem

Fills the tooltip with information about a usable item associated with a current quest

**Signature:**

```lua
GameTooltip:SetQuestLogSpecialItem(questIndex)
```

**Arguments:**

- `questIndex` - Index of a quest log entry with an associated usable item (between 1 and [`GetNumQuestLogEntries()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumQuestLogEntries)) (`number`)

---

### GameTooltip:SetQuestRewardSpell

Fills the tooltip with information about the spell reward in a questgiver dialog

**Signature:**

```lua
GameTooltip:SetQuestRewardSpell()
```

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

### GameTooltip:SetSendMailItem

Fills the tooltip with information about an item attached to the outgoing mail message

**Signature:**

```lua
GameTooltip:SetSendMailItem(slot)
```

**Arguments:**

- `slot` - Index of an outgoing attachment slot (between 1 and `ATTACHMENTS_MAX_SEND`) (`number`)

---

### GameTooltip:SetShapeshift

Fills the tooltip with information about an ability on the stance/shapeshift bar

**Signature:**

```lua
GameTooltip:SetShapeshift(index)
```

**Arguments:**

- `index` - Index of an ability on the stance/shapeshift bar (between 1 and [`GetNumShapeshiftForms()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumShapeshiftForms)) (`number`)

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

### GameTooltip:SetSocketGem

Fills the tooltip with information about a gem added to a socket

**Signature:**

```lua
GameTooltip:SetSocketGem(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumSockets)) (`number`)

---

### GameTooltip:SetSocketedItem

Fills the tooltip with information about the item currently being socketed

**Signature:**

```lua
GameTooltip:SetSocketedItem()
```

---

### GameTooltip:SetSpell

Fills the tooltip with information about a spell from the player (or pet's) spellbook

**Signature:**

```lua
GameTooltip:SetSpell(id, "bookType")
```

---

### GameTooltip:SetSpellByID

Fills the tooltip with information about a spell specified by ID

**Signature:**

```lua
GameTooltip:SetSpellByID(id)
```

**Arguments:**

- `id` - Numeric ID of a spell (`number`, [spellID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#spellID))

---

### GameTooltip:SetTalent

Fills the tooltip with information about a talent

**Signature:**

```lua
GameTooltip:SetTalent(tabIndex, talentIndex, inspect, pet, talentGroup)
```

**Arguments:**

- `tabIndex` - Index of a talent tab (between 1 and [`GetNumTalentTabs()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalentTabs)) (`number`)
- `talentIndex` - Index of a talent option (between 1 and [`GetNumTalents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTalents)) (`number`)
- `inspect` - true to return information for the currently inspected unit; false to return information for the player (`boolean`)
- `pet` - true to return information for the player's pet; false to return information for the player (`boolean`)
- `talentGroup` - Which set of talents to edit, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

---

### GameTooltip:SetText

Sets the tooltip's text. Any other content currently displayed in the tooltip will be removed or hidden, and the tooltip's size will be adjusted to fit the new text.

**Signature:**

```lua
GameTooltip:SetText("text" [, r [, g [, b [, a]]]])
```

**Arguments:**

- `text` - Text to be displayed in the tooltip (`string`)
- `r` - Red component of the text color (0.0 - 1.0) (`number`)
- `g` - Green component of the text color (0.0 - 1.0) (`number`)
- `b` - Blue component of the text color (0.0 - 1.0) (`number`)
- `a` - Alpha (opacity) for the text (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

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

### GameTooltip:SetTotem

Fills the tooltip with information about one of the player's active totems.. Totem functions are also used for ghouls summoned by a Death Knight's Raise Dead ability (if the ghoul is not made a controllable pet by the Master of Ghouls talent).

**Signature:**

```lua
GameTooltip:SetTotem(slot)
```

**Arguments:**

- `slot` - Which totem to query (`number`)
  - `1` - Fire (or Death Knight's ghoul)
  - `2` - Earth
  - `3` - Water
  - `4` - Air

---

### GameTooltip:SetTracking

Fills the tooltip with information about the currently selected tracking type

**Signature:**

```lua
GameTooltip:SetTracking()
```

---

### GameTooltip:SetTradePlayerItem

Fills the tooltip with information about an item offered for trade by the player. See [`:SetTradeTargetItem()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/GameTooltip/SetTradeTargetItem) for items to be received from the trade.

**Signature:**

```lua
GameTooltip:SetTradePlayerItem(index)
```

**Arguments:**

- `index` - Index of an item offered for trade by the player (between 1 and `MAX_TRADE_ITEMS`) (`number`)

---

### GameTooltip:SetTradeSkillItem

Fills the tooltip with information about an item created by a trade skill recipe or a reagent in the recipe

**Signature:**

```lua
GameTooltip:SetTradeSkillItem(skillIndex [, reagentIndex])
```

**Arguments:**

- `skillIndex` - Index of a recipe in the trade skill list (between 1 and [`GetNumTradeSkills()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTradeSkills)) (`number`)
- `reagentIndex` - Index of a reagent in the recipe (between 1 and [`GetTradeSkillNumReagents()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTradeSkillNumReagents)); if omitted, displays a tooltip for the item created by the recipe (`number`)

---

### GameTooltip:SetTradeTargetItem

Fills the tooltip with information about an item offered for trade by the target. See [`:SetTradePlayerItem()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/GameTooltip/SetTradePlayerItem) for items to be traded away by the player.

**Signature:**

```lua
GameTooltip:SetTradeTargetItem(index)
```

**Arguments:**

- `index` - Index of an item offered for trade by the target (between 1 and `MAX_TRADE_ITEMS`) (`number`)

---

### GameTooltip:SetTrainerService

Fills the tooltip with information about a trainer service

**Signature:**

```lua
GameTooltip:SetTrainerService(index)
```

**Arguments:**

- `index` - Index of an entry in the trainer service listing (between 1 and [`GetNumTrainerServices()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumTrainerServices)) (`number`)

---

### GameTooltip:SetUnit

Fills the tooltip with information about a unit

**Signature:**

```lua
GameTooltip:SetUnit("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitid](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitid))

---

### GameTooltip:SetUnitAura

Fills the tooltip with information about a buff or debuff on a unit

**Signature:**

```lua
GameTooltip:SetUnitAura("unit", index [, "filter"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of a buff or debuff on the unit (`number`)
- `filter` - A list of filters to use when resolving the index, separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `HARMFUL` - Show debuffs only
  - `HELPFUL` - Show buffs only
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

---

### GameTooltip:SetUnitBuff

Fills the tooltip with information about a buff on a unit. This method is an alias for [`:SetUnitAura()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/GameTooltip/SetUnitAura) with a built-in `HELPFUL` filter (which cannot be removed or negated with the `HARMFUL` filter).

**Signature:**

```lua
GameTooltip:SetUnitBuff("unit", index [, "filter"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of a buff or debuff on the unit (`number`)
- `filter` - A list of filters to use when resolving the index, separated by the pipe '|' character; e.g. `"RAID|PLAYER"` will query group buffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

---

### GameTooltip:SetUnitDebuff

Fills the tooltip with information about a debuff on a unit. This method is an alias for [`:SetUnitAura()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/GameTooltip/SetUnitAura) with a built-in `HARMFUL` filter (which cannot be removed or negated with the `HELPFUL` filter).

**Signature:**

```lua
GameTooltip:SetUnitDebuff("unit", index [, "filter"])
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))
- `index` - Index of a buff or debuff on the unit (`number`)
- `filter` - A list of filters to use when resolving the index, separated by the pipe '|' character; e.g. `"CANCELABLE|PLAYER"` will query cancelable debuffs cast by the player (`string`)
  - `CANCELABLE` - Show auras that can be cancelled
  - `NOT_CANCELABLE` - Show auras that cannot be cancelled
  - `PLAYER` - Show auras the player has cast
  - `RAID` - Show auras the player can cast on party/raid members (as opposed to self buffs)

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
Frame:StartMoving()
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
Region:StopAnimating()
```

*Inherited from [Region](Region.md)*

---

### Frame:StopMovingOrSizing

Ends movement or resizing of the frame initiated with [`:StartMoving()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartMoving) or [`:StartSizing()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/StartSizing)

**Signature:**

```lua
Frame:StopMovingOrSizing()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:UnregisterAllEvents

Unregisters the frame from any [events](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events) for which it is registered

**Signature:**

```lua
Frame:UnregisterAllEvents()
```

*Inherited from [Frame](Frame.md)*

---

### Frame:UnregisterEvent

Unregisters the frame for an event. Once unregistered, the frame's [`OnEvent`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnEvent) script handler will not be called for that event.

Unregistering from notifications for an event can be useful for improving addon performance at times when it's not necessary to process the event. For example, a frame which monitors target health does not need to receive the [`UNIT_HEALTH`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/UNIT_HEALTH) event while the player has no target. An addon that sorts the contents of the player's bags can register for the [`BAG_UPDATE`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/BAG_UPDATE) event to keep track of when items are picked up, but unregister from the event while it performs its sorting.

**Signature:**

```lua
Frame:UnregisterEvent("event")
```

**Arguments:**

- `event` - Name of an [event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events) (`string`)

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

### OnTooltipAddMoney

Run when an amount of money should be added to the tooltip

**Signature:**

```lua
OnTooltipAddMoney(self, amount, maxAmount)
```

---

### OnTooltipCleared

Run when the tooltip is hidden or its content is cleared

**Signature:**

```lua
OnTooltipCleared(self)
```

---

### OnTooltipSetAchievement

Run when the tooltip is filled with information about an achievement

**Signature:**

```lua
OnTooltipSetAchievement(self)
```

---

### OnTooltipSetDefaultAnchor

Run when the tooltip is repositioned to its default anchor location

**Signature:**

```lua
OnTooltipSetDefaultAnchor(self)
```

---

### OnTooltipSetEquipmentSet

Run when the tooltip is filled with information about an equipment set

**Signature:**

```lua
OnTooltipSetEquipmentSet(self)
```

---

### OnTooltipSetFrameStack

Run when the tooltip is filled with a list of frames under the mouse cursor

**Signature:**

```lua
OnTooltipSetFrameStack(self)
```

---

### OnTooltipSetItem

Run when the tooltip is filled with information about an item

**Signature:**

```lua
OnTooltipSetItem(self)
```

---

### OnTooltipSetQuest

Run when the tooltip is filled with information about a quest

**Signature:**

```lua
OnTooltipSetQuest(self)
```

---

### OnTooltipSetSpell

Run when the tooltip is filled with information about a spell

**Signature:**

```lua
OnTooltipSetSpell(self)
```

---

### OnTooltipSetUnit

Run when the tooltip is filled with information about a unit

**Signature:**

```lua
OnTooltipSetUnit(self)
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
