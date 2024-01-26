class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        maxes = []
        level = [root]
        while any(level):
            maxes.append(max(n.val for n in level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]

        return maxes