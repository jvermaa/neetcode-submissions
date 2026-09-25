class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxxxx = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            maxxxx = max(curr_sum, maxxxx)
        return maxxxx