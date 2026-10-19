class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(set)
        visited_set = set()

        for p,c in edges:
            adj[p].add(c)
            adj[c].add(p)

        def dfs(node, prev):

            if node in visited_set:
                return False
            
            visited_set.add(node)
            
            for nodes in adj[node]:
                if nodes in visited_set and nodes != prev:
                    return False
                dfs(nodes, node)
            
            return True 

        return dfs(0, -1) and len(visited_set) == n