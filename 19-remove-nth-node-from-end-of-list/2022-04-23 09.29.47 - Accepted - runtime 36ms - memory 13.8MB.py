# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)   # Create a dummy node with next value set to the head pointer
        left = dummy 
        right = head
        
        for _ in range(n):             # Initiate right pointer to the nth index of the list
            right = right.next
        
        while right != None:       # Update each pointer to the next node until right reaches the end
            right = right.next
            left = left.next
        
        left.next = left.next.next  # Remove nth node from the right
        
        return dummy.next