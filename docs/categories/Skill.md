# Skill functions

← [WoW API Docs](../index.md)

**7** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#skill)

---

## AbandonSkill `confirmation`

Unlearns a skill (used only for professions)

**Signature:**

```lua
AbandonSkill(index)
```

**Arguments:**

- `index` - Index of an entry in the skills list (between `1` and [`GetNumSkillLines()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumSkillLines)) (`number`)

---

## CollapseSkillHeader

Collapses a group header in the Skills UI

---

## ExpandSkillHeader

Expands a group header in the Skills UI

**Signature:**

```lua
ExpandSkillHeader(index)
```

**Arguments:**

- `index` - Index of an entry in the skills list (between 1 and [`GetNumSkillLines()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetNumSkillLines)) (`number`)

---

## GetNumSkillLines

Returns the number of entries in the Skills UI list. Includes both character skills (including non-ranked skills such as talent schools and armor proficiencies, as well as progressively learned skills such as trade skills, weapon skills, and Defense skill) and skill group headers. Reflects the current state of the list (i.e. returns a lower number if group headers are collapsed.)

**Signature:**

```lua
numSkills = GetNumSkillLines()
```

**Returns:**

- `numSkills` - Number of skills and headers to be displayed in the Skills UI (`number`)

---

## GetSelectedSkill

Returns the index of the selected skill in the Skills UI

---

## GetSkillLineInfo

**Signature:**

```lua
skillName, header, isExpanded, skillRank, numTempPoints, skillModifier, skillMaxRank, isAbandonable, stepCost, rankCost, minLevel, skillCostType, skillDescription = GetSkillLineInfo(index)
```

**Arguments:**

- `index` - The index of the skill line (`number`)

**Returns:**

- `skillName` - The name of the skill (`string`)
- `header` - 1 if the skill line is a header, instead of a skill (`1nil`)
- `isExpanded` - 1 if the skill line is a header and is expanded, otherwise nil (`1nil`)
- `skillRank` - The rank of the skill (`number`)
- `numTempPoints` - The temporary profession rank increase (for example 15 for engineering for Gnomes due to the racial trait) (`number`)
- `skillModifier` - The temporary rank modifier due to buffs, equipment, etc. (for example +Defense gear and the Defense skill) (`number`)
- `skillMaxRank` - The max rank available (`number`)
- `isAbandonable` - 1 if the skill can be unlearnt, otherwise nil (`1nil`)
- `stepCost` - Unused return value (`number`)
- `rankCost` - Unused return value (`number`)
- `minLevel` - The minimum level required to learn the skill (`number`)
- `skillCostType` - Unused return value (`number`)
- `skillDescription` - The description of the skill (`string`)

---

## SetSelectedSkill

Selects a skill in the Skills UI

---

← [WoW API Docs](../index.md)
