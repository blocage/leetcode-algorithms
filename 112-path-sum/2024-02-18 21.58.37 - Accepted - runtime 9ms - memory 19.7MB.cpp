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
    bool hasPathSum(TreeNode* r, int t) {
        if (!r) return false;
        if (!(r -> left || r -> right) && t == r -> val) return true;
        t -= r -> val;
        return hasPathSum(r -> left, t) || hasPathSum(r -> right, t);
    }
};