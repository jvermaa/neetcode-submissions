# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0 # diameter at a node is basicall max(left) + max(right)

        def dfs(node):

            nonlocal max_diameter

            if not node:
                return 0
            
            left =  dfs(node.left)
            right = dfs(node.right)

            diameter_of_current_node = left + right
            max_diameter = max(max_diameter, diameter_of_current_node)

            return 1 + max(left, right)
        
        dfs(root)
        return max_diameter

