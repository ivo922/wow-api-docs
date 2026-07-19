# Blizzard internal functions

← [WoW API Docs](../index.md)

**43** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#internal)

---

## AppendToFile `internal`

This is a Blizzard internal function

---

## CreateMiniWorldMapArrowFrame `internal`

This is a Blizzard internal function

---

## CreateWorldMapArrowFrame `internal`

This is a Blizzard internal function

---

## DeleteFile `internal`

This is a Blizzard internal function

---

## DetectWowMouse

Detects the presence of a "WoW" compatible multi-button mouse. This function is used by the default user interface to enable or disable the configuration option for a many buttoned WoW mouse. If the mouse is not found, the [`WOW_MOUSE_NOT_FOUND`](../events/WOW_MOUSE_NOT_FOUND.md) event will fire.

**Signature:**

```lua
DetectWowMouse()
```

---

## GMRequestPlayerInfo `internal`

This is a Blizzard internal function

---

## GetDebugStats `internal`

This is a Blizzard internal function

---

## GetDebugZoneMap `internal`

This is a Blizzard internal function

---

## GetGMStatus `internal`

This is a Blizzard internal function

---

## GetMapDebugObjectInfo `internal`

This is a Blizzard internal function

---

## GetNumMapDebugObjects `internal`

**Signature:**

```lua
GetNumMapDebugObjects()
```

---

## GetTexLodBias `internal`

This is a Blizzard internal function

---

## HasDebugZoneMap `internal`

This is a Blizzard internal function

---

## IsDebugBuild `internal`

**Signature:**

```lua
IsDebugBuild()
```

---

## PlayDance `internal`

This is a Blizzard internal function

---

## PositionMiniWorldMapArrowFrame `internal`

This is a Blizzard internal function

---

## PositionWorldMapArrowFrame `internal`

This is a Blizzard internal function

---

## ReadFile `internal`

This is a Blizzard internal function

---

## ResetPerformanceValues `internal`

This is a Blizzard internal function

---

## SetChannelWatch `internal`

This is a Blizzard internal function

---

## SetConsoleKey `internal`

This is a Blizzard internal function

---

## SetLayoutMode `internal`

This is a Blizzard internal function

---

## ShowWorldMapArrowFrame `internal`

This is a Blizzard internal function

---

## TargetDirectionEnemy `internal` `protected`

This is a Blizzard internal function

---

## TargetDirectionFinished `internal` `protected`

This is a Blizzard internal function

---

## TargetDirectionFriend `internal` `protected`

This is a Blizzard internal function

---

## TeleportToDebugObject `internal`

This is a Blizzard internal function

---

## ToggleCollision `internal`

This is a Blizzard internal function

---

## ToggleCollisionDisplay `internal`

This is a Blizzard internal function

---

## TogglePerformanceDisplay `internal`

This is a Blizzard internal function

---

## TogglePerformancePause `internal`

This is a Blizzard internal function

---

## TogglePerformanceValues `internal`

This is a Blizzard internal function

---

## TogglePlayerBounds `internal`

This is a Blizzard internal function

---

## TogglePortals `internal`

This is a Blizzard internal function

---

## ToggleTris `internal`

This is a Blizzard internal function

---

## UpdateWorldMapArrowFrames `internal`

This is a Blizzard internal function

---

## debugbreak `internal`

This is a Blizzard internal function

---

## debugdump `internal`

This is a Blizzard internal function

---

## debuginfo `internal`

This is a Blizzard internal function

---

## debugload `internal`

This is a Blizzard internal function

---

## debugprint `internal`

This is a Blizzard internal function

---

## debugtimestamp `internal`

This is a Blizzard internal function

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

← [WoW API Docs](../index.md)
