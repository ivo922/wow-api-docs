# GM Survey functions

← [WoW API Docs](../index.md)

**6** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#gmsurvey)

---

## GMSurveyAnswer

Returns text of multiple-choice question answers in a GM survey

**Signature:**

```lua
answerText = GMSurveyAnswer(questionIndex, answerIndex)
```

**Arguments:**

- `questionIndex` - Index of a survey question (between 1 and `MAX_SURVEY_QUESTIONS`) (`number`)
- `answerIndex` - Index of one of the question's answers (between 1 and `MAX_SURVEY_ANSWERS`) (`number`)

**Returns:**

- `answerText` - Text of the answer choice (`string`)

---

## GMSurveyAnswerSubmit

Submits an answer to a GM survey question

**Signature:**

```lua
GMSurveyAnswerSubmit(question, rank, "comment")
```

**Arguments:**

- `question` - The index of the question being answered (`number`)
- `rank` - The rank selected (`number`)
- `comment` - A comment for the given question (`string`)

---

## GMSurveyCommentSubmit

Submits a comment to the current GM survey

**Signature:**

```lua
GMSurveyCommentSubmit("comment")
```

**Arguments:**

- `comment` - The comment made on the GM Survey (`string`)

---

## GMSurveyNumAnswers `deprecated`

Returns the number of possible answers for a GM Survey question. Deprecated; default UI uses the constant `MAX_SURVEY_ANSWERS` instead.

**Signature:**

```lua
numAnswers = GMSurveyNumAnswers(questionIndex)
```

**Arguments:**

- `questionIndex` - Index of a survey question (between 1 and `MAX_SURVEY_QUESTIONS`) (`number`)

**Returns:**

- `numAnswers` - Number of multiple-choice answers to present for the question (`number`)

---

## GMSurveyQuestion

Returns the text of a specific question from a GM survey

**Signature:**

```lua
surveyQuestion = GMSurveyQuestion(index)
```

**Arguments:**

- `index` - The index of a GM survey question (`number`)

**Returns:**

- `surveyQuestion` - The question being asked (`string`)

---

## GMSurveySubmit

Submits the current GM survey

**Signature:**

```lua
GMSurveySubmit()
```

---

← [WoW API Docs](../index.md)
