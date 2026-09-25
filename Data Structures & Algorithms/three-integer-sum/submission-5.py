class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)
        result = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            

            second,third = first + 1, len(nums)-1
            #target = 0 - nums[first]
            while second < third:
                if nums[first] + nums[second] + nums[third] > 0:
                    third -=1
                elif nums[first] + nums[second] + nums[third] < 0:
                    second += 1
                else:
                    result.append([nums[first], nums[second], nums[third]])
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
                

        return result