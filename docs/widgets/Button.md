# Button

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/Button)

---

## Methods

---

### Button:AllowAttributeChanges

Temporarily allows insecure code to modify attributes on the Frame during combat.

**Signature:**

```lua
Button:AllowAttributeChanges()
```

---

### Button:CanChangeProtectedState

Returns whether or not a frame can make a protected change

**Signature:**

```lua
canChange = Button:CanChangeProtectedState()
```

---

### Button:ClearAllPoints

Clear all anchor point for the given region

**Signature:**

```lua
Button:ClearAllPoints()
```

---

### Button:Click

Performs a (virtual) mouse click on the button. Causes any of the button's mouse click-related [scripts](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts) to be run as if the button were clicked by the user.

Calling this method can result in an error if the button inherits from a secure frame template and performs protected actions.

**Signature:**

```lua
Button:Click("button", down)
```

**Arguments:**

- `button` - Name of the mouse button for the click action (`string`)
  - `Button4`
  - `Button5`
  - `LeftButton`
  - `MiddleButton`
  - `RightButton`
- `down` - True for a "mouse down" click action, false for "mouse up" or other click actions (`boolean`)

---

### Button:CreateAnimationGroup

Create and return a new AnimationGroup as a child of this Region

**Signature:**

```lua
Button:CreateAnimationGroup(["name" [, "inheritsFrom"]])
```

---

### Button:CreateFontString

Creates a new FontString for the Frame on a given layer, possibly inheriting from a template

**Signature:**

```lua
Button:CreateFontString(["name" [, "layer" [, "inherits"]]])
```

---

### Button:CreateTexture

Creates a new Texture for the Frame on the given layer, optionally inheriting from a template.

**Signature:**

```lua
Button:CreateTexture(["name" [, "layer" [, "inherits"]]])
```

---

### Button:CreateTitleRegion

Creates a title region for the frame

**Signature:**

```lua
Button:CreateTitleRegion()
```

---

### Button:Disable

Disallows user interaction with the button. Automatically changes the visual state of the button if its DisabledTexture, DisabledTextColor or DisabledFontObject are set.

**Signature:**

```lua
Button:Disable()
```

---

### Button:DisableDrawLayer

Disables rendering of the Frame's specified layer.

**Signature:**

```lua
Button:DisableDrawLayer("layer")
```

---

### Button:Enable

Allows user interaction with the button. If a disabled appearance was specified for the button, automatically returns the button to its normal appearance.

**Signature:**

```lua
Button:Enable()
```

---

### Button:EnableDrawLayer

Enables rendering of the Frame's specified layer.

**Signature:**

```lua
Button:EnableDrawLayer("layer")
```

---

### Button:EnableJoystick

Enables or disables joystick interactivity

**Signature:**

```lua
Button:EnableJoystick(enable)
```

---

### Button:EnableKeyboard

Enables or disables keyboard interactivity

**Signature:**

```lua
Button:EnableKeyboard(enable)
```

---

### Button:EnableMouse

Enables or disables mouse interactivity

**Signature:**

```lua
Button:EnableMouse(enable)
```

---

### Button:EnableMouseWheel

Enables or disables mousewheel interactivity

**Signature:**

```lua
Button:EnableMouseWheel(enable)
```

---

### Button:GetAlpha

Returns the current alpha value for the region

**Signature:**

```lua
alpha = Button:GetAlpha()
```

---

### Button:GetAnimationGroups

Returns a list of animation groups belonging to this region

**Signature:**

```lua
... = Button:GetAnimationGroups()
```

---

### Button:GetAttribute

Returns the value of a frame attribute

**Signature:**

```lua
value = Button:GetAttribute("name")
```

---

### Button:GetBackdrop

Returns the backdrop information for the frame

**Signature:**

```lua
backdropTbl = Button:GetBackdrop()
```

---

### Button:GetBackdropBorderColor

Returns the color of the frame's backdrop border

