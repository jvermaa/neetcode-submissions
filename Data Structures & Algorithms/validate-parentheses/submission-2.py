class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapper = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in mapper:
                if stk and stk[-1] == mapper[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        
        if not stk:
            return True
        return False

