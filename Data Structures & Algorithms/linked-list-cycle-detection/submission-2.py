# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# My solution works but it takes O(n) space Complexity
# Redo it using Floyd's Tortoise and Hare algorithm
# Hint 2: Use slow and fast pointer
# Hint 3: If it is a cycle, both pointers will meet each other at some point
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False