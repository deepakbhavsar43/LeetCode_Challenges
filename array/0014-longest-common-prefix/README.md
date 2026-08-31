# 14. Longest Common Prefix

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/longest-common-prefix/

**Topics:** Array, String, Trie

## Problem

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
**Input:** strs = ["flower","flow","flight"]
**Output:** "fl"
```

**Example 2:**

```
**Input:** strs = ["dog","racecar","car"]
**Output:** ""
**Explanation:** There is no common prefix among the input strings.
```

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Solution (python3)

```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ref = strs[0]   
        n = len(ref)
        for i in range(n):
            for j in strs:
                if i == len(j) or j[i] != ref[i]:
                    return ref[:i]

        return ref

        
```

*Runtime: 1 ms · Memory: 19.1 MB*

