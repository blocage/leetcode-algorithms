# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def extract(self, node: Optional[TreeNode]):
        if not node.left and not node.right:
            yield node.val
        else:
            if node.left:
                yield from self.extract(node.left)
            if node.right:
                yield from self.extract(node.right)
            
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return list(self.extract(root1)) == list(self.extract(root2))
        