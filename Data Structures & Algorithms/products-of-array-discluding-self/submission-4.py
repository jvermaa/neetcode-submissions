class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]* n
        left = 1
        # product with everything on its left
        for i in range(n):
            result[i] = left
            left *= nums[i]

        # product with everything on its right
        right = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result 

        