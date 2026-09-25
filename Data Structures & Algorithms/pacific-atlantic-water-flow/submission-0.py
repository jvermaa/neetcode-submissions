class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        flows_atlantic = set()
        flows_pacific = set()

        result = []
        def dfs(r,c, flow_set, prev_height):
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in flow_set or heights[r][c] < prev_height:
                return 
            
            flow_set.add((r,c))
            dfs(r+1, c, flow_set, heights[r][c])
            dfs(r-1, c, flow_set, heights[r][c])
            dfs(r, c+1, flow_set, heights[r][c])
            dfs(r, c-1, flow_set, heights[r][c])

        
        for c in range(COLS):
            dfs(0, c, flows_pacific, -1)
            dfs(ROWS-1, c, flows_atlantic, -1)

        for r in range(ROWS):
            dfs(r, 0, flows_pacific, -1)
            dfs(r, COLS-1, flows_atlantic, -1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in flows_atlantic and (r,c) in flows_pacific:
                    result.append([r,c])
        
        return result
                    
