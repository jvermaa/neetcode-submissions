class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0

        character_set = set()

        for i in range(len(s)):
            while s[i] in character_set:
                character_set.remove(s[left]) # this was the bug last time, I was removing s[i] but left se nikaalna h
                left += 1
            
            character_set.add(s[i])
            res = max(res, i - left + 1 )
        
        return res