class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res, l = [], [root]
        while root and l:
            res.append([f.val for f in l])
            pairs = [(f.left, f.right) for f in l]
            l = [node for pair in pairs for node in pair if node]

        return res