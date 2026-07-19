# Texture

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/Texture)

Textures are visible areas descended from LayeredRegion, that display either a color block, a gradient, or a graphic raster taken from a .tga or .blp file. Most of their methods relate to setting their appearance or their source information.

Textures are created as children of Frame elements in XML, or by calling `Frame:CreateTexture()` from Lua. They cannot be reassigned from one frame to another, although you can create another texture on another frame that has the same source. They can also be created in XML with the virtual tag, allowing several similar textures to be created easily.

The WoW client only loads those files that existed when the client was first opened. If you add texture files to your addon's directory, you will need to restart your client in order for those textures to be loadable by the client. Changes to existing files do not have this same restriction.

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

### Texture:GetBlendMode

Returns the blend mode of the texture

**Signature:**

```lua
mode = Texture:GetBlendMode()
```

**Returns:**

- `mode` - Blend mode of the texture (`string`)
  - `ADD` - Adds texture color values to the underlying color values, using the alpha channel; light areas in the texture lighten the background while dark areas are more transparent
  - `ALPHAKEY` - One-bit transparency; pixels with alpha values greater than ~0.8 are treated as fully opaque and all other pixels are treated as fully transparent
  - `BLEND` - Normal color blending, using any alpha channel in the texture image
  - `DISABLE` - Ignores any alpha channel, displaying the texture as fully opaque
  - `MOD` - Ignores any alpha channel in the texture and multiplies texture color values by background color values; dark areas in the texture darken the background while light areas are more transparent

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

### Region:GetHeight

Returns the height of the region.

**Signature:**

```lua
Region:GetHeight()
```

*Inherited from [Region](Region.md)*

---

### Texture:GetHorizTile

This function is not yet documented

**Signature:**

```lua
Texture:GetHorizTile()
```

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

### Texture:GetNonBlocking

