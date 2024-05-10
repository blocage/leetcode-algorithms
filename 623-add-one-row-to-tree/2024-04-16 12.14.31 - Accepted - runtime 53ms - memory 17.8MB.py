# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            r = TreeNode(val)
            r.left = root
            return r
        
        levels = deque([root])
        depth -= 2
        while depth > 0:
            depth -= 1
            for _ in range(len(levels)):
                n = levels.pop()
                if n.left:
                    levels.appendleft(n.left)
                if n.right:
                    levels.appendleft(n.right)
        
        while levels:
            n = levels.pop()
            left, right = TreeNode(val), TreeNode(val)
            left.left, right.right = n.left, n.right
            n.left, n.right = left, right
        
        return root
