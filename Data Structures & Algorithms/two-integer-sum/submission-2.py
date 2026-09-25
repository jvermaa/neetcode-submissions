class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_difference = {}

        for i in range(len(nums)):
            if target - nums[i] in map_difference:
                return [map_difference[target - nums[i]], i]
            map_difference[nums[i]] = i