**Signature:**

```lua
r, g, b, a = Button:GetBackdropBorderColor()
```

---

### Button:GetBackdropColor

Returns the frame's backdrop color

**Signature:**

```lua
r, g, b, a = Button:GetBackdropColor()
```

---

### Button:GetBottom

Returns the distance in pixels from the bottom of the screen to the bottom of the Region.

**Signature:**

```lua
bottom = Button:GetBottom()
```

---

### Button:GetBoundsRect

Returns the frame's boundaries, including all sub-regions

**Signature:**

```lua
left, bottom, width, height = Button:GetBoundsRect()
```

---

### Button:GetButtonState

Returns the button's current state

**Signature:**

```lua
state = Button:GetButtonState()
```

**Returns:**

- `state` - State of the button (`string`)
  - `DISABLED` - Button is disabled and cannot receive user input
  - `NORMAL` - Button is in its normal state
  - `PUSHED` - Button is pushed (as during a click on the button)

---

### Button:GetCenter

Returns the screen coordinates of the Region's center.

**Signature:**

```lua
Button:GetCenter()
```

---

### Button:GetChildren

Returns the list of child frames

**Signature:**

```lua
Button:GetChildren()
```

---

### Button:GetClampRectInsets

Returns the rect insets for the clampedtoscreen system

**Signature:**

```lua
Button:GetClampRectInsets()
```

---

### Button:GetDepth

This function is not yet documented

**Signature:**

```lua
Button:GetDepth()
```

---

### Button:GetDisabledFontObject

Returns the font object used for the button's disabled state

**Signature:**

```lua
font = Button:GetDisabledFontObject()
```

**Returns:**

- `font` - Reference to the `Font` object used when the button is disabled (`font`)

---

### Button:GetDisabledTexture

Returns the texture used when the button is disabled

**Signature:**

```lua
texture = Button:GetDisabledTexture()
```

**Returns:**

- `texture` - Reference to the `Texture` object used when the button is disabled (`texture`)

---

### Button:GetEffectiveAlpha

Returns the frame's effective alpha

**Signature:**

```lua
Button:GetEffectiveAlpha()
```

---

### Button:GetEffectiveDepth

This function is not yet documented

**Signature:**

```lua
Button:GetEffectiveDepth()
```

---

### Button:GetEffectiveScale

Returns the frame's effective scale

**Signature:**

```lua
Button:GetEffectiveScale()
```

---

### Button:GetFontString

Returns the `FontString` object used for the button's label text

**Signature:**

```lua
fontstring = Button:GetFontString()
```

**Returns:**

- `fontstring` - Reference to the `FontString` object used for the button's label text (`fontstring`)

---

### Button:GetFrameLevel

Returns the current frame level

**Signature:**

```lua
Button:GetFrameLevel()
```

---

### Button:GetFrameStrata

Returns the current framestrata

**Signature:**

```lua
strata = Button:GetFrameStrata()
```

---

### Button:GetFrameType

Returns the type of the frame, as a string

**Signature:**

```lua
Button:GetFrameType()
```

---

### Button:GetHeight

Returns the height of the region.

**Signature:**

```lua
Button:GetHeight()
```

---

### Button:GetHighlightFontObject

Returns the font object used when the button is highlighted

**Signature:**

```lua
font = Button:GetHighlightFontObject()
```

**Returns:**

- `font` - Reference to the `Font` object used when the button is highlighted (`font`)

---

### Button:GetHighlightTexture

Returns the texture used when the button is highlighted

**Signature:**

```lua
texture = Button:GetHighlightTexture()
```

**Returns:**

- `texture` - Reference to the `Texture` object used when the button is highlighted (`texture`)

---

### Button:GetHitRectInsets

Returns the inserts for the frame's HitRect

**Signature:**

```lua
Button:GetHitRectInsets()
```

---

### Button:GetID

Returns the frame's numeric identifier

**Signature:**

