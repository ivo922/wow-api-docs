# VisibleRegion

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/VisibleRegion)

VisibleRegion is an abstract UI type used to describe the common functionality of objects that can be placed on the screen, and visible. In particular, methods exist to show and hide the frame, and change the alpha transparency.

---

## Methods

---

### VisibleRegion:CanChangeProtectedState

Returns whether protected properties of the region can be changed by non-secure scripts

**Signature:**

```lua
canChange = VisibleRegion:CanChangeProtectedState()
```

---

### VisibleRegion:ClearAllPoints

Removes all anchor points from the region

**Signature:**

```lua
VisibleRegion:ClearAllPoints()
```

---

### VisibleRegion:CreateAnimationGroup

Creates a new AnimationGroup as a child of the region

**Signature:**

```lua
animationGroup = VisibleRegion:CreateAnimationGroup(["name" [, "inheritsFrom"]])
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

---

### VisibleRegion:GetAnimationGroups

Returns a list of animation groups belonging to the region

**Signature:**

```lua
... = VisibleRegion:GetAnimationGroups()
```

---

### VisibleRegion:GetBottom

Returns the distance from the bottom of the screen to the bottom of the region

**Signature:**

```lua
bottom = VisibleRegion:GetBottom()
```

---

### VisibleRegion:GetCenter

Returns the screen coordinates of the region's center

**Signature:**

```lua
x, y = VisibleRegion:GetCenter()
```

---

### VisibleRegion:GetHeight

Returns the height of the region

**Signature:**

```lua
height = VisibleRegion:GetHeight()
```

---

### VisibleRegion:GetLeft

Returns the distance from the left edge of the screen to the left edge of the region

**Signature:**

```lua
left = VisibleRegion:GetLeft()
```

---

### VisibleRegion:GetName

Returns the widget object's name

**Signature:**

```lua
name = VisibleRegion:GetName()
```

---

### VisibleRegion:GetNumPoints

Returns the number of anchor points defined for the region

**Signature:**

```lua
numPoints = VisibleRegion:GetNumPoints()
```

---

### VisibleRegion:GetObjectType

Returns the object's widget type

**Signature:**

```lua
type = VisibleRegion:GetObjectType()
```

---

### VisibleRegion:GetParent

Returns the region's parent region

**Signature:**

```lua
parent = VisibleRegion:GetParent()
```

---

### VisibleRegion:GetPoint

Returns information about one of the region's anchor points

**Signature:**

```lua
point, relativeTo, relativePoint, xOffset, yOffset = VisibleRegion:GetPoint(index)
```

---

### VisibleRegion:GetRect

Returns the position and dimensions of the region

**Signature:**

```lua
left, bottom, width, height = VisibleRegion:GetRect()
```

---

### VisibleRegion:GetRight

Returns the distance from the left edge of the screen to the right edge of the region

**Signature:**

```lua
right = VisibleRegion:GetRight()
```

---

### VisibleRegion:GetTop

Returns the distance from the bottom of the screen to the top of the region

**Signature:**

```lua
top = VisibleRegion:GetTop()
```

---

### VisibleRegion:GetWidth

Returns the width of the region

**Signature:**

```lua
width = VisibleRegion:GetWidth()
```

---

### VisibleRegion:Hide

Hides the region

**Signature:**

```lua
VisibleRegion:Hide()
```

---

### VisibleRegion:IsDragging

Returns whether the region is currently being dragged

**Signature:**

```lua
isDragging = VisibleRegion:IsDragging()
```

---

### VisibleRegion:IsObjectType

Returns whether the object belongs to a given widget type

**Signature:**

```lua
isType = VisibleRegion:IsObjectType("type")
```

---

### VisibleRegion:IsProtected

Returns whether the region is protected

**Signature:**

```lua
isProtected, explicit = VisibleRegion:IsProtected()
```

---

### VisibleRegion:IsShown

Returns whether the region is shown. Indicates only whether the region has been explicitly shown or hidden -- a region may be explicitly shown but not appear on screen because its parent region is hidden. See [`VisibleRegion:IsVisible()`](VisibleRegion.md#visibleregionisvisible) to test for actual visibility.

**Signature:**

```lua
shown = VisibleRegion:IsShown()
```

**Returns:**

- `shown` - `1` if the region is shown; otherwise `nil` (`1nil`)

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

---

### VisibleRegion:SetAllPoints

Sets all anchor points of the region to match those of another region

**Signature:**

```lua
VisibleRegion:SetAllPoints([region]) or VisibleRegion:SetAllPoints(["name"])
```

---

### VisibleRegion:SetAlpha

Sets the opacity of the region relative to its parent

**Signature:**

```lua
VisibleRegion:SetAlpha(alpha)
```

**Arguments:**

- `alpha` - Alpha (opacity) of the region (0.0 = fully transparent, 1.0 = fully opaque) (`number`)

---

### VisibleRegion:SetHeight

Sets the region's height

**Signature:**

```lua
VisibleRegion:SetHeight(height)
```

---

### VisibleRegion:SetParent

Makes another region the parent of this region

**Signature:**

```lua
VisibleRegion:SetParent(region) or VisibleRegion:SetParent("name")
```

---

### VisibleRegion:SetPoint

Sets an anchor point for the region

**Signature:**

```lua
VisibleRegion:SetPoint("point" [, relativeTo [, "relativePoint" [, xOffset [, yOffset]]]])
```

---

### VisibleRegion:SetWidth

Sets the region's width

**Signature:**

```lua
VisibleRegion:SetWidth(width)
```

---

### VisibleRegion:Show

Shows the region

**Signature:**

```lua
VisibleRegion:Show()
```

---

### VisibleRegion:StopAnimating

Stops any active animations involving the region or its children

**Signature:**

```lua
VisibleRegion:StopAnimating()
```

---

← [Widgets](../Widgets.md)
