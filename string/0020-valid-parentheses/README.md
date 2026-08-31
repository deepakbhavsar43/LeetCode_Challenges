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
        open_brackets=['(', '{', '[']
        close_brackets = {')':'(', '}':'{', ']':'['}

        result=[]
        for ch in s:
            if ch in open_brackets:
                result.append(ch)
            elif (ch in close_brackets) and result == []:
                return False
            else:
                if result:
                    del_ch = result.pop()
                    if del_ch != close_brackets[ch]:
                        return False
            # print("ch: ", ch)
            # print("result: ", result)
                
        if result:
            return False
        else:
            return True

```

*Runtime: 0 ms · Memory: 19.2 MB*

