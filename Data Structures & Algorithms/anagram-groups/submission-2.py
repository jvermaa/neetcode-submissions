class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = defaultdict(list)

        for word in strs:
            character_key = [0] *26

            for chars in word:
                character_key[ord(chars) - ord("a")] += 1
            
            result_map[tuple(character_key)].append(word)
        
        return list(result_map.values())