# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left, right = [], [root]
        res = 0
        while left or right:
            if left:
                n = left.pop()
                if not n.left and not n.right: res += n.val
                if n.left: left.append(n.left)
                if n.right: right.append(n.right)
            else:
                n = right.pop()
                if n.left: left.append(n.left)
                if n.right: right.append(n.right)
        
        return res