# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = deque([root])
        s = 0
        while level:
            s = 0
            for _ in range(len(level)):
                n = level.pop()
                s += n.val
                if n.left: level.appendleft(n.left)
                if n.right: level.appendleft(n.right)
        
        return s
