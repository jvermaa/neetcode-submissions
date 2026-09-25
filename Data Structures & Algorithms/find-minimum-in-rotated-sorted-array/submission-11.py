class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1
        global_min = float('inf')

        while left <= right:
            mid = (left+right)//2

            global_min = min(global_min, nums[mid], nums[left], nums[right])

            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        
        return global_min