class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_groups = {} # Key: tuple of freq, Val: Word

        for i in strs:
            freq_key = [0]*26 
            for j in i:
                freq_key[ord(j) - ord('a')] += 1
            freq_key = tuple(freq_key)
            
            if freq_key not in final_groups:
                final_groups[freq_key] = []

            final_groups[freq_key].append(i)
        
        return list(final_groups.values())
