class Solution:
    def isValid(self, s: str) -> bool:
        sack = []

        dict_map = {")":"(", ']':'[', '}':'{'}
        for i in s:
            if i in dict_map and len(sack) != 0:
                current = sack.pop()
                if current != dict_map[i]:
                    return False
            else:
                sack.append(i)
        
        return len(sack) == 0

        