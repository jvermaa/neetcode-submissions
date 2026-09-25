class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()

        l = 0
        max_substring = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1    
            
            visited.add(s[r])
            max_substring = max(max_substring, r-l + 1)
        
        return max_substring