```lua
Button:GetID()
```

---

### Button:GetLeft

Returns the distance in pixels between left edge of the screen and the left edge of the Region.

**Signature:**

```lua
Button:GetLeft()
```

---

### Button:GetMaxResize

Returns the maximum resize width and height

**Signature:**

```lua
Button:GetMaxResize()
```

---

### Button:GetMinResize

Returns the minimum resize height and width

**Signature:**

```lua
Button:GetMinResize()
```

---

### Button:GetName

Returns the name of the object.

**Signature:**

```lua
Button:GetName()
```

---

### Button:GetNormalFontObject

Returns the font object used for the button's normal state

**Signature:**

```lua
font = Button:GetNormalFontObject()
```

**Returns:**

- `font` - Reference to the `Font` object used for the button's normal state (`font`)

---

### Button:GetNormalTexture

Returns the texture used for the button's normal state

**Signature:**

```lua
texture = Button:GetNormalTexture()
```

**Returns:**

- `texture` - Reference to the `Texture` object used for the button's normal state (`texture`)

---

### Button:GetNumChildren

Returns the number of children this frame has

**Signature:**

```lua
Button:GetNumChildren()
```

---

### Button:GetNumPoints

Returns the number of anchor points set for the frame.

**Signature:**

```lua
Button:GetNumPoints()
```

---

### Button:GetNumRegions

Returns the number of regions belonging to this frame

**Signature:**

```lua
Button:GetNumRegions()
```

---

### Button:GetObjectType

Returns the type of the object ("Frame", "Button", etc.).

**Signature:**

```lua
Button:GetObjectType()
```

---

### Button:GetParent

Returns the Region's parent object.

**Signature:**

```lua
Button:GetParent()
```

---

### Button:GetPoint

Returns the specified anchor point for the frame.

**Signature:**

```lua
Button:GetPoint()
```

---

### Button:GetPushedTextOffset

Returns the offset for moving the button's label text when pushed

**Signature:**

```lua
x, y = Button:GetPushedTextOffset()
```

**Returns:**

- `x` - Horizontal offset for the text (in pixels; values increasing to the right) (`number`)
- `y` - Vertical offset for the text (in pixels; values increasing upward) (`number`)

---

### Button:GetPushedTexture

Returns the texture used when the button is pushed

**Signature:**

```lua
texture = Button:GetPushedTexture()
```

**Returns:**

- `texture` - Reference to the `Texture` object used when the button is pushed (`texture`)

---

### Button:GetRect

Returns the rectangle position and size for the Region.

**Signature:**

```lua
left, bottom, width, height = Button:GetRect()
```

---

### Button:GetRegions

Returns the regions (fontstrings, textures) that belong to this frame

**Signature:**

```lua
Button:GetRegions()
```

---

### Button:GetRight

Returns the distance in pixels between left edge of the screen and the right edge of the Region.

**Signature:**

```lua
Button:GetRight()
```

---

### Button:GetScale

Returns the scale of the frame

**Signature:**

```lua
Button:GetScale()
```

---

### Button:GetScript

Returns the handler function for a given widget script

**Signature:**

```lua
handler = Button:GetScript("scriptType")
```

---

### Button:GetText

Returns the text of the button's label

**Signature:**

```lua
text = Button:GetText()
```

**Returns:**

- `text` - Text of the button's label (`string`)

---

### Button:GetTextHeight

Returns the height of the button's text label. Reflects the height of the rendered text (which increases if the text wraps onto two lines), not the point size of the text's font.

**Signature:**

```lua
height = Button:GetTextHeight()
```

**Returns:**

- `height` - Height of the button's text (in pixels) (`number`)

---

### Button:GetTextWidth

Returns the width of the button's text label

**Signature:**

```lua
width = Button:GetTextWidth()
```

**Returns:**

- `width` - Width of the button's text (in pixels) (`number`)

---

### Button:GetTitleRegion

Returns the TitleRegion object for the frame.

