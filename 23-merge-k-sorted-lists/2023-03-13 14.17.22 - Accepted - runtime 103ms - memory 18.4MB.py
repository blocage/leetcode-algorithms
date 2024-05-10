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
                r += 1
                i = i.next
        
        dummy = curr = ListNode()
        for i in range(r):
            curr.next = ListNode(heapq.heappop(l))
            curr = curr.next
        
        return dummy.next