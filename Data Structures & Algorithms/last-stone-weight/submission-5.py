class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            collA = heapq.heappop(stones)
            collB = heapq.heappop(stones)

            if collB > collA:
                heapq.heappush(stones, collA-collB)
            
        stones.append(0)
        return abs(stones[0])