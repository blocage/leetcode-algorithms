class Solution {
public:
    ListNode* removeNodes(ListNode* head) {
        if (head == NULL) return head;
        head -> next = removeNodes(head -> next);
        return head->next && head->next->val > head->val? head->next: head;
    }
};