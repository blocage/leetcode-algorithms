# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, n, s='') -> str:
        s += str(n.val)
        if not n.left and not n.right:
            yield s
        
        else:
            if n.left:
                yield from self.traverse(n.left, s)
            
            if n.right:
                yield from self.traverse(n.right, s)


    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return sum(map(lambda x:int(x, 2), self.traverse(root)))