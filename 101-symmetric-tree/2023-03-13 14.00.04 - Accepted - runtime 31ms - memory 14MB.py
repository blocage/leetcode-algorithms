# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_nodes(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.check_nodes(left.left, right.right) and self.check_nodes(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root is None or self.check_nodes(root.left, root.right)