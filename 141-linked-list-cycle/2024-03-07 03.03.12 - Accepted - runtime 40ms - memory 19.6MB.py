# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = set()
        while head:
            if head in vis:
                return True
            vis.add(head)
            head = head.next
        return False