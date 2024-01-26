# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            if hasattr(head, 'visited'):
                return head
            head.visited = True
            head = head.next
        return None