# Frame

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/Frame)

---

## Methods

---

### Frame:AllowAttributeChanges

Temporarily allows insecure code to modify the frame's attributes during combat. This permission is automatically rescinded when the frame's [`OnUpdate`](#onupdate) script next runs.

**Signature:**

```lua
Frame:AllowAttributeChanges()
```

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

### Frame:CreateFontString

Creates a new FontString for the Frame on a given layer, possibly inheriting from a template

**Signature:**

```lua
Frame:CreateFontString(["name" [, "layer" [, "inherits"]]])
```

**Arguments:**

- `name` - A global name to use for the new font string (`string`)
- `layer` - The graphic layer on which to create the font string. Default value is `ARTWORK`. (`string`, [layer](../types/layer.md))
- `inherits` - A template from which the new front string should inherit (`string`)

---

### Frame:CreateTexture

Creates a new [`Texture`](Texture.md) as a child of the frame. The `sublevel` argument can be used to provide layering of textures within a draw layer. As it can be difficult to compute the proper layering, addon authors should avoid using this option, and it's XML equivalent `textureSubLevel` without reason. It should also be noted that `FontStrings` will always appear on top of all textures in a given draw layer.

**Signature:**

```lua
texture = Frame:CreateTexture(["name" [, "layer" [, "inherits" [, sublevel]]]])
```

**Arguments:**

- `name` - Global name for the new texture (`string`)
- `layer` - Graphic layer on which to create the texture; defaults to `ARTWORK` if not specified (`string`, [layer](../types/layer.md))
- `inherits` - Name of a template from which the new texture should inherit (`string`)
- `sublevel` - The sub-level on the given graphics layer ranging from `-8`- to `7`. The default value of this argument is `0` (`number`)

**Returns:**

- `texture` - Reference to the new `Texture` object (`texture`)

---

### Frame:CreateTitleRegion

Creates a title region for dragging the frame. Creating a title region allows a frame to be repositioned by the user (by clicking and dragging in the region) without requiring additional scripts. (This behavior only applies if the frame is [mouse enabled](Frame.md#frameenablemouse).)

**Signature:**

```lua
region = Frame:CreateTitleRegion()
```

**Returns:**

- `region` - Reference to the new `Region` object (`region`)

---

### Frame:DisableDrawLayer

Prevents display of all child objects of the frame on a specified graphics layer

**Signature:**

```lua
Frame:DisableDrawLayer("layer")
```

**Arguments:**

- `layer` - Name of a graphics layer (`string`, [layer](../types/layer.md))

---

### Frame:EnableDrawLayer

Allows display of all child objects of the frame on a specified graphics layer

**Signature:**

```lua
Frame:EnableDrawLayer("layer")
```

**Arguments:**

- `layer` - Name of a graphics layer (`string`, [layer](../types/layer.md))

---

### Frame:EnableJoystick

Enables or disables joystick interactivity. Joystick interactivity must be enabled in order for a frame's joystick-related [script](#script-handlers) handlers to be run.

(As of this writing, joystick support is partially implemented but not enabled in the current version of World of Warcraft.)

**Signature:**

```lua
Frame:EnableJoystick(enable)
```

**Arguments:**

- `enable` - True to enable joystick interactivity; false to disable (`boolean`)

---

### Frame:EnableKeyboard

Enables or disables keyboard interactivity for the frame. Keyboard interactivity must be enabled in order for a frame's [`OnKeyDown`](#onkeydown), [`OnKeyUp`](#onkeyup), or [`OnChar`](#onchar) scripts to be run.

**Signature:**

```lua
Frame:EnableKeyboard(enable)
```

**Arguments:**

- `enable` - True to enable keyboard interactivity; false to disable (`boolean`)

---

### Frame:EnableMouse

Enables or disables mouse interactivity for the frame. Mouse interactivity must be enabled in order for a frame's mouse-related [script](#script-handlers) handlers to be run.

**Signature:**

```lua
Frame:EnableMouse(enable)
```

**Arguments:**

- `enable` - True to enable mouse interactivity; false to disable (`boolean`)

---

### Frame:EnableMouseWheel

Enables or disables mouse wheel interactivity for the frame. Mouse wheel interactivity must be enabled in order for a frame's [`OnMouseWheel`](#onmousewheel) script handler to be run.

**Signature:**

```lua
Frame:EnableMouseWheel(enable)
```

**Arguments:**

- `enable` - True to enable mouse wheel interactivity; false to disable (`boolean`)

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

### Frame:GetAttribute

Returns the value of a secure frame attribute. See the [secure template documentation](../categories/Secure execution utility.md) for more information about frame attributes.

**Signature:**

```lua
value = Frame:GetAttribute("name")
```

**Arguments:**

- `name` - Name of an attribute to query (`string`)

**Returns:**

- `value` - Value of the named attribute (`value`)

---

### Frame:GetBackdrop

Returns information about the frame's backdrop graphic. See [SetBackdrop](Frame.md#framesetbackdrop).

**Signature:**

```lua
backdrop = Frame:GetBackdrop()
```

**Returns:**

- `backdrop` - A table containing the backdrop settings, or `nil` if the frame has no backdrop (`table`, [backdrop](../types/backdrop.md))

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

Returns the position and dimension of the smallest area enclosing the frame and its children. This information may not match that returned by [`:GetRect()`](Region.md#regiongetrect) if the frame contains textures, font strings, or child frames whose boundaries lie outside its own.

**Signature:**

```lua
left, bottom, width, height = Frame:GetBoundsRect()
```

**Returns:**

- `left` - Distance from the left edge of the screen to the left edge of the area (in pixels) (`number`)
- `bottom` - Distance from the bottom edge of the screen to the bottom of the area (in pixels) (`number`)
- `width` - Width of the area (in pixels) (`number`)
- `height` - Height of the area (in pixels) (`number`)

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

---

### Frame:GetDepth

Returns the 3D depth of the frame (for stereoscopic 3D setups)

**Signature:**

```lua
depth = Frame:GetDepth()
```

**Returns:**

- `depth` - Apparent 3D depth of this frame relative to that of its parent frame (`number`)

---

### Frame:GetEffectiveAlpha

Returns the overall opacity of the frame. Unlike [`:GetAlpha()`](Frame.md#visibleregiongetalpha) which returns the opacity of the frame relative to its parent, this function returns the absolute opacity of the frame, taking into account the relative opacity of parent frames.

**Signature:**

```lua
alpha = Frame:GetEffectiveAlpha()
```

**Returns:**

- `alpha` - Effective alpha (opacity) of the region (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

---

### Frame:GetEffectiveDepth

Returns the overall 3D depth of the frame (for stereoscopic 3D configurations). Unlike [`:GetDepth()`](Frame.md#framegetdepth) which returns the apparent depth of the frame relative to its parent, this function returns the absolute depth of the frame, taking into account the relative depths of parent frames.

**Signature:**

```lua
depth = Frame:GetEffectiveDepth()
```

**Returns:**

- `depth` - Apparent 3D depth of this frame relative to the screen (`number`)

---

### Frame:GetEffectiveScale

Returns the frame's effective scale

**Signature:**

```lua
Frame:GetEffectiveScale()
```

---

### Frame:GetFrameLevel

Sets the level at which the frame is layered relative to others in its strata. Frames with higher frame level are layered "in front of" frames with a lower frame level. When not set manually, a frame's level is determined by its place in the frame hierarchy -- e.g. UIParent's level is 1, children of UIParent are at level 2, children of those frames are at level 3, etc.

**Signature:**

```lua
level = Frame:GetFrameLevel()
```

**Returns:**

- `level` - Layering level of the frame relative to others in its [`frameStrata`](../types/frameStrata.md) (`number`)

---

### Frame:GetFrameStrata

Returns the general layering strata of the frame

**Signature:**

```lua
strata = Frame:GetFrameStrata()
```

**Returns:**

- `strata` - Token identifying the strata in which the frame should be layered (`string`, [frameStrata](../types/frameStrata.md))
  - `BACKGROUND`
  - `DIALOG`
  - `FULLSCREEN`
  - `FULLSCREEN_DIALOG`
  - `HIGH`
  - `LOW`
  - `MEDIUM`
  - `PARENT`
  - `TOOLTIP`

---

### Frame:GetFrameType

Returns the type of the frame, as a string

**Signature:**

```lua
Frame:GetFrameType()
```

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

---

### Frame:GetID

Returns the frame's numeric identifier. Frame IDs have no effect on frame behavior, but can be a useful way to keep track of multiple similar frames, especially in cases where a list of frames is created from a template (such as for action buttons, loot slots, or lines in a FauxScrollFrame).

**Signature:**

```lua
id = Frame:GetID()
```

**Returns:**

- `id` - A numeric identifier for the frame (`number`)

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

Returns the maximum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](Frame.md#framestartsizing).

**Signature:**

```lua
maxWidth, maxHeight = Frame:GetMaxResize()
```

**Returns:**

- `maxWidth` - Maximum width of the frame (in pixels), or `0` for no limit (`number`)
- `maxHeight` - Maximum height of the frame (in pixels), or `0` for no limit (`number`)

---

### Frame:GetMinResize

Returns the minimum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](Frame.md#framestartsizing).

**Signature:**

```lua
minWidth, minHeight = Frame:GetMinResize()
```

**Returns:**

- `minWidth` - Minimum width of the frame (in pixels), or `0` for no limit (`number`)
- `minHeight` - Minimum height of the frame (in pixels), or `0` for no limit (`number`)

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

### Region:GetParent

Returns the Region's parent object.

**Signature:**

```lua
Region:GetParent()
```

*Inherited from [Region](Region.md)*

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

### Frame:GetRegions

Returns a list of non-Frame child regions belonging to the frame

**Signature:**

```lua
... = Frame:GetRegions()
```

**Returns:**

- `...` - A list of each non-Frame child region (`FontString` or `Texture`) belonging to the frame (`list`)

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

---

### Frame:GetScript

Returns the widget handler for "type"

**Signature:**

```lua
Frame:GetScript()
```

---

### Frame:GetTitleRegion

Returns the frame's TitleRegion object. See [`:CreateTitleRegion()`](Frame.md#framecreatetitleregion) for more information.

**Signature:**

```lua
region = Frame:GetTitleRegion()
```

**Returns:**

- `region` - Reference to the frame's TitleRegion object (`region`)

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

### Frame:HasScript

Returns whether or not the frame has the widget handler "type"

**Signature:**

```lua
Frame:HasScript()
```

---

### VisibleRegion:Hide

Hides the region

**Signature:**

```lua
VisibleRegion:Hide()
```

*Inherited from [VisibleRegion](VisibleRegion.md)*

---

### Frame:HookScript

Securely hooks a widget handler script

**Signature:**

```lua
Frame:HookScript()
```

---

### Frame:IgnoreDepth

Sets whether the frame's depth property is ignored (for stereoscopic 3D setups). If a frame's depth property is ignored, the frame itself is not rendered with stereoscopic 3D separation, but 3D graphics within the frame may be; this property is used on the default UI's WorldFrame.

**Signature:**

```lua
Frame:IgnoreDepth(enable)
```

**Arguments:**

- `enable` - True to ignore the frame's depth property; false to disable (`boolean`)

---

### Frame:IsClampedToScreen

Returns whether or not the frame is clamped to the screen

**Signature:**

```lua
Frame:IsClampedToScreen()
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

Returns whether or not the frame is registered for the given event

**Signature:**

```lua
Frame:IsEventRegistered()
```

---

### Frame:IsFrameType

Returns whether or not the frame is of the given type

**Signature:**

```lua
Frame:IsFrameType()
```

---

### Frame:IsIgnoringDepth

Returns whether the frame's depth property is ignored (for stereoscopic 3D setups)

**Signature:**

```lua
enabled = Frame:IsIgnoringDepth()
```

**Returns:**

- `enabled` - `1` if the frame's depth property is ignored; otherwise `nil` (`1nil`)

---

### Frame:IsJoystickEnabled

This function is not yet documented

**Signature:**

```lua
Frame:IsJoystickEnabled()
```

---

### Frame:IsJumpNavigateEnabled

This function is not yet documented

**Signature:**

```lua
Frame:IsJumpNavigateEnabled()
```

---

### Frame:IsJumpNavigateStart

This function is not yet documented

**Signature:**

```lua
Frame:IsJumpNavigateStart()
```

---

### Frame:IsKeyboardEnabled

Returns whether or not the frame is keyboard enabled

**Signature:**

```lua
Frame:IsKeyboardEnabled()
```

---

### Frame:IsMouseEnabled

Returns whether mouse interactivity is enabled for the frame

**Signature:**

```lua
enabled = Frame:IsMouseEnabled()
```

**Returns:**

- `enabled` - `1` if mouse interactivity is enabled for the frame; otherwise `nil` (`1nil`)

---

### Frame:IsMouseWheelEnabled

Returns whether mouse wheel interactivity is enabled for the frame

**Signature:**

```lua
enabled = Frame:IsMouseWheelEnabled()
```

**Returns:**

- `enabled` - `1` if mouse wheel interactivity is enabled for the frame; otherwise `nil` (`1nil`)

---

### Frame:IsMovable

Returns whether the frame can be moved by the user

**Signature:**

```lua
movable = Frame:IsMovable()
```

**Returns:**

- `movable` - `1` if the frame can be moved by the user; otherwise `nil` (`1nil`)

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

### Frame:IsResizable

Returns whether the frame can be resized by the user

**Signature:**

```lua
enabled = Frame:IsResizable()
```

**Returns:**

- `enabled` - `1` if the frame can be resized by the user; otherwise `nil` (`1nil`)

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

### Frame:IsToplevel

Returns whether the frame is automatically raised to the front when clicked

**Signature:**

```lua
enabled = Frame:IsToplevel()
```

**Returns:**

- `enabled` - `1` if the frame is automatically raised to the front when clicked; otherwise `nil` (`1nil`)

---

### Frame:IsUserPlaced

Returns whether the frame is flagged for automatic saving and restoration of position and dimensions

**Signature:**

```lua
enabled = Frame:IsUserPlaced()
```

**Returns:**

- `enabled` - `1` if the frame is flagged for automatic saving and restoration of position and dimensions; otherwise `nil` (`1nil`)

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

---

### Frame:Raise

Increases the frame's frame level above all other frames in its strata

**Signature:**

```lua
Frame:Raise()
```

---

### Frame:RegisterAllEvents

Registers the frame for all events. This method is recommended for debugging purposes only, as using it will cause the frame's [`OnEvent`](#onevent) script handler to be run very frequently for likely irrelevant events. (For code that needs to be run very frequently, use an [`OnUpdate`](#onupdate) script handler.)

**Signature:**

```lua
Frame:RegisterAllEvents()
```

---

### Frame:RegisterEvent

Registers the frame for an [event](../Events.md). The frame's [`OnEvent`](#onevent) script handler will be run whenever the event fires. See the event documentation for details on event arguments.

**Signature:**

```lua
Frame:RegisterEvent("event")
```

**Arguments:**

- `event` - Name of an [event](../Events.md) (`string`)

---

### Frame:RegisterForDrag

Registers the frame for dragging. Once the frame is registered for dragging (and [mouse enabled](Frame.md#frameenablemouse)), the frame's [`OnDragStart`](#ondragstart) and [`OnDragStop`](#ondragstop) scripts will be called when the specified mouse button(s) are clicked and dragged starting from within the frame (or its mouse-interactive area).

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

### Frame:SetAttribute

Sets a secure frame attribute. See the [secure template documentation](../categories/Secure execution utility.md) for more information about frame attributes.

**Signature:**

```lua
Frame:SetAttribute("name", value)
```

**Arguments:**

- `name` - Name of an attribute, case insensitive (`string`)
- `value` - New value to set for the attribute (`value`)

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

---

### Frame:SetBackdropBorderColor

Sets a shading color for the frame's border graphic. As with [`Texture:SetVertexColor()`](Texture.md#layeredregionsetvertexcolor), this color is a shading applied to the colors of the texture image; a color of `(1, 1, 1)` allows the image's original colors to show.

**Signature:**

```lua
Frame:SetBackdropBorderColor(red, green, blue [, alpha])
```

**Arguments:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

---

### Frame:SetBackdropColor

Sets a shading color for the frame's background graphic. As with [`Texture:SetVertexColor()`](Texture.md#layeredregionsetvertexcolor), this color is a shading applied to the colors of the texture image; a color of `(1, 1, 1)` allows the image's original colors to show.

**Signature:**

```lua
Frame:SetBackdropColor(red, green, blue [, alpha])
```

**Arguments:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the graphic (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

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

---

### Frame:SetClampedToScreen

Sets whether the frame's boundaries should be limited to those of the screen. Applies to user moving/resizing of the frame (via [`:StartMoving()`](Frame.md#framestartmoving), [`:StartSizing()`](Frame.md#framestartsizing), or [title region](Frame.md#framesettitleregion)); attempting to move or resize the frame beyond the edges of the screen will move/resize it no further than the edge of the screen closest to the mouse position. Does not apply to programmatically setting the frame's position or size.

**Signature:**

```lua
Frame:SetClampedToScreen(enable)
```

**Arguments:**

- `enable` - True to limit the frame's boundaries to those of the screen; false to allow the frame to be moved/resized without such limits (`boolean`)

---

### Frame:SetDepth

Sets the 3D depth of the frame (for stereoscopic 3D configurations)

**Signature:**

```lua
Frame:SetDepth(depth)
```

**Arguments:**

- `depth` - Apparent 3D depth of this frame relative to that of its parent frame (`number`)

---

### Frame:SetFrameLevel

Sets the level at which the frame is layered relative to others in its strata. Frames with higher frame level are layered "in front of" frames with a lower frame level.

**Signature:**

```lua
Frame:SetFrameLevel(level)
```

**Arguments:**

- `level` - Layering level of the frame relative to others in its [`frameStrata`](../types/frameStrata.md) (`number`)

---

### Frame:SetFrameStrata

Sets the general layering strata of the frame. Where [frame level](Frame.md#framesetframelevel) provides fine control over the layering of frames, frame strata provides a coarser level of layering control: frames in a higher strata always appear "in front of" frames in lower strata regardless of frame level.

**Signature:**

```lua
Frame:SetFrameStrata("strata")
```

**Arguments:**

- `strata` - Token identifying the strata in which the frame should be layered (`string`, [frameStrata](../types/frameStrata.md))

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

---

### Frame:SetID

Sets a numeric identifier for the frame. Frame IDs have no effect on frame behavior, but can be a useful way to keep track of multiple similar frames, especially in cases where a list of frames is created from a template (such as for action buttons, loot slots, or lines in a FauxScrollFrame).

**Signature:**

```lua
Frame:SetID(id)
```

**Arguments:**

- `id` - A numeric identifier for the frame (`number`)

---

### Frame:SetJumpNavigateEnabled

This function is not yet documented

**Signature:**

```lua
Frame:SetJumpNavigateEnabled()
```

---

### Frame:SetJumpNavigateStart

This function is not yet documented

**Signature:**

```lua
Frame:SetJumpNavigateStart()
```

---

### Frame:SetMaxResize

Sets the maximum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](Frame.md#framestartsizing).

**Signature:**

```lua
Frame:SetMaxResize(maxWidth, maxHeight)
```

**Arguments:**

- `maxWidth` - Maximum width of the frame (in pixels), or `0` for no limit (`number`)
- `maxHeight` - Maximum height of the frame (in pixels), or `0` for no limit (`number`)

---

### Frame:SetMinResize

Sets the minimum size of the frame for user resizing. Applies when resizing the frame with the mouse via [`:StartSizing()`](Frame.md#framestartsizing).

**Signature:**

```lua
Frame:SetMinResize(minWidth, minHeight)
```

**Arguments:**

- `minWidth` - Minimum width of the frame (in pixels), or `0` for no limit (`number`)
- `minHeight` - Minimum height of the frame (in pixels), or `0` for no limit (`number`)

---

### Frame:SetMovable

Sets whether the frame can be moved by the user. Enabling this property does not automatically implement behaviors allowing the frame to be dragged by the user -- such behavior must be implemented in the frame's mouse script handlers. If this property is not enabled, [`Frame:StartMoving()`](Frame.md#framestartmoving) causes a Lua error.

For simple automatic frame dragging behavior, see [`Frame:CreateTitleRegion()`](Frame.md#framecreatetitleregion).

**Signature:**

```lua
Frame:SetMovable(enable)
```

**Arguments:**

- `enable` - True to allow the frame to be moved by the user; false to disable (`boolean`)

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

### Frame:SetResizable

Sets whether the frame can be resized by the user. Enabling this property does not automatically implement behaviors allowing the frame to be drag-resized by the user -- such behavior must be implemented in the frame's mouse script handlers. If this property is not enabled, [`Frame:StartSizing()`](Frame.md#framestartsizing) causes a Lua error.

**Signature:**

```lua
Frame:SetResizable(enable)
```

**Arguments:**

- `enable` - True to allow the frame to be resized by the user; false to disable (`boolean`)

---

### Frame:SetScale

Sets the frame's scale factor. A frame's scale factor affects the size at which it appears on the screen relative to that of its parent. The entire interface may be scaled by changing `UIParent`'s scale factor (as can be done via the Use UI Scale setting in the default interface's Video Options panel).

**Signature:**

```lua
Frame:SetScale(scale)
```

**Arguments:**

- `scale` - Scale factor for the frame relative to its parent (`number`)

---

### Frame:SetScript

Sets a function to call for the given widget handler on this frame

**Signature:**

```lua
Frame:SetScript("type", function)
```

**Arguments:**

- `type` - The frame script to set a handler for (`string`)
  - `OnAnimFinished`
  - `OnAttributeChanged`
  - `OnChar`
  - `OnCharComposition`
  - `OnClick`
  - `OnColorSelect`
  - `OnCursorChanged`
  - `OnDoubleClick`
  - `OnDragStart`
  - `OnDragStop`
  - `OnEditFocusGained`
  - `OnEditFocusLost`
  - `OnEnter`
  - `OnEnterPressed`
  - `OnEscapePressed`
  - `OnEvent`
  - `OnHide`
  - `OnHorizontalScroll`
  - `OnHyperlinkClick`
  - `OnHyperlinkEnter`
  - `OnHyperlinkLeave`
  - `OnInputLanguageChanged`
  - `OnKeyDown`
  - `OnKeyUp`
  - `OnLeave`
  - `OnLoad`
  - `OnMessageScrollChanged`
  - `OnMouseDown`
  - `OnMouseUp`
  - `OnMouseWheel`
  - `OnReceiveDrag`
  - `OnScrollRangeChanged`
  - `OnShow`
  - `OnSizeChanged`
  - `OnSpacePressed`
  - `OnTabPressed`
  - `OnTextChanged`
  - `OnTextSet`
  - `OnTooltipAddMoney`
  - `OnTooltipCleared`
  - `OnTooltipSetDefaultAnchor`
  - `OnTooltipSetItem`
  - `OnTooltipSetQuest`
  - `OnTooltipSetSpell`
  - `OnTooltipSetUnit`
  - `OnUpdate`
  - `OnUpdateModel`
  - `OnValueChanged`
  - `OnVerticalScroll`
  - `PostClick`
  - `PreClick`
- `function` - The function to use as the given script handler. The signature of this function depends on the script. (`function`)

---

### Frame:SetToplevel

Sets whether the frame should automatically come to the front when clicked. When a frame with `Toplevel` behavior enabled is clicked, it automatically changes its [frame level](Frame.md#framesetframelevel) such that it is greater than (and therefore drawn "in front of") all other frames in its [strata](Frame.md#framesetframestrata).

**Signature:**

```lua
Frame:SetToplevel(enable)
```

**Arguments:**

- `enable` - True to cause the frame to automatically come to the front when clicked; false otherwise (`boolean`)

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

---

### Frame:StartSizing

Begins resizing the frame via mouse movement

**Signature:**

```lua
Frame:StartSizing()
```

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

Ends movement or resizing of the frame initiated with [`:StartMoving()`](Frame.md#framestartmoving) or [`:StartSizing()`](Frame.md#framestartsizing)

**Signature:**

```lua
Frame:StopMovingOrSizing()
```

---

### Frame:UnregisterAllEvents

Unregisters the frame from any [events](../Events.md) for which it is registered

**Signature:**

```lua
Frame:UnregisterAllEvents()
```

---

### Frame:UnregisterEvent

Unregisters the frame for an event. Once unregistered, the frame's [`OnEvent`](#onevent) script handler will not be called for that event.

Unregistering from notifications for an event can be useful for improving addon performance at times when it's not necessary to process the event. For example, a frame which monitors target health does not need to receive the [`UNIT_HEALTH`](../events/UNIT_HEALTH.md) event while the player has no target. An addon that sorts the contents of the player's bags can register for the [`BAG_UPDATE`](../events/BAG_UPDATE.md) event to keep track of when items are picked up, but unregister from the event while it performs its sorting.

**Signature:**

```lua
Frame:UnregisterEvent("event")
```

**Arguments:**

- `event` - Name of an [event](../Events.md) (`string`)

---

## Script Handlers

---

### OnAttributeChanged

Sets an arbitrary, named, taintless value on a frame.

**Signature:**

```lua
OnAttributeChanged(self, name, value)
```

---

### OnChar

Fires when a text character is received by a frame.

**Signature:**

```lua
OnChar(self, character)
```

---

### OnDragStart

Fires when the user starts moving the mouse after clicking down on the frame.

**Signature:**

```lua
OnDragStart(self, button)
```

---

### OnDragStop

Fires when you release the mouse button after beginning a drag on the frame.

**Signature:**

```lua
OnDragStop(self)
```

---

### OnEnter

Fires whenever the cursor becomes focused on a frame.

**Signature:**

```lua
OnEnter(self, motion)
```

---

### OnEvent

Fires on each frame that is registered for a given event.

**Signature:**

```lua
OnEvent(self, event, ...)
```

---

### OnHide

Fires when the frame is hidden.

**Signature:**

```lua
OnHide(self)
```

---

### OnKeyDown

Fires when the frame receives a "down" key press.

**Signature:**

```lua
OnKeyDown(self, key)
```

---

### OnKeyUp

Fires when the frame receives an "up" key press.

**Signature:**

```lua
OnKeyUp(self, key)
```

---

### OnLeave

Fires whenever the cursor is no longer focused on a frame.

**Signature:**

```lua
OnLeave(self, motion)
```

---

### OnLoad

Fires when a frame is first created.

**Signature:**

```lua
OnLoad(self)
```

---

### OnMouseDown

Fires when a mouse button is pressed down while the mouse-enabled frame has mouse focus. See also: OnMouseUp, OnClick

**Signature:**

```lua
OnMouseDown(self, button)
```

---

### OnMouseUp

Fires when the mouse button is released after clicking on a frame.

**Signature:**

```lua
OnMouseUp(self, button)
```

---

### OnMouseWheel

Fires for a mouse wheel-enabled frame when the user rolls the mouse wheel while over the frame.

**Signature:**

```lua
OnMouseWheel(self, delta)
```

---

### OnReceiveDrag

Fires when you release the mouse button over a frame after starting a drag.

**Signature:**

```lua
OnReceiveDrag(self)
```

---

### OnShow

Fires whenever a frame becomes visible after being not visible.

**Signature:**

```lua
OnShow(self)
```

---

### OnSizeChanged

Fires whenever a frame's size changes.

**Signature:**

```lua
OnSizeChanged(self, width, height)
```

---

### OnUpdate

Fires once for every visible frame each time the UI is rendered.

**Signature:**

```lua
OnUpdate(self, elapsed)
```

---

← [Widgets](../Widgets.md)
