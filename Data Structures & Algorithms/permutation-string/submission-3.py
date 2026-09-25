class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):  # Edge case
            return False
            
        k = len(s1)
        s1_freq_map = {}
        for char in s1:
            s1_freq_map[char] = s1_freq_map.get(char, 0) + 1
        
        # Check first window
        s2_freq_map = {}
        for j in range(k):
            s2_freq_map[s2[j]] = s2_freq_map.get(s2[j], 0) + 1
        if s1_freq_map == s2_freq_map:
            return True
        
        # Slide window
        for i in range(k, len(s2)):
            substring = s2[i-k+1:i+1]  # ← Fixed slice
            s2_freq_map = {}
            for j in range(k):
                s2_freq_map[substring[j]] = s2_freq_map.get(substring[j], 0) + 1  # ← Fixed lookup
            if s1_freq_map == s2_freq_map:
                return True
        return False