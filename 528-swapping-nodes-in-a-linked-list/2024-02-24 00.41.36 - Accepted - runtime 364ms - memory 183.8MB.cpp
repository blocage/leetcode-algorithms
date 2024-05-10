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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode *a = nullptr, *b = nullptr;
        for (ListNode* p = head; p != NULL; p = p -> next){
            b = b == nullptr? nullptr: b->next;
            if (--k == 0){
                a = p;
                b = head;
            }
        }
        swap(a -> val, b -> val);
        return head;
    }
};