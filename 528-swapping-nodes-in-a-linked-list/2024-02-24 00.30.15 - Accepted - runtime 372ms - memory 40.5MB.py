# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head)
            head = head.next
        k -= 1
        l[k].val, l[~k].val = l[~k].val, l[k].val

        return l[0]