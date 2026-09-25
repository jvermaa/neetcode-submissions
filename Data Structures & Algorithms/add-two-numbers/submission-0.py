# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        p1 = l1
        p2 = l2

        rr = returnal = ListNode()

        while p1 and p2:
            ssum = p1.val + p2.val + carry

            carry = (ssum) // 10

            returnal.next = ListNode(ssum%10)
            returnal = returnal.next

            p1 = p1.next
            p2 = p2.next
        
        while p1:
            ssum = p1.val + carry
            carry = ssum//10
            returnal.next = ListNode(ssum%10)
            returnal = returnal.next
            p1 = p1.next
        
        while p2:
            ssum = p2.val + carry
            carry = ssum//10
            returnal.next = ListNode(ssum%10)
            returnal = returnal.next
            p2 = p2.next
        
        if carry != 0:
            returnal.next = ListNode(carry)
            returnal = returnal.next
            carry = 0
        
        return rr.next

