# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False

        def sameTree(node, subNode):

            if not node and not subNode:
                return True
            if not node or not subNode or node.val != subNode.val:
                return False
            
            return sameTree(node.left, subNode.left) and sameTree(node.right, subNode.right)
        

        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)