class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            # 1. Check if left child already signaled failure
            if left_height == -1: return -1
            
            right_height = dfs(node.right)
            # 2. Check if right child already signaled failure
            if right_height == -1: return -1
            
            # 3. Check current node balance
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
            
        return dfs(root) != -1