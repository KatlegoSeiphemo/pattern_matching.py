# Regular Expression Matching in Python

This project implements regular expression matching with support for `.` and `*`. The solution determines whether a given pattern matches the entire input string.

## Problem Description

Given an input string `s` and a pattern `p`, implement a function that returns whether `s` matches `p` where:

- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.

The matching should **cover the entire input string**, not partial matches.

### Examples

```python
Input: s = "aa", p = "a"
Output: False

Input: s = "aa", p = "a*"
Output: True

Input: s = "ab", p = ".*"
Output: True

Input: s = "mississippi", p = "mis*is*p*."
Output: False
