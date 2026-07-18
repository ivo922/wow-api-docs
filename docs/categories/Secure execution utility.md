# Secure execution utility functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#security)

---

## InCombatLockdown

Returns whether the user interface is protected due to combat. Non-Blizzard code is allowed to perform certain UI actions (such as changing secure template attributes or moving/showing/hiding secure frames) only if the player is not in combat; this function can be used to determine whether such actions are currently available.

**Signature:**

```lua
inLockdown = InCombatLockdown()
```

**Returns:**

- `inLockdown` - 1 if the user interface is protected due to combat; otherwise nil (`1nil`)

---

## forceinsecure

Causes the current execution path to continue outside the secure environment. Meaningless when called from outside of the secure environment.

**Signature:**

```lua
forceinsecure()
```

---

## hooksecurefunc

Add a function to be called after execution of a secure function. Allows one to "post-hook" a secure function without tainting the original.

The original function will still be called, but the function supplied will be called after the original, with the same arguments. Return values from the supplied function are discarded. Note that there is no API to remove a hook from a function: any hooks applied will remain in place until the UI is reloaded.

Only allows hooking of functions named by a global variable; to hook a script handler on a Frame object, see [`Frame:HookScript()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/widgets/Frame/HookScript).

**Signature:**

```lua
hooksecurefunc([table,] "function", hookfunc)
```

**Arguments:**

- `table` - A table object that contains the function to be hooked (`table`)
- `function` - The name of the function to be hooked (`string`)
- `hookfunc` - The function to be called each time the original function is called (`function`)

---

## issecure

Returns whether the current execution path is secure. Meaningless when called from outside of the secure environment: always returns `nil` in such situations.

**Signature:**

```lua
secure = issecure()
```

**Returns:**

- `secure` - 1 if the current execution path is secure; otherwise nil (`1nil`)

---

## issecurevariable

Returns whether a variable is secure (and if not, which addon tainted it)

**Signature:**

```lua
issecure, taint = issecurevariable([table,] "variable")
```

**Arguments:**

- `table` - A table to be used when checking table elements (`table`)
- `variable` - The name of a variable to check. In order to check the status of a table element, you should specify the table, and then the key of the element (`string`)

**Returns:**

- `issecure` - 1 if the variable is secure; otherwise nil (`1nil`)
- `taint` - Name of the addon that tainted the variable, or nil if the variable is secure (`string`)

---

## newproxy `luaapi`

Creates a zero-length userdata with an optional metatable.. newproxy is a experimental, undocumented and unsupported function in the Lua base library. It can be used to create a zero-length userdata, with a optional proxy.

This function allows you to bypass the table type restriction on setmetatable, and thus create just a metatable. One of the main benefits from doing this is that you don't have to take the full overhead of creating a dummy table, and it's the only object that honors the metamethod __len.

**Signature:**

```lua
userdata = newproxy(boolean) or newproxy(userdata)
```

**Arguments:**

- `boolean` - Controls if the returned userdata should have a metatable or not. (`boolean`)
- `userdata` - Needs to be a proxy. The metatable will be shared between the proxies. (`userdata`)

**Returns:**

- `userdata` - A zero-length user-data object. (`userdata`)

---

## securecall

Calls a function without tainting the execution path. Meaningless when called from outside of the secure environment.

Used in Blizzard code to call functions which may be tainted or operate on potentially tainted variables. For example, consider the function `CloseSpecialWindows`, which iterates through the table `UISpecialFrames` and hides any frames named therein. Addon authors may put the names of their frames in that table to make them automatically close when the user presses the ESC key, but this taints `UISpecialFrames`. Were the default UI to then call `CloseSpecialWindows` normally, every frame in `UISpecialFrames` would become tainted, which could later lead to errors when handlers on those frames call protected functions.

Instead, the default UI uses `securecall(CloseSpecialWindows)`: within `CloseSpecialWindows` the execution path may become tainted, but afterward the environment remains secure.

**Signature:**

```lua
... = securecall(function, ...)
```

**Arguments:**

- `function` - Function to be called (`function`)
- `...` - Arguments to the function (`list`)

**Returns:**

- `...` - Values returned after calling the function (`list`)

---

← [WoW API Docs](../index.md)
