# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_elements = 0
        iteration_first = head
        
        while iteration_first:
            total_elements += 1
            iteration_first = iteration_first.next
        
        index = total_elements - n

        if index == 0:
            return head.next
            
        prev = None
        target = head
        for i in range(0, index):
            prev = target
            target = target.next
        
        prev.next = target.next
        target.next = None

        return head
