# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []
        r = 0
        for i in lists:
            while i:
                heapq.heappush(l, i.val)
                i = i.next
                r += 1
        
        if not r:
            return None
        
        res = curr = ListNode(heapq.heappop(l))
        for i in range(r - 1):
            curr.next = ListNode(heapq.heappop(l))
            curr = curr.next

        return res