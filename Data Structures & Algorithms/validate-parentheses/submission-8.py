class Solution:
    def isValid(self, s: str) -> bool:
         
        sack = []

        mapper = {"}":"{", "]":"[", ")":"("}

        for i in s:
            if i in mapper and sack:
                curr = sack.pop()
                if mapper[i] != curr:
                    return False
            else:
                sack.append(i)
        
        return len(sack) == 0

            
