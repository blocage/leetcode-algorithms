# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.levels = defaultdict(list)
    
    def traverse(self, node, d: int = 0):
        self.levels[d].append(node.val)
        if node.left:
            self.traverse(node.left, d + 1)
        if node.right:
            self.traverse(node.right, d + 1)

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        for a,b in self.levels.items():
            if a % 2:
                f = b[0]
                if f % 2: return False
                for i in b[1:]:
                    if i % 2 or f <= i: return False
                    f = i
            else:
                f = b[0]
                if f % 2 == 0: return False
                for i in b[1:]:
                    if i % 2 == 0 or f >= i: return False
                    f = i
        
        return True