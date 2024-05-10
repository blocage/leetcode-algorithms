# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_head = prev = None
        new_head = head
        while head:
            if not new_head:
                new_head = head
            if prev and prev.val == head.val:
                if head.val == new_head.val:
                    new_head = None
            elif not head.next or (head.next and head.val != head.next.val):
                if prev_head:
                    prev_head.next = head
                prev_head = head
            
            else:
                if prev_head:
                    prev_head.next = None
            
            prev = head
            head = head.next

        return new_head
            