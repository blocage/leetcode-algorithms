# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head)
            head = head.next
        for i in range(len(l) - 1):
            l[~i].next = l[~i - 1]
        if l:
            l[0].next = None
            return l[-1]
        
        return None