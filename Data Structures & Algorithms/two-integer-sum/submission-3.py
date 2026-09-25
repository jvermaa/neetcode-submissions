class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cum_dump = {}

        for index, value in enumerate(nums):
            if target - value in cum_dump:
                return [cum_dump[target-value], index]
            cum_dump[value]  = index
        
