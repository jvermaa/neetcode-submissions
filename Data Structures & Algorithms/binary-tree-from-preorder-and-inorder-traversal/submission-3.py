# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        idx = {value:index for index, value in enumerate(inorder)}
        i = 0

        def recursive(left_index_inorder, right_index_inorder):
            nonlocal i

            if left_index_inorder > right_index_inorder:
                return None
                
            root = TreeNode(preorder[i])
            i += 1
            separator_index = idx[root.val]
            root.left = recursive(left_index_inorder,separator_index-1)
            root.right = recursive(separator_index+1, right_index_inorder)

            return root
        
        return recursive(0, len(inorder)-1)
