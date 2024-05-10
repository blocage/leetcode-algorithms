import sys
sys.set_int_max_str_digits(int(1e5))
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        r = ''
        while head:
            r += str(head.val)
            head = head.next
        
        r = str(int(r) * 2)
        head = ListNode(r[0])
        prev = head
        for i in range(1, len(r)):
            temp = ListNode(r[i])
            prev.next = temp
            prev = temp
        
        return head
