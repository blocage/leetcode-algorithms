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
    ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
        vector<int> st;
        while (a){
            st.push_back(a -> val);
            a = a -> next;
        }
        while (b){
            st.push_back(b -> val);
            b = b -> next;
        }
        sort(st.begin(), st.end());
        if (st.empty()) return NULL;
        ListNode* res = new ListNode(st[0]);
        ListNode* prev = res;
        for (int i=1;i < st.size();i++){
            ListNode* temp = new ListNode(st[i]);
            prev -> next = temp;
            prev = temp;
        }
        return res;
    }
};