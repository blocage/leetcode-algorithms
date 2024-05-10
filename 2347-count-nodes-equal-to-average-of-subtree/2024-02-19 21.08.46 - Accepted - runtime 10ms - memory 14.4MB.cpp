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
    int res = 0;
    tuple<int, int> traverse(TreeNode* n){
        if (!n) return make_tuple(0, 0);
        int ls, lc, rs, rc;
        tie(ls, lc) = traverse(n -> left);
        tie(rs, rc) = traverse(n -> right);
        int s = ls + rs + n -> val, c = lc + rc + 1;
        if (s / c == n -> val) res++;
        return make_tuple(s, c);

    }
    int averageOfSubtree(TreeNode* root) {
        traverse(root);
        return res;
    }
};