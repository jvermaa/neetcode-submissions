# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()
        queue.append(root)
        resultant = []

        while queue:
            n = len(queue)
            lower_res = []
            for i in range(n):
                a = queue.popleft()
                lower_res.append(a.val)

                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)

            resultant.append(lower_res)
        
        return resultant