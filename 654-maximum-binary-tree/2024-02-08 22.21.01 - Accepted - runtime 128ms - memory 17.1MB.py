# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nodes = []
        for i in nums:
            node = TreeNode(i)
            while nodes and nodes[-1].val < i:
                node.left = nodes.pop()

            if nodes:
                nodes[-1].right = node

            nodes.append(node)

        return nodes.pop(0)
        