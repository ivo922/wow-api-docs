# Type: auraFilter

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

This parameter can be any of "HELPFUL", "HARMFUL", "PLAYER", "RAID", "CANCELABLE", "NOT_CANCELABLE". You can also specify several filters separated by a | or space character to chain multiple filters together (e.g. "HELPFUL|RAID" or "HELPFUL RAID" == helpful buffs that you can cast on your raid). By default UnitAura has "HELPFUL" as an implicit filter - you cannot get back BOTH helpful and harmful at the same time. Neither "HELPFUL" or "HARMFUL" have meaning for UnitBuff/UnitDebuff, and will be ignored.

---

← [API Types](../API Types.md)
