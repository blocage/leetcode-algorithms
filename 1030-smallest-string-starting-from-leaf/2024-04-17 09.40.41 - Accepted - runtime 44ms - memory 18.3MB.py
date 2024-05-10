# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, r, s = ()):
        if not r or (not r.left and not r.right):
            if r:
                s += r.val,
            if len(s) > 1:
                yield s[::-1]
        else:
            s += r.val,
            if r.left:yield from self.dfs(r.left, s)
            if r.right:yield from self.dfs(r.right, s)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root.left and not root.right:
            return chr(97 + root.val)
        l = list(self.dfs(root))
        return ''.join(chr(97 + f)for f in min(l))