# Lua library functions

← [WoW API Docs](../index.md)

**59** functions · [Source category](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_categories#lua)

---

## abs `luaapi`

Returns the absolute value of a number. Alias for the standard library function `math.abs`.

**Signature:**

```lua
absoluteValue = abs(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `absoluteValue` - Absolute value of `x` (`number`)

---

## assert `luaapi`

Causes a Lua error if a condition is failed

**Signature:**

```lua
value = assert(condition, "message")
```

**Arguments:**

- `condition` - Any value (commonly the result of an expression) (`value`)
- `message` - Error message to be produced if `condition` is `false` or `nil` (`string`)

**Returns:**

- `value` - The `condition` value provided, if not `false` or `nil` (`value`)

---

## ceil `luaapi`

Returns the smallest integer larger than or equal to a number. Alias for the standard library function `math.ceil`.

**Signature:**

```lua
ceiling = ceil(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `ceiling` - Smallest integer larger than or equal to `x` (`number`)

---

## collectgarbage `luaapi`

Interface to the Lua garbage collector

**Signature:**

```lua
collectgarbage(option [, arg])
```

**Arguments:**

- `option` - One of the following options
  - `collect` - Performs a full garbage collection cycle
  - `count` - Returns the total Lua memory usage (in kilobytes)
  - `restart` - Restarts the garbage collector
  - `setpause` - Sets the garbage collector's pause percentage to `arg`; e.g., if 200, the collector waits for memory usage to double before starting a new cycle
  - `setstepmul` - Sets the garbage collector's speed (as a percentage relative to memory allocation) to `arg`; e.g., if 200, the collector runs twice as fast as memory is allocated
  - `step` - Performs a garbage collection step, with size `arg`
  - `stop` - Stops the garbage collector
- `arg` - Argument applicable to some options

---

## date `luaapi`

Returns a formatted date/time string for a date (or the current date). Alias to the standard library function `os.date`.

**Signature:**

```lua
dateValue = date(["format" [, time]])
```

**Arguments:**

- `format` - A string describing the formatting of time values (as in the ANSI C `strftime()`function), or `*t` to return the time as a table; optionally preceded by `!` for Coordinated Universal Time instead of the local time zone; omitted for a date printed in the default format (`string`)
- `time` - Time value to be formatted (see [`time()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/time) for description); if omitted, uses the current time (`number`)

**Returns:**

- `dateValue` - A formatted date/time string, (`string or table`)

---

## deg `luaapi`

Converts an angle measurement in radians to degrees. Alias for the standard library function `math.deg`.

**Signature:**

```lua
degrees = deg(radians)
```

**Arguments:**

- `radians` - An angle specified in radians (`number`)

**Returns:**

- `degrees` - The angle specified in degrees (`number`)

---

## difftime `luaapi`

Returns the number of seconds between two time values. Alias for the standard library function `os.difftime`.

**Signature:**

```lua
seconds = difftime(time2, time1)
```

**Arguments:**

- `time2` - A time value (see [`time()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/time) for description) (`number`)
- `time1` - A time value (see [`time()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/time) for description) (`number`)

**Returns:**

- `seconds` - Number of seconds between `time2` and `time1`; equivalent to `time2 - time1` on all current WoW clients (`number`)

---

## error `luaapi`

Causes a Lua error message

**Signature:**

```lua
error("message" [, level])
```

**Arguments:**

- `message` - An error message to be displayed (`string`)
- `level` - Level in the function stack at which the error message begins providing function information; e.g. 1 (the default, if omitted) to start at the position where `error()` was called, 2 to start at the function which called `error()`, 3 to start at the function which called that function, etc. (`number`)

---

## exp `luaapi`

Returns the value of the exponential function for a number. Alias for the standard library function `math.exp`.

**Signature:**

```lua
exp = exp(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `exp` - Value of the mathematical constant *e* (Euler's number) raised to the `x`th power (`number`)

---

## floor `luaapi`

Returns the largest integer smaller than or equal to a number. Alias for the standard library function `math.floor`.

**Signature:**

```lua
floor = floor(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `floor` - Largest integer smaller than or equal to `x` (`number`)

---

## foreach `deprecated` `luaapi`

This function is deprecated and should no longer be used

---

## foreachi `deprecated` `luaapi`

This function is deprecated and should no longer be used

---

## format `luaapi`

Returns a formatted string containing specified values. Alias for the standard library function `string.format`. This version, however, includes the positional argument specifiers from Lua 4.0.

Lua does not support the ANSI C format specifiers `*`, `l`, `L`, `n`, `p`, and `h` but includes an extra specifier, `q`, which formats a string in a form suitable to be safely read back by the Lua interpreter: the string is written between double quotes, and all double quotes, newlines, embedded zeros, and backslashes in the string are correctly escaped when written.

**Signature:**

```lua
formatted = format("formatString", ...)
```

**Arguments:**

- `formatString` - A string containing format specifiers as per the ANSI C `printf` function (`string`)
- `...` - A list of values to be included in the formatted string (`list`)

**Returns:**

- `formatted` - The formatted string (`number`)

---

## frexp `luaapi`

Returns the normalized fraction and base-2 exponent for a number. Alias for the standard library function `math.frexp`.

**Signature:**

```lua
m, e = frexp(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `m` - A number whose absolute value is in the range [0.5, 1), or 0 if `x` is 0 (`number`)
- `e` - An integer, such that `x = m * 2 ^ e` (`number`)

---

## gcinfo `deprecated` `luaapi`

Returns the total Lua memory usage. Deprecated in Lua 5.1; use `collectgarbage("count")` instead.

**Signature:**

```lua
count = gcinfo()
```

**Returns:**

- `count` - Total Lua memory usage (in kilobytes) (`number`)

---

## getfenv `luaapi`

Returns the environment for a function (or the global environment). If the environment has a `__environment` metatable, that value is returned instead.

**Signature:**

```lua
env = getfenv([f]) or getfenv([stackLevel])
```

**Arguments:**

- `f` - A function (`function`)
- `stackLevel` - Level of a function in the calling stack (`number`)

**Returns:**

- `env` - Table containing all variables in the function's environment, or the global environment if `f` or `stackLevel` is omitted (`table`)

---

## getmetatable `luaapi`

Returns an object's metatable

**Signature:**

```lua
metatable = getmetatable(object)
```

**Arguments:**

- `object` - Any table or userdata object (`value`)

**Returns:**

- `metatable` - Contents of the object's `__metatable` field, or nil if the object has no metatable (`value`)

---

## getn `deprecated` `luaapi`

This function is deprecated and should no longer be used

---

## gmatch `luaapi`

Returns an iterator function for finding pattern matches in a string. Alias for the standard library function `string.gmatch`.

**Signature:**

```lua
iterator = gmatch("s", "pattern")
```

**Arguments:**

- `s` - A string (`string`)
- `pattern` - A regular expression pattern (`string`, [pattern](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#pattern))

**Returns:**

- `iterator` - A function which, each time it is called, returns the next capture of `pattern` in the string `s`; always returns the whole string if `pattern` specifies no captures (`function`)

---

## gsub `luaapi`

Returns a string in which occurrences of a pattern are replaced. Alias for the standard library function `string.gsub`.

**Signature:**

```lua
newString, numMatched = gsub("s", "pattern", "rep" [, maxReplaced]) or gsub("s", "pattern", repTable [, maxReplaced]) or gsub("s", "pattern", repFunc [, maxReplaced])
```

**Arguments:**

- `s` - A string (`string`)
- `pattern` - A regular expression pattern (`string`, [pattern](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#pattern))
- `rep` - String with which to replace occurrences of `pattern`; may contain specifiers for numbered captures in the `pattern` (`string`)
- `repTable` - Table containing replacement strings; replacements are looked up using captured substrings as keys, or the entire match if `pattern` specifies no captures (`table`)
- `repFunc` - Function to supply replacement strings; called with captured substrings (or the entire match if `pattern` specifies no captures) as arguments (`function`)
- `maxReplaced` - Maximum number of replacements to be made (`number`)

**Returns:**

- `newString` - A copy of `s` in which occurrences of the `pattern` have been replaced as specified (`string`)
- `numMatched` - Number of matches found (`number`)

---

## ipairs `luaapi`

Returns an iterator function for integer keys in a table. Return values are such that the construction
` for k,v in ipairs(t) do
 -- body
 end
`

will iterate over the pairs `1,t[1]`, `2,t[2]`, etc, up to the first integer key absent from the table.

**Signature:**

```lua
iterator, t, index = ipairs(t)
```

**Arguments:**

- `t` - A table (`table`)

**Returns:**

- `iterator` - An iterator (`function`)
- `t` - The table provided (`table`)
- `index` - Always 0; used internally (`number`)

---

## ldexp `luaapi`

Returns the number generated by a normalized fraction and base-2 exponent. Alias for the standard library function `math.ldexp`.

**Signature:**

```lua
x = ldexp(m, e)
```

**Arguments:**

- `m` - A number (`number`)
- `e` - A number (`number`)

**Returns:**

- `x` - The value of `m * 2 ^ e` (`number`)

---

## loadstring `luaapi`

Loads and compiles Lua source code

**Signature:**

```lua
chunk, error = loadstring("s" [, "chunkname"])
```

**Arguments:**

- `s` - A string containing Lua code (`string`)
- `chunkname` - Name for the loaded chunk; used in error messages and debug information (`string`)

**Returns:**

- `chunk` - A function which can be run to execute the provided code, or nil if the code could not be compiled (`function`)
- `error` - Error message, if the code could not be compiled (`string`)

---

## log `luaapi`

Returns the natural logarithm of a number. Alias for the standard library function `math.log`.

**Signature:**

```lua
naturalLog = log(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `naturalLog` - The natural logarithm of `x` (`number`)

---

## log10 `luaapi`

Returns the base-10 logarithm of a number. Alias for the standard library function `math.log10`.

**Signature:**

```lua
base10log = log10(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `base10log` - The base-10 logarithm of `x` (`number`)

---

## max `luaapi`

Returns the greatest of a list of numbers. Alias for the standard library function `math.max`.

**Signature:**

```lua
maximum = max(...)
```

**Arguments:**

- `...` - A list of numbers (`list`)

**Returns:**

- `maximum` - The highest number among all arguments (`number`)

---

## min `luaapi`

Returns the least of a list of numbers. Alias for the standard library function `math.min`.

**Signature:**

```lua
maximum = min(...)
```

**Arguments:**

- `...` - A list of numbers (`list`)

**Returns:**

- `maximum` - The lowest number among all arguments (`number`)

---

## mod `luaapi`

Returns the remainder from division of two numbers. Alias for the standard library function `math.fmod`.

**Signature:**

```lua
remainder = mod(x, y)
```

**Arguments:**

- `x` - A number (`number`)
- `y` - A number (`number`)

**Returns:**

- `remainder` - Remainder of the division of `x` by `y` that rounds the quotient towards zero (`number`)

---

## next `luaapi`

Returns the next key/value pair in a table

**Signature:**

```lua
nextKey, nextValue = next(t [, key])
```

**Arguments:**

- `t` - A table (`table`)
- `key` - A key in the table (`value`)

**Returns:**

- `nextKey` - The next key in the table `t` (`value`)
- `nextValue` - Value associated with the next key in the table `t` (`value`)

---

## pairs `luaapi`

Returns an iterator function for a table. Return values are such that the construction
` for k,v in pairs(t)
 -- body
 end
`

will iterate over all key/value pairs in the table.

**Signature:**

```lua
iterator, t, index = pairs(t)
```

**Arguments:**

- `t` - A table (`table`)

**Returns:**

- `iterator` - The [`next()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/next) function (`function`)
- `t` - The table provided (`table`)
- `index` - Always nil; used internally (`number`)

---

## pcall `luaapi`

Executes a function in protected mode. When running a function in protected mode, any errors do not propagate beyond the function (i.e. they do not stop all execution and call the default error handler).

**Signature:**

```lua
status, ... = pcall(f, ...)
```

**Arguments:**

- `f` - A function (`function`)
- `...` - Arguments to be passed to the function (`list`)

**Returns:**

- `status` - True if the function succeeded without errors; false otherwise (`boolean`)
- `...` - If `status` is `false`, the error message produced by the function; if `status` is `true`, the return values from the function (`list or string`)

---

## rad `luaapi`

Converts an angle specified in degrees to radians. Alias for the standard library function `math.rad`.

**Signature:**

```lua
radians = rad(degrees)
```

**Arguments:**

- `degrees` - An angle specified in degrees (`number`)

**Returns:**

- `radians` - The angle specified in radians (`number`)

---

## random `luaapi`

Generates a pseudo-random number. Alias for the standard library function `math.random`.

**Signature:**

```lua
randomNum = random([m [, n]])
```

**Arguments:**

- `m` - First limit for randomly generated numbers (`number`)
- `n` - Second limit for randomly generated numbers (`number`)

**Returns:**

- `randomNum` - If called without arguments, a uniform pseudo-random real number in the range [0,1); if `m` is specified, a uniform pseudo-random integer in the range [1,m]; if both `m` and `n` are specified, a uniform pseudo-random integer in the range [m,n] (`number`)

---

## rawequal `luaapi`

Returns whether two values are equal without invoking any metamethods

**Signature:**

```lua
isEqual = rawequal(v1, v2)
```

**Arguments:**

- `v1` - Any value (`value`)
- `v2` - Any value (`function`)

**Returns:**

- `isEqual` - True if the values are equal; false otherwise (`boolean`)

---

## rawget `luaapi`

Returns the real value associated with a key in a table without invoking any metamethods

**Signature:**

```lua
value = rawget(t, key)
```

**Arguments:**

- `t` - A table (`table`)
- `key` - A key in the table (`value`)

**Returns:**

- `value` - Value of `t[key]` (`value`)

---

## rawset `luaapi`

Sets the value associated with a key in a table without invoking any metamethods

**Signature:**

```lua
rawset(t, key, value)
```

**Arguments:**

- `t` - A table (`table`)
- `key` - A key in the table (cannot be `nil`) (`value`)
- `value` - New value to set for the key (`value`)

---

## select `luaapi`

Returns one or more values from a list (`...`), or the number of values in a list

**Signature:**

```lua
... = select(index, ...) or select("#", ...)
```

**Arguments:**

- `index` - Index of a value in the list (`number`)
- `#` - The string `"#"` (`string`)
- `...` - A list of values (`list`)

**Returns:**

- `...` - If called with a first argument of `"#"`, the number of values in the list; otherwise, all values in the list starting with the value at position `index` (`list`)

---

## setfenv `luaapi`

Sets the environment to be used by a function. If the environment has a `__environment` metatable, this function will error.

**Signature:**

```lua
f = setfenv([f,] t) or setfenv([stackLevel,] t)
```

**Arguments:**

- `f` - A function (`function`)
- `stackLevel` - Level of a function in the calling stack, or 0 to set the global environment (`number`)
- `t` - A table (`table`)

**Returns:**

- `f` - The input function `f` (`function`)

---

## setmetatable `luaapi`

Sets the metatable for a table

**Signature:**

```lua
t = setmetatable(t, metatable)
```

**Arguments:**

- `t` - A table (`table`)
- `metatable` - A metatable for the table `t`, or nil to remove an existing metatable (`table`)

**Returns:**

- `t` - The input table `t` (`table`)

---

## sort `luaapi`

Sorts a table. Alias for the standard library function `table.sort`.

**Signature:**

```lua
sort(table [, comparator])
```

**Arguments:**

- `table` - A table (`number`)
- `comparator` - A function to compare table elements during the sort; takes two arguments and returns `true` if the first argument should be ordered before the second in the sorted table; equivalent to `function(a,b) return a < b end` if omitted (`function`)

---

## sqrt `luaapi`

Returns the square root of a number. Alias for the standard library function `math.sqrt`.

**Signature:**

```lua
root = sqrt(x)
```

**Arguments:**

- `x` - A number (`number`)

**Returns:**

- `root` - The square root of `x` (`number`)

---

## strbyte `luaapi`

Returns the numeric code for one or more characters in a string. Alias for the standard library function `string.byte`.

**Signature:**

```lua
value, ... = strbyte("s" [, firstChar [, lastChar]])
```

**Arguments:**

- `s` - A string (`string`)
- `firstChar` - Position of a character in the string (can be negative to count backwards from the end of the string); defaults to 1 if omitted (`number`)
- `lastChar` - Position of a later character in the string (can be negative to count backwards from the end of the string); defaults to `firstChar` if omitted (`number`)

**Returns:**

- `value` - Numeric code for the character at position `firstChar` in the string (`number`)
- `...` - A list of numbers, each the numeric codes of additional characters in the string if `lastChar` specifies a position later in the string than `firstChar` (`list`)

---

## strchar `luaapi`

Returns the character(s) for one or more numeric codes. Alias for the standard library function `string.char`.

**Signature:**

```lua
s = strchar(n [, ...])
```

**Arguments:**

- `n` - An integer (`number`)
- `...` - Additional integers (`number`)

**Returns:**

- `s` - A string containing the character(s) for the given numeric code(s) (`number`)

---

## strfind `luaapi`

Returns information about matches for a pattern in a string. Alias for the standard library function `string.find`.

Returns `nil` if no matches are found.

**Signature:**

```lua
start, end, ... = strfind("s", "pattern" [, init [, plain]])
```

**Arguments:**

- `s` - A string (`string`)
- `pattern` - A regular expression pattern (`string`, [pattern](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#pattern))
- `init` - Initial position in the string `s` at which to begin the search; defaults to 1 if omitted (`number`)
- `plain` - True to perform a simple substring search (i.e. considering `pattern` only as a literal string, not a regular expression); false or omitted otherwise (`boolean`)

**Returns:**

- `start` - Character position in `s` at which the first match begins (`number`)
- `end` - Character position in `s` at which the first match ends (`number`)
- `...` - Captured substrings from `s`, if `pattern` specifies captures (`list`)

---

## strlen `luaapi`

Returns the number of characters in a string. Alias for the standard library function `string.len`.

**Signature:**

```lua
length = strlen("s")
```

**Arguments:**

- `s` - A string (`string`)

**Returns:**

- `length` - Number of characters in the string (`number`)

---

## strlower `luaapi`

Returns a copy of a string with all uppercase letters converted to lowercase. Alias for the standard library function `string.lower`

**Signature:**

```lua
lowerCase = strlower("s")
```

**Arguments:**

- `s` - A string (`string`)

**Returns:**

- `lowerCase` - A copy of the string `s` with all uppercase letters converted to lowercase (`string`)

---

## strmatch `luaapi`

Returns the matches for a for a pattern in a string. Alias for the standard library function `string.match`.

**Signature:**

```lua
match, ... = strmatch("s", "pattern")
```

**Arguments:**

- `s` - A string (`string`)
- `pattern` - A regular expression pattern (`string`, [pattern](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api_types#pattern))

**Returns:**

- `match` - First substring of `s` matching `pattern`, or the first capture if `pattern` specifies captures; nil if no match is found (`string`)
- `...` - Additional captures found, if `pattern` specifies multiple captures (`list`)

---

## strrep `luaapi`

Returns a string produced by a number of repetitions of another string. Alias for the standard library function `string.rep`.

**Signature:**

```lua
repeated = strrep("s", n)
```

**Arguments:**

- `s` - A string (`string`)
- `n` - A number (`number`)

**Returns:**

- `repeated` - The concatenation of `n` copies of the string `s` (`string`)

---

## strrev `luaapi`

Returns the reverse of a string. Alias for the standard library function `string.reverse`.

**Signature:**

```lua
s = strrev("s")
```

**Arguments:**

- `s` - A string (`string`)

**Returns:**

- `s` - A string containing the characters of string `s` in reverse order (`string`)

---

## strsub `luaapi`

Returns a substring of a string. Alias for the standard library function `string.sub`.

**Signature:**

```lua
s = strsub("s", firstChar [, lastChar])
```

**Arguments:**

- `s` - A string (`string`)
- `firstChar` - Position of a character in the string (can be negative to count backwards from the end of the string) (`number`)
- `lastChar` - Position of a later character in the string (can be negative to count backwards from the end of the string); defaults to -1 if omitted (`number`)

**Returns:**

- `s` - The substring of `s` starting at the character `firstChar` and ending with the character `lastChar` (`string`)

---

## strupper `luaapi`

Returns a copy of a string with all lowercase letters converted to uppercase. Alias for the standard library function `string.upper`.

**Signature:**

```lua
lowerCase = strupper("str")
```

**Arguments:**

- `str` - A string (`string`)

**Returns:**

- `lowerCase` - A copy of the string `s` with all lowercase letters converted to uppercase (`string`)

---

## time `luaapi`

Returns the numeric time value for a described date/time (or the current time). Alias for the standard library function `os.time`.

According to the Lua manual, the returned value may vary across different systems; however, the Lua libraries included with current WoW clients on both Mac and Windows share the same implementation.

For higher-precision time measurements not convertible to a date, see [`GetTime()`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/GetTime).

**Signature:**

```lua
t = time([timeDesc])
```

**Arguments:**

- `timeDesc` - Table describing a date and time, as returned by [`date("*t")`](https://web.archive.org/web/20100726112636/http://wowprogramming.com/docs/api/date); if omitted, uses the current time (`table`)

**Returns:**

- `t` - Number of seconds elapsed since midnight, January 1, 1970 UTC (`number`)

---

## tinsert `luaapi`

Inserts a value into a table. Alias for the standard library function `table.insert`.

**Signature:**

```lua
tinsert(table [, position] value)
```

**Arguments:**

- `table` - A table (`table`)
- `position` - Index in the table at which to insert the new value; if omitted, defaults to `#table + 1` (`number`)
- `value` - Any value (`value`)

---

## tonumber `luaapi`

Returns the numeric value of a string

**Signature:**

```lua
numValue = tonumber(x [, base])
```

**Arguments:**

- `x` - A string or number (`value`)
- `base` - Base in which to interpret the numeral (integer between 2 and 36); letters 'A-Z' can be used to denote place values 10 or above in bases greater than 10; defaults to 10 if omitted (`number`)

**Returns:**

- `numValue` - Numeric value of `x` in the given base, or nil if the value cannot be converted to a number (`number`)

---

## tostring `luaapi`

Returns a string representation of a value

**Signature:**

```lua
stringValue = tostring(value)
```

**Arguments:**

- `value` - Any value (`value`)

**Returns:**

- `stringValue` - String representation of the given `value` (if `value` is an object with a `__tostring` metamethod, that method is used to produce the string representation) (`string`)

---

## tremove `luaapi`

Removes an element from a table. Alias for the standard library function `table.remove`.

**Signature:**

```lua
tremove(table [, position])
```

**Arguments:**

- `table` - A table (`table`)
- `position` - Index in the table from which to remove the value; if omitted, defaults to `#table` (`number`)

---

## type `luaapi`

Returns a string describing the data type of a value

**Signature:**

```lua
typeString = type(v)
```

**Arguments:**

- `v` - Any value (`value`)

**Returns:**

- `typeString` - A string describing the type of value `v` (`string`)
  - `boolean` - A boolean value (`true` or `false`)
  - `function` - A function
  - `nil` - The special value `nil`
  - `number` - A numeric value
  - `string` - A string
  - `table` - A table
  - `thread` - A coroutine thread
  - `userdata` - Data external to the Lua environment (e.g. the main element of a Frame object)

---

## unpack `luaapi`

Returns the list of elements in a table. Equivalent to 
` return t[i], t[i+1], ... t[j]
`

for an arbitrary number of elements.

**Signature:**

```lua
... = unpack(t [, i [, j]])
```

**Arguments:**

- `t` - A table (`table`)
- `i` - A numeric index to the table; defaults to 1 if omitted (`number`)
- `j` - A numeric index to the table; defaults to `#t` if omitted (`number`)

**Returns:**

- `...` - The list of values in the table between indices `i` and `j` (`list`)

---

## xpcall `luaapi`

Executes a function in protected mode with a custom error handler

**Signature:**

```lua
status, ... = xpcall(f, err)
```

**Arguments:**

- `f` - A function (`function`)
- `err` - Error handler function to be used should `f` cause an error (`function`)

**Returns:**

- `status` - True if the function succeeded without errors; false otherwise (`boolean`)
- `...` - If `status` is `false`, the error message produced by the function; if `status` is `true`, the return values from the function (`list or string`)

---

← [WoW API Docs](../index.md)
