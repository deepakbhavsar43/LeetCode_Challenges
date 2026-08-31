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

        