**Signature:**

```lua
Button:GetTitleRegion()
```

---

### Button:GetTop

Returns the distance in pixels between the bottom of the screen and the top of the Region.

**Signature:**

```lua
top = Button:GetTop()
```

---

### Button:GetWidth

Returns the width of the Region

**Signature:**

```lua
Button:GetWidth()
```

---

### Button:HasScript

Returns whether or not a widget supports the given script handler

**Signature:**

```lua
hasScript = Button:HasScript("scriptType")
```

---

### Button:Hide

Hides the region

**Signature:**

```lua
Button:Hide()
```

---

### Button:HookScript

Securely hooks a widget handler script

**Signature:**

```lua
Button:HookScript()
```

---

### Button:IgnoreDepth

This function is not yet documented

**Signature:**

```lua
Button:IgnoreDepth()
```

---

### Button:IsClampedToScreen

Returns whether or not the frame is clamped to the screen

**Signature:**

```lua
Button:IsClampedToScreen()
```

---

### Button:IsDragging

This function is not yet documented

**Signature:**

```lua
Button:IsDragging()
```

---

### Button:IsEnabled

Returns if the button is enabled

**Signature:**

```lua
isEnabled = Button:IsEnabled()
```

---

### Button:IsEventRegistered

Returns whether or not the frame is registered for the given event

**Signature:**

```lua
Button:IsEventRegistered()
```

---

### Button:IsFrameType

Returns whether or not the frame is of the given type

**Signature:**

```lua
Button:IsFrameType()
```

---

### Button:IsIgnoringDepth

This function is not yet documented

**Signature:**

```lua
Button:IsIgnoringDepth()
```

---

### Button:IsJoystickEnabled

This function is not yet documented

**Signature:**

```lua
Button:IsJoystickEnabled()
```

---

### Button:IsJumpNavigateEnabled

This function is not yet documented

**Signature:**

```lua
Button:IsJumpNavigateEnabled()
```

---

### Button:IsJumpNavigateStart

This function is not yet documented

**Signature:**

```lua
Button:IsJumpNavigateStart()
```

---

### Button:IsKeyboardEnabled

Returns whether or not the frame is keyboard enabled

**Signature:**

```lua
Button:IsKeyboardEnabled()
```

---

### Button:IsMouseEnabled

Returns whether or not the frame is mouse enabled

**Signature:**

```lua
Button:IsMouseEnabled()
```

---

### Button:IsMouseWheelEnabled

Returns whether or not the frame is mouse wheel enabled

**Signature:**

```lua
Button:IsMouseWheelEnabled()
```

---

### Button:IsMovable

Returns whether or not the frame is movable

**Signature:**

```lua
Button:IsMovable()
```

---

### Button:IsObjectType

Returns whether the object is of the given type ("Frame", "Button", etc.).

**Signature:**

```lua
Button:IsObjectType()
```

---

### Button:IsProtected

Indicates that insecure code cannot call protected methods of this region during combat.

**Signature:**

```lua
isProtected, explicit = Button:IsProtected()
```

---

### Button:IsResizable

Returns whether or not the frame is resizable

**Signature:**

```lua
Button:IsResizable()
```

---

### Button:IsShown

Returns if the region is shown

**Signature:**

```lua
Button:IsShown()
```

---

### Button:IsToplevel

Returns whether or not the frame is at the top level

**Signature:**

```lua
Button:IsToplevel()
```

---

### Button:IsUserPlaced

Returns whether or not the frame is flagged as "user placed"

**Signature:**

```lua
Button:IsUserPlaced()
```

---

### Button:IsVisible

Returns if the region is visible

**Signature:**

```lua
Button:IsVisible()
```

---

### Button:LockHighlight

Locks the button's highlight state, so it is always drawn as highlighted

**Signature:**

```lua
Button:LockHighlight()
```

---

### Button:Lower

Lowers the frame's frameLevel

