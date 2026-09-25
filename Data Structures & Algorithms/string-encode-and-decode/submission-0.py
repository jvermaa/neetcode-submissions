class Solution:

    def encode(self, strs: List[str]) -> str:
        returnal = ""
        for i in strs:
            returnal += i+"|"
        
        return returnal

    def decode(self, s: str) -> List[str]:
        returnal = []
        prev = 0
        for i in range(len(s)):
            if s[i] == "|":
                returnal.append(s[prev:i])
                prev = i+1
        
        return returnal
