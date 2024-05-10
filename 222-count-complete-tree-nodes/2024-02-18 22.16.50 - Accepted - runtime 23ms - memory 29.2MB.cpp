/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int countNodes(TreeNode* root) {
        stack<TreeNode*> st;
        if (root) st.push(root);
        int res = 0;
        while (!st.empty()){
            TreeNode* n = st.top(); st.pop(); res++;
            if (n -> left) st.push(n -> left);
            if (n -> right) st.push(n -> right);
        }
        return res;
    }
};