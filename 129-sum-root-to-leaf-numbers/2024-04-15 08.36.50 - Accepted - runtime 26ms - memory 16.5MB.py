# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], t = 0) -> int:
        if not root: return 0
        t = t * 10 + root.val
        if not root.left and not root.right: return t
        return self.sumNumbers(root.right, t) + self.sumNumbers(root.left, t)