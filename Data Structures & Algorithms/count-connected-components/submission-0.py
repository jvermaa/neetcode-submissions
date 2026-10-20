class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(set)

        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)

        count = 0
        visited = set()

        def dfs(node):
            
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count 