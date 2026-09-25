# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_k = 0
        stack = []
        curr = root

        while curr or stack: # we have this cuz in case curr is None but the stack is not empty
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            current_k += 1
            if current_k == k:
                return curr.val
            
            curr = curr.right