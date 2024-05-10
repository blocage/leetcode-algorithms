# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, n1, n2) -> bool:
        if n1 and n2:
            return n1.val == n2.val and self.check(n1.left, n2.left) and self.check(n1.right, n2.right)
        else:
            return n1 is n2
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            n = stack.pop()
            if self.check(n, subRoot):
                return True
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

        return False