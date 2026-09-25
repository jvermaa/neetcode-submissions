class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0

        def dfs(row, col):

            # base case: 0 or out of bounds
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return

            # 0 is the mark of visited
            # So the main if condition in the 2x for loop
            # Does not get passed for an island

            grid[row][col] = "0"

            # Run a DFS in all 4 direction with the goal to mark all 1s as 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    count += 1
        
        return count
