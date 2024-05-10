# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left, right = [root.left], [root.right]
        while left and right:
            l, r = left.pop(), right.pop()
            if l is None or r is None:
                if l != r:
                    return False
            else:
                if l.val != r.val:
                    return False
            
                left.extend([l.left, l.right])
                right.extend([r.right, r.left])
        
        return left == right