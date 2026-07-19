# Animation

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/Animation)

Animations are used to change presentations or other characteristics of a frame or other region over time. The Animation object will take over the work of calling code over time, or when it is done, and tracks how close the animation is to completion.

The Animation type doesn't create any visual effects by itself, but it does provide an OnUpdate handler that you can use to support specialized time-sensitive behaviors that aren't provided by the transformations descended from Animations. In addition to tracking the passage of time through an elapsed argument, you can query the animation's progress as a 0-1 fraction to determine how you should set your behavior.

You can also change how the elapsed time corresponds to the progress by changing the smoothing, which creates acceleration or deceleration, or by adding a delay to the beginning or end of the animation.

You can also use an Animation as a timer, by setting the Animation's OnFinished script to trigger a callback and setting the duration to the desired time.

---

## Methods

---

### Animation:GetDuration

Returns the time for the animation to progress from start to finish

**Signature:**

```lua
duration = Animation:GetDuration()
```

**Returns:**

- `duration` - Time for the animation to progress from start to finish (in seconds) (`number`)

---

### Animation:GetElapsed

Returns the amount of time since the animation began playing. This amount includes start and end delays.

**Signature:**

```lua
elapsed = Animation:GetElapsed()
```

**Returns:**

- `elapsed` - Amount of time since the animation began playing (in seconds) (`number`)

---

### Animation:GetEndDelay

Returns the amount of time the animation delays after finishing. A later animation in an animation group will not begin until after the end delay period of the preceding animation has elapsed.

**Signature:**

```lua
delay = Animation:GetEndDelay()
```

**Returns:**

- `delay` - Time the animation delays after finishing (in seconds) (`number`)

---

### Animation:GetMaxFramerate

Returns the maximum number of times per second that the animation will update its progress

**Signature:**

