# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            nodes = []
            while list1:
                nodes.append(list1)
                list1 = list1.next
            while list2:
                nodes.append(list2)
                list2 = list2.next
            nodes.sort(key=lambda x: x.val)
            for i in range(len(nodes) - 1):nodes[i].next = nodes[i + 1]

            return nodes[0]
        
        elif list1:return list1
        return list2