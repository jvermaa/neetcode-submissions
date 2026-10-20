import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # O(n.log(n)) solution 
        
        # heapq.heapify(nums)

        # size = len(nums)

        # while size > k:
        #     heapq.heappop(nums)
        #     size -= 1
        
        # return nums[0]

        # O(n.log(k)) solution

        newH = []

        for n in nums:
            heapq.heappush(newH, n)
            size = len(newH)
            if size > k:
                heapq.heappop(newH)
        
        return newH[0]