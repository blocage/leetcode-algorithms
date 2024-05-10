# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        r = []
        s = [root]
        while s:
            n = s.pop()
            r.append(n)
            for i in (n.left, n.right):
                if i:s.append(i)
        r.sort(key=lambda x: x.val)
        for i in range(len(r) - 1):
            r[i].left = None
            r[i].right = r[i + 1]
        r[-1].left = r[-1].right = None

        return r[0]