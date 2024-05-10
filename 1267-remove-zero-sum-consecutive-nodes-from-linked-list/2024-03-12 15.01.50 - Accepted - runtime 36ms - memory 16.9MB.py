# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = 0
        dic = {0: dummy}
        while head:
            pre += head.val
            if pre in dic:
                tmp = dic[pre]
                start = tmp
                tmpsum = pre
                while tmp != head:
                    tmp = tmp.next
                    tmpsum += tmp.val
                    if tmp != head:
                        del dic[tmpsum]
                
                start.next = head.next
            else:
                dic[pre] = head

            head = head.next
        
        return dummy.next