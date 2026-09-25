class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for s in strs:
            encoded_list.append(str(len(s)))
            encoded_list.append("%") # Delimiter
            encoded_list.append(s)
        
        return ''.join(encoded_list)

    def decode(self, s: str) -> List[str]:
        result = []
        p = 0
        i = 0
        while i < len(s):
            j = s.index("%", i)
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return result
