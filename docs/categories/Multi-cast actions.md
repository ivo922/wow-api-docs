# Multi-cast actions

← [WoW API Docs](../index.md)

**1** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#multicast)

---

## SetMultiCastSpell

Sets a multi-cast action slot to a given spell. This function is used to set up the multi-cast action slots, such as the totem bar that was introduced with WoW 3.2. The player is able to customize three different sets of totems that can then be cast with a single click.

**Signature:**

```lua
SetMultiCastSpell(action, spell)
```

**Arguments:**

- `action` - The multi-cast action slot to set (`number`)
- `spell` - The numeric spellId to set to the given action slot (`number`)

---

← [WoW API Docs](../index.md)
