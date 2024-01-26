class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        res, l = [], [root]
        while l:
            res.append([f.val for f in l])
            pairs = [(f.left, f.right) for f in l]
            l = [node for pair in pairs for node in pair if node]

        return res