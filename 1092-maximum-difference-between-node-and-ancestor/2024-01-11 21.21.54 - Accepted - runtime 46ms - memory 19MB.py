# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root, m=100000, M=0) -> int:
        return max(self.maxAncestorDiff(root.left, min(m, root.val), max(M, root.val)), \
            self.maxAncestorDiff(root.right, min(m, root.val), max(M, root.val))) \
            if root else M - m