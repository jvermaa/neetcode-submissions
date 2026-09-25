class Solution:
    def climbStairs(self, n: int) -> int:
        
        visited = [0] * (n+1)

        if n <= 2:
            return n
            
        visited[0] = 1
        visited[1] = 1
        for i in range(2, n+1):
            visited[i] = visited[i-1] + visited[i-2]
            
        return visited[n]
            