class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets=['(', '{', '[']
        close_brackets = {')':'(', '}':'{', ']':'['}

        stack=[]
        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            elif (ch in close_brackets) and stack == []:
                return False
            else:
                if stack:
                    del_ch = stack.pop()
                    if del_ch != close_brackets[ch]:
                        return False

        return len(stack)==0
