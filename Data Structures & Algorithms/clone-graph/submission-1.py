"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        already_cloned = {} # We will map old nodes to new so in case
                            # we reach to one of the old nodes again through
                            # connection, we will just use it instead of
                            # remaking the node

        def dfs(node): # Takes a node to copy one

            # Base Case: Have we already cloned this node?
            if node in already_cloned:
                return already_cloned[node]
            
            # if it is not
            # Then create a new node
            copy = Node(node.val)

            # Then log it
            already_cloned[node] = copy

            # Then explore the neighbours
            for i in node.neighbors:
                n = dfs(i)
                copy.neighbors.append(n)
            
            return copy
        
        return dfs(node)

