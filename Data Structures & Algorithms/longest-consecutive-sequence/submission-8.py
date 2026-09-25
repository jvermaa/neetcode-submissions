class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in numSet:
                current_length = 1
                while (n+current_length) in numSet:
                    current_length += 1
                longest = max(longest, current_length)
        
        return longest