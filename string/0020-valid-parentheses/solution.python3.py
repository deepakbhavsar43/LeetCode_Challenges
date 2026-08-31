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
