# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, res = ''):
        if not root: 
            yield int(res)
        else:
            res += str(root.val)
            if not root.left and not root.right:
                yield int(res)
            else:
                if root.left: yield from self.traverse(root.left, res)
                if root.right: yield from self.traverse(root.right, res)
    def sumNumbers(self, root: Optional[TreeNode], t = 0) -> int:
        return sum(self.traverse(root))