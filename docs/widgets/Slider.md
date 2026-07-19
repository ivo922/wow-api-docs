# Slider

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/Slider)

Sliders are elements intended to display or allow the user to choose a value in a range. They are often used for configuration, to choose scale, camera distance, and similar settings. Like Buttons, Sliders can be enabled or disabled, but unlike Buttons, they include no support for automatically changing appearance when this is done. You can set both their minimum and maximum values (one function returns or accepts both), and the step by which dragging changes their value. Sliders can be oriented either horizontally or vertically.

While you do not have to provide any code to manage the dragging of a slider's "thumb", you do have to provide a texture that will represent it, which the engine will position and draw automatically. In XML, you do this by providing a `<ThumbTexture>` element as a direct child of the `<Slider>` element, which can have any of the attributes or children allowed to any `<Texture>` element.

Sliders come in two common forms: thin tracks with a wide thumb, used for setting scalar options, or scroll bars used for positioning the contents of a frame.

---

## Methods

---

### Frame:AllowAttributeChanges

Temporarily allows insecure code to modify the frame's attributes during combat. This permission is automatically rescinded when the frame's [`OnUpdate`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnUpdate) script next runs.

**Signature:**

```lua
Frame:AllowAttributeChanges()
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

### Slider:Disable

Disallows user interaction with the slider. Does not automatically change the visual state of the slider; directly making a visible change is recommended in order to communicate the change in state to the user.

**Signature:**

```lua
Slider:Disable()
```

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

### Slider:Enable

Allows user interaction with the slider

**Signature:**

```lua
Slider:Enable()
```

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
Slider:GetDontSavePosition()
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

### Slider:GetMinMaxValues

Returns the minimum and maximum values for the slider

**Signature:**

```lua
minValue, maxValue = Slider:GetMinMaxValues()
```

**Returns:**

- `minValue` - Lower boundary for values represented by the slider position (`number`)
- `maxValue` - Upper boundary for values represented by the slider position (`number`)

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

### Slider:GetOrientation

Returns the orientation of the slider

**Signature:**

```lua
orientation = Slider:GetOrientation()
```

**Returns:**

- `orientation` - Token describing the orientation and direction of the slider (`string`)
  - `HORIZONTAL` - Slider thumb moves from left to right as the slider's value increases
  - `VERTICAL` - Slider thumb moves from top to bottom as the slider's value increases

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

### Slider:GetThumbTexture

Returns the texture for the slider thumb

**Signature:**

```lua
texture = Slider:GetThumbTexture()
```

**Returns:**

- `texture` - Reference to the `Texture` object used for the slider thumb (`texture`)

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

### Slider:GetValue

Returns the value representing the current position of the slider thumb

**Signature:**

```lua
value = Slider:GetValue()
```

**Returns:**

- `value` - Value representing the current position of the slider thumb (between `minValue` and `maxValue`, where `minValue, maxValue = slider`[`:GetMinMaxValues()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Slider/GetMinMaxValues)) (`number`)

---

### Slider:GetValueStep

Returns the minimum increment between allowed slider values

**Signature:**

```lua
step = Slider:GetValueStep()
```

**Returns:**

- `step` - Minimum increment between allowed slider values (`number`)

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

### Slider:IsEnabled

Returns whether user interaction with the slider is allowed

**Signature:**

```lua
enabled = Slider:IsEnabled()
```

**Returns:**

- `enabled` - `1` if user interaction with the slider is allowed; otherwise `nil` (`1nil`)

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
enabled = Slider:IsJoystickEnabled()
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
Slider:SetDontSavePosition()
```

*Inherited from [Frame](Frame.md)*

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

### Slider:SetMinMaxValues

Sets the minimum and maximum values for the slider

**Signature:**

```lua
Slider:SetMinMaxValues(minValue, maxValue)
```

**Arguments:**

- `minValue` - Lower boundary for values represented by the slider position (`number`)
- `maxValue` - Upper boundary for values represented by the slider position (`number`)

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

### Slider:SetOrientation

Sets the orientation of the slider

**Signature:**

```lua
Slider:SetOrientation("orientation")
```

**Arguments:**

- `orientation` - Token describing the orientation and direction of the slider (`string`)
  - `HORIZONTAL` - Slider thumb moves from left to right as the slider's value increases
  - `VERTICAL` - Slider thumb moves from top to bottom as the slider's value increases (default)

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

### Slider:SetThumbTexture

Sets the texture for the slider thumb

**Signature:**

```lua
Slider:SetThumbTexture(texture [, "layer"]) or Slider:SetThumbTexture("filename" [, "layer"])
```

**Arguments:**

- `texture` - Reference to an existing `Texture` object (`texture`)
- `filename` - Path to a texture image file (`string`)
- `layer` - Graphics layer in which the texture should be drawn; defaults to `ARTWORK` if not specified (`string`, [layer](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#layer))

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

### Slider:SetValue

Sets the value representing the position of the slider thumb

**Signature:**

```lua
Slider:SetValue(value)
```

**Arguments:**

- `value` - Value representing the new position of the slider thumb (between `minValue` and `maxValue`, where `minValue, maxValue = slider`[`:GetMinMaxValues()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Slider/GetMinMaxValues)) (`number`)

---

### Slider:SetValueStep

Sets the minimum increment between allowed slider values. The portion of the slider frame's area in which the slider thumb moves is its width (or height, for vertical sliders) minus 16 pixels on either end. If the number of possible values determined by the slider's minimum, maximum, and step values is less than the width (or height) of this area, the step value also affects the movement of the slider thumb; see example for details.

**Signature:**

```lua
Slider:SetValueStep(step)
```

**Arguments:**

- `step` - Minimum increment between allowed slider values (`number`)

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

### OnMinMaxChanged

Run when the slider's or status bar's minimum and maximum values change

**Signature:**

```lua
OnMinMaxChanged(self, min, max)
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

### OnUpdate

Run each time the screen is drawn by the game engine

**Signature:**

```lua
OnUpdate(self, elapsed)
```

---

### OnValueChanged

Run when the slider's or status bar's value changes

**Signature:**

```lua
OnValueChanged(self, value)
```

---

← [Widgets](../Widgets.md)
