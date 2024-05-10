# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd, even = ListNode(), ListNode()
        a, b = odd, even
        node, ind = head, 1
        while node:
            if ind % 2:
                odd.next = node
                odd = node
            else:
                even.next = node
                even = node
            node = node.next
            ind += 1
        even.next = None
        odd.next = b.next
        return a.next
        
        