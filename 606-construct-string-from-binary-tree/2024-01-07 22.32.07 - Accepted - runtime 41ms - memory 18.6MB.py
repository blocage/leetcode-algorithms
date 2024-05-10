# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node) -> str:
        s = str(node.val)
        if node.left or node.right:
            if node.left:
                s += '(' + self.traverse(node.left) + ')'
            else:
                s += '()'
            if node.right:
                s += '(' + self.traverse(node.right) + ')'
        return s

    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root)