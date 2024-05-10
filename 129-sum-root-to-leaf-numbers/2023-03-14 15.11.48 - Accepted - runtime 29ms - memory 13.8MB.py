class Solution:
    def sum(self, node: Optional[TreeNode], s: int = 0) -> int:
        if not node: return 0
        if not node.left and not node.right: return s * 10 + node.val
        return self.sum(node.left, s * 10 + node.val) + self.sum(node.right, s * 10 + node.val)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sum(root)