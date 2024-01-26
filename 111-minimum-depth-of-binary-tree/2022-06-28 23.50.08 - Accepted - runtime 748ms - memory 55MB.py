# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root: Optional[TreeNode], depth: int) -> int:
        if not root.left and not root.right:
            return depth
        if root.left and root.right:
            return min(self.bfs(root.left, depth+1), self.bfs(root.right, depth+1))
        if root.left:
            return self.bfs(root.left, depth+1)
        return self.bfs(root.right, depth+1)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.bfs(root, 1)