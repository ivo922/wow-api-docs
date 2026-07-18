# GM Ticket functions

← [WoW API Docs](../index.md)

**9** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#gmticket)

---

## DeleteGMTicket `confirmation`

Abandons the currently pending GM ticket

**Signature:**

```lua
DeleteGMTicket()
```

---

## GMResponseNeedMoreHelp

Requests further GM interaction on a ticket to which a GM has already responded

**Signature:**

```lua
GMResponseNeedMoreHelp()
```

---

## GMResponseResolve `server`

Notifies the server that the player's GM ticket issue has been resolved

**Signature:**

```lua
GMResponseResolve()
```

---

## GetGMStatus `internal`

This is a Blizzard internal function

---

## GetGMTicket `server`

Requests GM ticket status from the server. The `UPDATE_TICKET` event fires when data is ready.

**Signature:**

```lua
GetGMTicket()
```

---

## GetGMTicketCategories `deprecated`

Returns a list of available GM ticket categories. No longer used in the current GM Help UI.

**Signature:**

```lua
... = GetGMTicketCategories()
```

**Returns:**

- `...` - A variable number of categories (`string`)

---

## NewGMTicket `protected`

Opens a new GM support ticket. The default UI sets the `needResponse` flag to `true` for "Talk to a GM" and "Stuck" tickets, and `false` for "Report an issue" tickets.

**Signature:**

```lua
NewGMTicket("text", needResponse)
```

**Arguments:**

- `text` - The text to be sent in the ticket (`string`)
- `needResponse` - `true` if the issue requires personal response from a GM; otherwise `false` (`boolean`)

---

## Stuck `protected`

Uses the auto-unstuck feature

**Signature:**

```lua
Stuck()
```

---

## UpdateGMTicket `protected`

Updates the open GM ticket with new text

**Signature:**

```lua
UpdateGMTicket("text")
```

**Arguments:**

- `text` - New text for the ticket (`string`)

---

← [WoW API Docs](../index.md)
