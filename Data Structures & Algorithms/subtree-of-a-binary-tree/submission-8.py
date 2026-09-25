# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot: # This checks if one is not null and the other one is so def cant be the same tree
            return False
        if not subRoot and root:
            return False
        if root.val != subRoot.val:
            return False
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False # Because if the root is Null then how can it have a subtree
        
        # Assuming the subtree starts from the root of the tree
        if self.sameTree(root, subRoot):
            return True
        
        # Now giving multiple conditions like if the subTree starts from the left node of the root tree or the right node of the root tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)