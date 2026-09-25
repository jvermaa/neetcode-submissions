class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map_s = defaultdict(int)
        freq_map_t = defaultdict(int)

        for i in s:
            freq_map_s[i] += 1
        for i in t:
            freq_map_t[i] += 1
        
        return freq_map_s == freq_map_t