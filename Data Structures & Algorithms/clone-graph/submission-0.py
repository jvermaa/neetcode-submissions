"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapper = {}
        def depth_first_search(node):
            if node in mapper:
                return mapper[node]
            
            copy = Node(node.val)
            mapper[node] = copy

            for i in node.neighbors:
                copy.neighbors.append(depth_first_search(i))
            
            return copy
        
        if node:
            return depth_first_search(node)
        else:
            None