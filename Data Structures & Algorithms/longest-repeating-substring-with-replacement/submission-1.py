class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxf = 0
        char_dict = {key: 0 for key in range(26)}
        while r < len(s):
            char_dict[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, char_dict[ord(s[r]) - ord('A')])
            if (r-l+1) - maxf > k:
                char_dict[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        
        return r - l

        