Returns whether the texture object loads its image file in the background. See [`:SetNonBlocking()`](Texture.md#texturesetnonblocking) for further details.

**Signature:**

```lua
nonBlocking = Texture:GetNonBlocking()
```

**Returns:**

- `nonBlocking` - `1` if the texture object loads its image file in the background; `nil` if the game engine is halted while the texture loads (`1nil`)

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

### Texture:GetTexCoord

Returns corner coordinates for scaling or cropping the texture image. See [`Texture:SetTexCoord()`](Texture.md#texturesettexcoord) example for details.

**Signature:**

```lua
ULx, ULy, LLx, LLy, URx, URy, LRx, LRy = Texture:GetTexCoord()
```

**Returns:**

- `ULx` - Upper left corner X position, as a fraction of the image's width from the left (`number`)
- `ULy` - Upper left corner Y position, as a fraction of the image's height from the top (`number`)
- `LLx` - Lower left corner X position, as a fraction of the image's width from the left (`number`)
- `LLy` - Lower left corner Y position, as a fraction of the image's height from the top (`number`)
- `URx` - Upper right corner X position, as a fraction of the image's width from the left (`number`)
- `URy` - Upper right corner Y position, as a fraction of the image's height from the top (`number`)
- `LRx` - Lower right corner X position, as a fraction of the image's width from the left (`number`)
- `LRy` - Lower right corner Y position, as a fraction of the image's height from the top (`number`)

---

### Texture:GetTexture

Returns the path to the texture's image file

**Signature:**

```lua
texture = Texture:GetTexture()
```

**Returns:**

- `texture` - Path to the texture image file, or one of the following values: (`string`)
  - `Portrait1` - Texture is set to a generated image (e.g. via [`SetPortraitTexture()`](../categories/Unit.md#setportraittexture))
  - `SolidTexture` - Texture is set to a solid color instead of an image

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

### Texture:GetVertTile

This function is not yet documented

**Signature:**

```lua
Texture:GetVertTile()
```

---

### Texture:GetVertexColor

Returns the shading color of the texture. For details about vertex color shading, see [`LayeredRegion:SetVertexColor()`](LayeredRegion.md#layeredregionsetvertexcolor).

**Signature:**

```lua
red, green, blue, alpha = Texture:GetVertexColor()
```

**Returns:**

- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the texture (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

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

### Texture:IsDesaturated

Returns whether the texture image should be displayed with zero saturation (i.e. converted to grayscale). The texture may not actually be displayed in grayscale if the current display hardware doesn't support that feature; see [`Texture:SetDesaturated()`](Texture.md#texturesetdesaturated) for details.

**Signature:**

```lua
desaturated = Texture:IsDesaturated()
```

**Returns:**

- `desaturated` - `1` if the texture should be displayed in grayscale; otherwise `nil` (`1nil`)

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

### Texture:SetBlendMode

Sets the blend mode of the texture

**Signature:**

```lua
Texture:SetBlendMode("mode")
```

**Arguments:**

- `mode` - Blend mode of the texture (`string`)
  - `ADD` - Adds texture color values to the underlying color values, using the alpha channel; light areas in the texture lighten the background while dark areas are more transparent
  - `ALPHAKEY` - One-bit transparency; pixels with alpha values greater than ~0.8 are treated as fully opaque and all other pixels are treated as fully transparent
  - `BLEND` - Normal color blending, using any alpha channel in the texture image
  - `DISABLE` - Ignores any alpha channel, displaying the texture as fully opaque
  - `MOD` - Ignores any alpha channel in the texture and multiplies texture color values by background color values; dark areas in the texture darken the background while light areas are more transparent

---

### Texture:SetDesaturated

Sets whether the texture image should be displayed with zero saturation (i.e. converted to grayscale). Returns `nil` if the current system does not support texture desaturation; in such cases, this method has no visible effect (but still flags the texture object as desaturated). Authors may wish to implement an alternative to desaturation for such cases (see example).

**Signature:**

```lua
supported = Texture:SetDesaturated(desaturate)
```

**Arguments:**

- `desaturate` - True to display the texture in grayscale; false to display original texture colors (`boolean`)

**Returns:**

- `supported` - `1` if the current system supports texture desaturation; otherwise `nil` (`1nil`)

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

### Texture:SetGradient

Sets a gradient color shading for the texture. Gradient color shading does not change the underlying color of the texture image, but acts as a filter: see [`LayeredRegion:SetVertexColor()`](LayeredRegion.md#layeredregionsetvertexcolor) for details.

**Signature:**

```lua
Texture:SetGradient("orientation", startR, startG, startB, endR, endG, endB)
```

**Arguments:**

- `orientation` - Token identifying the direction of the gradient (`string`)
  - `HORIZONTAL` - Start color on the left, end color on the right
  - `VERTICAL` - Start color at the bottom, end color at the top
- `startR` - Red component of the start color (0.0 - 1.0) (`number`)
- `startG` - Green component of the start color (0.0 - 1.0) (`number`)
- `startB` - Blue component of the start color (0.0 - 1.0) (`number`)
- `endR` - Red component of the end color (0.0 - 1.0) (`number`)
- `endG` - Green component of the end color (0.0 - 1.0) (`number`)
- `endB` - Blue component of the end color (0.0 - 1.0) (`number`)

---

### Texture:SetGradientAlpha

Sets a gradient color shading for the texture (including opacity in the gradient). Gradient color shading does not change the underlying color of the texture image, but acts as a filter: see [`LayeredRegion:SetVertexColor()`](LayeredRegion.md#layeredregionsetvertexcolor) for details.

**Signature:**

```lua
Texture:SetGradientAlpha("orientation", startR, startG, startB, startAlpha, endR, endG, endB, endAlpha)
```

**Arguments:**

- `orientation` - Token identifying the direction of the gradient (`string`)
  - `HORIZONTAL` - Start color on the left, end color on the right
  - `VERTICAL` - Start color at the bottom, end color at the top
- `startR` - Red component of the start color (0.0 - 1.0) (`number`)
- `startG` - Green component of the start color (0.0 - 1.0) (`number`)
- `startB` - Blue component of the start color (0.0 - 1.0) (`number`)
- `startAlpha` - Alpha (opacity) for the start side of the gradient (0.0 = fully transparent, 1.0 = fully opaque) (`number`)
- `endR` - Red component of the end color (0.0 - 1.0) (`number`)
- `endG` - Green component of the end color (0.0 - 1.0) (`number`)
- `endB` - Blue component of the end color (0.0 - 1.0) (`number`)
- `endAlpha` - Alpha (opacity) for the end side of the gradient (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

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

### Texture:SetHorizTile

This function is not yet documented

**Signature:**

```lua
Texture:SetHorizTile()
```

---

### Texture:SetNonBlocking

Sets whether the texture object loads its image file in the background. Texture loading is normally synchronous, so that UI objects are not shown partially textured while loading; however, non-blocking (asynchronous) texture loading may be desirable in some cases where large numbers of textures need to be loaded in a short time. This feature is used in the default UI's icon chooser window for macros and equipment sets, allowing a large number of icon textures to be loaded without causing the game's frame rate to stagger.

**Signature:**

```lua
Texture:SetNonBlocking(nonBlocking)
```

**Arguments:**

- `nonBlocking` - True to allow the texture object to load its image file in the background; false (default) to halt the game engine while the texture loads (`boolean`)

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

### Texture:SetRotation

Rotates the texture image. This is an efficient shorthand for the more complex `Texture:SetTexCoord()`.

**Signature:**

```lua
Texture:SetRotation(radians)
```

**Arguments:**

- `radians` - Amount by which the texture image should be rotated (in radians; positive values for counter-clockwise rotation, negative for clockwise) (`number`)

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

### Texture:SetTexCoord

Sets corner coordinates for scaling or cropping the texture image. See example for details.

**Signature:**

```lua
Texture:SetTexCoord(left, right, top, bottom) or Texture:SetTexCoord(ULx, ULy, LLx, LLy, URx, URy, LRx, LRy)
```

**Arguments:**

- `left` - Left edge of the scaled/cropped image, as a fraction of the image's width from the left (`number`)
- `right` - Right edge of the scaled/cropped image, as a fraction of the image's width from the left (`number`)
- `top` - Top edge of the scaled/cropped image, as a fraction of the image's height from the top (`number`)
- `bottom` - Bottom edge of the scaled/cropped image, as a fraction of the image's height from the top (`number`)
- `ULx` - Upper left corner X position, as a fraction of the image's width from the left (`number`)
- `ULy` - Upper left corner Y position, as a fraction of the image's height from the top (`number`)
- `LLx` - Lower left corner X position, as a fraction of the image's width from the left (`number`)
- `LLy` - Lower left corner Y position, as a fraction of the image's height from the top (`number`)
- `URx` - Upper right corner X position, as a fraction of the image's width from the left (`number`)
- `URy` - Upper right corner Y position, as a fraction of the image's height from the top (`number`)
- `LRx` - Lower right corner X position, as a fraction of the image's width from the left (`number`)
- `LRy` - Lower right corner Y position, as a fraction of the image's height from the top (`number`)

---

### Texture:SetTexture

Sets the texture object's image or color. Returns `nil` if the texture could not be set (e.g. if the file path is invalid or points to a file which cannot be used as a texture).

**Signature:**

```lua
visible = Texture:SetTexture("texture") or Texture:SetTexture(red, green, blue [, alpha])
```

**Arguments:**

- `texture` - Path to a texture image (`string`)
- `red` - Red component of the color (0.0 - 1.0) (`number`)
- `green` - Green component of the color (0.0 - 1.0) (`number`)
- `blue` - Blue component of the color (0.0 - 1.0) (`number`)
- `alpha` - Alpha (opacity) for the color (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

**Returns:**

- `visible` - `1` if the texture was successfully changed; otherwise `nil` (`1nil`)

---

### Texture:SetVertTile

This function is not yet documented

**Signature:**

```lua
Texture:SetVertTile()
```

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
