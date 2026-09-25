# Even though I am getting all the testcases right
# I should do it again because I am missing some things
# Get back to it and remember what you were missing 

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         returnal = ""
#         for i in strs:
#             returnal += i + "|"
        
#         return returnal

#     def decode(self, s: str) -> List[str]:
#         returnal = []
#         prev = 0
#         for i in range(len(s)):
#             if s[i] == "|":
#                 returnal.append(s[prev:i])
#                 prev = i+1
#         return returnal



class Solution:

    def encode(self, strs: List[str]) -> str:
        # This method converts the list of strings into a single string with lengths and "|" as delimiters
        returnal = ""
        for i in strs:
            returnal += str(len(i)) + "|" + i
        return returnal

    def decode(self, s: str) -> List[str]:
        returnal = []
        i = 0
        while i < len(s):
            # First, we find the length of the string (until we hit the "|")
            j = i
            while s[j] != "|":
                j += 1
            # Extract the length of the string
            length = int(s[i:j])
            # Move past the "|" and extract the string of the given length
            returnal.append(s[j + 1: j + 1 + length])
            # Update the index to move to the next encoded string
            i = j + 1 + length
        return returnal

