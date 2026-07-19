# Debugging and Profiling functions

← [WoW API Docs](../index.md)

**20** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#debug)

---

## FrameXML_Debug

Enables or disables logging of XML loading. When logging is enabled, status and error text will be saved to the file `Logs/FrameXML.log` (path is relative to the folder containing the World of Warcraft client) as the client parses and loads XML files in the default UI and addons.

**Signature:**

```lua
FrameXML_Debug(enable)
```

**Arguments:**

- `enable` - True to enable verbose XML logging; false to disable (`boolean`)

---

## GetAddOnCPUUsage

Returns the amount of CPU time used by an addon. Only returns valid data if the `scriptProfile` CVar is set to 1; returns 0 otherwise.

The value returned is from a cache only updated when calling [`UpdateAddOnCPUUsage()`](Debugging and Profiling.md#updateaddoncpuusage). This value is the sum of [`GetFunctionCPUUsage()`](Debugging and Profiling.md#getfunctioncpuusage) for all functions created on the addon's behalf -- note that if the addon calls external functions which in turn create new functions, the new functions are considered to belong to the addon.

**Signature:**

```lua
usage = GetAddOnCPUUsage("name") or GetAddOnCPUUsage(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](Addon-related.md#getnumaddons)) (`number`)

**Returns:**

- `usage` - Amount of CPU time used by the addon (in milliseconds) since the UI was loaded or [`ResetCPUUsage()`](Debugging and Profiling.md#resetcpuusage) was last called (`number`)

---

## GetAddOnMemoryUsage

Returns the amount of memory used by an addon. The value returned is from a cache only updated when calling [`UpdateAddOnMemoryUsage()`](Debugging and Profiling.md#updateaddonmemoryusage).

**Signature:**

```lua
mem = GetAddOnMemoryUsage("name") or GetAddOnMemoryUsage(index)
```

**Arguments:**

- `name` - Name of an addon (name of the addon's folder and TOC file, not the Title found in the TOC) (`string`)
- `index` - Index of an addon in the addon list (between 1 and [`GetNumAddOns()`](Addon-related.md#getnumaddons)) (`number`)

**Returns:**

- `mem` - Memory usage of the addon (in kilobytes) (`number`)

---

## GetEventCPUUsage

Returns information about the CPU usage of an event. Only returns valid data if the `scriptProfile` CVar is set to 1; returns 0 otherwise.

**Signature:**

```lua
usage, numEvents = GetEventCPUUsage(["event"])
```

**Arguments:**

- `event` - Name of an [event](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events); if omitted, returns usage information for all events (`string`)

**Returns:**

- `usage` - Amount of CPU time used by handlers for the event (in milliseconds) since the UI was loaded or [`ResetCPUUsage()`](Debugging and Profiling.md#resetcpuusage) was last called (`number`)
- `numEvents` - Number of times the event has fired this session (`number`)

---

## GetFrameCPUUsage

Returns information about CPU usage by a frame's script handlers. Only returns valid data if the `scriptProfile` CVar is set to 1; returns 0 otherwise.

**Signature:**

```lua
usage, calls = GetFrameCPUUsage(frame, includeChildren)
```

**Arguments:**

- `frame` - A Frame object (`table`)
- `includeChildren` - True to include CPU usage by children of the frame; false to include only the frame itself (`boolean`)

**Returns:**

- `usage` - Amount of CPU time used by the frame's script handlers (in milliseconds) since the UI was loaded or [`ResetCPUUsage()`](Debugging and Profiling.md#resetcpuusage) was last called (`number`)
- `calls` - Number of function calls made from the frame's script handlers (`number`)

---

## GetFramerate

Returns the number of frames per second rendered by the client

**Signature:**

```lua
framerate = GetFramerate()
```

**Returns:**

- `framerate` - Number of frames per second rendered by the client (`number`)

---

## GetFunctionCPUUsage

Returns information about CPU usage by a function. Only returns valid data if the `scriptProfile` CVar is set to 1; returns 0 otherwise.

**Signature:**

```lua
usage, calls = GetFunctionCPUUsage(function, includeSubroutines)
```

**Arguments:**

- `function` - A function reference (`function`)
- `includeSubroutines` - True to include time spent in other functions called by the given function; false to count only time spent in the function body (`boolean`)

**Returns:**

- `usage` - Amount of CPU time used by the function (in milliseconds) since the UI was loaded or [`ResetCPUUsage()`](Debugging and Profiling.md#resetcpuusage) was last called (`number`)
- `calls` - Number times the function was called (`number`)

---

## GetNetStats

Returns information about current network connection performance

**Signature:**

```lua
bandwidthIn, bandwidthOut, latencyHome, latencyWorld = GetNetStats()
```

**Returns:**

- `bandwidthIn` - Current incomming bandwidth (download) usage, measured in KB/s (`number`)
- `bandwidthOut` - Current outgoing bandwidth (upload) usage, measured in KB/s (`number`)
- `latencyHome` - Average roundtrip latency to the home realm server (only updated every 30 seconds) (`number`)
- `latencyWorld` - Average roundtrip latency to the current world server (only updated every 30 seconds) (`number`)

---

## GetScriptCPUUsage

Returns the total CPU time used by the scripting system. Only returns valid data if the `scriptProfile` CVar is set to 1; returns 0 otherwise.

**Signature:**

```lua
usage = GetScriptCPUUsage()
```

**Returns:**

- `usage` - Amount of CPU time used by the scripting system (in milliseconds) since the UI was loaded or [`ResetCPUUsage()`](Debugging and Profiling.md#resetcpuusage) was last called (`number`)

---

## GetTaxiBenchmarkMode

Returns whether flight path benchmark mode is enabled

**Signature:**

```lua
isBenchmark = GetTaxiBenchmarkMode()
```

**Returns:**

- `isBenchmark` - 1 if taxi benchmark mode is enabled; otherwise nil (`1nil`)

---

## ResetCPUUsage

Resets CPU usage statistics. Only has effect if the `scriptProfile` CVar is set to 1.

**Signature:**

```lua
ResetCPUUsage()
```

---

## SetTaxiBenchmarkMode

Enables or disables flight path benchmark mode. When benchmark mode is enabled, the next taxi flight the player takes will behave differently: camera movement is disabled and players/creatures/objects below the flight path will not be shown (allowing for consistent test conditions). After the flight, framerate statistics will be printed in the chat window and benchmark mode will be automatically disabled.

**Signature:**

```lua
SetTaxiBenchmarkMode("arg")
```

**Arguments:**

- `arg` - nil, `"on"`, or 1 to enable benchmark mode; `"off"` or 0 to disable (`string`)

---

## UpdateAddOnCPUUsage

Updates addon CPU profiling information. Only has effect if the `scriptProfile` CVar is set to 1. See [`GetAddOnCPUUsage()`](Debugging and Profiling.md#getaddoncpuusage) for the updated data.

**Signature:**

```lua
UpdateAddOnCPUUsage()
```

---

## UpdateAddOnMemoryUsage

Updates addon memory usage information. See [`GetAddOnMemoryUsage()`](Debugging and Profiling.md#getaddonmemoryusage) for the updated data.

**Signature:**

```lua
UpdateAddOnMemoryUsage()
```

---

## debugprofilestart

Starts/resets the high resolution profiling timer. Subsequent calls to [`debugprofilestop()`](Debugging and Profiling.md#debugprofilestop) will return the current value of the timer.

Note that debugprofilestart() is more of a global reset than a "start". It is not necessary to call it, ever. In fact, it is probably a much better idea to simply do 2 calls to stop() and calculate the difference, since calling start() will interrupt timing measurements done by other addons.

**Signature:**

```lua
debugprofilestart()
```

---

## debugprofilestop

Returns the value of the profiling timer

**Signature:**

```lua
time = debugprofilestop()
```

**Returns:**

- `time` - Current value of the profiling timer (in milliseconds, with sub-millisecond precision) (`number`)

---

## debugstack

Returns information about the current function call stack

**Signature:**

```lua
debugstring = debugstack(start, countTop, countBot)
```

**Arguments:**

- `start` - Stack level at which to begin listing functions; 0 is the `debugstack()` function itself, 1 is the function that called `debugstack()`, 2 is the function that called function 1, etc. Defaults to 1 if omitted (`number`)
- `countTop` - Maximum number of functions to output at the top of the stack trace (`number`)
- `countBot` - Maximum number of functions to output at the bottom of the stack trace, (`number`)

**Returns:**

- `debugstring` - A multi-line string describing the current function call stack (`string`)

---

## geterrorhandler

Returns the current error handler function

**Signature:**

```lua
handler = geterrorhandler()
```

**Returns:**

- `handler` - The current error handler (`function`)

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

## seterrorhandler

Changes the error handler to a specified function. The error handler is called by Lua's `error()` function, which in turn is called whenever a Lua error occurs. WoW's default error handler displays the error message, a stack trace and information about the local variables for the function. This dialog will only be shown if the "Show Lua errors" option is enabled in Interface Options.

**Signature:**

```lua
seterrorhandler(errHandler)
```

**Arguments:**

- `errHandler` - A function to use as the error handler (`function`)

---

← [WoW API Docs](../index.md)
