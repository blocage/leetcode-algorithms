# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        k = set()
        s = [root]
        while s:
            n = s.pop()
            k.add(n.val)
            for c in (n.left, n.right):
                if c:
                    s.append(c)
            
        return len(k) < 2