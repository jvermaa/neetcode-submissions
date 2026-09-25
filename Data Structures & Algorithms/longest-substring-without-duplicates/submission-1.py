class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        testsetter = set()
        l = 0 # Having this left pointer to slide the window I guess so that we can pretend to be removing the leftmost element?
        res = 0 # Assuming the smallest length to be 0
        for right_pointer in range(len(s)): # Because we wanna go through each element in the list
            # We need to implement the method that will kick out the duplicate elements

            while s[right_pointer] in testsetter:
                testsetter.remove(s[l])
                l += 1

            testsetter.add(s[right_pointer])
            res = max(res, right_pointer-l + 1)
        return res
