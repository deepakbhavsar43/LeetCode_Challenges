class Solution:
    def isValid(self, s: str) -> bool:
        # demo LeetSync
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
