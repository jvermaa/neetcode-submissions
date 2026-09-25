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

            if not node: # If we are at the leaf node, the height will be 0
                return 0
            
            left =  dfs(node.left) # calculate the height of left subtree
            right = dfs(node.right) # calculate the height of right subtree

            diameter_of_current_node = left + right 
            max_diameter = max(max_diameter, diameter_of_current_node) # Check whether the previous dia was max or the current node has the max dia

            return 1 + max(left, right) # return the height of the tree so that other nodes can calculate dias from their nodes
        
        dfs(root)
        return max_diameter

