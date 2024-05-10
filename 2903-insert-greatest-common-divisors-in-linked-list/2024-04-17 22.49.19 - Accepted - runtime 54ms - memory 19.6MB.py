# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            next_tmp = curr.next
            curr.next = ListNode(math.gcd(curr.val, next_tmp.val))
            curr.next.next = next_tmp
            curr = next_tmp
        return head