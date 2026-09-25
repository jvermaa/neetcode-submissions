class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestRepeating = 0
        maxf = 0
        l = 0

        freq_map = {}

        for i, v in enumerate(s):
            if v in freq_map:
                freq_map[v] += 1
            else:
                freq_map[v] = 1
            
            maxf = max(maxf, freq_map[v])

            window_length = i - l + 1

            if window_length - maxf > k:
                freq_map[s[l]] -= 1
                l += 1
            
            longestRepeating = max(longestRepeating,  i - l + 1)
        
        return longestRepeating
