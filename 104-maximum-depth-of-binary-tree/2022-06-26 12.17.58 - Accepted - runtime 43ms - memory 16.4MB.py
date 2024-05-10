# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deep(self, root: Optional[TreeNode], deep=0) -> int:
        if not root:
            return deep
        deep += 1
        return max(self.deep(root.left, deep), self.deep(root.right, deep))
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.deep(root)