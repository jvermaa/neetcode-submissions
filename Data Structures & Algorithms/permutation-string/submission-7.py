class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        k = len(s1)
        s1_map = {}
        s2_map = {}
            
        for i in range(k):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        if s1_map == s2_map:
            return True
        
        for i in range(k, len(s2)):
            # first we add the new letter in the place
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

            # Remove the previous one. AKA Move the window right
            s2_map[s2[i-k]] -= 1

            if s2_map[s2[i-k]] == 0:
                del s2_map[s2[i-k]]
            
            if s1_map == s2_map:
                return True
        
        return False
        
