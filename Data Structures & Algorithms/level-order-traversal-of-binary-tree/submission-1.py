# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            current_level = []
            current_size = len(q)

            for i in range(current_size):
                current_node = q.popleft()
                if current_node:
                    if current_node.left:
                        q.append(current_node.left)
                    if current_node.right:
                        q.append(current_node.right)
                    current_level.append(current_node.val)
            
            if current_level != []:
                result.append(current_level)

        return result