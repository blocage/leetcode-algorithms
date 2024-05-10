# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node) -> bool:
        if not node:
            return False
        if not node.val and not node.left and not node.right:
            return False
        if node.val:
            return True
        return self.traverse(node.left) or self.traverse(node.right)

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r = root
        if not self.traverse(r):
            return None
        stack = [r]
        while stack:
            n = stack.pop()
            if n.left:
                if self.traverse(n.left):
                    stack.append(n.left)
                else:
                    n.left = None
            if n.right:
                if self.traverse(n.right):
                    stack.append(n.right)
                else:
                    n.right = None
        
        return r