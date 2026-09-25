class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(grid: List[List[str]], row, col):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            queue = collections.deque()
            queue.append((row, col))
            visited_indeces.add((row,col))

            while queue:
                curr_row, curr_col = queue.popleft()

                for dr, dc in (directions):
                    r = curr_row + dr
                    c = curr_col + dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r,c) not in visited_indeces:
                        queue.append((r,c))
                        visited_indeces.add((r,c))

        num_islands = 0
        visited_indeces = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited_indeces:
                    num_islands += 1
                    bfs(grid, r, c)
                    
        return num_islands