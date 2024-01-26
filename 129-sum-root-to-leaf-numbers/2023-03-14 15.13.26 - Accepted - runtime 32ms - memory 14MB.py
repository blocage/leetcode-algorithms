class Solution:
    def sum(self, node: Optional[TreeNode], s: int = 0) -> int:
        if not node: return 0
        s = s * 10 + node.val
        if not node.left and not node.right: return s
        return self.sum(node.left, s) + self.sum(node.right, s)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum(root)