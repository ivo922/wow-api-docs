# Knowledge-base functions

← [WoW API Docs](../index.md)

**22** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#kb)

---

## KBArticle_BeginLoading `server`

Requests a specific knowledge base article from the server

**Signature:**

```lua
KBArticle_BeginLoading(articleId, searchType)
```

**Arguments:**

- `articleId` - The unique articleId to request (`number`)
- `searchType` - The search type of the request (`number`)
  - `1` - Default "top issues" search
  - `2` - Search for specific text

---

## KBArticle_GetData

Returns information about the last requested knowledge base article. Only available once the `KNOWLEDGE_BASE_ARTICLE_LOAD_SUCCESS` event has fired following an article request.

**Signature:**

```lua
id, subject, subjectAlt, text, keywords, languageId, isHot = KBArticle_GetData()
```

**Returns:**

- `id` - A unique identifier for the article (`number`)
- `subject` - The subject of the article (`string`)
- `subjectAlt` - Alternate text for the article subject (`string`)
- `text` - The body of the article (`string`)
- `keywords` - A comma separated list of keywords for the article (`string`)
- `languageId` - Identifier for the article's language (ee [`KBSetup_GetLanguageData`](Knowledge-base.md#kbsetup_getlanguagedata)) (`number`)
- `isHot` - true if the article is a "Hot Item", otherwise false (`boolean`)

---

## KBArticle_IsLoaded

Returns whether the requested knowledge base article has been loaded. The `KNOWLEDGE_BASE_ARTICLE_LOAD_SUCCESS` also indicates that the requested article is available; this function presents an alternative that can be used across UI reloads or login/logout.

**Signature:**

```lua
isLoaded = KBArticle_IsLoaded()
```

**Returns:**

- `isLoaded` - True if data for the last requested article is available; otherwise false (`boolean`)

---

## KBQuery_BeginLoading `server`

Queries the knowledge base server for articles

**Signature:**

```lua
KBQuery_BeginLoading("searchText", categoryIndex, subcategoryIndex, numArticles, page)
```

**Arguments:**

- `searchText` - The search string to use. The empty string will search for all articles in the given category (`string`)
- `categoryIndex` - The category index (`number`)
- `subcategoryIndex` - The subcategory index (`number`)
- `numArticles` - The number of articles to be returned for each page (`number`)
- `page` - The page of the total results that should be displayed. (`number`)

---

## KBQuery_GetArticleHeaderCount

Returns the number of articles on the current knowledge base search result page

**Signature:**

```lua
articleHeaderCount = KBQuery_GetArticleHeaderCount()
```

**Returns:**

- `articleHeaderCount` - The number of articles on the current knowledge base search result base page (`number`)

---

## KBQuery_GetArticleHeaderData

Returns information about an article returned in a knowledge base query

**Signature:**

```lua
articleId, title, isHotIssue, isRecentlyUpdated = KBQuery_GetArticleHeaderData(index)
```

**Arguments:**

- `index` - The index of the article to query (`number`)

**Returns:**

- `articleId` - A unique articleId for the article (`number`)
- `title` - The title of the article (`string`)
- `isHotIssue` - true if the article is a "Hot Issue", otherwise false (`boolean`)
- `isRecentlyUpdated` - true if the article has been recently updated, otherwise false (`boolean`)

---

## KBQuery_GetTotalArticleCount

Returns the total number of articles returned for the given query

**Signature:**

```lua
totalArticleHeaderCount = KBQuery_GetTotalArticleCount()
```

**Returns:**

- `totalArticleHeaderCount` - The total number of articles returned for the given query (`number`)

---

## KBQuery_IsLoaded

Returns whether results of a knowledge base query have been loaded. The `KNOWLEDGE_BASE_QUERY_LOAD_SUCCESS` also indicates that the requested results are available; this function presents an alternative that can be used across UI reloads or login/logout.

**Signature:**

```lua
isLoaded = KBQuery_IsLoaded()
```

**Returns:**

- `isLoaded` - True if query results are available; otherwise false (`boolean`)

---

## KBSetup_BeginLoading

Loads a maximum number of "Top Issues" from a given page

**Signature:**

```lua
KBSetup_BeginLoading(numArticles, currentPage)
```

**Arguments:**

- `numArticles` - The number of articles displayed per page. This is typically the constant `KBASE_NUM_ARTICLES_PER_PAGE` (`number`)
- `currentPage` - The page to display (`number`)

---

## KBSetup_GetArticleHeaderCount

