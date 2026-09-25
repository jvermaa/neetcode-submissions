# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_nodes = set()
        counter = 0
        while head:
            list_nodes.add(head)
            if head.next in list_nodes:
                return True
            head = head.next
        
        return False