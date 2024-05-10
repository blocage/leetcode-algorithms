class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head, int prev = -101) {
        if (head == NULL) return head;
        if (head->val == prev) return deleteDuplicates(head->next, prev);
        if (head->next && head->next->val == head->val) 
            return deleteDuplicates(head->next, head->val);
        head -> next = deleteDuplicates(head->next, head->val);
        return head;
    }
};