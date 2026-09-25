'''
My OG solution
Problems with it:
    . Missed the edge case to check both strings need to be the
      same size atleast in order to return True
    . I used a set but I should have used map/dictionaries because
      set cannot count the frequency of these letters. So my code
      will say True for "aatt" and "at" using sets

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper = set()
        for i in s:
            mapper.add(i)

        for i in t:
            if i not in mapper:
                return False
        
        return True
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]] += 1
            else:
                map_s[s[i]] = 1
            
            if t[i] in map_t:
                map_t[t[i]] += 1
            else:
                map_t[t[i]] = 1

        return map_s == map_t