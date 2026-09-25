# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 3 step problem. 
        #   First split the list
        #   Reverse the second half
        #   Relink them

        # These lines help find the middle point
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now we will reverse it
        second_half = slow.next
        prev = None
        slow.next = None # This breaks the link between the first and the second half of the list.
        
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        #This part will merge both of them
        start = head
        start_2 = prev # So the second_half would become None by the end of the loop so prev would be the head of the second half
        
        while start_2:
            tmp1 = start.next
            tmp2 = start_2.next
            start.next = start_2
            start_2.next = tmp1
            start = tmp1
            start_2 = tmp2

