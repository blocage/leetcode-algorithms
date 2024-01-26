# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = b = 0
        t1, t2 = headA, headB
        while t1: a += 1; t1 = t1.next
        while t2: b += 1; t2 = t2.next
        while a > b:a -= 1; headA = headA.next
        while a < b:b -= 1; headB = headB.next
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next