class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_map = {}
        for i in s1:
            s1_map[i] = s1_map.get(i, 0) + 1
        
        s2_map = {}
        k = len(s1)

        for i in range(k):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1


        if s1_map == s2_map:
            return True
        
        for i in range(k, len(s2)):
            current_substr = s2[i-k+1:i+1]

            local_s2_map = {}

            for j in current_substr:
                local_s2_map[j] = local_s2_map.get(j, 0) + 1
            
            if s1_map == local_s2_map:
                return True
        
        return False
        
