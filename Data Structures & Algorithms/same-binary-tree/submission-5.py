# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = []
        stack_q = [] 

        def dfs(node, stack):
            if not node:
                stack.append(None)
                return
            
            stack.append(node.val)
            dfs(node.left, stack)
            dfs(node.right, stack)
        
        dfs(p, stack_p)
        dfs(q, stack_q)

        if len(stack_p) != len(stack_q):
            return False
        for i in range(len(stack_p)):
            if stack_p[i] != stack_q[i]:
                return False
            
        return True