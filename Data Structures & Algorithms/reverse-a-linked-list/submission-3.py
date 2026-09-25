# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_pointer = None # We assume that there is no pointer behind the first node so it will null by default when you reverse the linkedList
        current_pointer = head # Starting from the fist one

        while current_pointer: # basically we are turning the face of the next pointer of the currentpointer to point to the previous pointer and then incrementing both previous and next by 1
            temp = current_pointer.next
            current_pointer.next = previous_pointer
            previous_pointer = current_pointer
            current_pointer = temp
        
        return previous_pointer # By the time the algo reaches its end, the current pointer will be pointing to null and the previous pointer will be pointing to the last node

