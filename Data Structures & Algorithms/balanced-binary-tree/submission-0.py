# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True

        def dfs(node):
            nonlocal isBal

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            height_diff = abs(left - right)
            if height_diff > 1:
                isBal = False
            
            return 1 + max(left,right)
        
        dfs(root)
        return isBal