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
    ListNode* swapPairs(ListNode* head) {
        if (!head) return head;
        ListNode* f = head;
        ListNode* res = head;
        head = head -> next;
        int d = 1;
        while (head){
            if (d % 2) swap(f -> val, head -> val);
            f = head;
            head = head -> next;
            d++;
        }
        return res;
    }
};