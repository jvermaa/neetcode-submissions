# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            n = len(queue)
            for i in range(n):
                a = queue.popleft()
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
                if i == n-1:
                    result.append(a.val)
        
        return result