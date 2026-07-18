# Taxi/Flight functions

← [WoW API Docs](../index.md)

**17** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#taxi)

---

## CloseTaxiMap

Ends interaction with the Taxi (flight master) UI. Causes the [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) event to fire, indicating that Taxi APIs may no longer have effects or return valid data.

**Signature:**

```lua
CloseTaxiMap()
```

---

## GetNumRoutes

Returns the number of hops from the current location to another taxi node. Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
numHops = GetNumRoutes(index)
```

**Arguments:**

- `index` - Index of a flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `numHops` - Number of hops from the current location to the given node (`number`)

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

## NumTaxiNodes

Returns the number of flight points on the taxi map. Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
numNodes = NumTaxiNodes()
```

**Returns:**

- `numNodes` - Number of flight points on the taxi map (`number`)

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

## SetTaxiMap

Sets a Texture object to show the appropriate flight map texture. Only has effect while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
SetTaxiMap(texture)
```

**Arguments:**

- `texture` - A Texture object (`table`)

---

## TakeTaxiNode

Embarks on a taxi flight to a given destination. Only has effect while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
TakeTaxiNode(index)
```

**Arguments:**

- `index` - Index of a flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

---

## TaxiGetDestX

Returns the horizontal coordinate of a taxi flight's destination node. Used in the default UI to draw lines between nodes; [`TaxiNodeSetCurrent()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TaxiNodeSetCurrent) should be called first so the client can compute routes.

Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
dX = TaxiGetDestX(source, dest)
```

**Arguments:**

- `source` - Index of the source flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)
- `dest` - Index of the destination flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `dX` - X coordinate of the destination taxi node (as a proportion of the taxi map's width; 0 = left edge, 1 = right edge) (`number`)

---

## TaxiGetDestY

Returns the vertical coordinate of a taxi flight's destination node. Used in the default UI to draw lines between nodes; [`TaxiNodeSetCurrent()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TaxiNodeSetCurrent) should be called first so the client can compute routes.

Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
dY = TaxiGetDestY(source, dest)
```

**Arguments:**

- `source` - Index of the source flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)
- `dest` - Index of the destination flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `dY` - Y coordinate of the destination taxi node (as a proportion of the taxi map's height; 0 = bottom, 1 = top) (`number`)

---

## TaxiGetSrcX

Returns the horizontal coordinate of a taxi flight's source node. Used in the default UI to draw lines between nodes; [`TaxiNodeSetCurrent()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TaxiNodeSetCurrent) should be called first so the client can compute routes.

Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
sX = TaxiGetSrcX(source, dest)
```

**Arguments:**

- `source` - Index of the source flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)
- `dest` - Index of the destination flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `sX` - X coordinate of the source taxi node (as a proportion of the taxi map's width; 0 = left edge, 1 = right edge) (`number`)

---

## TaxiGetSrcY

Returns the vertical coordinate of a taxi flight's source node. Used in the default UI to draw lines between nodes; [`TaxiNodeSetCurrent()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TaxiNodeSetCurrent) should be called first so the client can compute routes.

Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
sY = TaxiGetSrcY(source, dest)
```

**Arguments:**

- `source` - Index of the source flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)
- `dest` - Index of the destination flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `sY` - Y coordinate of the source taxi node (as a proportion of the taxi map's height; 0 = bottom, 1 = top) (`number`)

---

## TaxiNodeCost

Returns the cost to fly to a given taxi node. Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
cost = TaxiNodeCost(index)
```

**Arguments:**

- `index` - Index of a flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `cost` - Price of a flight to the given node (in copper) (`number`)

---

## TaxiNodeGetType

Returns the type of a flight pont. Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
type = TaxiNodeGetType(index)
```

**Arguments:**

- `index` - Index of a flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `type` - Type of the flight point (`string`)
  - `CURRENT` - The player's current location
  - `DISTANT` - Unreachable from the current location
  - `NONE` - Not currently in use
  - `REACHABLE` - Reachable from the current location (directly or through other nodes)

---

## TaxiNodeName

Returns the name of a flight point. Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
name = TaxiNodeName(index)
```

**Arguments:**

- `index` - Index of a flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `name` - Name of the taxi node (`string`)

---

## TaxiNodePosition

Returns the position of a flight point on the taxi map. Only returns valid data while interacting with a flight master (i.e. between the [`TAXIMAP_OPENED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_OPENED) and [`TAXIMAP_CLOSED`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/TAXIMAP_CLOSED) events).

**Signature:**

```lua
x, y = TaxiNodePosition(index)
```

**Arguments:**

- `index` - Index of a flight point (between 1 and [`NumTaxiNodes()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/NumTaxiNodes)) (`number`)

**Returns:**

- `x` - Horizontal coordinate of the taxi node (as a proportion of the taxi map's width; 0 = left edge, 1 = right edge) (`number`)
- `y` - Vertical coordinate of the taxi node (as a proportion of the taxi map's height; 0 = bottom, 1 = top) (`number`)

---

## TaxiNodeSetCurrent

Sets the "current" flight path node. Used in the default UI when mousing over a node; tells the client to compute the route paths involving the node (see [`TaxiGetSrcX()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/TaxiGetSrcX) et al).

**Signature:**

```lua
TaxiNodeSetCurrent(slot)
```

**Arguments:**

- `slot` - The internal index of a flight path node (`number`)

---

## UnitOnTaxi

Returns whether a unit is currently riding a flight path (taxi). Valid for any unit in the player's area of interest, but generally useful only for `player` -- taxi flights move quickly, so a taxi-riding unit visible to the player will not remain visible for very long.

**Signature:**

```lua
onTaxi = UnitOnTaxi("unit")
```

**Arguments:**

- `unit` - A unit to query (`string`, [unitID](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#unitID))

**Returns:**

- `onTaxi` - 1 if the unit is on a taxi; otherwise nil (`1nil`)

---

← [WoW API Docs](../index.md)
