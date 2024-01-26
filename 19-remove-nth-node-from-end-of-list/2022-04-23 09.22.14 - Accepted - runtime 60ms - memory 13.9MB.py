# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [head]
        
        while head.next:
            nodes.append(head.next)
            head = head.next

        res = nodes.pop(-n)
        if nodes:nodes[-1].next = None
        if len(nodes) - 1:
            for i in range(len(nodes) - 1):nodes[i].next = nodes[i + 1]
        else:
            pass
            
        return nodes[0] if nodes else res.next