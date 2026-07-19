# Calendar functions

← [WoW API Docs](../index.md)

**93** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#calendar)

---

## CalendarAddEvent

Saves the event recently created (and selected for editing) to the calendar. Until this function is called, an event created with [`CalendarNewEvent()`](Calendar.md#calendarnewevent), [`CalendarNewGuildEvent()`](Calendar.md#calendarnewguildevent), or [`CalendarNewGuildAnnouncement()`](Calendar.md#calendarnewguildannouncement) will not exist on the calendar -- that is, guild members or invitees will not see it, and it will not persist if the player closes the calendar, reloads the UI, or goes to view or edit another event.

**Signature:**

```lua
CalendarAddEvent()
```

---

## CalendarCanAddEvent

Returns whether the player can add an event to the calendar

**Signature:**

```lua
canAdd = CalendarCanAddEvent()
```

**Returns:**

- `canAdd` - True if the player can add an event to the calendar; otherwise false (`boolean`)

---

## CalendarCanSendInvite

Returns whether the player can invite others to a calendar event

**Signature:**

```lua
canInvite = CalendarCanSendInvite()
```

**Returns:**

- `canInvite` - True if the player can invite others to a calendar event; otherwise false (`boolean`)

---

## CalendarCloseEvent

Deselects (ends viewing/editing on) an event. After calling this function, results of attempting to query or change event information are not guaranteed until a new event is created or another existing event is opened.

**Signature:**

```lua
CalendarCloseEvent()
```

---

## CalendarContextDeselectEvent

Clears the event selection used only for `CalendarContext` functions. The selection state cleared by this function is used only by other `CalendarContext` functions; other calendar event functions use the selection state set by [`CalendarOpenEvent`](Calendar.md#calendaropenevent), [`CalendarNewEvent`](Calendar.md#calendarnewevent), [`CalendarNewGuildEvent`](Calendar.md#calendarnewguildevent), or [`CalendarNewGuildAnnouncement`](Calendar.md#calendarnewguildannouncement) (if they use a selection state at all).

**Signature:**

```lua
CalendarContextDeselectEvent()
```

---

## CalendarContextEventCanComplain

Returns whether the player can report an event invitation as spam. If all arguments are omitted, uses the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent).

**Signature:**

```lua
canReport = CalendarContextEventCanComplain([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from `1` to `CalendarGetNumDayEvents()`) (`number`)

**Returns:**

- `canReport` - `true` if the player can report the event as spam; otherwise `false` (`boolean`)

---

## CalendarContextEventCanEdit

Returns whether the player can edit an event

**Signature:**

```lua
canEdit = CalendarContextEventCanEdit([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from `1` to `CalendarGetNumDayEvents()`) (`number`)

**Returns:**

- `canEdit` - True if the player can edit the event (`boolean`)

---

## CalendarContextEventClipboard

Returns whether the player can paste an event

**Signature:**

```lua
canPaste = CalendarContextEventClipboard()
```

**Returns:**

- `canPaste` - `true` if an event has been copied via [`CalendarContextEventCopy`](Calendar.md#calendarcontexteventcopy); otherwise `false` (`boolean`)

---

## CalendarContextEventComplain

Reports an event invitation as spam

**Signature:**

```lua
CalendarContextEventComplain([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from `1` to `CalendarGetNumDayEvents()`) (`number`)

---

## CalendarContextEventCopy

Copies an event for later pasting

**Signature:**

```lua
CalendarContextEventCopy([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from `1` to `CalendarGetNumDayEvents()`) (`number`)

---

## CalendarContextEventGetCalendarType

Returns the type of a calendar event. If all arguments are omitted, uses the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent).

**Signature:**

```lua
calendarType = CalendarContextEventGetCalendarType([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from `1` to `CalendarGetNumDayEvents()`) (`number`)

**Returns:**

- `calendarType` - Token identifying the type of event (`string`)
  - `GUILD_ANNOUNCEMENT` - Guild announcement (does not allow players to sign up)
  - `GUILD_EVENT` - Guild event (allows players to sign up)
  - `HOLIDAY` - World event (e.g. Lunar Festival, Darkmoon Faire, Stranglethorn Fishing Tournament, Call to Arms: Arathi Basin)
  - `PLAYER` - Player-created event or invitation
  - `RAID_LOCKOUT` - Indicates when one of the player's saved instances resets
  - `RAID_RESET` - Indicates scheduled reset times for major raid instances
  - `SYSTEM` - Other server-provided event

---

## CalendarContextEventPaste

Pastes a copied event into a given date. Does nothing if no event has been copied via [`CalendarContextEventCopy`](Calendar.md#calendarcontexteventcopy).

**Signature:**

```lua
CalendarContextEventPaste(monthOffset, day)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
- `day` - Day of the month (`number`)

---

## CalendarContextEventRemove `confirmation`

Deletes an event from the calendar

**Signature:**

```lua
CalendarContextEventRemove([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from `1` to `CalendarGetNumDayEvents()`) (`number`)

---

## CalendarContextEventSignUp

Signs the player up for a guild event

**Signature:**

```lua
CalendarContextEventSignUp([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarContextGetEventIndex

Returns the month, day, and index of the event selection used only for `CalendarContext` functions. The selection state referenced by this function is used only by other `CalendarContext` functions; other calendar event functions use the selection state set by [`CalendarOpenEvent`](Calendar.md#calendaropenevent), [`CalendarNewEvent`](Calendar.md#calendarnewevent), [`CalendarNewGuildEvent`](Calendar.md#calendarnewguildevent), or [`CalendarNewGuildAnnouncement`](Calendar.md#calendarnewguildannouncement) (if they use a selection state at all).

Used in the default UI to implement the calendar's context menu (on right-click).

**Signature:**

```lua
monthOffset, day, index = CalendarContextGetEventIndex()
```

**Returns:**

- `monthOffset` - Month relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
- `day` - Day of the month (`number`)
- `index` - Index of the event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarContextInviteAvailable

Accepts an event invitation

**Signature:**

```lua
CalendarContextInviteAvailable([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarContextInviteDecline

Declines an event invitation

**Signature:**

```lua
CalendarContextInviteDecline([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarContextInviteIsPending

Returns whether the player has been invited to an event and not yet responded

**Signature:**

```lua
pendingInvite = CalendarContextInviteIsPending([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `pendingInvite` - True if the player is invited to the event and has yet to respond; otherwise false (`boolean`)

---

## CalendarContextInviteModeratorStatus

Returns the player's moderator status for an event

**Signature:**

```lua
modStatus = CalendarContextInviteModeratorStatus([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `modStatus` - The player's level of authority for the event, or "" if not applicable (`number`)
  - `CREATOR` - The player is the original creator of the event
  - `MODERATOR` - The player has been granted moderator status for the event

---

## CalendarContextInviteRemove

Removes an invitation from the player's calendar or removes the player from a guild event's signup list

**Signature:**

```lua
CalendarContextInviteRemove([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarContextInviteStatus

Returns the player's invite status for an event

**Signature:**

```lua
inviteStatus = CalendarContextInviteStatus([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `inviteStatus` - The player's status regarding the event (`number`)
  - `1` - Invited (also used for non-invitation/non-signup events)
  - `2` - Accepted
  - `3` - Declined
  - `4` - Confirmed
  - `5` - Out
  - `6` - Standby
  - `7` - Signed up
  - `8` - Not signed up

---

## CalendarContextInviteType

Returns the invite type for an event

**Signature:**

```lua
inviteType = CalendarContextInviteType([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `inviteType` - Invitation/announcement type for the event (`number`)
  - `1` - Characters can only be explicitly invited to the event (or event is a non-invite/non-signup event)
  - `2` - Event is visible to the player's entire guild; guild members can sign up and other characters can be explicitly invited

---

## CalendarContextSelectEvent

Selects an event for use only with other `CalendarContext` functions. The selection state set by this function is used only by other `CalendarContext` functions; other calendar event functions use the selection state set by [`CalendarOpenEvent`](Calendar.md#calendaropenevent), [`CalendarNewEvent`](Calendar.md#calendarnewevent), [`CalendarNewGuildEvent`](Calendar.md#calendarnewguildevent), or [`CalendarNewGuildAnnouncement`](Calendar.md#calendarnewguildannouncement) (if they use a selection state at all).

Used in the default UI to implement the calendar's context menu (on right-click).

**Signature:**

```lua
CalendarContextSelectEvent([monthOffset,] day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
  - `nil` - Use the event selected by [`CalendarContextSelectEvent`](Calendar.md#calendarcontextselectevent) and ignore further arguments
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarDefaultGuildFilter

Returns default options for the guild member Mass Invite filter

**Signature:**

```lua
minLevel, maxLevel, rank = CalendarDefaultGuildFilter()
```

**Returns:**

- `minLevel` - Lowest level of characters to invite (`number`)
- `maxLevel` - Highest level of characters to invite (`number`)
- `rank` - Lowest guild rank of characters to invite (`number`)

---

## CalendarEventAvailable

Accepts invitation to the selected calendar event. Only applies to player-created events and invitations sent by other players; has no effect if the current calendar event is of another type.

**Signature:**

```lua
CalendarEventAvailable()
```

---

## CalendarEventCanEdit

Returns whether the player can edit the selected calendar event

**Signature:**

```lua
canEdit = CalendarEventCanEdit()
```

**Returns:**

- `canEdit` - True if the player can edit the current event; otherwise false (`boolean`)

---

## CalendarEventCanModerate

Returns whether an event invitee can be granted moderator authority

**Signature:**

```lua
canModerate = CalendarEventCanModerate(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and [`CalendarEventGetNumInvites()`](Calendar.md#calendareventgetnuminvites)) (`number`)

**Returns:**

- `canModerate` - True if the given character can be given moderator authority for the event; otherwise false (`boolean`)

---

## CalendarEventClearAutoApprove

Disables the auto-approve feature (currently unused) for the selected calendar event

**Signature:**

```lua
CalendarEventClearAutoApprove()
```

---

## CalendarEventClearLocked

Unlocks the selected calendar event. Locked events do not allow invitees to respond or guild members to sign up, but can still be edited.

**Signature:**

```lua
CalendarEventClearLocked()
```

---

## CalendarEventClearModerator

Removes moderator status from a character on the selected event's invite/signup list. Moderators can change the status of characters on the invite/signup list and invite more characters, but cannot otherwise edit the event.

**Signature:**

```lua
CalendarEventClearModerator(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()) (`number`)

---

## CalendarEventDecline

Declines invitation to the selected calendar event. Only applies to player-created events and invitations sent by other players; has no effect if the current calendar event is of another type.

**Signature:**

```lua
CalendarEventDecline()
```

---

## CalendarEventGetCalendarType

Returns the type of the selected calendar event

**Signature:**

```lua
calendarType = CalendarEventGetCalendarType()
```

**Returns:**

- `calendarType` - Token identifying the type of event (`string`)
  - `GUILD_ANNOUNCEMENT` - Guild announcement (does not allow players to sign up)
  - `GUILD_EVENT` - Guild event (allows players to sign up)
  - `PLAYER` - Player-created event or invitation

---

## CalendarEventGetInvite

Returns information about an entry in the selected event's invite/signup list

**Signature:**

```lua
name, level, className, classFileName, inviteStatus, modStatus, inviteIsMine, inviteType = CalendarEventGetInvite(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and [`CalendarEventGetNumInvites()`](Calendar.md#calendareventgetnuminvites)) (`number`)

**Returns:**

- `name` - Name of the character (`string`)
- `level` - The character's current level (`number`)
- `className` - Localized name of the character's class (`string`)
- `classFileName` - Non-localized token representing the character's class (`string`)
- `inviteStatus` - The character's status regarding the event (`number`)
  - `1` - Invited
  - `2` - Accepted
  - `3` - Declined
  - `4` - Confirmed
  - `5` - Out
  - `6` - Standby
  - `7` - Signed up
- `modStatus` - The character's level of authority for the event, or "" if not applicable (`number`)
  - `CREATOR` - The character is the original creator of the event
  - `MODERATOR` - The character has been granted moderator status for the event
- `inviteIsMine` - True if this list entry represents the player; otherwise false (`boolean`)
- `inviteType` - Invitation/announcement type for the event (`number`)
  - `1` - Characters can only be explicitly invited to the event
  - `2` - Event is visible to the player's entire guild; guild members can sign up and other characters can be explicitly invited

---

## CalendarEventGetInviteResponseTime

Returns the time at which a character on the selected event's invite/signup list responded. Returns all zeros if the character has not yet responded or is the event's creator.

**Signature:**

```lua
weekday, month, day, year, hour, minute = CalendarEventGetInviteResponseTime(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()) (`number`)

**Returns:**

- `weekday` - Index of the day of the week (starting at 1 = Sunday) (`number`)
- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)
- `hour` - Hour part of the time (on a 24-hour clock) (`number`)
- `minute` - Minute part of the time (`number`)

---

## CalendarEventGetInviteSortCriterion

Returns the current sort mode for the event invite/signup list

**Signature:**

```lua
criterion, reverse = CalendarEventGetInviteSortCriterion()
```

**Returns:**

- `criterion` - Token identifying the attribute used for sorting the list (`string`)
  - `class` - Sorted by character class (according to the global table `CLASS_SORT_ORDER`)
  - `name` - Sorted by character name
  - `status` - Sorted by invite status
- `reverse` - True if the list is sorted in reverse order; otherwise false (`boolean`)

---

## CalendarEventGetNumInvites

Returns the number of characters on the selected calendar event's invite/signup list

**Signature:**

```lua
numInvites = CalendarEventGetNumInvites()
```

**Returns:**

- `numInvites` - Number of characters on the event's invite/signup list (`number`)

---

## CalendarEventGetRepeatOptions

Returns a list of localized event repetition option labels (currently unused)

**Signature:**

```lua
... = CalendarEventGetRepeatOptions()
```

**Returns:**

- `...` - List of localized event repetition option labels (`list`)

---

## CalendarEventGetSelectedInvite

Returns the index of the selected entry on the selected event's invite/signup list. In the current default UI, selection behavior in the invite list is implemented but disabled; selecting an invite list entry has no effect on the behavior of other APIs.

**Signature:**

```lua
index = CalendarEventGetSelectedInvite()
```

**Returns:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()), or 0 if no selection has been made (`number`)

---

## CalendarEventGetStatusOptions

Returns a list of localized invite status labels

**Signature:**

```lua
... = CalendarEventGetStatusOptions()
```

**Returns:**

- `...` - List of localized invite status labels (`list`)

---

## CalendarEventGetTextures

Returns a list of instance names and icons for dungeon or raid events

**Signature:**

```lua
name, icon, expansion = CalendarEventGetTextures(eventType)
```

**Arguments:**

- `eventType` - Type (display style) of event to query (`number`)
  - `1` - Raid dungeon
  - `2` - Five-player dungeon

**Returns:**

- `name` - Name of an instance (may include heroic designation) (`string`)
- `icon` - Unique part of the path to the instance's icon texture; for the full path, prepend with `"Interface\LFGFrame\LFGIcon-"` (`string`)
- `expansion` - Expansion to which the instance belongs; localized names can be found in the constants `EXPANSION_NAME0`, `EXPANSION_NAME1`, etc. (`number`)

---

## CalendarEventGetTypes

Returns a list of event display style labels

**Signature:**

```lua
... = CalendarEventGetTypes()
```

**Returns:**

- `...` - A list of localized event display style labels (`list`)

---

## CalendarEventHasPendingInvite

Returns whether the player has been invited to the selected event and not yet responded

**Signature:**

```lua
pendingInvite = CalendarEventHasPendingInvite()
```

**Returns:**

- `pendingInvite` - True if the player has been invited to the event and not yet responded; otherwise false (`boolean`)

---

## CalendarEventHaveSettingsChanged

Returns whether the selected event has unsaved changes

**Signature:**

```lua
settingsChanged = CalendarEventHaveSettingsChanged()
```

**Returns:**

- `settingsChanged` - True if any of the event's attributes have been changed since the event was last saved; otherwise false (`boolean`)

---

## CalendarEventInvite

Attempts to invite a character to the selected event. If successful, the `CALENDAR_UPDATE_INVITE_LIST` event fires indicating the character has been added to the invite list; otherwise the `CALENDAR_UPDATE_ERROR` event fires containing a localized error message.

**Signature:**

```lua
CalendarEventInvite("name")
```

**Arguments:**

- `name` - Name of a character to invite (`string`)

---

## CalendarEventIsModerator

Returns whether the player has moderator status for the selected calendar event. Also returns true if the player is the event's creator.

**Signature:**

```lua
isModerator = CalendarEventIsModerator()
```

**Returns:**

- `isModerator` - True if the player has moderator status for the event; otherwise false (`boolean`)

---

## CalendarEventRemoveInvite

Removes a character from the selected event's invite/signup list. Cannot be used to remove the event's creator (fires a `CALENDAR_UPDATE_ERROR` event with nil error message if such is attempted).

**Signature:**

```lua
CalendarEventRemoveInvite(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()) (`number`)

---

## CalendarEventSelectInvite

Selects an entry in the selected event's invite/signup list. In the current default UI, selection behavior in the invite list is implemented but disabled; selecting an invite list entry has no effect on the behavior of other APIs.

**Signature:**

```lua
CalendarEventSelectInvite(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()) (`number`)

---

## CalendarEventSetAutoApprove

Enables the auto-approve feature (currently unused) for the selected calendar event

**Signature:**

```lua
CalendarEventSetAutoApprove()
```

---

## CalendarEventSetDate

Changes the scheduled date of the selected calendar event

**Signature:**

```lua
CalendarEventSetDate(month, day, year)
```

**Arguments:**

- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarEventSetDescription

Changes the descriptive text for the selected event

---

## CalendarEventSetLocked

Locks the selected calendar event. Locked events do not allow invitees to respond or guild members to sign up, but can still be edited.

**Signature:**

```lua
CalendarEventSetLocked()
```

---

## CalendarEventSetLockoutDate

Changes the lockout date associated with the selected event (currently unused). This feature is not enabled in the current version of World of Warcraft; saving an event in which the lockout date has been changed will revert it to its default of 1, 1, 1, 2000 (January 1, 2000).

**Signature:**

```lua
CalendarEventSetLockoutDate(month, day, year)
```

**Arguments:**

- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarEventSetLockoutTime

Changes the lockout time associated with the selected event (currently unused). This feature is not enabled in the current version of World of Warcraft; saving an event in which the lockout time has been changed will revert it to its default of 0, 0 (midnight).

**Signature:**

```lua
CalendarEventSetLockoutTime(hour, minute)
```

**Arguments:**

- `hour` - Hour part of the time (on a 24-hour clock) (`number`)
- `minute` - Minute part of the time (`number`)

---

## CalendarEventSetModerator

Grants moderator status to a character on the selected event's invite/signup list. Moderators can change the status of characters on the invite/signup list and invite more characters, but cannot otherwise edit the event.

**Signature:**

```lua
CalendarEventSetModerator(index)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()) (`number`)

---

## CalendarEventSetRepeatOption

Changes the repetition option for the selected event (currently unused). This feature is not enabled in the current version of World of Warcraft; saving an event in which the repeat option has been changed will revert it to its default of 1 (Never).

**Signature:**

```lua
CalendarEventSetRepeatOption(title)
```

**Arguments:**

- `title` - Index of a repeating event option; see CalendarEventGetRepeatOptions() (`number`)

---

## CalendarEventSetSize

Changes the maximum number of invites/signups for the selected event (currently unused). This feature is not enabled in the current version of World of Warcraft; saving an event in which the max size has been changed will revert it to its default of 100.

**Signature:**

```lua
CalendarEventSetSize(size)
```

**Arguments:**

- `size` - Maximum number of invites/signups for the event (`number`)

---

## CalendarEventSetStatus

Sets the status of a character on the selected event's invite/signup list

**Signature:**

```lua
CalendarEventSetStatus(index, inviteStatus)
```

**Arguments:**

- `index` - Index of a character on the event's invite list (between 1 and CalendarEventGetNumInvites()) (`number`)
- `inviteStatus` - The player's status regarding the event (`number`)
  - `1` - Invited (also used for non-invitation/non-signup events)
  - `2` - Accepted
  - `3` - Declined
  - `4` - Confirmed
  - `5` - Out
  - `6` - Standby
  - `7` - Signed up
  - `8` - Not signed up (displays as "")

---

## CalendarEventSetTextureID

Changes the raid or dungeon instance for the selected event. Only applicable if the event's `eventType` is set to 1 or 2 (see [`CalendarEventSetType`](Calendar.md#calendareventsettype)).

A list of dungeon or raid instances can be found by calling [`CalendarEventGetTextures`](Calendar.md#calendareventgettextures) with the current `eventType`. That function returns three values (`name`, `icon`, and `expansion`) for each instance in the list; e.g. to get the `index` for use with this function, find the index of the instance's name in that list and divide by 3.

**Signature:**

```lua
CalendarEventSetTextureID(index)
```

**Arguments:**

- `index` - Index of a dungeon or raid instance (`number`)

---

## CalendarEventSetTime

Changes the scheduled time of the selected event

**Signature:**

```lua
CalendarEventSetTime(hour, minute)
```

**Arguments:**

- `hour` - Hour part of the time (on a 24-hour clock) (`number`)
- `minute` - Minute part of the time (`number`)

---

## CalendarEventSetTitle

Changes the title for the selected event

**Signature:**

```lua
CalendarEventSetTitle("title")
```

**Arguments:**

- `title` - A title to be displayed for the event (`string`)

---

## CalendarEventSetType

Changes the display type of the selected event

**Signature:**

```lua
CalendarEventSetType(eventType)
```

**Arguments:**

- `eventType` - Display type for the event; used in the default UI to determine which icon to show (`number`)
  - `1` - Raid dungeon
  - `2` - Five-player dungeon
  - `3` - PvP event
  - `4` - Meeting
  - `5` - Other event

---

## CalendarEventSignUp

Signs the player up for the selected calendar event. Only applies to guild events; has no effect if called when the current calendar event is not a guild event.

**Signature:**

```lua
CalendarEventSignUp()
```

---

## CalendarEventSortInvites

Sorts the event invite/signup list. Does not cause the list to automatically remain sorted; e.g. if sorted by status and a character's status is changed, the list will not be resorted until this function is called again.

**Signature:**

```lua
CalendarEventSortInvites("criterion", reverse)
```

**Arguments:**

- `criterion` - Token identifying the attribute to use for sorting the list (`string`)
  - `class` - Sort by character class (according to the global table `CLASS_SORT_ORDER`)
  - `name` - Sort by character name
  - `status` - Sort by invite status
- `reverse` - True to sort the lis in reverse order; otherwise false (`boolean`)

---

## CalendarGetAbsMonth

Returns date information for a given month and year. Note: This function is broken in WoW 3.1.1, but is expected to work as described in WoW Patch 3.2.0 and later.

**Signature:**

```lua
month, year, numDays, firstWeekday = CalendarGetAbsMonth(month, year)
```

**Arguments:**

- `month` - Index of a month (starting at 1 = January) (`number`)
- `year` - Year (full four-digit year) (`number`)

**Returns:**

- `month` - Index of the month (starting at 1 = January) (`number`)
- `year` - Year (full four-digit year) (`number`)
- `numDays` - Number of days in the month (`number`)
- `firstWeekday` - Index of the weekday (starting at 1 = Sunday) for the first day of the month (`number`)

---

## CalendarGetDate

Returns the current date (in the server's time zone). Only returns valid information after the `PLAYER_LOGIN` event has fired.

**Signature:**

```lua
weekday, month, day, year = CalendarGetDate()
```

**Returns:**

- `weekday` - Index of the day of the week (starting at 1 = Sunday) (`number`)
- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarGetDayEvent

Returns information about a calendar event on a given day. Information can only be retrieved for events which might be visible in the calendar's current month -- i.e. those in the current month as well as those in (roughly) the last week of the previous month and (roughly) the first two weeks of the following month. To reliably retrieve information for events outside the calendar's current month, first change the calendar's month with [`CalendarSetMonth`](Calendar.md#calendarsetmonth).

**Signature:**

```lua
title, hour, minute, calendarType, sequenceType, eventType, texture, modStatus, inviteStatus, invitedBy, difficulty, inviteType = CalendarGetDayEvent(monthOffset, day, index)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
- `day` - Day of the month containing an event (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `title` - Title displayed for the event (`string`)
- `hour` - Hour part of the event's start time (on a 24-hour clock) (`number`)
- `minute` - Minute part of the event's start time (`number`)
- `calendarType` - Token identifying the type of event (`string`)
  - `GUILD_ANNOUNCEMENT` - Guild announcement (does not allow players to sign up)
  - `GUILD_EVENT` - Guild event (allows players to sign up)
  - `HOLIDAY` - World event (e.g. Lunar Festival, Darkmoon Faire, Stranglethorn Fishing Tournament, Call to Arms: Arathi Basin)
  - `PLAYER` - Player-created event or invitation
  - `RAID_LOCKOUT` - Indicates when one of the player's saved instances resets
  - `RAID_RESET` - Indicates scheduled reset times for major raid instances
  - `SYSTEM` - Other server-provided event
- `sequenceType` - Display cue for multi-day events, or "" if not applicable (`string`)
  - `END` - Last day of the event
  - `INFO` - An additional specially-labeled day related the event
  - `ONGOING` - Continuation of the event
  - `START` - First day of the event
- `eventType` - Display type for the event; used in the default UI to determine which icon to show (`number`)
  - `0` - Holiday or other server-provided event
  - `1` - Raid dungeon
  - `2` - Five-player dungeon
  - `3` - PvP event
  - `4` - Meeting
  - `5` - Other event
- `texture` - Unique portion of the path to a texture for the event (e.g. "Calendar*ChildrensWeek"). The mechanism by which a full texture path can be generated is not public API, but can be found in Addons/Blizzard*Calendar/Blizzard_Calendar.lua after extracting default UI files with the AddOn Kit. (`string`)
- `modStatus` - The player's level of authority for the event, or "" if not applicable (`number`)
  - `CREATOR` - The player is the original creator of the event
  - `MODERATOR` - The player has been granted moderator status for the event
- `inviteStatus` - The player's status regarding the event (`number`)
  - `1` - Invited (also used for non-invitation/non-signup events)
  - `2` - Accepted
  - `3` - Declined
  - `4` - Confirmed
  - `5` - Out
  - `6` - Standby
  - `7` - Signed up
  - `8` - Not signed up
- `invitedBy` - Name of the character who created (or invited the player to) the event (`string`)
- `difficulty` - Difficulty of the dungeon or raid instance associated with the event (used only for `RAID_LOCKOUT` and `RAID_RESET` events, not player-created raid/dungeon events) (`number`)
  - `1` - Normal
  - `2` - Heroic
- `inviteType` - Invitation/announcement type for the event (`number`)
  - `1` - Characters can only be explicitly invited to the event (or event is a non-invite/non-signup event)
  - `2` - Event is visible to the player's entire guild; guild members can sign up and other characters can be explicitly invited

---

## CalendarGetEventIndex

Returns the month, day, and index of the selected calendar event

**Signature:**

```lua
monthOffset, day, index = CalendarGetEventIndex()
```

**Returns:**

- `monthOffset` - Month relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month
- `day` - Day of the month (`number`)
- `index` - Index of the event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarGetEventInfo

Returns information about the selected calendar event (for player/guild events)

**Signature:**

```lua
title, description, creator, eventType, repeatOption, maxSize, textureIndex, weekday, month, day, year, hour, minute, lockoutWeekday, lockoutMonth, lockoutDay, lockoutYear, lockoutHour, lockoutMinute, locked, autoApprove, pendingInvite, inviteStatus, inviteType, calendarType = CalendarGetEventInfo()
```

**Returns:**

- `title` - Title displayed for the event (`string`)
- `description` - Descriptive text about the event (`string`)
- `creator` - Name of the character who created the event (`string`)
- `eventType` - Display style for the event; used in the default UI to determine which icon to show (`number`)
  - `1` - Raid dungeon
  - `2` - Five-player dungeon
  - `3` - PvP event
  - `4` - Meeting
  - `5` - Other event
- `repeatOption` - Index of an event repetition option (see CalendarEventGetRepeatOptions); currently unused (always 1) (`number`)
- `maxSize` - Maximum number of invites/signups; currently unused (always 100) (`number`)
- `textureIndex` - Index of the dungeon or raid instance (between `1` and `select("#", CalendarEventGetTextures(eventType)) / 3` (`number`)
- `weekday` - Index of the day of the week on which the event starts (starting at 1 = Sunday) (`number`)
- `month` - Index of the month in which the event starts (starting at 1 = January) (`number`)
- `day` - Day of the month on which the event starts (`number`)
- `year` - Year in which the event starts (full four-digit year) (`number`)
- `hour` - Hour part of the event's start time (on a 24-hour clock) (`number`)
- `minute` - Minute part of the event's start time (`number`)
- `lockoutWeekday` - Currently unused (`number`)
- `lockoutMonth` - Currently unused (`number`)
- `lockoutDay` - Currently unused (`number`)
- `lockoutYear` - Currently unused (`number`)
- `lockoutHour` - Currently unused (`number`)
- `lockoutMinute` - Currently unused (`number`)
- `locked` - 1 if the event is locked (preventing invitees from responding); otherwise nil (`1nil`)
- `autoApprove` - 1 if signups to the event should be automatically approved (currently unused); otherwise nil (`1nil`)
- `pendingInvite` - 1 if the player has been invited to this event and has not yet responded; otherwise nil (`1nil`)
- `inviteStatus` - The player's status regarding the event (`number`)
  - `1` - Invited
  - `2` - Accepted
  - `3` - Declined
  - `4` - Confirmed
  - `5` - Out
  - `6` - Standby
  - `7` - Signed up
  - `8` - Not signed up
- `inviteType` - Invitation/announcement type for the event (`number`)
  - `1` - Player has been explicitly invited to the event and can accept or decline
  - `2` - Event is visible to the player's entire guild; player can sign up if desired
- `calendarType` - Token identifying the type of event (`string`)
  - `GUILD_ANNOUNCEMENT` - Guild announcement (does not allow players to sign up)
  - `GUILD_EVENT` - Guild event (allows players to sign up)
  - `PLAYER` - Player-created event or invitation
  - `SYSTEM` - Other server-provided event

---

## CalendarGetFirstPendingInvite

Returns the index of the first invitation on a given day to which the player has not responded

**Signature:**

```lua
index = CalendarGetFirstPendingInvite(monthOffset, day)
```

**Arguments:**

- `monthOffset` - Month to query relative to the calendar's currently displayed month (i.e. 0 for current month, 1 for next month, -1 for previous month) (`number`)
- `day` - Day of the month to query (`number`)

**Returns:**

- `index` - Index of the event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarGetHolidayInfo

Returns additional information about a holiday event. Information can only be retrieved for events which might be visible in the calendar's current month -- i.e. those in the current month as well as those in (roughly) the last week of the previous month and (roughly) the first two weeks of the following month. To reliably retrieve information for events outside the calendar's current month, first change the calendar's month with [`CalendarSetMonth`](Calendar.md#calendarsetmonth).

**Signature:**

```lua
name, description, texture = CalendarGetHolidayInfo(monthOffset, day, index)
```

**Arguments:**

- `monthOffset` - Month to query relative to the calendar's currently displayed month (i.e. 0 for current month, 1 for next month, -1 for previous month) (`number`)
- `day` - Day of the month to query (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `name` - Localized name of the event (`string`)
- `description` - Localized text describing the event (`string`)
- `texture` - Unique portion of the path to a texture for the event (e.g. "Calendar*ChildrensWeek"). The mechanism by which a full texture path can be generated is not public API, but can be found in Addons/Blizzard*Calendar/Blizzard_Calendar.lua after extracting default UI files with the AddOn Kit. (`string`)

---

## CalendarGetMaxCreateDate

Returns the latest date for which events may be scheduled. Currently, events can only be created up to one year from the last day of the current month (e.g. If the current date is May 19, 2009, the player is not allowed to create events scheduled for later than May 31, 2010). The default Calendar UI also does not allow viewing months beyond this date.

**Signature:**

```lua
weekday, month, day, year = CalendarGetMaxCreateDate()
```

**Returns:**

- `weekday` - Index of the day of the week (starting at 1 = Sunday) (`number`)
- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarGetMaxDate

Returns the latest date usable in the calendar system. This function currently always returns December 31st, 2030 as the max date.

**Signature:**

```lua
weekday, month, day, year = CalendarGetMaxDate()
```

**Returns:**

- `weekday` - Index of the day of the week (starting at 1 = Sunday) (`number`)
- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarGetMinDate

Returns the earliest date usable in the calendar system. This function currently returns November 24th, 2004 as the minimum date. This is the date that World of Warcraft was launched in the U.S.

**Signature:**

```lua
weekday, month, day, year = CalendarGetMinDate()
```

**Returns:**

- `weekday` - Index of the day of the week (starting at 1 = Sunday) (`number`)
- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarGetMinHistoryDate

Returns the earliest date for which information about past player events is available. Applies to events created by the player, invites the player accepted, and guild events or announcements. Currently, the default UI only shows past events from up to two weeks before the current date.

**Signature:**

```lua
weekday, month, day, year = CalendarGetMinHistoryDate()
```

**Returns:**

- `weekday` - Index of the day of the week (starting at 1 = Sunday) (`number`)
- `month` - Index of the month (starting at 1 = January) (`number`)
- `day` - Day of the month (`number`)
- `year` - Year (full four-digit year) (`number`)

---

## CalendarGetMonth

Returns information about a calendar month

**Signature:**

```lua
month, year, numDays, firstWeekday = CalendarGetMonth([monthOffset])
```

**Arguments:**

- `monthOffset` - Month to query relative to the calendar's currently displayed month (i.e. 0 for current month, 1 for next month, -1 for previous month). Defaults to the calendar's current month if omitted. (`number`)

**Returns:**

- `month` - Index of the month (starting at 1 = January) (`number`)
- `year` - Year (full four-digit year) (`number`)
- `numDays` - Number of days in the month (`number`)
- `firstWeekday` - Index of the weekday (starting at 1 = Sunday) for the first day of the month (`number`)

---

## CalendarGetMonthNames

Returns a list of localized month names

**Signature:**

```lua
... = CalendarGetMonthNames()
```

**Returns:**

- `...` - A list of localized month names in calendar order (i.e. 1 = January) (`list`)

---

## CalendarGetNumDayEvents

Returns the number of calendar events on a given day

**Signature:**

```lua
numEvents = CalendarGetNumDayEvents(monthOffset, day)
```

**Arguments:**

- `monthOffset` - Month to query relative to the calendar's currently displayed month (i.e. 0 for current month, 1 for next month, -1 for previous month) (`number`)
- `day` - Day of the month to query (`number`)

**Returns:**

- `numEvents` - Number of events on the given day (`number`)

---

## CalendarGetNumPendingInvites

Returns the number of calendar invitations to which the player has yet to respond

**Signature:**

```lua
numInvites = CalendarGetNumPendingInvites()
```

**Returns:**

- `numInvites` - Number of pending calendar invitations (`number`)

---

## CalendarGetRaidInfo

Returns information about a raid lockout or scheduled raid reset event. Information can only be retrieved for events which might be visible in the calendar's current month -- i.e. those in the current month as well as those in (roughly) the last week of the previous month and (roughly) the first two weeks of the following month. To reliably retrieve information for events outside the calendar's current month, first change the calendar's month with [`CalendarSetMonth`](Calendar.md#calendarsetmonth).

**Signature:**

```lua
title, calendarType, raidID, hour, minute, difficulty = CalendarGetRaidInfo(monthOffset, day, index)
```

**Arguments:**

- `monthOffset` - Month to query relative to the calendar's currently displayed month (i.e. 0 for current month, 1 for next month, -1 for previous month) (`number`)
- `day` - Day of the month to query (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

**Returns:**

- `title` - Title displayed for the event (`number`)
- `calendarType` - Token identifying the type of event (`string`)
  - `RAID_LOCKOUT` - Indicates when one of the player's saved instances resets
  - `RAID_RESET` - Indicates scheduled reset times for major raid instances
- `raidID` - ID number of the instance to which the player is saved, or 0 if not applicable (`number`)
- `hour` - Hour part of the time at which the instance resets (on a 24-hour clock) (`number`)
- `minute` - Minute part of the time at which the instance resets (`number`)
- `difficulty` - Difficulty of the dungeon or raid instance associated with the event (`number`)
  - `1` - Normal
  - `2` - Heroic

---

## CalendarGetWeekdayNames

Returns a list of localized weekday names

**Signature:**

```lua
... = CalendarGetWeekdayNames()
```

**Returns:**

- `...` - A list of localized weekday names in calendar order (i.e. 1 = Sunday) (`list`)

---

## CalendarIsActionPending

Returns whether an update to calendar information is in progress. Returns true while the client is synchronizing its calendar information from the server; e.g. after calling CalendarOpenEvent, CalendarAddEvent, or CalendarUpdateEvent. During such periods, using other calendar API functions to query or change event information may not have valid orexpected results.

**Signature:**

```lua
isPending = CalendarIsActionPending()
```

**Returns:**

- `isPending` - True if an update to calendar information is in progress; otherwise false (`boolean`)

---

## CalendarMassInviteArenaTeam

Repopulates the current event's invite list with members of one of the player's arena teams. Clears any invites already listed. Can only be used for events not yet created (i.e. saved to the calendar).

**Signature:**

```lua
CalendarMassInviteArenaTeam(index)
```

**Arguments:**

- `index` - Index of an arena team type (`number`)
  - `1` - 2v2 team
  - `2` - 3v3 team
  - `3` - 5v5 team

---

## CalendarMassInviteGuild

Repopulates the selected event's invite list with members of the player's guild. Clears any invites already listed. Can only be used for events not yet created (i.e. saved to the calendar).

**Signature:**

```lua
CalendarMassInviteGuild(minLevel, maxLevel, rank)
```

**Arguments:**

- `minLevel` - Lowest level of characters to invite (`number`)
- `maxLevel` - Highest level of characters to invite (`number`)
- `rank` - Lowest guild rank of characters to invite (`number`)

---

## CalendarNewEvent

Creates a new event and selects it for viewing/editing

**Signature:**

```lua
CalendarNewEvent()
```

---

## CalendarNewGuildAnnouncement

Creates a new guild announcement and selects it for viewing/editing. Guild announcements are visible to all guild members but do not allow signups or invitations.

**Signature:**

```lua
CalendarNewGuildAnnouncement()
```

---

## CalendarNewGuildEvent

Creates a new guild event and selects it for viewing/editing. Guild events are visible to all guild members and allow members to sign up (or non-members to be invited).

**Signature:**

```lua
CalendarNewGuildEvent()
```

---

## CalendarOpenEvent

Selects a calendar event for viewing/editing

**Signature:**

```lua
CalendarOpenEvent(monthOffset, day, index)
```

**Arguments:**

- `monthOffset` - Month to query relative to the calendar's currently displayed month (i.e. 0 for current month, 1 for next month, -1 for previous month) (`number`)
- `day` - Day of the month to query (`number`)
- `index` - Index of an event on the given day (from 1 to CalendarGetNumDayEvents()) (`number`)

---

## CalendarRemoveEvent

Removes the selected event invitation from the player's calendar or removes the player from the selected guild event's signup list. NOTE: May disconnect the player if called when the selected calendar event is not a received invitation or a guild event.

**Signature:**

```lua
CalendarRemoveEvent()
```

---

## CalendarSetAbsMonth

Set's the calendar's month to an absolute date

**Signature:**

```lua
CalendarSetAbsMonth(month [, year])
```

**Arguments:**

- `month` - Index of the month (starting at 1 = January) (`number`)
- `year` - Year (full four-digit year); uses current year if omitted (`number`)

---

## CalendarSetMonth

Sets the calendar's month relative to its current month

**Signature:**

```lua
CalendarSetMonth(monthOffset)
```

**Arguments:**

- `monthOffset` - Month containing an event relative to the calendar's currently displayed month (`number`)
  - `-1` - Month preceding the calendar's current month
  - `0` - The calendar's current month (i.e. same month as CalendarGetMonth())
  - `1` - Month after the calendar's current month

---

## CalendarUpdateEvent

Saves changes made to the selected event. Until this function is called, changes made to an event will not be saved -- they will not propagate to guild members or invitees, and the event will revert to its previous state if the player closes the calendar, reloads the UI, or goes to view or edit another event.

Only applies to existing events; for newly created events use [`CalendarAddEvent()`](Calendar.md#calendaraddevent) once the event's attributes and initial invite list are set.

**Signature:**

```lua
CalendarUpdateEvent()
```

---

## CanEditGuildEvent

Returns whether the player is allowed to edit guild-wide calendar events

**Signature:**

```lua
canEdit = CanEditGuildEvent()
```

**Returns:**

- `canEdit` - 1 if the player can create or edit guild calendar events, otherwise nil (`1nil`)

---

## OpenCalendar `server`

Queries the server for calendar status information. May cause one or more `CALENDAR_UPDATE_*` events to fire depending on the contents of the player's calendar. In the default UI, called when the calendar is shown.

**Signature:**

```lua
OpenCalendar()
```

---

← [WoW API Docs](../index.md)
