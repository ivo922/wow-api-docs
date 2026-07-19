# Tutorial functions

← [WoW API Docs](../index.md)

**3** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#tutorial)

---

## ClearTutorials

Disables contextual tutorial display

**Signature:**

```lua
ClearTutorials()
```

---

## FlagTutorial

Marks a contextual tutorial as displayed so it doesn't appear again

**Signature:**

```lua
FlagTutorial("tutorial")
```

**Arguments:**

- `tutorial` - Numeric identifier for the tutorial step (as string); supplied in the [`TUTORIAL_TRIGGER`](../events/TUTORIAL_TRIGGER.md) event (`string`)

---

## ResetTutorials

Enables contextual tutorial display and clears the list of already displayed tutorials. Tutorials that have already been shown to the player will appear again (via [`TUTORIAL_TRIGGER`](../events/TUTORIAL_TRIGGER.md) events) once their conditions are met. The first tutorial will appear again immediately.

**Signature:**

```lua
ResetTutorials()
```

---

← [WoW API Docs](../index.md)
