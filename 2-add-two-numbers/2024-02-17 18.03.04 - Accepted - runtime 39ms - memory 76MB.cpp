/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* prev = dummy;
        int remainder = 0, sum;
        while (l1 || l2 || remainder){
            sum = 0;
            if (l1){ sum = l1 -> val; l1 = l1 -> next; }
            if (l2){ sum += l2 -> val; l2 = l2 -> next; }
            sum += remainder;
            remainder = sum / 10;
            ListNode* tmp = new ListNode(sum % 10);
            prev -> next = tmp;
            prev = tmp;
        }
        return dummy -> next;
    }
};