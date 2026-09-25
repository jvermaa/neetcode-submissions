class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest_seq = 0

        for n in nums:
            if n-1 in nums:
                continue
            
            current_seq = 0
            while n+current_seq in nums:
                current_seq += 1
            
            longest_seq = max(longest_seq, current_seq)
        
        return longest_seq