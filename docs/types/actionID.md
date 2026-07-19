# Type: actionID

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

Index identifying one of the player's action bar slots.

In UI terms, action slots are a layer of abstraction between spells or items and the mechanisms available to the player for using them conveniently. For example, instead of the default UI internally using [`SetBindingSpell()`](../categories/Keybind.md#setbindingspell), [`SetBindingMacro()`](../categories/Keybind.md#setbindingmacro), et al whenever the player changes the contents of the visible action bars, it instead manages a set of key bindings corresponding to the action bar slots.

Every player has at least `NUM_ACTIONBAR_PAGES * NUM_ACTIONBAR_BUTTONS` (in the current client, 6 * 12, or 72) action slots corresponding to the six default action bar pages. In addition, players of certain classes (or with certain talents) may have additional `actionID`s available corresponding to the "bonus" action bars that automatically become available when changing stances, stealthing, shapeshifting, etc.

---

← [API Types](../API Types.md)
