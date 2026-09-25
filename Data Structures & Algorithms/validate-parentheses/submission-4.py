class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        inserters = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i == '(' or i == '{' or i == "[":
                stk.append(i)
            else:
                if len(stk) == 0 or stk.pop() != inserters[i]:
                    return False
        
        if len(stk) == 0:
            return True
        return False