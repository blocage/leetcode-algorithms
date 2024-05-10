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
        string a, b, res;
        while (l1){ a += to_string(l1 -> val); l1 = l1 -> next; }
        while (l2){ b += to_string(l2 -> val); l2 = l2 -> next; }
        ListNode* dummy = new ListNode();
        ListNode* prev = dummy;
        bool remainder = false;
        for (int i = 0; i < max(a.size(), b.size()); i++){
            int val = (i < a.size()? a[i]: '0') + (i < b.size()? b[i]: '0') - 96;
            if (remainder) { val++; remainder=false; };
            if (val > 9) remainder = true;
            ListNode* tmp = new ListNode(val % 10);
            prev -> next = tmp;
            prev = tmp;
        }
        if (remainder) prev -> next = new ListNode(1);
        return dummy -> next;
    }
};