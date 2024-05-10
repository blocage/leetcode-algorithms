# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        r = 0
        while head:
            l.append(head)
            head = head.next
            r += 1
        return l[r // 2]