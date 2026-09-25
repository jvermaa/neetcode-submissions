class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {} # Key = (r,c) val = LIP
        ROWS = len(matrix)
        COLS = len(matrix[0])

        def dfs(r,c, prev):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0

            if matrix[r][c] <= prev:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]       

            current_val = matrix[r][c]
            cache[(r,c)] = 1 + max(dfs(r+1, c, current_val), dfs(r-1, c, current_val), dfs(r, c+1, current_val), dfs(r, c-1, current_val))

            return cache[(r,c)]

        bigest = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                bigest= max(bigest, dfs(r,c,-1))

        return bigest
