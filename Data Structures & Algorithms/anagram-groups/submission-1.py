class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}

        for i in strs:
            key = [0]*26
            for character in i:
                key[ord(character)-ord('a')] += 1
            
            if tuple(key) in mapper:
                mapper[tuple(key)].append(i)
            else:
                mapper[tuple(key)] = [i]
        
        return mapper.values()
                    