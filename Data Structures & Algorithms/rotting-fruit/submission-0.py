from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh_fruits = 0
        time = 0
        q = deque()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh_fruits > 0:
            
            current_cycle_rotten_fruits = len(q)
            for i in range(current_cycle_rotten_fruits):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append([nr, nc])
                    fresh_fruits -= 1
            time += 1
        
        return time if fresh_fruits == 0 else -1

