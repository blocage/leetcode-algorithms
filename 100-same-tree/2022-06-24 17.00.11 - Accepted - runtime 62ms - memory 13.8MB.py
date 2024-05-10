# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1:
            return not node2
        if not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.check(node1.left, node2.left) and self.check(node1.right, node2.right)
        
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)