# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = starter = ListNode()
        l1_pointer = list1
        l2_pointer = list2

        while l1_pointer and l2_pointer:
            if l1_pointer.val < l2_pointer.val:
                tail.next = l1_pointer
                l1_pointer = l1_pointer.next
            else:
                tail.next = l2_pointer
                l2_pointer = l2_pointer.next
            tail = tail.next
        
        if l1_pointer:
            tail.next = l1_pointer
        
        if l2_pointer:
            tail.next = l2_pointer
        
        return starter.next
