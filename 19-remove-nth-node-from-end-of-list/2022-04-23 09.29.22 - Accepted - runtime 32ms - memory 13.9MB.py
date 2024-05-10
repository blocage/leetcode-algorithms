# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0
        
        itr = head
        
        while itr:
            itr = itr.next
            k+=1  

        pos = k-n
        j=0
        itr = head
        prev = head
        
        if pos == 0:
            head = head.next
            return head
        
        while itr:
            if j == pos-1:
                prev = itr
            itr = itr.next
            j+=1
            
        prev.next = prev.next.next
        
        return head