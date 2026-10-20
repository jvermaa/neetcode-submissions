import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        size = len(nums)

        while size > k:
            heapq.heappop(nums)
            size -= 1
        
        return nums[0]