**Signature:**

```lua
Button:Lower()
```

---

### Button:Raise

Raises the frame's frameLevel

**Signature:**

```lua
Button:Raise()
```

---

### Button:RegisterAllEvents

Registers the frame for all events

**Signature:**

```lua
Button:RegisterAllEvents()
```

---

### Button:RegisterEvent

Registers the frame for an event

**Signature:**

```lua
Button:RegisterEvent()
```

---

### Button:RegisterForClicks

Registers a button to receive mouse clicks

**Signature:**

```lua
Button:RegisterForClicks("...")
```

---

### Button:RegisterForDrag

Registers the frame for dragging via specific mouse buttons

**Signature:**

```lua
Button:RegisterForDrag()
```

---

### Button:SetAllPoints

Sets all anchors of this region to match the given region's

**Signature:**

```lua
Button:SetAllPoints()
```

---

### Button:SetAlpha

Sets the alpha value for the given region

**Signature:**

```lua
Button:SetAlpha(alpha)
```

---

### Button:SetAttribute

Sets an attribute on the given frame

**Signature:**

```lua
Button:SetAttribute()
```

---

### Button:SetBackdrop

Sets a frame's backdrop as defined by a table

**Signature:**

```lua
Button:SetBackdrop()
```

---

### Button:SetBackdropBorderColor

Sets the color of the frame's backdrop border

**Signature:**

```lua
Button:SetBackdropBorderColor(r, g, b [, a])
```

---

### Button:SetBackdropColor

Sets the backdrop color for the frame

**Signature:**

```lua
Button:SetBackdropColor(r, g, b [, a])
```

---

### Button:SetButtonState

Sets the button's state

**Signature:**

```lua
Button:SetButtonState("state", lock)
```

**Arguments:**

- `state` - State for the button (`string`)
  - `DISABLED` - Button is disabled and cannot receive user input
  - `NORMAL` - Button is in its normal state
  - `PUSHED` - Button is pushed (as during a click on the button)
- `lock` - Locks the button in the given state; e.g. if `NORMAL`, the button cannot be clicked but remains in the `NORMAL` state (`boolean`)

---

### Button:SetClampRectInsets

Sets the clamp rect insets for the frame, so portion of it could move offscreen

**Signature:**

```lua
Button:SetClampRectInsets()
```

---

### Button:SetClampedToScreen

Sets whether or not the frame should be clamped to the screen

**Signature:**

```lua
Button:SetClampedToScreen()
```

---

### Button:SetDepth

This function is not yet documented

**Signature:**

```lua
Button:SetDepth()
```

---

### Button:SetDisabledFontObject

Sets the font object to be used when the button is disabled

**Signature:**

```lua
Button:SetDisabledFontObject(font)
```

---

### Button:SetDisabledTexture

Sets the texture to be used when the button is disabled

**Signature:**

```lua
Button:SetDisabledTexture(texture)
```

---

### Button:SetFontString

Sets the `FontString` object used for the button's label text

**Signature:**

```lua
Button:SetFontString(fontstring)
```

**Arguments:**

- `fontstring` - Reference to a `FontString` object to be used for the button's label text (`fontstring`)

---

### Button:SetFormattedText

Sets the button's label, using a format string and arguments. This prevents a new text string from being allocated, saving memory if the text is frequently changed to a new string

**Signature:**

```lua
Button:SetFormattedText("fmt", ...)
```

**Arguments:**

- `fmt` - A format string to be passed to string.format() (`string`)
- `...` - A list of arguments to the string.format() function corresponding to the specified format string (`values`)

---

### Button:SetFrameLevel

Sets the frame level of the frame

**Signature:**

```lua
Button:SetFrameLevel()
```

---

### Button:SetFrameStrata

Sets the frame's frameStrata

**Signature:**

```lua
Button:SetFrameStrata("strata")
```

---

### Button:SetHeight

Sets the height of this region to the given value

**Signature:**

