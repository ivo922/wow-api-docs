# LOGOUT_CANCEL

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LOGOUT_CANCEL)

---

Fires when the logout countdown is aborted. The player is required to wait several seconds before logging out or quitting if not in an inn, major city or other "resting" area -- this method fires if the player attempts to log out or quit, starting the countdown, and then performs an action which aborts it.

**Signature:**

```lua
()
```
