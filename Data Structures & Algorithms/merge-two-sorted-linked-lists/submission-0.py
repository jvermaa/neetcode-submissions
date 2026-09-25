# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummyNode = ListNode() # We are doing this to intialize a node so we can move through it as the tail
        l1 = list1
        l2 = list2
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next # BEcause now we will attach the value to the next element. DOnt confuse tail with always being the first element from left. Tail is the first element from the right
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummyNode.next
