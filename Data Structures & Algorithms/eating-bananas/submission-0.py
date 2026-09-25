class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        global_h = float('inf')


        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            current_h = 0

            for p in piles:
                current_h += math.ceil(p/mid)
            
            if current_h <= h:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
            