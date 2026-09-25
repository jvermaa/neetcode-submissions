# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = new_head = ListNode()
        pointer_1 = list1
        pointer_2 = list2

        while pointer_1 and pointer_2:
            if pointer_1.val < pointer_2.val:
                new_head.next = pointer_1
                new_head = new_head.next
                pointer_1 = pointer_1.next
            else:
                new_head.next = pointer_2
                new_head = new_head.next
                pointer_2 = pointer_2.next

        new_head.next = pointer_1 or pointer_2

        return dum.next