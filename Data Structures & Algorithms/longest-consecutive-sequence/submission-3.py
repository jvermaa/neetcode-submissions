class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_to_sets = set(nums)
        longest_seq = 0

        for n in nums:
            current_seq = 0
            if (n - 1) not in nums_to_sets:
                while (n+current_seq) in nums_to_sets:
                    current_seq += 1

                longest_seq = max(longest_seq, current_seq)
        
        return longest_seq