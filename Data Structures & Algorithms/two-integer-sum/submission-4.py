class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differencer = {}

        for index, num in enumerate(nums):
            if target-num in differencer:
                return [differencer[target-num], index]
            differencer[num] = index
        
        return [-1,-1]