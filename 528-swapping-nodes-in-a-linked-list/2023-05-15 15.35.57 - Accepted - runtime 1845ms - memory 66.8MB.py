# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        k -= 1
        l[k], l[~k] = l[~k], l[k]
        dummy = curr = ListNode()
        for i in l:
            curr.next = ListNode(i)
            curr = curr.next
        
        return dummy.next