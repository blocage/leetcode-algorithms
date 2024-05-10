# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], val = 0) -> int:
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right:return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)