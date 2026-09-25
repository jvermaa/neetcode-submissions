class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue


            left = i + 1 # We will check from the array after the 
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            
        return result