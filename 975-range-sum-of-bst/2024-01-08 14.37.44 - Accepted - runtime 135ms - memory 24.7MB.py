# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        stack = [root]
        while stack:
            n = stack.pop()
            if low <= n.val <= high:
                s += n.val
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        return s
        