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
    vector<string> traverse(TreeNode* node, string l = "") {
        l += to_string(node->val);
        vector<string> paths;
        if (!(node->left || node->right)) {
            paths.push_back(l);
        } else {
            l += "->";
            if (node->left) {
                vector<string> leftPaths = traverse(node->left, l);
                paths.insert(paths.end(), leftPaths.begin(), leftPaths.end());
            }
            if (node->right) {
                vector<string> rightPaths = traverse(node->right, l);
                paths.insert(paths.end(), rightPaths.begin(), rightPaths.end());
            }
        }
        return paths;
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        return traverse(root);
    }
};