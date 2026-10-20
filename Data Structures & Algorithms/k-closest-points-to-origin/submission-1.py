import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        kclosest = [] # Heaps are also initialized like normal arrays, we just use heappush and heappop instead of append and pop, respectively.

        for x,y in points:
            dist_sq = x**2 + y**2
            heapq.heappush(kclosest, (-dist_sq, [x, y]))
        
        size = len(kclosest)

        while size > k:
            heapq.heappop(kclosest)
            size -= 1
        
        return [y for x,y in kclosest]