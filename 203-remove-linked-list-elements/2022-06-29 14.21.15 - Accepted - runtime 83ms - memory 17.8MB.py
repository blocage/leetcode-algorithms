# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode()
        returned_head = prev
        while head:
            if head.val == val:
                head = head.next
                prev.next = None
                continue
            prev.next = head
            prev = head
            head = head.next
            
        return returned_head.next