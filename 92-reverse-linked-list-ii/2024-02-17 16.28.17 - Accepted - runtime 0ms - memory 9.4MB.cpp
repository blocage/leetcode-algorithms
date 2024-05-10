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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head == NULL || left == right) return head;
        ListNode* dummy = new ListNode();
        ListNode* p = dummy;
        dummy -> next = head;
        for (int i=0; i < left - 1;i++) p = p -> next;
        ListNode* tail = p -> next;
        for (int i=0; i < right - left; i++){
            ListNode* tmp = p -> next;
            p -> next = tail -> next;
            tail -> next = tail -> next -> next;
            p -> next -> next = tmp;
        }
        return dummy -> next;
    }

};