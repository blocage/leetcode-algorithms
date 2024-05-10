class Solution:
    def traverse(self, node: Optional[TreeNode], level: int, d: dict[int, list[int]]) -> None:
        if node:
            d[level] = d.get(level, []) + [node.val]
            self.traverse(node.left, level + 1, d)
            self.traverse(node.right, level + 1, d)

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        d = {}
        self.traverse(root, 0, d)
        return d.values()
        