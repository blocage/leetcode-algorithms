# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]
        while stack:
            node = stack.pop()
            if not node:continue
            if node.val == target.val:
                return node
            stack.append(node.left)
            stack.append(node.right)
        
        return -1