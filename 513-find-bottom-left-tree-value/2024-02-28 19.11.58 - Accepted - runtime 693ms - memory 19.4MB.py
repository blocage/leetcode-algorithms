# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, depth = 1, left: bool = False):
        if node:
            yield depth, node.val
            yield from self.traverse(node.left, depth + 1, True)
            yield from self.traverse(node.right, depth + 1)

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = list(self.traverse(root))
        return max(d, key=lambda x: (x[0], -d.index(x)))[1]