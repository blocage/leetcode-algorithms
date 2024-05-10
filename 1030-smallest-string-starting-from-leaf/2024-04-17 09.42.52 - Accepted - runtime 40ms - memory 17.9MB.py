# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.results = []

        def solve(node, res):
            if node.left:
                solve(node.left, res + chr(97 + node.val))

            if node.right:
                solve(node.right, res + chr(97 + node.val))  

            if not node.left and not node.right:
                res += chr(97 + node.val) 
                self.results.append(res[::-1])        


        solve(root, '')
        return min(self.results)