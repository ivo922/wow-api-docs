# AnimationGroup

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/AnimationGroup)

An AnimationGroup is how various animations are actually applied to a region; this is how different behaviors can be run in sequence or in parallel with each other, automatically. When you pause an AnimationGroup, it tracks which of its child animations were playing and how far advanced they were, and resumes them from that point.

An Animation in a group has an order from 1 to 100, which determines when it plays; once all animations with order 1 have completed, including any delays, the AnimationGroup starts all animations with order 2.

An AnimationGroup can also be set to loop, either repeating from the beginning or playing backward back to the beginning. An AnimationGroup has an OnLoop handler that allows you to call your own code back whenever a loop completes. The `:Finish()` method stops the animation after the current loop has completed, rather than immediately.

---

## Methods

---

### AnimationGroup:CreateAnimation

Creates an Animation as a child of this group

**Signature:**

```lua
animation = AnimationGroup:CreateAnimation("animationType" [, "name" [, "inheritsFrom"]])
```

**Arguments:**

- `animationType` - Type of `Animation` object to be created (see [widgets hierarchy](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets_hierarchy) for available subtypes) (`string`)
- `name` - Global name to use for the new animation (`string`)
- `inheritsFrom` - A template from which to inherit (`string`)

**Returns:**

- `animation` - The newly created animation (`animation`)

---

### AnimationGroup:Finish

Causes animations within the group to complete and stop. If the group is playing, animations will continue until the current loop cycle is complete before stopping. For example, in a group which manages a repeating fade-out-fade-in animation, the associated object will continue to fade completely back in, instead of the animation stopping and the object instantly switching from partial opacity to full opacity instantly. Does nothing if this group is not playing.

To instantly stop an animation, see [`AnimationGroup:Stop()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/AnimationGroup/Stop).

**Signature:**

```lua
AnimationGroup:Finish()
```

---

### AnimationGroup:GetAnimations

Returns a list of animations belonging to the group

**Signature:**

```lua
... = AnimationGroup:GetAnimations()
```

**Returns:**

- `...` - A list of `Animation` objects belonging to the animation group (`list`)

---

### AnimationGroup:GetDuration

Returns the duration of a single loop cycle for the group, as determined by its child animations. Total duration is based on the durations, delays, and order of child animations; see example for details.

**Signature:**

```lua
duration = AnimationGroup:GetDuration()
```

**Returns:**

- `duration` - Total duration of all child animations (in seconds) (`number`)

---

### AnimationGroup:GetInitialOffset

Returns the starting static translation for the animated region

**Signature:**

```lua
x, y = AnimationGroup:GetInitialOffset()
```

**Returns:**

- `x` - Horizontal distance to offset the animated region (in pixels) (`number`)
- `y` - Vertical distance to offset the animated region (in pixels) (`number`)

---

### AnimationGroup:GetLoopState

Returns the current loop state of the group

**Signature:**

```lua
loopState = AnimationGroup:GetLoopState()
```

**Returns:**

- `loopState` - Loop state of the animation group (`string`)
  - `FORWARD` - In transition from the start state to the final state
  - `NONE` - Not looping
  - `REVERSE` - In transition from the final state back to the start state

---

### AnimationGroup:GetLooping

Returns the looping behavior of the group

**Signature:**

```lua
loopType = AnimationGroup:GetLooping()
```

**Returns:**

- `loopType` - Looping type for the animation group (`string`)
  - `BOUNCE` - Repeatedly animates forward from the initial state to the final state then backwards to the initial state
  - `NONE` - No looping; animates from the initial state to the final state once and stops
  - `REPEAT` - Repeatedly animates forward from the initial state to the final state (instantly resetting from the final state to the initial state between repetitions)

---

### AnimationGroup:GetMaxOrder

Returns the highest order amongst the animations in the group

**Signature:**

```lua
maxOrder = AnimationGroup:GetMaxOrder()
```

**Returns:**

- `maxOrder` - Highest ordering value (see [`Animation:GetOrder()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/Animation/GetOrder)) of the animations in the group (`number`)

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

### AnimationGroup:GetProgress

