# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def validator(lower_limit: int, upper_limit: int, node: TreeNode) -> bool:
            if not node:
                return True
            
            if node.val <= lower_limit or node.val >= upper_limit:
                return False
            
            return validator(lower_limit, node.val, node.left) and validator(node.val, upper_limit, node.right)
        
        return validator(float('-inf'), float('inf'), root)