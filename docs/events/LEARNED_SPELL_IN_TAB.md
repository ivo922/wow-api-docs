# LEARNED_SPELL_IN_TAB

← [Events](../Events.md) · [Home](../index.md)

[Source](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/events/LEARNED_SPELL_IN_TAB)

---

Fires when a spell is learned inside of a given spell book tab, including when spells are learned upon changing the active talent spec.

**Signature:**

```lua
(spellID, tabID)
```

**Arguments:**

- `spellID` - The spell id of the spell that was learned. (`number`)
- `tabID` - The id of the tab that has the updated item. (`number`)
