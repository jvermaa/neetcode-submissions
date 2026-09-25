class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map_of_all_characters = {key: 0 for key in range(26)} # want it to start with 0 default value for all

        left_pointer = 0
        max_frequency = 0

        for right_pointer in range(len(s)):
            map_of_all_characters[ord(s[right_pointer]) - ord('A')] += 1
            max_frequency = max(max_frequency, map_of_all_characters[ord(s[right_pointer]) - ord('A')])

            if right_pointer - left_pointer - max_frequency + 1 > k:
                map_of_all_characters[ord(s[left_pointer]) - ord('A')] -= 1
                left_pointer += 1
        
        return right_pointer - left_pointer + 1
            

        
