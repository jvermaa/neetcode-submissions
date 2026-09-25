class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency_mapper =defaultdict(list) # Key = Tuple of frequency, Val = word from the list

        for s in strs:
            current_key = [0]*27
            for c in s:
                current_key[97-ord(c)] += 1
            frequency_mapper[tuple(current_key)].append(s)
        
        return list(frequency_mapper.values())
