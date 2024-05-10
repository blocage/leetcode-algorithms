# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def traverse(self, n):
        if not n: return 0, 0
        ls, lc = self.traverse(n.left)
        rs, rc = self.traverse(n.right)
        s, c = ls + rs + n.val, lc + rc + 1
        self.res += s // c == n.val
        return s, c

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res
        