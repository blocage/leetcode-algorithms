# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def grandpa(node) -> int:
            l = []
            for i in (node.left, node.right):
                if i:
                    l.append(i)
            if not l: return 0
            res = 0
            for i in l:
                for j in (i.left, i.right):
                    if j:
                        res += j.val
            
            return res
        
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val % 2 == 0:
                res += grandpa(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res