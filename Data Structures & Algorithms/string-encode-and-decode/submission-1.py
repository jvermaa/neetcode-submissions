# Even though I am getting all the testcases right
# I should do it again because I am missing some things
# Get back to it and remember what you were missing 

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