```lua
framerate = Animation:GetMaxFramerate()
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

### Animation:GetOrder

Returns the order of the animation within its parent group. When the parent `AnimationGroup` plays, Animations with a lower order number are played before those with a higher number. Animations with the same order number are played at the same time.

**Signature:**

```lua
order = Animation:GetOrder()
```

**Returns:**

- `order` - Position at which the animation will play relative to others in its group (between 0 and 100) (`number`)

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

### Animation:GetProgress

Returns the progress of an animation, ignoring smoothing effects. The value returned by this method increases linearly with time while the animation is playing, while the value returned by [`Animation:GetSmoothProgress()`](Animation.md#animationgetsmoothprogress) may change at a different rate if the animation's smoothing type is set to a value other than `NONE`.

**Signature:**

```lua
progress = Animation:GetProgress()
```

**Returns:**

- `progress` - Progress of the animation: between 0.0 (at start) and 1.0 (at end) (`number`)

---

### Animation:GetProgressWithDelay

Returns the progress of the animation and associated delays

**Signature:**

```lua
progress = Animation:GetProgressWithDelay()
```

**Returns:**

- `progress` - Progress of the animation and its delays: between 0.0 (at start of start delay) and 1.0 (at end of end delay) (`number`)

---

### Animation:GetRegionParent

Returns the `Region` object on which the animation operates

**Signature:**

```lua
region = Animation:GetRegionParent()
```

**Returns:**

- `region` - Reference to the `Region` object on which the animation operates (i.e. the parent of the animation's parent `AnimationGroup`). (`region`, [Region](Region.md))

---

### ScriptObject:GetScript

Returns the widget's handler function for a script

**Signature:**

```lua
handler = ScriptObject:GetScript("scriptType")
```

**Arguments:**

- `scriptType` - A script type; see [scripts reference](#script-handlers) for details (`string`)

**Returns:**

- `handler` - The object's handler function for the script type (`function`)

*Inherited from [ScriptObject](ScriptObject.md)*

---

### Animation:GetSmoothProgress

Returns the progress of the animation (ignoring start and end delay). When using a generic `Animation` object to animate effects not handled by the built-in `Animation` subtypes, this method should be used for updating effects in the animation's `OnUpdate` handler, as it properly accounts for smoothing and delays managed by the `Animation` object.

**Signature:**

```lua
progress = Animation:GetSmoothProgress()
```

**Returns:**

- `progress` - Progress of the animation: between 0.0 (at start) and 1.0 (at end) (`number`)

---

### Animation:GetSmoothing

Returns the smoothing type for the animation. This setting affects the rate of change in the animation's progress value as it plays.

**Signature:**

```lua
smoothType = Animation:GetSmoothing()
```

**Returns:**

- `smoothType` - Type of smoothing for the animation (`string`)
  - `IN` - Initially progressing slowly and accelerating towards the end
  - `IN_OUT` - Initially progressing slowly and accelerating towards the middle, then slowing down towards the end
  - `NONE` - Progresses at a constant rate from beginning to end
  - `OUT` - Initially progressing quickly and slowing towards the end

---

### Animation:GetStartDelay

Returns the amount of time the animation delays before its progress begins

**Signature:**

```lua
delay = Animation:GetStartDelay()
```

**Returns:**

- `delay` - Amount of time the animation delays before its progress begins (in seconds) (`number`)

---

### ScriptObject:HasScript

Returns whether the widget supports a script handler

**Signature:**

```lua
hasScript = ScriptObject:HasScript("scriptType")
```

**Arguments:**

- `scriptType` - A script type; see [scripts reference](#script-handlers) for details (`string`)

**Returns:**

- `hasScript` - `1` if the widget can handle the script, otherwise `nil` (`1nil`)

*Inherited from [ScriptObject](ScriptObject.md)*

---

### ScriptObject:HookScript

Securely hooks a script handler. Equivalent to [`hooksecurefunc()`](../categories/Secure execution utility.md#hooksecurefunc) for script handlers; allows one to "post-hook" a secure handler without tainting the original.

The original handler will still be called, but the handler supplied will also be called after the original, with the same arguments. Return values from the supplied handler are discarded. Note that there is no API to remove a hook from a handler: any hooks applied will remain in place until the UI is reloaded.

If there was no prior script handler set, then this simply sets the new function as the handler for the script type.

**Signature:**

```lua
ScriptObject:HookScript("scriptType", handler)
```

**Arguments:**

- `scriptType` - Name of the [script](#script-handlers) whose handler should be hooked (`string`)
- `handler` - A function to be called whenever the script handler is run (`function`)

*Inherited from [ScriptObject](ScriptObject.md)*

---

### Animation:IsDelaying

Returns whether the animation is currently in the middle of a start or end delay

**Signature:**

```lua
delaying = Animation:IsDelaying()
```

**Returns:**

- `delaying` - True if the animation is currently in its start or end delay period; false if the animation is currently between its start and end periods (or has none) or is not playing (`boolean`)

---

### Animation:IsDone

Returns whether the animation has finished playing

**Signature:**

```lua
done = Animation:IsDone()
```

**Returns:**

- `done` - True if the animation is finished playing; otherwise false (`boolean`)

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

### Animation:IsPaused

Returns whether the animation is currently paused

**Signature:**

```lua
paused = Animation:IsPaused()
```

**Returns:**

- `paused` - True if the animation is currently paused; false otherwise (`boolean`)

---

### Animation:IsPlaying

Returns whether the animation is currently playing

**Signature:**

```lua
playing = Animation:IsPlaying()
```

**Returns:**

- `playing` - True if the animation is currently playing; otherwise false (`boolean`)

---

### Animation:IsStopped

Returns whether the animation is currently stopped

**Signature:**

```lua
stopped = Animation:IsStopped()
```

**Returns:**

- `stopped` - True if the animation is currently stopped; otherwise false (`boolean`)

---

### Animation:Pause

Pauses the animation. Unlike with [`Animation:Stop()`](Animation.md#animationstop), the animation is paused at its current progress state (e.g. in a fade-out-fade-in animation, the element will be at partial opacity) instead of reset to the initial state; animation can be resumed with [`Animation:Play()`](Animation.md#animationplay).

**Signature:**

```lua
Animation:Pause()
```

---

### Animation:Play

Plays the animation. If the animation has been paused, it resumes from the paused state; otherwise the animation begins at its initial state.

**Signature:**

```lua
Animation:Play()
```

---

### Animation:SetDuration

Sets the time for the animation to progress from start to finish

**Signature:**

```lua
Animation:SetDuration(duration)
```

**Arguments:**

- `duration` - Time for the animation to progress from start to finish (in seconds) (`number`)

---

### Animation:SetEndDelay

Sets the amount of time for the animation to delay after finishing. A later animation in an animation group will not begin until after the end delay period of the preceding animation has elapsed.

**Signature:**

```lua
Animation:SetEndDelay(delay)
```

**Arguments:**

- `delay` - Time for the animation to delay after finishing (in seconds) (`number`)

---

### Animation:SetMaxFramerate

Sets the maximum number of times per second for the animation to update its progress

**Signature:**

```lua
Animation:SetMaxFramerate(framerate)
```

---

### Animation:SetOrder

Sets the order for the animation to play within its parent group. When the parent `AnimationGroup` plays, Animations with a lower order number are played before those with a higher number. Animations with the same order number are played at the same time.

**Signature:**

```lua
Animation:SetOrder(order)
```

**Arguments:**

- `order` - Position at which the animation should play relative to others in its group (between 0 and 100) (`number`)

---

### Animation:SetParent

Sets the parent for the animation. If the animation was not already a child of the parent, the parent will insert the animation into the proper order amongst its children.

**Signature:**

```lua
Animation:SetParent(animGroup) or Animation:SetParent("animGroupName")
```

**Arguments:**

- `animGroup` - The animation group to set as the parent of this animation (`animgroup`, [AnimationGroup](AnimationGroup.md))
- `animGroupName` - The name of the animation group to set as the parent of this animation (`string`)

---

### ScriptObject:SetScript

Sets the widget's handler function for a script

**Signature:**

```lua
ScriptObject:SetScript("scriptType", handler)
```

**Arguments:**

- `scriptType` - A script type; see [scripts](#script-handlers) for details (`string`)
- `handler` - A function to become the widget's handler for the script type (`function`)

*Inherited from [ScriptObject](ScriptObject.md)*

---

### Animation:SetSmoothProgress

This function is not yet documented

**Signature:**

```lua
Animation:SetSmoothProgress()
```

---

### Animation:SetSmoothing

Sets the smoothing type for the animation. This setting affects the rate of change in the animation's progress value as it plays.

**Signature:**

```lua
Animation:SetSmoothing("smoothType")
```

**Arguments:**

- `smoothType` - Type of smoothing for the animation (`string`)
  - `IN` - Initially progressing slowly and accelerating towards the end
  - `IN_OUT` - Initially progressing slowly and accelerating towards the middle, then slowing down towards the end
  - `NONE` - Progresses at a constant rate from beginning to end
  - `OUT` - Initially progressing quickly and slowing towards the end

---

### Animation:SetStartDelay

Sets the amount of time for the animation to delay before its progress begins. Start delays can be useful with concurrent animations in a group: see example for details.

**Signature:**

```lua
Animation:SetStartDelay(delay)
```

**Arguments:**

- `delay` - Amount of time for the animation to delay before its progress begins (in seconds) (`number`)

---

### Animation:Stop

Stops the animation. Also resets the animation to its initial state.

**Signature:**

```lua
Animation:Stop()
```

---

## Script Handlers

---

### OnEvent

Run whenever an [[docs/events|event]] fires for which the frame is registered

**Signature:**

```lua
OnEvent(self, "event", ...)
```

---

### OnFinished

Run when the animation (or animation group) finishes animating

**Signature:**

```lua
OnFinished(self, requested)
```

---

### OnLoad

Run when the frame is created

**Signature:**

```lua
OnLoad(self)
```

---

### OnPause

Run when the animation (or animation group) is paused

**Signature:**

```lua
OnPause(self)
```

---

### OnPlay

Run when the animation (or animation group) begins to play

**Signature:**

```lua
OnPlay(self)
```

---

### OnStop

Run when the animation (or animation group) is stopped

**Signature:**

```lua
OnStop(self, requested)
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
