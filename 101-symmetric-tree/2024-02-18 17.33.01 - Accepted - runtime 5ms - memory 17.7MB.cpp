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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        stack<TreeNode*> left, right;
        left.push(root -> left); right.push(root -> right);
        while (!left.empty() && !right.empty()){
            TreeNode* l = left.top(); left.pop();
            TreeNode* r = right.top(); right.pop();
            if (!l || !r){
                if (l != r) return false;
            }
            else { 
                if (l -> val != r -> val) return false;
                left.push(l -> left); left.push(l -> right);
                right.push(r -> right); right.push(r -> left);
            }
        }
        return left.empty() && right.empty();
    }
};