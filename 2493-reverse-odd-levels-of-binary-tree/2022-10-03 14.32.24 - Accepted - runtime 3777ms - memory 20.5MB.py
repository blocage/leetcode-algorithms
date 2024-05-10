class Solution:
    def reverse(self, root: TreeNode, level: int) -> None:
        if root.left:
            if level % 2:
                if level in self.levels:
                    self.levels[level] += [root.left, root.right]
                else:
                    self.levels[level] = [root.left, root.right]
            self.reverse(root.left, level + 1)
            self.reverse(root.right, level + 1)
        
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.levels = {}
        if root:
            self.reverse(root, 1)
        for _, nodes in self.levels.items():
            l = len(nodes) // 2
            for a,b in zip(nodes[:l], nodes[l:][::-1]):
                a.val, b.val = b.val, a.val
        return root