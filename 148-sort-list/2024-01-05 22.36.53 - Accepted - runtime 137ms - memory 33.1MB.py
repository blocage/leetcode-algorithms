# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head)
            head = head.next
        
        k = sorted(l, key=lambda x: x.val)
        for i in range(len(k) - 1):
            k[i].next = k[i + 1]
        if k:
            k[-1].next = None
        else:
            return None
        return k[0]