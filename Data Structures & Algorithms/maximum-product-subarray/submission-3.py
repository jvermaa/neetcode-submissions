class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        resultant = max(nums)
        current_min = 1
        current_max = 1

        for n in nums:

            if n == 0:
                current_min = 1
                current_max = 1
                continue 

            tempo = current_max * n
            current_max = max(n, current_max * n, current_min * n) # n because what if n alone is greater than the multiple of predecessors, then the current_max * n will become the new current_max if the n is positive, if n is negative then current_min * n will become the new max
            current_min = min(n, tempo, n * current_min)
            resultant = max(resultant, current_max) #since we need to return the max product subarray
        return resultant