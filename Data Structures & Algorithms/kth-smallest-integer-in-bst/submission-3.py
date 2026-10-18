# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = 0
        def dfs(node):
            nonlocal count
            nonlocal res
            if not node:
                return None
            
            dfs(node.left)
            if count >= k: return
            count += 1
            if count == k:
                res = node.val
            
            dfs(node.right)            
            return res

        dfs(root)
        return res