Returns the current state of the animation group's progress

**Signature:**

```lua
progress = AnimationGroup:GetProgress()
```

**Returns:**

- `progress` - Value indicating the current state of the group animation: between 0.0 (initial state, child animations not yet started) and 1.0 (final state, all child animations complete) (`number`)

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

### ScriptObject:HasScript

Returns whether the widget supports a script handler

**Signature:**

```lua
hasScript = AnimationGroup:HasScript("scriptType")
```

*Inherited from [ScriptObject](ScriptObject.md)*

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

### AnimationGroup:IsDone

Returns whether the group has finished playing. Only valid in the [`OnFinished`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnFinished) and [`OnUpdate`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/scripts/OnUpdate) handlers, and only applies if the animation group does not loop.

**Signature:**

```lua
done = AnimationGroup:IsDone()
```

**Returns:**

- `done` - True if the group has finished playing; false otherwise (`boolean`)

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

### AnimationGroup:IsPaused

Returns whether the group is paused

**Signature:**

```lua
paused = AnimationGroup:IsPaused()
```

**Returns:**

- `paused` - True if animation of the group is currently paused; false otherwise (`boolean`)

---

### AnimationGroup:IsPendingFinish

Returns whether or not the animation group is pending finish

**Signature:**

```lua
isPending = AnimationGroup:IsPendingFinish()
```

**Returns:**

- `isPending` - Whether or not the animation group is currently pending a finish command. Since the `Finish()` method does not immediately stop the animation group, this method can be used to test if `Finish()` has been called and the group will finish at the end of the current loop. (`boolean`)

---

### AnimationGroup:IsPlaying

Returns whether the group is playing

**Signature:**

```lua
playing = AnimationGroup:IsPlaying()
```

**Returns:**

- `playing` - True if the group is currently animating; false otherwise (`boolean`)

---

### AnimationGroup:Pause

Pauses animation of the group. Unlike with [`AnimationGroup:Stop()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/AnimationGroup/Stop), the animation is paused at its current progress state (e.g. in a fade-out-fade-in animation, the element will be at partial opacity) instead of reset to the initial state; animation can be resumed with [`AnimationGroup:Play()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/AnimationGroup/Play).

**Signature:**

```lua
AnimationGroup:Pause()
```

---

### AnimationGroup:Play

Starts animating the group. If the group has been paused, animation resumes from the paused state; otherwise animation begins at the initial state.

**Signature:**

```lua
AnimationGroup:Play()
```

---

### AnimationGroup:SetInitialOffset

Sets a static translation for the animated region. This translation is only used while the animation is playing.

For example, applying an initial offset of `0,-50` to an animation group which fades the PlayerPortrait in and out would cause the portrait image to jump down 50 pixels from its normal position when the animation begins playing, and return to its initial position when the animation is finished or stopped.

**Signature:**

```lua
AnimationGroup:SetInitialOffset(x, y)
```

**Arguments:**

- `x` - Horizontal distance to offset the animated region (in pixels) (`number`)
- `y` - Vertical distance to offset the animated region (in pixels) (`number`)

---

### AnimationGroup:SetLooping

Sets the looping behavior of the group

**Signature:**

```lua
AnimationGroup:SetLooping("loopType")
```

**Arguments:**

- `loopType` - Looping type for the animation group (`string`)
  - `BOUNCE` - Repeatedly animates forward from the initial state to the final state then backwards to the initial state
  - `NONE` - No looping; animates from the initial state to the final state once and stops
  - `REPEAT` - Repeatedly animates forward from the initial state to the final state (instantly resetting from the final state to the initial state between repetitions)

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

### AnimationGroup:Stop

Stops animation of the group. Unlike with [`AnimationGroup:Pause()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/AnimationGroup/Pause), the animation is reset to the initial state (e.g. in a fade-out-fade-in animation, the element will be instantly returned to full opacity) instead of paused at its current progress state.

**Signature:**

```lua
AnimationGroup:Stop()
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

### OnLoop

Run when the animation group's loop state changes

**Signature:**

```lua
OnLoop(self, "loopState")
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
