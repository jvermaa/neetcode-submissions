class Solution:

    def encode(self, strs: List[str]) -> str:
        # easy approach would be to just add a delimeter but the problem isthat
        # if a string has special characters then it will be cooked
        # Delimeter + Range to parse 
        # Format: <Delimiter><Range><Delimiter's Delimiter>
        resultant = []

        for s in strs:
            a = str(len(s)) + "%"
            resultant.append(a)
            resultant.append(s)
        return ''.join(resultant)

    def decode(self, s: str) -> List[str]:
        prev_ptr = 0
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1
            n = int(s[i:j])          # parse the numeric length
            result.append(s[j+1:j+1+n])  # extract exactly n characters
            i = j + 1 + n            # move past the extracted string
        return result