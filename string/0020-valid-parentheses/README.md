# 20. Valid Parentheses

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/valid-parentheses/

**Topics:** String, Stack, Bracket Sequences

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()[]{}"

**Output:** true

**Example 3:**

**Input:** s = "(]"

**Output:** false

**Example 4:**

**Input:** s = "([])"

**Output:** true

**Example 5:**

**Input:** s = "([)]"

**Output:** false

**Constraints:**

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Solution (python3)

```py
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {')':'(', '}':'{', ']':'['}

        stack=[]
        for ch in s:
            if ch in bracket_mapping:
                top_element = stack.pop() if stack else '#'
                if bracket_mapping[ch] != top_element:
                    return False
            else:
                stack.append(ch)
        
        return not stack

```

*Runtime: 0 ms · Memory: 19.3 MB*

