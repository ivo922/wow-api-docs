# Type: arenaTeamID

← [API Types](../API Types.md) · [WoW API Docs](../index.md)

---

Identifies one of the (up to three) Arena teams to which a player can belong. These indices begin at `1` for the player's smallest team and increase with team size. For example, if the player belongs to a 2v2 team and a 5v5 team, `1` indicates the 2v2 team and `2` indicates the 5v5 team. But if the player belongs to a 3v3 team and a 5v5 team, `1` indicates 3v3 and `2` indicates 5v5. If the player is on teams of all three sizes, `1` indicates 2v2, `2` is 3v3, and `3` is 5v5.

The Blizzard UI's Lua function `ArenaTeam_GetTeamSizeID` can be used to translate a team size (2, 3, or 5) to the appropriate `arenaTeamID` for the player.

---

← [API Types](../API Types.md)
