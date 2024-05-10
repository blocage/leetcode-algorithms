# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum_bst(self, node, low, high):
        if node:
            if node.val >= low and node.val <= high:
                yield node.val
            yield from self.sum_bst(node.left, low, high)
            yield from self.sum_bst(node.right, low, high)
        return 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return sum(self.sum_bst(root, low, high))