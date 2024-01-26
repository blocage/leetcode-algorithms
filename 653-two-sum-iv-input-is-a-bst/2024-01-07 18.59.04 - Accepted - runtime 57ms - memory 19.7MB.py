# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        stack = [root]
        while stack:
            n = stack.pop()
            if n.val in s:
                return True
            s.add(k - n.val)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)

        return False