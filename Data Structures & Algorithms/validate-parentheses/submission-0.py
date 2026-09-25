class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {']':'[', ')':'(', '}':'{'}
        opening = {'(','[','{'}
        stk = []
        
        for br in s:
            if br in opening:
                stk.append(br)
            else:
                if stk and stk[-1] == mapper[br]:
                    stk.pop()
                else:
                    return False
        return not stk