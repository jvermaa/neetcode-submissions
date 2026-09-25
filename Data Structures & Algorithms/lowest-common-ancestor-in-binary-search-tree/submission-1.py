# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current_node = root

        while current_node:
            if current_node.val < p.val and current_node.val < q.val:
                current_node = current_node.right
            elif current_node.val > p.val and current_node.val > q.val:
                current_node = current_node.left
            else:
                return current_node