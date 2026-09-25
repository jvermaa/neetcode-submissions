class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets_of_nums = set(nums)
        longest_sequence = 0
        for n in sets_of_nums:
            if (n-1) not in sets_of_nums:
                longer = 1
                while (n+longer) in sets_of_nums:
                    longer += 1
                longest_sequence = max(longest_sequence, longer)
        
        return longest_sequence