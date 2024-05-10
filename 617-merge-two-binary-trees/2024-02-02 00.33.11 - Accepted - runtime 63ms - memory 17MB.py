# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, a, b):
        if a and b:
            k = TreeNode(a.val + b.val)
            k.left = self.merge(a.left, b.left)
            k.right = self.merge(a.right, b.right)
            return k
        return a or b
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        res = self.merge(root1, root2)
        return res