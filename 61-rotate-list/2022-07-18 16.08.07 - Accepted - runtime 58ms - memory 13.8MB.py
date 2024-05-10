# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:return head
        last, L = head, 1
        while last.next:last = last.next; L += 1
        last.next = head
        
        for i in range(L - k % L):last = last.next
        final = last.next
        last.next = None
        
        return final
        