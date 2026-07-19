# Socketing functions

← [WoW API Docs](../index.md)

**15** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#socket)

---

## AcceptSockets `confirmation`

Accepts changes made in the Item Socketing UI. Any gems added are permanently socketed into the item, and any existing gems replaced by new gems are destroyed. This function only has effect while the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
AcceptSockets()
```

---

## ClickSocketButton

Picks up or places a gem in the Item Socketing UI. If the Item Socketing UI is open and the cursor contains a socketable gem, places the gem into socket `index`. If the cursor does not hold an item and socket `index` is not locked, picks up the gem in that socket.

Only has an effect while the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
ClickSocketButton(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Examples:**

```lua
-- Put the item in the top left slot of the backpack into the first gem socket
PickupContainerItem(0,1)
ClickSocketButton(1)
```

---

## CloseSocketInfo

Ends interaction with the Item Socketing UI, discarding any changes made. Causes the [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) event to fire, indicating that Socket API functions may no longer have effects or return valid data.

**Signature:**

```lua
CloseSocketInfo()
```

---

## GetExistingSocketInfo

Returns information about a permanently socketed gem. If the given socket contains a permanently socketed gem, returns information for that gem (even if a new gem has been dropped in the socket to overwrite the existing gem, but has not yet been confirmed). If the socket is empty, returns `nil`.

Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
name, texture, name = GetExistingSocketInfo(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Returns:**

- `name` - Name of the socketed gem (`string`)
- `texture` - Path to an icon texture for the socketed gem (`string`)
- `name` - 1 if the gem matches the socket's color; otherwise nil (`1nil`)

---

## GetExistingSocketLink

Returns a hyperlink for a permanently socketed gem. If the given socket contains a permanently socketed gem, returns an item link for that gem (even if a new gem has been dropped in the socket to overwrite the existing gem, but has not yet been confirmed). If the socket is empty, returns `nil`.

Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
link = GetExistingSocketLink(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Returns:**

- `link` - A hyperlink for the socketed gem (`string`, [hyperlink](../types/hyperlink.md))

---

## GetItemGem

Returns information about gems socketed in an item

**Signature:**

```lua
name, link = GetItemGem(itemID, index) or GetItemGem("itemName", index) or GetItemGem("itemLink", index)
```

**Arguments:**

- `itemID` - An item's ID (`number`)
- `itemName` - An item's name (`string`)
- `itemLink` - An item's hyperlink, or any string containing the [`itemString`](../types/itemString.md) portion of an item link (`string`)
- `index` - Index of a socket on the item (`number`)

**Returns:**

- `name` - Name of the gem in the socket (`string`)
- `link` - A hyperlink for the gem in the socket (`string`, [hyperlink](../types/hyperlink.md))

---

## GetNewSocketInfo

Returns information about a gem added to a socket. If the given socket contains a new gem (one that has been placed in the UI, but not yet confirmed for permanently socketing into the item), returns information for that gem. If the socket is empty or has a permanently socketed gem but no new gem, returns `nil`.

Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
name, texture, matches = GetNewSocketInfo(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Returns:**

- `name` - Name of the gem added to the socket (`string`)
- `texture` - Path to an icon texture for the gem added to the socket (`string`)
- `matches` - 1 if the gem matches the socket's color; otherwise nil (`1nil`)

---

## GetNewSocketLink

Returns a hyperlink for a gem added to a socket. If the given socket contains a new gem (one that has been placed in the UI, but not yet confirmed for permanently socketing into the item), returns an item link for that gem. If the socket is empty or has a permanently socketed gem but no new gem, returns `nil`.

Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
link = GetNewSocketLink(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Returns:**

- `link` - A hyperlink for the gem added to the socket (`string`, [hyperlink](../types/hyperlink.md))

---

## GetNumSockets

Returns the number of sockets on the item currently being socketed. Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
numSockets = GetNumSockets()
```

**Returns:**

- `numSockets` - Number of sockets on the item (`number`)

---

## GetSocketItemBoundTradeable

Returns whether the item open for socketing is temporarily tradeable. A Bind on Pickup item looted by the player can be traded to other characters who were originally eligible to loot it, but only within a limited time after looting. This period can be ended prematurely if the player attempts certain actions (such as socketing gems into the item).

**Signature:**

```lua
tradeable = GetSocketItemBoundTradeable()
```

**Returns:**

- `tradeable` - `1` if the item can temporarily be traded to other players; otherwise `nil` (`1nil`)

---

## GetSocketItemInfo

Returns information about the item currently being socketed. Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
name, icon, quality = GetSocketItemInfo()
```

**Returns:**

- `name` - Name of the item (`string`)
- `icon` - Path to an icon texture for the item (`string`)
- `quality` - Quality level of the item (`number`, [itemQuality](../types/itemQuality.md))

---

## GetSocketItemRefundable

Returns whether the item open for socketing is temporarily refundable. Items bought with alternate currency (honor points, arena points, or special items such as Emblems of Heroism and Dalaran Cooking Awards) can be returned to a vendor for a full refund, but only within a limited time after the original purchase. This period can be ended prematurely if the player attempts certain actions (such as socketing gems into the item).

**Signature:**

```lua
refundable = GetSocketItemRefundable()
```

**Returns:**

- `refundable` - `1` if the item can be returned to a vendor for a refund; otherwise `nil` (`1nil`)

---

## GetSocketTypes

Returns information about the gem types usable in a socket. Only returns valid information when the Item Socketing UI is open (i.e. between the [`SOCKET_INFO_UPDATE`](../events/SOCKET_INFO_UPDATE.md) and [`SOCKET_INFO_CLOSE`](../events/SOCKET_INFO_CLOSE.md) events).

**Signature:**

```lua
gemColor = GetSocketTypes(index)
```

**Arguments:**

- `index` - Index of a gem socket (between 1 and [`GetNumSockets()`](Socketing.md#getnumsockets)) (`number`)

**Returns:**

- `gemColor` - Type of the gem socket (`string`)
  - `Blue` - Accepts any gem, but requires a blue, green, purple or prismatic gem to activate the item's socket bonus
  - `Meta` - Accepts only meta gems
  - `Red` - Accepts any gem, but requires a red, purple, orange or prismatic gem to activate the item's socket bonus
  - `Socket` - Accepts any gem
  - `Yellow` - Accepts any gem, but requires a yellow, orange, green or prismatic gem to activate the item's socket bonus

---

## SocketContainerItem

Opens an item from the player's bags for socketing

**Signature:**

```lua
SocketContainerItem(container, slot)
```

**Arguments:**

- `container` - Index of one of the player's bags or other containers (`number`, [containerID](../types/containerID.md))
- `slot` - Index of an item slot within the container (`number`, [containerSlotID](../types/containerSlotID.md))

---

## SocketInventoryItem

Opens an equipped item for socketing

**Signature:**

```lua
SocketInventoryItem(slot)
```

**Arguments:**

- `slot` - An inventory slot number, as can be obtained from [`GetInventorySlotInfo`](Inventory.md#getinventoryslotinfo) (`number`, [inventoryID](../types/inventoryID.md))

---

← [WoW API Docs](../index.md)
