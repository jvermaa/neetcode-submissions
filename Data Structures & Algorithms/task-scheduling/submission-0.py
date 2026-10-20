from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq_map = defaultdict(int)

        for t in tasks:
            freq_map[t] += 1
        
        q = deque() # [time+n, frequency]

        h = [-c for c in freq_map.values()]
        heapq.heapify(h)
        
        time = 0

        while h or q:
            
            if q and time == q[0][0]:
                heapq.heappush(h,q.popleft()[1])
            
            if h:
                cnt = heapq.heappop(h) + 1   # ran it once (counts are negative)
                if cnt != 0:
                    q.append((time + n + 1, cnt))


            time +=1
        
        return time


        