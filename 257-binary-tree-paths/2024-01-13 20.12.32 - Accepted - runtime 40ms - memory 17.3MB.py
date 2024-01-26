# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, l=''):
        l += str(node.val)
        if not (node.left or node.right):
            yield l
        else:
            l += '->'
            if node.left:
                yield from self.traverse(node.left, l)
            if node.right:
                yield from self.traverse(node.right, l)
            
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return list(self.traverse(root))