```lua
Button:SetHeight()
```

---

### Button:SetHighlightFontObject

Sets the font object used when the button is highlighted

**Signature:**

```lua
Button:SetHighlightFontObject(font)
```

**Arguments:**

- `font` - Reference to a `Font` object to be used when the button is highlighted (`font`)

---

### Button:SetHighlightTexture

Sets the texture used when the button is highlighted. Unlike the other button textures for which only one is visible at a time, the button's highlight texture is drawn on top of its existing (normal or pushed) texture; thus, this method also allows specification of the texture's blend mode.

**Signature:**

```lua
Button:SetHighlightTexture(texture [, "mode"]) or Button:SetHighlightTexture("filename" [, "mode"])
```

**Arguments:**

- `texture` - Reference to an existing `Texture` object (`texture`)
- `filename` - Path to a texture image file (`string`)
- `mode` - Blend mode for the texture; defaults to `ADD` if omitted (`string`)
  - `ADD` - Adds texture color values to the underlying color values, using the alpha channel; light areas in the texture lighten the background while dark areas are more transparent
  - `ALPHAKEY` - One-bit transparency; pixels with alpha values greater than ~0.8 are treated as fully opaque and all other pixels are treated as fully transparent
  - `BLEND` - Normal color blending, using any alpha channel in the texture image
  - `DISABLE` - Ignores any alpha channel, displaying the texture as fully opaque
  - `MOD` - Ignores any alpha channel in the texture and multiplies texture color values by background color values; dark areas in the texture darken the background while light areas are more transparent

---

### Button:SetHitRectInsets

Sets the frame's HitRectInsets, which define where the mouse can interact with the frame

**Signature:**

```lua
Button:SetHitRectInsets()
```

---

### Button:SetID

Sets the numeric identifier for the frame

**Signature:**

```lua
Button:SetID()
```

---

### Button:SetJumpNavigateEnabled

This function is not yet documented

**Signature:**

```lua
Button:SetJumpNavigateEnabled()
```

---

### Button:SetJumpNavigateStart

This function is not yet documented

**Signature:**

```lua
Button:SetJumpNavigateStart()
```

---

### Button:SetMaxResize

Sets the maximum resize limits for the frame

**Signature:**

```lua
Button:SetMaxResize()
```

---

### Button:SetMinResize

Sets the minimum resize limits for the frame

**Signature:**

```lua
Button:SetMinResize()
```

---

### Button:SetMovable

Sets whether or not the frame is movable

**Signature:**

```lua
Button:SetMovable()
```

---

### Button:SetNormalFontObject

Sets the font object used for the button's normal state

**Signature:**

```lua
Button:SetNormalFontObject(font)
```

**Arguments:**

- `font` - Reference to a `Font` object to be used in the button's normal state (`font`)

---

### Button:SetNormalTexture

Sets the texture used for the button's normal state

**Signature:**

```lua
Button:SetNormalTexture(texture) or Button:SetNormalTexture("filename")
```

**Arguments:**

- `texture` - Reference to an existing `Texture` object (`texture`)
- `filename` - Path to a texture image file (`string`)

---

### Button:SetParent

Sets the parent of this region to the given region

**Signature:**

```lua
Button:SetParent()
```

---

### Button:SetPoint

Sets a given anchor point on this region

**Signature:**

```lua
Button:SetPoint()
```

---

### Button:SetPushedTextOffset

Sets the offset for moving the button's label text when pushed. Moving the button's text while it is being clicked can provide an illusion of 3D depth for the button -- in the default UI's standard button templates, this offset matches the apparent movement seen in the difference between the buttons' normal and pushed textures.

**Signature:**

```lua
Button:SetPushedTextOffset(x, y)
```

**Arguments:**

- `x` - Horizontal offset for the text (in pixels; values increasing to the right) (`number`)
- `y` - Vertical offset for the text (in pixels; values increasing upward) (`number`)

---

