# Solution is working but it still has logic flaws
# Something is wrong with the usage of mini
# Check under your if and else way of moving the pointers.
# Cuz even tho it is working, it is not the right way to do it

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        global_min = 10000000
        while l < r:
            mid = (l + r)//2

            if nums[mid] < global_min:
                global_min = nums[mid]
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return min(global_min, nums[r])