# Camera functions

← [WoW API Docs](../index.md)

**25** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#camera)

---

## CameraOrSelectOrMoveStart `protected`

Begins camera movement or selection (equivalent to left-clicking in the 3-D world). After calling this function (i.e. while the left mouse button is held), cursor movement rotates the camera. Final results vary by context and are determined when calling [`CameraOrSelectOrMoveStop()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/CameraOrSelectOrMoveStop) (i.e. releasing the left mouse button).

Used by the `CAMERAORSELECTORMOVE` binding (not customizable in the default UI), which is bound to the left mouse button by default.

**Signature:**

```lua
CameraOrSelectOrMoveStart()
```

---

## CameraOrSelectOrMoveStop `protected`

Ends action initiated by [`CameraOrSelectOrMoveStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/CameraOrSelectOrMoveStart). After calling this function (i.e. releasing the left mouse button), camera movement stops and normal cursor movement resumes. If the cursor has not moved significantly since calling [`CameraOrSelectOrMoveStart()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/CameraOrSelectOrMoveStart) (i.e. pressing the left mouse button) and is over a unit, that unit becomes the player's target; if the cursor has not moved significantly and is not over a unit, clears the player's target unless the "Sticky Targeting" option is enabled (i.e. the "deselectOnClick" CVar is 0).

Used by the `CAMERAORSELECTORMOVE` binding (not customizable in the default UI), which is bound to the left mouse button by default.

**Signature:**

```lua
CameraOrSelectOrMoveStop(isSticky)
```

**Arguments:**

- `isSticky` - If 1, the camera will remain static until cancelled. Otherwise, the camera will pan back to be directly behind the character (`1nil`)

---

## CameraZoomIn

Zooms the camera in by a specified distance.

The max distance of the camera is set in the Interface Options screen, and the maximum distance allowed is enforced by this setting, and the game client. Depending on the setting, this is between 15.0 and 24.0 in the current version of the client.

**Signature:**

```lua
CameraZoomIn(distance)
```

**Arguments:**

- `distance` - The distance to zoom in (`number`)

---

## CameraZoomOut

Zooms the camera out by a specified distance.

This function is used to zoom the camera out. The max distance of the camera is set in the Interface Options screen, and the maximum distance allowed is enforced by this setting, and the game client. Depending on the setting, this is between 15.0 and 24.0 in the current version of the client.

**Signature:**

```lua
CameraZoomOut(distance)
```

**Arguments:**

- `distance` - The distance to zoom out (`number`)

---

## FlipCameraYaw

Rotates the camera around the player

**Signature:**

```lua
FlipCameraYaw(degrees)
```

**Arguments:**

- `degrees` - The number of degrees to rotate; positive for counter-clockwise, negative for clockwise. (`number`)

**Examples:**

```lua
-- Dramatically Rotate the camera 360 degrees around the player
if not YawFrame then CreateFrame("Frame", "YawFrame") end
local degree = 0
local function OnUpdate(self, elapsed)
  degree = degree + 1
  FlipCameraYaw(1)
  if degree >= 360 then
    self:Hide()
  end
end
YawFrame:SetScript("OnUpdate", OnUpdate)
YawFrame:Show()
```

---

## IsMouselooking

Returns whether mouselook mode is active

**Signature:**

```lua
isLooking = IsMouselooking()
```

**Returns:**

- `isLooking` - True if mouselook mode is active; otherwise false (`boolean`)

---

## MouselookStart

Enables mouselook mode, in which cursor movement rotates the camera

**Signature:**

```lua
MouselookStart()
```

---

## MouselookStop

Disables mouselook mode

**Signature:**

```lua
MouselookStop()
```

---

## MoveViewDownStart

Begins orbiting the camera downward (to look upward)

**Signature:**

```lua
MoveViewDownStart()
```

---

## MoveViewDownStop

Ends camera movement initiated by [`MoveViewDownStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveViewDownStart)