### Button:SetPushedTexture

Sets the texture used when the button is pushed

**Signature:**

```lua
Button:SetPushedTexture(texture) or Button:SetPushedTexture("filename")
```

**Arguments:**

- `texture` - Reference to an existing `Texture` object (`texture`)
- `filename` - Path to a texture image file (`string`)

---

### Button:SetResizable

Sets whether or not the frame is resizable

**Signature:**

```lua
Button:SetResizable()
```

---

### Button:SetScale

Sets the scale of the frame

**Signature:**

```lua
Button:SetScale()
```

---

### Button:SetScript

Sets the handler function for a given widget script

**Signature:**

```lua
Button:SetScript("scriptType", handler)
```

---

### Button:SetText

Sets the text displayed as the button's label

**Signature:**

```lua
Button:SetText("text")
```

**Arguments:**

- `text` - Text to be displayed as the button's label (`string`)

---

### Button:SetToplevel

Sets whether or not the frame should raise itself to the top frame level when clicked

**Signature:**

```lua
Button:SetToplevel()
```

---

### Button:SetUserPlaced

Flags the frame as user placed, or not

**Signature:**

```lua
Button:SetUserPlaced()
```

---

### Button:SetWidth

Sets the width of this region to the given value

**Signature:**

```lua
Button:SetWidth()
```

---

### Button:Show

Shows the region

**Signature:**

```lua
Button:Show()
```

---

### Button:StartMoving

Start moving the frame

**Signature:**

```lua
Button:StartMoving()
```

---

### Button:StartSizing

Start resizing the frame

**Signature:**

```lua
Button:StartSizing()
```

---

### Button:StopAnimating

This function is not yet documented

**Signature:**

```lua
Button:StopAnimating()
```

---

### Button:StopMovingOrSizing

Stops the frame from being moved or resized, and saves the position in layout-cache.txt

**Signature:**

```lua
Button:StopMovingOrSizing()
```

---

### Button:UnlockHighlight

Unlocks the button's highlight state. Can be used after a call to [`:LockHighlight()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widget/Button/LockHighlight) to restore the button's normal mouseover behavior.

**Signature:**

```lua
Button:UnlockHighlight()
```

---

### Button:UnregisterAllEvents

Unregisters all events for the frame

**Signature:**

```lua
Button:UnregisterAllEvents()
```

---

### Button:UnregisterEvent

Unregistered the frame for the given event

**Signature:**

```lua
Button:UnregisterEvent()
```

---

## Script Handlers

---

### OnAttributeChanged

Sets an arbitrary, named, taintless value on a frame.

**Signature:**

```lua
OnAttributeChanged(self, "name", value)
```

---

### OnChar

Fires when a text character is received by a frame.

**Signature:**

```lua
OnChar(self, "text")
```

---

### OnClick

OnClick fires in response to a click on the button.

**Signature:**

```lua
OnClick(self, "button", down)
```

---

### OnDoubleClick

Fires when the user double-clicks the button.

**Signature:**

```lua
OnDoubleClick(self, "button")
```

---

### OnDragStart

Fires when the user starts moving the mouse after clicking down on the frame.

**Signature:**

```lua
OnDragStart(self, "button")
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
OnEvent(self, "event", ...)
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
OnKeyDown(self, "key")
```

---

### OnKeyUp

Fires when the frame receives an "up" key press.

**Signature:**

```lua
OnKeyUp(self, "key")
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
OnMouseDown(self, "button")
```

---

### OnMouseUp

Fires when the mouse button is released after clicking on a frame.

**Signature:**

```lua
OnMouseUp(self, "button")
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

### PostClick

PostClick fires immediately after OnClick with the same parameters.

**Signature:**

```lua
PostClick(self, "button", down)
```

---

### PreClick

PostClick fires immediately before OnClick with the same parameters.

**Signature:**

```lua
PreClick(self, "button", down)
```

---

← [Widgets](../Widgets.md)
