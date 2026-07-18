# Locale-specific functions

← [WoW API Docs](../index.md)

**3** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#locale)

---

## DeclineName

Returns suggested declensions for a name. In the Russian language, nouns (including proper names) take different form based on their usage in a sentence. When the player enters the base name for a character or pet, the game suggests one or more sets of variations for the five additional cases; the player is asked to choose from among the suggestions and/or enter their own. (The set of declensions ultimately chosen/entered by the player are only used internally and not available to addons.)

Has no effect in non-Russian-localized clients.

**Signature:**

```lua
genitive, dative, accusative, instrumental, prepositional = DeclineName("name", gender, declensionSet)
```

**Arguments:**

- `name` - Nominative form of the player's or pet's name (`string`)
- `gender` - Gender for the returned names (for declensions of the player's name, should match the player's gender; for the pet's name, should be neuter) (`number`)
  - `1or nil` - Neuter
  - `2` - Male
  - `3` - Female
- `declensionSet` - Index of a set of suggested declensions (between 1 and [`GetNumDeclensionSets(name,gender)`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumDeclensionSets). Lower indices correspond to "better" suggestions for the given name. (`number`)

**Returns:**

- `genitive` - Genitive form of the name (`string`)
- `dative` - Dative form of the name (`string`)
- `accusative` - Accusative form of the name (`string`)
- `instrumental` - Instrumental form of the name (`string`)
- `prepositional` - Prepositional form of the name (`string`)

---

## FillLocalizedClassList

Fills a table with localized class names keyed by non-localized class tokens. Note that while localized class names have no gender in English, other locales have different names for each gender.

**Signature:**

```lua
FillLocalizedClassList(table [, female])
```

**Arguments:**

- `table` - An empty table to be filled (`number`)
- `female` - True to fill the table with female class names; false or omitted to fill it with male class names (`boolean`)

**Examples:**

```lua
-- prints the localized names for each class in the main chat window,
-- with each name in the appropriate color
local classes = {}
FillLocalizedClassList(classes, true)
for token, localizedName in pairs(classes) do
   local color = RAID_CLASS_COLORS[token];
   ChatFrame1:AddMessage(localizedName, color.r, color.g, color.b)
end
```

---

## GetNumDeclensionSets

Returns the number of suggested declension sets for a name. Used in the Russian localized World of Warcraft client; see [`DeclineName`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/DeclineName) for further details. Returns 0 in other locales.

**Signature:**

```lua
numSets = GetNumDeclensionSets("name", gender)
```

**Arguments:**

- `name` - Nominative form of the player's or pet's name (`string`)
- `gender` - Gender for names (for declensions of the player's name, should match the player's gender; for the pet's name, should be neuter) (`number`)
  - `1 or nil` - Neuter
  - `2` - Male
  - `3` - Female

**Returns:**

- `numSets` - Number of available declension sets usable with [`DeclineName`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/DeclineName) (`number`)

---

← [WoW API Docs](../index.md)
