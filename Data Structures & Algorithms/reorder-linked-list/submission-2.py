# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start_2nd = slow.next # start of the second list

        prev = slow.next = None
        # Reverse the 2nd half of the linkedList
        while start_2nd:
            temp = start_2nd.next
            start_2nd.next = prev
            prev = start_2nd
            start_2nd = temp
        
        # Merge the two linked Lists

        first_list = head
        second_list = prev

        while second_list:
            temp_first = first_list.next
            temp_second = second_list.next

            first_list.next = second_list
            second_list.next = temp_first

            first_list = temp_first
            second_list = temp_second

    