Returns the number of "Top Issues" articles on the current page

**Signature:**

```lua
articleHeaderCount = KBSetup_GetArticleHeaderCount()
```

**Returns:**

- `articleHeaderCount` - The number of "Top Issues" articles on the current page (`number`)

---

## KBSetup_GetArticleHeaderData

Returns header information about a "Top Issue" article

**Signature:**

```lua
articleId, title, isHotIssue, isRecentlyUpdated = KBSetup_GetArticleHeaderData(index)
```

**Arguments:**

- `index` - The index of the article to query (`number`)

**Returns:**

- `articleId` - A unique articleId for the article (`number`)
- `title` - The title of the article (`string`)
- `isHotIssue` - true if the article is a "Hot Issue", otherwise false (`boolean`)
- `isRecentlyUpdated` - true if the article has been recently updated, otherwise false (`boolean`)

---

## KBSetup_GetCategoryCount

Returns the number of available knowledge base categories

**Signature:**

```lua
numCategories = KBSetup_GetCategoryCount()
```

**Returns:**

- `numCategories` - The number of available knowledge base categories (`number`)

---

## KBSetup_GetCategoryData

Returns information about a knowledge base category

**Signature:**

```lua
categoryId, name = KBSetup_GetCategoryData(index)
```

**Arguments:**

- `index` - The index of the category (`number`)

**Returns:**

- `categoryId` - The unique identifier for the given category (`number`)
- `name` - The name of the category (`string`)

---

## KBSetup_GetLanguageCount

Returns the number of available knowledge base languages

**Signature:**

```lua
numLanguages = KBSetup_GetLanguageCount()
```

**Returns:**

- `numLanguages` - The number of available knowledge base languages (`number`)

---

## KBSetup_GetLanguageData

Returns information about a given knowledge base language

**Signature:**

```lua
languageId, name = KBSetup_GetLanguageData(index)
```

**Arguments:**

- `index` - Index of a language to query (between 1 and [`KBSetup_GetLanguageCount()`](Knowledge-base.md#kbsetup_getlanguagecount) (`number`)

**Returns:**

- `languageId` - A number identifying the language in article headers (`number`)
- `name` - The name of the language (`string`)

---

## KBSetup_GetSubCategoryCount

Returns the number of available subcategories for a given category

**Signature:**

```lua
numSubCategories = KBSetup_GetSubCategoryCount(index)
```

**Arguments:**

- `index` - The index of the category (`number`)

**Returns:**

- `numSubCategories` - The number of available subcategories (`number`)

---

## KBSetup_GetSubCategoryData

Returns information a knowledge base subcategory

**Signature:**

```lua
categoryId, name = KBSetup_GetSubCategoryData(index, subindex)
```

**Arguments:**

- `index` - The index of the category (`number`)
- `subindex` - The index of the subcategory (`number`)

**Returns:**

- `categoryId` - The unique categoryId for the given subcategory (`number`)
- `name` - The name of the subcategory (`string`)

---

## KBSetup_GetTotalArticleCount

Returns the number of "Top Issues" articles

**Signature:**

```lua
numArticles = KBSetup_GetTotalArticleCount()
```

**Returns:**

- `numArticles` - The total number of "Top Issues" articles (`number`)

---

## KBSetup_IsLoaded

Returns whether the knowledge base default query has completed successfully. The `KNOWLEDGE_BASE_SETUP_LOAD_SUCCESS` also indicates that the knowledge base setup is complete; this function presents an alternative that can be used across UI reloads or login/logout.

**Signature:**

```lua
isLoaded = KBSetup_IsLoaded()
```

**Returns:**

- `isLoaded` - True if results for the knowledge base's default "Top Issues" query are available; false if a query is in progress or has failed (`boolean`)

---

## KBSystem_GetMOTD

Returns the currently knowledge base MOTD

**Signature:**

```lua
text = KBSystem_GetMOTD()
```

**Returns:**

- `text` - The message of the day for the knowledge base system (`string`)

---

## KBSystem_GetServerNotice

Returns the text of the knowledge base server system notice

**Signature:**

```lua
text = KBSystem_GetServerNotice()
```

**Returns:**

- `text` - The text of the knowledgebase system server notice (`string`)

---

## KBSystem_GetServerStatus

Returns the knowledge base server system status message

**Signature:**

```lua
statusMessage = KBSystem_GetServerStatus()
```

**Returns:**

- `statusMessage` - The knowledge base server status message, or nil (`string`)

---

← [WoW API Docs](../index.md)
