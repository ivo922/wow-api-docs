# Glyph functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#glyph)

---

## GetGlyphLink

Gets a hyperlink for the contents of a glyph socket.

Glyph links are distinct from item and spell links: e.g. "|cff66bbff|Hglyph:21:361|h[Glyph of Hunter's Mark]|h|r".

**Signature:**

```lua
link = GetGlyphLink(socket, talentGroup)
```

**Arguments:**

- `socket` - Which glyph socket to query (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](../types/glyphIndex.md))
- `talentGroup` - Which set of glyphs to query, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `link` - A hyperlink for the glyph socket's contents, or "" if the socket is empty (`string`, [hyperlink](../types/hyperlink.md))

---

## GetGlyphSocketInfo

Returns information about a glyph socket and its contents.

The spell ID referenced in the third return glyphSpell refers to the spell used to put the glyph in the socket -- not the Inscription spell that creates a glyph item, but the spell associated with that item's "Use:" effect.

**Signature:**

```lua
enabled, glyphType, glyphTooltipIndex, glyphSpell, icon = GetGlyphSocketInfo(socket, talentGroup)
```

**Arguments:**

- `socket` - Which glyph socket to query (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](../types/glyphIndex.md))
- `talentGroup` - Which set of glyphs to query, if the player has Dual Talent Specialization enabled (`number`)
  - `1` - Primary Talents
  - `2` - Secondary Talents
  - `nil` - Currently active talents

**Returns:**

- `enabled` - True if the socket can be given a glyph at the player's current level; false if the socket is locked (`boolean`)
- `glyphType` - 1 for minor glyph sockets, 2 for major glyph sockets, 3 for prime glyph sockets (`number`)
- `glyphTooltipIndex` - Index to be used with `GLYPH_SLOT_TOOLTIP#` for the overlay (`number`)
- `glyphSpell` - Spell ID of the spell that inscribed a glyph into the socket, or nil if the socket is empty (`number`)
- `icon` - Path to a texture for the glyph inscribed into the socket, or nil if the socket is empty (`string`)

---

## GetNumGlyphSockets `deprecated`

Currently unused. Use the constant `NUM_GLYPH_SLOTS` instead.

**Signature:**

```lua
GetNumGlyphSockets()
```

---

## GlyphMatchesSocket

Returns whether a socket is eligible for the glyph currently awaiting a target.

Only valid during glyph application: when the player has activated the glyph item but before she has chosen the glyph slot to put it in (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
match = GlyphMatchesSocket(socket)
```

**Arguments:**

- `socket` - Which glyph socket to query (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](../types/glyphIndex.md))

**Returns:**

- `match` - 1 if the glyph awaiting a target fits the given socket; nil if it doesn't fit or if no glyph is awaiting a target (`1nil`)

---

## PlaceGlyphInSocket `confirmation`

Applies the glyph currently awaiting a target to a socket. Only valid during glyph application: when the player has activated the glyph item but before she has chosen the glyph slot to put it in (i.e. the glowing hand cursor is showing).

This function does not ask for confirmation before overwriting an existing glyph. However, calling this function only begins the "spellcast" that applies the glyph, so canceling glyph application is still possible.

**Signature:**

```lua
PlaceGlyphInSocket(socket)
```

**Arguments:**

- `socket` - Which glyph socket to apply the glyph to (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](../types/glyphIndex.md))

---

## RemoveGlyphFromSocket `confirmation`

Removes the glyph from a socket

**Signature:**

```lua
RemoveGlyphFromSocket(socket)
```

**Arguments:**

- `socket` - Which glyph socket to query (between 1 and `NUM_GLYPH_SLOTS`) (`number`, [glyphIndex](../types/glyphIndex.md))

---

## SpellCanTargetGlyph

Returns whether the spell currently awaiting a target requires a glyph slot to be chosen.

Only applies when the player has attempted to cast a spell -- in this case, the "spell" cast when one uses a glyph item -- but the spell requires a target before it can begin casting (i.e. the glowing hand cursor is showing).

**Signature:**

```lua
canTarget = SpellCanTargetGlyph()
```

**Returns:**

- `canTarget` - 1 if the spell can target glyph slots (`1nil`)

---

← [WoW API Docs](../index.md)
