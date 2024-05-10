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
    bool isUnivalTree(TreeNode* root) {
        stack<TreeNode*> st; st.push(root);
        int& v = root -> val;
        while (!st.empty()){
            TreeNode* n = st.top(); st.pop();
            if (n -> val != v) return false;
            if (n -> left) st.push(n -> left);
            if (n -> right) st.push(n -> right);
        }
        return true;
    }
};