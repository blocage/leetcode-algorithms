# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def extract(self, node:Optional[TreeNode]) -> list[int]:
        r, R = [], [node]
        while R:
            n = R.pop()
            if not n.left and not n.right:
                r.append(n.val)
                continue
            if n.left:
                R.append(n.left)
            if n.right:
                R.append(n.right)
        return r

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.extract(root1) == self.extract(root2)