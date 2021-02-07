---
title: 'Replace multiple characters in a string using `string.translate()` (python)'
---
If you need to replace a character in a string, you can use `string.replace(old, new)` or `re.swap(pattern, new, string)` if you need regex.

If you need to replace many characters at once, it can be easier to use the string method `string.translate(table)` which returns a copy of the string in which each character has been mapped through the given translation table. The translation table can be conveniently created from a character to character dict mapping using the `str.maketrans()` method.

See this example from the 2020 Advent of Code [Day 5](https://adventofcode.com/2020/day/5):
```python
chars_to_swap = {'B': '1',
                 'F': '0',
                 'R': '1',
                 'L': '0'}

'BFFFBBFRRR'.translate(str.maketrans(chars_to_swap)
```
returns: `1000110111`