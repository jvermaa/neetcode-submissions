"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        deepMap = {}
        curr = head

        while curr:
            deepMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            deepMap[curr].next = deepMap.get(curr.next)
            deepMap[curr].random = deepMap.get(curr.random)
            curr = curr.next

        return deepMap[head]