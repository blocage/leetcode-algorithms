# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> Optional[TreeNode]:
        if a and b:
            res = TreeNode(a.val + b.val)
            res.left = self.mergeTrees(a.left, b.left)
            res.right = self.mergeTrees(a.right, b.right)
            return res
        return a or b