# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], prev:int = -101) -> Optional[ListNode]:
        if head is None:
            return head
        
        if head.val == prev:
            return self.deleteDuplicates(head.next, prev)
        
        if head.next and head.next.val == head.val:
            return self.deleteDuplicates(head.next, head.val)
        
        head.next = self.deleteDuplicates(head.next, head.val)
        return head
            