**Signature:**

```lua
MoveViewDownStop()
```

---

## MoveViewInStart

Begins zooming the camera inward (towards/through the player character)

**Signature:**

```lua
MoveViewInStart()
```

---

## MoveViewInStop

Ends camera movement initiated by [`MoveViewInStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveViewInStart)

**Signature:**

```lua
MoveViewInStop()
```

---

## MoveViewLeftStart

Begins orbiting the camera around the player character to the left. "Left" here is relative to the player's facing; i.e. the camera orbits clockwise if looking down. Moving the camera to the left causes it to look towards the character's right.

**Signature:**

```lua
MoveViewLeftStart()
```

---

## MoveViewLeftStop

Ends camera movement initiated by [`MoveViewLeftStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveViewLeftStart)

**Signature:**

```lua
MoveViewLeftStop()
```

---

## MoveViewOutStart

Begins zooming the camera outward (away from the player character)

**Signature:**

```lua
MoveViewOutStart()
```

---

## MoveViewOutStop

Ends camera movement initiated by [`MoveViewOutStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveViewOutStart)

**Signature:**

```lua
MoveViewOutStop()
```

---

## MoveViewRightStart

Begins orbiting the camera around the player character to the right. "Right" here is relative to the player's facing; i.e. the camera orbits counter--clockwise if looking down. Moving the camera to the right causes it to look towards the character's left.

**Signature:**

```lua
MoveViewRightStart()
```

---

## MoveViewRightStop

Ends camera movement initiated by [`MoveViewRightStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveViewRightStart)

**Signature:**

```lua
MoveViewRightStop()
```

---

## MoveViewUpStart

Begins orbiting the camera upward (to look down)

**Signature:**

```lua
MoveViewUpStart()
```

---

## MoveViewUpStop

Ends camera movement initiated by [`MoveViewUpStart`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/MoveViewUpStart)

**Signature:**

```lua
MoveViewUpStop()
```

---

## NextView

Moves the camera to the next predefined setting. There are five "slots" for saved camera settings, indexed 1-5. These views can be set and accessed directly using [`SaveView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SaveView) and [`SetView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetView), and cycled through using [`NextView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NextView) and [`PrevView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PrevView).

**Signature:**

```lua
NextView()
```

---

## PrevView

Moves the camera to the previous predefined setting. There are five "slots" for saved camera settings, indexed 1-5. These views can be set and accessed directly using [`SaveView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SaveView) and [`SetView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetView), and cycled through using [`NextView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NextView) and [`PrevView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PrevView).

**Signature:**

```lua
PrevView()
```

---

## ResetView

Resets a saved camera setting to default values. There are five "slots" for saved camera settings, indexed 1-5. These views can be set and accessed directly using [`SaveView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SaveView) and [`SetView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetView), and cycled through using [`NextView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NextView) and [`PrevView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PrevView).

**Signature:**

```lua
ResetView(index)
```

**Arguments:**

- `index` - Index of a saved camera setting (between 1 and 5) (`number`)

---

## SaveView

Saves the current camera settings. There are five "slots" for saved camera settings, indexed 1-5. These views can be set and accessed directly using [`SaveView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SaveView) and [`SetView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetView), and cycled through using [`NextView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NextView) and [`PrevView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PrevView).

**Signature:**

```lua
SaveView(index)
```

**Arguments:**

- `index` - Index of a saved camera setting (between 1 and 5) (`number`)

---

## SetView

Moves the camera to a saved camera setting. There are five "slots" for saved camera settings, indexed 1-5. These views can be set and accessed directly using [`SaveView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SaveView) and [`SetView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/SetView), and cycled through using [`NextView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NextView) and [`PrevView()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/PrevView).

**Signature:**

```lua
SetView(index)
```

**Arguments:**

- `index` - Index of a saved camera setting (between 1 and 5) (`number`)

---

← [WoW API Docs](../index.md)
