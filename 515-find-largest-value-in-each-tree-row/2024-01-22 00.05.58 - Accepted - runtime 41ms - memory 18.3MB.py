# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, level, l={}):
        if level in l:
            l[level].append(root.val)
        else:
            l[level] = [root.val]
        if root.left:
            self.traverse(root.left, level + 1, l)
        if root.right:
            self.traverse(root.right, level + 1, l)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = {}
        self.traverse(root, 1, l)
        return [max(f) for f in l.values()]