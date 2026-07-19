# ControlPoint

← [Widgets](../Widgets.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726120937/http://wowprogramming.com/docs/widgets/ControlPoint)

A `ControlPoint` is a special type of UIObject that represent a point in a Path Animation. The offset for each control point is from the origin of the animated Region. See Path for more details.

---

## Methods

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

### ControlPoint:GetOffset

Returns the offset for the control point

**Signature:**

```lua
x, y = ControlPoint:GetOffset()
```

---

### ControlPoint:GetOrder

Returns the order of the control point in a path animation

**Signature:**

```lua
order = ControlPoint:GetOrder()
```

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

### ControlPoint:SetOffset

Sets the offset for the control point

**Signature:**

```lua
ControlPoint:SetOffset(x, y)
```

---

### ControlPoint:SetOrder

Sets the order of the control point in a path animation. When the parent path animation plays, the control points with a lower number are traversed before those with a higher number. Control points must have distinct order indices, and these will be assigned automatically as new points are created.

**Signature:**

```lua
ControlPoint:SetOrder(order)
```

**Arguments:**

- `order` - Position at which the control point will be traversed relative to others in the same path animation (between 0 and 100) (`number`)

---

### ControlPoint:SetParent

Sets a new path animation parent for a control point

**Signature:**

```lua
ControlPoint:SetParent([path [, order]]) or ControlPoint:SetParent(["path" [, order]])
```

**Arguments:**

- `path` - The path object to be set as parent. (`table`)
- `path` - The name of a path object to be set as parent. (`string`)
- `order` - The order index to set for the control point in the new parent animation. (`number`)

---

← [Widgets](../Widgets.md)
