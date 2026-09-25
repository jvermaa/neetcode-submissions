# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        final_a = True
        final_b = True
        final_c = True
        final_d = True

        # Case where both are None, so they are the same
        if not p and not q:
            return True
        
        # If one is None and the other is not, they are not the same
        if not p or not q:
            return False
        
        # Check if the values are not equal
        if p.val != q.val:
            final_d = False
        
        # Recursively check left subtrees
        if p.left or q.left:
            final_a = self.isSameTree(p.left, q.left)
        
        # Recursively check right subtrees
        if p.right or q.right:
            final_b = self.isSameTree(p.right, q.right)

        # Combine the results: return True if all conditions are met
        return final_a and final_b and final_c and final_d
